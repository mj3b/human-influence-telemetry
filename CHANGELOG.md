# Changelog

All notable changes to Human Influence Telemetry are documented here.

The project follows Semantic Versioning for the public technical artifact. A version change refers to the public specification, schema, rubric, fixtures, evidence packs, and reference tooling. It does not imply independent validation or institutional adoption.

## [Unreleased]

### Added

- Public-record case-study directory with source provenance and explicit research boundaries
- Dutch childcare-benefits harm-period HIT application
- Obermeyer population-health application with separate deployer and manufacturer assessments
- Cigna PxDx application with a designed Command disagreement for inter-rater testing
- Four actor-specific machine-readable case assessments
- Evidence-gated roadmap from 0.1.0 through 1.0.0
- Validation coverage for public case-assessment JSON files

### Changed

- README maturity table and repository map now distinguish public evidence from independent scoring reliability
- Research status now records that the public case-study workstream is complete while inter-rater reliability remains unresolved

### Fixed

- Normalized `case-studies/assessments/cigna-pxdx.json` and `case-studies/assessments/obermeyer-manufacturer.json` to the repository-standard indented JSON format without changing assessment findings, evidence claims, or schema semantics

### Planned

- Independent inter-rater exercise and disagreement record
- Rubric revisions derived from public cases and scorer disagreement
- Validation protocol with a preregistered population and statistical method

### Research boundary

The public case studies demonstrate that HIT can be applied to heterogeneous documentary records and can produce differentiated actor profiles. They do not establish inter-rater reliability, legal liability, causal effectiveness, certification, or independent adoption.

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

[Unreleased]: https://github.com/mj3b/human-influence-telemetry/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/mj3b/human-influence-telemetry/releases/tag/v0.1.0
