# CubePilot flight controllers

**Brick id:** `CubePilot_FC`  
**Chunks:** 258  
**Package:** `CubePilot_FC_portable.zip` (~1077 KB)

## Purpose

Cube / CubePilot hardware and related documentation (GitBook-style clean path).

## Audience

Cube hardware users and integrators.

## Snapshot (critical for this domain)

Corpus packaged **2026-07-18** from CubePilot/related docs after GitBook sanitize prep. Hardware revs differ (Orange/Red/etc.).

## Export / quality gate (what “waived” meant)

Portable export; soft residual only (e.g. smoke not always re-run).

Internal Job C soft-gate language is **not** a silent pass. If a card previously said only `Export gate waived: True` without explanation, treat that as insufficient — this section replaces it.

## Known limits / residual (specific)

- Cross-check board revision and connector pinouts against current CubePilot docs for your hardware.
- GitBook conversion may leave residual craft noise; report bad sections.

## License / rights

**Upstream:** CubePilot / Hex documentation terms apply to source material — verify on the publisher site.

**This brick:** Derived retrieval package. Preserve attribution; do not treat as official CubePilot distribution. Not affiliated with or endorsed by CubePilot.

## How to use (portable — not VF-only)

1. Download and unzip `CubePilot_FC_portable.zip`.
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

- Recut 2026-08-19: outline 69/120 (chunk_headings); tables=186 (camelot=0, md=186); SECURITY_REPORT.md in ZIP

- Recut 2026-08-17: outline 69/120 (chunk_headings); SECURITY_REPORT.md in ZIP
