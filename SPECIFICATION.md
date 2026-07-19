# Human Influence Telemetry Specification

**Status:** Released pre-1.0 normative contract  
**Version:** 0.4.0  
**Released:** 2026-07-18  
**Predecessor:** 0.1.0  
**Stable target:** 1.0.0, gated candidate  
**Author:** Mark Julius Banasihan  
**ORCID:** 0009-0001-8121-2878  
**Originating concept DOI:** 10.5281/zenodo.21204892  
**Current repository research maturity:** Level 2, Applicable

This file remains the released `0.4.0` normative contract. The `1.0.0` readiness work does not change its scoring semantics. Any promotion to `1.0.0` requires synchronized specification, schema, catalog, handbook, implementation, migration, audit, and exact-release validation.

## 1. Purpose

Human Influence Telemetry (HIT) is a documentary assurance method for evaluating whether formal human oversight retained practical force in an AI-mediated institutional decision process.

HIT evaluates what observable, time-bounded records establish about human access, judgment, authority, correction, repair, and reform. It does not infer unrecorded intention, evaluate model quality, certify legal compliance, determine whether an outcome was substantively correct, or enforce agent actions at runtime.

## 2. Unit of analysis

The unit of analysis is one defined decision process, within one identified institutional unit, over one bounded period or one explicitly declared event.

Before evidence review begins, the assessment must declare:

- institutional unit and decision process;
- AI-system role and stated human role;
- period or event boundary and any follow-up period;
- population or record universe;
- sampling and aggregation rules;
- material actors and authority relationships;
- known exclusions and likely selection effects.

A boundary may be revised only when the change, reason, timing, and effect are recorded.

## 3. System and terminology boundary

### 3.1 Documentary telemetry

In HIT, telemetry means observable, time-bounded documentary evidence that may reveal whether human influence existed and had practical force. It does not mean a runtime observability SDK, tracing system, event collector, agent middleware, policy engine, or enforcement layer.

### 3.2 HIT assessment record

A HIT assessment record is the structured evidentiary analysis produced under this specification. It is not a runtime decision log, signed receipt, policy pack, compliance certificate, or portable proof of legal conformity.

### 3.3 Institutional decision

An institutional decision is a consequential determination made through an organizational process that allocates benefits, burdens, access, treatment, status, rights, obligations, or remedies.

## 4. Evidence states

Each substantive finding must use one evidence state:

- **affirmative_absence:** reliable evidence establishes that the relevant human function did not exist, could not operate, or was systematically unavailable;
- **formal_presence:** a process-specific human role or authority existed, but the record does not establish substantive exercise;
- **operational_capability:** the actor had a directly demonstrated ability to exercise the function, although the record may not show use in the assessed event;
- **observed_exercise:** the record shows the function was exercised within the declared boundary;
- **indeterminate:** the packet cannot distinguish absence, presence, capability, or exercise after a documented search or request.

Documentary silence alone is not affirmative absence.

## 5. Findings

Each substantive dimension must receive exactly one finding:

- `0`: absent, supported only by `affirmative_absence`;
- `1`: present but ceremonial, supported only by `formal_presence`;
- `2`: substantively present, supported by `operational_capability` or `observed_exercise`;
- `IE`: insufficient evidence, supported only by `indeterminate`.

`IE` is an evidentiary result. It must not be converted to `0`, imputed, averaged, or used as a neutral midpoint.

## 6. Substantive dimensions

### 6.1 Counsel

Counsel measures whether a named human authority had timely access to the evidence needed to influence the decision before the decision became effective.

A formal notification or dashboard access supports `1` only when it is process-specific and linked to the decision stage. A finding of `2` requires observed pre-decision access or a directly tested capability that the actor could use in the assessed process.

### 6.2 Judgment

Judgment measures whether a named human authority independently evaluated reasons, alternatives, uncertainty, context, and consequences.

A signature, click, or acknowledgment does not by itself establish judgment. A finding of `2` requires records of independent evaluation or a directly demonstrated deliberative process.

### 6.3 Command

Command measures whether a named human authority could practically approve, reject, modify, stop, defer, or escalate the decision.

Formal authority supports `1` when operational use remains unestablished. A finding of `2` requires observed exercise or directly demonstrated operational capability within the decision architecture.

### 6.4 Correction

Correction measures whether a decision could be contested, interrupted, reconsidered, modified, reversed, or appealed in practice.

A published appeal channel supports `1` only when it applies to the assessed process. A finding of `2` requires observed correction or a directly demonstrated operational correction pathway.

### 6.5 Repair

Repair measures whether, after qualifying harm, a named actor owned and delivered remediation to affected persons.

Repair is assessed only when the harm trigger is `triggered`, `not_triggered`, or `indeterminate`.

- `triggered` means the record substantiates material harm within the declared boundary;
- `not_triggered` means reliable evidence establishes that the qualifying harm condition did not occur;
- `indeterminate` means the packet cannot resolve whether the trigger occurred.

An indeterminate Repair trigger requires finding `IE`. General policy reform, apology, settlement, or process improvement does not by itself establish person-level Repair.

### 6.6 Reform

Reform measures whether a named authority had and exercised power to change the decision architecture itself, including rules, thresholds, data use, system configuration, escalation structure, or institutional assignment of authority.

Later reform may be recorded as follow-up evidence, but it does not retroactively change an earlier period-level finding unless the assessment predeclares a temporal rule permitting that inference.

## 7. Actor and authority attribution

Every material actor must be represented separately. Evidence may be attributed only to the actor whose institutional identity, authority, mechanism, and decision stage are supported by the record.

Conduct by a vendor, deployer, regulator, court, corporate affiliate, affected person, or external reviewer must not be assigned to another actor without evidence of authority, delegation, control, or agency.

## 8. Evidence claims

Every finding must trace to structured evidence claims. Each claim must identify:

- artifact and source;
- precise locator;
- proposition;
- whether the source supports, contradicts, or limits the proposition;
- affected dimensions and actors;
- provenance and independence status;
- transformation history.

A source reference without a proposition and locator is not sufficient evidence attribution.

## 9. Contradictory evidence

Contradictions must remain visible. The assessor must evaluate source type, procedural posture, specificity, corroboration, institutional response, temporal proximity, independence, and unresolved conflict.

A later institutional statement does not automatically override contemporaneous records. A pleading, allegation, ruling, audit finding, settlement, policy statement, and observed event have different evidentiary functions.

## 10. Sampling and aggregation

The assessment must predeclare:

- population or record universe;
- selection rule;
- known exclusions;
- likely selection effects;
- aggregation mode.

Permitted aggregation modes are:

- dominant pattern;
- event specific;
- tested capability;
- another explicitly predeclared rule.

A finding for one observed event must not be generalized to a dominant institutional pattern without a declared sampling basis.

## 11. Telemetry Integrity

Telemetry Integrity has two separate components.

### 11.1 Institutional-record integrity

This component evaluates whether the institution's underlying records have adequate provenance, scope, completeness, edit authority, independence, tamper evidence, retention, and contradiction handling.

### 11.2 Assessment-packet integrity

This component evaluates whether the assessor's packet preserves source provenance, declared scope, selection logic, transformations, locators, exclusions, contradictions, and reproducibility.

Each component receives `adequate`, `limited`, `unreliable`, or `IE`.

The overall status is derived using:

`unreliable > IE > limited > adequate`

The derived overall status does not replace either component.

## 12. Assessment-contract conformance

A record conforms to the HIT assessment contract when it satisfies the released schema and the executable semantic checks declared compatible with this specification.

Conformance establishes structural and rule consistency. It does not establish that the evidence is true, complete, legally sufficient, admissible, or causally valid.

## 13. Migration

Historical `0.1.0` assessments remain immutable. Migration to `0.4.0` is prohibited when the current contract requires new evidence interpretation, actor separation, sampling declarations, Repair-trigger analysis, split Telemetry Integrity, or precise locators that the historical record does not contain.

A migration plan may identify required work. It must not fabricate a current-contract assessment.

## 14. Non-claims

HIT does not:

- enforce runtime policy;
- block or authorize agent actions;
- verify identity, privileges, or signed receipts;
- provide policy packs or compliance automation;
- determine legal conformity or evidentiary admissibility;
- make governance evidence portable across legal or institutional regimes;
- certify meaningful human control in a causal sense;
- establish that a decision was fair, accurate, harmless, or morally justified.

## 15. Version and maturity boundary

The specification version identifies the normative contract. Repository releases may add implementation, evidence, or research records without changing this contract.

Research maturity is governed separately by `RESEARCH.md`. A later repository release or stable semantic version does not automatically advance research maturity.
