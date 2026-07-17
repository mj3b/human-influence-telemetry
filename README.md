# Human Influence Telemetry

[![HIT Validation](https://github.com/mj3b/human-influence-telemetry/actions/workflows/validate.yml/badge.svg)](https://github.com/mj3b/human-influence-telemetry/actions/workflows/validate.yml)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Status: Working Specification](https://img.shields.io/badge/status-working%20specification-orange.svg)](SPECIFICATION.md)

**A decision-record method for testing whether formal human oversight retained practical force in AI-mediated institutional decisions.**

Human Influence Telemetry (HIT) evaluates what contemporaneous records can show about human participation in a consequential decision. It does not infer intentions, certify legal compliance, or treat a signature as proof of substantive judgment.

**Current release:** 0.2.1  
**Specification version:** 0.1.0  
**Assessment schema version:** 0.1.0  
**Development workstream:** v0.3.0 human inter-rater result, pending eligible scorers; v0.4.0 rubric stabilization  
**Current maturity:** Level 1, Defined  
**Originating research DOI:** [10.5281/zenodo.21204892](https://doi.org/10.5281/zenodo.21204892)  
**Software DOI:** Pending the first successful Zenodo archive of a GitHub release

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

A passing run validates the schema, dimension catalog, deterministic fixtures, released public case assessments, inter-rater protocol artifacts, comparison test vectors, negative cases, release files, and citation metadata.

## Current maturity

HIT is a research instrument, not a certified standard.

| Capability | Status |
|---|---|
| Stable construct definitions | Available |
| Machine-readable assessment schema | Available |
| Deterministic substantive, ceremonial, and insufficient-evidence fixtures | Available |
| Automated positive, negative, case-record, protocol, and metadata validation | Available |
| Retrospective public-record case studies | Released in v0.2.0: three narratives and four actor-specific JSON assessments |
| Blinded inter-rater protocol and comparison tooling | Protocol locked on `main`; coordinator infrastructure available |
| Independent human scorer submissions and reliability result | Pending; no eligible pair enrolled |
| Adversarial rubric-friction review | Available as a non-scoring coordinator artifact |
| Model-based rubric stress test | Protocol prepared; no conforming result claimed |
| Prospective institutional validation | Pending |
| Legal or standards conformity determination | Not claimed |

The released case studies add public evidence, but the repository remains at Level 1 until a documented independent human inter-rater exercise satisfies the Level 2 entry criterion. Protocols, model runs, and tooling do not count as an empirical human result. See [`ROADMAP.md`](ROADMAP.md).

## Public evidence pack

The v0.2.0 evidence pack in [`case-studies/`](case-studies/) contains:

- the Dutch childcare-benefits scandal during the documented harm period;
- the Obermeyer population-health algorithm, separating deploying institutions from the manufacturer;
- Cigna PxDx, including a designed disagreement for inter-rater testing.

These cases demonstrate application of the rubric to heterogeneous public records. They do not establish scoring reliability, causal effectiveness, legal liability, or independent validation.

## v0.3.0 human inter-rater workstream

The [`validation/`](validation/) directory contains the locked blinded protocol, fixed scorer packet, submission schema, deterministic comparison tool, disagreement taxonomy, and adjudication controls.

The release gate still requires two eligible human scorers who are independent of the author and of each other. A passing or failing result will be published without replacing original scores after adjudication. Maturity advancement depends on the predeclared pre-adjudication threshold, not on post-hoc consensus.

The coordinator-only [`validation/adversarial-rubric-friction-review.md`](validation/adversarial-rubric-friction-review.md) identifies plausible construct-level disagreement before any case evidence is scored. It assigns no findings and must not be distributed to scorers before their submissions are locked.

## Model stress-test workstream

[`validation/model-stress-test/`](validation/model-stress-test/) defines a separate exploratory procedure using two fresh language-model sessions. It may expose rubric ambiguity, boundary drift, evidence-weighting differences, and unsupported claims. It does not replace the human exercise, satisfy claim H3, or advance maturity.

## Repository map

| Path | Purpose |
|---|---|
| [`SPECIFICATION.md`](SPECIFICATION.md) | Normative purpose, scope, constructs, findings, and conformance boundary |
| [`RESEARCH.md`](RESEARCH.md) | Research protocol, evidence classes, claim register, and maturity model |
| [`ROADMAP.md`](ROADMAP.md) | Evidence-gated release plan through 1.0.0 |
| [`schema/`](schema/) | Assessment schema and machine-readable dimension catalog |
| [`fixtures/`](fixtures/) | Deterministic substantive, ceremonial, and insufficient-evidence cases |
| [`case-studies/`](case-studies/) | Released public case narratives and actor-specific machine-readable assessments |
| [`validation/`](validation/) | Human protocol, frozen packet, model stress test, friction review, comparison tests, and pending results |
| [`coordinator/`](coordinator/) | Coordinator-only preservation and comparison procedure |
| [`recruitment/`](recruitment/) | Human scorer invitation, eligibility screen, and neutral instructions |
| [`docs/application-handbook.md`](docs/application-handbook.md) | Practitioner application procedure |
| [`LIMITATIONS.md`](LIMITATIONS.md) | Known limitations and interpretation rules |
| [`PROVENANCE.md`](PROVENANCE.md) | Public/private extraction lineage and canonical-source rule |
| [`CHANGELOG.md`](CHANGELOG.md) | Version history and research boundary |
| [`GOVERNANCE.md`](GOVERNANCE.md) | Decision authority and release governance |
| [`docs/doi-and-release-strategy.md`](docs/doi-and-release-strategy.md) | Software DOI and archival strategy |
| [`scripts/validate.py`](scripts/validate.py) | Repository-wide validation command |
| [`scripts/compare_raters.py`](scripts/compare_raters.py) | Deterministic pre-adjudication scorer comparison |
| [`scripts/validate_scorer_submission.py`](scripts/validate_scorer_submission.py) | Individual scorer-submission validation |
| [`scripts/record_submission.py`](scripts/record_submission.py) | SHA-256 receipt generation for unchanged submissions |

## Validation boundary

A passing repository run demonstrates structural validity, deterministic fixture behavior, case-record schema conformance, protocol-artifact consistency, comparison-tool behavior, negative-case rejection, and metadata consistency for the included artifacts. It does not establish scorer independence, scoring reliability, field effectiveness, legal compliance, certification, or independent adoption.

## Relationship to adjacent work

- **[Governed Decision Intelligence](https://github.com/mj3b/governed-decision-intelligence)** records the institutional decision question, evidence, alternatives, uncertainty, authority, outcome, and conditions.
- **HIT** tests whether the human authority represented in those records had practical force.
- **Decision Evidence Portability Specification (DEPS)** examines what resulting evidence may support under different governance regimes and where apparent equivalence fails.
- Runtime governors, audit-event systems, signed-receipt protocols, and portable record standards may supply evidence to HIT. HIT does not replace them.

HIT can be applied to a Governed Decision Record or to another sufficiently documented institutional decision record.

## Claims boundary

A high HIT finding means the available records show substantive human influence under the published rubric. It does not establish that the decision was correct, lawful, fair, accurate, or harmless.

## Citation and DOI status

Use [`CITATION.cff`](CITATION.cff) for repository citation metadata and identify the exact release used. The originating DOI identifies the research concept, not the standalone software. No standalone software DOI has been assigned yet. The first successful Zenodo archive of a GitHub release should establish a HIT software concept DOI and a version DOI. See the [DOI and release strategy](docs/doi-and-release-strategy.md).

## Contributing and security

See [`CONTRIBUTING.md`](CONTRIBUTING.md), [`GOVERNANCE.md`](GOVERNANCE.md), [`SECURITY.md`](SECURITY.md), and [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## License

Apache License 2.0. See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).
