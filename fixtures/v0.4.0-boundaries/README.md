# HIT v0.4.0 Boundary Fixtures

This directory contains executable candidate fixtures for all 16 ambiguity classes in `HIT-ARFR-001`.

The canonical fixture set contains exactly 48 cases:

- one `accepted` case per friction class;
- one `rejected` interpretation per friction class;
- one `boundary` case per friction class.

Each case supplies bounded facts and an expected result. `src/rubric/rules_v040.py` recomputes the result. `scripts/validate_v040_candidate.py` rejects missing friction classes, missing roles, duplicate identifiers, schema-invalid fixtures, and expected results that diverge from the rule engine.

These fixtures test the candidate rubric contract. They are synthetic and do not establish empirical validity, human inter-rater reliability, legal compliance, or field effectiveness.
