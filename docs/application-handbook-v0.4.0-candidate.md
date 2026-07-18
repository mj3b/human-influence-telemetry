# HIT Application Handbook

**Status:** Approved development candidate; not yet released  
**Candidate version:** `0.4.0`  
**Released predecessor:** `0.1.0`  
**Research maturity:** Level 1, Defined

## 1. Define the assessment before reviewing evidence

Record:

- the institutional unit;
- the decision type or event;
- the AI system's role;
- the named human authority or authorities;
- the bounded period;
- any declared follow-up period;
- the population or record universe;
- the sampling rule;
- the aggregation rule;
- material actors and authority relationships.

Do not change the boundary after seeing the evidence without recording the change, reason, timing, and effect on the assessment.

### 1.1 Choose the aggregation rule

For a period-level assessment, use the **dominant operational pattern** unless another rule was justified before evidence review.

For an event-specific assessment, score the event but do not generalize the result to the institution or period without additional evidence.

State whether each finding represents:

- a dominant pattern;
- an event-specific result;
- tested capability;
- another predeclared rule.

## 2. Build the actor-authority matrix

Before assigning findings, identify each material actor.

| Actor | Institutional identity | Human or automated role | Authority held | Mechanism controlled | Decision stage | Relationship | Evidence source |
|---|---|---|---|---|---|---|---|
| | | | | | | direct / delegated / shared / advisory / appellate / remedial / reformative | |

Do not attribute one actor's conduct, authority, evidence, or failure to another without evidence of delegation, control, agency, shared decision rights, or another defined relationship.

Separate vendors, deployers, regulators, courts, corporate affiliates, and individual professionals when their authorities differ.

## 3. Request artifacts, not conclusions

Ask for records by type. Do not ask the institution to prove that oversight was meaningful.

| Dimension | Illustrative requests |
|---|---|
| Counsel | evidence packets, case-file access logs, retrieval timestamps, reviewer screens |
| Judgment | reviewer-authored reasons, alternatives considered, questions, disagreement, modifications |
| Command | authority matrix, delegation instruments, override logs, stop-use tests, escalation records |
| Correction | appeal channels, accessibility records, appeal registers, reconsideration notes, reversals |
| Repair | harm determinations, restitution, corrected records, notifications, remediation ownership |
| Reform | threshold changes, model retirement, workflow redesign, control changes, authorizing records |
| Institutional-record integrity | record architecture, edit permissions, retention, provenance, tamper evidence |
| Assessment-packet integrity | source manifest, hashes, transformation history, preservation record, missing-file disclosure |

Record what was requested, what was produced, what was unavailable, and the stated reason.

## 4. Create structured evidence claims

Every material claim should be recorded before the final finding.

| Claim ID | Source ID | Locator | Dimension | Proposition | Relation | Actor | Time | Notes |
|---|---|---|---|---|---|---|---|---|
| | | page / paragraph / section / timestamp / record ID | | bounded statement | supports / contradicts / limits | | | |

A source ID without a locator is insufficient when the source permits a more precise citation.

When a source lacks a stable locator, identify the smallest reproducible passage or record unit and explain the limitation.

## 5. Classify the evidence state

Use the following sequence before assigning a finding:

```text
affirmative absence
        ↓
formal presence
        ↓
operational capability
        ↓
observed exercise
```

The sequence is not an ordinal score. It is an evidentiary classification procedure.

### 5.1 Affirmative absence

Use only when evidence supports nonexistence through one or more of:

- explicit nonexistence from a competent source;
- binding process or system design excluding the capacity;
- a documented search across a credibly complete record set;
- contemporaneous evidence showing the decision path excluded the capacity;
- multiple consistent records establishing nonexistence.

Do not infer affirmative absence from silence, missing files, unanswered requests, or generic descriptions.

### 5.2 Formal presence

Require a process-specific artifact showing that the role, step, mechanism, or channel:

- was defined or assigned; and
- applied to the institutional unit, decision type, and bounded period.

Generic policies, job descriptions, vendor statements, or undated authority claims do not establish formal presence without traceable applicability.

### 5.3 Operational capability

Require evidence that the capacity was usable in practice, including:

- mechanism;
- applicable authority;
- required access;
- usable timing;
- defined decision consequence;
- no material barrier making use impracticable.

A test, drill, verified configuration, or comparable successful use may establish capability. Nominal permission alone does not.

### 5.4 Observed exercise

Require a documented instance in which the human capacity affected, interrupted, redirected, reconsidered, repaired, or reformed the decision path.

Confirm actor attribution, timing, and fit with the sampling rule.

## 6. Assign the substantive finding

### `0`: absent

Assign only when affirmative absence is established.

### `1`: present but ceremonial

Assign when formal presence is established but:

- operational capability is not established;
- the practice could not materially alter the path; or
- the human role operated only as ratification, intake, acknowledgment, routing, or another non-substantive form.

A `1` requires evidence that the practice existed.

### `2`: present and substantively exercised

Assign when:

- observed exercise affected the path; or
- operational capability is directly demonstrated and the assessment design does not reasonably permit observation of an exercise.

For capability-only `2`, confirm:

- named authority;
- technical and procedural availability;
- identifiable decision consequence;
- no material contrary evidence showing impracticability or control by another actor.

### `IE`: insufficient evidence

Assign when the evidence cannot distinguish absence, formal presence, operational capability, and observed exercise.

Record:

- unresolved proposition;
- missing or conflicting artifact;
- search or request performed;
- why a determinate finding is unavailable.

Do not convert `IE` to zero.

## 7. Apply dimension-specific procedures

### 7.1 Counsel

Separate:

- permission to access;
- technical availability;
- actual retrieval or presentation;
- pre-decision timing;
- scope of underlying evidence.

| Finding | Rule |
|---|---|
| `0` | The authority could not access relevant evidence before the decision. |
| `1` | A formal route existed, but actual access is not shown, or only a compressed output was available. |
| `2` | The authority actually received, retrieved, or reviewed relevant underlying evidence before the decision. |
| `IE` | Permission, retrieval, timing, or scope cannot be determined. |

### 7.2 Judgment

Prefer direct evidence:

- reviewer-authored reasons;
- alternatives;
- disagreement;
- modification;
- questions;
- requests for more evidence;
- rationale not reducible to the system output.

Indirect indicators may include review duration, adoption rate, boilerplate language, batch size, and repeated identical dispositions.

Indirect indicators alone do not establish `0`. A `1` based primarily on indirect evidence requires at least two mutually reinforcing, process-specific indicators and no material contrary evidence.

### 7.3 Command

Separate formal authority from practical control.

Check:

- named authority;
- mechanism owner;
- timing;
- technical availability;
- procedural availability;
- decision consequence;
- friction or dependency;
- whether a vendor or another institution controlled the intervention.

Do not attribute vendor-controlled intervention to the assessed institution.

### 7.4 Correction

Assess five states separately:

1. channel existence;
2. accessibility;
3. procedural use;
4. substantive reconsideration;
5. interruption, modification, or reversal.

A channel that only accepts, routes, or acknowledges submissions supports at most `1`.

A reversal is strong evidence for `2`, but substantive reconsideration plus practical authority to alter the outcome may also support `2`.

### 7.5 Repair

Determine the trigger first.

| Trigger | Rule |
|---|---|
| `triggered` | Harm is established through adjudication, formal acknowledgment, or specific contemporaneous evidence corroborated by an independent source or record class. |
| `not_triggered` | The bounded record affirmatively establishes no qualifying harm event. |
| `indeterminate` | Allegations or indicators exist, but qualifying harm cannot be established. |

When `indeterminate`, assign Repair `IE`.

When `triggered`:

| Finding | Rule |
|---|---|
| `0` | No named actor owned remediation, or repair was affirmatively excluded. |
| `1` | A formal owner or process existed, but no practical person-level remedy is established. |
| `2` | A named actor delivered or directed restitution, correction, notification, restored access, or another linked remedy. |
| `IE` | Ownership or action cannot be determined. |

When `not_triggered`, assess standing capability only when capability testing was included in the original boundary. Formal ownership alone supports at most `1`; `2` requires a tested or previously exercised mechanism.

### 7.6 Reform

A later change counts only when:

- a follow-up period was declared;
- the changed architecture is identifiable;
- a record links the change to the assessed failure, risk, or architecture;
- the authorizing or implementing actor is identified.

Externally compelled change supports `2` only when a named institutional authority substantively implemented, adapted, or extended it.

## 8. Evaluate contradictory evidence

Use these weighting factors:

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

A determinate finding is permitted when one account is materially better supported and the assessment explains why the conflict does not change the result.

Use `IE` when unresolved conflict could reasonably change the finding or actor attribution.

Do not turn HIT into an adjudication of legal liability or ultimate merits.

## 9. Reuse evidence without collapsing constructs

One artifact may support more than one dimension only when a separate proposition is recorded for each use.

Example:

- an override log may support Command because it records a usable intervention;
- the same log supports Judgment only when it also records independent reasoning.

For each reuse, record the locator, proposition, relation, and construct-specific reasoning.

## 10. Assess Telemetry Integrity separately

Assess two components.

### 10.1 Institutional-record integrity

Evaluate records generated or retained by the institution and governed systems.

### 10.2 Assessment-packet integrity

Evaluate the provenance, completeness, transformation history, and preservation of materials supplied to the assessor.

### 10.3 Component status decision

| Status | Rule |
|---|---|
| `adequate` | Traceable provenance, disclosed scope, controlled edit authority, credible retention, sufficient independence or corroboration, and no unresolved material contradiction. |
| `limited` | Named gaps or provenance weaknesses exist, but bounded findings remain traceable. |
| `unreliable` | Tampering, unexplained alteration, irreconcilable contradiction, circular dependence, compromised generation, or provenance failure makes the records unsafe as support. |
| `IE` | Information about provenance, completeness, edit authority, retention, independence, or transformation is insufficient to classify the component. |

Missing substantive evidence may make a dimension `IE` without making record integrity `IE`.

### 10.4 Derive the overall status

Apply in this order:

1. either component `unreliable` → overall `unreliable`;
2. otherwise either component `IE` → overall `IE`;
3. otherwise either component `limited` → overall `limited`;
4. otherwise overall `adequate`.

Keep both component statuses visible.

## 11. Produce the assessment record

### 11.1 Substantive findings table

| Dimension | Evidence state | Finding | Supporting claims | Contradicting or limiting claims | Requested and missing | Rationale |
|---|---|---|---|---|---|---|
| Counsel | | | | | | |
| Judgment | | | | | | |
| Command | | | | | | |
| Correction | | | | | | |
| Repair | | | | | | |
| Reform | | | | | | |

For Repair, include the trigger state.

### 11.2 Telemetry Integrity table

| Component | Status | Supporting claims | Limitations | Affected dimensions |
|---|---|---|---|---|
| Institutional-record integrity | | | | |
| Assessment-packet integrity | | | | |
| Derived overall status | | | | |

### 11.3 Required closing statements

Report:

- assessment boundary;
- actor-authority matrix;
- sampling and aggregation rule;
- dominant pattern or event-specific result;
- most consequential missing artifact;
- unresolved propositions;
- limitations;
- specification and schema versions;
- migration status.

## 12. Quality-control checklist

Before finalization, confirm that:

- every `0` rests on affirmative absence;
- every `1` rests on process-specific formal presence;
- every `2` rests on observed exercise or directly demonstrated operational capability;
- every `IE` identifies an unresolved proposition and search or request;
- actor attribution is explicit;
- sampling and aggregation were predeclared;
- contradictory evidence is preserved and weighted;
- reused evidence has separate construct propositions;
- every material claim has a locator;
- both integrity components are assessed;
- the overall integrity status is derived deterministically;
- no total score is calculated;
- no legal compliance, certification, or causal-effectiveness claim is made.

## 13. Inter-rater and historical-record boundary

This candidate handbook does not modify `HIT-IRP-CIGNA-001`, its frozen packet, threshold, or critical-disagreement rules.

Historical public assessments released under specification `0.1.0` remain unchanged. Any `0.4.0` migration must be a separate record with an explicit change report.
