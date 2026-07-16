# Roadmap to Human Influence Telemetry 1.0.0

This roadmap treats version advancement as an evidence claim. Dates are secondary. A milestone is complete only when its stated artifacts and tests exist in the public repository.

## Release principles

- `0.x` releases may change assessment semantics as evidence accumulates.
- `1.0.0` means the public method is stable enough for independent implementation, not that HIT is legally certified, causally validated, or institutionally adopted.
- Missing evidence must remain `IE`; it is never converted to zero for aggregation convenience.
- Normative changes require migration notes, synchronized schema and handbook updates, and revised fixtures.
- Repository release versions remain distinct from component versions when the specification, schema, or catalog does not change.
- Every numbered release must pass repository validation and identify its exact GitHub tag. Zenodo identifiers are recorded after successful archival and are not fabricated or anticipated.

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

## Current release: 0.2.0 public evidence pack

**Status:** Complete for release.

### Released artifacts

- three public case-study narratives with source provenance;
- four machine-readable assessments covering each institutional actor;
- documented public/private extraction boundary;
- case-derived ambiguities recorded rather than silently resolved;
- validator coverage for every machine-readable case assessment;
- release notes and compatibility statement.

### Included cases

1. Dutch childcare-benefits scandal: harm-period decision architecture.
2. Obermeyer population-health algorithm: deploying health systems and manufacturer scored separately.
3. Cigna PxDx: claims-review workflow with a designed Command disagreement.

### Completion result

A reader with no access to the private source repository can inspect the cited public record, reproduce each assessment boundary, validate the JSON records, and identify where findings depend on interpretation.

Version 0.2.0 does not change the 0.1.0 specification, assessment schema, dimension catalog, or scoring semantics. Its contribution is public evidence and reproducible application records.

## 0.3.0: Inter-rater protocol and result

### Prepared development artifacts

- `validation/inter-rater-protocol.md`;
- `validation/protocol-lock.json`;
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

- protocol reviewed and locked on `main` before scoring begins;
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

A passing or failing exercise may be released as v0.3.0. Maturity Level 2 is claimed only when the predeclared threshold and independence conditions are met.

## 0.4.0: Rubric stabilization

### Candidate normative revisions

- Reform scope: harmed process versus architecture class;
- Reform provenance: institution-initiated versus externally forced;
- actor decomposition for vendor, deployer, and public authority;
- evidentiary tiers for allegation, reporting, administrative finding, pleading-stage ruling, and merits judgment;
- explicit rule for `0` versus `IE`;
- minimum evidence for a finding of `2` under different sampling designs;
- conflicting-artifact handling;
- process-level versus record-level assessment;
- prohibition on unsupported composite scores.

### Completion test

Every normative change is represented consistently in the specification, schema, catalog, handbook, fixtures, cases, validator, changelog, and migration notes.

## 0.9.0: Stable release candidate

### Required conditions

- all seven advancement criteria in `SPECIFICATION.md` are provisionally satisfied;
- schema and catalog are frozen for the release-candidate period;
- independent application materials are complete;
- all public cases validate under the candidate schema;
- no unresolved ambiguity is known to systematically change findings without being governed by a documented rule;
- citation and archival metadata are synchronized;
- a breaking-change review from 0.1.0 is published.

### Completion test

External reviewers can implement the candidate method from public artifacts, reproduce the included assessments, and identify the method's non-claims without relying on private explanation.

## 1.0.0: Stable public method

Version 1.0.0 may be declared only when:

1. the schema and catalog are internally consistent;
2. deterministic fixtures cover substantive, ceremonial, and insufficient-evidence cases;
3. two independent scorers have applied the method to the same frozen materials;
4. disagreement handling is documented and exercised;
5. at least three public-record case studies are released with source provenance;
6. limitations, claim statuses, and update conditions are current;
7. repository validation passes for the exact release commit.

Version 1.0.0 will establish a stable documentary assessment contract. It will not establish that:

- higher HIT findings cause lower harm;
- HIT determines legal compliance;
- HIT is a certification standard;
- recorded reasons are truthful;
- human involvement is always preferable to automation;
- HIT has been independently adopted.

## Beyond 1.0.0

- **Maturity Level 4, Validated:** preregistered prospective design and pilot result.
- **Maturity Level 5, Adopted:** independent institutional use and external reference.
- Cross-artifact work may add a Governed Decision Intelligence input profile and shared decision-assurance test vectors without making GDI a required dependency.
