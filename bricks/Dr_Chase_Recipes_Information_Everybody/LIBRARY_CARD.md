# Dr. Chase's Recipes, or Information for Everybody

**Brick id (folder):** `Dr_Chase_Recipes_Information_Everybody`  
**Chunks:** 1099  
**Muted / exclude_from_rag:** 405  
**Package:** `Dr_Chase_Recipes_Information_Everybody_portable.zip` (19079 KB)  
**Search smoke:** PASS  
**Public gallery:** **yes** (public domain historical work)  
**Family:** historical_practical  

## Purpose

Nineteenth-century practical handbook attributed to **A. W. Chase** — household and commercial recipes across medical, merchants/grocers, cooking, and related departments. Packaged for residual-honest retrieval and **pre-digital OCR stress** (scan + text layer).

## ⚠️ Not medical advice

**Do not** use this brick for diagnosis, treatment, dosing, or any health decision. Content is **historical** and often unsafe by modern standards. Same residual honesty bar as other historical medical-adjacent bricks.

## Related bricks

- [`ST_31_91B_SF_Medical`](../ST_31_91B_SF_Medical/) — historical medical field text (USG; different era; also not clinical advice)

## Audience

Historians, curiosity readers, and integrators testing **19th-century OCR books** (department structure, index pages, typography residual) for offline RAG — not practitioners.

## Sources

- **Primary:** Chase, A. W. (Alvin Wood), 1817–1885 — *Dr. Chase's recipes, or, Information for everybody…*  
- File as ingested: `drchasesrecipeso00chas_1.pdf` (~394 pages; IA-style scan).  
- Public-domain / Internet Archive haul for factory dogfood and public brick packaging.

## License / rights

**Public domain** in the United States (19th-century work; author died 1885). This brick is a **derived retrieval package** only. Confirm local rules if redistributing outside the US. Original scan remains system of record when you hold a copy.

## Known limits / residual honesty

- Recut 2026-08-19: false-headings figures=2; outline 12/16 (chunk_headings); tables=51 (camelot=19, md=32); SECURITY_REPORT.md in ZIP

- OCR text layer on image pages — expect garble, index/TOC debris, soft hyphens (finish A3c), figure shells.  
- Built with **`figure-magazine --profile hard_pdf`**.  
- Recut **2026-08-17:** `repair-false-headings` — 387 “Figures” + 318 book-title headings cleared; departments now carry the outline (220 sections).  
- Soft ship gates may remain.  
- Other gallery ZIPs still need this remill (enzyme is on the plant; this ZIP is the first public test).  
- Sidecars: `finish_report.json`, `figure_magazine.json`, `job_b_recheck.json`, `_full_build.log`.

## How to use

1. Unzip `Dr_Chase_Recipes_Information_Everybody_portable.zip` (or load per `HANDOFF_README.md`).  
2. `load_kb("Dr_Chase_Recipes_Information_Everybody")` in VF Runtime Connect / Engine.  
3. Prefer historical / curiosity queries — **cite chunks; never treat as clinical**.  
4. Chat LLM is **not** bundled.

## Feedback

Open an issue on [kbmill-brick-library](https://github.com/CMiller56/kbmill-brick-library) with brick name + failing query.

Built: 2026-07-31 08:49:07 · 100-brick B2 · figure-magazine profile=hard_pdf · Dr. Chase

## Residual craft (post-build)

- **Index mute (A3d):** 11 INDEX/PAGE. OCR pages off RAG.  
- **Heading sanitize (A2b):** OCR first-line / overlong recipe headings replaced (prefer DEPARTMENT labels or book title fallback).  
- Figure shells muted earlier in magazine.  
- Active muted after craft: **411** of 1026. **Not medical advice.**  
