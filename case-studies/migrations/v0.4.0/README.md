# HIT v0.4.0 Public-Case Migration Dispositions

The four public case assessments released under HIT specification and schema `0.1.0` remain immutable historical artifacts.

Version `0.4.0` changes the assessment contract materially. Existing findings are not relabeled or copied into the current schema without a fresh source review.

`migration-manifest.json` records one explicit disposition for every released assessment:

- `historical_version_bound`: the original remains a valid historical `0.1.0` artifact, and no `0.4.0` record is claimed;
- `deferred_locked_protocol`: migration remains prohibited while a locked human protocol is pending;
- `protocol_completed_historical_version_bound`: the locked protocol is complete, the original and scorer records remain historical `0.1.0` artifacts, and a current-contract record requires a separate fresh source review.

The Cigna assessment moved to `protocol_completed_historical_version_bound` in release `0.6.0`. The change records completion of the human exercise. It does not change any historical finding or claim current-contract conformance.

These dispositions are release exceptions. They preserve historical findings and prevent silent reinterpretation.
