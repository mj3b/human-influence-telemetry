# Adjacent-System Boundaries

**Status:** Normative terminology and claim boundary for the HIT v1 workstream  
**Reviewed:** 2026-07-17

Human Influence Telemetry occupies a documentary-assurance layer. It evaluates what observable records establish about human influence across one bounded institutional decision process.

HIT does not implement runtime agent enforcement, signed-receipt interoperability, cryptographic verification, policy-pack harmonization, compliance automation, or the decision-record architecture supplied by Governed Decision Intelligence.

## Layer comparison

| System or artifact | Unit of analysis | Primary function | Typical output | Relationship to HIT |
|---|---|---|---|---|
| Microsoft Agent Governance Toolkit | Agent action, tool call, message, delegation, or runtime request | Intercept actions, evaluate policy, verify identity or capability, allow, deny, require approval, sandbox, and audit | Runtime policy decision and audit event | Its events may supply evidence to HIT. HIT does not enforce the action. |
| ScopeBlind agent-governance test vectors and Acta receipts | Signed governance receipt and receipt chain | Verify schema, canonicalization, signatures, attribution, ordering, and hash-chain integrity across implementations | Cryptographically verifiable receipt result | Verified receipts may strengthen provenance evidence. HIT does not define or verify the receipt protocol. |
| Credo AI platform and Agent Governor | Governed AI entity, policy requirement, risk, control, workflow, or runtime trace | Translate policy into controls, apply policy packs, map compliance requirements, collect evidence, and govern agents into runtime | Policy, control, workflow, evidence, and runtime-governance artifacts | Credo artifacts may become evidence inputs. HIT does not provide policy packs, universal control mappings, or compliance automation. |
| Governed Decision Intelligence | One consequential AI-assisted decision | Preserve the decision question, evidence, uncertainty, alternatives, authority, gate classification, outcome, and obligations | Governed Decision Record | A GDR may supply structured inputs to HIT. HIT does not replace the GDR. |
| Decision Evidence Applicability Specification | One decision-evidence artifact evaluated against one external requirement | Determine relevance, assurance use, local evidence requirements, sufficiency limits, and points of non-equivalence | Evidence-applicability determination | DEAS evaluates what HIT or GDI evidence may support under a specified regime. |
| Human Influence Telemetry | One bounded institutional decision process | Assess whether human access, judgment, authority, correction, repair, and reform retained practical force | HIT assessment record with six findings plus Telemetry Integrity | This repository's scope. |

## Terminology contract

### Institutional decision

A consequential decision made or adopted by an institution and capable of affecting a person, organization, resource, right, benefit, risk posture, or system state.

### Runtime policy decision

A pre-execution or in-execution determination that an agent action is allowed, denied, constrained, escalated, or requires approval under configured policy.

A runtime policy decision is not automatically an institutional decision and does not by itself establish substantive human influence.

### Governed Decision Record

The GDI artifact that preserves the evidence, authority, uncertainty, alternatives, gate classification, outcome, and obligations of one consequential decision.

### HIT assessment record

The machine-readable output of applying the HIT rubric to one bounded process. It contains findings about Counsel, Judgment, Command, Correction, Repair, Reform, and Telemetry Integrity.

A HIT assessment record is not a runtime policy decision or a cryptographic receipt.

### Documentary telemetry

Observable, time-bounded evidence that may reveal whether human influence existed and had practical force. It may include decision records, access logs, reviewer notes, authority records, override events, appeals, remediation records, system-change records, and provenance metadata.

In HIT, telemetry does not mean a runtime observability SDK, event collector, tracing system, or enforcement middleware.

### Assessment-contract conformance

A determination that a HIT assessment satisfies the published structural and normative contract for its declared version.

Unqualified claims of agent-governance conformance, legal conformity, standards certification, or receipt interoperability are prohibited.

### Cryptographic receipt

A signed, canonically encoded, independently verifiable artifact that establishes properties such as attribution, integrity, ordering, and chain linkage.

HIT may consume the evidentiary result of receipt verification. HIT does not generate or verify cryptographic receipts unless a future, separately versioned capability explicitly implements that function.

### Evidence-applicability determination

A DEAS result stating whether a defined evidence artifact is relevant to a specified governance requirement, what assurance claim it may support, what local evidence is additionally required, and where apparent equivalence fails.

Applicability does not mean that governance, evidence, controls, or legal conclusions are portable across regimes.

## Claim restrictions

HIT must not claim that it:

- intercepts, allows, denies, blocks, sandboxes, or terminates agent actions;
- compiles policy into runtime or harness configuration;
- verifies agent identity, trust, privileges, or capabilities;
- creates signed receipts, canonical wire formats, or cryptographic receipt chains;
- provides cross-implementation receipt conformance;
- supplies policy packs or a universal harmonized-control crosswalk;
- automates legal compliance, certification, or standards conformity;
- makes governance findings or evidence legally portable across regimes;
- guarantees that a human decision was correct, lawful, fair, accurate, or harmless.

Preferred HIT verbs are: **assess, evaluate, reconstruct, distinguish, identify, classify, document, and test documentary evidence**.

## Composition rules

The systems may compose without collapsing their boundaries:

1. A runtime governor evaluates an action and emits a control or enforcement event.
2. A signed-receipt system may seal that event or a larger payload and make integrity independently verifiable.
3. GDI may preserve the institutional decision context surrounding the event.
4. HIT may assess whether the broader records show substantive human influence.
5. DEAS may evaluate what the resulting evidence can support under a specified governance regime.

No layer inherits the claims of another merely because their artifacts are linked.

## v1 claim-audit gate

Before HIT `1.0.0`, the repository must pass an adjacent-system claim audit confirming that public language:

- describes HIT as documentary assurance rather than runtime governance;
- uses **HIT assessment record**, not an unqualified **decision record**, for HIT outputs;
- qualifies conformance as HIT assessment-contract conformance;
- distinguishes Telemetry Integrity from cryptographic receipt verification;
- names Microsoft AGT, ScopeBlind/Acta, Credo AI, GDI, and DEAS accurately;
- contains no claim that HIT performs enforcement, signed-receipt interoperability, policy-pack harmonization, compliance automation, or evidence portability.

## Public references reviewed

- Microsoft Agent Governance Toolkit: https://github.com/microsoft/agent-governance-toolkit
- Microsoft AGT limitations: https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/LIMITATIONS.md
- ScopeBlind agent-governance test vectors: https://github.com/ScopeBlind/agent-governance-testvectors
- Credo AI platform: https://www.credo.ai/
- Credo AI Policy Packs: https://www.credo.ai/glossary/credo-ai-policy-pack
- Governed Decision Intelligence: https://github.com/mj3b/governed-decision-intelligence
