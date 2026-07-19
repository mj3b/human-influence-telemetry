# Human Influence Telemetry

[![HIT Validation](https://github.com/mj3b/human-influence-telemetry/actions/workflows/validate.yml/badge.svg)](https://github.com/mj3b/human-influence-telemetry/actions/workflows/validate.yml)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Public release: v0.6.0](https://img.shields.io/badge/public%20release-v0.6.0-blue.svg)](https://github.com/mj3b/human-influence-telemetry/releases/tag/v0.6.0)
[![v1 readiness: active](https://img.shields.io/badge/v1%20readiness-active-orange.svg)](docs/v1-readiness-plan.md)

**An open documentary assurance method for evaluating whether human authority retained practical force in AI-mediated institutional decisions.**

HIT evaluates what contemporaneous records establish about human access, judgment, authority, correction, repair, and reform. It does not infer intention, certify legal compliance, perform runtime enforcement, or treat a signature as proof of substantive judgment.

**Current public release:** `0.6.0`  
**Stable-release target:** `1.0.0`, readiness work active, release prohibited  
**Conformance engine version:** `0.5.0`  
**Specification version:** `0.4.0`  
**Assessment schema version:** `0.4.0`  
**Dimension catalog version:** `0.4.0`  
**Current maturity:** Level 2, Applicable  
**Human reliability claim:** Supported for one frozen packet under `HIT-IRP-CIGNA-001`  
**Originating research DOI:** [10.5281/zenodo.21204892](https://doi.org/10.5281/zenodo.21204892)  
**Software DOI:** Pending a successful standalone software archive

## Current release position

The public release remains `v0.6.0`. The repository now contains the release controls, manual-workbook contract, clean-room implementation-packet architecture, and machine-readable gate ledger needed to advance through `v0.7.0`, `v0.8.0`, `v0.9.0`, and `v1.0.0`.

| Release | Meaning | Status |
|---|---|---|
| `v0.6.0` | First bounded human inter-rater result | Published |
| `v0.7.0` | Locked current-contract protocol and three frozen scorer packets | Active workstream |
| `v0.8.0` | Current-contract applications and empirical result, or an explicit recruitment disposition | Pending |
| `v0.9.0` | Public stable-release candidate and clean-room implementation audit | Pending |
| `v1.0.0` | Stable public assessment contract suitable for independent implementation | Release prohibited until all gates pass |

Version `1.0.0` is a compatibility and implementation claim. It will not establish population reliability, causal effectiveness, legal conformity, certification, or independent adoption. See [`ROADMAP.md`](ROADMAP.md), [`docs/v1-readiness-plan.md`](docs/v1-readiness-plan.md), and [`docs/releases/v1.0.0-candidate.md`](docs/releases/v1.0.0-candidate.md).

## Research question

> Can observable records distinguish substantive human influence from ceremonial human presence in AI-mediated institutional decisions?

## Six substantive dimensions plus Telemetry Integrity

1. **Counsel:** Did a named human authority have actual pre-decision access to relevant underlying evidence?
2. **Judgment:** Did the authority independently evaluate reasons, alternatives, uncertainty, and context?
3. **Command:** Could the authority practically approve, reject, modify, stop, or escalate?
4. **Correction:** Could the decision be contested, interrupted, reconsidered, modified, reversed, or appealed in practice?
5. **Repair:** After qualifying harm, did a named actor own and deliver remediation to affected persons?
6. **Reform:** Did a named authority have and exercise power to change the decision architecture?
7. **Telemetry Integrity:** Can the institutional records and assessment packet be trusted as bounded audit evidence?

## Findings

- `0`: absent; requires affirmative evidence of absence;
- `1`: present but ceremonial; requires process-specific formal presence;
- `2`: present and substantively exercised; requires observed exercise or directly demonstrated operational capability;
- `IE`: insufficient evidence; records an unresolved evidentiary state.

`IE` is not converted to zero and is not averaged into an ordinal total.

## Human inter-rater result

Release `0.6.0` publishes the first completed locked human exercise.

Two eligible independent scorers applied frozen packet `HIT-IR-CIGNA-PXDX-001` under the preserved `0.1.0` scorer contract. The pre-adjudication comparison produced:

- 7 of 7 exact agreements;
- exact-agreement proportion `1.0000`;
- zero critical disagreements;
- advancement threshold met.

Both scorers assigned `1` to Counsel, Judgment, Command, Correction, Repair, and Reform. Both assigned `limited` to Telemetry Integrity.

Supplementary Cohen's kappa is `null` because all six substantive ratings fell in one category. The data contain no category variance for chance-corrected estimation. The primary exact-agreement measure remains defined and passed.

See [`validation/results/`](validation/results/), [`RESEARCH.md`](RESEARCH.md), and [ADR-0004](docs/decisions/ADR-0004-advance-hit-to-maturity-level-2.md).

## v1 readiness architecture

The repository now includes:

- a machine-readable `v1.0.0` gate ledger under [`release/v1.0.0/`](release/v1.0.0/);
- a candidate stable-release outline under [`docs/releases/v1.0.0-candidate.md`](docs/releases/v1.0.0-candidate.md);
- a standalone clean-room implementation packet under [`implementation/v1.0.0-candidate/`](implementation/v1.0.0-candidate/);
- clean-room audit protocol `HIT-CRI-V100-001`;
- draft manual workbooks for Scorers A, B, and C under the `v0.7.0` workbook contract;
- CI controls that prevent premature scoring, audit activation, component promotion, or `v1.0.0` release.

The immediate blocking gate is a signed human selection of one exercise-rich, one constraint-rich, and one evidence-limited case. Packet IDs, recruitment, scoring, and clean-room audit remain prohibited.

## Release layers

Release `0.4.0` stabilized the normative assessment contract. It introduced evidence states, explicit finding thresholds, dimension-specific rules, Repair triggers, split Telemetry Integrity, sampling and aggregation declarations, actor-authority attribution, contradiction handling, structured evidence propositions, precise locators, and 48 executable boundary fixtures.

Release `0.5.0` added executable complete-record conformance without changing the `0.4.0` contract.

Release `0.6.0` publishes the bounded human agreement result. It changes research maturity and claim status. It does not change the `0.4.0` specification, schema, catalog, handbook, or scoring semantics, and it does not change the `0.5.0` conformance engine.

The `v0.7.0` through `v1.0.0` sequence separates empirical evidence, release-candidate review, and stable-contract promotion. This prevents version numbers from being treated as substitutes for evidence.

## Quick start

```bash
git clone https://github.com/mj3b/human-influence-telemetry.git
cd human-influence-telemetry
python -m pip install --requirement requirements-dev.txt

python -m src conformance --all
python -m src conformance --path assessment.json
python -m src migration-plan --path historical-assessment.json
```

The complete-record engine checks cross-record references, evidence relations, actor attribution, finding and evidence-state consistency, Repair triggers, Telemetry Integrity derivation, aggregation scope, citation precision, and protected migration behavior.

A passing conformance report establishes assessment-contract conformance for the supplied record. It does not establish evidentiary truth, legal sufficiency, certification, or institutional effectiveness.

## Research status

HIT remains a research instrument, not a certified standard.

| Capability | Status |
|---|---|
| Normative 0.4.0 rubric | Released |
| Machine-readable 0.4.0 assessment schema and catalog | Released |
| 48 accepted, rejected, and boundary fixtures | Released |
| Complete-record executable conformance | Released in 0.5.0 |
| Historical public case studies | Four `0.1.0` assessments preserved |
| Public-case 0.4.0 migrations | Not claimed; explicit exceptions recorded |
| Locked human inter-rater protocol | Completed under the 0.1.0 scorer contract |
| Independent human submissions | Two verified submissions published |
| Pre-adjudication result | 7 / 7 exact agreement; zero critical disagreements |
| H3 | Supported for one frozen packet |
| Research maturity | Level 2, Applicable |
| Current-contract replication architecture | Candidate protocol and controls complete |
| Manual scorer workbooks | Draft assets complete; scoring prohibited |
| Clean-room implementation packet | Candidate architecture complete; audit prohibited |
| Stable `v1.0.0` contract | Pending release gates |
| Prospective institutional validation | Pending |
| Legal or standards conformity determination | Not claimed |

The completed exercise supports reproducibility for one frozen packet. General reliability across sectors, evidence conditions, scorer populations, and contract versions remains unresolved.

## Historical public evidence pack

The `case-studies/` directory contains three retrospective narratives and four actor-specific machine-readable assessments released under specification and schema `0.1.0`.

They remain immutable historical artifacts. No `0.4.0` public-case finding is claimed. The Cigna protocol is complete, but a current-contract Cigna reassessment would require a separate fresh source review.

## Project structure

```text
src/                              -- Public CLI and conformance implementation
compatibility/                    -- Supported contracts and migration rules
schema/                           -- Canonical assessment schema and dimension catalog
fixtures/                         -- Boundary and complete-record test vectors
case-studies/                     -- Historical 0.1.0 records and migration dispositions
validation/                       -- Human submissions, receipts, results, and v0.7.0 controls
implementation/v1.0.0-candidate/ -- Clean-room implementation packet and audit protocol
release/v1.0.0/                  -- Machine-readable stable-release gate ledger
coordinator/                      -- Submission preservation and comparison procedures
recruitment/                      -- Neutral human-scorer materials
docs/releases/                   -- Published notes and candidate release outlines
archive/v0.1.0/                  -- Superseded contract preserved for reproducibility
scripts/                          -- Release validation and CLI smoke tests
```

## Relationship to adjacent systems

- **Microsoft Agent Governance Toolkit** enforces and audits runtime actions. Its events may supply evidence to HIT; HIT does not enforce actions.
- **ScopeBlind/Acta** verifies signed-receipt integrity and interoperability. Verified receipts may strengthen provenance; HIT does not define or verify that protocol.
- **Credo AI** provides policy packs, risk and control mappings, governance workflows, evidence collection, and runtime governance. HIT does not provide policy packs, compliance automation, or universal control mappings.
- **Governed Decision Intelligence** structures consequential decisions in Governed Decision Records.
- **Decision Evidence Applicability Specification** evaluates what evidence may support under a specified requirement and where equivalence fails.

## What HIT does not implement

HIT does not intercept, allow, deny, block, sandbox, or terminate agent actions. It does not compile policy into runtime configuration, verify agent identity or privileges, create signed receipts, provide cryptographic receipt conformance, supply policy packs, automate legal compliance, declare evidentiary admissibility, or make governance evidence portable across regimes.

## Claims boundary

A high HIT finding means the available records satisfy the published documentary rubric. It does not establish that the decision was correct, lawful, fair, accurate, harmless, or morally justified.

The `0.6.0` result shows that two independent reviewers reached the declared threshold on one frozen packet. It does not estimate population reliability.

The v1 readiness architecture shows that the repository has a controlled path to a stable contract. It does not establish that the remaining human, clean-room, or release gates have passed.

## Releases, citation, and DOI status

The release index is [`docs/releases/README.md`](docs/releases/README.md). GitHub release artifacts are published at the repository [Releases](https://github.com/mj3b/human-influence-telemetry/releases) page.

Use [`CITATION.cff`](CITATION.cff) and identify the exact published release. The citation file remains at `0.6.0` until a later numbered release is actually published. The originating DOI identifies the research concept, not a standalone software version. No standalone software DOI has been assigned yet.

## License

Apache License 2.0. See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).
