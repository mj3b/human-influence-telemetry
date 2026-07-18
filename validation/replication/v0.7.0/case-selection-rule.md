# HIT v0.7.0 Case-Selection Rule

## Purpose

The first human exercise produced perfect exact agreement and zero category variance across the six substantive dimensions. The next sample must test whether the `0.4.0` contract distinguishes different evidence states and levels of human influence.

Case selection therefore targets discriminating power. It does not target a preferred pass result.

## Selection sequence

Candidate cases are screened in this order:

1. define the institutional decision process;
2. define the actor or actor class;
3. define the assessment period;
4. identify the public record universe;
5. classify source procedural posture;
6. determine whether the record can support precise locators and proposition-level evidence;
7. estimate the expected evidence-state profile without assigning final HIT findings;
8. assess contamination risk from prior HIT analysis;
9. assess whether the packet can be frozen and used by independent scorers;
10. record inclusion or exclusion before author scoring.

## Required strata

The three-case set must contain:

- one exercise-positive stratum, where the record appears capable of showing at least one observed exercise or directly demonstrated operational capability;
- one ceremonial-presence stratum, where the record appears capable of showing formal human presence with thin practical influence;
- one evidence-limited stratum, where the record appears unable to resolve at least one material proposition and should test disciplined use of `IE`.

The stratum label is coordinator-only. It is a sampling rationale and cannot appear in scorer-facing materials.

## Inclusion criteria

A case is eligible when:

1. the institutional unit and actor boundary can be stated without relying on private knowledge;
2. at least two independent primary or high-quality secondary sources describe the same bounded process;
3. the source set supports stable archiving or exact citation locators;
4. procedural posture can be stated for every legal or investigative source;
5. the packet can include contradictory or limiting evidence where it exists;
6. the record supports a declared sampling and aggregation rule;
7. the case can be evaluated under the `0.4.0` Repair trigger and split Telemetry Integrity model;
8. scorer exposure to prior HIT findings can be controlled;
9. affected persons and institutions can be described without unnecessary personal data;
10. publication of the frozen packet is legally and ethically supportable.

## Exclusion criteria

Exclude a case when:

- the actor boundary changes across sources and cannot be resolved before scoring;
- the central evidence depends on inaccessible, unstable, or unverifiable material;
- a court record is treated as a merits finding when it reflects only allegations or procedural rulings;
- the packet would require copyrighted full-text redistribution beyond permitted use;
- the author has already published a detailed `0.4.0` assessment that scorers are likely to encounter;
- the record is so sparse that every substantive dimension would predictably collapse to `IE`;
- the record is so homogeneous that the full three-case sample would still contain only one substantive finding category;
- case selection depends on knowing which case would make the protocol pass.

## Candidate scoring matrix

Each candidate receives a coordinator-only screening record with these fields:

| Field | Allowed values |
|---|---|
| actor boundary stability | high, medium, low |
| source accessibility | complete, partial, unstable |
| locator precision | exact, bounded, weak |
| procedural posture clarity | clear, mixed, unclear |
| contradiction availability | present, absent, unknown |
| likely evidence-state variation | high, medium, low |
| prior HIT contamination risk | low, medium, high |
| privacy burden | low, medium, high |
| packet feasibility | ready, remediable, exclude |
| sampling stratum | exercise-positive, ceremonial-presence, evidence-limited |

No predicted dimension finding belongs in this matrix.

## Selection decision record

Every included and excluded candidate receives a short decision record containing:

- candidate identifier;
- decision process and actor boundary;
- source classes reviewed;
- inclusion or exclusion decision;
- mechanism supporting the decision;
- contamination assessment;
- unresolved uncertainty;
- update condition.

## Freeze condition

The final three cases are frozen together. Replacing one case after scorer findings become known is prohibited. A source-access failure discovered before any scorer begins may justify a documented packet replacement. Once one scorer begins, replacement requires a new protocol version and preservation of the abandoned packet.
