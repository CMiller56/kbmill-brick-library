# FM 7-85 Ranger Unit Operations

**Brick id (folder):** `FM_7_85_Ranger_Unit_Operations`  
**Chunks:** 420  
**Muted / exclude_from_rag:** 6  
**Package:** `FM_7_85_Ranger_Unit_Operations_portable.zip` (44821 KB)  
**Search smoke:** PASS  
**Public gallery:** **yes** (US Government work)  
**Family:** doctrine  

## Purpose

US Army **Field Manual 7-85, Ranger Unit Operations** — ranger unit organization, employment, and operations doctrine packaged for residual-honest retrieval.

**Not** official Army redistribution or current operational authority. Pair with Ranger handbook bricks (small-unit skills) and FM 3-90 (broader tactics).

## Related bricks

- [`Ranger_Handbook_SH_21_76`](../Ranger_Handbook_SH_21_76/) — Ranger Handbook SH 21-76 (2000) — historical small-unit sibling
- [`Ranger_Handbook_TC_3_21_76`](../Ranger_Handbook_TC_3_21_76/) — Ranger Handbook TC 3-21.76 (2017) — modern TC sibling
- [`FM_3_90_Tactics`](../FM_3_90_Tactics/) — FM 3-90 Tactics (2001) — broader land tactics

## Audience

Students of ranger / light-infantry unit operations, veterans refreshing doctrine vocabulary, integrators stress-testing **mid-size** field-manual bricks (figures, multi-section, residual mutes), and air-gap / local-LLM users who need attributed offline text.

## Sources

- **Primary:** United States Army — *FM 7-85 Ranger Unit Operations*.  
- File as ingested: `fm_7-85_ranger_unit_operations.pdf` (~182 pages).  
- Internet Archive / public haul for factory dogfood and public brick packaging.

## License / rights

**US Government work.** Works of the US federal government are generally not subject to copyright in the United States (17 U.S.C. § 105). This brick is a **derived retrieval package** — **not** an official DoD/Army product and **not endorsed** by the US Army.

- Do not claim currency of doctrine; verify against official sources when it matters.  
- Confirm local rules if redistributing outside the US.  
- Original PDF remains system of record when you hold a copy.

## Known limits / residual honesty

- Mid-size FM: expect figure-shell / diagram mutes after figure magazine.  
- OCR promote is **quality-gated** (F1); plot/debris OCR not lifted as prose.  
- Built with **`figure-magazine --profile gov_fm`** (multi_section re-pass included).  
- Layout, tables, and illustrations may lose fidelity in plain text.  
- Soft ship gates (human Mark Ready) may remain; high-priority residual cleared when possible.  
- Sidecars: `finish_report.json`, `figure_magazine.json`, `figure_index.json`, `job_b_recheck.json`, `_full_build.log`.

## How to use

1. Unzip `FM_7_85_Ranger_Unit_Operations_portable.zip` (or load per `HANDOFF_README.md`).  
2. `load_kb("FM_7_85_Ranger_Unit_Operations")` in VF Runtime Connect / Engine.  
3. Prefer questions grounded in ranger unit ops — cite chunks; verify residual.  
4. Chat LLM is **not** bundled.

## Feedback

Open an issue on [vf-brick-library](https://github.com/CMiller56/vf-brick-library) with brick name + failing query.

Built: 2026-07-30 18:11:24 · 100-brick B2 · figure-magazine profile=gov_fm · FM 7-85

## Residual note (post-build fix)

1. Unmuted **178** chunks re-muted by `mute_open_hollow` after `promote-figure-ocr` (same class as SF Medical shell re-mute).  
2. `mute_open_hollow` now **skips** `promoted_from_figure_ocr`.  
3. Restored extraction quality on promoted shells so Job B is clean (promote default now floors green).  
4. Active muted after fix: **6** of 420 (plot debris only).  
5. Portable ZIP is large (~461 MB) because extract produced ~10k image crops.

## Package note (gallery slim)

Portable ZIP includes **364** primary figure images (≥8000 B, max 2/page), not the full extract crop set. Full assets remain under Pro `kbs/FM_7_85_Ranger_Unit_Operations/` when manufactured locally.
