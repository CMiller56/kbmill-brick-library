# Getting started — drop in a brick (5–15 minutes)

No account. No cloud dependency. Chat LLM is **not** bundled.

## 1. Pick a brick

| If you want… | Start with |
|--------------|------------|
| Measurable demo (20 Q + citations) | **[ArduPilot_Plane](bricks/ArduPilot_Plane/)** + **[RETRIEVAL_DEMO](RETRIEVAL_DEMO_ArduPilot_Plane.md)** |
| Large parameter reference | **[ArduPilot_Plane_Params](bricks/ArduPilot_Plane_Params/)** |
| Protocol | **MAVLink**, **DroneCAN**, **UAVCAN_cvra** |
| Technical PDF paper | **[Advanced_Rockets](bricks/Advanced_Rockets/)** |

Index: [`catalog.json`](catalog.json). Rights + residual: each brick’s `LIBRARY_CARD.md`.
**Contract:** [BRICK_SPEC.md](BRICK_SPEC.md).

## 2. Unzip

```bash
cd bricks/ArduPilot_Plane
unzip ArduPilot_Plane_portable.zip -d ArduPilot_Plane
cd ArduPilot_Plane
ls   # kb.json  chunks.jsonl  embeddings.npy  HANDOFF_README.md  *.md …
```

You need at least: primary `*.md`, `craft_brief.md` (when present), `chunks.jsonl`, `kb.json`, `embeddings.npy`, `HANDOFF_README.md`.

## 3a. Chat with your LLM (start here — no code)

**Full walkthrough:** **[HOW_TO_USE_WITH_YOUR_LLM.md](HOW_TO_USE_WITH_YOUR_LLM.md)**

1. Open the primary `*.md` and skim `craft_brief.md`.  
2. In ChatGPT / Claude / Grok / Gemini / Open-WebUI / LM Studio / etc.: **attach** those files or **paste** a section + the craft brief.  
3. Ask questions; ask the model to answer only from the package.

That is enough for a first real test in *your* environment. The ZIP does not auto-wire itself — someone opens the files once.

## 3b. Plain text search (zero ML)

```bash
rg -n "FBWA|first flight" chunks.jsonl | head
```

Good for reading and grep. No semantic ranking.

## 3c. Semantic rank / RAG without the mill runtime

Same embed family as the brick (**nomic-embed-text**, 768-d). See **[PORTABILITY.md](PORTABILITY.md)** for a minimal cosine sketch.

**RAG path honesty:** skip chunks with `exclude_from_rag: true` or `muted: true` (figure-shell / imprint debris). Your ranker should filter them the same way a production loader would.

## 3d. Optional — KBMill plant operators only

If you already run **KBMill plant tooling** locally, Connect is an optional **read-only** MCP surface. Strangers do **not** need this — use §3a–3c.

There is **no** public `pip install` Connect package. Unpack the ZIP first. Exact CLI/module paths ship with the plant install docs — not repeated here so public copy stays **KBMill-only**.

## 4. Read craft notes first

| File | Why |
|------|-----|
| `LIBRARY_CARD.md` (beside the zip) | Purpose, rights, residual one-liner |
| `HANDOFF_README.md` (inside zip) | Operator bar, cleanliness |
| `craft_brief.md` (if present) | Answer policy for this brick |

## 5. Feedback (this is the point)

Open an [Issue](https://github.com/CMiller56/kbmill-brick-library/issues) with:

1. Brick name  
2. Query  
3. Expected vs got (chunk id / heading if possible)  
4. Loader (Connect / custom / Markdown only)

Template: [`.github/ISSUE_TEMPLATE/brick_feedback.md`](.github/ISSUE_TEMPLATE/brick_feedback.md)

Honest criticism beats polite praise. Packs get re-cut as the factory improves.

## Shelf map (ArduPilot family)

```text
ArduPilot_Plane          ← ops / first flight / modes
ArduPilot_Plane_Params   ← parameter reference (large)
ArduPilot_MAVLink        ← messages / protocol
ArduPilot_MissionPlanner ← GCS UI/docs
CubePilot_FC             ← hardware
DroneCAN / UAVCAN_cvra   ← bus protocols
```

Compose multiple bricks for a vehicle stack — one zip is not the entire wiki.

## What is *not* published here

Commercial textbooks (e.g. radar handbooks dogfooded privately for stress) and customer bricks stay private. The front-page hard-corpus screenshot shows **difficulty**, not a downloadable commercial book.
