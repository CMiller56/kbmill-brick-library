#!/usr/bin/env python3
"""Minimal load / cosine re-rank sketch for CMiller/kbmill-brick-retrieval."""

from __future__ import annotations

import csv
from pathlib import Path

# Optional heavy deps — install if evaluating:
#   pip install datasets sentence-transformers scikit-learn numpy


def load_qrels_tsv(path: str | Path) -> dict[str, set[str]]:
    """query_id -> set of relevant corpus ids."""
    path = Path(path)
    out: dict[str, set[str]] = {}
    with path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        # header: query-id corpus-id score
        for row in reader:
            # support both naming styles
            q = row.get("query-id") or row.get("query_id")
            c = row.get("corpus-id") or row.get("corpus_id")
            if not q or not c:
                # DictReader may use first line keys as-is
                keys = list(row.keys())
                if len(keys) >= 2:
                    q = q or row[keys[0]]
                    c = c or row[keys[1]]
            if not q or not c:
                continue
            out.setdefault(q, set()).add(c)
    return out


def load_from_hub(config: str = "ardupilot_plane"):
    from datasets import load_dataset

    corpus = load_dataset("CMiller/kbmill-brick-retrieval", config, split="corpus")
    queries = load_dataset("CMiller/kbmill-brick-retrieval", config, split="queries")
    return corpus, queries


def evaluate_embeddings(
    model_name: str = "nomic-ai/nomic-embed-text-v1.5",
    config: str = "ardupilot_plane",
    top_k: int = 3,
    qrels_path: str | None = None,
):
    """Encode corpus+queries; return top-k hits. Optionally compute Recall@k vs qrels."""
    import numpy as np
    from sentence_transformers import SentenceTransformer
    from sklearn.metrics.pairwise import cosine_similarity

    corpus, queries = load_from_hub(config)
    model = SentenceTransformer(model_name, trust_remote_code=True)

    corpus_texts = [c["text"] for c in corpus]
    corpus_ids = [c["_id"] for c in corpus]
    corp_emb = model.encode(
        corpus_texts, normalize_embeddings=True, show_progress_bar=True
    )

    results: dict[str, dict[str, float]] = {}
    for q in queries:
        q_emb = model.encode([q["text"]], normalize_embeddings=True)
        scores = cosine_similarity(q_emb, corp_emb)[0]
        top_idx = np.argsort(scores)[::-1][:top_k]
        results[q["_id"]] = {corpus_ids[i]: float(scores[i]) for i in top_idx}

    metrics = None
    if qrels_path:
        qrels = load_qrels_tsv(qrels_path)
        recalls = []
        for qid, hits in results.items():
            rel = qrels.get(qid, set())
            if not rel:
                continue
            got = set(hits.keys())
            recalls.append(len(got & rel) / len(rel))
        metrics = {
            "recall_at_k_mean": float(sum(recalls) / len(recalls)) if recalls else None,
            "n_queries_scored": len(recalls),
            "k": top_k,
        }
    return results, metrics


if __name__ == "__main__":
    print("Loader helper for CMiller/kbmill-brick-retrieval")
    print("Example:")
    print('  from load_vf_brick_retrieval import load_from_hub')
    print('  corpus, queries = load_from_hub("ardupilot_plane")')
