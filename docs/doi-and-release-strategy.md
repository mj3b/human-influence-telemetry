# DOI and Release Strategy

## Decision

Human Influence Telemetry should receive a separate Zenodo software record when the GitHub `v0.1.0` release is archived.

The existing DOI `10.5281/zenodo.21204892` identifies the originating research concept and the broader Poenitentia Institutionum research record. It should not be presented as the version DOI for this standalone software repository.

## Identifier model

The project should maintain three distinct identifiers:

1. **Originating research DOI**
   - `10.5281/zenodo.21204892`
   - Identifies the concept record and broader originating research.

2. **HIT software concept DOI**
   - Assigned by Zenodo after the first GitHub release is archived.
   - Identifies the collection of archived HIT software releases.
   - Becomes the preferred DOI when citing the evolving software project without requiring a specific version.

3. **HIT version DOI**
   - Assigned to each archived release, beginning with `v0.1.0`.
   - Identifies the exact released files and metadata.
   - Should be used for reproducibility and version-specific claims.

## Relationship metadata

The HIT software record should reference the originating research DOI using a related-identifier relationship. The initial repository metadata uses `isSupplementTo` because the public software artifact operationalizes and supplements the originating concept record without replacing it.

After Zenodo assigns the software identifiers:

- add the HIT software concept DOI and `v0.1.0` version DOI to `CITATION.cff`;
- keep the originating research DOI as a clearly described related identifier;
- add a DOI badge to `README.md`;
- update the release note and changelog with the version DOI;
- do not rewrite the files in the already archived `v0.1.0` snapshot solely to insert its newly assigned DOI.

The next repository version may carry the identifiers assigned to `v0.1.0`, while Zenodo remains the authoritative record for the archived release.

## Release sequence

1. Merge the release-hardening pull request after CI passes.
2. In Zenodo, connect and enable `mj3b/human-influence-telemetry`.
3. Create a GitHub release from tag `v0.1.0` using `docs/releases/v0.1.0.md` as the release notes.
4. Wait for Zenodo to archive the GitHub release.
5. Verify the Zenodo metadata, software concept DOI, version DOI, and archival status.
6. Record the assigned identifiers in a follow-up pull request.

## Metadata precedence

The repository contains both `CITATION.cff` and `.zenodo.json` for different audiences. Zenodo uses `.zenodo.json` when both files are present. The two files must remain semantically consistent even though `.zenodo.json` controls Zenodo release ingestion.

## Non-claims

A DOI establishes persistence, citation, and archival identity. It does not establish peer review, validation, certification, legal compliance, or institutional adoption.
