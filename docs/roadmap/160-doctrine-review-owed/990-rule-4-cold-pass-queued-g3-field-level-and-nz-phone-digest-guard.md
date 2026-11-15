- [~] ⏳ **Rule-4 cold pass queued: G3 keeps image metadata (Exif, GPS,
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
      📝 BRIEF WRITTEN 2026-11-09 by session d4a0fcf3 (Opus 5.5, headless,
      started by coordinating session 74f2b8cd; neither authored this delta):
      `docs/reviews/2026-11-09-0207-g3-field-level-nz-phone-digest-cold.md`,
      with its `.deferred.md` sibling. Pass size: large. Review NOT run: this
      pass waits for a criterion-passing cold Fable session and the
      principal's explicit permission for Fable work. Neither named session
      may run it.
      🗒️ Noted 2026-11-09: `29021b9`, cited above, is a pre-rebase hash that
      is not on `main`; the landed part 1 commit is `2ba261b`.
      🔒 CLAIMED 2026-11-15T19:55Z UTC for the cold pass, in Mike's weekly Fable drain
      (his `/fable-drain` order, 2026-11-16 06:53 NZDT; approval lapses at the
      reset, 2026-11-15 23:00 UTC). Orchestrator: a headless Opus 5.5 session
      started by drain session 21a271a5, a rule-4 off-tier orchestrator that
      holds the context partition, forms no finding and writes no severity.
      Reviewer: Fable 5.1, tier checked at selection, spawned by that
      orchestrator. Neither is a barred session (d4a0fcf3, 74f2b8cd, 4c65083c
      and what it started). The sibling is held out of the worktree until act 1
      is committed. The item's "waits for the principal's explicit permission
      for Fable work" is met by that drain order.
