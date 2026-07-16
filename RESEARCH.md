# Research Protocol and Claim Register

## Research object

Human Influence Telemetry is a design-science research artifact. It operationalizes substantive human influence as observable properties of institutional decision records.

## Primary research question

> Can independent reviewers use the HIT rubric to distinguish substantive human influence, ceremonial oversight, and insufficient evidence in AI-mediated institutional decision processes?

## Evidence classes

| Class | Meaning |
|---|---|
| E1 | Executable evidence produced by validation or deterministic fixtures |
| E2 | Artifact evidence directly contained in the specification, schema, case record, or public assessment |
| E3 | External source evidence supporting a construct or case finding |
| E4 | Comparative inference connecting HIT to adjacent governance concepts |
| E5 | Hypothesis requiring independent application, field data, or statistical testing |

## Claim register

| ID | Claim | Status | Update condition |
|---|---|---|---|
| H1 | HIT can represent six substantive dimensions and one cross-cutting integrity dimension in one machine-readable assessment | Demonstrated by schema, fixtures, and public case records once CI passes | Revise when a required finding cannot be represented |
| H2 | The 0/1/2/IE rubric distinguishes absence, ceremonial presence, substantive exercise, and missing evidence | Demonstrated for included fixtures and author-scored public cases only | Revise after independent scoring or failed discrimination cases |
| H3 | Independent reviewers can reach substantial agreement using the published handbook | Unresolved | Requires documented inter-rater exercise |
| H4 | HIT can identify oversight theater that binary human-in-the-loop labels miss | Supported by design logic and three public case studies; not independently validated | Requires external replication |
| H5 | Higher HIT findings predict lower harm or better repair | Hypothesis | Requires preregistered population, outcomes, and statistical method |
| H6 | A high HIT finding proves meaningful human control | Unsupported | Would require stronger causal and institutional evidence than documentary assessment alone |
| H7 | HIT evidence may support oversight, accountability, and contestability obligations in external frameworks | Provisional mapping claim | Requires qualified standards or legal review |
| H8 | HIT is independently adopted | Not yet | Requires use by an institution outside the author's control |

## Public application register

| Case | Unit of analysis | Machine-readable assessments | Primary methodological test |
|---|---|---:|---|
| Dutch childcare-benefits scandal | Belastingdienst/Toeslagen harm-period decision architecture | 1 | Ceremonial authority and appeal; separation of harm and repair windows |
| Obermeyer population-health algorithm | Deploying health systems and manufacturer | 2 | Actor decomposition; near-total IE profile; externally prompted reform |
| Cigna PxDx | Cigna claims-review workflow | 1 | Signature versus practical command; evidentiary tiers; designed disagreement |

These are retrospective, author-scored applications. Publication demonstrates applicability to heterogeneous public records. It does not resolve H3 or establish field validity.

## Methods

The research program uses artifact construction, schema validation, deterministic fixtures, retrospective public-record case studies, inter-rater reliability testing, comparative mapping, and prospective validation when institutional access becomes available.

## Threats to validity

Institutional records may be incomplete, curated, or controlled by the governed system. Recorded reasons may be post-hoc rationalizations. One exercised override may overstate intervention capacity. Retrospective cases have selection bias. Public records may not expose internal evidence access or authority. Ordinal findings may conceal variation. Reviewers may interpret ceremonial presence differently. Litigation records have different evidentiary weight at allegation, pleading, and merits stages. Framework mappings may overstate equivalence without qualified review.

## Maturity model

| Level | Name | Entry criterion |
|---|---|---|
| 1 | Defined | Stable constructs, schema, citable archive |
| 2 | Applicable | A stranger can apply the method using public materials; inter-rater exercise completed |
| 3 | Evidenced | Level 2 satisfied and at least three public-record applications published |
| 4 | Validated | Preregistered validation design and pilot result |
| 5 | Adopted | Independent institutional use and external reference |

The levels are cumulative. The repository remains at Level 1 until the inter-rater requirement for Level 2 is completed, even though the three-case evidence condition for Level 3 is now available in public-review form.

## Release discipline

A numbered release requires passing validation, synchronized schema and examples, updated limitations, accurate claim status, migration notes for normative changes, and citation metadata pointing to the exact release.

The evidence and version gates through 1.0.0 are defined in [`ROADMAP.md`](ROADMAP.md).
