#!/usr/bin/env python3
"""
Build Hugging Face BEIR-style retrieval dataset from VF portable bricks + published evals.

Outputs under hf_datasets/vf-brick-retrieval/:
  ardupilot_plane/{corpus.jsonl,queries.jsonl,qrels/test.tsv,published_hits.json}
  nasa_skylab/{...}

Stdlib + zipfile only for the build.
"""

from __future__ import annotations

import json
import re
import shutil
import zipfile
from pathlib import Path
from typing import Any, Iterable

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "hf_datasets" / "vf-brick-retrieval"

BRICKS = {
    "ardupilot_plane": {
        "zip": REPO / "bricks" / "ArduPilot_Plane" / "ArduPilot_Plane_portable.zip",
        "eval": REPO / "demos" / "ardupilot_plane_eval.json",
        "demo_md": "RETRIEVAL_DEMO_ArduPilot_Plane.md",
        "brick_name": "ArduPilot_Plane",
        "brick_url": "https://github.com/CMiller56/vf-brick-library/tree/main/bricks/ArduPilot_Plane",
    },
    "ardupilot_plane_params": {
        "zip": REPO
        / "bricks"
        / "ArduPilot_Plane_Params"
        / "ArduPilot_Plane_Params_portable.zip",
        "eval": REPO / "demos" / "ardupilot_plane_params_eval.json",
        "demo_md": "RETRIEVAL_DEMO_ArduPilot_Plane_Params.md",
        "brick_name": "ArduPilot_Plane_Params",
        "brick_url": "https://github.com/CMiller56/vf-brick-library/tree/main/bricks/ArduPilot_Plane_Params",
    },
    "nasa_skylab": {
        "zip": REPO
        / "bricks"
        / "NASA_Skylab_History_Living_Working_Space"
        / "NASA_Skylab_History_Living_Working_Space_portable.zip",
        "eval": REPO / "demos" / "nasa_skylab_history_eval.json",
        "demo_md": "RETRIEVAL_DEMO_NASA_Skylab_History.md",
        "brick_name": "NASA_Skylab_History_Living_Working_Space",
        "brick_url": "https://github.com/CMiller56/vf-brick-library/tree/main/bricks/NASA_Skylab_History_Living_Working_Space",
    },
}


def is_eligible(chunk: dict) -> bool:
    if not isinstance(chunk, dict):
        return False
    if chunk.get("muted") or chunk.get("exclude_from_rag"):
        return False
    text = (chunk.get("text") or "").strip()
    return bool(text)


def normalize_chunk_id(cid: Any) -> str:
    s = str(cid or "").strip()
    return s


def chunk_to_corpus_row(chunk: dict) -> dict[str, Any]:
    cid = normalize_chunk_id(chunk.get("chunk_id") or chunk.get("id"))
    heading = chunk.get("section_heading") or chunk.get("heading") or ""
    if heading is None:
        heading = ""
    page = chunk.get("page_number")
    if page is None:
        page = chunk.get("page")
    source = chunk.get("source_document") or chunk.get("source") or ""
    return {
        "_id": cid,
        "title": str(heading) if heading else "",
        "text": str(chunk.get("text") or ""),
        "source": str(source),
        "heading": str(heading) if heading else "",
        "page": page,
        "muted": bool(chunk.get("muted") or False),
        "token_count": chunk.get("token_count"),
        "document_type": chunk.get("document_type"),
    }


def load_eligible_chunks_from_zip(zpath: Path) -> list[dict]:
    with zipfile.ZipFile(zpath) as zf:
        names = set(zf.namelist())
        chunks: list[dict] = []
        if "kb.json" in names:
            kb = json.loads(zf.read("kb.json").decode("utf-8"))
            chunks = list(kb.get("chunks") or [])
        elif "chunks.jsonl" in names:
            with zf.open("chunks.jsonl") as f:
                for line in f:
                    line = line.decode("utf-8").strip()
                    if line:
                        chunks.append(json.loads(line))
        else:
            raise FileNotFoundError(f"No kb.json or chunks.jsonl in {zpath}")
    return [c for c in chunks if is_eligible(c)]


def load_eval(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def query_id(i: int) -> str:
    return f"q{i:03d}"


def build_subset(config: str, meta: dict) -> dict[str, Any]:
    zpath = Path(meta["zip"])
    epath = Path(meta["eval"])
    if not zpath.is_file():
        raise FileNotFoundError(zpath)
    if not epath.is_file():
        raise FileNotFoundError(epath)

    eligible = load_eligible_chunks_from_zip(zpath)
    by_id = {normalize_chunk_id(c.get("chunk_id")): c for c in eligible}
    eval_doc = load_eval(epath)
    results = eval_doc.get("results") or []

    out_dir = OUT / config
    qrels_dir = out_dir / "qrels"
    if out_dir.exists():
        shutil.rmtree(out_dir)
    qrels_dir.mkdir(parents=True, exist_ok=True)

    # corpus: all eligible chunks (self-contained eval)
    corpus_rows = [chunk_to_corpus_row(c) for c in eligible]
    # ensure qrel hit chunks exist in corpus (if a hit was muted, still include it with note)
    missing_hits: list[str] = []
    for item in results:
        for hit in item.get("hits") or []:
            cid = normalize_chunk_id(hit.get("chunk_id"))
            if cid and cid not in by_id:
                missing_hits.append(cid)

    # If published hits reference a chunk not in eligible set, pull raw from zip once
    if missing_hits:
        with zipfile.ZipFile(zpath) as zf:
            kb = json.loads(zf.read("kb.json").decode("utf-8"))
            all_chunks = {normalize_chunk_id(c.get("chunk_id")): c for c in (kb.get("chunks") or [])}
        for cid in sorted(set(missing_hits)):
            raw = all_chunks.get(cid)
            if raw:
                row = chunk_to_corpus_row(raw)
                row["muted"] = True
                row["note"] = "included because published hit; may be muted/excluded in brick RAG default"
                corpus_rows.append(row)
                by_id[cid] = raw

    with (out_dir / "corpus.jsonl").open("w", encoding="utf-8") as f:
        for row in corpus_rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    queries: list[dict] = []
    qrel_lines = ["query-id\tcorpus-id\tscore"]
    for i, item in enumerate(results, start=1):
        qid = query_id(i)
        qtext = str(item.get("query") or "").strip()
        queries.append({"_id": qid, "text": qtext})
        seen: set[str] = set()
        for hit in item.get("hits") or []:
            cid = normalize_chunk_id(hit.get("chunk_id"))
            if not cid or cid in seen:
                continue
            seen.add(cid)
            # binary relevance for published top-k
            qrel_lines.append(f"{qid}\t{cid}\t1")

    with (out_dir / "queries.jsonl").open("w", encoding="utf-8") as f:
        for row in queries:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    (qrels_dir / "test.tsv").write_text("\n".join(qrel_lines) + "\n", encoding="utf-8")

    # published hits transparency
    published = {
        "brick": eval_doc.get("brick") or meta["brick_name"],
        "config": config,
        "generated": eval_doc.get("generated"),
        "method": eval_doc.get("method"),
        "min_score_note": eval_doc.get("min_score_note"),
        "eligible_count_in_eval": eval_doc.get("eligible_count"),
        "chunk_count_in_eval": eval_doc.get("chunk_count"),
        "top_k": eval_doc.get("top_k") or 3,
        "demo_md": meta["demo_md"],
        "brick_library_url": meta["brick_url"],
        "results": results,
    }
    (out_dir / "published_hits.json").write_text(
        json.dumps(published, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    stats = {
        "config": config,
        "brick": meta["brick_name"],
        "corpus_docs": len(corpus_rows),
        "queries": len(queries),
        "qrel_rows": len(qrel_lines) - 1,
        "missing_hits_readded": len(set(missing_hits)),
    }
    (out_dir / "STATS.json").write_text(json.dumps(stats, indent=2) + "\n", encoding="utf-8")
    return stats


def write_dataset_card(stats: list[dict]) -> None:
    stats_by = {s["config"]: s for s in stats}
    ap = stats_by.get("ardupilot_plane", {})
    sk = stats_by.get("nasa_skylab", {})
    card = f'''---
license: other
license_name: composite-upstream-and-brick-packaging
license_link: https://github.com/CMiller56/vf-brick-library
task_categories:
- text-retrieval
- question-answering
language:
- en
tags:
- rag
- retrieval
- knowledge-base
- technical-documentation
- residual-honest
- vectorforge
- ardupilot
- uav
- nasa
- skylab
- ocr
- local-llm
- air-gapped
- beir
- mteb
- llm-native
- knowledge-brick
- production-rag
pretty_name: VectorForge Brick Retrieval Demos
size_categories:
- n<1K
configs:
- config_name: ardupilot_plane
  data_files:
  - split: corpus
    path: ardupilot_plane/corpus.jsonl
  - split: queries
    path: ardupilot_plane/queries.jsonl
- config_name: nasa_skylab
  data_files:
  - split: corpus
    path: nasa_skylab/corpus.jsonl
  - split: queries
    path: nasa_skylab/queries.jsonl
---

# VectorForge Brick Retrieval Demos

Portable, **residual-honest** knowledge bricks turned into retrieval evaluation sets.

These are **not** unbounded wiki dumps or synthetic QA. They come from real [VectorForge Pro](https://x.com/VectorForgePro) manufacturing: bounded packages with muted residual junk filtered where applicable, craft notes, and **published, re-runnable cosine retrieval evidence**.

| Config | Queries | Corpus docs (eligible) | Source brick |
|--------|--------:|-----------------------:|--------------|
| `ardupilot_plane` | {ap.get("queries", 20)} | {ap.get("corpus_docs", "?")} | [ArduPilot_Plane](https://github.com/CMiller56/vf-brick-library/tree/main/bricks/ArduPilot_Plane) |
| `nasa_skylab` | {sk.get("queries", 15)} | {sk.get("corpus_docs", "?")} | [NASA_Skylab_History_Living_Working_Space](https://github.com/CMiller56/vf-brick-library/tree/main/bricks/NASA_Skylab_History_Living_Working_Space) |

## Design intent (the differentiator)

Most public retrieval corpora were built for **traditional IR** or as **general training fuel**. They were never optimized as the **final working surface for an LLM**.

VectorForge bricks invert that: the package is shaped so the **model can use the knowledge cleanly** — bounded scope, residual honesty (muted junk stays off the path), stable chunk identity, clear provenance, and craft notes that tell the system what the brick is and is not for. When the consumer is the LLM itself, those choices compound.

That is why bricks are designed so models **spend less capacity fighting noise** — retrieval quality and downstream answer fidelity both have a cleaner path. The published ArduPilot and Skylab demos already show the **retrieval side** of that claim in a re-runnable form (cosine top-3; not chat transcripts or invented answers).

**Framing for this dataset:**

- These are **not** “just another technical corpus.”
- They are **LLM-native knowledge units** — manufactured so the **model is the primary user**.
- **Residual honesty + bounded packaging** is the practical expression of that design goal.

This is the story that should land with people who care about **production RAG quality** (and the LocalLLaMA / air-gapped crowd) rather than pure leaderboard optics: *here is what a knowledge package looks like when it was built for the model that has to live with it.*

## Why this exists

Most RAG failures are **data-preparation** failures. These demos let you measure retrieval quality on:

- **Technical operations documentation** (ArduPilot Plane ops facet)
- **Hostile OCR / paper-capture** historical technical text (NASA Skylab history)

Both packages already publish top-3 cosine results with chunk IDs, headings, sources, and excerpts so you can verify without trusting marketing claims.

Full write-ups:

- [RETRIEVAL_DEMO_ArduPilot_Plane.md](https://github.com/CMiller56/vf-brick-library/blob/main/RETRIEVAL_DEMO_ArduPilot_Plane.md)
- [RETRIEVAL_DEMO_NASA_Skylab_History.md](https://github.com/CMiller56/vf-brick-library/blob/main/RETRIEVAL_DEMO_NASA_Skylab_History.md)

Full portable ZIPs (Markdown + chunks + embeddings + cards) live in the [vf-brick-library](https://github.com/CMiller56/vf-brick-library).

## Dataset layout (BEIR-compatible)

```text
ardupilot_plane/
  corpus.jsonl          # eligible chunks (_id, text, source, heading, page, …)
  queries.jsonl         # _id, text
  qrels/test.tsv        # query-id  corpus-id  score (tab)
  published_hits.json   # original cosine top-3 evidence (scores + excerpts)
nasa_skylab/
  … same layout
```

**qrels:** published top-3 hits are treated as relevant (`score=1`). Expand later with graded judgments if needed.

## How to load

```python
from datasets import load_dataset

corpus = load_dataset("CMiller/vf-brick-retrieval", "ardupilot_plane", split="corpus")
queries = load_dataset("CMiller/vf-brick-retrieval", "ardupilot_plane", split="queries")

# qrels are TSV (not a datasets split by default) — parse locally:
# ardupilot_plane/qrels/test.tsv
```

From a local checkout of this folder:

```python
from datasets import load_dataset
corpus = load_dataset("json", data_files="ardupilot_plane/corpus.jsonl", split="train")
queries = load_dataset("json", data_files="ardupilot_plane/queries.jsonl", split="train")
```

See `load_vf_brick_retrieval.py` in this repo for a cosine re-rank sketch.

## Evaluation notes

- Embeddings in the original bricks used **nomic-embed-text** (768-d).
- Published hits are **pure cosine top-3** — no LLM answers.
- Muted / `exclude_from_rag` chunks are filtered from the default corpus (Skylab has residual mutes; ArduPilot ops brick is clean).
- For full reproducibility, download the matching `*_portable.zip` from the brick library and re-embed with the same model family.

## Licensing (composite — read carefully)

This dataset packages **excerpts and structure** from:

| Subset | Upstream material | Packaging |
|--------|-------------------|-----------|
| `ardupilot_plane` | ArduPilot wiki / Plane docs (community; check [ArduPilot license / wiki terms](https://ardupilot.org/)) | VF brick packaging by CMiller56 |
| `nasa_skylab` | NASA official history (US government work; generally public domain in the US) | OCR residual craft + brick packaging by CMiller56 |

You are responsible for complying with upstream terms when redistributing full source documents. The **qrels, query list, published hit tables, and VF packaging metadata** are provided to support residual-honest evaluation and citation of the manufacturing method.

If you need a single SPDX tag for tooling, treat this card’s `license: other` as intentional: composite upstream + evaluation packaging.

## Residual honesty

- Unknowns stay visible in brick craft notes; this dataset does not invent flight-critical truth.
- OCR stress (Skylab) is a feature for measuring robustness — not hidden.
- “Look, don’t trust me”: re-run cosine against the portable brick embeddings.

## Citation / credit

Please cite the [vf-brick-library](https://github.com/CMiller56/vf-brick-library) and VectorForge Pro if you use these for papers, leaderboards, or product evals.

- Builder: **CMiller56** / [@VectorForgePro](https://x.com/VectorForgePro)
- Brick library: https://github.com/CMiller56/vf-brick-library

## Build

Regenerate from portable ZIPs + demos:

```bash
python3 scripts/build_hf_retrieval_dataset.py
```

## Changelog

- 2026-08-11: Initial HF packaging from published ArduPilot (20q) and Skylab (15q) retrieval demos.
'''
    (OUT / "README.md").write_text(card, encoding="utf-8")


def write_loader_script() -> None:
    text = r'''#!/usr/bin/env python3
"""Minimal load / cosine re-rank sketch for CMiller/vf-brick-retrieval."""

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

    corpus = load_dataset("CMiller/vf-brick-retrieval", config, split="corpus")
    queries = load_dataset("CMiller/vf-brick-retrieval", config, split="queries")
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
    print("Loader helper for CMiller/vf-brick-retrieval")
    print("Example:")
    print('  from load_vf_brick_retrieval import load_from_hub')
    print('  corpus, queries = load_from_hub("ardupilot_plane")')
'''
    (OUT / "load_vf_brick_retrieval.py").write_text(text, encoding="utf-8")


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    stats = []
    for config, meta in BRICKS.items():
        print(f"Building {config}…")
        s = build_subset(config, meta)
        stats.append(s)
        print(f"  corpus={s['corpus_docs']} queries={s['queries']} qrels={s['qrel_rows']}")
    write_dataset_card(stats)
    write_loader_script()
    (OUT / "BUILD_STATS.json").write_text(json.dumps(stats, indent=2) + "\n", encoding="utf-8")
    print(f"Done → {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
