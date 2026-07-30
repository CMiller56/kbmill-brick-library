# Ranger Handbook (TC 3-21.76, 2017)

**Brick id (folder):** `Ranger_Handbook_TC_3_21_76`  
**Chunks:** 509  
**Muted / exclude_from_rag:** 116  
**Package:** `Ranger_Handbook_TC_3_21_76_portable.zip` (35216 KB)  
**Search smoke:** PASS (see build log)  
**Public gallery:** **yes** (US Government work)  
**Sibling brick:** [`Ranger_Handbook_SH_21_76`](../Ranger_Handbook_SH_21_76/) — SH 21-76 (2000) historical student handbook

## Purpose

US Army **Ranger Handbook**, Training Circular **TC 3-21.76** (April 2017) — the modern TC-series handbook many readers know as “the Ranger Handbook.” Patrols, skills, battle drills, and related small-unit content packaged for residual-honest retrieval.

**Not** official Army redistribution or current operational authority. For discriminating consumers: pair with **SH 21-76 (2000)** to compare editions, organization, and extract quality across two doctrine packages.

## Audience

Students of small-unit tactics, veterans comparing editions, integrators testing mid/large field-manual bricks, and anyone who trained on TC 3-21.76 rather than the older SH.

## Sources

- **Primary:** United States Army — *Ranger Handbook*, **TC 3-21.76** (2017).  
- File as ingested: `TC 3-21.76 Ranger Handbook  2017.pdf` (~370 pages).  
- Internet Archive / public haul for factory dogfood and public brick packaging.

## License / rights

**US Government work.** Works of the US federal government are generally not subject to copyright in the United States (17 U.S.C. § 105). This brick is a **derived retrieval package** — **not** an official DoD/Army product and **not endorsed** by the US Army.

- Do not claim currency of doctrine; verify against official sources when it matters.  
- Confirm local rules if redistributing outside the US.  
- Original PDF remains system of record when you hold a copy.

## Known limits / residual honesty

- Larger than SH 21-76 (2000): more pages, denser figures — expect more **figure-shell / diagram** mutes.  
- OCR promote is **quality-gated** (F1); plot/debris OCR not lifted as prose.  
- Dual-stream / imprint tools applied when pair-rate warrants.  
- Layout, tables, and illustrations may lose fidelity in plain text.  
- Soft ship gates (human Mark Ready) may remain; high-priority residual cleared when possible.
- Soft craft flags: several **multi_section** chunks (two ## headings) and one review_extraction — not muted; optional finish split later.  
- Sidecars: `finish_report.json`, `mute_plot_debris.json`, `figure_index.json`, `job_b_recheck.json`, `_full_build.log`.

## How to use

1. Unzip `Ranger_Handbook_TC_3_21_76_portable.zip` (or load per `HANDOFF_README.md`).  
2. `load_kb("Ranger_Handbook_TC_3_21_76")` in VF Runtime Connect / Engine.  
3. For edition discrimination, also load or compare **`Ranger_Handbook_SH_21_76`**.  
4. Chat LLM is **not** bundled.

## Feedback

Open an issue on [vf-brick-library](https://github.com/CMiller56/vf-brick-library) with brick name + failing query.

Built: 2026-07-29 20:24:45 · 100-brick B2 · sibling pair with SH 21-76  
