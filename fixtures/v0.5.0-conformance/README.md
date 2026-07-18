# HIT 0.5.0 complete-record conformance suite

This suite derives complete assessment records from the canonical `0.4.0` example through deterministic mutations. It tests structural validity and cross-record semantics that cannot be represented by isolated rubric facts alone.

The suite currently covers:

- schema-version rejection;
- exact dimension coverage;
- actor and evidence-claim references;
- actor-to-claim attribution reciprocity;
- claim relation and dimension consistency;
- Telemetry Integrity derivation;
- Repair trigger consistency;
- event and period aggregation boundaries;
- citation precision;
- support requirements for determinate findings;
- documentation requirements for `IE`.

Each derived record receives a SHA-256 digest over canonical JSON. Reports omit timestamps and sort cases and issues deterministically.

These fixtures establish implementation conformance only. They do not establish empirical validity, human reviewer agreement, legal compliance, or institutional effectiveness.
