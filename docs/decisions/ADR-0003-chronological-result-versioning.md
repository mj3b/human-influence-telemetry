# ADR-0003: Allocate empirical-result releases chronologically

**Status:** Accepted  
**Date:** 2026-07-18  
**Decision owner:** Mark Julius Banasihan  
**Related decisions:** ADR-0001, ADR-0002  
**Protocol affected:** No

## Context

Earlier repository plans reserved `v0.3.0` for the result of locked protocol `HIT-IRP-CIGNA-001`.

ADR-0001 separated semantic-version advancement from research-maturity advancement and approved a technical path through `v0.4.0`, `v0.5.0`, `v0.9.0`, and `v1.0.0` without requiring scorer availability. Retaining a future `v0.3.0` release after publishing a higher version would make version order diverge from release chronology and create ambiguous upgrade semantics.

## Decision

1. `v0.3.0` is a superseded planning target and must not be created as a later Git tag or GitHub release.
2. Completion of `HIT-IRP-CIGNA-001` remains mandatory for H3 and Maturity Level 2.
3. The original submissions and the pre-adjudication result must still be published, passing or failing.
4. The empirical result will be assigned the next available repository version at the time the result package is complete.
5. The result release notes must identify the locked protocol version, frozen packet, original target label, and actual release version.
6. No technical release may imply that the human exercise was completed.

## Consequences

- semantic versions remain monotonic and chronological;
- the human protocol is no longer tied to a version number that may become unavailable;
- the research gate remains unchanged;
- historical references to “planned v0.3.0” remain valid as planning history but must be marked superseded in current documentation.

## Non-effects

This decision does not modify the protocol, scorer instructions, evidence packet, threshold, critical-disagreement rules, adjudication controls, or publication obligation.
