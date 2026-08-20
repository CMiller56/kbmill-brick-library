# FM 3-90 Tactics (2001)

**Brick id (folder):** `FM_3_90_Tactics`  
**Chunks:** 1070  
**Muted / exclude_from_rag:** 189  
**Package:** `FM_3_90_Tactics_portable.zip` (8379 KB)  
**Search smoke:** PASS  
**Public gallery:** **yes** (US Government work)  
**Family:** doctrine  

## Purpose

US Army **Field Manual 3-90, Tactics** (2001) — offensive and defensive operations, tactical concepts, and related land-tactics doctrine packaged for residual-honest retrieval.

**Not** official Army redistribution or current operational authority. Pair with Ranger handbook bricks for small-unit vs broader tactics surface.

## Related bricks

- [`Ranger_Handbook_SH_21_76`](../Ranger_Handbook_SH_21_76/) — public Ranger handbook sibling
- [`Ranger_Handbook_TC_3_21_76`](../Ranger_Handbook_TC_3_21_76/) — public Ranger handbook sibling

## Audience

Students of land tactics, veterans refreshing doctrine vocabulary, integrators stress-testing **large** field-manual bricks (figures, multi-section, residual mutes), and air-gap / local-LLM users who need attributed offline text.

## Sources

- **Primary:** United States Army — *FM 3-90 Tactics* (2001).  
- File as ingested: `fm_3-90_tactics_2001.pdf` (~627 pages).  
- Internet Archive / public haul for factory dogfood and public brick packaging.

## License / rights

**US Government work.** Works of the US federal government are generally not subject to copyright in the United States (17 U.S.C. § 105). This brick is a **derived retrieval package** — **not** an official DoD/Army product and **not endorsed** by the US Army.

- Do not claim currency of doctrine; verify against official sources when it matters.  
- Confirm local rules if redistributing outside the US.  
- Original PDF remains system of record when you hold a copy.

## Known limits / residual honesty

- Recut 2026-08-19: outline 31/51 (chunk_headings); tables=21 (camelot=7, md=14); SECURITY_REPORT.md in ZIP

- Recut 2026-08-17: outline 53/250 (chunk_headings); SECURITY_REPORT.md in ZIP

- Large FM: expect **many figure-shell / diagram** mutes after figure magazine.  
- OCR promote is **quality-gated** (F1); plot/debris OCR not lifted as prose.  
- Built with **`figure-magazine --profile gov_fm`** (multi_section re-pass included).  
- Layout, tables, and illustrations may lose fidelity in plain text.  
- Soft ship gates (human Mark Ready) may remain; high-priority residual cleared when possible.  
- Sidecars: `finish_report.json`, `figure_magazine.json`, `figure_index.json`, `job_b_recheck.json`, `_full_build.log`.

## How to use

1. Unzip `FM_3_90_Tactics_portable.zip` (or load per `HANDOFF_README.md`).  
2. `load_kb("FM_3_90_Tactics")` in VF Runtime Connect / Engine.  
3. Prefer questions grounded in offensive/defensive tactics — cite chunks; verify residual.  
4. Chat LLM is **not** bundled.

## Feedback

Open an issue on [vf-brick-library](https://github.com/CMiller56/vf-brick-library) with brick name + failing query.

Built: 2026-07-30 07:02:45 · 100-brick B2 · figure-magazine profile=gov_fm · FM 3-90  
