# Research Protocol and Claim Register

## Research object

Human Influence Telemetry is a design-science research artifact that operationalizes substantive human influence as observable properties of institutional decision records.

## Primary research question

> Can independent reviewers use HIT to distinguish substantive human influence, ceremonial oversight, affirmative absence, and insufficient evidence in AI-mediated institutional decision processes?

## Evidence classes

| Class | Meaning |
|---|---|
| E1 | Executable evidence from validation, deterministic fixtures, or comparison tooling |
| E2 | Artifact evidence contained in specifications, schemas, records, assessments, or locked protocols |
| E3 | External source evidence supporting a construct or case proposition |
| E4 | Comparative inference connecting HIT to adjacent governance systems |
| E5 | Empirical hypothesis requiring independent application, field data, or statistical testing |

## Claim register

| ID | Claim | Status after 0.4.0 | Update condition |
|---|---|---|---|
| H1 | HIT can represent six substantive dimensions and split Telemetry Integrity in a machine-readable assessment | Demonstrated structurally by the 0.4.0 schema, catalog, canonical example, and CI | Revise when a required construct cannot be represented |
| H2 | The evidence-state and `0/1/2/IE` rules distinguish affirmative absence, ceremonial presence, substantive exercise, and missing evidence | Demonstrated for 48 synthetic boundary cases; not independently validated | Revise after independent scoring or failed discrimination cases |
| H3 | Independent reviewers can reach the predeclared agreement threshold using the published materials | Unresolved | Requires two eligible independent submissions and a published pre-adjudication result under the locked protocol |
| H4 | HIT can expose oversight theater that binary human-in-the-loop labels miss | Supported by design logic and historical public cases; not independently validated | Requires external replication under a compatible contract |
| H5 | Higher HIT findings predict lower harm or better repair | Hypothesis | Requires preregistered population, outcomes, and statistical method |
| H6 | A high HIT finding proves meaningful human control in a causal or legal sense | Unsupported | Would require evidence beyond documentary assessment |
| H7 | HIT evidence may support external oversight, accountability, and contestability obligations | Provisional mapping claim | Requires qualified standards or legal review and DEAS-style applicability analysis |
| H8 | HIT is independently adopted | Not yet | Requires use by an institution outside the author's control |

## Executable evidence register

Release `0.4.0` includes:

- one canonical schema-valid synthetic assessment;
- 48 deterministic rubric boundary cases;
- one accepted, one rejected, and one boundary case for each `FR-01` through `FR-16`;
- mutation tests for changed outcomes, missing coverage, and duplicate identifiers;
- validators for the contract, historical case preservation, migration dispositions, protocol artifacts, claim boundaries, and metadata.

This is E1 evidence about internal representation and deterministic behavior. It is not E5 evidence about independent reviewer agreement or field effectiveness.

## Historical public application register

| Case | Unit of analysis | Historical assessments | Current disposition |
|---|---|---:|---|
| Dutch childcare-benefits scandal | Belastingdienst/Toeslagen harm-period architecture | 1 | `historical_version_bound` |
| Obermeyer population-health algorithm | Deploying health systems and manufacturer | 2 | `historical_version_bound` |
| Cigna PxDx | Cigna claims-review workflow | 1 | `deferred_locked_protocol` |

The four author-scored assessments were released under specification and schema `0.1.0`. They demonstrate historical application to heterogeneous public records but do not conform automatically to `0.4.0`, resolve H3, or establish field validity.

## Locked inter-rater exercise register

| Field | Current state |
|---|---|
| Protocol | `HIT-IRP-CIGNA-001`, locked version 1.0.0 |
| Frozen packet | `HIT-IR-CIGNA-PXDX-001` |
| Scorer contract | Specification and schema 0.1.0 |
| Primary measure | Exact agreement across six substantive dimensions plus Telemetry Integrity |
| Advancement threshold | At least 6 of 7 exact agreements and zero critical disagreements |
| Supplementary measure | Unweighted Cohen's kappa across six substantive dimensions |
| Eligible scorers enrolled | 0 of 2 |
| Locked submissions | 0 of 2 |
| Pre-adjudication result | Pending |
| H3 decision | Pending |
| Maturity Level 2 decision | Pending |
| Release version | Next available version when the result package is complete |

The previous planned `v0.3.0` result label is superseded under ADR-0003. The protocol, packet, threshold, critical disagreements, preservation controls, and pass/fail publication obligation remain unchanged.

Prepared infrastructure is evidence about study design and reproducibility controls. It is not evidence that independent scorers agree.

## Methods

The research program uses artifact construction, normative specification, JSON Schema validation, deterministic fixtures, retrospective public-record case studies, blinded inter-rater testing, comparative boundary analysis, and prospective validation when institutional access becomes available.

The locked inter-rater design predeclares eligibility, blinding, source boundaries, agreement threshold, critical disagreements, supplementary kappa, preservation of original scores, and publication of passing and failing results.

## Threats to validity

1. Institutional records may be incomplete, curated, or controlled by the governed system.
2. Recorded reasons may be post-hoc rationalizations.
3. One observed exercise may not represent the dominant architecture.
4. Retrospective public cases have selection bias.
5. Public records may not expose internal access or authority.
6. Findings compress variation within each dimension.
7. Reviewers may apply normative thresholds differently.
8. Litigation records vary by procedural posture.
9. Framework comparisons may overstate equivalence.
10. Synthetic fixtures demonstrate deterministic design choices, not empirical correctness.
11. The first human exercise has only two scorers, seven compared items, and one retrospective case.
12. A passing first exercise would demonstrate reproducibility under one frozen packet, not general reliability across sectors.

## Maturity model

| Level | Name | Entry criterion |
|---|---|---|
| 1 | Defined | Public constructs, machine-readable contract, executable fixtures, citable archive |
| 2 | Applicable | A stranger can apply the method and the locked human exercise passes its declared independence and agreement rules |
| 3 | Evidenced | Level 2 plus at least three public applications under a compatible contract |
| 4 | Validated | Preregistered prospective design and pilot result |
| 5 | Adopted | Independent institutional use and external reference |

The levels are cumulative. Release `0.4.0` remains Level 1. A stable semantic version does not advance maturity by itself.

## Release discipline

A numbered release requires:

- passing exact-commit validation;
- synchronized specification, schema, catalog, handbook, implementation, and metadata;
- current limitations and claim status;
- migration or compatibility records;
- accurate citation metadata;
- preserved historical and locked artifacts;
- explicit adjacent-system non-claims.

Semantic versioning and research maturity are governed separately by ADR-0001. Normative 0.4.0 rules are governed by ADR-0002. Chronological empirical-result versioning is governed by ADR-0003.
