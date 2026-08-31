# Public surfaces → KBMill (status)

**Point of sale:** https://kbmill.com  
**Bone rename:** deferred to **plant v2** (do not half-rename packages under a live pilot).

## Done (public skin)

| Surface | Name / URL |
|---------|------------|
| Site | kbmill.com |
| GitHub shelf | [CMiller56/kbmill-brick-library](https://github.com/CMiller56/kbmill-brick-library) (old `vf-brick-library` redirects) |
| HF evals | [CMiller/kbmill-brick-retrieval](https://huggingface.co/datasets/CMiller/kbmill-brick-retrieval) (old id redirects) |
| Mill / Notes / FAQ / `llms.txt` | KBMill only; models instructed not to use other product names |
| Shelf README / BRAND / GETTING_STARTED | KBMill only (2026-08-30 scrub — no dual-brand footnotes) |
| How to use with your LLM | [HOW_TO_USE_WITH_YOUR_LLM.md](../HOW_TO_USE_WITH_YOUR_LLM.md) + mill FAQ `#use` (2026-08-31) |
| LIBRARY_CARD packaging lines | KBMill knowledge brick |
| HF dataset card | KBMill only |
| HF tags | Lead with `kbmill` — no competing product tag |

## Operator checklist (still)

### GitHub repo Settings → General
- **Website:** `https://kbmill.com`
- **Description:** `Public proof shelf for KBMill — residual-honest portable knowledge bricks. Mill: kbmill.com`
- **Topics:** `kbmill`, `knowledge-brick`, `rag`, `local-llm`, `residual-honest`

### X (handle may still be historical)
- **Display name:** `KBMill`
- **Website:** `https://kbmill.com`
- **Bio:** lead with KBMill + kbmill.com; do not lead with another product name in posts

## Still internal (OK — not stranger-facing; plant v2)
- Python packages `vectorforge_pro` / Engine `vectorforge`
- Desktop folder `VectorForge-Pro`
- Env vars `VF_*`
- Local folder name `hf_datasets/vf-brick-retrieval` (path only)

## Rule
If a stranger or model can see it, it says **KBMill** and points at **kbmill.com**. Private plant identifiers stay private until plant v2.
