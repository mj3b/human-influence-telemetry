# Initial Case-candidate Source-surface Screen

**Protocol:** `HIT-IRP-HIT040-002`  
**Status:** Coordinator screening, no selection  
**Scorer access:** Prohibited until case selection and packet lock  
**Prepared:** 2026-07-18

## Purpose

This screen identifies public cases that may test different parts of the `0.4.0` contract. It records source functions, boundary feasibility, and evidentiary limits. It does not assign expected HIT findings.

A candidate survives this stage only when a later archive review confirms stable access, reproducible locators, manageable burden, actor separability, and a defensible Repair-trigger procedure.

## Slot A: exercise-rich candidates

### A1. Duke Sepsis Watch

**Proposed institutional unit:** Duke University Hospital emergency-department sepsis workflow.  
**System role:** machine-learning surveillance of EHR variables and alert routing to the rapid-response team.  
**Source-surface reason for screening:** public records describe a named clinical workflow in which rapid-response nurses review alerts, confer with treating physicians, document assessment, and facilitate or place treatment orders under defined phases.

Candidate sources:

1. ClinicalTrials.gov, `NCT03655626`, *Implementation and Evaluations of Sepsis Watch*: https://clinicaltrials.gov/study/NCT03655626
2. Sendak et al., *Real-World Integration of a Sepsis Deep Learning Technology Into Routine Clinical Care*: https://pmc.ncbi.nlm.nih.gov/articles/PMC7391165/
3. Beede et al., *Integrating a Machine Learning System Into Clinical Workflows: Qualitative Study*: https://pmc.ncbi.nlm.nih.gov/articles/PMC7714645/
4. Duke Health, *Duke’s Augmented Intelligence System Helps Prevent Sepsis in the ED*: https://physicians.dukehealth.org/articles/dukes-augmented-intelligence-system-helps-prevent-sepsis-ed

Source functions:

- ClinicalTrials.gov fixes intervention phases, workflow changes, order authority, and outcome measures.
- The implementation study documents deployment design and operating roles.
- The qualitative study documents how clinicians encountered and communicated model output.
- The Duke page supplies institutional self-description and named workflow actors.

What the surface may support:

- a stable event or period boundary;
- direct observation of human action after an alert;
- named decision consequences;
- separable system, nurse, and physician roles;
- tested changes to ordering authority and workflow.

What the surface does not yet settle:

- whether the public records expose a credibly complete decision universe;
- how often alerts were dismissed, changed, or acted upon;
- whether review notes and override records are publicly reproducible at case level;
- whether Repair is triggered within the proposed boundary.

Archive risk: low for ClinicalTrials.gov and PMC; moderate for the Duke institutional page.  
Packet burden: moderate.  
Contamination risk: low.

### A2. Allegheny Family Screening Tool

**Proposed institutional unit:** Allegheny County child-welfare hotline screening.  
**System role:** predictive risk score supporting call-screening decisions.  
**Source-surface reason for screening:** county publications and evaluations describe caseworker use of the score, changes in screening practice, impact evaluation, and a later tool and policy revision.

Candidate sources:

1. Allegheny County Analytics, *Developing Predictive Risk Models to Support Child Maltreatment Hotline Screening Decisions*: https://analytics.alleghenycounty.us/2019/05/01/developing-predictive-risk-models-support-child-maltreatment-hotline-screening-decisions/
2. Allegheny County Analytics, *Evaluation Findings on the Use of Predictive Risk Models in Child Welfare*: https://analytics.alleghenycounty.us/2024/05/31/predictive-risk-models-in-child-welfare/
3. Linked county impact-evaluation and process-evaluation reports identified from those pages, subject to archive review.

Source functions:

- County technical documentation describes system purpose, data use, workflow, and version changes.
- Evaluation reports may establish how screening decisions changed after deployment.
- Process studies may expose interaction between caseworker judgment and the score.

What the surface may support:

- a stable institutional unit and decision process;
- a process-specific human role;
- measured human decisions relative to model recommendations;
- later reform of algorithm, data sources, and associated policies;
- sampling and aggregation based on evaluation cohorts.

What the surface does not yet settle:

- whether public records provide decision-level evidence of independent reasons;
- which actor held practical command in individual referrals;
- whether corrections or appeals altered screening outcomes;
- whether the same evidence can support both period-level and event-specific claims.

Archive risk: moderate because several source files are linked from county pages.  
Packet burden: moderate to high.  
Contamination risk: low.

### A3. State v. Loomis

**Proposed institutional unit:** Wisconsin circuit-court sentencing in *State v. Loomis*.  
**System role:** COMPAS risk assessment included in the presentence record and considered by the sentencing court.  
**Source-surface reason for screening:** the official opinion identifies a named judge, a bounded sentencing event, the COMPAS assessment, other sentencing factors, and the resulting sentence.

Candidate sources:

1. Wisconsin Supreme Court, *State v. Loomis*, 2016 WI 68: https://www.wicourts.gov/sc/opinion/DisplayDocument.pdf?content=pdf&seqNo=171690
2. Wisconsin Court System case materials and certification records for docket `2015AP000157-CR`, subject to archive review.

Source functions:

- The supreme-court opinion is an adjudicated record of procedural history, sentencing use, actor roles, and legal limits on COMPAS use.
- Docket materials may supply the lower-court posture and fixed event sequence.

What the surface may support:

- an event-specific unit with named judicial authority;
- evidence that a human actor considered system output and imposed a consequential decision;
- direct actor attribution;
- explicit limits on permissible use of the assessment.

What the surface does not yet settle:

- the judge’s independent reasoning beyond the recorded explanation;
- access to the proprietary model’s internal basis;
- whether Correction and Repair can be assessed without converting HIT into a legal-merits inquiry;
- whether the packet contains enough evidence-state diversity beyond one adjudicated event.

Archive risk: low.  
Packet burden: low to moderate.  
Contamination risk: moderate because COMPAS is a heavily analyzed case.

## Slot B: constraint-rich candidates

### B1. Australian Robodebt Scheme

**Proposed institutional unit:** Australian Commonwealth income-compliance debt assessment and recovery process.  
**System role:** automated income averaging, debt calculation, and recovery workflow.  
**Source-surface reason for screening:** the Royal Commission record documents process design, administrative responsibility, review pathways, institutional knowledge, harm, and later reform recommendations.

Candidate sources:

1. Royal Commission into the Robodebt Scheme, final report and Chapter 17 materials: https://robodebt.royalcommission.gov.au/publications/report
2. Royal Commission exhibits, hearing transcripts, process maps, and witness statements selected through a bounded source review.

Source functions:

- The final report supplies adjudicated investigative findings, actor roles, procedural history, and recommendations.
- Exhibits and transcripts may provide contemporaneous or testimonial evidence of workflow, authority, review, and institutional response.
- Process maps may establish structural availability or exclusion of human capacities.

What the surface may support:

- explicit automated decision stages and named institutional actors;
- formal review and appeal channels;
- evidence of operational constraints and responsibility diffusion;
- a triggered Repair inquiry;
- a declared follow-up period for reform.

What the surface does not yet settle:

- whether a manageable packet can preserve the necessary actor distinctions;
- which decision layer should be the sole unit of analysis;
- whether the source universe can be sampled without cherry-picking the Commission record;
- whether three scorers can complete the packet within a reasonable burden.

Archive risk: low.  
Packet burden: high.  
Contamination risk: low to moderate.

### B2. Houston EVAAS Teacher Evaluation

**Proposed institutional unit:** Houston Independent School District teacher evaluation and termination process using EVAAS value-added scores.  
**System role:** proprietary statistical score used in personnel evaluation and termination decisions.  
**Source-surface reason for screening:** the federal court record describes a formal human employment process constrained by a proprietary model whose calculations teachers and the district could not independently verify or reproduce.

Candidate sources:

1. U.S. District Court for the Southern District of Texas, *Houston Federation of Teachers Local 2415 et al. v. Houston Independent School District*, No. 4:14-cv-01189: https://www.govinfo.gov/app/details/USCOURTS-txsd-4_14-cv-01189
2. Orders and exhibits within the official GovInfo case package, subject to procedural-posture review.

Source functions:

- Court orders provide procedural findings and descriptions of the evaluation mechanism.
- Record exhibits may establish employment authority, score use, challenge mechanisms, and access limits.

What the surface may support:

- process-specific human employment authority;
- a proprietary score entering a consequential personnel decision;
- evidence-access and contestability constraints;
- named institutional and vendor roles;
- a bounded judicial challenge to the process.

What the surface does not yet settle:

- the degree of independent administrator judgment in each termination;
- the population and sampling rule for period-level findings;
- whether the court record establishes affirmative absence or leaves some dimensions indeterminate;
- Repair and Reform evidence outside the litigation period.

Archive risk: low.  
Packet burden: moderate.  
Contamination risk: low.

### B3. Cigna PxDx Fresh Current-contract Review

**Proposed institutional unit:** Cigna PxDx post-service claims-review workflow.  
**System role:** procedure-to-diagnosis logic routing claims for batch medical-director disposition.  
**Source-surface reason for screening:** the prior frozen exercise documented strong process constraints. A fresh packet could test migration from the archived `0.1.0` contract to the current actor, evidence-state, Repair-trigger, sampling, and split-integrity model.

Candidate sources:

1. The prior source identifiers preserved under `validation/frozen-packet/source-manifest.json`.
2. A fresh source search conducted after protocol approval, with new hashes and procedural-posture labels.

Source functions:

- Investigative reporting describes workflow speed, batch review, and institutional response.
- Court records define allegations and procedural posture.
- Later records may support Correction, Repair, or Reform within a declared follow-up period.

What the surface may support:

- direct comparison between old and current contract requirements;
- process-specific formal presence and constraint indicators;
- actor separation among medical directors, Cigna, patients, providers, and courts;
- a useful migration stress test.

What the surface does not yet settle:

- scorer independence after public release of the prior HIT result;
- whether prior author and scorer findings create unacceptable contamination;
- whether a fresh packet would add evidence diversity beyond the first exercise;
- whether source reuse would create the appearance of confirming a known answer.

Archive risk: low.  
Packet burden: moderate.  
Contamination risk: high.  
Screening posture: backup candidate only unless contamination controls are stronger than the value of continuity.

## Slot C: evidence-limited candidates

### C1. Mobley v. Workday

**Proposed institutional unit:** employer applicant-screening process using Workday algorithmic tools, limited to the functions described in the pleadings and court record.  
**System role:** alleged screening, recommendation, or automated rejection of applicants on behalf of customer employers.  
**Source-surface reason for screening:** the public record defines the alleged system function and delegation theory while leaving employer-specific workflows, human authority, model operations, and individual decision records unresolved.

Candidate sources:

1. EEOC amicus page and brief, *Mobley v. Workday, Inc.*, No. 3:23-cv-00770: https://www.eeoc.gov/litigation/briefs/mobley-v-workday-inc
2. Published district-court orders and docket materials, with procedural posture recorded for each proposition.
3. EEOC Office of General Counsel annual report discussion of the July 12, 2024 order.

Source functions:

- The EEOC brief presents an agency theory of delegated hiring functions.
- Court orders distinguish plausible allegations from adjudicated merits.
- Docket materials may define the claims, parties, and procedural sequence.

What the surface may support:

- a bounded allegation and litigation posture;
- identified vendor and employer actor classes;
- a documented search for employer-specific authority and review records;
- genuine unresolved propositions after that search.

What the surface does not yet settle:

- which customer employer made any individual decision;
- whether a human reviewed or could change a given rejection;
- system configuration, model logic, access, correction, or repair;
- factual truth of allegations at the merits stage.

Archive risk: low to moderate.  
Packet burden: moderate.  
Contamination risk: low.

### C2. Epic Sepsis Model at Michigan Medicine

**Proposed institutional unit:** Michigan Medicine operational paging workflow using the Epic Sepsis Model, bounded to the period described in the external validation study.  
**System role:** proprietary risk score and alert threshold used to generate clinician pages.  
**Source-surface reason for screening:** the study defines the model, threshold, cohort, performance, and operational use while excluding alert-eligible patients from the retrospective evaluation and providing sparse evidence about human response and authority.

Candidate sources:

1. Wong et al., *External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients*: https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2781307
2. Published correction and related methodological materials linked from the article.
3. Later model-validation studies used only when a follow-up period is predeclared.

Source functions:

- The primary study provides performance data, cohort definition, selected threshold, and stated clinical use.
- The correction establishes the transformation history of published results.
- Later studies may clarify model version changes without establishing the earlier human workflow.

What the surface may support:

- a bounded institution, model, threshold, and period;
- sampling and selection-effect analysis;
- assessment of packet integrity and publication corrections;
- documented unresolved propositions about human action and command.

What the surface does not yet settle:

- case-level alert responses;
- who reviewed, dismissed, escalated, or acted on alerts;
- practical override or correction mechanisms;
- whether the model score changed any patient decision.

Archive risk: low.  
Packet burden: low to moderate.  
Contamination risk: low.

### C3. Population-health Risk Algorithm Studied by Obermeyer et al.

**Proposed institutional unit:** one health system’s high-risk care-management enrollment process studied in the 2019 Science paper.  
**System role:** commercial risk score using predicted cost to identify patients for additional care-management attention.  
**Source-surface reason for screening:** the study establishes the model target, allocation consequence, racial disparity, and a reformulated target while withholding vendor identity and providing limited documentation of human enrollment authority and appeal mechanisms.

Candidate sources:

1. Obermeyer et al., *Dissecting racial bias in an algorithm used to manage the health of populations*: https://doi.org/10.1126/science.aax2342
2. PubMed record: https://pubmed.ncbi.nlm.nih.gov/31649194/
3. Supplementary materials and author-posted manuscript, subject to archive and license review.

Source functions:

- The primary study establishes algorithm purpose, proxy mechanism, measured disparity, allocation context, and a technical reform experiment.
- Supplementary materials may define sample construction and decision thresholds.

What the surface may support:

- a population and sampling rule;
- the algorithm’s role in care-management allocation;
- a specific mechanism producing disparate allocation;
- a technical reform to the prediction target.

What the surface does not yet settle:

- vendor and deploying-institution identity in the public packet;
- named human authority and decision-stage control;
- appeal, correction, and individual repair mechanisms;
- whether technical reform was implemented in the assessed institution.

Archive risk: moderate because supplementary-access and licensing must be checked.  
Packet burden: moderate.  
Contamination risk: high because HIT already has an Obermeyer case narrative and two historical assessments.

## Cross-sample affirmative-absence backup

### X1. EEOC v. iTutorGroup

**Possible function:** source surface capable of testing structural exclusion of human intervention in an automated applicant-rejection rule.

Candidate sources:

1. EEOC complaint announcement: https://www.eeoc.gov/newsroom/eeoc-sues-itutorgroup-age-discrimination
2. EEOC settlement announcement: https://www.eeoc.gov/newsroom/itutorgroup-pay-365000-settle-eeoc-discriminatory-hiring-suit
3. Court filings and consent-decree materials from *EEOC v. iTutorGroup, Inc.*, No. 1:22-cv-02565.

The EEOC states that the software was programmed to automatically reject applicants above specified age thresholds and that more than 200 qualified applicants were rejected. The case may provide an explicit structural rule capable of testing affirmative absence for a bounded human intervention stage.

The current limitation is unit design. The packet must identify a consequential human capacity that the automatic rule structurally excluded. It must avoid converting the settlement into a general claim about all hiring stages.

Archive risk: low.  
Packet burden: low.  
Contamination risk: low.

## Provisional ranking for full source-function audit

The following order governs research effort. It does not select cases.

1. Duke Sepsis Watch, Slot A.
2. Houston EVAAS, Slot B.
3. Mobley v. Workday, Slot C.
4. Robodebt, Slot B, retained as the deeper public-sector alternative.
5. Allegheny Family Screening Tool, Slot A, retained as the period-level alternative.
6. iTutorGroup, cross-sample affirmative-absence backup.
7. State v. Loomis, Slot A backup.
8. Epic Sepsis Model, Slot C backup.
9. Cigna PxDx, Slot B backup with high contamination risk.
10. Obermeyer population-health algorithm, Slot C backup with high contamination risk.

## Next gate

For the first six ranked candidates, build a source-function inventory that records:

- exact artifact title and version;
- source function;
- procedural posture;
- stable locator quality;
- archive and redistribution terms;
- actor and authority information;
- Repair-trigger evidence;
- affirmative-absence, formal-presence, observed-exercise, and indeterminate test coverage;
- packet burden;
- contamination risk;
- inclusion or exclusion decision.

No candidate may receive a packet ID until that inventory is complete.
