# The Electrical News (1923)

**Brick id (folder):** `Electrical_News_1923`  
**Chunks:** 2903  
**Muted / exclude_from_rag:** 2  
**Package:** `Electrical_News_1923_portable.zip` (12493 KB)  
**Search smoke:** PASS  
**Public gallery:** **yes** (US public domain for 1923 publication; **not certain outside the US**)  
**Family:** historical_periodical  
**Rights class:** public_domain_us (ex-US uncertain)

## Purpose

*The Electrical News* (1923) — Canadian / North American electrical trade periodical from the Internet Archive haul. Packaged as a **large single-brick periodical dogfood** for residual-honest retrieval: multi-column ads, trade articles, conventions, product copy, and OCR/print-era debris at magazine scale (~1096 pages → 2903 chunks).

Factory also produced a **multi-brick split plan** (audit ≈ 4 parts). This library unit is the **single mega-brick stress** path — one bounded package, honest residual, not four sibling bricks.

## Related bricks

- [`TM_11_666_Antennas_Radio_Propagation`](../TM_11_666_Antennas_Radio_Propagation/) — historical RF technical manual (USG; different genre)
- Multi-brick P1–P4 siblings are **not** published here yet (Constructor / federation optional later)

## Audience

Historians of electrical power and trade press; integrators stress-testing **periodical + multi-column + ad density** OCR at ~3k chunks; air-gap / local-LLM users who want attributed 1920s electrical trade vocabulary offline.

## Sources

- **Primary:** *The Electrical News* (1923 volume / compilation as ingested).  
- File as ingested: `electricalnews1923.pdf` (~1096 pages; IA-style scan + mixed extract: PyMuPDF primary, Docling triage, Camelot tables).  
- Internet Archive public haul for factory dogfood and public brick packaging.

## License / rights

**United States:** treated as **public domain** for this **1923** publication (pre-1929 US PD rule of thumb for published works; periodical content as packaged here). This brick is a **derived retrieval package** only — not a claim of clean title on every advertisement, photo credit, or foreign contribution inside the volume.

**Outside the United States:** **not certain.** Term and national treatment of 1920s periodicals vary by jurisdiction. Confirm local copyright rules before redistributing or commercial reuse outside the US. Original scan remains system of record when you hold a copy.

- Do not treat trade ads or technical claims as current engineering authority.  
- Derived package for retrieval demo / craft stress — not official publisher redistribution.

## Known limits / residual honesty

- Recut 2026-08-19: outline 158/174 (chunk_headings); tables=61 (camelot=13, md=48); SECURITY_REPORT.md in ZIP

- Recut 2026-08-17: false-headings procedure_or_biblio=206; outline 158/174 (chunk_headings); SECURITY_REPORT.md in ZIP

- **~1077 soft residual issues** at ship (no high-priority open) — periodical density, figure shells, multi-column debris expected.  
- Soft-hyphen residual: **0** active after finish Bag A (A3b joined ~1511 soft-hyphen chunks).  
- Index mute (A3d): **2** TOC/index debris off RAG.  
- Finish: 2996 → 2903 chunks (near-dup drop + soft wrap reflow).  
- **Text-first portable** (`image_policy=none`) so the ZIP stays under GitHub soft max; figure images not in package.  
- Quality smoke PASS; generic smoke queries often hit ad/figure headings — prefer domain queries (convention, transformers, trade papers).  
- Audit recommended multi-brick (~4); this unit is single-brick stress.  
- Sidecars: `finish_report.json`, `soft_hyphen_residual.json`, `ship_check.json`, `search_smoke.json`, `KBM_FACTORY_ELECTRICAL_NEWS_LOG.json`.

## How to use

1. Unzip `Electrical_News_1923_portable.zip` (or load per `HANDOFF_README.md`).  
2. `load_kb("Electrical_News_1923")` in VF Runtime Connect / Engine.  
3. Prefer historical trade / electrical industry queries — cite chunks; treat ads as period artifacts.  
4. Chat LLM is **not** bundled.

## Feedback

Open an issue on [vf-brick-library](https://github.com/CMiller56/vf-brick-library) with brick name + failing query.

Built: 2026-07-31 18:52:56 · Factory dogfood · text-first portable · US PD / ex-US uncertain  
