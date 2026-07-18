# Changelog

All notable changes to Human Influence Telemetry are documented here.

The project uses Semantic Versioning for the public technical artifact. Research maturity is reported separately.

## [Unreleased]

### Planned

- Replicate human scoring under a compatible current contract
- Produce additional public `0.4.x` assessments
- Conduct a clean-room implementation audit
- Prepare a public release candidate in `0.9.0`
- Develop a preregistered prospective validation protocol

### Research boundary

One passing frozen-packet exercise does not establish general inter-rater reliability, field effectiveness, causal validity, legal correctness, certification, or adoption.

## [0.6.0] - 2026-07-18

### Added

- Two verified independent scorer JSON submissions under locked protocol `HIT-IRP-CIGNA-001`
- Original, correction, receipt, and transcription-verification records
- Deterministic pre-adjudication comparison in JSON and Markdown
- Preservation and release-asset manifests
- No-disagreement adjudication record
- H3 and Maturity Level 2 decision
- ADR-0004
- Human-result release notes and exact-head validation rules

### Result

- Exact agreements: 7 of 7
- Exact-agreement proportion: `1.0000`
- Critical disagreements: 0
- Advancement threshold: met
- Supplementary Cohen's kappa: `null` because all six substantive ratings used one category

### Changed

- Repository version advances to `0.6.0`
- Research maturity advances to Level 2, Applicable
- H3 changes from unresolved to supported for one frozen packet
- Cigna migration disposition changes from protocol-deferred to protocol-completed historical version binding
- Conformance engine remains `0.5.0`
- Specification, schema, catalog, handbook, and scoring semantics remain `0.4.0`

### Research boundary

This release reports one exercise with two scorers, seven categorical items, one retrospective insurance case, and the preserved `0.1.0` scorer contract. It does not estimate population reliability.

## [0.5.0] - 2026-07-18

### Added

- Reusable complete-assessment conformance engine for the `0.4.0` contract
- Public CLI, stable error codes, deterministic reports, compatibility metadata, migration planning, and complete-record vectors

### Compatibility

Version `0.5.0` is implementation-compatible with the `0.4.0` normative assessment contract.

## [0.4.0] - 2026-07-18

### Added

- Evidence states, explicit finding thresholds, dimension-specific rules, Repair triggers, split Telemetry Integrity, actor-authority controls, structured evidence propositions, precise locators, and 48 boundary fixtures

### Compatibility

Version `0.4.0` is a breaking normative and data-contract release. Historical `0.1.0` assessments remain immutable.

## [0.2.1] - 2026-07-16

Added the locked inter-rater protocol, frozen scorer packet, comparison tooling, coordinator materials, recruitment package, rubric-friction review, model stress-test protocol, and archival metadata.

## [0.2.0] - 2026-07-16

Added three public retrospective case narratives and four actor-specific machine-readable assessments.

## [0.1.0] - 2026-07-16

Established the first public HIT specification, schema, catalog, handbook, fixtures, validator, governance files, and release controls.

[Unreleased]: https://github.com/mj3b/human-influence-telemetry/compare/v0.6.0...HEAD
[0.6.0]: https://github.com/mj3b/human-influence-telemetry/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/mj3b/human-influence-telemetry/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/mj3b/human-influence-telemetry/compare/v0.2.1...v0.4.0
[0.2.1]: https://github.com/mj3b/human-influence-telemetry/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/mj3b/human-influence-telemetry/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/mj3b/human-influence-telemetry/releases/tag/v0.1.0
