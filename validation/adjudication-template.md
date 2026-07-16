# HIT Inter-rater Adjudication Record

**Protocol ID:** `HIT-IRP-CIGNA-001`  
**Packet ID:** `HIT-IR-CIGNA-PXDX-001`  
**Comparison artifact:** `results/pre-adjudication-comparison.json`  
**Adjudicator:**  
**Date:**

## 1. Integrity checks

- [ ] Both original scorer submissions are committed unchanged.
- [ ] Both submissions validate against `scorer-submission.schema.json`.
- [ ] Scorer public IDs are distinct.
- [ ] All independence attestations are true.
- [ ] All three packet sources were accessed by both scorers.
- [ ] The deterministic comparison was generated before adjudication.
- [ ] No scorer revised a finding after seeing the other submission.

## 2. Pre-adjudication result

- Exact agreements: ___ / 7
- Exact-agreement proportion: ___
- Critical disagreements: ___
- Supplementary substantive-dimension Cohen's kappa: ___
- Predeclared threshold met: yes / no

The maturity decision must use this pre-adjudication result.

## 3. Dimension-level disagreements

Repeat this section for each nonmatching item.

### Dimension: [name]

- Scorer A finding:
- Scorer B finding:
- Mechanically critical: yes / no
- Taxonomy code or codes:
- Source references cited by Scorer A:
- Source references cited by Scorer B:
- Difference in evidence interpretation:
- Difference in construct interpretation:
- Adjudicator analysis:
- Is one finding better supported under the current rubric?:
- Does the current rubric govern the disagreement clearly?:
- Proposed change, if any:
- Target version for proposed change:

## 4. Agreement without adjudication

List any dimensions where findings match but rationales reveal a material difference that should be recorded.

## 5. Method update consequences

For each proposed change, identify the affected artifacts:

- [ ] `SPECIFICATION.md`
- [ ] `schema/hit-assessment.schema.json`
- [ ] `schema/hit-dimension-catalog.json`
- [ ] `docs/application-handbook.md`
- [ ] fixtures
- [ ] public case studies
- [ ] scorer protocol
- [ ] validator
- [ ] migration notes

No normative change becomes effective through this adjudication file alone.

## 6. Claim and maturity decision

- H3 status after the exercise:
- Maturity level after the exercise:
- Basis for the decision:
- Remaining uncertainty:

## 7. Preservation statement

The original scorer submissions and pre-adjudication comparison remain authoritative evidence of the exercise. This adjudication record explains disagreement and may recommend later changes. It does not overwrite original findings or recalculate the primary result after discussion.
