# ST 31-91B Special Forces Medical Handbook

**Brick id (folder):** `ST_31_91B_SF_Medical`  
**Chunks:** 618  
**Muted / exclude_from_rag:** 63  
**Package:** `ST_31_91B_SF_Medical_portable.zip` (29675 KB)  
**Search smoke:** PASS  
**Public gallery:** **yes** (US Government work)  
**Family:** doctrine / medical  

## Purpose

US Army **Special Forces medical handbook** (ST **31-91B**) — historical field medical reference packaged for residual-honest retrieval and multimodal (text + extracted figures) offline use.

**Not medical advice.** **Not** current clinical protocol. **Not** official Army redistribution or endorsement. For study, history, and factory dogfood of medical field-manual extract.

## Related bricks

- [`FM_3_90_Tactics`](../FM_3_90_Tactics/)
- [`Ranger_Handbook_SH_21_76`](../Ranger_Handbook_SH_21_76/)
- [`Ranger_Handbook_TC_3_21_76`](../Ranger_Handbook_TC_3_21_76/)

## Audience

Students of military medical history, austere-care literature, and integrators testing **medical + figure-heavy** manuals as knowledge bricks.

## Sources

- **Primary:** United States Army — Special Forces medical handbook material published as **ST 31-91B** (scan/IA haul).  
- File as ingested: `st_31-91b-_us_army_special_forces_medical_handbook.pdf` (~210 pages).  
- PDF metadata dates ~1999 production of the scan; treat content as **historical**.

## License / rights

**US Government work.** Works of the US federal government are generally not subject to copyright in the United States (17 U.S.C. § 105). This brick is a **derived retrieval package** — **not** an official DoD/Army product.

- Do not use for clinical decisions; verify against current authoritative medical sources.  
- Confirm local rules if redistributing outside the US.

## Known limits / residual honesty

- Recut 2026-08-19: outline 87/104 (chunk_headings); tables=35 (camelot=0, md=35); SECURITY_REPORT.md in ZIP

- Recut 2026-08-17: outline 173/244 (chunk_headings); SECURITY_REPORT.md in ZIP

- Scan-era PDF: pages are full-page images; **promoted OCR is kept on RAG** after magazine (shell mute must not re-mute promoted bodies).


- May be **scan-era** PDF: OCR promote quality-gated (F1); hollow figure shells muted.  
- Built with **`figure-magazine --profile gov_fm`**.  
- Layout, tables, and illustrations may lose fidelity in plain text.  
- Soft ship gates may remain; high-priority residual cleared when possible.  
- Sidecars: `finish_report.json`, `figure_magazine.json`, `figure_index.json`, `job_b_recheck.json`, `_full_build.log`.

## How to use

1. Unzip `ST_31_91B_SF_Medical_portable.zip` (includes `images/` when present).  
2. `load_kb("ST_31_91B_SF_Medical")` in VF Runtime Connect / Engine.  
3. Prefer retrieval + citation over free-form clinical advice.  
4. Chat LLM is **not** bundled.

## Feedback

Open an issue on [vf-brick-library](https://github.com/CMiller56/vf-brick-library) with brick name + failing query.

Built: 2026-07-30 08:02:39 · 100-brick B2 · figure-magazine profile=gov_fm · ST 31-91B  
