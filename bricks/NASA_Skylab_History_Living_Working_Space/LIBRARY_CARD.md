# NASA Skylab History (Living and Working in Space)

**Brick id (folder):** `NASA_Skylab_History_Living_Working_Space`  
**Chunks:** 1260  
**Muted / exclude_from_rag:** 120  
**Package:** `NASA_Skylab_History_Living_Working_Space_portable.zip` (5315 KB)  
**Search smoke:** PASS  
**Public gallery:** **yes** (US Government / NASA history)  
**Family:** aerospace_history  

## Purpose

NASA **official Skylab history** — concept through decision, development, missions, living and working in space, experiments, and notes. Paper-capture OCR scan edition packaged for residual-honest retrieval and to demonstrate **space history narrative** manufacture (distinct from multi-paper mechanisms proceedings).

**Not** official NASA redistribution or endorsement of this derived package. Prefer official NASA History publications for formal citation when required.

## Related bricks

- [`NASA_41st_Aerospace_Mechanisms_Symposium`](../NASA_41st_Aerospace_Mechanisms_Symposium/) — Modern NASA mechanisms symposium papers
- [`Advanced_Rockets`](../Advanced_Rockets/) — Aerospace technical paper brick

## Audience

Space history readers, veterans of the AAP/Skylab era, and integrators testing **NASA history OCR scans** (hyphenation, figures, notes apparatus) for offline RAG.

## Sources

- **Primary:** NASA History Program — Skylab / *Living and Working in Space* class official history.  
- File as ingested: `HistoryofSkylab.pdf` (~467 pages; Adobe Paper Capture).  
- Public technical/history haul for factory dogfood and public brick packaging.

## License / rights

**US Government work** (NASA official history). Federal works are generally not subject to copyright in the United States (17 U.S.C. § 105). This brick is a **derived retrieval package** only — **not** an official NASA product. Confirm local rules if redistributing outside the US. Original scan remains system of record.

## Known limits / residual honesty

- Recut 2026-08-19: outline 27/43 (chunk_headings); tables=10 (camelot=6, md=4); SECURITY_REPORT.md in ZIP

- Recut 2026-08-17: outline 156/250 (chunk_headings); SECURITY_REPORT.md in ZIP

- Paper-capture OCR: empty covers, soft hyphens, figure plates, notes apparatus.  
- Built with **`figure-magazine --profile hard_pdf`** + full finish (soft-hyphen, TOC/index mute, heading sanitize).  
- Soft ship gates may remain.  
- Sidecars: `finish_report.json`, `figure_magazine.json`, `job_b_recheck.json`, `_full_build.log`.

## How to use

1. Unzip `NASA_Skylab_History_Living_Working_Space_portable.zip` (or load per `HANDOFF_README.md`).  
2. `load_kb("NASA_Skylab_History_Living_Working_Space")` in VF Runtime Connect / Engine.  
3. Prefer Skylab / AAP / space-station history questions — cite chunks; verify residual.  
4. Chat LLM is **not** bundled.

## Feedback

Open an issue on [vf-brick-library](https://github.com/CMiller56/vf-brick-library) with brick name + failing query.

Built: 2026-07-31 09:32:40 · 100-brick B2 · figure-magazine profile=hard_pdf · Skylab history

## Residual craft (post-build)

- Paper-capture OCR: **396** figure shells promoted; shells/plot-debris muted.  
- **Post-promote soft-hyphen** magazine step: 357 chunks joined (finish A3c alone runs *before* promote).  
- Index mute + heading sanitize on finish path.  
- Active muted: **108** of 1207. Soft ship warnings may remain.

## Portable package policy

- Public portable uses **`image_policy=none`** (text/OCR retrieval; figure plates omitted so package stays under GitHub soft max ~50 MB).  
- Desk KB still retains `images/` for operator figure work.  
- Re-export full images with `maintain export --images all` when needed.  
