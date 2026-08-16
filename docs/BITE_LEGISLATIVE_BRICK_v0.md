# Bite — Legislative brick (US bills / public law)

**Status:** Ready for next session (opened 2026-08-12)  
**Product:** VectorForge brick library · residual-honest packaging demo  
**Depends on:** [BRICK_SPEC.md](../BRICK_SPEC.md) · composition lessons from [COMPOSITION_ArduPilot_Plane.md](../COMPOSITION_ArduPilot_Plane.md)  

---

## 1. Goal

Manufacture **1–3** carefully versioned, residual-honest **US legislative text** bricks that show the packaging method transfers beyond:

- clean ops wiki (ArduPilot Plane)
- dense param tables (Plane_Params)
- OCR history (Skylab)

**One line:** *Bounded legislative snapshot + visible structure residual + not legal advice.*

---

## 2. Why this domain (accept)

| Pro | Note |
|-----|------|
| Clean rights | US government works → generally public domain in the US |
| New residual profile | Cross-refs, definitions, amendment/strike language, nested titles/sections |
| Domain transfer signal | Method not tuned only to manuals / OCR books |
| Audience | Legal/policy RAG, civics tools, gov-facing systems — **if** framing stays technical |

---

## 3. Risks (manage, don’t ignore)

| Risk | Control |
|------|---------|
| Political perception | Select for **structure**, not heat; neutral card language |
| Currency | Frozen snapshot only: bill/congress/stage/date on card |
| Authority confusion | Loud **not legal advice / not operative annotated law** |
| Wrong attention | No “current legislation feed”; no volume play |

---

## 4. Selection criteria (structure over politics)

**Prefer:**

- Clear official source (congress.gov / GPO / enrolled text)
- Interesting structure: long titles, many cross-refs, definitions title, multi-title act
- Stable identity: H.R. / S. number + Congress + stage (introduced / engrossed / enrolled / public law)
- Rights-clear and complete enough to bound

**Avoid (for v0):**

- Bills chosen primarily for partisan controversy
- “Latest everything” scraping
- Partial downloads without stage/date residual
- Multi-bill mega-melt without composition plan

**Volume:** **1 brick first** (or one act + siblings only if composition is obvious). Cap at 3 for this campaign.

---

## 5. Package requirements (every legislative brick)

### 5.1 LIBRARY_CARD (plain, loud)

- Purpose: residual-honest offline retrieval of **this snapshot**
- Rights: US government work / public domain (US) + packaging attribution
- **Version:** bill id, Congress, stage, official retrieval date/URL
- Residual: structure noise, amendment language, what was muted
- **Not legal advice. Not a substitute for counsel. Not current annotated operative law.**
- Pair with ops-style demos only if retrieval smoke exists

### 5.2 Identity / versioning string (example)

```text
H.R. ____, ___th Congress — [as introduced | engrossed | enrolled | Public Law ___-___]
Retrieved: YYYY-MM-DD from [URL]
Brick freeze: same date unless re-manufacture
```

### 5.3 Residual honesty targets

Mute or residual-tag when justified:

- Pure TOC / navigation chrome (if extract noise)
- Duplicate front matter
- Image-only pages without text
- Incomplete amendment tables if unreadable

**Do not** silently “clean” amendment language into smooth prose. That invents statute.

### 5.4 Composition

- One bill/act = one brick unless multi-volume edition forces split (§7a BRICK_SPEC)
- Optional later: “definitions” vs “operative titles” only if structure is obvious — not to dodge size

---

## 6. Deliverables for the bite (session)

| # | Deliverable | Done when |
|---|-------------|-----------|
| 1 | Source chosen + stage/date locked | Written on card |
| 2 | Corpus ingest → brick (Pro manufacture or documented path) | Portable ZIP + card |
| 3 | Residual notes on card | Specific, not boilerplate |
| 4 | Optional: 8–12 query retrieval smoke | Same pattern as Params demo |
| 5 | Library README / catalog row | Linked |
| 6 | Optional HF config | Only after smoke is green |

**Non-goals this bite:** live feed, multi-Congress corpus, HF before smoke, political commentary.

---

## 7. Suggested first-session order

1. Pick **one** bill/act with boring-but-structural interest (or a short public law).  
2. Download official text; record URL + stage + date.  
3. Manufacture brick; residual craft.  
4. LIBRARY_CARD with legal disclaimers.  
5. Thin retrieval demo if time.  
6. Catalog + README pointer.  

Bill shortlist for the session is **operator choice** at start (structure first).

---

## 8. Success criteria

- Someone can open the brick and see **versioned legislative snapshot**, not “the law.”  
- Residual challenges of legislative structure are **visible**.  
- Framing stays **packaging method**, not advocacy.  
- Portable ZIP loads without Pro.

---

*Campaign: residual-honest domain transfer · Not a Congress mirror · Snapshot only · Not legal advice.*
