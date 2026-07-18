# Provenance

Human Influence Telemetry originated within the research program for *Poenitentia Institutionum: Prudence, Responsibility, and Institutional Repentance in the Age of Artificial Intelligence*.

The public technical instrument is extracted from that program without publishing the chapter manuscript, editorial correspondence, restricted annotations, unpublished theological synthesis, contractual records, or source-pack contents not required to apply HIT.

## Public extraction lineage

- Concept author: Mark Julius Banasihan
- ORCID: 0009-0001-8121-2878
- Originating concept DOI: 10.5281/zenodo.21204892
- Source repository: private and retained by the author
- Canonical public repository: `mj3b/human-influence-telemetry`
- Public repository release: 0.5.0
- Conformance engine version: 0.5.0
- Public specification version: 0.4.0
- Assessment schema version: 0.4.0
- Dimension catalog version: 0.4.0
- Research maturity: Level 1, Defined

## Version lineage

### 0.1.0

Established the first public specification, schema, catalog, handbook, fixtures, and repository validator.

### 0.2.0

Released three retrospective case narratives and four actor-specific machine-readable assessments under the `0.1.0` contract.

### 0.2.1

Added locked evaluation procedures, coordinator tooling, recruitment materials, adversarial rubric-friction review, model stress-test protocol, and software-archival metadata without changing the `0.1.0` component contracts.

### 0.4.0

Promoted a breaking normative and data-contract revision derived from all 16 friction classes in `HIT-ARFR-001`. It introduced the evidence-state model, explicit finding thresholds, split Telemetry Integrity, actor-authority attribution, Repair triggers, sampling and aggregation controls, contradiction handling, evidence propositions, precise locators, and 48 executable boundary fixtures.

The superseded `0.1.0` contract is preserved under `archive/v0.1.0/`. The `0.2.1` validator is preserved under `archive/v0.2.1/`.

### 0.5.0

Added executable complete-record conformance for the `0.4.0` contract. The release introduced reusable semantic validation, stable error codes, deterministic reports, a compatibility manifest, protected migration planning, complete-record mutation vectors, CLI operation, and a package-oriented implementation structure.

Release `0.5.0` does not revise the specification, assessment schema, dimension catalog, handbook, or scoring semantics. Those remain `0.4.0`.

## Canonical construct decision

The public instrument uses six substantive dimensions: Counsel, Judgment, Command, Correction, Repair, and Reform.

Telemetry Integrity is cross-cutting and has two visible components:

- institutional-record integrity;
- assessment-packet integrity.

One overall status is derived deterministically without concealing either component.

## Case-study lineage

The historical public evidence pack contains:

- Dutch childcare-benefits harm-period assessment;
- Obermeyer population-health deployer assessment;
- Obermeyer population-health manufacturer assessment;
- Cigna PxDx assessment.

These files remain canonical historical `0.1.0` artifacts in `case-studies/assessments/` and are pinned by Git blob SHA in `case-studies/migrations/v0.4.0/migration-manifest.json`.

Three records are `historical_version_bound`. Cigna is `deferred_locked_protocol` to avoid contaminating or retrospectively changing the locked human exercise. No `0.4.0` public-case findings are claimed in this release.

## Normative decision lineage

- ADR-0001 separates semantic-version stability from research maturity.
- ADR-0002 approves the `0.4.0` evidence-state and finding rules.
- ADR-0003 supersedes the planned `v0.3.0` human-result label and requires the eventual result to use the next available chronological version.

ADR-0003 does not modify the locked protocol, frozen packet, scorer contract, threshold, critical disagreements, adjudication controls, or pass/fail publication obligation.

## Source-control rule

This public repository is canonical for the HIT specification, schemas, catalogs, implementation, fixtures, public case artifacts, and releases. The private source repository remains canonical for the book chapter and unpublished research lineage.

Changes to the public contract or case assessments must be versioned here and must not silently inherit unpublished changes.
