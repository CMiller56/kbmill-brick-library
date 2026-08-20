# NASA AMBR Engine Information Summary (May 2009)

**Brick id (folder):** `NASA_AMBR_Engine_Information_Summary`  
**Chunks:** 21  
**Muted / exclude_from_rag:** 0  
**Package:** `NASA_AMBR_Engine_Information_Summary_portable.zip` (103 KB)  
**Search smoke:** PASS  
**Public gallery:** **yes** (US Government / NASA)  
**Family:** aerospace_propulsion  

## Purpose

Short NASA **Advanced Materials Bi-propellant Rocket (AMBR)** engine information summary (May 2009): performance (Isp/thrust class), development notes, dual-mode propulsion context, and mission implementation cues for in-space propulsion.

**Not** an official NASA product redistribution or endorsement of this derived package.

## Related bricks

- [`Advanced_Rockets`](../Advanced_Rockets/) — Advanced chemical rocket engines (Haidn / RTO educational notes)
- [`NASA_41st_Aerospace_Mechanisms_Symposium`](../NASA_41st_Aerospace_Mechanisms_Symposium/) — NASA mechanisms proceedings
- [`NASA_Skylab_History_Living_Working_Space`](../NASA_Skylab_History_Living_Working_Space/) — NASA Skylab history

## Audience

Propulsion / mission design readers and integrators testing a **compact NASA technical summary** brick (factory dogfood + public gallery).

## Sources

- **Primary:** NASA Science Mission Directorate / In-Space Propulsion Technology (ISPT) — AMBR Engine Information Summary, May 2009.  
- File as ingested: `35AMBR_NF-AOrefdocument_May09.pdf` (~9 pages).

## License / rights

**US Government work** (NASA). Federal works are generally not subject to copyright in the United States (17 U.S.C. § 105). This brick is a **derived retrieval package** only — **not** an official NASA product. Confirm local rules if redistributing outside the US.

## Known limits / residual honesty

- Recut 2026-08-19: outline 5/5 (chunk_headings); SECURITY_REPORT.md in ZIP

- Recut 2026-08-17: outline 5/5 (chunk_headings); SECURITY_REPORT.md in ZIP

- Short paper-scale brick (few chunks); soft ship gates may remain (e.g. Mark Ready human step).  
- Built with Engine extract + **KBM Factory** manufacture path (`kbm-state` / `next` / `run` / `ship_check` / `export`).  
- Portable uses **`image_policy=none`** for gallery size when applicable.

## How to use

1. Unzip `NASA_AMBR_Engine_Information_Summary_portable.zip` (or load per HANDOFF).  
2. `load_kb("NASA_AMBR_Engine_Information_Summary")` in VF Runtime Connect.  
3. Prefer AMBR / bipropellant thruster / Isp / dual-mode questions — cite chunks.

## Feedback

Open an issue on [vf-brick-library](https://github.com/CMiller56/vf-brick-library) with brick name + failing query.

Built: 2026-07-31 13:39 · public gallery · figure-magazine ready · KBM Factory dogfood

## Residual craft (post-build)

- Active muted: **0** of 21.  
- Ship-check: **warnings** (hard=0, soft=1).  
- Search smoke: **PASS**.  
