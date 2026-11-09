- [~] (claimed 2026-11-09-0105, wt: under ~/worktrees/briefs, brief only, session d4a0fcf3) ⏳ **Rule-4 cold pass queued: G3 keeps image metadata (Exif, GPS,
      IPTC, XMP, PNG text) field by field, with a dated migration for
      type-level lines, and `nz-phone` skips digit runs inside hex digests
      (`020/450` parts 1 and 2, `320/470`).**
      `leakscan` is a blocking guard every child runs, and a too-wide skip or
      a misread tag is silent by construction. So the authoring session (a
      principal-opened Opus 5.5 queue run, session 4c65083c, 2026-11-03,
      which dispatched the Sonnet worker that wrote the code) queues this and
      does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/leakscan.py`, `tools/test_leakscan.py`,
      `tools/test_report.py`, `tools/README.md`, `CHANGELOG.md` (commits
      `7bc0f87` and `29021b9`, which close `320/470` and land `020/450`
      part 1, widened by `1297df4`, part 2; all on `main`, 2026-11-03).
      *Intent records:*
      [`../020-policy-as-code-programme-five-tracks-mik/450-g3-keeps-image-metadata-field-by-field-not-by-data-type.md`](../020-policy-as-code-programme-five-tracks-mik/450-g3-keeps-image-metadata-field-by-field-not-by-data-type.md),
      [`../320-child-filed-findings-via-pointing-up/470-leakscan-nz-phone-matches-digit-runs-inside-hex-digests.md`](../320-child-filed-findings-via-pointing-up/470-leakscan-nz-phone-matches-digit-runs-inside-hex-digests.md).
