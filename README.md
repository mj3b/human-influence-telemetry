# Human Influence Telemetry

[![HIT Validation](https://github.com/mj3b/human-influence-telemetry/actions/workflows/validate.yml/badge.svg)](https://github.com/mj3b/human-influence-telemetry/actions/workflows/validate.yml)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Status: Working Specification](https://img.shields.io/badge/status-working%20specification-orange.svg)](SPECIFICATION.md)

**An open documentary assurance method for evaluating whether human authority retained practical force in AI-mediated institutional decisions.**

HIT evaluates what contemporaneous records establish about human access, judgment, authority, correction, repair, and reform. It does not infer intention, certify legal compliance, perform runtime enforcement, or treat a signature as proof of substantive judgment.

**Current release:** 0.4.0  
**Specification version:** 0.4.0  
**Assessment schema version:** 0.4.0  
**Dimension catalog version:** 0.4.0  
**Current maturity:** Level 1, Defined  
**Human reliability claim:** Unresolved  
**Originating research DOI:** [10.5281/zenodo.21204892](https://doi.org/10.5281/zenodo.21204892)  
**Software DOI:** Pending a successful standalone software archive

## Research question

> Can observable records distinguish substantive human influence from ceremonial human presence in AI-mediated institutional decisions?

## Six substantive dimensions plus Telemetry Integrity

1. **Counsel:** Did a named human authority have actual pre-decision access to relevant underlying evidence?
2. **Judgment:** Did the authority independently evaluate reasons, alternatives, uncertainty, and context?
3. **Command:** Could the authority practically approve, reject, modify, stop, or escalate?
4. **Correction:** Could the decision be contested, interrupted, reconsidered, modified, reversed, or appealed in practice?
5. **Repair:** After qualifying harm, did a named actor own and deliver remediation to affected persons?
6. **Reform:** Did a named authority have and exercise power to change the decision architecture?
7. **Telemetry Integrity:** Can the institutional records and the assessment packet be trusted as bounded audit evidence?

## Findings

- `0`: absent; requires affirmative evidence of absence;
- `1`: present but ceremonial; requires process-specific formal presence;
- `2`: present and substantively exercised; requires observed exercise or directly demonstrated operational capability;
- `IE`: insufficient evidence; records an unresolved evidentiary state.

`IE` is not converted to zero and is not averaged into an ordinal total.

## What changed in 0.4.0

Release `0.4.0` is a breaking normative and data-contract revision. It resolves all 16 ambiguity classes in the public friction register by adding:

- affirmative-absence, formal-presence, operational-capability, observed-exercise, and indeterminate evidence states;
- explicit finding thresholds;
- dimension-specific decision rules;
- a Repair trigger;
- split institutional-record and assessment-packet integrity;
- deterministic overall integrity derivation;
- sampling and aggregation declarations;
- actor-authority attribution;
- contradictory-evidence rules;
- structured evidence propositions and precise locators;
- 48 executable boundary fixtures.

See [`docs/breaking-change-review-v0.4.0.md`](docs/breaking-change-review-v0.4.0.md) and [`docs/migration-guide-v0.1.0-to-v0.4.0.md`](docs/migration-guide-v0.1.0-to-v0.4.0.md).

## Quick start

```bash
git clone https://github.com/mj3b/human-influence-telemetry.git
cd human-influence-telemetry
python -m pip install --requirement requirements-dev.txt
python scripts/validate.py
```

A passing run validates the released `0.4.0` contract, canonical synthetic example, 48 boundary fixtures, historical case preservation, migration dispositions, locked protocol artifacts, adjacent-system claim boundaries, and release metadata.

## Research status

HIT remains a research instrument, not a certified standard.

| Capability | Status |
|---|---|
| Normative 0.4.0 rubric | Released |
| Machine-readable 0.4.0 assessment schema and catalog | Released |
| 48 accepted, rejected, and boundary fixtures | Released |
| Historical public case studies | Four `0.1.0` assessments preserved |
| Public-case 0.4.0 migrations | Not claimed; explicit exceptions recorded |
| Locked human inter-rater protocol | Available under 0.1.0 contract |
| Independent human submissions and reliability result | Pending; no eligible pair enrolled |
| Prospective institutional validation | Pending |
| Legal or standards conformity determination | Not claimed |

The locked human exercise remains the entry condition for claim H3 and Maturity Level 2. The previous planned `v0.3.0` result label is superseded; the result must use the next available repository version when completed. Its original submissions and pre-adjudication result must be published, passing or failing.

## Historical public evidence pack

The `case-studies/` directory contains three retrospective narratives and four actor-specific machine-readable assessments released under specification and schema `0.1.0`:

- Dutch childcare-benefits harm-period assessment;
- Obermeyer deployer and manufacturer assessments;
- Cigna PxDx assessment.

They remain immutable historical artifacts. Three are `historical_version_bound`; Cigna is `deferred_locked_protocol`. No `0.4.0` case finding is claimed. See [`case-studies/migrations/v0.4.0/`](case-studies/migrations/v0.4.0/).

## Project structure

```text
src/
  rubric/                         -- Deterministic 0.4.0 boundary-rule evaluators
schema/
  hit-assessment.schema.json      -- Canonical public assessment contract
  hit-dimension-catalog.json      -- Canonical construct and rule catalog
  candidates/                     -- Development and migration schemas retained for provenance
fixtures/
  v0.4.0-canonical-example.json   -- Canonical synthetic assessment
  v0.4.0-boundaries/              -- 48 executable ambiguity fixtures
case-studies/
  assessments/                    -- Immutable historical 0.1.0 records
  migrations/v0.4.0/              -- Explicit migration dispositions
validation/                       -- Locked human and model protocols
coordinator/                      -- Submission preservation and comparison procedures
recruitment/                      -- Neutral human-scorer materials
docs/                             -- Handbook, decisions, boundaries, migration, and releases
archive/v0.1.0/                   -- Superseded public contract preserved for reproducibility
scripts/                          -- Repository, boundary, migration, and protocol validation
```

## Relationship to adjacent systems

- **Microsoft Agent Governance Toolkit** enforces and audits runtime actions. Its events may supply evidence to HIT; HIT does not enforce actions.
- **ScopeBlind/Acta** verifies signed-receipt integrity and interoperability. Verified receipts may strengthen provenance; HIT does not define or verify that protocol.
- **Credo AI** provides policy packs, risk and control mappings, governance workflows, evidence collection, and runtime governance. HIT does not provide policy packs, compliance automation, or universal control mappings.
- **Governed Decision Intelligence** structures consequential decisions in Governed Decision Records.
- **Decision Evidence Applicability Specification** evaluates what evidence may support under a specified requirement and where equivalence fails.

See [`docs/adjacent-system-boundaries.md`](docs/adjacent-system-boundaries.md) and the [`0.4.0` claim audit](docs/adjacent-system-claim-audit-v0.4.0.md).

## What HIT does not implement

HIT does not intercept, allow, deny, block, sandbox, or terminate agent actions. It does not compile policy into runtime configuration, verify agent identity or privileges, create signed receipts, provide cryptographic receipt conformance, supply policy packs, automate legal compliance, declare evidentiary admissibility, or make governance evidence portable across regimes.

## Claims boundary

A high HIT finding means the available records satisfy the published documentary rubric. It does not establish that the decision was correct, lawful, fair, accurate, harmless, or morally justified.

## Citation and DOI status

Use [`CITATION.cff`](CITATION.cff) and identify the exact release. The originating DOI identifies the research concept, not a standalone software version. No standalone software DOI has been assigned yet.

## License

Apache License 2.0. See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).
