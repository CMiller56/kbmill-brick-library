# MAVLink (ArduPilot-oriented)

**Brick id:** `ArduPilot_MAVLink`  
**Chunks:** 310  
**Package:** `ArduPilot_MAVLink_portable.zip` (~1214 KB)

## Purpose

Protocol / message knowledge for MAVLink in ArduPilot-oriented contexts (basics + dialect-oriented material from the corpus build).

## Audience

Developers and advanced integrators.

## Snapshot (critical for this domain)

Corpus packaged **2026-07-18** from structured MAVLink doctrine/MD in the local shelf corpus. Dialect XML evolves — treat as a **snapshot**, not live mavlink.io.

## Export / quality gate (what “waived” meant)

Portable export without hard gate failure. Soft residual may exist; none were hard-blocking at ship.

Internal Job C soft-gate language is **not** a silent pass. If a card previously said only `Export gate waived: True` without explanation, treat that as insufficient — this section replaces it.

## Known limits / residual (specific)

- Protocol surface is incomplete vs the full dialect universe — use for common messages and concepts.
- Copter-specific notes may appear in shared dialect material; filter by your vehicle.

## License / rights

**Upstream:** MAVLink / ArduPilot documentation terms apply to source text (often CC-style — verify at source).

**This brick:** Derived retrieval package with attribution. Preserve upstream license obligations. Not affiliated with Dronecode/ArduPilot.

## How to use (portable — not VF-only)

1. Download and unzip `ArduPilot_MAVLink_portable.zip`.
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

- Recut 2026-08-17: outline 205/250 (chunk_headings); SECURITY_REPORT.md in ZIP
