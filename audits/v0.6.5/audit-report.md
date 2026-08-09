# HIT v0.6.5 Research-Integrity Audit

**Audit date:** 2026-08-09

**State:** `PASS_WITH_EXCEPTIONS`

**Scope:** H1 through H9 and four material claims in the working paper. Unmapped repository prose remains outside this audit.

## Decision

The mapped claim set passes the executable controls with published exceptions. H1, H2, H3, and three bounded paper claims may enter a conclusion. The audit blocks current-contract replication, causal, legal, adoption, outcome, and clean-room claims whose required evidence is absent or indeterminate.

## Claim gates

| Claim | Traceability | Integrity | Human review | Fitness | Closure | Conclusion |
|---|---|---|---|---|---|---|
| H1 | pass | pass | pass | pass | pass | eligible |
| H2 | pass | pass | pass | pass | pass | eligible |
| H3 | pass | pass | pass | pass | pass | eligible |
| H4 | pass | pass | pass | indeterminate | pass | blocked |
| H5 | pass | pass | pass | fail | pass | blocked |
| H6 | pass | pass | pass | fail | pass | blocked |
| H7 | pass | pass | pass | indeterminate | pass | blocked |
| H8 | pass | pass | pass | fail | pass | blocked |
| H9 | pass | pass | pass | fail | pass | blocked |
| PAPER-C01 | pass | pass | pass | pass | pass | eligible |
| PAPER-C02 | pass | pass | pass | pass | pass | eligible |
| PAPER-C03 | pass | pass | pass | pass | pass | eligible |
| PAPER-C04 | pass | pass | pass | fail | pass | blocked |

## Negative controls

| Control | Expected gate | Detected |
|---|---|---|
| HIT-NC-01 | traceability | yes |
| HIT-NC-02 | integrity | yes |
| HIT-NC-03 | human_support_review | yes |
| HIT-NC-04 | evidence_fitness | yes |
| HIT-NC-05 | dependency_closure | yes |
| HIT-NC-06 | conclusion_eligibility | yes |
| HIT-NC-07 | traceability | yes |
| HIT-NC-08 | claim_boundary | yes |

## Published exceptions

- `HIT-EX-01`: Current-contract external-rater replication is unresolved; PAPER-C04 remains blocked.
- `HIT-EX-02`: H4 and H7 lack complete external review; neither may enter the paper conclusion.
- `HIT-EX-03`: H5, H8, and H9 lack outcome, adoption, or clean-room evidence.
- `HIT-EX-04`: The responsible author supplied the recorded support review; no independent assessor reproduced the v0.6.5 fitness judgments.

## Interpretation

`PASS_WITH_EXCEPTIONS` means the committed controls behaved as declared and every blocked claim remains blocked. It does not establish source truth, population reliability, current-contract replication, causal validity, legal conformity, or independent adoption.
