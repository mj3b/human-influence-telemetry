# HIT Application Handbook

**Version:** 0.4.0  
**Released:** 2026-07-18  
**Normative source:** `SPECIFICATION.md`

This handbook provides the operating procedure for producing a HIT assessment record. It does not replace the specification.

## 1. Define the boundary before reviewing findings

Record:

- institutional unit and decision process;
- period or event boundary and any follow-up period;
- AI-system role and stated human-authority role;
- population or record universe;
- sampling rule;
- aggregation rule;
- known exclusions and likely selection effects.

Do not revise the boundary after seeing results without recording the change, reason, timing, and effect.

## 2. Identify actors and authority

Create an actor-authority matrix before assigning findings.

For each material actor, record:

- institutional identity;
- human, automated, institutional, or external-authority role;
- named role;
- direct, delegated, shared, advisory, appellate, remedial, reformative, technical, or absent authority;
- mechanisms controlled;
- decision stages affected;
- relationship to other actors;
- evidence supporting the attribution.

Do not attribute vendor, regulator, court, affiliate, deployer, or professional authority to another actor without evidence of delegation, control, agency, or shared rights.

## 3. Request artifacts, not conclusions

Ask for record types rather than asking an institution to prove that oversight was meaningful.

| Dimension | Illustrative artifact requests |
|---|---|
| Counsel | case-file access logs, evidence packet, retrieval timestamps, source inventory |
| Judgment | reviewer notes, reasons, alternatives, dissent, questions, modifications |
| Command | authority matrix, delegation instrument, override, rejection, stop-use, escalation logs |
| Correction | appeal register, escalation log, reconsideration notes, interruption and reversal records |
| Repair | harm substantiation, restitution, correction, notification, restored-access and ownership records |
| Reform | threshold revision, workflow redesign, model retirement, control redesign, authorization records |
| Telemetry Integrity | provenance, edit permissions, retention, transformations, hashes, chain and contradiction records |

## 4. Convert artifacts into evidence claims

Every material claim must contain:

1. claim, artifact, and source identifiers;
2. precise locator;
3. bounded proposition;
4. relation: `supports`, `contradicts`, or `limits`;
5. relevant dimensions and actors;
6. provenance status;
7. independence status;
8. transformation history.

When no stable locator exists, identify the smallest reproducible unit and explain the limitation.

One artifact may be reused across dimensions only through separate propositions and reasoning paths.

## 5. Classify the evidence state

Determine the evidence state before selecting a finding.

### Affirmative absence

Use only when records establish nonexistence through explicit statement, structural impossibility, a credibly complete search, contemporaneous exclusion, or multiple consistent records.

Silence, nonproduction, an unanswered request, or omission from a generic description is not affirmative absence.

### Formal presence

Use when a process-specific artifact establishes that a role, mechanism, step, or channel applied to the assessed unit, decision type, and period.

### Operational capability

Use when the formally present capacity was practically usable: authority, mechanism, access, timing, consequence, and absence of material barriers are established.

### Observed exercise

Use when a documented instance shows the capacity affected, interrupted, redirected, reconsidered, repaired, or reformed the decision path.

### Indeterminate

Use when the record cannot distinguish among the preceding states.

## 6. Assign the finding

- `0`: affirmative absence established.
- `1`: process-specific formal presence established, but substantive capability or effect is not established or is affirmatively ceremonial.
- `2`: observed exercise established, or directly tested operational capability meets every bounded condition in the specification.
- `IE`: the evidence state remains indeterminate.

For `IE`, record the unresolved proposition, missing or conflicting artifact, search or request performed, and why the remaining evidence is insufficient.

When evidence supports both `1` and `2`, use `1` unless the `2` criteria are affirmatively established.

## 7. Apply dimension-specific procedures

### Counsel

Separate general authorization from actual, timely access to relevant underlying evidence. A score or summary alone is not underlying evidence.

### Judgment

Prefer direct reviewer-authored reasoning. Indirect indicators may support `1` only when at least two process-specific indicators reinforce one another and no material contrary evidence exists.

### Command

Separate formal authority from practical control. Identify who controls the intervention mechanism and the consequence it can produce.

### Correction

Record channel existence, accessibility, use, substantive reconsideration, and practical outcome effect separately. Intake or template disposition alone is ceremonial.

### Repair

Determine the harm trigger first:

- `triggered`;
- `not_triggered`;
- `indeterminate`.

An indeterminate trigger requires Repair `IE`. When no qualifying event occurred, evaluate standing capability only when capability testing was predeclared.

### Reform

Use later evidence only when a follow-up period was declared and the change, linkage, authority, and implementation are identifiable. External compulsion alone does not establish institutional reform capacity.

## 8. Apply sampling and aggregation

Use the dominant operational pattern for period-level assessments unless another rule was predeclared.

A rare exception does not automatically establish a period-level `2`. Determine whether it represents a generally available capacity, a narrow exception, or conduct outside the dominant architecture.

An event-specific finding must not be generalized without additional evidence.

## 9. Resolve contradictory evidence

Evaluate conflicts using:

- directness;
- contemporaneity;
- specificity;
- source competence;
- independence;
- corroboration;
- disclosed interest;
- procedural posture;
- internal consistency;
- consistency with other record classes.

No source type automatically controls. A determinate finding is permitted only when one account is materially better supported and the reasoning is recorded. Use `IE` when the unresolved conflict could change the finding or actor attribution.

## 10. Assess Telemetry Integrity separately

Assess:

1. institutional-record integrity;
2. assessment-packet integrity.

For each component, evaluate provenance, disclosed scope and completeness, edit authority, independence, tamper evidence, retention, transformations, contradictions, and affected dimensions.

Assign `adequate`, `limited`, `unreliable`, or `IE` under the specification. Derive the overall status in this order:

`unreliable` > `IE` > `limited` > `adequate`

Do not conceal the component statuses behind the overall result.

## 11. Produce the assessment record

A conforming record includes:

- versions and migration status;
- boundary, sampling, and aggregation;
- actor-authority matrix;
- assessor and conflict disclosure;
- structured evidence claims;
- six dimension findings;
- Repair trigger;
- split Telemetry Integrity and overall derivation;
- summary, most consequential missing artifact, limitations, and migration notes.

Validate the file against `schema/hit-assessment.schema.json`.

## 12. Quality-control checklist

Before publication, confirm that:

- no `0` rests only on missing evidence;
- no `1` rests only on generic role or policy language;
- no `2` rests only on nominal authority or hypothetical capability;
- every `IE` names an unresolved proposition and search effort;
- actor attribution is explicit;
- reused evidence has separate propositions;
- material contradictions are preserved;
- locators are reproducible;
- sampling and aggregation are predeclared;
- integrity components and derivation agree;
- the assessment makes no compliance, liability, certification, or causal claim.

## 13. Historical records and migration

Do not overwrite `0.1.0` assessments. Migration requires a fresh bounded reassessment and a separate `0.4.0` record. Follow `docs/migration-guide-v0.1.0-to-v0.4.0.md` and preserve the historical Git blob SHA.

The current public migration dispositions appear in `case-studies/migrations/v0.4.0/migration-manifest.json`.

## 14. Inter-rater exercise

The locked Cigna protocol remains governed by specification and schema `0.1.0`. Do not use this `0.4.0` handbook to brief or rescore participants in that exercise.

The human result remains required for H3 and Maturity Level 2. Original submissions and the pre-adjudication comparison must be published, passing or failing, without replacing original scores after discussion.
