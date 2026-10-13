# What these prints actually do (119th Congress, 16 Sept 2026)

**Type:** workbench note · **synthesis** (not statute, not opinion)  
**Shelf date:** 2026-09-16 · **Catalog:** `/bills.json` schema_v3  
**Shelf counts:** **11 bill instruments** + **1 synthesis compare** + **this workbench note** + **1 hole card** — synthesis is never a 12th bill.  
**Rule:** Official text stays at GovInfo / Congress.gov. KBMill is the prep layer. Compare / this note are labeled synthesis. Walk the chain.

---

## 1. Scope and holes

**On the shelf today (11 introduced prints, milled as version bricks):**

| version_id | bill_family | Short title | Print | comparison_status |
|---|---|---|---|---|
| `119-s-2938-is` | `AI_RISK_EVALUATION_2025` | AI Risk Evaluation Act of 2025 | IS | IS_only |
| `119-s-5061-is` | `SECURE_AI_DEVELOPMENT_2026` | Secure A.I. Development Act of 2026 | IS | IS_only |
| `119-s-4441-is` | `CREATE_AI_2025` | CREATE AI Act | IS | IS_companion_to_IH |
| `119-hr-2385-ih` | `CREATE_AI_2025` | CREATE AI Act of 2025 (House) | IH | IH_only |
| `119-hr-9925-ih` | `FRONTIER_ACT_2026` | FRONTIER Act | IH | IH_only |
| `119-hr-10152-ih` | `OPEN_SOURCE_AI_LEADERSHIP_2026` | Open-Source AI Leadership Act | IH | IH_only |
| `119-hr-9917-ih` | `AI_KILL_SWITCH_2026` | AI Kill Switch Act | IH | IH_only |
| `119-hr-9477-ih` | `AI_INCIDENT_REPORTING_2026` | AI Incident Reporting Act | IH | IH_only |
| `119-hr-5388-ih` | `AI_LEADERSHIP_UNIFORMITY_2025` | American AI Leadership and Uniformity Act | IH | IH_only |
| `119-hr-9442-ih` | `AI_DATA_CENTER_MORATORIUM_2026` | AI Data Center Moratorium Act | IH | IH_companion_to_IS |
| `119-s-4214-is` | `AI_DATA_CENTER_MORATORIUM_2026` | AI Data Center Moratorium Act | IS | IS_companion_to_IH |

**None of these are enacted law.** IS/IH = introduced prints only.  
**Document class:** every row above is `instrument_type: bill`, `branch: legislative`, `official_text: true`, `authority_level: introduced_print`.

### Included / excluded / unavailable

| Disposition | Item | Rationale |
|---|---|---|
| **Included** | 11 version bricks above | Official introduced prints milled from GovInfo HTML |
| **Unavailable** | Thune–Klobuchar–Cruz 2026 draft | **No official text** — hole card only: `/bills/draft-unofficial-thune-klobuchar-cruz-2026/` (`official_text: false`) |
| **Unavailable** | H.R. 2385 **RH** | Exists on GovInfo; **not** this shelf’s House CREATE brick (IH only). Same `bill_family`, different `version_id` |
| **Unavailable** | AIRIA (118th) | Ancestor talk in press; separate congress if milled later — not a 119th substitute |
| **Excluded** | News recaps as “bill text” | Press is not primary text; would fake a brick |
| **Excluded** | Congress firehose of every AI mention | Curated starter for **mechanism** comparison, not a dump |
| **Excluded (pending class)** | EOs / agency rules / court opinions | Useful later; keep in separate `instrument_type` indexes — do not mix into bill bricks |
| **Excluded** | Treating IH and RH as one document | Forbidden — see `bill_families` / `comparison_status` |

Machine copy: `inclusion_register` + `holes_and_absences` + `bill_families` in `/bills.json`.

---

## 2. Mechanism table

Topic words out. Mechanisms in. Fields align with `/bills.json`. Section cites live in compare + each brick’s `section_cites`.

| version_id | Covered (one line) | Trigger | Agency | Open weights | Pre-release gate | Preemption | Enforcement |
|---|---|---|---|---|---|---|---|
| `119-s-2938-is` | “Advanced AI system” (compute >10^26 FLOPs) — SEC. 3 | Definitional compute gate; program duties — SEC. 5 | **DOE** Evaluation Program — SEC. 5 | Not center | Not a license gate — **gov testing program** | Silent / not headline | Fine language — SEC. 4 |
| `119-s-5061-is` | AI systems; frontier models in registry language — SEC. 2/4 | Incidents; public frontier models | **NIST / Commerce** path — SEC. 3–4 | Not center | Registry / tracking — not IVO license | Silent / not headline | Process-oriented (cite SEC. 4–7) |
| `119-s-4441-is` | NAIRR users / research resource — SEC. 2 | Eligibility for access | **NSF / Initiative** NAIRR | Not an open-weight code | N/A (research access) | Silent / not headline | Program establishment |
| `119-hr-2385-ih` | NAIRR (House IH) — SEC. 3 | Eligibility for access | NSF / operating entity / PMO | Not an open-weight code | N/A (research access) | Silent / not headline | Program establishment · **IH ≠ RH** |
| `119-hr-9925-ih` | Frontier models; very large frontier developers — SEC. 2 | Compute + commercial tiers | **Commerce Under Secretary** + **IVOs** — SEC. 2–5 | Cite before claiming carve-outs | Developer duties + **independent verification** — SEC. 4–5 | SEC. 9 | Civil penalties; SEC. 8 emergency orders |
| `119-hr-10152-ih` | Open / qualified open models — SEC. 5 | Definitional | **Secretary of Commerce** — SEC. 2–3 | **Center** — SEC. 2/4/5; SEC. 4 does **not** authorize ban | Not a pre-approval regime | Silent / not headline | Support statute (anti-ban construction) |
| `119-hr-9917-ih` | Covered entity / covered technology (DHS rule) — SEC. 2 | Covered incident | **DHS** (+ Commerce/DNI on orders) | Not center | **Shutdown capability** + graduated corrections — SEC. 2 | Silent / not headline | Civil penalty up to $2M/day (IH text) |
| `119-hr-9477-ih` | Covered models / developers (Commerce designates) — SEC. 2 | Regulatory thresholds (NS/public safety) | **Commerce** | Not center | **Incident reports** to Commerce — SEC. 2 | Silent / not headline | Penalty / compel language in print |
| `119-hr-5388-ih` | States (moratorium on enforcing AI regs) — SEC. 6 | 5-year period from enactment | White House Action Plan to Congress — SEC. 5 | Not center | N/A | **Temporary 5-year state moratorium** — SEC. 6 | Moratorium on state enforcement |
| `119-hr-9442-ih` / `119-s-4214-is` | AI data centers; compute hardware exports — SEC. 3–4 | Until specified federal laws enacted | **Commerce** (exports), **DOE** (reports) | Not center | Construction pause — not model license | Not state-AI-law preemption | Export controls + reporting |

Full auditable matrix: `/bills/compare-ai-bills-119/compare.md`.

---

## 3. Public sentence vs print

Method only — three pairs. Public claim in a few words; print cite with `version_id` + section. If silent, say silent.

### A. “Kill switch”

- **Public talk:** headlines about a government “kill switch” for AI.  
- **Print:** `119-hr-9917-ih` — short title “AI Kill Switch Act”; SEC. 2 shutdown-capability standard and graduated deployment-corrections framework under the Homeland Security Act.  
- **Check:** quote SEC. 2 / nested `SEC. 2220F` in `/bills/hr-9917-ai-kill-switch/brick.md`. Do not import FRONTIER IVO duties into this print.

### B. “Ban open source”

- **Public talk:** fear that Congress will ban open-weight models.  
- **Print:** `119-hr-10152-ih` SEC. 4 — “Nothing in this Act may be construed to authorize the Secretary to ban, restrict, or otherwise make unavailable an open artificial intelligence model…”  
- **Also on shelf:** `119-hr-9925-ih` is a frontier-developer / IVO oversight print — different mechanism; do not collapse into “ban open source” without a section cite.  
- **Hole:** Thune draft — **no print**; do not invent an open-source ban from aides.

### C. “Light touch” / lab-safety evaluation

- **Public talk:** “light touch” standards; labs must evaluate / work with government on safety.  
- **Print (evaluation program):** `119-s-2938-is` SEC. 5 — Secretary of Energy shall establish an Advanced Artificial Intelligence Evaluation Program (testing, red teams, reports).  
- **Print (IVO path):** `119-hr-9925-ih` SEC. 5 — Independent Verification; Under Secretary oversees licensing of IVOs.  
- **Hole:** Thune–Klobuchar–Cruz 2026 — press conflicts on voluntary testing vs government verification; **silent as instrument** until IS exists (`/bills/draft-unofficial-thune-klobuchar-cruz-2026/`).

---

## 4. Debate map → shelf bricks (synthesis)

**Not statute.** Maps press “theories” of the Sept 2026 AI fight onto **prints already on this shelf**. Use for orientation; verify in `brick.md`.

| Debate lane (plain language) | On-shelf print(s) | Mechanism (one line) | Caveat |
|---|---|---|---|
| Pre-market evaluation / “FDA-ish” testing | `119-s-2938-is` | DOE Evaluation Program — SEC. 5 | Not the same as FRONTIER IVO licensing (`119-hr-9925-ih` SEC. 5) |
| Frontier oversight / third-party verifiers | `119-hr-9925-ih` | Commerce Under Secretary + IVOs — SEC. 4–5 | Do not merge with S.2938 “evaluation” |
| Unreleased bipartisan safety package | **Hole card only** — Thune–Klobuchar–Cruz | No print | Highest watch priority; **do not invent text from news** |
| Data-center construction / compute export pause | `119-hr-9442-ih` / `119-s-4214-is` | Construction moratorium + export controls — SEC. 3–4 | Different from **ratepayer** cost-allocation bills (watch) |
| Emergency shutdown / “kill switch” | `119-hr-9917-ih` | **DHS** shutdown capability + orders — SEC. 2 | Press also cites a **Kennedy** Senate UC attempt (company-held switch) — **no milled Senate print yet**; do not collapse into H.R.9917 |
| State-law preemption / uniformity | `119-hr-5388-ih` | 5-year state moratorium — SEC. 6 | FRONTIER has separate SEC. 9 preemption — different statute |
| Open-weight posture | `119-hr-10152-ih` | Commerce support + anti-ban — SEC. 2/4/5 | Not a release ban |

---

## 5. Watch list (not on shelf as instruments)

Structured copy: `/bills.json` → `watch_list`. Disposition = unavailable / optional next mill — **not** invented text.

| Priority | Item | Why watch | Disposition |
|---|---|---|---|
| **P0** | Thune–Klobuchar–Cruz 2026 | Closely watched unreleased package; hole card already live | Mill **IS the hour it drops**; retire/supersede hole card |
| **P1** | Kennedy Senate “kill switch” UC | Press (mid-Sept 2026): company-controlled switch, not government — **mechanism contrast** with H.R.9917 | Hole/watch until S. number + GovInfo HTML; then separate brick |
| **P2** | H.R. 9340 Ratepayer Protection Act | Related **energy/ratepayer** lane (large-load cost allocation); RH exists on GovInfo | Optional mill — **different mechanism** from data-center construction moratorium; keep class = bill |
| **P3** | H.R. 2385 RH | Already tracked (`missing_versions: ["RH"]`) | Optional remill as separate `version_id` |
| **P3** | AIRIA (118th) | Ancestor talk only | Optional ancestor brick — not a Thune substitute |

---

## 6. Document classes (do not collapse)

A bill, executive order, agency rule, committee report, court opinion, and unofficial discussion draft may address the same issue but have different legal status. Schema fields (see `/bills.json` → `document_class_fields`):

```text
instrument_type: bill | executive_order | regulation | court_opinion | report | draft | synthesis
status / instrument_status: introduced | passed | enacted | revoked | proposed | unofficial | …
branch: legislative | executive | judicial | none
authority_level: introduced_print | … | unofficial_draft | kbmill_synthesis
official_text: true | false
```

**Indexes by type** (machine): `instrument_indexes` in `/bills.json`.  
**Human:** `/bills/what-the-prints-say/INDEX_BY_TYPE.md`.

| Class | On shelf now | Rule |
|---|---|---|
| `bill` | 11 version bricks | Official prints; quote `brick.md` |
| `draft` | 1 hole card (Thune) | No `brick.md`; do not invent text |
| `synthesis` | compare + this note | Analytical aid; cite back to sections |
| `executive_order` / `regulation` / `court_opinion` / `report` | 0 | Reserved empty indexes — add as separate classes |

---

## 7. How to use the set

1. Fetch **https://kbmill.com/bills.json** (machine catalog: fields, `policy_actions`, `bill_families`, `section_cites`, `inclusion_register`, hashes) or **https://kbmill.com/bills.txt**.  
2. For each question, open the relevant **`brick.md`** (and `status.md`). Answer **only** from the package.  
3. For cross-bill structure, use **https://kbmill.com/bills/compare-ai-bills-119/compare.md** and **policy_actions.md** — labeled **synthesis v0**; every row should point to `version_id` + section.  
4. **IS/IH ≠ law.** **IH ≠ RH.** Companions share `bill_family` but remain separate bricks.  
5. GitHub mirror (if crawl blocked): `https://github.com/CMiller56/kbmill-brick-library` under `bricks/`. Portable ZIPs on each instrument card.  
6. Hole cards have **no** `brick.md` — do not invent one.  
7. Document-class indexes: `instrument_indexes` / `INDEX_BY_TYPE.md`.

That chain — GovInfo/Congress.gov → mill prep → labeled synthesis → checkable files — is the federated-KB demonstration.
