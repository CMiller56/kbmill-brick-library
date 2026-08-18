# UAVCAN (CVRA / legacy facet)

**Brick id:** `UAVCAN_cvra`  
**Chunks:** 41  
**Package:** `UAVCAN_cvra_portable.zip` (~209 KB)

## Purpose

Small UAVCAN-oriented DSDL / protocol facet from CVRA-style materials.

## Audience

Protocol developers.

## Snapshot (critical for this domain)

Corpus packaged **2026-07-18** from structured UAVCAN/CVRA MD. Legacy-oriented; not full UAVCAN v1 universe.

## Export / quality gate (what “waived” meant)

Soft residual (non-blocking).

Internal Job C soft-gate language is **not** a silent pass. If a card previously said only `Export gate waived: True` without explanation, treat that as insufficient — this section replaces it.

## Known limits / residual (specific)

- Small brick — incomplete vs modern UAVCAN/DroneCAN full surface.
- Prefer DroneCAN brick for current bus work unless you know you need this facet.

## License / rights

**Upstream:** UAVCAN / CVRA materials under their respective licenses — verify.

**This brick:** Derived package; attribution required. Not an official UAVCAN distribution.

## How to use (portable — not VF-only)

1. Download and unzip `UAVCAN_cvra_portable.zip`.
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

- Recut 2026-08-17: outline 17/22 (chunk_headings); SECURITY_REPORT.md in ZIP
