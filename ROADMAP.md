# Roadmap to Human Influence Telemetry 1.0.0

This roadmap treats version advancement as a public compatibility claim. Research maturity remains an evidence claim governed by `RESEARCH.md`.

Dates are secondary. A milestone is complete only when its stated artifacts and tests exist in the public repository.

## Release principles

- `0.x` releases may change assessment semantics as evidence and implementation testing accumulate.
- `1.0.0` means the public assessment contract is stable enough for independent implementation.
- Research maturity is reported separately from repository and component versions.
- A stable `1.0.0` contract may remain at Maturity Level 1 while human inter-rater evidence is pending.
- Missing evidence remains `IE`; it is never converted to zero for aggregation convenience.
- Normative changes require migration notes, synchronized schema and handbook updates, and revised fixtures.
- Repository release versions remain distinct from component versions when the specification, schema, or catalog does not change.
- Every numbered release must pass repository validation and identify its exact GitHub tag.
- Zenodo identifiers are recorded after successful archival and are never fabricated or anticipated.
- The governance basis for separating semantic versioning from research maturity is recorded in `docs/decisions/ADR-0001-separate-semantic-versioning-from-research-maturity.md`.

## Foundation release: 0.1.0

Completed:

- six substantive dimensions plus cross-cutting Telemetry Integrity;
- `0`, `1`, `2`, and `IE` finding contract;
- machine-readable schema and dimension catalog;
- deterministic substantive, ceremonial, and insufficient-evidence fixtures;
- public application handbook;
- automated positive, negative, and metadata validation;
- citable GitHub release and Zenodo archival workflow.

Research boundary:

- no inter-rater reliability result;
- no prospective institutional validation;
- no legal or standards conformity determination;
- no independent adoption claim.

## Current release: 0.2.1 research-readiness infrastructure

**Status:** Complete for release.

### Released artifacts

- three public case-study narratives with source provenance;
- four machine-readable assessments covering each institutional actor;
- documented public/private extraction boundary;
- case-derived ambiguities recorded without silent resolution;
- locked human inter-rater protocol and frozen scorer packet;
- deterministic scorer-comparison tooling and synthetic vectors;
- adversarial rubric-friction review;
- coordinator and recruitment infrastructure;
- separate model-based rubric stress-test protocol;
- validator coverage for release, protocol, coordinator, fixture, and case artifacts;
- release notes and compatibility statement.

### Research status

The repository remains at Maturity Level 1. Claim H3 remains unresolved because no eligible pair of independent human scorers has completed the locked protocol.

## Human inter-rater research track

### Prepared artifacts

- `validation/inter-rater-protocol.md`;
- locked `validation/protocol-lock.json`;
- frozen scorer packet and source manifest;
- machine-readable scorer-submission schema;
- neutral submission template;
- deterministic comparison tool;
- synthetic comparison test vectors;
- disagreement taxonomy;
- adjudication template;
- explicit pending-results boundary.

These artifacts prepare the exercise. They do not constitute an inter-rater result.

### Remaining empirical gates

- at least two eligible scorers independent of the author and of each other;
- no author scoring and no scorer-to-scorer coordination;
- two complete schema-valid submissions;
- deterministic pre-adjudication comparison;
- dimension-level disagreement register;
- adjudication record preserving original scores;
- statement of whether the handbook, schema, or later rubric should change;
- repository claim and maturity status updated from the pre-adjudication result.

### Predeclared threshold

The Level 2 agreement gate requires:

- at least six exact agreements across the six substantive dimensions and Telemetry Integrity;
- at least `0.8571` exact agreement;
- zero critical disagreements;
- satisfied independence and completeness conditions.

Unweighted Cohen's kappa across the six substantive dimensions is supplementary because the sample is small and category prevalence may dominate the estimate.

### Completion test

Two independent reviewers can apply the frozen public materials without author coaching. The repository publishes both original submissions, the deterministic pre-adjudication comparison, and all disagreements without collapsing them into a favorable post-hoc consensus.

A passing or failing exercise must be released when completed. Maturity Level 2 is claimed only when the predeclared threshold and independence conditions are met. A compatible result may be published in the `1.x` series after `1.0.0`.

## 0.4.0: Normative rubric stabilization

### Required revisions

- affirmative evidence of absence and the boundary between `0` and `IE`;
- minimum evidence establishing formal presence before `1` can be assigned;
- minimum evidence for `2` under observed, tested, and asserted capacity;
- actor and authority decomposition;
- temporal admissibility for correction, repair, and reform;
- substantiated-harm trigger for Repair;
- institutional-record and packet-level Telemetry Integrity;
- status thresholds for `adequate`, `limited`, `unreliable`, and `IE`;
- contradictory-artifact handling and evidentiary tiers;
- process sampling and aggregation rule;
- source locators and citation precision;
- prohibition on unsupported composite scores.

### Completion test

Every friction class in `HIT-ARFR-001` has a governing rule or a documented reason it remains outside the contract. Every normative change is represented consistently in the specification, schema, catalog, handbook, fixtures, cases, validator, changelog, and migration notes.

## 0.5.0: Executable conformance

### Required artifacts

- positive, negative, and boundary fixtures for every normative rule;
- explicit absence-versus-missing-evidence vectors;
- formal-authority and exercised-capacity vectors;
- contradictory-source vectors;
- multi-actor and temporal-attribution vectors;
- Telemetry Integrity boundary vectors;
- machine-readable compatibility manifest;
- migration suite from component version `0.1.0`;
- deterministic conformance report;
- one-command repository validation.

### Completion test

The repository rejects every known invalid state and produces deterministic results for every included valid and boundary case.

## 0.9.0: Stable release candidate

### Required conditions

- normative contract frozen for the candidate;
- specification, schema, catalog, handbook, and validator synchronized;
- all public cases validate under the candidate schema or have documented migrations;
- no unresolved ambiguity is known to systematically change findings without a documented rule;
- citation and archival metadata synchronized;
- breaking-change review from component version `0.1.0` published;
- public implementation package complete;
- clean-room implementation audit completed with original outputs preserved;
- no release-blocking defect remains open.

### Completion test

A reader can implement and validate the candidate method from public artifacts, reproduce the included fixtures and assessments, and identify the method's non-claims without private explanation.

## 1.0.0: Stable public contract

Version `1.0.0` may be declared only when:

1. the six substantive dimensions and Telemetry Integrity have stable normative definitions;
2. the decision rules for `0`, `1`, `2`, and `IE` govern the known ambiguity classes;
3. the schema and catalog are internally consistent;
4. deterministic fixtures cover substantive, ceremonial, insufficient-evidence, invalid, and boundary cases;
5. disagreement handling remains documented and executable for future human scoring;
6. at least three public-record case studies are released with source provenance and validate under the stable contract;
7. limitations, claim statuses, update conditions, migration notes, and non-claims are current;
8. the implementation package is complete and requires no private author explanation;
9. one public release candidate has been published and no release-blocking defect remains open;
10. repository validation passes for the exact release commit.

Version `1.0.0` will establish a stable documentary assessment contract. It will not establish that:

- independent human reviewers agree;
- HIT has reached Maturity Level 2;
- higher HIT findings cause lower harm;
- HIT determines legal compliance;
- HIT is a certification standard;
- recorded reasons are truthful;
- human involvement is always preferable to automation;
- HIT has been independently adopted.

## Beyond 1.0.0

- **Maturity Level 2, Applicable:** complete the locked independent human exercise under its declared threshold.
- **Maturity Level 3, Evidenced:** Level 2 satisfied with at least three public-record applications.
- **Maturity Level 4, Validated:** preregistered prospective design and pilot result.
- **Maturity Level 5, Adopted:** independent institutional use and external reference.
- Compatible research results, mappings, and implementation profiles may use `1.x` releases.
- Breaking normative changes require `2.0.0`.
- Cross-artifact work may add a Governed Decision Intelligence input profile and shared decision-assurance test vectors without making GDI a required dependency.
