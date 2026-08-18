# ArduPilot Plane Parameters

**Brick id:** `ArduPilot_Plane_Params`  
**Chunks:** 1781  
**Package:** `ArduPilot_Plane_Params_portable.zip` (~6014 KB)

## Purpose

Parameter reference facet for Plane — name-oriented sections for lookup. Pair with the ops brick; do not treat as the sole flight manual.

**Public retrieval demo:** [RETRIEVAL_DEMO_ArduPilot_Plane_Params.md](../../RETRIEVAL_DEMO_ArduPilot_Plane_Params.md) (15 questions) · composition: [COMPOSITION_ArduPilot_Plane.md](../../COMPOSITION_ArduPilot_Plane.md)

## Audience

Tuners and integrators looking up parameters offline.

## Snapshot (critical for this domain)

Corpus packaged **2026-07-18** from structured parameter reference MD derived from ArduPilot Plane params HTML. **Not locked to one firmware tag** — always cross-check param defaults and units against the parameter list for your exact Plane version.

## Export / quality gate (what “waived” meant)

Export used the normal portable path. Manufacturing soft residual was **high volume** (structure/craft noise on a multi-thousand-param surface) but **not hard-blocked**. That is expected for this shape of reference, not a silent pass.

Internal Job C soft-gate language is **not** a silent pass. If a card previously said only `Export gate waived: True` without explanation, treat that as insufficient — this section replaces it.

## Known limits / residual (specific)

- Large brick (~1.8k chunks): retrieval is for **param lookup**, not reading cover-to-cover.
- Structure debt is common: multi-section or thin param stubs from automated HTML→MD conversion.
- Defaults and availability change by release — snapshot dating above is mandatory reading.

## License / rights

**Upstream:** ArduPilot documentation (typically **CC BY-SA** — verify current terms).

**This brick:** Derived, attributed parameter reference for offline retrieval. Preserve attribution and ShareAlike obligations on the documentation content. Not affiliated with or endorsed by ArduPilot.

## How to use (portable — not VF-only)

1. Download and unzip `ArduPilot_Plane_Params_portable.zip`.
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

- Recut 2026-08-17: outline 176/250 (chunk_headings); SECURITY_REPORT.md in ZIP
