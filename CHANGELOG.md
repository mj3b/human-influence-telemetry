# Changelog

All notable changes to Human Influence Telemetry are documented here.

The project follows Semantic Versioning for the public technical artifact. Repository release versions are distinct from component versions when the specification, schema, or catalog does not change.

## [Unreleased]

### Planned

- Independent inter-rater exercise and disagreement record
- Rubric revisions derived from public cases and scorer disagreement
- Validation protocol with a preregistered population and statistical method

## [0.2.0] - 2026-07-16

### Added

- Public-record case-study directory with source provenance and explicit research boundaries
- Dutch childcare-benefits harm-period HIT application
- Obermeyer population-health application with separate deployer and manufacturer assessments
- Cigna PxDx application with a designed Command disagreement for inter-rater testing
- Four actor-specific machine-readable case assessments
- Evidence-gated roadmap from 0.1.0 through 1.0.0
- Validation coverage for public case-assessment JSON files
- Release notes for v0.2.0

### Changed

- README maturity table and repository map now identify the evidence pack as released rather than pending
- Research status now records that the three-case public evidence condition is satisfied while inter-rater reliability remains unresolved
- Release metadata now identifies repository release 0.2.0 while retaining specification, schema, and catalog version 0.1.0
- DOI documentation now treats the first successfully archived GitHub release as the event that establishes the HIT software concept DOI

### Fixed

- Normalized `case-studies/assessments/cigna-pxdx.json` and `case-studies/assessments/obermeyer-manufacturer.json` to the repository-standard indented JSON format without changing assessment findings, evidence claims, or schema semantics

### Compatibility

Version 0.2.0 adds evidence artifacts and release metadata. It does not change the 0.1.0 specification, assessment schema, dimension catalog, scoring semantics, or existing fixture contract. All v0.2.0 case assessments therefore continue to declare `schema_version` 0.1.0.

### Research boundary

The public case studies demonstrate that HIT can be applied to heterogeneous documentary records and can produce differentiated actor profiles. They do not establish inter-rater reliability, legal liability, causal effectiveness, certification, prospective validation, or independent adoption.

## [0.1.0] - 2026-07-16

### Added

- Working Human Influence Telemetry specification
- Six substantive dimensions: Counsel, Judgment, Command, Correction, Repair, and Reform
- Cross-cutting Telemetry Integrity assessment
- Four findings: `0`, `1`, `2`, and `IE`
- Machine-readable assessment schema and dimension catalog
- Deterministic substantive, ceremonial, and insufficient-evidence fixtures
- Application handbook
- Research protocol and bounded claim register
- Provenance and limitations documents
- Repository-wide validation workflow
- Citation metadata and Apache License 2.0

### Research boundary

Version 0.1.0 demonstrates that the method can be represented structurally and exercised against included fixtures. It does not establish inter-rater reliability, causal effectiveness, legal compliance, certification, or independent adoption.

[Unreleased]: https://github.com/mj3b/human-influence-telemetry/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/mj3b/human-influence-telemetry/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/mj3b/human-influence-telemetry/releases/tag/v0.1.0
