# ArduPilot Plane (operations)

**Brick id:** `ArduPilot_Plane`  
**Chunks:** 335  
**Package:** `ArduPilot_Plane_portable.zip` (~1472 KB)

## Purpose

Flight operations / Plane wiki-oriented knowledge for fixed-wing ArduPilot (modes, setup, failsafes, missions, landing — not the full parameter encyclopedia).

## Audience

ArduPilot tinkerers, GCS users, restricted-environment integrators who need offline ops reference.

## Snapshot (critical for this domain)

Corpus packaged **2026-07-18** from a local mirror of ArduPilot Plane–style documentation (wiki/HTML → structured MD). **Not pinned to a single Plane firmware tag** — parameter numbers and mode behavior can differ by release; verify critical values against the docs for *your* Plane version.

## Export / quality gate (what “waived” meant)

Recut **2026-08-17:** wiki nav chrome stripped (Commercial Support / Stores prefixes); headings propagated by source file; false “math garble” on param/mode tables and GCS logs suppressed. Ship check **ready_to_ship**. Still **not** flight-certified.

## Known limits / residual (specific)

- This is the **ops facet** — for parameters use `ArduPilot_Plane_Params`.
- Wiki HTML can still leave thin sections or wrap artifacts; if a hit looks like menu noise, open an issue.
- Some retrieval questions land on **adjacent** sections (e.g. VTOL/Q modes vs pure fixed-wing) — see the published retrieval demo.
- Not a substitute for the live docs when you are online and need the latest revision.

## License / rights

**Upstream:** ArduPilot documentation is generally offered under **Creative Commons Attribution-ShareAlike** (CC BY-SA; confirm current deed on the ArduPilot wiki / docs site).

**This brick (derived package):** Text content in the ZIP is a **transformed, attributed derivation** of that documentation for offline retrieval. Redistribution of this package should preserve **attribution to the ArduPilot project and original authors** and respect **ShareAlike** for the documentation content. Embeddings and packaging structure are VectorForge brick format, not a claim of ownership over ArduPilot text.

**Not affiliated with or endorsed by** the ArduPilot project.

## How to use (portable — not VF-only)

1. Download and unzip `ArduPilot_Plane_portable.zip`.
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

- Recut 2026-08-19: outline 121/199 (chunk_headings); SECURITY_REPORT.md in ZIP

- Recut 2026-08-17: false-headings running_title=2; outline 121/199 (chunk_headings); SECURITY_REPORT.md in ZIP
