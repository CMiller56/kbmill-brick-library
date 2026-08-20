# DroneCAN

**Brick id:** `DroneCAN`  
**Chunks:** 182  
**Package:** `DroneCAN_portable.zip` (~779 KB)

## Purpose

DroneCAN protocol and related documentation for offline reference.

## Audience

Avionics / bus integrators.

## Snapshot (critical for this domain)

Corpus packaged **2026-07-18** from structured DroneCAN MD corpus.

## Export / quality gate (what “waived” meant)

Soft residual at export (non-blocking); ship-for-feedback.

Internal Job C soft-gate language is **not** a silent pass. If a card previously said only `Export gate waived: True` without explanation, treat that as insufficient — this section replaces it.

## Known limits / residual (specific)

- Protocol docs evolve; treat as snapshot.
- Soft craft residual may remain from site conversion.

## License / rights

**Upstream:** DroneCAN project documentation license — verify at source.

**This brick:** Derived retrieval package with attribution. Not affiliated with or endorsed by the DroneCAN project.

## How to use (portable — not VF-only)

1. Download and unzip `DroneCAN_portable.zip`.
2. **Any stack that can read the package**, for example:
   - **Plain:** open the primary `*.md` and search; or index `chunks.jsonl` with any search tool.
   - **Embeddings:** load `embeddings.npy` + chunk order from `kb.json` / `chunks.jsonl` and cosine-rank (see [PORTABILITY.md](../../PORTABILITY.md)).
   - **VF Runtime Connect / Engine** if you have it — optional, not required.
3. Read **Known limits** and **Snapshot** first.
4. Chat LLM is **not** bundled.

**Reproducible quality check:** [RETRIEVAL_DEMO_ArduPilot_Plane.md](../../RETRIEVAL_DEMO_ArduPilot_Plane.md) (flagship Plane brick).


## Feedback (one channel)

Open an **Issue on this repository** (`vf-brick-library`), title: `<BrickName>: <short problem>`.

Include: question asked, what you expected, chunk id if you have one. That is how re-cuts happen.

Do **not** use the private Pro monorepo for public brick feedback.

## Known limits / residual honesty

- Recut 2026-08-19: outline 55/121 (chunk_headings); tables=11 (camelot=0, md=11); SECURITY_REPORT.md in ZIP

- Recut 2026-08-17: outline 55/121 (chunk_headings); SECURITY_REPORT.md in ZIP
