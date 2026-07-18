# HIT v0.4.0 Adjacent-System Claim Audit

**Audit status:** Passed for candidate artifacts  
**Audit date:** 2026-07-18  
**Systems reviewed:** Microsoft Agent Governance Toolkit, ScopeBlind/Acta, Credo AI, Governed Decision Intelligence, Decision Evidence Applicability Specification

## Audit questions and results

| Boundary | Candidate representation | Result |
|---|---|---|
| Runtime enforcement | HIT evaluates documentary evidence and does not intercept, allow, deny, sandbox, or terminate actions | Pass |
| Agent identity and privileges | HIT may consume identity or capability records but does not implement identity or privilege enforcement | Pass |
| Signed receipts | HIT may consume verified receipts but does not define canonicalization, signatures, chaining, or receipt interoperability | Pass |
| Policy packs and harmonized controls | HIT does not provide policy packs, universal control mappings, policy-to-code compilation, or compliance automation | Pass |
| Governed Decision Records | HIT produces a HIT assessment record, not a GDR | Pass |
| Evidence applicability | DEAS evaluates regime-specific applicability, sufficiency boundaries, and non-equivalence; HIT does not make evidence portable | Pass |
| Conformance | Candidate claims are limited to HIT assessment-contract and fixture conformance | Pass |
| Telemetry | Defined as time-bounded documentary evidence, not a runtime observability product | Pass |

## Prohibited release claims

The release must not state or imply that HIT:

- is a runtime agent governor;
- provides agent-governance conformance generally;
- creates or verifies cryptographic receipts;
- harmonizes controls across legal regimes;
- certifies compliance or legal sufficiency;
- makes governance evidence portable;
- establishes human reliability through synthetic fixtures.

## Composition statement

Runtime systems, signed receipts, policy platforms, GDRs, and DEAS determinations may supply or qualify evidence used by HIT. Their functions remain separate and are not inherited by composition.
