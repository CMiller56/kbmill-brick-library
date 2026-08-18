# Advanced Rocket Engines (Haidn / RTO-EN-AVT-150)

**Brick id:** `Advanced_Rockets`  
**Chunks:** 66  
**Package:** `Advanced_Rockets_portable.zip` (~1460 KB)

## Purpose

Technical reference on advanced chemical rocket engines from educational notes (cycles, turbomachinery, basics).

## Audience

Propulsion engineers and students — not flight certification.

## Snapshot (critical for this domain)

PDF educational notes **RTO-EN-AVT-150** Paper 6 (Haidn, DLR). Brick built **2026-07-03**. Paper date is the educational-notes series, not a living wiki.

## Export / quality gate (what “waived” meant)

Clean portable export (no hard block). Soft residual: craft flags present.

Internal Job C soft-gate language is **not** a silent pass. If a card previously said only `Export gate waived: True` without explanation, treat that as insufficient — this section replaces it.

## Known limits / residual (specific)

- **Named defect:** `chunk-0039` — `garbled_extraction` / math-font debris (~46% single-character lines). Do not trust that slice for equations without the original PDF.
- One waived thin/low-extraction stub on a late chunk.
- Dense figures/equations may be incomplete in plain text (honest PDF limits).

## License / rights

**Upstream:** NATO RTO/STO educational notes **RTO-EN-AVT-150** (Haidn / DLR). Confirm redistribution terms with the rights holder before commercial use.

**This brick:** Derived retrieval package, not an official NATO/DLR publication. Not affiliated with or endorsed by NATO STO, DLR, or the author.

## How to use (portable — not VF-only)

1. Download and unzip `Advanced_Rockets_portable.zip`.
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

- Recut 2026-08-17: false-headings running_title=54; outline 2/2 (chunk_headings); SECURITY_REPORT.md in ZIP
