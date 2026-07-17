# Portfolio Terminology Audit

Use this checklist before each release candidate and stable release.

## Human Influence Telemetry

- [ ] HIT is described as documentary assurance.
- [ ] HIT outputs are called HIT assessment records.
- [ ] Telemetry is qualified as documentary telemetry.
- [ ] Conformance is qualified as HIT assessment-contract conformance.
- [ ] HIT does not claim runtime enforcement, signed-receipt verification, policy-pack harmonization, compliance automation, or evidence portability.

## Microsoft Agent Governance Toolkit

- [ ] AGT is described as runtime action-governance middleware.
- [ ] Allow, deny, approval, identity, capability, sandboxing, and audit functions are attributed to AGT rather than HIT.
- [ ] AGT audit events are described as possible evidence inputs, not proof of substantive human influence.

## ScopeBlind / Acta

- [ ] Signed-receipt schema, canonicalization, signature, attribution, ordering, and chain verification are attributed to the receipt layer.
- [ ] HIT does not claim cross-implementation receipt conformance.
- [ ] Cryptographic integrity is distinguished from record completeness, truth, and substantive human influence.

## Credo AI

- [ ] Policy packs, policy-to-code translation, control mapping, governance workflows, compliance mapping, evidence collection, and runtime governance are attributed to Credo AI.
- [ ] HIT does not claim to be a governance platform, policy-pack system, or compliance engine.

## GDI

- [ ] Governed Decision Record refers only to the GDI artifact.
- [ ] HIT may consume a GDR but does not replace it.
- [ ] Decision reconstruction is separated from assessment of human influence.

## DEAS

- [ ] DEAS means Decision Evidence Applicability Specification.
- [ ] DEAS evaluates relevance, assurance use, local evidence requirements, sufficiency limits, and non-equivalence.
- [ ] Public language does not imply that governance, controls, findings, evidence, or legal conclusions are portable across regimes.

## Release decision

- [ ] No overloaded term remains unqualified where it could collapse two system layers.
- [ ] README, specification, handbook, release notes, citation metadata, and external descriptions use the same terminology.
- [ ] Any exception is documented with a specific reason and expiration or update condition.
