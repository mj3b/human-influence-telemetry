# Human Influence Telemetry Specification

**Status:** Working specification  
**Version:** 0.1.0  
**Author:** Mark Julius Banasihan  
**ORCID:** 0009-0001-8121-2878  
**Concept DOI:** 10.5281/zenodo.21204892

## 1. Purpose

Human Influence Telemetry (HIT) is a documentary assurance method for evaluating whether formal human oversight retained practical force in an AI-mediated institutional decision process.

The unit of analysis is one defined decision process, within one institutional unit, over one bounded period.

## 2. Scope

HIT evaluates records. It does not infer unrecorded intentions, evaluate model quality, certify legal compliance, or determine whether an outcome was substantively correct.

HIT may consume governed decision records, case-management records, access logs, reviewer notes, authority records, override and escalation events, appeal registers, remediation records, system-change records, and provenance metadata.

## 3. Construct model

### 3.1 Substantive dimensions

#### Counsel

**Question:** Did the human authority have access to the relevant evidence before the decision?

**Passing evidence:** records showing access to underlying evidence, not only an AI score, ranking, summary, or recommendation.

**Failure signs:** the reviewer sees only a compressed output; relevant particulars remain inaccessible; access occurs only after the decision.

#### Judgment

**Question:** Did the human authority evaluate reasons, alternatives, uncertainty, and context?

**Passing evidence:** independent reasons, alternatives considered, documented disagreement, or a recorded modification of the system recommendation.

**Failure signs:** boilerplate acceptance; near-total recommendation adoption without reasons; review time inconsistent with substantive evaluation.

#### Command

**Question:** Could a named human authority direct otherwise?

**Passing evidence:** documented authority to approve, reject, modify, stop, or escalate, with at least one exercised instance where the sample permits.

**Failure signs:** approval is frictionless while override is practically unavailable; a vendor or technical system controls meaningful intervention; human action is limited to ratification.

#### Correction

**Question:** Could the decision be contested, interrupted, reversed, or appealed in practice?

**Passing evidence:** an operative appeal or escalation path with at least one substantive reconsideration, reversal, or interruption.

**Failure signs:** formal appeal channels with no effect; template dispositions; unresolved appeals; no interruption capability.

#### Repair

**Question:** Did a named actor own remediation after substantiated harm?

**Passing evidence:** restitution, corrected records, notification, and named remediation ownership.

**Failure signs:** harm is acknowledged without remedy; the model or process is corrected while affected persons remain unrepaired.

#### Reform

**Question:** Did a named authority have power to change the decision architecture itself?

**Passing evidence:** authorized threshold changes, workflow redesign, model retirement, control redesign, or governance reform linked to a documented failure.

**Failure signs:** local compensation without system change; the same failure architecture persists elsewhere; vendors alone control material changes.

### 3.2 Cross-cutting dimension

#### Telemetry Integrity

**Question:** Can the evidence used to assess the six substantive dimensions be trusted as an audit record?

Telemetry Integrity evaluates provenance, completeness, edit authority, independence from the governed system, tamper evidence, retention, missing-record disclosure, and consistency across related records.

Telemetry Integrity is reported separately because poor record integrity can invalidate confidence in every substantive finding.

## 4. Findings

Each substantive dimension receives one of four findings:

- `0`: absent;
- `1`: present but ceremonial;
- `2`: present and substantively exercised;
- `IE`: insufficient evidence.

A finding of `1` means the institution preserved the form of oversight without evidence that the practice could alter the decision path.

A finding of `2` requires observable evidence that the relevant human capacity affected, or could credibly have affected, the decision path.

`IE` records that the method cannot distinguish absence from unavailable evidence. It must not be averaged into an ordinal total.

## 5. Assessment record

A conforming HIT assessment must identify the assessment and schema versions, institutional unit, decision process, bounded period, sampling rule, evidence requested and received, one finding per substantive dimension, one Telemetry Integrity finding, assessor identity, limitations, unresolved ambiguities, and artifact provenance.

## 6. Conformance

A record conforms structurally when it validates against `schema/hit-assessment.schema.json`.

Structural conformance does not establish scoring correctness. Substantive conformance additionally requires application of the published rubric and traceable evidence citations.

## 7. Relationship to GDI

A Governed Decision Record may supply HIT inputs, including decision authority, evidence access, recorded reasoning, conditions, escalation, and audit metadata. HIT remains independent of GDI and may be applied to other decision-record systems.

## 8. Non-claims

HIT does not claim that human involvement is always preferable to automation, that a high finding proves a good decision, that a low finding proves unlawful conduct, that recorded reasoning is truthful, or that the framework is statistically validated or independently adopted.

## 9. Advancement criteria

Version 1.0 should not be declared stable until:

1. the schema and catalog are internally consistent;
2. deterministic fixtures cover substantive, ceremonial, and insufficient-evidence cases;
3. two independent scorers apply the method to the same fixture;
4. disagreement handling is documented;
5. at least three public-record case studies are released with source provenance;
6. limitations and update conditions are current;
7. the repository passes automated validation.