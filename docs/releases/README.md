# Human Influence Telemetry Releases

This directory is the repository release index. GitHub release artifacts and downloadable assets are published on the [Releases](https://github.com/mj3b/human-influence-telemetry/releases) page.

## Published releases

| Release | Public meaning | Notes |
|---|---|---|
| [`v0.6.0`](v0.6.0.md) | First bounded human inter-rater result | Two eligible scorers, 7 of 7 exact agreements, zero critical disagreements, Level 2 maturity |
| [`v0.5.0`](v0.5.0.md) | Executable complete-record conformance | Conformance engine `0.5.0` for normative contract `0.4.0` |
| [`v0.4.0`](v0.4.0.md) | Normative rubric stabilization | Specification, schema, catalog, handbook, and 48 boundary fixtures |
| [`v0.2.1`](v0.2.1.md) | Locked research and scorer infrastructure | Frozen protocol, packet, comparison tooling, recruitment materials, archival controls |
| [`v0.2.0`](v0.2.0.md) | Historical public evidence pack | Three narratives and four actor-specific `0.1.0` assessments |
| [`v0.1.0`](v0.1.0.md) | Initial public contract | First specification, schema, catalog, handbook, validator, and governance files |

## Active release train

| Target | Required public claim | Current state |
|---|---|---|
| [`v0.7.0`](v0.7.0-candidate.md) | Locked current-contract protocol and three frozen scorer packets | Candidate architecture complete; human case selection and packet freeze pending |
| `v0.8.0` | Current-contract applications and empirical result, or explicit recruitment disposition | Pending `v0.7.0` publication |
| `v0.9.0` | Stable-release candidate and clean-room implementation audit | Candidate implementation-packet architecture staged |
| `v1.0.0` | Stable public assessment contract suitable for independent implementation | Release prohibited until the gate ledger passes |

The detailed stable-release outline is [`v1.0.0-candidate.md`](v1.0.0-candidate.md).

## Version layers

HIT reports several versions because the repository, normative contract, and executable implementation can change on different schedules.

| Layer | Current version |
|---|---|
| Public repository release | `0.6.0` |
| Normative specification | `0.4.0` |
| Assessment schema | `0.4.0` |
| Dimension catalog | `0.4.0` |
| Application handbook | `0.4.0` |
| Conformance engine | `0.5.0` |
| Research maturity | Level 2, Applicable |

The `v1.0.0` target will synchronize the stable normative and implementation components at `1.0.0`. Research maturity remains a separate evidence claim.

## Publication controls

A candidate document does not authorize a Git tag, GitHub release, DOI archive, workbook activation, recruitment, scoring, or maturity advancement. A numbered release requires exact-commit validation, synchronized metadata, current limitations, accurate citation data, migration records, and release assets whose hashes match the public manifest.

The authoritative readiness documents are:

- [`ROADMAP.md`](../../ROADMAP.md);
- [`docs/v1-readiness-plan.md`](../v1-readiness-plan.md);
- [`release/v1.0.0/contract-freeze.candidate.json`](../../release/v1.0.0/contract-freeze.candidate.json);
- [`implementation/v1.0.0-candidate/`](../../implementation/v1.0.0-candidate/).
