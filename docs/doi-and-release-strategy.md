# DOI and Release Strategy

## Decision

Human Influence Telemetry should receive a separate Zenodo software record when a release is successfully archived.

DOI `10.5281/zenodo.21204892` identifies the originating research concept. It is not a version DOI for this standalone software repository.

As of release `0.4.0`, no standalone HIT software DOI has been assigned. The repository must state that directly and must not display a software DOI badge until a public Zenodo record exists.

## Identifier model

1. **Originating research DOI**
   - `10.5281/zenodo.21204892`
   - Identifies the originating concept and research lineage.

2. **HIT software concept DOI**
   - Assigned after the first successful standalone software archive.
   - Identifies the collection of archived HIT releases.

3. **HIT version DOI**
   - Assigned to a successfully archived release.
   - Identifies the exact released files and metadata.

A GitHub tag or release does not by itself prove that a software DOI exists.

## Relationship metadata

The software record should reference the originating research DOI as `isSupplementTo`. The public software operationalizes and supplements the research concept without replacing it.

After Zenodo assigns software identifiers:

- add the software concept DOI and exact version DOI to `CITATION.cff` in a follow-up release;
- retain the originating DOI as a clearly described related identifier;
- add a DOI badge only after the public record resolves;
- update release documentation and the changelog;
- do not move or rewrite an immutable Git tag merely to insert a DOI.

## Release sequence

1. Prepare synchronized repository, component, citation, and Zenodo metadata.
2. Run validation on the exact release candidate.
3. Merge the release pull request.
4. Create the Git tag and GitHub release from the exact merged commit.
5. Confirm the Zenodo repository integration state.
6. Observe the processing record for the release event.
7. Verify any public concept DOI, version DOI, and metadata.
8. Record assigned identifiers in a controlled follow-up pull request.

A missing software DOI does not invalidate the GitHub release. It means archival identity remains incomplete and must be reported accurately.

## 0.4.0 handling

Release `0.4.0` is the next archival opportunity. Repository, specification, assessment schema, and dimension catalog all identify version `0.4.0`.

The release remains Maturity Level 1. A software DOI would identify an archived software artifact; it would not establish human reliability, validation, certification, legal compliance, or institutional adoption.

When the GitHub integration does not produce a record, a manual Zenodo software upload may be used after checking for duplicate-record risk. The uploaded archive must correspond exactly to the tagged release, and the resulting DOI must be added only in a later repository update.

## Metadata precedence

The repository contains both `CITATION.cff` and `.zenodo.json`. When `.zenodo.json` is present, it controls Zenodo ingestion metadata. The two files must remain semantically consistent.

Current component versions:

- repository release: 0.4.0;
- specification: 0.4.0;
- assessment schema: 0.4.0;
- dimension catalog: 0.4.0.

## Non-claims

A DOI establishes persistence, citation, and archival identity. It does not establish peer review, empirical validity, certification, legal compliance, institutional adoption, or correctness of assessments.
