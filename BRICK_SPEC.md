# Knowledge brick specification (public contract)

**Version:** 1.0  
**Date:** 2026-07-30  
**Status:** Public contract for portable bricks in this library and compatible loaders  
**Audience:** Integrators, local/air-gap operators, tool authors — not a Pro desk manual  

**Companions:** [GETTING_STARTED.md](./GETTING_STARTED.md) · [PORTABILITY.md](./PORTABILITY.md) · per-brick `LIBRARY_CARD.md`

---

## 1. What a knowledge brick is

A **knowledge brick** is a **bounded, portable, residual-honest** package of technical knowledge:

| Property | Meaning |
|----------|---------|
| **Bounded** | One curatable unit (not an unbounded RAG dump of a whole domain) |
| **Portable** | A `*_portable.zip` you can unzip, inspect, and rank **without** VectorForge Pro |
| **Residual-honest** | Known limits and muted debris are **visible** — not hidden behind “looks fine” |
| **Retrieval-first** | Designed for search → cite → answer, not paste-the-whole-corpus into every prompt |

A brick is the **smallest unit** of handoff and daily use. Larger topics are **composed** from multiple bricks (e.g. Plane ops + Plane params + MAVLink), not melted into one mega-index.

```text
Program / shelf (many bricks — expected)
  └── Brick  ← atom: build, scrub, ZIP, load, search, cite
```

---

## 2. What a brick is not

- Not a live wiki scrape that silently drifts  
- Not “all of ArduPilot (or any domain) in one vector store”  
- Not a chat LLM product (chat models are **not** bundled)  
- Not a promise that every page of every source OCR’d perfectly  
- Not a substitute for upstream manuals when legal/currency authority matters  

---

## 3. Required package layout (`*_portable.zip`)

After unzip, a library brick is expected to contain at least:

| Path | Role | Required |
|------|------|----------|
| `kb.json` | Manifest + ordered chunk list (alignment with embeddings) | **Yes** |
| `chunks.jsonl` | One JSON object per chunk (`chunk_id`, `text`, …) | **Yes** |
| `embeddings.npy` | Float matrix, **one row per chunk**, same order as `kb.json` chunks | **Yes** |
| `embedding_provenance.json` | Model family, dims, notes | Strongly recommended |
| Primary `*.md` | Human-readable source of truth (rich Markdown) | Strongly recommended |
| `SECURITY_REPORT.md` | In-ZIP security / trust scan for remilled gallery bricks | **Yes** for this library’s remilled shelf |
| `craft_brief.md` | Purpose, limits, answer policy | Strongly recommended (present on remilled gallery ZIPs) |
| `HANDOFF_README.md` | Operator notes from export | Strongly recommended |
| Quality / finish sidecars | e.g. `finish_report.json`, `figure_index.json` | Optional |

**Honesty artifacts (do not invent filenames):** residual honesty is **muted / `exclude_from_rag` flags** plus disclosure on `LIBRARY_CARD.md` / `craft_brief.md`. A separate `residual_board.md` or `MILL_RECEIPT.md` may appear on some cuts — it is **not** required on every ZIP. Prefer naming what is actually in the package.

Beside the ZIP (library shelf, not always inside the zip):

| Path | Role |
|------|------|
| `LIBRARY_CARD.md` | Purpose, **rights**, residual honesty, load tips |
| `catalog.json` (repo root) | Machine index of published bricks |

**Alignment rule:** `embeddings.npy` row *i* must correspond to chunk *i* in `kb.json`’s `chunks` array. Loaders that use only `chunks.jsonl` should re-order to match `kb.json` when both exist.

---

## 4. Chunk contract (minimum fields)

Chunks are retrieval units. Implementations may carry more fields; loaders should tolerate extras.

| Field | Type | Notes |
|-------|------|--------|
| `chunk_id` | string | Stable id (e.g. `chunk-0042`) |
| `text` | string | Body text (Markdown-ish prose) |
| `section_heading` | string | Human section label when known |
| `page_number` | number | When source is paginated |
| `source_document` | string | Provenance |
| `exclude_from_rag` | bool | **Off** the retrieval path when true |
| `muted` | bool | Same intent as exclude (operator mute) |
| `mute_reason` | string | Why muted (figure shell, imprint, …) |
| `extraction_quality` | number | Diagnostic; not a substitute for mute |

Typical body size guidance (not a hard API limit): **~250–512 mean tokens** per chunk after craft; oversized and multi-section debt are finish-time concerns for the manufacturer.

---

## 5. RAG eligibility (mandatory for honest rankers)

At handoff, **known junk should be off the path**, not merely labeled for the model to “be careful.”

| Flag | Loader behavior |
|------|-----------------|
| `exclude_from_rag: true` | **Do not** retrieve or cite in normal search |
| `muted: true` | Treat as off-path (same as exclude) |
| Neither | Eligible for cosine / hybrid rank |

Typical mute classes: figure-shell placeholders, unusable plot OCR, garbled imprint tables, dual-stream debris that cannot be repaired safely.

If your loader **ignores** these flags, hollow image stubs and imprint garbage can win top-k on generic queries. That is a **loader bug**, not a brick feature.

See [PORTABILITY.md](./PORTABILITY.md) for a minimal Python cosine sketch that filters eligibility.

---

## 6. Embeddings

| Item | Public library default |
|------|------------------------|
| **Model family** | `nomic-embed-text` (e.g. nomic-ai/nomic-embed-text-v1.5) |
| **Dimensions** | **768** |
| **Matrix** | `float` rows in `embeddings.npy`, L2-normalize before cosine |
| **Query** | Embed with the **same family** and dim; mismatch → meaningless scores |

Bricks may document alternate embed paths in provenance; this library’s packs ship **nomic 768-d** unless a card says otherwise.

---

## 7. Size bands (chunks)

Chunk count is **design language**, not a hard API max — and **not** a rule against earlier splits.

| Band | Chunks (guide) | Role |
|------|----------------|------|
| **Small / paper-scale** | ~50–200 | Often readable end-to-end; thin modules |
| **Design sweet spot** | **~500–2,000** | Default engagement / SOW unit |
| **Stress / acceptable** | ~2,000–4,000 | Hard-corpus dogfood still **one** brick when one locus |
| **Split** | >~4,000, multi-domain mess, **or earlier when §7a is safe** | Multiple bricks; compose — do not mega-merge |

Examples in this gallery: Plane ops **~335**; Plane params **~1.8k** (large on purpose); field manuals hundreds of chunks with more figure mutes.

### 7a. Process latitude — split when obviously safe

Manufacture may (and should) produce **separate bricks** when the cut is **structurally obvious**. Waiting for ~4k chunks is **not** required.

| **Safe to split (in-spec)** | **Not a free split** |
|----------------------------|----------------------|
| Separate source files / manuals in one drop | Mid-chapter or mid-argument cuts |
| Explicit volumes / parts in the edition | Arbitrary “every N pages” |
| Distinct domains (ops vs params vs protocol) | Split only to dodge embed/VRAM pain |
| Pre-named SOW brick list | Inventing facets with no TOC/file evidence |

Each child brick is a full package (schema, embeds, residual honesty). Cards may name siblings. VRAM/OOM is fixed with **safe reembed / GPU hygiene**, not by inventing splits without a locus boundary.

---

## 8. Multi-brick programs

| Rule | Practice |
|------|----------|
| **One locus per load** | Daily search treats **one** brick as the active set unless you deliberately multi-load |
| **Compose, don’t melt** | Ops + params + protocol stay separate packages |
| **Split early when safe** | Obvious seams → multiple bricks at manufacture (§7a); do not grow one unit past need |
| **Cards name siblings** | `LIBRARY_CARD.md` may point at related bricks |
| **Find/sort across bricks** | Human picks the brick, or a future “Constructor” routes — not one infinite timeline |

Anti-goal: merge every facet into one scrubbable mega-KB “for convenience.” That reintroduces an unbounded worst case and throws away the brick bet.

---

## 9. Residual honesty (LIBRARY_CARD)

Every published brick should say, in plain language:

1. **Purpose** — what it is for  
2. **Rights / license posture** — upstream source and redistribution limits  
3. **Residual** — what still hurts (garble regions, figure mutes, soft gates)  
4. **How to load** — unzip + search or Connect  

Honesty means **limits stay lit**, not that every residual is zero. High-priority retrieval poison (shells, imprint debris) should be muted; soft craft debt may remain and must be disclosed.

---

## 10. Quality posture (manufacturer bar)

What “finished enough for a portable ZIP” means for this library:

| Bar | Intent |
|-----|--------|
| Schema-valid `kb.json` / chunks | Machine-loadable |
| Embeddings aligned to chunk order | Rankable |
| Known hollow / garble **off RAG** | Handoff cleanliness |
| Card + residual one-liner | Human trust |
| Search smoke when claimed PASS | Published demo evidence where linked |

Pro desk tools (timeline, job B, figure magazine) are **how bricks are made**. They are **not** required to *consume* a brick.

---

## 11. Versioning and identity

| Field | Use |
|-------|-----|
| Folder / brick id | Stable name (e.g. `ArduPilot_Plane`) |
| `kb_name` inside `kb.json` | Should match folder when possible |
| `kb_version` / export time | Rebuilds may refresh embeddings and mutes |
| Catalog `updated` | Library shelf date |

Treat a new ZIP as a **new cut** of the same brick id unless the card renames it. Compare residual notes when upgrading.

---

## 12. Interoperability checklist (for your loader)

- [ ] Unzip; require `kb.json`, `chunks.jsonl`, `embeddings.npy`  
- [ ] Order chunks like `kb.json` before applying embedding rows  
- [ ] Filter `muted` / `exclude_from_rag` before top-k  
- [ ] Embed queries with the **same** model family and dim  
- [ ] Cite `chunk_id` + `section_heading` (+ page when present)  
- [ ] Read `LIBRARY_CARD.md` / `HANDOFF_README.md` before trusting answers in production  

Optional: VF Runtime Connect (`load_kb` / `search_kb`) if you already run VectorForge Runtime — still optional.

---

## 13. Rights and redistribution

- Each brick’s **`LIBRARY_CARD.md` is authoritative** for that pack’s rights class.  
- This repository’s public gallery publishes only **rights-clear** external/open sources as stated on cards.  
- US Government works, CC BY-SA wiki material, educational third-party notes, etc. differ — **read the card**.  
- Derived bricks are **not** official endorsement by upstream projects or agencies.  

---

## 14. One-line contract

| Topic | Line |
|-------|------|
| **Unit** | One curatable, portable, clean-enough KB module (the brick). |
| **Package** | ZIP with aligned `kb.json` + `chunks.jsonl` + `embeddings.npy`. |
| **Honesty** | Mute junk off RAG; disclose residual on the card. |
| **Size** | Design ~500–2k chunks; split when multi-domain, unwieldy, **or earlier when seams are obviously safe** (§7a). |
| **Scale** | Compose many bricks; do not mega-merge. |
| **Field use** | Search-first, cite chunk ids; do not dump the whole brick into every prompt. |
| **Pro** | Builds bricks; **loaders** need only this contract + PORTABILITY. |

---

## 15. Worked evidence

- [RETRIEVAL_DEMO_ArduPilot_Plane.md](https://github.com/CMiller56/vf-brick-library/blob/main/RETRIEVAL_DEMO_ArduPilot_Plane.md) — 20 real questions with scores and citations  
- [catalog.json](./catalog.json) — machine index of packs in this shelf  

---

*Public distill of Pro brick doctrine (size, handoff cleanliness, multi-brick composition). Implementation details of the Pro desk are out of scope for this document.*
