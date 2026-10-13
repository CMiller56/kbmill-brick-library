# Indexes by instrument type

**Type:** workbench index · **synthesis helper** (not statute)  
**As of:** 2026-09-16 · Machine source of truth: `/bills.json` → `instrument_indexes`

Same issue, different instrument → different legal status. Do not mix classes in one analytical bucket without labeling.

---

## bill (`instrument_type: bill`)

**Count:** 11 · **branch:** legislative · **official_text:** true · **authority_level:** introduced_print

| version_id | slug | bill_family | print |
|---|---|---|---|
| `119-s-2938-is` | [s-2938-ai-risk-evaluation](https://kbmill.com/bills/s-2938-ai-risk-evaluation/) | `AI_RISK_EVALUATION_2025` | IS |
| `119-s-5061-is` | [s-5061-secure-ai-development](https://kbmill.com/bills/s-5061-secure-ai-development/) | `SECURE_AI_DEVELOPMENT_2026` | IS |
| `119-s-4441-is` | [s-4441-create-ai](https://kbmill.com/bills/s-4441-create-ai/) | `CREATE_AI_2025` | IS |
| `119-hr-2385-ih` | [hr-2385-create-ai](https://kbmill.com/bills/hr-2385-create-ai/) | `CREATE_AI_2025` | IH |
| `119-hr-9925-ih` | [hr-9925-frontier-act](https://kbmill.com/bills/hr-9925-frontier-act/) | `FRONTIER_ACT_2026` | IH |
| `119-hr-10152-ih` | [hr-10152-open-source-ai-leadership](https://kbmill.com/bills/hr-10152-open-source-ai-leadership/) | `OPEN_SOURCE_AI_LEADERSHIP_2026` | IH |
| `119-hr-9917-ih` | [hr-9917-ai-kill-switch](https://kbmill.com/bills/hr-9917-ai-kill-switch/) | `AI_KILL_SWITCH_2026` | IH |
| `119-hr-9477-ih` | [hr-9477-ai-incident-reporting](https://kbmill.com/bills/hr-9477-ai-incident-reporting/) | `AI_INCIDENT_REPORTING_2026` | IH |
| `119-hr-5388-ih` | [hr-5388-ai-uniformity](https://kbmill.com/bills/hr-5388-ai-uniformity/) | `AI_LEADERSHIP_UNIFORMITY_2025` | IH |
| `119-hr-9442-ih` | [hr-9442-ai-data-center-moratorium](https://kbmill.com/bills/hr-9442-ai-data-center-moratorium/) | `AI_DATA_CENTER_MORATORIUM_2026` | IH |
| `119-s-4214-is` | [s-4214-ai-data-center-moratorium](https://kbmill.com/bills/s-4214-ai-data-center-moratorium/) | `AI_DATA_CENTER_MORATORIUM_2026` | IS |

Primary text: each card’s `brick.md`.

---

## draft (`instrument_type: draft`)

**Count:** 1 · **official_text:** false · **authority_level:** unofficial_draft

| id | card | Rule |
|---|---|---|
| `draft-unofficial-thune-klobuchar-cruz-2026` | [hole card](https://kbmill.com/bills/draft-unofficial-thune-klobuchar-cruz-2026/) | No `brick.md`. Do not invent provisions from news. |

---

## synthesis (`instrument_type: synthesis`)

**Count:** 2 · **official_text:** false · **authority_level:** kbmill_synthesis

| slug | URL | Role |
|---|---|---|
| `compare-ai-bills-119` | [compare](https://kbmill.com/bills/compare-ai-bills-119/) | Mechanism matrix + section cites + policy_actions |
| `what-the-prints-say` | [workbench](https://kbmill.com/bills/what-the-prints-say/) | Scope/holes · mechanisms · public vs print · how to use |

Every synthesis claim should point back to one or more `version_id` + sections.

---

## Reserved empty classes

| instrument_type | Count | Note |
|---|---|---|
| `executive_order` | 0 | Add as separate class when milled |
| `regulation` | 0 | Agency rules — separate class |
| `court_opinion` | 0 | Slip opinions — separate class |
| `report` | 0 | Committee/agency reports — separate class |

When these land, give them their own index rows and never silently merge them into bill `bricks[]`.
