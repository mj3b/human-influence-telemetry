# Changelog

All notable changes to Human Influence Telemetry are documented here.

The project follows Semantic Versioning for the public technical artifact. Repository release versions are distinct from component versions when the specification, schema, or catalog does not change.

## [Unreleased]

### Planned

- Enroll two scorers independent of the author and of each other
- Collect and preserve two blinded scorer submissions
- Publish the deterministic pre-adjudication comparison
- Classify disagreements and publish an adjudication record without overwriting original scores
- Release v0.3.0 with either a passing or failing human result
- Begin rubric revisions under the v0.4.0 stabilization workstream
- Develop a preregistered prospective validation protocol

### Research boundary

Claim H3 and Maturity Level 2 remain unresolved until two eligible independent human submissions are compared under the locked protocol. A model stress test has no maturity consequence. Adjudication cannot retroactively change the pre-adjudication advancement result.

## [0.2.1] - 2026-07-16

### Added

- Locked blinded inter-rater protocol `HIT-IRP-CIGNA-001`
- Frozen Cigna PxDx scorer packet with a fixed decision boundary and three-source manifest
- Machine-readable scorer-submission schema and neutral submission template
- Deterministic scorer-comparison tool reporting exact agreement, critical disagreements, and supplementary Cohen's kappa
- Synthetic comparison test vectors
- Disagreement taxonomy and adjudication template
- Results directory with an explicit pending-evidence boundary
- Human-readable fixture index explaining each synthetic scenario and its expected finding pattern
- Automated fixture-formatting check requiring two-space indented JSON with a final newline
- Adversarial rubric-friction review `HIT-ARFR-001` and machine-readable friction register
- Coordinator toolkit index and corrected comparison runbook
- Individual scorer-submission validator
- SHA-256 scorer-submission receipt generator
- Independent human-scorer recruitment package
- Separate model-based rubric stress-test protocol `HIT-MST-CIGNA-001`, prompt, schema, template, and pending-result boundary
- DOI-readiness plan and release notes for v0.2.1

### Changed

- README now distinguishes prepared reliability infrastructure from an empirical reliability result
- Repository validation is extended to protocol identifiers, packet identifiers, scorer-schema validity, source-manifest completeness, synthetic comparison behavior, and absence of unsupported result claims
- GitHub Actions now rejects minified or non-canonical deterministic fixture JSON
- The v0.3.0 roadmap now separates protocol completion, scorer enrollment, independent submission, comparison, adjudication, and maturity advancement
- The human protocol is locked on `main`; scoring remains pending because two eligible independent scorers have not yet been enrolled
- Coordinator comparison instructions now use the actual `compare_raters.py` interface: `--format` and `--output`
- Repository release metadata advances to 0.2.1 while the specification, assessment schema, and dimension catalog remain at 0.1.0

### Fixed

- Reformatted all three deterministic fixture records as human-readable, two-space indented JSON without changing assessment IDs, findings, evidence claims, schema versions, or limitations
- Corrected the coordinator operating procedure, which previously referenced unsupported `--json-output` and `--markdown-output` flags
- Decoupled the current repository release from the original v0.2.0 case-study release marker so maintenance releases do not rewrite evidence-pack provenance

### Compatibility

Version 0.2.1 adds research-readiness, coordinator, recruitment, and archival infrastructure. It does not change the 0.1.0 specification, assessment schema, dimension catalog, scoring semantics, or the four public case assessments. Existing v0.2.0 assessments remain structurally compatible and retain their original release provenance.

### Research boundary

The locked human protocol, packet, schema, coordinator tooling, friction review, and model stress-test procedure do not establish human inter-rater reliability. HIT remains at Maturity Level 1 until two eligible independent human submissions are compared under the locked protocol. A software DOI identifies the archived repository artifact; it does not certify the method or imply completion of the human exercise.

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

[Unreleased]: https://github.com/mj3b/human-influence-telemetry/compare/v0.2.1...HEAD
[0.2.1]: https://github.com/mj3b/human-influence-telemetry/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/mj3b/human-influence-telemetry/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/mj3b/human-influence-telemetry/releases/tag/v0.1.0
