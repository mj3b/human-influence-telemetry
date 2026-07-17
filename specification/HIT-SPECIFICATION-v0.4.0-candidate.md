# Human Influence Telemetry Specification

**Status:** Approved development candidate; not yet released  
**Candidate version:** `0.4.0`  
**Released predecessor:** `0.1.0`  
**Author:** Mark Julius Banasihan  
**ORCID:** 0009-0001-8121-2878  
**Concept DOI:** 10.5281/zenodo.21204892  
**Research maturity:** Level 1, Defined

## 1. Purpose

Human Influence Telemetry (HIT) is a documentary assurance method for evaluating whether formal human oversight retained practical force in an AI-mediated institutional decision process.

HIT evaluates what observable, time-bounded records establish about human access, judgment, authority, correction, repair, and reform. It does not infer unrecorded intention, evaluate model quality, certify legal compliance, determine whether an outcome was substantively correct, or enforce agent actions at runtime.

## 2. Unit of analysis

The unit of analysis is one defined decision process, within one identified institutional unit, over one bounded period or one explicitly declared event.

Before evidence review begins, an assessment must declare:

- the institutional unit;
- the decision type or event;
- the AI system's role;
- the human authority's stated role;
- the period or event boundary;
- the population or record universe;
- the sampling rule;
- the aggregation rule;
- the material actors and authority relationships;
- any declared follow-up period for later repair or reform evidence.

A boundary may be revised only when the change, reason, timing, and effect on the assessment are recorded.

## 3. System and terminology boundary

### 3.1 Documentary telemetry

In HIT, telemetry means observable, time-bounded documentary evidence that may reveal whether human influence existed and had practical force.

It does not mean a runtime observability SDK, tracing system, event collector, agent middleware, policy engine, or enforcement layer.

### 3.2 HIT assessment record

The output of HIT is a **HIT assessment record** containing:

- six substantive findings;
- institutional-record integrity;
- assessment-packet integrity;
- one derived overall Telemetry Integrity status;
- the assessment boundary, evidence claims, actor attribution, limitations, and unresolved propositions.

A HIT assessment record is not a runtime policy decision, Governed Decision Record, signed receipt, compliance determination, or DEAS evidence-applicability determination.

### 3.3 Assessment-contract conformance

Structural conformance means that a record validates against the declared HIT schema version.

Substantive conformance means that the assessor applied the published rubric, actor-attribution rules, sampling rule, evidence-state sequence, citation requirements, and Telemetry Integrity procedure.

Structural validity does not establish substantive correctness.

## 4. Governing evidence states

Before assigning `0`, `1`, `2`, or `IE`, the assessor must determine which evidence state is established for the dimension.

### 4.1 Affirmative absence

Affirmative absence means the evidence supports the proposition that the relevant capacity, practice, authority, mechanism, or artifact did not exist in the assessed process during the bounded period.

It requires at least one of:

1. an explicit statement of nonexistence from a competent source responsible for the process;
2. a binding process design, system constraint, or authority instrument that made the capacity structurally unavailable;
3. a documented search across a defined and credibly complete record set that would ordinarily contain the artifact if it existed;
4. contemporaneous process evidence showing that the decision path excluded the capacity;
5. multiple mutually consistent records that establish nonexistence rather than merely omit mention of the capacity.

Documentary silence, an unanswered request, a missing file, or a generic process description does not by itself establish affirmative absence.

### 4.2 Formal presence

Formal presence means that the capacity or practice existed in the assessed process as an assigned role, required step, documented mechanism, or available channel.

It requires a process-specific artifact showing both:

1. the capacity was defined or assigned; and
2. the artifact applied to the assessed institutional unit, decision type, and bounded period.

A generic job description, enterprise policy, vendor statement, or undated authority claim does not establish formal presence unless its applicability is traceable.

### 4.3 Operational capability

Operational capability means that a formally present capacity was usable in practice during the assessed period.

It requires evidence of:

- a mechanism;
- applicable authority;
- required access;
- usable timing;
- a defined decision consequence;
- no material barrier making use impracticable.

Operational capability may be shown through an operational test, drill, verified configuration, successful use in a comparable sampled decision, or other direct process evidence. Nominal permission alone is insufficient.

### 4.4 Observed exercise

Observed exercise means the human capacity was used in a documented instance and affected, interrupted, redirected, reconsidered, repaired, or reformed the decision path.

Observed exercise must remain attributable to the assessed actor and fall within the declared temporal and sampling boundaries.

## 5. Findings

### 5.1 `0`: absent

Assign `0` only when affirmative absence is established.

Do not assign `0` because records were not produced, a source is silent, the packet is incomplete, or an expected artifact was not found.

### 5.2 `1`: present but ceremonial

Assign `1` when formal presence is established and one or more of the following applies:

1. operational capability is not established;
2. evidence shows that the practice could not materially alter the decision path;
3. the capacity operated only as ratification, intake, acknowledgment, routing, or another non-substantive form.

A `1` requires evidence that the form of the practice existed. Uncertainty about existence remains `IE`.

### 5.3 `2`: present and substantively exercised

Assign `2` when either:

1. observed exercise shows that the human capacity affected the decision path; or
2. operational capability is directly demonstrated and the assessment design does not reasonably permit an observed exercise, provided that:
   - a named authority could use the mechanism during the bounded period;
   - the mechanism was technically and procedurally available;
   - the decision consequence was identifiable;
   - no material evidence shows that use was prohibitively difficult, routinely ignored, or controlled by another actor.

Mere legal authority, policy language, interface presence, or hypothetical capability does not support `2`.

When evidence supports both `1` and `2`, use `1` unless the criteria for `2` are affirmatively established.

### 5.4 `IE`: insufficient evidence

Assign `IE` when the evidence cannot distinguish among absence, formal presence, operational capability, and observed exercise.

The record must identify:

- the unresolved proposition;
- the missing or conflicting artifact;
- the search or request performed;
- why the remaining evidence cannot support a determinate finding.

`IE` is not ordinal and must not be averaged, converted to zero, or treated as evidence of failure.

## 6. Substantive dimensions

### 6.1 Counsel

**Question:** Did the named human authority have actual pre-decision access to relevant underlying evidence?

Counsel concerns actual presentation, retrieval, or review before the decision, not general system permission.

- `0`: the record establishes that the authority could not access the relevant evidence before the decision.
- `1`: a formal access route existed, but actual pre-decision presentation or retrieval is not shown, or the human received only a compressed score, ranking, summary, or recommendation.
- `2`: records show that the authority actually received, retrieved, or reviewed relevant underlying evidence before the decision, with timing and scope sufficient to inform judgment.
- `IE`: permission, actual retrieval, timing, or evidence scope cannot be determined.

Authorization and actual access must be recorded separately.

### 6.2 Judgment

**Question:** Did the human authority independently evaluate reasons, alternatives, uncertainty, and context?

Direct evidence includes reviewer-authored reasons, alternatives considered, disagreement, modification, questions, requests for additional evidence, or rationale not reducible to system output.

Indirect indicators include review duration, adoption rate, boilerplate language, batch size, and repeated identical dispositions.

Indirect indicators may corroborate a finding but do not alone establish `0` unless the process design affirmatively excluded evaluation.

- `0`: no human evaluation step existed, or the role was structurally prohibited from evaluating the merits.
- `1`: a formal review step existed, but the record shows ratification or ceremonial review. A `1` based primarily on indirect indicators requires at least two mutually reinforcing, process-specific indicators and no material contrary evidence.
- `2`: direct evidence shows independent reasoning capable of affecting the decision path.
- `IE`: the presence or substance of human reasoning cannot be resolved.

### 6.3 Command

**Question:** Could a named human authority practically approve, reject, modify, stop, or escalate?

Legal or organizational authority and practical intervention capability must be assessed separately.

- `0`: no named human authority could direct otherwise, or the intervention was structurally unavailable.
- `1`: authority or a mechanism existed formally, but usability, timing, control, or practical consequence is not established, or material friction reduced the role to ratification.
- `2`: a named authority exercised the power, or an operational test or comparable verified use demonstrates that the authority could produce a specified change during the bounded period.
- `IE`: actor authority, mechanism availability, or practical control cannot be determined.

An intervention controlled solely by a vendor or another institution must not be attributed to the assessed actor.

### 6.4 Correction

**Question:** Could the decision be contested, interrupted, reconsidered, modified, reversed, or appealed in practice?

Correction must distinguish:

1. channel existence;
2. channel accessibility;
3. procedural use;
4. substantive reconsideration;
5. outcome interruption, modification, or reversal.

- `0`: no contest, appeal, interruption, or escalation channel existed.
- `1`: a channel existed and may have accepted submissions, but the record shows only intake, routing, template disposition, or procedural acknowledgment.
- `2`: a documented instance shows substantive reconsideration, interruption, modification, or reversal, or a directly tested process demonstrates that a named authority could produce those consequences.
- `IE`: existence, accessibility, use, or substantive effect cannot be determined.

A reversal is strong evidence but is not required when substantive reconsideration and practical authority to alter the outcome are otherwise established.

### 6.5 Repair

**Question:** After qualifying harm, did a named actor own and deliver remediation to affected persons?

Repair requires a trigger determination before a finding.

#### Trigger states

- `triggered`: harm is established through adjudication, formal institutional acknowledgment, or specific contemporaneous evidence corroborated by at least one independent source or record class.
- `not_triggered`: the bounded record affirmatively establishes that no qualifying harm event occurred.
- `indeterminate`: allegations or indicators exist, but qualifying harm cannot be established.

When the trigger is `indeterminate`, assign Repair `IE` and state the unresolved harm proposition.

When the trigger is `triggered`:

- `0`: no named actor owned remediation, or the process affirmatively excluded repair.
- `1`: a formal owner or process existed, but no practical remedy to affected persons is established, or only the process was corrected.
- `2`: a named actor delivered or operationally directed restitution, record correction, notification, restored access, or another remedy tied to the substantiated harm.
- `IE`: repair ownership or action cannot be determined.

When the trigger is `not_triggered`, standing repair capability may be evaluated only when the boundary explicitly includes capability testing. Formal ownership alone supports at most `1`; `2` requires a tested or previously exercised mechanism. Otherwise assign `IE` and state that no qualifying repair event occurred within the boundary.

### 6.6 Reform

**Question:** Did a named authority have and exercise power to change the decision architecture?

Reform concerns thresholds, models, workflows, controls, delegations, or governance rules rather than only the individual outcome.

Later change is admissible only when:

1. a follow-up period was declared;
2. the changed architecture is identifiable;
3. a record links the change to the assessed failure, risk, or architecture; and
4. the implementing or authorizing actor is identified.

Externally compelled change may support `2` when a named institutional authority substantively implemented, adapted, or extended it. External compulsion alone does not prove internal reform capacity.

- `0`: no assessed actor held authority to change the architecture, or change was structurally impossible within that actor's role.
- `1`: formal authority or a change process existed, but no operative architecture change is established.
- `2`: a named authority implemented or operationally directed a linked architecture change.
- `IE`: authority, linkage, timing, or implementation cannot be determined.

## 7. Telemetry Integrity

Telemetry Integrity evaluates two objects separately.

### 7.1 Institutional-record integrity

The integrity of records generated or retained by the institution and governed systems.

### 7.2 Assessment-packet integrity

The provenance, completeness, transformation history, and preservation of materials supplied to the assessor.

### 7.3 Component statuses

#### `adequate`

Traceable provenance, disclosed scope, controlled edit authority, credible retention, sufficient independence or corroboration where needed, and no unresolved material contradiction affecting the finding.

#### `limited`

Specific gaps, transformations, dependencies, or provenance weaknesses exist, but the remaining record set still permits bounded, traceable findings. Affected dimensions must be named.

#### `unreliable`

Material tampering, unexplained alteration, irreconcilable contradiction, circular dependence, compromised generation, or provenance failure makes the record unsafe as support for one or more findings.

#### `IE`

Information about provenance, completeness, edit authority, retention, independence, or transformation is insufficient to determine whether the component is adequate, limited, or unreliable.

Missing substantive records do not automatically make integrity `IE`; they may instead make a substantive dimension `IE`.

### 7.4 Derived overall status

Derive the overall status deterministically:

1. if either component is `unreliable`, overall is `unreliable`;
2. otherwise, if either component is `IE`, overall is `IE`;
3. otherwise, if either component is `limited`, overall is `limited`;
4. otherwise, overall is `adequate`.

The component statuses must remain visible.

## 8. Sampling and aggregation

Unless another rule was justified before evidence review, period-level HIT assessments report the **dominant operational pattern** within the declared sample and period.

One exceptional exercise does not automatically elevate a period-level finding to `2`. The assessor must determine whether it demonstrates a generally available capacity, a narrow exception, or conduct outside the dominant architecture.

For an event-specific boundary, the event may determine the finding, but the assessment must not generalize that finding to an institution or period without additional evidence.

Every assessment must declare:

- population or record universe;
- sample-selection rule;
- period covered;
- whether each finding represents a dominant pattern, event-specific result, tested capability, or another predeclared rule;
- known exclusions and likely selection effects.

## 9. Actor and authority attribution

Before assigning findings, the assessment must contain an actor-authority matrix recording:

- institutional identity;
- human or automated role;
- authority held;
- mechanism controlled;
- decision stage affected;
- evidence source;
- whether authority was direct, delegated, shared, advisory, appellate, remedial, or reformative.

Conduct, authority, evidence, or failure must not be attributed across institutional boundaries without evidence of delegation, control, agency, shared decision rights, or another defined relationship.

Vendors, deployers, regulators, courts, corporate affiliates, and individual professionals must be separated when their authorities differ.

A combined institutional finding is permitted only when the assessment explains why the actors form one decision architecture for the dimension being scored.

## 10. Contradictory evidence

Conflicting evidence must be evaluated using:

- directness;
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

A determinate finding is permitted when one account is materially better supported and the assessment explains why the conflict does not alter the finding.

Assign `IE` when unresolved conflict could reasonably change the finding or actor attribution.

HIT evaluates evidentiary support for its constructs; it does not adjudicate legal liability or the ultimate merits of a disputed claim.

## 11. Cross-dimensional evidence reuse

One artifact may support more than one dimension only when the assessment records a distinct proposition for each use.

For every reuse, record:

- source and precise locator;
- dimension-specific proposition;
- relation: `supports`, `contradicts`, or `limits`;
- reasoning connecting the artifact to the construct.

Evidence establishing one dimension does not automatically establish another. An override log may support Command but does not establish Judgment unless it also records independent reasoning.

## 12. Citation precision

Every material evidence claim must include:

1. source identifier;
2. page, paragraph, section, timestamp, event identifier, record identifier, or another available locator;
3. a bounded evidence proposition;
4. relation: `supports`, `contradicts`, or `limits`.

When no stable locator exists, identify the smallest reproducible passage or record unit and explain the limitation.

A source identifier without a locator is insufficient for substantive conformance when the source permits more precise citation.

## 13. Required assessment record

A conforming candidate `0.4.0` assessment must identify:

- specification and schema versions;
- institutional unit, decision process, and boundary;
- sampling and aggregation rules;
- actor-authority matrix;
- evidence requested and received;
- structured evidence claims;
- evidence-state rationale for each substantive dimension;
- one finding for each substantive dimension;
- Repair trigger state;
- institutional-record integrity;
- assessment-packet integrity;
- derived overall Telemetry Integrity;
- assessor identity and conflict disclosure;
- limitations and unresolved ambiguities;
- artifact provenance and migration status.

## 14. Relationship to adjacent systems

- Governed Decision Intelligence may supply decision authority, evidence, alternatives, uncertainty, conditions, escalation, and audit metadata. HIT remains independent of GDI.
- Microsoft Agent Governance Toolkit may supply runtime policy, approval, identity, capability, enforcement, and audit events. HIT does not enforce actions.
- ScopeBlind/Acta may supply verified receipt evidence about attribution, integrity, ordering, canonicalization, and chain linkage. HIT does not define or verify the protocol.
- Credo AI may supply policy-pack, risk, control, workflow, monitoring, and evidence artifacts. HIT does not provide policy packs, compliance automation, universal control mappings, or runtime agent governance.
- DEAS evaluates what a defined artifact may support under a specified governance requirement. HIT does not make evidence or legal conclusions portable across regimes.

## 15. Non-claims

HIT does not claim that:

- human involvement is always preferable to automation;
- a high finding proves a good, lawful, fair, accurate, or harmless decision;
- a low finding proves unlawful conduct;
- recorded reasoning is truthful;
- the method is statistically validated or independently adopted;
- it provides runtime enforcement, signed-receipt interoperability, compliance automation, certification, or legal portability.

## 16. Version stability and research maturity

Semantic versioning describes the stability and compatibility of the public assessment contract.

Research maturity describes the strength of evidence supporting HIT claims.

A stable version does not imply human inter-rater reliability, causal validity, legal conformity, certification, or independent adoption.

Claim H3 and Maturity Level 2 remain unavailable until two eligible independent human scorers complete the locked protocol under its predeclared rules.

## 17. Prospective application and locked-protocol boundary

This candidate applies prospectively.

It does not alter:

- protocol `HIT-IRP-CIGNA-001`;
- the frozen Cigna packet;
- original human submissions when collected;
- the pre-adjudication threshold or critical-disagreement rules;
- historical public findings released under specification `0.1.0`.

Historical cases must either remain explicitly version-bound to `0.1.0` or be migrated as separate `0.4.0` records with a change explanation.

## 18. Release conditions

Candidate `0.4.0` must not be released until:

1. the candidate specification and handbook are synchronized;
2. the schema and dimension catalog express the required fields and statuses;
3. accepted, rejected, and boundary fixtures cover every `FR-01` through `FR-16` class;
4. validation rejects each known invalid state;
5. public cases are migrated or explicitly version-bound;
6. migration and breaking-change reports are published;
7. claim, limitation, provenance, citation, and release metadata are synchronized;
8. the adjacent-system claim audit passes;
9. CI passes on the exact release commit.
