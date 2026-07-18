# Public-record case studies

This directory contains retrospective Human Influence Telemetry applications released with repository version `0.2.0` under specification and assessment schema `0.1.0`.

The cases are evidence demonstrations, not legal opinions, compliance determinations, certifications, or causal validation. A finding of `IE` means the historical record could not distinguish absence from unavailable evidence under the `0.1.0` contract.

## Historical cases

| Case | Institutional setting | Historical assessment files | 0.4.0 disposition |
|---|---|---|---|
| [Dutch childcare-benefits scandal](toeslagenaffaire.md) | Public-benefits fraud designation and clawback | [`toeslagenaffaire-harm-period.json`](assessments/toeslagenaffaire-harm-period.json) | `historical_version_bound` |
| [Obermeyer population-health algorithm](obermeyer.md) | Algorithmic allocation of care-management attention | [`obermeyer-deployers.json`](assessments/obermeyer-deployers.json), [`obermeyer-manufacturer.json`](assessments/obermeyer-manufacturer.json) | `historical_version_bound` |
| [Cigna PxDx](cigna-pxdx.md) | Algorithmic post-service claims review | [`cigna-pxdx.json`](assessments/cigna-pxdx.json) | `deferred_locked_protocol` |

## Contract boundary

The four machine-readable files conform to schema `0.1.0`. They are immutable historical artifacts and do not conform automatically to `0.4.0`.

Migration requires a fresh bounded reassessment under the current specification, schema, actor-authority matrix, evidence-state rules, Repair trigger, sampling and aggregation contract, structured locators, and split Telemetry Integrity model.

No `0.4.0` public-case finding is claimed in release `0.4.0`.

## Migration controls

The migration manifest in [`migrations/v0.4.0/`](migrations/v0.4.0/) pins every historical file by Git blob SHA and records its explicit disposition and update condition.

Cigna migration is deferred until the locked human exercise publishes its original submissions and pre-adjudication result. This prevents the new rubric from contaminating or retrospectively changing the locked `0.1.0` scorer contract.

## Provenance

The narratives were extracted from the private *Poenitentia Institutionum* research repository under the controls in [`PROVENANCE.md`](../PROVENANCE.md). The public files are canonical for HIT use. Private annotations are not normative dependencies.

## Research status

The historical cases demonstrate that the initial rubric could be applied to heterogeneous public records and produce differentiated actor profiles. They do not establish independent reviewer agreement, field validity, causal effectiveness, legal liability, certification, or independent adoption.
