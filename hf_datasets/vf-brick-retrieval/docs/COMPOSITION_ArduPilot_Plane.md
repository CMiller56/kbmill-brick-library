# Composition note — ArduPilot Plane shelf

**Status:** Public composition example (2026-08-12)  
**Principle:** *Compose, don’t melt.* Separate bricks for separate jobs; route queries by facet.

This is the flagship **multi-brick** story in the library: one vehicle domain, several residual-honest packages, not one mega-index of “all of ArduPilot.”

---

## The shelf (core trio)

| Brick | Chunks (approx.) | Source shape | Job for the LLM |
|-------|-----------------:|--------------|-----------------|
| [`ArduPilot_Plane`](bricks/ArduPilot_Plane/) | 335 | Ops wiki / HTML | **How** — modes, setup, failsafe, TECS narrative, first flight |
| [`ArduPilot_Plane_Params`](bricks/ArduPilot_Plane_Params/) | 1781 | Structured parameter list | **What** — each param name, meaning, values |
| [`ArduPilot_MAVLink`](bricks/ArduPilot_MAVLink/) | 310 | Protocol / message docs | **Wire** — messages, fields, integration |

Optional same-family facets (not required for the core story):

| Brick | Job |
|-------|-----|
| [`ArduPilot_MissionPlanner`](bricks/ArduPilot_MissionPlanner/) | GCS UI / Mission Planner procedures |
| [`CubePilot_FC`](bricks/CubePilot_FC/) | Flight-controller hardware manuals |
| [`DroneCAN`](bricks/DroneCAN/) / [`UAVCAN_cvra`](bricks/UAVCAN_cvra/) | Bus / peripheral protocol facets |

---

## Why not one melted brick?

| Melted “all ArduPilot” dump | Composed shelf |
|----------------------------|----------------|
| Ops prose and param tables compete in one ranking | Route ops questions → Plane; param questions → Params |
| Protocol noise dilutes flight-mode answers | Protocol lives in MAVLink |
| Residual profile becomes unreadable | Each brick has its own residual card |
| Hard to mute junk without nuking good pages | Facet-level mute / soft residual |

LLM-native packaging means the **model is the primary user** of each package. Composition is how you scale a domain without becoming an unbounded dump.

---

## Routing sketch (for loaders / agents)

```text
User question
    │
    ├─ "what does PARAM_X mean / range / units?"     → ArduPilot_Plane_Params
    ├─ "how do I set up FBWA / failsafe / TECS?"      → ArduPilot_Plane
    ├─ "what is HEARTBEAT / message field?"          → ArduPilot_MAVLink
    ├─ "how do I do this in Mission Planner?"        → ArduPilot_MissionPlanner
    └─ ambiguous → search Plane first; if hit is thin, Params; cite brick id
```

**Human custody:** routing can be soft (keywords + brick craft notes) or hard (user selects shelf). Do not invent param values not present in the Params brick.

---

## Residual profiles (why developers care)

| Brick | Residual character |
|-------|-------------------|
| **Plane (ops)** | Cleaner technical prose; soft residual possible; public **20-question** retrieval demo |
| **Plane_Params** | **Large soft residual by design** (table density, repeated structure); still retrieval-useful; public **15-question** demo |
| **MAVLink** | Protocol facet; soft residual possible; retrieval smoke optional later |

Dense param tables are a **different stress** from wiki ops or OCR history (Skylab). That is intentional diversity.

---

## Published retrieval evidence

| Demo | Questions | Machine JSON |
|------|----------:|--------------|
| [RETRIEVAL_DEMO_ArduPilot_Plane.md](RETRIEVAL_DEMO_ArduPilot_Plane.md) | 20 | [demos/ardupilot_plane_eval.json](demos/ardupilot_plane_eval.json) |
| [RETRIEVAL_DEMO_ArduPilot_Plane_Params.md](RETRIEVAL_DEMO_ArduPilot_Plane_Params.md) | 15 | [demos/ardupilot_plane_params_eval.json](demos/ardupilot_plane_params_eval.json) |

HF retrieval set today ships the **ops** facet (`ardupilot_plane` config). Params can be added as a second ArduPilot config later if needed; full portable ZIPs remain the leave-behind.

Hub: [CMiller/kbmill-brick-retrieval](https://huggingface.co/datasets/CMiller/kbmill-brick-retrieval) · Contract: [BRICK_SPEC.md](BRICK_SPEC.md)

---

## Loader checklist (integrators)

1. Unzip each `*_portable.zip` you need (do not require Pro).  
2. Load only the facets your route selected.  
3. Respect `muted` / `exclude_from_rag` when present.  
4. Prefer brick embeddings + same embed family for ranking; re-embed only with a named model if comparing.  
5. Cite **brick + chunk_id** (and heading when present).  
6. Read craft / library cards for limits — especially Params soft residual.

---

## What this is not

- Not a full ArduPilot mirror or flight-critical authority  
- Not a promise that composed retrieval beats every embedder  
- Not legal or safety advice — upstream docs remain the operational source of truth  

---

*Composition example for KBMill portable bricks — CMiller56 / kbmill.com**
