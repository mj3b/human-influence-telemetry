# Changelog

All notable changes to Human Influence Telemetry are documented here.

The project uses Semantic Versioning for the public technical artifact. Research maturity is reported separately.

## [Unreleased]

### Planned

- Extend complete-record conformance checks in `0.5.0`
- Prepare a public release candidate in `0.9.0`
- Continue neutral recruitment for the locked human inter-rater exercise
- Publish the original human result, passing or failing, under the next available version
- Develop a preregistered prospective validation protocol

### Research boundary

H3 and Maturity Level 2 remain unresolved. Synthetic fixtures and internal conformance checks do not substitute for independent human scoring.

## [0.4.0] - 2026-07-18

### Added

- Evidence-state model: affirmative absence, formal presence, operational capability, observed exercise, and indeterminate
- Explicit thresholds for `0`, `1`, `2`, and `IE`
- Dimension-specific decision rules for Counsel, Judgment, Command, Correction, Repair, and Reform
- Repair trigger states: `triggered`, `not_triggered`, and `indeterminate`
- Separate institutional-record and assessment-packet integrity components
- Deterministic overall Telemetry Integrity derivation
- Sampling and aggregation contract with a dominant-pattern default
- Actor-authority matrix and cross-institution attribution rules
- Contradictory-evidence weighting procedure
- Structured evidence propositions, support relations, and precise locators
- Canonical specification, schema, dimension catalog, handbook, and synthetic example version 0.4.0
- 48 executable accepted, rejected, and boundary fixtures covering `FR-01` through `FR-16`
- Deterministic rubric rule engine under `src/rubric/`
- Migration manifest pinning all four historical assessments by Git blob SHA
- Breaking-change review and 0.1.0-to-0.4.0 migration guide
- Adjacent-system claim audit against Microsoft AGT, ScopeBlind/Acta, Credo AI, GDI, and DEAS
- ADR-0002 approving the normative rule set
- ADR-0003 preserving chronological release versioning
- Archived copies of the superseded 0.1.0 contract and 0.2.1 validator

### Changed

- Repository, specification, assessment schema, and dimension catalog advance to 0.4.0
- `0` now requires affirmative evidence of absence
- `1` now requires process-specific formal presence
- `2` now requires observed exercise or directly demonstrated operational capability under bounded conditions
- `IE` now requires an unresolved proposition and search or request record
- The prior planned `v0.3.0` human-result label is superseded; the eventual result uses the next available repository version
- Validation now covers the canonical 0.4.0 contract, boundary fixtures, historical-case preservation, migration dispositions, locked protocol artifacts, adjacent-system claims, and release metadata

### Compatibility

Version 0.4.0 is a breaking normative and data-contract release. A 0.1.0 assessment does not become a 0.4.0 assessment by changing its version field. Migration requires a fresh bounded reassessment.

The four historical public assessments remain unchanged under schema 0.1.0. Three are `historical_version_bound`; Cigna is `deferred_locked_protocol`. No 0.4.0 public-case findings are claimed.

### Research boundary

Release 0.4.0 remains Maturity Level 1. It does not establish human inter-rater reliability, field effectiveness, legal compliance, certification, causal validity, or independent adoption.

## [0.2.1] - 2026-07-16

### Added

- Locked blinded inter-rater protocol `HIT-IRP-CIGNA-001`
- Frozen Cigna scorer packet and source manifest
- Scorer-submission schema, template, comparison tooling, synthetic vectors, disagreement taxonomy, and adjudication controls
- Adversarial rubric-friction review `HIT-ARFR-001`
- Coordinator, recruitment, and model stress-test infrastructure
- Software-archival metadata and release-readiness documentation

### Compatibility

Added research-readiness infrastructure without changing the 0.1.0 component contracts or historical case findings.

### Research boundary

Prepared infrastructure does not establish independent reviewer agreement.

## [0.2.0] - 2026-07-16

### Added

- Three public retrospective case narratives
- Four actor-specific machine-readable assessments
- Public provenance and evidence-gated roadmap

### Compatibility

Added evidence artifacts without changing the 0.1.0 contract.

### Research boundary

Historical applications do not establish reliability, causal effectiveness, legal liability, certification, or independent adoption.

## [0.1.0] - 2026-07-16

### Added

- Initial public HIT specification
- Six substantive dimensions and Telemetry Integrity
- `0`, `1`, `2`, and `IE`
- Machine-readable schema and catalog
- Basic deterministic fixtures
- Application handbook, research register, provenance, limitations, validator, and release governance

### Research boundary

The foundation release demonstrated structural representation only.

[Unreleased]: https://github.com/mj3b/human-influence-telemetry/compare/v0.4.0...HEAD
[0.4.0]: https://github.com/mj3b/human-influence-telemetry/compare/v0.2.1...v0.4.0
[0.2.1]: https://github.com/mj3b/human-influence-telemetry/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/mj3b/human-influence-telemetry/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/mj3b/human-influence-telemetry/releases/tag/v0.1.0
