# HIT 0.4.0 Replication Comparison Plan

**Protocol:** `HIT-IRP-HIT040-002`  
**Status:** Candidate  
**Primary analysis:** Pre-adjudication  
**Scorers:** Three  
**Packets:** Three

## Comparison object

The comparison operates on scorer-verified assessment JSON files. It does not compare coordinator summaries or adjudicated replacements.

Each packet contributes eight primary categorical items. Three scorer pairs create 24 pairwise comparisons per packet and 72 across the study.

## Substantive composite rule

For Counsel, Judgment, Command, Correction, and Reform, one pair agrees only when both fields match:

- `finding`;
- `evidence_state`.

For Repair, all three fields must match:

- `finding`;
- `evidence_state`;
- `repair_trigger`.

A finding match with an evidence-state mismatch is a disagreement. This rule exposes the difference between observed exercise and tested operational capability when both support finding `2`.

## Integrity rule

Compare the two component statuses separately:

- `institutional_record_integrity.status`;
- `assessment_packet_integrity.status`.

Validate `overall_status` against `unreliable>IE>limited>adequate`. Exclude the derived status from the primary denominator.

## Primary outputs

The deterministic comparison must report:

- exact pairwise matches and denominator;
- pooled pairwise exact agreement count and proportion;
- packet-level pairwise exact agreement counts and proportions;
- item unanimity count and proportion across packet-item units;
- every disagreement with packet, item, scorer pair, values, and critical status;
- threshold decision;
- input filenames and SHA-256 digests;
- protocol and packet versions;
- interpretation boundary.

## Supplementary outputs

### Finding-only agreement

Compare the six findings without evidence-state fields. This reveals whether disagreement originates in the ordinal conclusion or the evidence-state path.

### Evidence-state agreement

Compare evidence states independently across the six dimensions.

### Repair-trigger agreement

Compare `triggered`, `not_triggered`, and `indeterminate` before evaluating Repair findings.

### Weighted pairwise kappa

Calculate linearly weighted Cohen's kappa for paired determinate findings `0`, `1`, and `2`. Exclude an item from this statistic when either scorer assigns `IE`. Report the retained item count.

### Krippendorff's alpha

Report nominal alpha across `0`, `1`, `2`, and `IE` for the substantive findings. Report ordinal alpha across determinate `0`, `1`, and `2` with `IE` treated as missing. Publish the distance function and missing-data treatment.

### Source-reference overlap

For each packet-item unit, compare the set of frozen source IDs used in supporting, contradicting, and limiting evidence claims. Report Jaccard overlap separately for each relation. Do not compare scorer-generated claim IDs.

### Actor-authority agreement

For each frozen actor ID, compare:

- authority-type sets;
- mechanisms controlled;
- decision stages;
- relationship classification.

Actor-authority disagreement is reported separately from finding agreement.

### Rationale divergence

Human coders classify rationale divergence after the pre-adjudication output is frozen. Permitted categories are defined in the disagreement taxonomy. No language model may classify or summarize scorer rationales for the primary research record.

## Critical-disagreement mechanics

The comparison code mechanically marks these value conflicts:

- `IE` versus any determinate substantive finding;
- `0` versus `2`;
- Repair `triggered` versus `not_triggered`;
- integrity `unreliable` versus `adequate`;
- integrity `IE` versus a determinate status.

Boundary, actor-identity, and conformance-invalidating disagreements require coordinator review against the frozen packet and are added to the immutable comparison supplement. They do not alter the original deterministic output.

## Threshold evaluation

The comparison reports the H3 replication gate exactly as declared in the lock record:

- pooled pairwise exact agreement at least 60 of 72;
- each packet at least 19 of 24;
- unanimity at least 18 of 24 packet-item units;
- zero critical disagreements;
- nine valid, verified, independent submissions.

No threshold is recalculated after adjudication.

## Synthetic vectors

Before protocol lock, tests must cover:

1. complete unanimity;
2. one adjacent ordinal disagreement;
3. `IE` versus determinate critical disagreement;
4. `0` versus `2` critical disagreement;
5. Repair-trigger conflict;
6. integrity `unreliable` versus `adequate`;
7. derived-overall-integrity mismatch;
8. one packet below its local threshold while pooled agreement passes;
9. duplicate scorer ID;
10. missing packet submission;
11. hash mismatch;
12. schema-valid assessment with a frozen-boundary deviation.

## Interpretation boundary

The study supports a bounded claim about three public packets, three scorers, one current contract, and one comparison design. Agreement does not establish evidence truth, legal correctness, causal effectiveness, or population-wide reliability.
