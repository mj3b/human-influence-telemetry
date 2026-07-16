# HIT Application Handbook

## 1. Define the assessment boundary

Before requesting records, define one decision type, one institutional unit, one bounded period, one sampling rule, the AI system's role, and the human authority's stated role.

Do not change the boundary after seeing the evidence without recording the change and reason.

## 2. Request artifacts, not conclusions

Ask for records by type. Do not ask the institution to prove that human oversight was meaningful.

| Dimension | Illustrative requests |
|---|---|
| Counsel | case-file access logs, evidence packet shown to reviewers, retrieval timestamps |
| Judgment | reviewer notes, decision rationales, dissent records, alternatives considered |
| Command | authority matrix, delegation instrument, override and stop-use logs |
| Correction | appeal register, escalation log, reversals, interruption tests |
| Repair | restitution records, corrected decisions, notifications, remediation ownership |
| Reform | model retirement, threshold revision, workflow redesign, authorizing records |
| Telemetry Integrity | record architecture, edit permissions, provenance, retention, tamper evidence |

## 3. Apply the findings

### 0: Absent

The relevant practice or artifact did not exist in the assessed process.

### 1: Present but ceremonial

The form of oversight existed, but the records do not show practical capacity to alter the decision path.

### 2: Present and substantively exercised

The records show an instance where the relevant human capacity affected the decision path or where the institution demonstrably maintained and exercised that capacity.

### IE: Insufficient evidence

Use `IE` when the requested records were not produced or cannot distinguish absence from missing evidence. Record the missing artifact and the stated reason. Do not convert `IE` to zero.

## 4. Resolve ambiguity downward

When evidence supports both a ceremonial and substantive interpretation, use the lower finding and document the ambiguity. This reduces optimistic inference.

The downward rule applies to ordinal ambiguity such as `1` versus `2`. It does not authorize converting uncertainty about whether a practice existed into `0`. Use `IE` when the evidence cannot distinguish absence from unavailable evidence.

## 5. Assess Telemetry Integrity separately

Report provenance, completeness, controlled edit authority, operational independence, tamper evidence, retention, and missing-record disclosure. Telemetry Integrity is not averaged with the six substantive dimensions.

## 6. Produce one finding table

| Dimension | Finding | Supporting artifacts | Requested and missing | Rationale |
|---|---|---|---|---|
| Counsel | | | | |
| Judgment | | | | |
| Command | | | | |
| Correction | | | | |
| Repair | | | | |
| Reform | | | | |

Report Telemetry Integrity below the table, followed by the assessment boundary, dominant pattern, most consequential missing artifact, and limitations.

## 7. Quality-control rules

Cite each artifact precisely. Separate observation from interpretation. Preserve contradictory records. Record sampling changes. Do not infer intention. Do not declare compliance. Do not use a total score until a validated aggregation rule exists. Keep synthetic fixtures clearly labeled.

## 8. Inter-rater exercise

Two reviewers should independently assess the same frozen materials without discussing findings. The scorer packet, evidence boundary, protocol, submission contract, comparison rule, and advancement threshold must be fixed before scoring begins.

The candidate v0.3.0 procedure is defined in [`validation/inter-rater-protocol.md`](../validation/inter-rater-protocol.md). It requires:

- two scorers independent of the author and of each other;
- no prior access to the author's case scores;
- the same fixed source packet;
- one schema-valid submission per scorer;
- publication of original submissions before adjudication changes any method artifact;
- exact comparison across six substantive dimensions plus Telemetry Integrity;
- preservation and classification of every disagreement.

The predeclared Level 2 gate is at least six exact agreements across seven items and zero critical disagreements. Unweighted Cohen's kappa across the six substantive dimensions is supplementary rather than decisive because the first exercise is small.

Adjudication may explain disagreement or propose later rubric changes. It must not overwrite original scores, recalculate the primary result after discussion, or conceal a failing exercise.
