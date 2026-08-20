# Mission Planner (GCS)

**Brick id:** `ArduPilot_MissionPlanner`  
**Chunks:** 182  
**Package:** `ArduPilot_MissionPlanner_portable.zip` (~800 KB)

## Purpose

Mission Planner ground-control documentation facet (calibration, setup, common workflows).

## Audience

GCS operators and setup tinkerers offline.

## Snapshot (critical for this domain)

Corpus packaged **2026-07-18** from Mission Planner / common ArduPilot GCS MD corpus. UI labels change by MP version.

## Export / quality gate (what “waived” meant)

Soft residual craft debt at export (non-blocking).

Internal Job C soft-gate language is **not** a silent pass. If a card previously said only `Export gate waived: True` without explanation, treat that as insufficient — this section replaces it.

## Known limits / residual (specific)

- Screenshots and menu paths age quickly — prefer concepts over pixel-perfect UI steps.
- A few soft craft flags may remain from HTML/MD conversion.

## License / rights

**Upstream:** ArduPilot / Mission Planner documentation terms (typically **CC BY-SA** on wiki-class material — verify).

**This brick:** Derived offline retrieval package; keep attribution and ShareAlike. Not affiliated with or endorsed by ArduPilot.

## How to use (portable — not VF-only)

1. Download and unzip `ArduPilot_MissionPlanner_portable.zip`.
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

- Recut 2026-08-19: outline 79/102 (chunk_headings); SECURITY_REPORT.md in ZIP

- Recut 2026-08-17: outline 79/102 (chunk_headings); SECURITY_REPORT.md in ZIP
