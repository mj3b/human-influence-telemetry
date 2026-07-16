# DOI and Release Strategy

## Decision

Human Influence Telemetry should receive a separate Zenodo software record when a GitHub release is successfully archived.

The existing DOI `10.5281/zenodo.21204892` identifies the originating research concept and the broader *Poenitentia Institutionum* research record. It must not be presented as a version DOI for this standalone software repository.

As of the v0.2.0 release preparation, no standalone HIT software DOI has been assigned. The repository must state that condition directly and must not display a DOI badge for the software until Zenodo produces a public record.

## Identifier model

The project maintains three distinct identifier classes:

1. **Originating research DOI**
   - `10.5281/zenodo.21204892`
   - Identifies the originating concept record and broader research lineage.

2. **HIT software concept DOI**
   - Assigned by Zenodo after the first successfully archived GitHub release.
   - Identifies the collection of archived HIT software releases.
   - Becomes the preferred DOI when citing the evolving software project without requiring a specific version.

3. **HIT version DOI**
   - Assigned to each successfully archived release.
   - Identifies the exact released files and metadata.
   - Should be used for reproducibility and version-specific claims.

The first successful archive may be v0.1.0 or a later release. The repository must not claim that a version DOI exists merely because a GitHub tag or release exists.

## Relationship metadata

The HIT software record should reference the originating research DOI using a related-identifier relationship. Repository metadata uses `isSupplementTo` because the public software artifact operationalizes and supplements the originating concept record without replacing it.

After Zenodo assigns software identifiers:

- add the HIT software concept DOI and the archived release's version DOI to `CITATION.cff` in a later repository version;
- keep the originating research DOI as a clearly described related identifier;
- add a DOI badge to `README.md` only after the public Zenodo record resolves;
- update release documentation and the changelog with the assigned version DOI;
- do not rewrite or move an already published Git tag solely to insert a DOI into that immutable snapshot.

Zenodo remains authoritative for version relationships among archived deposits.

## Release sequence

1. Prepare synchronized repository-release metadata.
2. Run repository validation on the exact release candidate.
3. Merge the release-preparation pull request.
4. Create the GitHub tag and release from the merged commit.
5. Confirm that Zenodo has the repository enabled before publication.
6. Observe the Zenodo processing record for the new release event.
7. Verify the public record, software concept DOI, version DOI, and metadata.
8. Record assigned identifiers in a follow-up pull request.

A missing software DOI does not invalidate the GitHub release. It means the archival and identifier step remains incomplete and must be reported as such.

## v0.2.0 handling

Version 0.2.0 is the next automatic archival opportunity. Its `.zenodo.json` metadata identifies repository release 0.2.0 while the unchanged specification, assessment schema, and dimension catalog remain at version 0.1.0.

Do not create a duplicate manual Zenodo upload while the GitHub integration may still process the release. If Zenodo records an error, preserve the exact error message and correct the metadata or release event through a controlled follow-up.

## Metadata precedence

The repository contains both `CITATION.cff` and `.zenodo.json` for different audiences. Zenodo uses `.zenodo.json` when both files are present. The two files must remain semantically consistent about the repository release even though `.zenodo.json` controls Zenodo release ingestion.

Component versions are intentionally separate:

- repository release: 0.2.0;
- specification: 0.1.0;
- assessment schema: 0.1.0;
- dimension catalog: 0.1.0.

## Non-claims

A DOI establishes persistence, citation, and archival identity. It does not establish peer review, validation, certification, legal compliance, institutional adoption, or correctness of the included assessments.
