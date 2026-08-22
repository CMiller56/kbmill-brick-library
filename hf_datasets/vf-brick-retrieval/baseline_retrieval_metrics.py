#!/usr/bin/env python3
"""
Tiny baseline retrieval metrics for CMiller/kbmill-brick-retrieval.

Re-embeds HF corpus + queries with a named SentenceTransformer model,
ranks by cosine similarity, scores against qrels/test.tsv.

Example:
  python3 baseline_retrieval_metrics.py
  python3 baseline_retrieval_metrics.py --config ardupilot_plane --model nomic-ai/nomic-embed-text-v1.5

Deps: pip install sentence-transformers scikit-learn numpy datasets
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
from typing import Any

import numpy as np

HERE = Path(__file__).resolve().parent
DEFAULT_MODEL = "nomic-ai/nomic-embed-text-v1.5"
CONFIGS = ("ardupilot_plane", "ardupilot_plane_params", "nasa_skylab")


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def load_qrels(path: Path) -> dict[str, set[str]]:
    """query_id -> set of relevant corpus ids."""
    out: dict[str, set[str]] = {}
    with path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            q = row.get("query-id") or row.get("query_id")
            c = row.get("corpus-id") or row.get("corpus_id")
            if not q or not c:
                keys = list(row.keys())
                if len(keys) >= 2:
                    q = q or row[keys[0]]
                    c = c or row[keys[1]]
            if not q or not c:
                continue
            out.setdefault(q, set()).add(c)
    return out


def dcg_at_k(relevances: list[float], k: int) -> float:
    s = 0.0
    for i, rel in enumerate(relevances[:k]):
        s += (2**rel - 1) / math.log2(i + 2)
    return s


def ndcg_at_k(ranked_ids: list[str], relevant: set[str], k: int) -> float:
    rels = [1.0 if doc in relevant else 0.0 for doc in ranked_ids[:k]]
    dcg = dcg_at_k(rels, k)
    ideal = dcg_at_k(sorted(rels, reverse=True) + [0.0] * k, k)
    # better: ideal from |relevant|
    n_rel = min(k, len(relevant))
    ideal = dcg_at_k([1.0] * n_rel, k)
    if ideal <= 0:
        return 0.0
    return dcg / ideal


def recall_at_k(ranked_ids: list[str], relevant: set[str], k: int) -> float:
    if not relevant:
        return 0.0
    got = set(ranked_ids[:k]) & relevant
    return len(got) / len(relevant)


def hit_rate_at_k(ranked_ids: list[str], relevant: set[str], k: int) -> float:
    """1 if any relevant in top-k."""
    if not relevant:
        return 0.0
    return 1.0 if set(ranked_ids[:k]) & relevant else 0.0


def encode_texts(model, texts: list[str], batch_size: int = 64) -> np.ndarray:
    # nomic: document vs query prefixes optional in v1.5; trust_remote_code
    emb = model.encode(
        texts,
        batch_size=batch_size,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )
    return np.asarray(emb, dtype=np.float32)


def evaluate_config(
    config: str,
    model_name: str,
    top_k: int,
    data_root: Path,
    batch_size: int,
) -> dict[str, Any]:
    from sentence_transformers import SentenceTransformer

    cfg_dir = data_root / config
    corpus = load_jsonl(cfg_dir / "corpus.jsonl")
    queries = load_jsonl(cfg_dir / "queries.jsonl")
    qrels = load_qrels(cfg_dir / "qrels" / "test.tsv")

    corpus_ids = [c["_id"] for c in corpus]
    corpus_texts = [c["text"] for c in corpus]
    query_ids = [q["_id"] for q in queries]
    query_texts = [q["text"] for q in queries]

    print(f"\n=== {config} | model={model_name} | corpus={len(corpus)} queries={len(queries)} ===")
    model = SentenceTransformer(model_name, trust_remote_code=True)

    print("Encoding corpus…")
    corp_emb = encode_texts(model, corpus_texts, batch_size=batch_size)
    print("Encoding queries…")
    q_emb = encode_texts(model, query_texts, batch_size=batch_size)

    # cosine via normalized embeddings = dot product
    scores = q_emb @ corp_emb.T  # (n_q, n_c)

    recalls = []
    ndcgs = []
    hits = []
    per_query = []

    for i, qid in enumerate(query_ids):
        rel = qrels.get(qid, set())
        order = np.argsort(-scores[i])[:top_k]
        ranked = [corpus_ids[j] for j in order]
        ranked_scores = [float(scores[i, j]) for j in order]
        r = recall_at_k(ranked, rel, top_k)
        n = ndcg_at_k(ranked, rel, top_k)
        h = hit_rate_at_k(ranked, rel, top_k)
        recalls.append(r)
        ndcgs.append(n)
        hits.append(h)
        per_query.append(
            {
                "query_id": qid,
                "text": query_texts[i],
                "recall_at_k": r,
                "ndcg_at_k": n,
                "hit_at_k": h,
                "top_ids": ranked,
                "top_scores": ranked_scores,
                "qrel_ids": sorted(rel),
            }
        )

    summary = {
        "config": config,
        "model": model_name,
        "top_k": top_k,
        "n_queries": len(queries),
        "n_corpus": len(corpus),
        "recall_at_k_mean": float(np.mean(recalls)) if recalls else None,
        "ndcg_at_k_mean": float(np.mean(ndcgs)) if ndcgs else None,
        "hit_at_k_mean": float(np.mean(hits)) if hits else None,
        "qrels_note": (
            "qrels = published cosine top-3 from original brick embeddings "
            "(binary relevance). Baseline re-embeds HF corpus/queries with the named model."
        ),
        "per_query": per_query,
    }
    print(
        f"  Recall@{top_k}={summary['recall_at_k_mean']:.4f}  "
        f"nDCG@{top_k}={summary['ndcg_at_k_mean']:.4f}  "
        f"Hit@{top_k}={summary['hit_at_k_mean']:.4f}"
    )
    return summary


def main() -> int:
    p = argparse.ArgumentParser(description="VF brick retrieval baseline metrics")
    p.add_argument(
        "--config",
        choices=[*CONFIGS, "all"],
        default="all",
        help="dataset config (default: all)",
    )
    p.add_argument("--model", default=DEFAULT_MODEL, help="SentenceTransformer model id")
    p.add_argument("--top-k", type=int, default=3)
    p.add_argument(
        "--data-root",
        type=Path,
        default=HERE,
        help="folder containing ardupilot_plane/ and nasa_skylab/",
    )
    p.add_argument("--batch-size", type=int, default=64)
    p.add_argument(
        "--out",
        type=Path,
        default=HERE / "baseline_results.json",
        help="write full JSON results here",
    )
    args = p.parse_args()

    configs = list(CONFIGS) if args.config == "all" else [args.config]
    results = []
    for cfg in configs:
        results.append(
            evaluate_config(
                cfg,
                args.model,
                args.top_k,
                args.data_root,
                args.batch_size,
            )
        )

    payload = {
        "model": args.model,
        "top_k": args.top_k,
        "results": [
            {k: v for k, v in r.items() if k != "per_query"} for r in results
        ],
        "results_with_per_query": results,
    }
    args.out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"\nWrote {args.out}")

    # Markdown table for card paste
    print("\n### Baseline table (markdown)\n")
    print("| Config | Model | k | Recall@k | nDCG@k | Hit@k |")
    print("|--------|--------|--:|---------:|-------:|------:|")
    for r in results:
        print(
            f"| `{r['config']}` | `{r['model']}` | {r['top_k']} | "
            f"{r['recall_at_k_mean']:.3f} | {r['ndcg_at_k_mean']:.3f} | "
            f"{r['hit_at_k_mean']:.3f} |"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
