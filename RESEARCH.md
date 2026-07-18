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
| E5 | Empirical evidence from independent application, field data, or statistical testing |

## Claim register

| ID | Claim | Status after 0.6.0 | Update condition |
|---|---|---|---|
| H1 | HIT can represent six substantive dimensions and split Telemetry Integrity in a machine-readable assessment | Demonstrated structurally by the 0.4.0 schema, catalog, canonical example, and CI | Revise when a required construct cannot be represented |
| H2 | The evidence-state and `0/1/2/IE` rules distinguish affirmative absence, ceremonial presence, substantive exercise, and missing evidence | Demonstrated for 48 synthetic boundary cases; independently applied under the preserved 0.1.0 scorer contract | Requires replication under a compatible current contract and cases with category variation |
| H3 | Independent reviewers can reach the predeclared agreement threshold using the published materials | Supported for one frozen Cigna packet: 7 of 7 exact agreements and zero critical disagreements | Replicate across additional cases, sectors, scorer populations, and a compatible current contract |
| H4 | HIT can expose oversight theater that binary human-in-the-loop labels miss | Supported by design logic, historical cases, and convergent ceremonial findings in the first human exercise | Requires external replication under a compatible contract |
| H5 | Higher HIT findings predict lower harm or better repair | Hypothesis | Requires preregistered population, outcomes, and statistical method |
| H6 | A high HIT finding proves meaningful human control in a causal or legal sense | Unsupported | Would require evidence beyond documentary assessment |
| H7 | HIT evidence may support external oversight, accountability, and contestability obligations | Provisional mapping claim | Requires qualified standards or legal review and DEAS-style applicability analysis |
| H8 | HIT is independently adopted | Not yet | Requires use by an institution outside the author's control |

## Executable evidence register

Release `0.5.0` established E1 evidence about internal representation, rejection behavior, determinism, and compatibility controls through:

- one canonical schema-valid synthetic assessment under contract `0.4.0`;
- 48 deterministic rubric boundary cases;
- one valid and fifteen invalid complete-record vectors;
- reusable semantic checks across actors, claims, findings, Repair triggers, integrity, aggregation, and citations;
- deterministic reports;
- compatibility metadata;
- protected migration planning;
- CLI smoke tests and exact-head validation.

## Human evidence register

Release `0.6.0` adds the first E5 result.

| Field | Result |
|---|---|
| Protocol | `HIT-IRP-CIGNA-001`, locked version 1.0.0 |
| Frozen packet | `HIT-IR-CIGNA-PXDX-001` |
| Scorer contract | Specification and schema 0.1.0 |
| Eligible independent scorers | 2 of 2 |
| Verified locked submissions | 2 of 2 |
| Compared items | 7 |
| Exact agreements | 7 |
| Exact-agreement proportion | `1.0000` |
| Required threshold | At least 6 of 7 and zero critical disagreements |
| Critical disagreements | 0 |
| Supplementary Cohen's kappa | `null`, because all six substantive ratings used one category |
| H3 decision | Supported for this bounded exercise |
| Maturity decision | Level 2, Applicable |
| Result release | 0.6.0 |

Both scorers assigned `1` to all six substantive dimensions and `limited` to Telemetry Integrity. The scorer submissions used different primary source references and different analytical language, but those differences did not produce categorical disagreement.

The result establishes successful independent application under one frozen packet. It does not estimate general inter-rater reliability.

## Historical public application register

| Case | Unit of analysis | Historical assessments | Current disposition |
|---|---|---:|---|
| Dutch childcare-benefits scandal | Belastingdienst/Toeslagen harm-period architecture | 1 | `historical_version_bound` |
| Obermeyer population-health algorithm | Deploying health systems and manufacturer | 2 | `historical_version_bound` |
| Cigna PxDx | Cigna claims-review workflow | 1 | `protocol_completed_historical_version_bound` |

The four author-scored assessments remain immutable `0.1.0` artifacts. The human exercise does not convert the historical Cigna assessment into a `0.4.0` assessment.

## Methods

The research program uses artifact construction, normative specification, JSON Schema validation, deterministic fixtures, complete-record mutation testing, retrospective public-record case studies, blinded inter-rater testing, comparative boundary analysis, and prospective validation when institutional access becomes available.

The locked inter-rater design predeclared eligibility, blinding, source boundaries, agreement threshold, critical disagreements, supplementary kappa, preservation of original scores, and publication of passing and failing results.

## Threats to validity

1. Institutional records may be incomplete, curated, or controlled by the governed system.
2. Recorded reasons may be post-hoc rationalizations.
3. One observed exercise may not represent the dominant architecture.
4. Retrospective public cases have selection bias.
5. Public records may not expose internal access or authority.
6. Findings compress variation within each dimension.
7. Reviewers may apply normative thresholds differently in other cases.
8. Litigation records vary by procedural posture.
9. Framework comparisons may overstate equivalence.
10. Synthetic fixtures demonstrate deterministic design choices, not empirical correctness.
11. Complete-record mutation tests demonstrate rejection behavior, not evidence truth.
12. The first human exercise has two scorers, seven compared items, and one retrospective insurance case.
13. All six substantive ratings used one category, so Cohen's kappa is undefined and category discrimination was not tested empirically.
14. The scorer exercise used the preserved `0.1.0` contract, not the current `0.4.0` contract.
15. A passing first exercise demonstrates reproducibility under one frozen packet, not general reliability.

## Maturity model

| Level | Name | Entry criterion | Current status |
|---|---|---|---|
| 1 | Defined | Public constructs, machine-readable contract, executable fixtures, citable archive | Complete |
| 2 | Applicable | A stranger can apply the method and the locked human exercise passes its declared independence and agreement rules | Current |
| 3 | Evidenced | Level 2 plus at least three public applications under a compatible contract | Pending |
| 4 | Validated | Preregistered prospective design and pilot result | Pending |
| 5 | Adopted | Independent institutional use and external reference | Pending |

The levels are cumulative. Release `0.6.0` advances research maturity to Level 2 because the locked exercise passed. The version number alone did not produce that advancement.

## Release discipline

A numbered release requires:

- passing exact-commit validation;
- synchronized repository metadata and component-version boundaries;
- current limitations and claim status;
- migration or compatibility records;
- accurate citation metadata;
- preserved historical and locked artifacts;
- explicit adjacent-system non-claims;
- public release assets matching the recorded SHA-256 digest.
