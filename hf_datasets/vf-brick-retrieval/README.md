---
license: other
license_name: composite-upstream-and-brick-packaging
license_link: https://github.com/CMiller56/kbmill-brick-library
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
- kbmill
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
pretty_name: KBMill Brick Retrieval Demos
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

# KBMill Brick Retrieval Demos

Portable, **residual-honest** knowledge bricks turned into retrieval evaluation sets for **[KBMill](https://kbmill.com)** — the public mill at kbmill.com. Shelf packages live in [kbmill-brick-library](https://github.com/CMiller56/kbmill-brick-library).

These are **not** unbounded wiki dumps or synthetic QA. They come from real **KBMill** manufacturing: bounded packages with muted residual junk filtered where applicable, craft notes, security report in the ZIP, and **published, re-runnable cosine retrieval evidence**.

| Config | Queries | Corpus docs (eligible) | Source brick |
|--------|--------:|-----------------------:|--------------|
| `ardupilot_plane` | 20 | 332 | [ArduPilot_Plane](https://github.com/CMiller56/kbmill-brick-library/tree/main/bricks/ArduPilot_Plane) (ops wiki) |
| `ardupilot_plane_params` | 15 | 1781 | [ArduPilot_Plane_Params](https://github.com/CMiller56/kbmill-brick-library/tree/main/bricks/ArduPilot_Plane_Params) (dense param tables) |
| `nasa_skylab` | 15 | 1141 | [NASA_Skylab_History_Living_Working_Space](https://github.com/CMiller56/kbmill-brick-library/tree/main/bricks/NASA_Skylab_History_Living_Working_Space) |

**Compose, don’t melt:** ops vs params are separate packages — [COMPOSITION_ArduPilot_Plane.md](https://github.com/CMiller56/kbmill-brick-library/blob/main/COMPOSITION_ArduPilot_Plane.md).

## If your local model is up and answers from your docs are still junk

The model is fine. The corpus is not.

A **knowledge brick** is a **residual-honest** **portable ZIP** you keep: shaped corpus, **`craft_brief.md`**, and **`SECURITY_REPORT.md`** in the remilled gallery ZIP. Known junk is **muted off the answer path** (listed on the card / brief — not hidden). It is **not a chatbot** and **not a per-page parser**. We do not host your files as a library.

**Mill:** **[https://kbmill.com](https://kbmill.com)** — drop the pile. **Small $149 / Medium $399 / Hard $999** is craft load, not page count. You **pay only if we produce** a usable ZIP. After Ready, download within 72 hours, then we purge. Point *your* existing model at the package.

These evals and the [kbmill-brick-library](https://github.com/CMiller56/kbmill-brick-library) shelf are the public proof next to the mill.

**Look, don’t trust me:** [ArduPilot Plane retrieval demo](https://github.com/CMiller56/kbmill-brick-library/blob/main/RETRIEVAL_DEMO_ArduPilot_Plane.md) (20 questions). This dataset is the machine twin.

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

## Why this exists

Most RAG failures are **data-preparation** failures. These demos let you measure retrieval quality on:

- **Technical operations documentation** (ArduPilot Plane ops facet)
- **Dense parameter tables** (ArduPilot Plane Params)
- **Hostile OCR / paper-capture** historical technical text (NASA Skylab history)

Configs publish top-3 cosine results with chunk IDs, headings, sources, and excerpts so you can verify without trusting marketing claims.

Full write-ups:

- [RETRIEVAL_DEMO_ArduPilot_Plane.md](https://github.com/CMiller56/kbmill-brick-library/blob/main/RETRIEVAL_DEMO_ArduPilot_Plane.md)
- [RETRIEVAL_DEMO_ArduPilot_Plane_Params.md](https://github.com/CMiller56/kbmill-brick-library/blob/main/RETRIEVAL_DEMO_ArduPilot_Plane_Params.md)
- [RETRIEVAL_DEMO_NASA_Skylab_History.md](https://github.com/CMiller56/kbmill-brick-library/blob/main/RETRIEVAL_DEMO_NASA_Skylab_History.md)
- [COMPOSITION_ArduPilot_Plane.md](https://github.com/CMiller56/kbmill-brick-library/blob/main/COMPOSITION_ArduPilot_Plane.md)

Full portable ZIPs (Markdown + chunks + embeddings + cards) live in the [kbmill-brick-library](https://github.com/CMiller56/kbmill-brick-library).

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

corpus = load_dataset("CMiller/kbmill-brick-retrieval", "ardupilot_plane", split="corpus")
queries = load_dataset("CMiller/kbmill-brick-retrieval", "ardupilot_plane", split="queries")

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
| `ardupilot_plane_params` | ArduPilot Plane parameter / log reference | VF brick packaging by CMiller56 |
| `nasa_skylab` | NASA official history (US government work; generally public domain in the US) | OCR residual craft + brick packaging by CMiller56 |

You are responsible for complying with upstream terms when redistributing full source documents. The **qrels, query list, published hit tables, and VF packaging metadata** are provided to support residual-honest evaluation and citation of the manufacturing method.

If you need a single SPDX tag for tooling, treat this card’s `license: other` as intentional: composite upstream + evaluation packaging.

## Residual honesty

- Unknowns stay visible in brick craft notes; this dataset does not invent flight-critical truth.
- OCR stress (Skylab) is a feature for measuring robustness — not hidden.
- “Look, don’t trust me”: re-run cosine against the portable brick embeddings.

## Citation / credit

Please cite [KBMill](https://kbmill.com) and the [public brick shelf](https://github.com/CMiller56/kbmill-brick-library) if you use these for papers, leaderboards, or product evals.

- Product: **[KBMill](https://kbmill.com)** · X [@VectorForgePro](https://x.com/VectorForgePro) · GitHub **CMiller56**
- Brick library: https://github.com/CMiller56/kbmill-brick-library

## Build

Regenerate from portable ZIPs + demos:

```bash
python3 scripts/build_hf_retrieval_dataset.py
```

## Changelog

- 2026-08-19: Rebuild corpus after Camelot-fix gallery remill (Skylab eligible docs 1099→1141; Plane/Params unchanged). Package claims aligned with ZIP reality (`SECURITY_REPORT.md` + `craft_brief.md`; no invented `MILL_RECEIPT` / `residual_board.md` on every brick). Catalog/LIBRARY_CARD chunk counts synced to ZIPs.
- 2026-08-17: Rebuild corpus from remilled gallery ZIPs (wiki-nav strip + false-heading mop + `SECURITY_REPORT.md` in the brick). Card names KBMill, brick-vs-parse, pay-on-success. Published hits may still quote pre-remill excerpts until the Plane/Params/Skylab *eval JSON* is re-run.
- 2026-08-12: Clarify middle position — neither lab-clean nor raw dump; residual-honest real source material.
- 2026-08-12: Add `ardupilot_plane_params` config (15q, dense tables) + composition link.
- 2026-08-12: Baseline metrics + `docs/BRICK_SPEC.md` snapshot.
- 2026-08-11: Initial HF packaging from published ArduPilot (20q) and Skylab (15q) retrieval demos.
