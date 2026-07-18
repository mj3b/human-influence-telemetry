# Public-record case studies

This directory contains retrospective Human Influence Telemetry applications released with repository version `0.2.0` under specification and assessment schema `0.1.0`.

The cases are evidence demonstrations, not legal opinions, compliance determinations, certifications, or causal validation.

## Historical cases

| Case | Institutional setting | Historical assessment files | 0.4.0 disposition |
|---|---|---|---|
| [Dutch childcare-benefits scandal](toeslagenaffaire.md) | Public-benefits fraud designation and clawback | [`toeslagenaffaire-harm-period.json`](assessments/toeslagenaffaire-harm-period.json) | `historical_version_bound` |
| [Obermeyer population-health algorithm](obermeyer.md) | Algorithmic allocation of care-management attention | [`obermeyer-deployers.json`](assessments/obermeyer-deployers.json), [`obermeyer-manufacturer.json`](assessments/obermeyer-manufacturer.json) | `historical_version_bound` |
| [Cigna PxDx](cigna-pxdx.md) | Algorithmic post-service claims review | [`cigna-pxdx.json`](assessments/cigna-pxdx.json) | `protocol_completed_historical_version_bound` |

## Contract boundary

The four machine-readable files conform to schema `0.1.0`. They are immutable historical artifacts and do not conform automatically to `0.4.0`.

Migration requires a fresh bounded reassessment under the current specification, schema, actor-authority matrix, evidence-state rules, Repair trigger, sampling and aggregation contract, structured locators, and split Telemetry Integrity model.

No `0.4.0` public-case finding is claimed.

## Cigna protocol result

The Cigna inter-rater exercise is complete and published under `validation/results/`. Completion removes the contamination-based deferral. It does not convert the historical author assessment or the scorer submissions into `0.4.0` assessments.

A future current-contract Cigna assessment must be created as a separate record after a fresh source review.

## Provenance

The narratives were extracted from the private *Poenitentia Institutionum* research repository under the controls in [`PROVENANCE.md`](../PROVENANCE.md). The public files are canonical for HIT use. Private annotations are not normative dependencies.

## Research status

The historical cases demonstrate application to heterogeneous public records. The first locked human exercise demonstrates agreement for one frozen Cigna packet. Neither establishes field validity, causal effectiveness, legal liability, certification, or independent adoption.
