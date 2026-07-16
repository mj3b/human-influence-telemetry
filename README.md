# Human Influence Telemetry

[![HIT Validation](https://github.com/mj3b/human-influence-telemetry/actions/workflows/validate.yml/badge.svg)](https://github.com/mj3b/human-influence-telemetry/actions/workflows/validate.yml)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Status: Working Specification](https://img.shields.io/badge/status-working%20specification-orange.svg)](SPECIFICATION.md)

**A decision-record method for testing whether formal human oversight retained practical force in AI-mediated institutional decisions.**

Human Influence Telemetry (HIT) evaluates what contemporaneous records can show about human participation in a consequential decision. It does not infer intentions, certify legal compliance, or treat a signature as proof of substantive judgment.

**Version:** 0.1.0  
**Current maturity:** Level 1, Defined  
**Originating research DOI:** [10.5281/zenodo.21204892](https://doi.org/10.5281/zenodo.21204892)  
**Software DOI:** Pending archival of the first GitHub release

## Research question

> Can observable decision-record artifacts distinguish substantive human influence from ceremonial human presence in AI-mediated institutional decisions?

## The six-plus-one model

HIT contains six substantive dimensions and one cross-cutting integrity dimension:

1. **Counsel:** Did the human authority have access to the relevant evidence before the decision?
2. **Judgment:** Did the human authority evaluate reasons, alternatives, uncertainty, and context rather than merely restating the system output?
3. **Command:** Could a named human authority approve, reject, modify, stop, or escalate the action?
4. **Correction:** Could an affected person or reviewer contest, interrupt, reverse, or appeal the decision in practice?
5. **Repair:** Did a named actor own remediation after substantiated harm?
6. **Reform:** Did a named authority have power to change the decision architecture that produced the failure?
7. **Telemetry Integrity:** Are the records complete, traceable, resistant to silent alteration, and sufficiently independent to audit?

The first six dimensions assess substantive human influence. Telemetry Integrity evaluates whether the evidence used to assess those dimensions can itself be trusted.

## Findings

Each substantive dimension receives one of four findings:

- `0`: absent;
- `1`: present but ceremonial;
- `2`: present and substantively exercised;
- `IE`: insufficient evidence.

`IE` is not converted to zero. Missing evidence and evidence of absence are different findings.

## Quick start

```bash
git clone https://github.com/mj3b/human-influence-telemetry.git
cd human-influence-telemetry
python -m pip install --requirement requirements-dev.txt
python scripts/validate.py
```

A passing run validates the schema, dimension catalog, included fixtures, negative cases, release files, and synchronized citation metadata.

## Current maturity

HIT is a research instrument, not a certified standard.

| Capability | Status |
|---|---|
| Stable construct definitions | Available |
| Machine-readable assessment schema | Available |
| Deterministic substantive, ceremonial, and insufficient-evidence fixtures | Available |
| Automated positive, negative, and metadata validation | Available |
| Retrospective public-record case studies | Completed in source research; public release pending provenance review |
| Inter-rater reliability result | Pending |
| Prospective institutional validation | Pending |
| Legal or standards conformity determination | Not claimed |

## Repository map

| Path | Purpose |
|---|---|
| [`SPECIFICATION.md`](SPECIFICATION.md) | Normative purpose, scope, constructs, findings, and conformance boundary |
| [`RESEARCH.md`](RESEARCH.md) | Research protocol, evidence classes, claim register, and maturity model |
| [`schema/`](schema/) | Assessment schema and machine-readable dimension catalog |
| [`fixtures/`](fixtures/) | Deterministic substantive, ceremonial, and insufficient-evidence cases |
| [`docs/application-handbook.md`](docs/application-handbook.md) | Practitioner application procedure |
| [`LIMITATIONS.md`](LIMITATIONS.md) | Known limitations and interpretation rules |
| [`PROVENANCE.md`](PROVENANCE.md) | Public/private extraction lineage and canonical-source rule |
| [`CHANGELOG.md`](CHANGELOG.md) | Version history and research boundary |
| [`GOVERNANCE.md`](GOVERNANCE.md) | Decision authority and release governance |
| [`docs/doi-and-release-strategy.md`](docs/doi-and-release-strategy.md) | Software DOI and archival strategy |
| [`scripts/validate.py`](scripts/validate.py) | Repository-wide validation command |

## Validation boundary

A passing run demonstrates structural validity, deterministic fixture behavior, negative-case rejection, and metadata synchronization for the included artifacts. It does not establish scoring reliability, field effectiveness, legal compliance, certification, or independent adoption.

## Relationship to adjacent work

- **[Governed Decision Intelligence](https://github.com/mj3b/governed-decision-intelligence)** records the institutional decision question, evidence, alternatives, uncertainty, authority, outcome, and conditions.
- **HIT** tests whether the human authority represented in those records had practical force.
- **Decision Evidence Portability Specification (DEPS)** examines what resulting evidence can support across governance regimes and where apparent equivalence fails.
- Runtime governors, audit-event systems, signed-receipt protocols, and portable record standards may supply evidence to HIT. HIT does not replace them.

HIT can be applied to a Governed Decision Record or to another sufficiently documented institutional decision record.

## Claims boundary

A high HIT finding means the available records show substantive human influence under the published rubric. It does not establish that the decision was correct, lawful, fair, accurate, or harmless.

## Citation and DOI status

Use [`CITATION.cff`](CITATION.cff) for citation metadata. The DOI above identifies the originating research concept, not the standalone software release. Zenodo should assign a separate software concept DOI and version DOI when tag `v0.1.0` is archived. See the [DOI and release strategy](docs/doi-and-release-strategy.md).

## Contributing and security

See [`CONTRIBUTING.md`](CONTRIBUTING.md), [`GOVERNANCE.md`](GOVERNANCE.md), [`SECURITY.md`](SECURITY.md), and [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## License

Apache License 2.0. See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).
