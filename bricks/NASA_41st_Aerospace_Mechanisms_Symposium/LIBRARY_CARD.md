# 41st Aerospace Mechanisms Symposium (NASA/CP-2012-217653)

**Brick id (folder):** `NASA_41st_Aerospace_Mechanisms_Symposium`  
**Chunks:** 1051  
**Muted / exclude_from_rag:** 282  
**Package:** `NASA_41st_Aerospace_Mechanisms_Symposium_portable.zip` (33436 KB)  
**Search smoke:** PASS  
**Public gallery:** **yes** (US Government / NASA conference publication)  
**Family:** aerospace  

## Purpose

**NASA Conference Publication CP-2012-217653** — proceedings of the **41st Aerospace Mechanisms Symposium** (Pasadena). Multi-paper collection on spacecraft mechanisms, deployment systems, actuators, bearings, lubrication, and related mechanical design. Packaged for residual-honest retrieval and to demonstrate **modern multi-paper technical proceedings** manufacture (distinct from field manuals and historical OCR books).

**Not** official NASA redistribution or endorsement of this derived package. Prefer official NTRS for formal citation when required.

## Related bricks

- [`Advanced_Rockets`](../Advanced_Rockets/) — Aerospace paper brick (rocket engines)
- [`TM_11_666_Antennas_Radio_Propagation`](../TM_11_666_Antennas_Radio_Propagation/) — Historical RF/antennas TM

## Audience

Aerospace mechanisms engineers, systems integrators, and operators stress-testing conference-proceedings bricks (many authors, figures, equations, TOC/index) for offline RAG.

## Sources

- **Primary:** NASA / compiled-edited by Edward A. Boesiger — *41st Aerospace Mechanisms Symposium*, NASA/CP-2012-217653.  
- File as ingested: `NASA_NTRS_Archive_20130008824.pdf` (~520 pages).  
- NTRS / public technical archive haul for factory dogfood and public brick packaging.

## License / rights

**US Government work** (NASA conference publication). Federal works are generally not subject to copyright in the United States (17 U.S.C. § 105). This brick is a **derived retrieval package** only — **not** an official NASA product. Confirm local rules if redistributing outside the US. Original PDF remains system of record.

## Known limits / residual honesty

- Multi-paper proceedings: expect TOC/front matter, figure shells, equation/layout fidelity loss.  
- Built with **`figure-magazine --profile hard_pdf`** + full finish (soft-hyphen, TOC/index mute, heading sanitize).  
- Soft ship gates may remain.  
- Sidecars: `finish_report.json`, `figure_magazine.json`, `job_b_recheck.json`, `_full_build.log`.

## How to use

1. Unzip `NASA_41st_Aerospace_Mechanisms_Symposium_portable.zip` (or load per `HANDOFF_README.md`).  
2. `load_kb("NASA_41st_Aerospace_Mechanisms_Symposium")` in VF Runtime Connect / Engine.  
3. Prefer mechanisms / deployment / actuator questions — cite chunks; verify residual.  
4. Chat LLM is **not** bundled.

## Feedback

Open an issue on [vf-brick-library](https://github.com/CMiller56/vf-brick-library) with brick name + failing query.

Built: 2026-07-31 09:15:14 · 100-brick B2 · figure-magazine profile=hard_pdf · NASA AMS 41  
