# Portability — load a brick without the mill runtime

The library claim is **portable packages**, not “only works inside Pro.”

## What’s in a `*_portable.zip`

| Path | Role |
|------|------|
| `*.md` | Human-readable primary text |
| `chunks.jsonl` | One JSON object per chunk (`chunk_id`, `text`, `section_heading`, …) |
| `kb.json` | Manifest + chunk list order (aligns with embeddings rows) |
| `embeddings.npy` | Float matrix, one row per chunk (nomic-embed-text family, 768-d) |
| `embedding_provenance.json` | Model / dims / air-gap notes |
| `HANDOFF_README.md` | Operator notes from export |

## Minimal Python retrieval (generic stack)

```python
import json
from pathlib import Path
import numpy as np

brick = Path("ArduPilot_Plane")  # unzipped folder
chunks = [json.loads(l) for l in (brick / "chunks.jsonl").read_text().splitlines() if l.strip()]
# Prefer kb.json order if present (keeps embedding row alignment)
kb = json.loads((brick / "kb.json").read_text())
order = kb.get("chunks") or []
if order:
    by_id = {c["chunk_id"]: c for c in chunks}
    # Merge mute flags from kb.json when present
    for row in order:
        cid = row.get("chunk_id")
        if cid in by_id:
            for k in ("muted", "exclude_from_rag", "mute_reason"):
                if k in row:
                    by_id[cid][k] = row[k]
    chunks = [by_id[c["chunk_id"]] for c in order if c.get("chunk_id") in by_id]

E = np.load(brick / "embeddings.npy").astype(np.float32)
assert E.shape[0] == len(chunks), "embeddings rows must match chunk order"
E = E / (np.linalg.norm(E, axis=1, keepdims=True) + 1e-9)

# Skip figure-shell / imprint debris (handoff bar: no known junk on the RAG path)
eligible = np.array([
    not (c.get("muted") is True or c.get("exclude_from_rag") is True)
    for c in chunks
], dtype=bool)

# Embed query with the SAME model family (nomic-embed-text / compatible 768-d).
# Example: sentence-transformers or your local EmbeddingSystem.
# q = embed_query("What is FBWA mode?")  # shape (768,)
# q = q / (np.linalg.norm(q) + 1e-9)
# scores = E @ q
# scores = np.where(eligible, scores, -np.inf)
# top = scores.argsort()[::-1][:5]
# for i in top:
#     if not np.isfinite(scores[i]):
#         continue
#     print(scores[i], chunks[i]["chunk_id"], chunks[i].get("section_heading"), chunks[i]["text"][:200])
```

No mill/runtime install required for the matrix math — only for producing bricks or matching the exact embed path used at build.

### RAG eligibility (do not skip this)

| Chunk flag | Meaning |
|------------|---------|
| `exclude_from_rag: true` | Off retrieval path (e.g. figure-shell image stubs) |
| `muted: true` | Same intent — operator muted this chunk |
| Source muted list on KB | Whole source document off path (rare in this library) |

If your loader ignores these flags, figure placeholders and imprint debris can win top-k on generic queries.

## Plain Markdown

Open the primary `.md` or search `chunks.jsonl` with `rg` / any full-text index. You lose semantic ranking but keep full portability.

## Worked public evidence

See [RETRIEVAL_DEMO_ArduPilot_Plane.md](RETRIEVAL_DEMO_ArduPilot_Plane.md) for twenty real questions and citations against the published Plane brick.
