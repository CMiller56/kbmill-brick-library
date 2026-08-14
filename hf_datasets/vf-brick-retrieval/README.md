---
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
- config_name: ardupilot_plane_params
  data_files:
  - split: corpus
    path: ardupilot_plane_params/corpus.jsonl
  - split: queries
    path: ardupilot_plane_params/queries.jsonl
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
| `ardupilot_plane` | 20 | 335 | [ArduPilot_Plane](https://github.com/CMiller56/vf-brick-library/tree/main/bricks/ArduPilot_Plane) (ops wiki) |
| `ardupilot_plane_params` | 15 | 1781 | [ArduPilot_Plane_Params](https://github.com/CMiller56/vf-brick-library/tree/main/bricks/ArduPilot_Plane_Params) (dense param tables) |
| `nasa_skylab` | 15 | 1099 | [NASA_Skylab_History_Living_Working_Space](https://github.com/CMiller56/vf-brick-library/tree/main/bricks/NASA_Skylab_History_Living_Working_Space) |

**Compose, don’t melt:** ops vs params are separate packages — [COMPOSITION_ArduPilot_Plane.md](https://github.com/CMiller56/vf-brick-library/blob/main/COMPOSITION_ArduPilot_Plane.md).

## If your local model is up and answers from your docs are still junk

The model is fine. The corpus is not.

A **knowledge brick** is a **residual-honest** **portable ZIP** you keep: structure, citations, and known junk **muted off the answer path** (listed, not hidden). It is **not a chatbot**. We do not host your files.

**When the plant is live:** drop the files you already have — often the same week. You **pay only if we produce**. You keep the ZIP. Point your existing local model at that package; do not replace your stack.

**No hopper URL yet.** These evals and the [vf-brick-library](https://github.com/CMiller56/vf-brick-library) are the public proof. The plant link will be added on that README when it vends — we will not invent one.

**Look, don’t trust me:** [ArduPilot Plane retrieval demo](https://github.com/CMiller56/vf-brick-library/blob/main/RETRIEVAL_DEMO_ArduPilot_Plane.md) (20 questions). This dataset is the machine twin.

## Design intent (the differentiator)

Most public retrieval corpora were built for **traditional IR** or as **general training fuel**. They were never optimized as the **final working surface for an LLM**.

VectorForge bricks invert that: the package is shaped so the **model can use the knowledge cleanly** — bounded scope, residual honesty (muted junk stays off the path), stable chunk identity, clear provenance, and craft notes that tell the system what the brick is and is not for. When the consumer is the LLM itself, those choices compound.

These are **not** heavily sanitized lab sets, and they are **not** raw unbounded dumps. They are **residual-honest packages of real source material**: known junk is muted and visible, bounds are explicit, and the package is shaped so a model can work with what it will actually see **outside the lab**.

That is why bricks are designed so models **spend less capacity fighting noise** — retrieval quality and downstream answer fidelity both have a cleaner path. The published ArduPilot and Skylab demos already show the **retrieval side** of that claim in a re-runnable form (cosine top-3; not chat transcripts or invented answers).

**Framing for this dataset:**

- These are **not** “just another technical corpus,” and **not** lab-clean synthetic IR fuel.
- They are **LLM-native knowledge units** — manufactured so the **model is the primary user**.
- **Residual honesty + bounded packaging** is the practical expression of that design goal (best realistic case after careful packaging; residuals stay visible).

This is the story that should land with people who care about **production RAG quality** (and the LocalLLaMA / air-gapped crowd) rather than pure leaderboard optics: *here is what a knowledge package looks like when it was built for the model that has to live with it.*

## Brick contract

Retrieval configs here are **instances** of VectorForge portable bricks. The manufacturing contract — what a brick is / is not, package layout, chunk fields, RAG eligibility (`muted` / `exclude_from_rag`), composition — lives in:

**[`docs/BRICK_SPEC.md`](docs/BRICK_SPEC.md)** (HF snapshot of [vf-brick-library/BRICK_SPEC.md](https://github.com/CMiller56/vf-brick-library/blob/main/BRICK_SPEC.md) v1.0)

Multi-brick routing example: **[`docs/COMPOSITION_ArduPilot_Plane.md`](docs/COMPOSITION_ArduPilot_Plane.md)** (ops + params + protocol — compose, don’t melt).

You do **not** need the spec to `load_dataset`. You **do** need it if you want to judge the method, build compatible packages, or understand why mutes and bounds exist.

## Why this exists

Most RAG failures are **data-preparation** failures. These demos let you measure retrieval quality on:

- **Technical operations documentation** (ArduPilot Plane ops facet)
- **Dense parameter tables** (ArduPilot Plane Params — large soft residual by design)
- **Hostile OCR / paper-capture** historical technical text (NASA Skylab history)

Configs publish top-3 cosine results with chunk IDs, headings, sources, and excerpts so you can verify without trusting marketing claims.

Full write-ups:

- [RETRIEVAL_DEMO_ArduPilot_Plane.md](https://github.com/CMiller56/vf-brick-library/blob/main/RETRIEVAL_DEMO_ArduPilot_Plane.md)
- [RETRIEVAL_DEMO_ArduPilot_Plane_Params.md](https://github.com/CMiller56/vf-brick-library/blob/main/RETRIEVAL_DEMO_ArduPilot_Plane_Params.md)
- [RETRIEVAL_DEMO_NASA_Skylab_History.md](https://github.com/CMiller56/vf-brick-library/blob/main/RETRIEVAL_DEMO_NASA_Skylab_History.md)
- [COMPOSITION_ArduPilot_Plane.md](https://github.com/CMiller56/vf-brick-library/blob/main/COMPOSITION_ArduPilot_Plane.md)

Full portable ZIPs (Markdown + chunks + embeddings + cards) live in the [vf-brick-library](https://github.com/CMiller56/vf-brick-library).

## Dataset layout (BEIR-compatible)

```text
README.md                      # this card
docs/BRICK_SPEC.md             # manufacturing contract (snapshot)
baseline_retrieval_metrics.py  # re-embed + Recall@k / nDCG@k / Hit@k
baseline_results_summary.json  # published baseline numbers
load_vf_brick_retrieval.py
ardupilot_plane/
  corpus.jsonl                 # eligible chunks (_id, text, source, heading, page, …)
  queries.jsonl                # _id, text
  qrels/test.tsv               # query-id  corpus-id  score (tab)
  published_hits.json          # original cosine top-3 evidence (scores + excerpts)
ardupilot_plane_params/
  … same layout (dense params; soft residual by design)
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

## Baseline metrics (re-runnable)

Public baseline: **re-embed** this HF corpus + queries with a named model, cosine top‑`k`, score against `qrels/test.tsv`.

| Config | Model | k | Recall@k | nDCG@k | Hit@k |
|--------|--------|--:|---------:|-------:|------:|
| `ardupilot_plane` | `nomic-ai/nomic-embed-text-v1.5` | 3 | **0.783** | **0.832** | **1.000** |
| `ardupilot_plane_params` | `nomic-ai/nomic-embed-text-v1.5` | 3 | **0.844** | **0.891** | **1.000** |
| `nasa_skylab` | `nomic-ai/nomic-embed-text-v1.5` | 3 | **0.378** | **0.416** | **0.867** |

- **Run:** `python3 baseline_retrieval_metrics.py` (from this dataset repo / local package).  
- **Machine JSON:** [`baseline_results_summary.json`](baseline_results_summary.json)  
- **Qrels definition:** binary relevance = **published cosine top‑3** chunk ids from the original brick embedding run (not multi-annotator graded IR). Re-encoding the HF text can differ from the brick’s stored vectors (especially OCR-heavy Skylab) — lower Skylab numbers are **expected stress**, not a silent failure.  
- **Hit@k:** fraction of queries with ≥1 qrel hit in top‑k. **Recall@k:** mean over queries of (|top‑k ∩ qrels| / |qrels|).

```bash
pip install sentence-transformers scikit-learn numpy
python3 baseline_retrieval_metrics.py --config all --model nomic-ai/nomic-embed-text-v1.5 --top-k 3
```

## Evaluation notes

- Original brick embeddings used **nomic-embed-text** (768-d); the baseline above re-encodes from **text** on this dataset for a fair public recipe.
- Published hits (`published_hits.json`) are **pure cosine top-3** from the brick matrix — no LLM answers.
- Muted / `exclude_from_rag` chunks are filtered from the default corpus (Skylab has residual mutes; ArduPilot ops brick is clean).
- For full brick reproducibility (stored `embeddings.npy` + sidecars), download the matching `*_portable.zip` from the brick library.

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

- 2026-08-12: Clarify middle position — neither lab-clean nor raw dump; residual-honest real source material.
- 2026-08-12: Add `ardupilot_plane_params` config (15q, dense tables) + composition link; baseline Recall@3 **0.844**.
- 2026-08-12: Baseline metrics — `baseline_retrieval_metrics.py` + public Recall@3 / nDCG@3 / Hit@3 table (nomic-embed-text-v1.5).
- 2026-08-12: Add `docs/BRICK_SPEC.md` (v1.0 snapshot) + brick contract section on the card.
- 2026-08-12: Design intent section — LLM-native knowledge units as the differentiator (not just another technical corpus).
- 2026-08-11: Initial HF packaging from published ArduPilot (20q) and Skylab (15q) retrieval demos.
