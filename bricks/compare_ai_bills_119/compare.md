# AI bills comparison v0 — published KBMill shelf only

**Generated:** 2026-09-16 (schema_v3: section cites + bill families) · **Synthesis** (not USG text)  
**Rule:** Distinguish **topic presence** from **policy mechanism**.  
**Prints:** all IS/IH unless noted — **not enacted law**.  
**Audit rule:** every matrix cell should be checkable against `version_id` + section in `brick.md`. Synthesis ≠ statute.

## Instruments in this compare

| Brick slug | Bill | Print | Short title | Sponsors (intro) | Primary mechanism (one line) | Tags |
|---|---|---|---|---|---|---|
| [s-2938-ai-risk-evaluation](https://kbmill.com/bills/s-2938-ai-risk-evaluation/) | S. 2938 | IS 2025-09-29 | AI Risk Evaluation Act of 2025 | Hawley, Blumenthal | **DOE program** offers standardized/classified testing & evaluation of “advanced AI systems”; informs Congress | `model_evaluations` `compute` `national_security` |
| [s-5061-secure-ai-development](https://kbmill.com/bills/s-5061-secure-ai-development/) | S. 5061 | IS 2026-07-21 | Secure A.I. Development Act of 2026 | Warner | **Incident taxonomy + tracking/registry** path (incl. frontier-model registry language at NIST Director) | `safety_incidents` `security_incidents` `frontier_models` `transparency` |
| [s-4441-create-ai](https://kbmill.com/bills/s-4441-create-ai/) | S. 4441 | IS 2026-04-29 | CREATE AI Act | Young, Heinrich, Rounds, Booker | **Research infrastructure (NAIRR)** — access to compute/data/tools for researchers; not a frontier licensing regime | `research_infrastructure` `compute` `funding` |
| [hr-2385-create-ai](https://kbmill.com/bills/hr-2385-create-ai/) | H.R. 2385 | IH | CREATE AI Act of 2025 | Obernolte et al. | **NAIRR research infrastructure** (House IH); companion to S.4441 — do not mix with RH substitute | `research_infrastructure` `compute` `funding` |
| [hr-9925-frontier-act](https://kbmill.com/bills/hr-9925-frontier-act/) | H.R. 9925 | IH 2026-07-23 | FRONTIER Act | Obernolte, Trahan, et al. | **Commerce Under Secretary + IVO licensing**, duties on frontier / very large frontier developers, civil penalties | `frontier_models` `model_evaluations` `transparency` `liability` `preemption` |
| [hr-10152-open-source-ai-leadership](https://kbmill.com/bills/hr-10152-open-source-ai-leadership/) | H.R. 10152 | IH | Open-Source AI Leadership Act | Evans | **Commerce support** for adoption/use of “qualified open models”; foreign-adversary model assessment; SEC. 4 does not authorize ban of open AI models | `open_weights` `transparency` `national_security` |
| [hr-9917-ai-kill-switch](https://kbmill.com/bills/hr-9917-ai-kill-switch/) | H.R. 9917 | IH | AI Kill Switch Act | Lieu, Moran | **DHS** shutdown-capability standard + graduated deployment corrections; orders after covered incident (w/ Commerce/DNI); civil penalties | `safety_incidents` `national_security` `critical_infrastructure` `liability` |
| [hr-9477-ai-incident-reporting](https://kbmill.com/bills/hr-9477-ai-incident-reporting/) | H.R. 9477 | IH | AI Incident Reporting Act | Moran | **Commerce** designates covered models/developers; **mandatory incident reports** to Commerce; enforcement/penalty language | `safety_incidents` `transparency` `national_security` |
| [hr-5388-ai-uniformity](https://kbmill.com/bills/hr-5388-ai-uniformity/) | H.R. 5388 | IH | American AI Leadership and Uniformity Act | Baumgartner | **Temporary 5-year state-law moratorium** on regulating AI models/systems/ADS in interstate commerce (carve-outs); National AI Action Plan | `preemption` `transparency` `standards` |
| [s-4214-ai-data-center-moratorium](https://kbmill.com/bills/s-4214-ai-data-center-moratorium/) | S. 4214 | IS | AI Data Center Moratorium Act | Sanders et al. | **Construction moratorium** on AI data centers until federal AI laws; **Commerce export controls** on compute hardware; DOE reports | `compute` `national_security` |
| [hr-9442-ai-data-center-moratorium](https://kbmill.com/bills/hr-9442-ai-data-center-moratorium/) | H.R. 9442 | IH | AI Data Center Moratorium Act | Ocasio-Cortez et al. | **Construction moratorium** on AI data centers until federal AI laws; **Commerce export controls** on compute hardware; DOE reports | `compute` `national_security` |

## Mechanism matrix (issue × bill) — with section cites

Cells are **claims + cites**. Open the named `brick.md` and verify the section before treating the cell as settled. Silent cells mean “not the center of this print,” not “the print forbids it.”

| Issue | S. 2938 (`119-s-2938-is`) | S. 5061 (`119-s-5061-is`) | S. 4441 (`119-s-4441-is`) | H.R. 9925 (`119-hr-9925-ih`) | H.R. 10152 (`119-hr-10152-ih`) | H.R. 9917 (`119-hr-9917-ih`) |
|---|---|---|---|---|---|---|
| **Covered system** | Advanced AI system (>10^26 FLOPs) — **SEC. 3** | AI + safety/security incidents; frontier registry language — **SEC. 2**, **SEC. 4** | NAIRR research terms — **SEC. 2** | Frontier model (>10^26 FLOPs); very large frontier developer — **SEC. 2** | Open AI model / qualified open model — **SEC. 5** | Covered entity / covered technology (DHS rule) — **SEC. 2** |
| **Primary agency** | **DOE** — **SEC. 5** | **NIST / Commerce** path — **SEC. 3–4** | **NSF / Initiative** NAIRR — **SEC. 2** | Commerce Under Secretary + IVOs — **SEC. 2–5** | Secretary of Commerce — **SEC. 2–3** | **DHS** (+ Commerce/DNI on orders) — **SEC. 2** |
| **Core duty** | Gov testing & evaluation program — **SEC. 5** | Pre-release testing enablement + incident database — **SEC. 3–4** | Establish NAIRR access — **SEC. 2** | Developer duties + IVO verification — **SEC. 4–5** | Support adoption of qualified open models; adversary assessment — **SEC. 2–3** | Maintain **shutdown capability**; graduated corrections — **SEC. 2** / nested `SEC. 2220F` |
| **Threshold / trigger** | Compute gate — **SEC. 3(1)** | Incident events + registry language — **SEC. 2**, **SEC. 4** | NAIRR eligibility — **SEC. 2** | Compute + commercial tiers — **SEC. 2** | Definitional open/qualified open — **SEC. 5** | Covered incident — **SEC. 2** |
| **Enforcement** | Fine language — **SEC. 4** | Process/registry oriented — cite **SEC. 4–7** | Program establishment — **SEC. 2** | Civil penalties; emergency orders — **SEC. 4–5**, **SEC. 8** | Support statute; anti-ban construction — **SEC. 4** | Civil penalty up to **$2,000,000/day** (IH) — **SEC. 2** |
| **Open weights** | Not center | Not center | Research access (not an open-weight code) | Cite before claiming carve-outs — **SEC. 2/4** | **Center** — **SEC. 2**, **SEC. 4**, **SEC. 5** | Not an open-weight promotion statute |
| **Shutdown / stop** | Not center | Not center | Not center | Emergency orders — **SEC. 8** | Limits bans of open models — **SEC. 4** | **Center** — **SEC. 2** |
| **Preemption** | Silent / not headline | Silent / not headline | Silent / not headline | Relationship to state laws — **SEC. 9** | Silent / not headline | Silent / not headline |
| **Research vs regulation** | Evidence for oversight options — **SEC. 2**, **SEC. 5** | Incident governance — **SEC. 3–4** | Capacity-building — **SEC. 2** | Direct frontier oversight — **SEC. 4–5** | Industrial-policy support — **SEC. 2** | Operational control / emergency corrections — **SEC. 2** |

### Extended shelf (same audit rule)

| Issue | H.R. 9477 (`119-hr-9477-ih`) | H.R. 5388 (`119-hr-5388-ih`) | H.R. 9442 / S. 4214 (`119-hr-9442-ih` / `119-s-4214-is`) | H.R. 2385 (`119-hr-2385-ih`) |
|---|---|---|---|---|
| **Covered system** | Covered models/developers (Commerce designates) — **SEC. 2** | AI models/systems/ADS in interstate commerce — **SEC. 2**, **SEC. 6** | AI data centers + compute hardware — **SEC. 3–4** | NAIRR — **SEC. 3** (House IH; **≠ RH**) |
| **Primary agency** | **Commerce** — **SEC. 2** | Action Plan to Congress — **SEC. 5** | Commerce (exports) / DOE (reports) — **SEC. 4** + print | NSF / operating entity / PMO — **SEC. 3** |
| **Core duty** | Report AI incidents — **SEC. 2** | Temporary state-law moratorium — **SEC. 6**; Action Plan — **SEC. 5** | Construction pause — **SEC. 3**; export controls — **SEC. 4** | Establish NAIRR — **SEC. 3** |
| **Threshold / trigger** | Regulatory thresholds (NS/public safety) — **SEC. 2** | 5-year period from enactment — **SEC. 6** | Until specified federal laws enacted — **SEC. 3** | Eligibility — **SEC. 3** |
| **Enforcement** | Penalty / compel language — **SEC. 2** | Moratorium on state enforcement — **SEC. 6** | Export controls + reporting — **SEC. 4** | Program establishment — **SEC. 3** |
| **Preemption** | Silent / not headline | **Center** — **SEC. 6** (carve-outs same section) | Not state-AI-law preemption | Silent / not headline |

Machine copy of cites: each brick’s `section_cites` in `/bills.json`. Families: `bill_families`.

## Version families (do not silently merge)

| bill_family | On shelf | Not on shelf / caution |
|---|---|---|
| `CREATE_AI_2025` | `119-hr-2385-ih`, `119-s-4441-is` (companions) | `119-hr-2385-rh` exists on GovInfo — **IH_only** on this shelf |
| `AI_DATA_CENTER_MORATORIUM_2026` | `119-hr-9442-ih`, `119-s-4214-is` | Quote each chamber’s brick separately |
| Others | Single introduced print each | See `comparison_status` on the brick |

## Topic presence ≠ same policy

| Shared topic word | Different mechanisms on this shelf |
|---|---|
| “Evaluation” / “testing” | S. 2938 = DOE-run evaluation program. FRONTIER = developer duties + licensed IVOs. Not the same. |
| “Frontier model” | S. 5061 uses registry language. FRONTIER defines frontier model + developer tiers + IVO oversight. |
| “AI safety” | S. 5061 defines safety vs security **incidents**. S. 2938 focuses adverse-incident likelihood via testing. CREATE AI builds research capacity. |
| “Compute” | S. 2938 and FRONTIER both use **10^26** FLOPs-style gates (different defined terms). CREATE AI is about **providing** research compute via NAIRR. |
| “Kill switch” / shutdown | H.R. 9917 = DHS shutdown-capability + orders. FRONTIER has separate emergency/restriction tools — different statute and agency path. Do not merge.
| “Open” / open weights | H.R. 10152 **defines** open AI model (public weights or open license) and qualified open model; Commerce support + anti-ban rule. FRONTIER/S.2938 are not open-weight promotion statutes — do not conflate. |

## Section-level schema (partially filled in v0.1)

Matrix rows above + per-brick `section_cites` in `/bills.json` are the first pass. Fuller per-section records still reserved:

```text
bill_id:
version_id:
bill_family:
section:
topic:
operative_action:
affected_entities:
responsible_agency:
trigger_or_threshold:
enforcement:
exceptions:
source_location:   # brick slug + heading
```

## Honest limits (GPT-6.6 / Grok)

- **Not** a representative sample of all congressional AI legislation.  
- **No** full text history yet (IH/IS only per brick; RH for H.R. 2385 not milled).  
- Section cites cover the **mechanism matrix**, not every operative subsection.  
- Executive orders / rules / opinions are **separate instrument classes** (indexes reserved empty).  
- Compare and the workbench note are **synthesis** — not statute.

## Cite the instruments

- S. 2938: https://kbmill.com/bills/s-2938-ai-risk-evaluation/brick.md  
- S. 5061: https://kbmill.com/bills/s-5061-secure-ai-development/brick.md  
- S. 4441: https://kbmill.com/bills/s-4441-create-ai/brick.md
- H.R. 2385: https://kbmill.com/bills/hr-2385-create-ai/brick.md  
- H.R. 9925: https://kbmill.com/bills/hr-9925-frontier-act/brick.md
- H.R. 10152: https://kbmill.com/bills/hr-10152-open-source-ai-leadership/brick.md
- H.R. 9917: https://kbmill.com/bills/hr-9917-ai-kill-switch/brick.md
- H.R. 9477: https://kbmill.com/bills/hr-9477-ai-incident-reporting/brick.md
- H.R. 5388: https://kbmill.com/bills/hr-5388-ai-uniformity/brick.md
- S. 4214: https://kbmill.com/bills/s-4214-ai-data-center-moratorium/brick.md
- H.R. 9442: https://kbmill.com/bills/hr-9442-ai-data-center-moratorium/brick.md  


## Incident reporting contrast (S.5061 vs H.R.9477 vs Kill Switch)

| | S. 5061 Secure A.I. Development | H.R. 9477 Incident Reporting | H.R. 9917 Kill Switch |
|---|---|---|---|
| **Agency** | NIST/Commerce incident + registry path | **Secretary of Commerce** designates + receives reports | **DHS** shutdown capability / orders |
| **Core action** | Taxonomy + frontier registry / tracking | **Report incidents** for covered models | Maintain shutdown capability; comply with orders |
| **Coverage gate** | Definitions + registry of frontier models available to public | Regulatory capability/other thresholds (national security / public safety) | Covered entity/technology by DHS rule |
| **Normalized actions** | `creates_incident_taxonomy_or_registry`, `mandates_reporting` | `mandates_reporting`, `establishes_liability` | `requires_shutdown_capability`, `establishes_liability` |

Do not treat “incident” language as one mechanism.

**Watch (not on shelf):** mid-Sept 2026 press describes a **Kennedy** Senate unanimous-consent “kill switch” idea framed as **company-held**, not government-held. That is a different mechanism from H.R. 9917’s DHS path — do not merge. No milled Senate print until an S. number + GovInfo HTML exist (`watch_list` in `/bills.json`).


## Preemption / uniformity contrast (H.R. 5388 vs FRONTIER)

| | H.R. 5388 Uniformity | H.R. 9925 FRONTIER |
|---|---|---|
| **Core federalism tool** | **5-year temporary moratorium** on state/local enforcement of laws regulating AI models/systems/ADS in interstate commerce (SEC. 6) | Preemption/inconsistency language tied to frontier oversight regime — cite FRONTIER sections |
| **Also creates** | National AI Action Plan to Congress (SEC. 5) | Under Secretary + IVO developer duties |
| **Normalized action** | `limits_state_regulation` (center) | `limits_state_regulation` among several actions |
| **Carve-outs** | Facilitation/streamlining; generally applicable criminal law; state procurement as market participant | See FRONTIER print |

Do not treat all “preemption” language as identical.


## Data-center vs state-law moratorium

| | H.R.9442 / S.4214 Data Center Moratorium | H.R.5388 Uniformity |
|---|---|---|
| **Target** | **Physical AI data centers** (build/upgrade) + compute hardware exports | **State/local laws** regulating AI models/systems/ADS |
| **Duration / trigger** | Until specified federal AI product/labor/environment laws enacted | **5-year** temporary moratorium from enactment |
| **Agencies** | Commerce (exports), Energy (reports) | White House Action Plan to Congress |
| **Normalized actions** | `imposes_infrastructure_moratorium`, `imposes_export_controls`, `mandates_reporting` | `limits_state_regulation`, `mandates_reporting` |

Do not conflate “moratorium” language across these bricks.


## CREATE AI companions (House IH vs Senate IS)

| | H.R. 2385 IH | S. 4441 IS |
|---|---|---|
| **Mechanism** | Establish **NAIRR** research resource | Establish **NAIRR** (Senate print) |
| **Normalized actions** | `authorizes_research`, `creates_federal_office_or_program`, `protects_research_or_public_interest_use` | same family |
| **Version caution** | House **RH/substitute exists** on GovInfo — not this brick | IS only on shelf |
| **Use** | Quote House IH from hr-2385 brick; Senate from s-4441 brick |

