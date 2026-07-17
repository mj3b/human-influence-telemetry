# HIT Normative Decision Rules — v0.4.0 Draft

**Status:** Candidate normative text; not part of a released HIT contract  
**Target release:** `v0.4.0`  
**Source review:** `HIT-ARFR-001`  
**Applies prospectively:** Yes  
**Changes locked protocol `HIT-IRP-CIGNA-001`:** No

## 1. Purpose

This document converts the ambiguity classes recorded in `HIT-ARFR-001` into candidate decision rules for Human Influence Telemetry.

The rules are designed to reduce reasonable scorer divergence without weakening the distinction between evidence of absence and absence of evidence. They do not revise completed assessments, alter the locked Cigna inter-rater protocol, or establish human inter-rater reliability.

The rules become normative only when they are synchronized with the specification, application handbook, assessment schema, dimension catalog, fixtures, case migrations, validator, changelog, and release metadata.

## 2. Governing evidence states

Before assigning `0`, `1`, `2`, or `IE`, the assessor must classify the available evidence for the dimension into one of four evidence states.

### 2.1 Affirmative absence

Affirmative absence means the available evidence supports the proposition that the relevant capacity, practice, authority, mechanism, or artifact did not exist in the assessed process during the bounded period.

Affirmative absence requires at least one of:

1. an explicit statement of nonexistence from a competent source with responsibility for the process;
2. a binding process design, system constraint, or authority instrument that made the capacity structurally unavailable;
3. a documented search across a defined and credible complete record set that would ordinarily contain the artifact if it existed;
4. contemporaneous process evidence showing that the decision path excluded the relevant human capacity;
5. multiple mutually consistent records that establish nonexistence rather than merely omit mention of the capacity.

Documentary silence, an unanswered request, a missing file, or a generic process description that omits the capacity does not by itself establish affirmative absence.

### 2.2 Formal presence

Formal presence means the capacity or practice existed in the assessed process as an assigned role, required step, documented mechanism, or available channel.

Formal presence requires a process-specific artifact showing both:

1. the capacity was defined or assigned; and
2. the artifact applied to the assessed institutional unit, decision type, and bounded period.

A generic job description, enterprise policy, vendor statement, or undated authority claim does not establish formal presence unless its applicability to the assessed process is traceable.

### 2.3 Operational capability

Operational capability means the formal capacity was usable in practice during the assessed period.

Operational capability requires evidence of the mechanism, authority, access, timing, and absence of a material barrier that would make use impracticable. It may be shown through an operational test, drill, verified configuration, successful use in a comparable sampled decision, or other direct process evidence.

A policy statement or nominal permission alone does not establish operational capability.

### 2.4 Observed exercise

Observed exercise means the relevant human capacity was used in a documented instance and affected, interrupted, redirected, reconsidered, repaired, or reformed the decision path.

Observed exercise is the strongest evidence for `2`, but it must remain attributable to the assessed actor and fall within the declared temporal and sampling rules.

## 3. Findings decision rule

### 3.1 Finding `0`: absent

Assign `0` only when affirmative absence is established.

Do not assign `0` because records were not produced, the evidence packet is incomplete, a source is silent, or the assessor expected an artifact but did not find it.

### 3.2 Finding `1`: present but ceremonial

Assign `1` when formal presence is established, but either:

1. operational capability is not established; or
2. evidence shows that the practice could not materially alter the decision path; or
3. the capacity was used only as ratification, intake, acknowledgment, routing, or another non-substantive form.

Assigning `1` requires evidence that the form of the practice existed. Uncertainty about whether it existed remains `IE`.

### 3.3 Finding `2`: present and substantively exercised

Assign `2` when either:

1. observed exercise shows that the human capacity affected the decision path; or
2. operational capability is directly demonstrated and the assessment design does not reasonably permit an observed exercise, provided that:
   - the named authority could use the mechanism during the bounded period;
   - the mechanism was technically and procedurally available;
   - the evidence identifies the decision consequence the mechanism could produce;
   - no material evidence shows that use was prohibitively difficult, routinely ignored, or controlled by a different actor.

Mere legal authority, policy language, interface presence, or hypothetical capability does not support `2`.

When evidence supports both `1` and `2`, apply the lower finding unless the criteria for `2` are affirmatively established.

### 3.4 Finding `IE`: insufficient evidence

Assign `IE` when the evidence cannot distinguish among absence, formal presence, operational capability, and observed exercise.

The assessment must identify:

- the unresolved proposition;
- the missing or conflicting artifact;
- the search or request performed;
- why the remaining evidence cannot support a determinate finding.

`IE` is not an ordinal value and must not be averaged, converted to zero, or treated as evidence of failure.

## 4. Dimension-specific rules

### 4.1 Counsel

Counsel concerns actual pre-decision access to relevant underlying evidence, not general system permission.

- `0`: the record establishes that the named human authority could not access the relevant evidence before the decision.
- `1`: a formal access route existed, but actual pre-decision presentation or retrieval is not shown, or the human received only a compressed score, ranking, summary, or recommendation.
- `2`: records show that the named authority actually received, retrieved, or reviewed relevant underlying evidence before the decision, with timing and scope sufficient to inform judgment.
- `IE`: access permission, actual retrieval, timing, or evidence scope cannot be determined.

Authorization to access and evidence of actual access must be recorded separately.

### 4.2 Judgment

Judgment concerns independent evaluation of reasons, alternatives, uncertainty, and context.

Direct evidence includes reviewer-authored reasons, alternatives considered, disagreement, modification, questions, requests for more evidence, or a rationale not reducible to the system output.

Indirect indicators include review duration, recommendation-adoption rate, boilerplate language, batch size, and repeated identical dispositions.

Indirect indicators may corroborate a finding but do not alone establish `0` unless the process design affirmatively excluded human evaluation.

- `0`: no human evaluation step existed, or the human role was structurally prohibited from evaluating the merits.
- `1`: a formal review step existed, but the record shows ratification or ceremonial review. A `1` based primarily on indirect indicators requires at least two mutually reinforcing indicators, process-specific applicability, and no material contrary evidence of independent reasoning.
- `2`: direct evidence shows independent reasoning capable of affecting the decision path.
- `IE`: the presence or substance of human reasoning cannot be resolved from the available evidence.

### 4.3 Command

Command concerns practical authority to approve, reject, modify, stop, or escalate.

Legal or organizational authority and practical intervention capability must be assessed separately.

- `0`: no named human authority could direct otherwise, or the relevant intervention was structurally unavailable.
- `1`: authority or an intervention mechanism existed formally, but usability, timing, control, or practical consequence is not established, or material friction reduced the role to ratification.
- `2`: a named authority exercised the power, or an operational test or comparable verified use demonstrates that the authority could produce a specified change during the bounded period.
- `IE`: actor authority, mechanism availability, or practical control cannot be determined.

An intervention controlled solely by a vendor or another institution must not be attributed to the assessed actor.

### 4.4 Correction

Correction must be decomposed into five states:

1. channel existence;
2. channel accessibility;
3. procedural use;
4. substantive reconsideration;
5. outcome interruption, modification, or reversal.

- `0`: no contest, appeal, interruption, or escalation channel existed for the assessed decision process.
- `1`: a channel existed and may have accepted submissions, but the record shows only intake, routing, template disposition, or procedural acknowledgment without substantive reconsideration.
- `2`: a documented instance shows substantive reconsideration, interruption, modification, or reversal, or a directly tested process demonstrates that a named authority could produce those consequences.
- `IE`: the channel's existence, accessibility, use, or substantive effect cannot be determined.

A reversal is strong evidence but is not required when substantive reconsideration and practical authority to alter the outcome are otherwise established.

### 4.5 Repair

Repair uses a separate trigger determination before the finding is assigned.

#### Trigger states

- `triggered`: harm is established through adjudication, formal institutional acknowledgment, or specific contemporaneous evidence corroborated by at least one independent source or record class.
- `not_triggered`: the bounded record affirmatively establishes that no qualifying harm event occurred.
- `indeterminate`: allegations or indicators exist, but the record cannot establish whether qualifying harm occurred.

When the trigger is `indeterminate`, assign `IE` and explain the unresolved harm proposition.

When the trigger is `triggered`:

- `0`: no named actor owned remediation, or the process affirmatively excluded repair.
- `1`: a formal remediation owner or process existed, but the record shows no practical remedy to affected persons or only process correction without person-level repair.
- `2`: a named actor delivered or operationally directed remediation such as restitution, record correction, notification, restored access, or another remedy tied to the substantiated harm.
- `IE`: repair ownership or action cannot be determined.

When the trigger is `not_triggered`, the assessor may evaluate standing repair capability only when the boundary explicitly includes capability testing. In that case, `2` requires a tested or previously exercised repair mechanism; formal ownership alone supports at most `1`. Otherwise assign `IE` and state that no qualifying repair event occurred within the boundary.

### 4.6 Reform

Reform concerns authority and action directed at the decision architecture, not only the individual outcome.

A later change is admissible only when:

1. the assessment declares a follow-up period;
2. the changed threshold, model, workflow, control, delegation, or governance rule is identifiable;
3. a record links the change to the assessed failure, risk, or architecture; and
4. the actor implementing or authorizing the change is identified.

Externally compelled change may support `2` when a named institutional authority substantively implemented, adapted, or extended the change. External compulsion alone does not prove internal reform capacity.

- `0`: no assessed actor held authority to change the relevant architecture, or change was structurally impossible within that actor's role.
- `1`: formal reform authority or a change process existed, but no operative architecture change is established.
- `2`: a named authority implemented or operationally directed a linked architecture change.
- `IE`: authority, linkage, timing, or implementation cannot be determined.

## 5. Telemetry Integrity

### 5.1 Two required objects

Telemetry Integrity must assess two objects separately:

1. **institutional-record integrity:** the integrity of the records generated or retained by the institution and governed systems;
2. **assessment-packet integrity:** the provenance, completeness, transformation history, and preservation of the materials supplied to the assessor.

A later schema version must contain separate fields for both objects and one derived overall status.

### 5.2 Status definitions

#### `adequate`

Assign `adequate` when the record set has traceable provenance, disclosed scope, controlled edit authority, credible retention, sufficiently independent corroboration where needed, and no unresolved material contradiction affecting the finding.

#### `limited`

Assign `limited` when specific gaps, transformations, dependencies, or provenance weaknesses exist but the remaining record set still permits bounded, traceable findings. The limitation and affected dimensions must be named.

#### `unreliable`

Assign `unreliable` when material tampering, unexplained alteration, irreconcilable contradiction, circular dependence, compromised generation, or provenance failure makes the record set unsafe as support for one or more findings.

#### `IE`

Assign `IE` when information about provenance, completeness, edit authority, retention, independence, or transformation is itself insufficient to determine whether the record set is adequate, limited, or unreliable.

Missing substantive records do not automatically make integrity `IE`; they may instead make a substantive dimension `IE`. Integrity `IE` concerns inability to determine the trustworthiness of the record system or packet.

### 5.3 Derived overall status

The overall Telemetry Integrity status is derived as follows:

1. if either component is `unreliable`, overall status is `unreliable`;
2. otherwise, if either component is `IE`, overall status is `IE`;
3. otherwise, if either component is `limited`, overall status is `limited`;
4. otherwise, overall status is `adequate`.

The component statuses must remain visible; the overall status must not conceal which object produced the limitation.

## 6. Assessment boundary, sampling, and aggregation

### 6.1 Default aggregation rule

Unless the assessment states another justified rule before evidence review, HIT reports the **dominant operational pattern** within the declared sample and bounded period.

One exceptional exercise does not automatically elevate a period-level finding to `2`. The assessor must determine whether the instance demonstrates a generally available capacity, a narrow exception, or conduct outside the dominant architecture.

### 6.2 Event-specific boundaries

When the unit of analysis is one event rather than a period-level process, the finding may be based on that event alone. The assessment must not generalize the event finding to the institution or period without additional evidence.

### 6.3 Required sampling statement

Every assessment must declare:

- population or record universe;
- sample-selection rule;
- period covered;
- whether the finding represents a dominant pattern, event-specific result, tested capability, or another predeclared aggregation rule;
- known exclusions and likely selection effects.

## 7. Actor and authority attribution

### 7.1 Actor-authority matrix

Before findings are assigned, the assessment must identify each material actor and record:

- institutional identity;
- human or automated role;
- authority held;
- mechanism controlled;
- decision stage affected;
- evidence source;
- whether authority was direct, delegated, shared, advisory, appellate, remedial, or reformative.

### 7.2 Attribution rule

Conduct, authority, evidence, or failure must not be attributed across institutional boundaries without evidence of delegation, control, agency, shared decision rights, or another defined relationship.

Vendors, deployers, regulators, courts, corporate affiliates, and individual professionals must be separated when their authorities differ.

A combined institutional finding is permitted only when the assessment explains why the actors form one decision architecture for the dimension being scored.

## 8. Contradictory evidence

### 8.1 Weighting factors

Conflicting evidence must be evaluated using:

- directness to the assessed event or process;
- contemporaneity;
- specificity;
- source competence;
- independence;
- corroboration;
- disclosed interest or conflict;
- procedural posture;
- internal consistency;
- consistency with other record classes.

No source type is automatically controlling.

### 8.2 Determinate finding under conflict

A determinate finding is permitted when one account is materially better supported under the weighting factors and the assessment explains why the conflict does not alter the finding.

Assign `IE` when the unresolved conflict could reasonably change the finding or actor attribution.

HIT evaluates evidentiary support for the published constructs. It does not adjudicate legal liability, credibility in a judicial sense, or the ultimate merits of a disputed claim.

## 9. Cross-dimensional evidence reuse

One artifact may support more than one dimension only when the assessment records a distinct evidentiary proposition for each use.

For every reused artifact, record:

- the source and precise locator;
- the dimension-specific proposition;
- whether the artifact supports, contradicts, or limits that proposition;
- the reasoning connecting the artifact to that construct.

Evidence that establishes one dimension must not be treated as automatically establishing another. For example, an override log may support Command but does not establish Judgment unless it also contains evidence of independent reasoning.

## 10. Citation precision

Every material evidence claim must include:

1. source identifier;
2. page, paragraph, section, timestamp, event identifier, record identifier, or another available locator;
3. a bounded evidence proposition;
4. the relation of the artifact to the proposition: `supports`, `contradicts`, or `limits`.

When a source has no stable locator, the assessment must identify the smallest reproducible passage or record unit and explain the limitation.

A source identifier without a locator is insufficient for substantive conformance when the source permits more precise citation.

## 11. Friction-register resolution map

| Friction ID | Candidate rule location |
|---|---|
| `FR-01` | Sections 2.1 and 3.1–3.4 |
| `FR-02` | Sections 2.2 and 3.2 |
| `FR-03` | Sections 2.3–2.4 and 3.3 |
| `FR-04` | Section 4.1 |
| `FR-05` | Section 4.2 |
| `FR-06` | Section 4.3 |
| `FR-07` | Section 4.4 |
| `FR-08` | Section 4.5 |
| `FR-09` | Section 4.6 |
| `FR-10` | Section 5.1 |
| `FR-11` | Sections 5.2–5.3 |
| `FR-12` | Section 6 |
| `FR-13` | Section 7 |
| `FR-14` | Section 8 |
| `FR-15` | Section 9 |
| `FR-16` | Section 10 |

## 12. Prospective application and locked-protocol boundary

These candidate rules do not alter:

- the frozen materials or scoring instructions for `HIT-IRP-CIGNA-001`;
- any original public case finding released under specification `0.1.0`;
- the predeclared inter-rater comparison threshold;
- the critical-disagreement rules;
- the requirement to publish a passing or failing human result unchanged.

When v0.4.0 is released, existing case assessments must either be migrated under the new contract or retain an explicit declaration that they remain historical `0.1.0` assessments.

## 13. Release conditions

This draft must not be represented as the released HIT rubric until:

1. each rule is incorporated into `SPECIFICATION.md` and `docs/application-handbook.md`;
2. the schema and dimension catalog express required fields and statuses;
3. positive, negative, and boundary fixtures exist for every friction class;
4. the validator deterministically checks the new contract;
5. the public cases are migrated or explicitly version-bounded;
6. a breaking-change and migration review is published;
7. claim, limitation, provenance, citation, and release metadata are synchronized;
8. CI passes on the exact release commit.
