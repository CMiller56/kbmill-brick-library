# MCRP 3-01A Rifle Marksmanship

**Brick id (folder):** `MCRP_3_01A_Rifle_Marksmanship`  
**Chunks:** 274  
**Muted / exclude_from_rag:** 106  
**Package:** `MCRP_3_01A_Rifle_Marksmanship_portable.zip` (5061 KB)  
**Search smoke:** PASS  
**Public gallery:** **yes** (US Government work)  
**Family:** doctrine  

## Purpose

US Marine Corps **MCRP 3-01A, Rifle Marksmanship** (29 March 2001) — individual rifle marksmanship techniques, positions, engagement, and maintenance, packaged for residual-honest retrieval.

**Not** official Marine Corps redistribution or current training authority. Pre-digital publication structures (leader-dot TOC, numbered paragraphs, running headers, glossary) stress extract/chunk honesty.

## Related bricks

- [`Ranger_Handbook_SH_21_76`](../Ranger_Handbook_SH_21_76/) — Ranger Handbook SH 21-76 — small-unit sibling
- [`Ranger_Handbook_TC_3_21_76`](../Ranger_Handbook_TC_3_21_76/) — Ranger Handbook TC 3-21.76 — modern TC sibling
- [`FM_7_85_Ranger_Unit_Operations`](../FM_7_85_Ranger_Unit_Operations/) — FM 7-85 — ranger unit operations

## Audience

Students of marksmanship doctrine, veterans refreshing fundamentals, integrators testing **Word-era doctrine PDFs** with figures and dense numbered structure, air-gap / local-LLM users who need attributed offline text.

## Sources

- **Primary:** United States Marine Corps — *MCRP 3-01A Rifle Marksmanship* (29 March 2001).  
- File as ingested: `MCRP3-01A.pdf` (~117 pages; Acrobat Distiller / Word 9 era).  
- Public haul for factory dogfood and public brick packaging.

## License / rights

**US Government work.** Works of the US federal government are generally not subject to copyright in the United States (17 U.S.C. § 105). This brick is a **derived retrieval package** — **not** an official DoD/USMC product and **not endorsed** by the US Marine Corps.

- Do not claim currency of training standards; verify against official sources when it matters.  
- Confirm local rules if redistributing outside the US.  
- Original PDF remains system of record when you hold a copy.

## Known limits / residual honesty

- Recut 2026-08-19: outline 19/21 (chunk_headings); tables=10 (camelot=1, md=9); SECURITY_REPORT.md in ZIP

- Recut 2026-08-17: false-headings procedure_or_biblio=2; outline 65/125 (chunk_headings); SECURITY_REPORT.md in ZIP

- Pre-digital layout: hyphenated wraps, leader-dot tables of contents, figure callouts, appendix glossary.  
- Built with **`figure-magazine --profile gov_fm`**.  
- Soft ship gates may remain; high-priority residual cleared when possible.  
- Sidecars: `finish_report.json`, `figure_magazine.json`, `job_b_recheck.json`, `_full_build.log`.

## How to use

1. Unzip `MCRP_3_01A_Rifle_Marksmanship_portable.zip` (or load per `HANDOFF_README.md`).  
2. `load_kb("MCRP_3_01A_Rifle_Marksmanship")` in VF Runtime Connect / Engine.  
3. Prefer questions grounded in marksmanship fundamentals — cite chunks; verify residual.  
4. Chat LLM is **not** bundled.

## Feedback

Open an issue on [vf-brick-library](https://github.com/CMiller56/vf-brick-library) with brick name + failing query.

Built: 2026-07-30 21:04:54 · 100-brick B2 · figure-magazine profile=gov_fm · MCRP 3-01A

## Residual craft (post-build)

- Finish **A3c** EOL soft-hyphen join (Distiller manuals) applied on re-export.  
- Finish **A3d** TOC leader mute: **3** pure TOC chunks off RAG.  
- Active muted after craft: **106** of 274 (figure shells / plot debris / TOC).  
