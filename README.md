# Human Influence Telemetry

**A decision-record method for testing whether formal human oversight retained practical force in AI-mediated institutional decisions.**

Human Influence Telemetry (HIT) evaluates what contemporaneous records can show about human participation in a consequential decision. It does not infer intentions, certify legal compliance, or treat a signature as proof of substantive judgment.

**Status:** Working research specification v0.1.0  
**Current maturity:** Level 1, Defined  
**Concept DOI:** [10.5281/zenodo.21204892](https://doi.org/10.5281/zenodo.21204892)

## Research question

> Can observable decision-record artifacts distinguish substantive human influence from ceremonial human presence in AI-mediated institutional decisions?

## The six-plus-one model

HIT contains six substantive dimensions and one cross-cutting integrity dimension:

1. **Counsel**: Did the human authority have access to the relevant evidence before the decision?
2. **Judgment**: Did the human authority evaluate reasons, alternatives, uncertainty, and context rather than merely restating the system output?
3. **Command**: Could a named human authority approve, reject, modify, stop, or escalate the action?
4. **Correction**: Could an affected person or reviewer contest, interrupt, reverse, or appeal the decision in practice?
5. **Repair**: Did a named actor own remediation after substantiated harm?
6. **Reform**: Did a named authority have power to change the decision architecture that produced the failure?
7. **Telemetry Integrity**: Are the records complete, traceable, resistant to silent alteration, and sufficiently independent to audit?

The first six dimensions assess substantive human influence. Telemetry Integrity evaluates whether the evidence used to score those dimensions can itself be trusted.

## Findings

Each substantive dimension receives one of four findings:

- `0`: absent;
- `1`: present but ceremonial;
- `2`: present and substantively exercised;
- `IE`: insufficient evidence.

`IE` is not converted to zero. Missing evidence and evidence of absence are different findings.

## Current maturity

HIT is a research instrument, not a certified standard.

| Capability | Status |
|---|---|
| Stable construct definitions | Available |
| Machine-readable assessment schema | Initialization in progress |
| Deterministic fixtures | Initialization in progress |
| Retrospective public-record case studies | Completed in source research; public release pending provenance review |
| Inter-rater reliability result | Pending |
| Prospective institutional validation | Pending |
| Legal or standards conformity determination | Not claimed |

## Relationship to adjacent work

- **Governed Decision Intelligence (GDI)** records the institutional decision question, evidence, alternatives, uncertainty, authority, outcome, and conditions.
- **HIT** tests whether the human authority represented in those records had practical force.
- **Decision Evidence Portability Specification (DEPS)** examines what resulting evidence can support across governance regimes and where apparent equivalence fails.
- Runtime governors, audit-event systems, signed-receipt protocols, and portable record standards may supply evidence to HIT. HIT does not replace them.

HIT can be applied to GDI records or to other sufficiently documented institutional decision records.

## Claims boundary

A high HIT finding means the available records show substantive human influence under the published rubric. It does not establish that the decision was correct, lawful, fair, accurate, or harmless.

## Citation

Banasihan, Mark Julius. *Human Influence Telemetry*. Working research specification. Node & Norm, 2026. Concept DOI: 10.5281/zenodo.21204892.

## License

Apache License 2.0.