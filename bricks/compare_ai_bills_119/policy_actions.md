# Normalized policy-action layer (v0)

**Type:** KBMill synthesis · **Not statute**  
**Pairs with:** [compare.md](./compare.md) · instrument `brick.md` files  
**Vocabulary:** controlled list in `/bills.json` → `policy_actions_vocabulary`

## Why this layer exists (GPT-6.6)

Two bills may say “AI safety” and do different things. Conversely, different wording may encode the **same** mechanism. This file maps each published brick to normalized actions.

| Normalized action | Meaning |
|---|---|
| `requires_evaluation` | Mandates or stands up testing/evaluation of systems |
| `authorizes_research` | Creates/expands research access or infrastructure |
| `mandates_reporting` | Requires reports to government or public |
| `creates_federal_office_or_program` | New office, under secretary, or named program |
| `directs_procurement_rules` | Federal buying / acquisition rules (none tagged yet on shelf) |
| `establishes_liability` | Civil/criminal penalties or private duties with teeth |
| `limits_state_regulation` | Preemption / uniformity limits on states |
| `regulates_open_weight_release` | Rules specifically gating weight release (none tagged yet — H.R.10152 is support, not a release ban) |
| `supports_open_model_adoption` | Affirmative Commerce/support for open/qualified open models |
| `protects_research_or_public_interest_use` | Research access / public-interest posture |
| `creates_standards_or_voluntary_guidance` | Standards, guidelines, recommended protocols |
| `requires_shutdown_capability` | Technical ability to throttle/suspend/shutdown |
| `creates_incident_taxonomy_or_registry` | Incident definitions and/or model registries |
| `licenses_or_oversees_third_party_verifiers` | IVO-style third-party verification |
| `imposes_infrastructure_moratorium` | Pause construction/upgrade of AI data centers / related infrastructure |
| `imposes_export_controls` | Restrict export/reexport of computing infrastructure hardware |

## Brick → actions (published shelf)

| Brick | policy_actions |
|---|---|
| S. 2938 Risk Evaluation | `requires_evaluation`, `creates_federal_office_or_program`, `creates_standards_or_voluntary_guidance`, `mandates_reporting` |
| S. 5061 Secure A.I. Development | `creates_incident_taxonomy_or_registry`, `mandates_reporting` |
| S. 4441 CREATE AI | `authorizes_research`, `creates_federal_office_or_program`, `protects_research_or_public_interest_use` |
| H.R. 2385 CREATE AI (House IH) | `authorizes_research`, `creates_federal_office_or_program`, `protects_research_or_public_interest_use` |
| H.R. 9925 FRONTIER | `requires_evaluation`, `licenses_or_oversees_third_party_verifiers`, `mandates_reporting`, `establishes_liability`, `limits_state_regulation`, `creates_federal_office_or_program` |
| H.R. 10152 Open-Source Leadership | `supports_open_model_adoption`, `mandates_reporting`, `protects_research_or_public_interest_use` |
| H.R. 9917 Kill Switch | `requires_shutdown_capability`, `establishes_liability`, `creates_standards_or_voluntary_guidance` |
| H.R. 9477 Incident Reporting | `mandates_reporting`, `creates_standards_or_voluntary_guidance`, `establishes_liability` |
| H.R. 5388 Uniformity | `limits_state_regulation`, `mandates_reporting`, `creates_standards_or_voluntary_guidance` |
| H.R. 9442 / S. 4214 Data Center Moratorium | `imposes_infrastructure_moratorium`, `imposes_export_controls`, `mandates_reporting` |

## Same theme, different action

| Theme word | Examples on this shelf |
|---|---|
| Evaluation | S.2938 = DOE **program**. FRONTIER = developer duties + **IVO** verification. |
| Open | H.R.10152 = **support adoption** of qualified open models (+ anti-ban construction). Not the same as regulating release under FRONTIER. |
| Safety / incidents | S.5061 = taxonomy/registry. H.R.9477 = **report to Commerce**. H.R.9917 = **shutdown capability**. |
| Preemption / uniformity | H.R.5388 = **temporary 5-year state moratorium** (carve-outs). FRONTIER = preemption tied to frontier oversight — different statute. |
| Moratorium (word collision) | Data-center bills pause **buildings/hardware exports**. Uniformity pauses **state AI regulation**. Same word, different targets. |
| Research | S.4441 = NAIRR **access**. S.2938 = evidence for future oversight. |

## Consistency checklist (every brick)

Expose the same fields in `/bills.json` (null or `na_fields` when N/A). Primary text stays in `brick.md`. Remill this file when new instruments land.
