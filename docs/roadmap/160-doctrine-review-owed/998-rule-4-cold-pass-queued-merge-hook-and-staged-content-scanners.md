- [~] ⏳ **Rule-4 cold pass queued: the `pre-merge-commit` hook, the repo-local
      seam documentation, and the five content scanners reading the staged index
      (`115/340`, `320/560`, `320/600` both slices).** The merge hook and the
      five scanners reach every child's hook plane and next CI run, and
      `GUARDS.md` gained a section, so the authoring session (a principal-opened
      Opus 5.5 queue run, session 4c65083c, 2026-11-03, which dispatched the
      Sonnet worker that wrote the code) queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code and doctrine cold pass, per `method/REVIEW.md` rule 4,
      since `docs/method/GUARDS.md` changed.
      *Delta, scoped to paths:* `tools/pre-merge-commit.sample`,
      `.githooks/pre-merge-commit`, `.githooks/pre-commit`,
      `tools/pre-commit.sample`, `tools/test_precommit.py`, `tools/report.py`,
      `tools/spellscan.py`, `tools/test_spellscan.py`, `tools/wrapscan.py`,
      `tools/test_wrapscan.py`, `tools/datescan.py`, `tools/test_datescan.py`,
      `tools/reviewscan.py`, `tools/test_reviewscan.py`, `tools/sizescan.py`,
      `tools/test_sizescan.py`, `tools/floor.py`, `tools/README.md`,
      `docs/method/GUARDS.md`, `commands/install-hook.md`,
      `skills/create-repo/SKILL.md`, `CHANGELOG.md` (commits `b5e6ead`, `625f29a`
      and `7673da1`, on `main`, 2026-11-03, and the commit that lands `320/600`
      slice 2).
      *Intent records:*
      [`../115-guardrail-architecture-mike-commissioned/340-merges-cherry-picks-and-rebases-skip-the-hook-plane.md`](../115-guardrail-architecture-mike-commissioned/340-merges-cherry-picks-and-rebases-skip-the-hook-plane.md),
      [`../320-child-filed-findings-via-pointing-up/560-the-repo-local-check-seam-is-absent-from-the-readme-and-method-docs.md`](../320-child-filed-findings-via-pointing-up/560-the-repo-local-check-seam-is-absent-from-the-readme-and-method-docs.md),
      [`../320-child-filed-findings-via-pointing-up/600-the-hook-plane-content-scanners-read-the-working-tree-not-the-staged-index.md`](../320-child-filed-findings-via-pointing-up/600-the-hook-plane-content-scanners-read-the-working-tree-not-the-staged-index.md).
      📝 BRIEF WRITTEN 2026-11-09 by session d4a0fcf3 (Opus 5.5, headless,
      started by coordinating session 74f2b8cd; neither authored this delta):
      `docs/reviews/2026-11-09-0207-merge-hook-staged-scanners-cold.md`, with
      its `.deferred.md` sibling. Pass size: large. Review NOT run: this pass
      waits for a criterion-passing cold Fable session and the principal's
      explicit permission for Fable work. Neither named session may run it.
      🔒 CLAIMED 2026-11-15T19:37Z UTC for the cold pass, in Mike's weekly Fable drain
      (his `/fable-drain` order, 2026-11-16 06:53 NZDT; approval lapses at the
      reset, 2026-11-15 23:00 UTC). Orchestrator: a headless Opus 5.5 session
      started by drain session 21a271a5, a rule-4 off-tier orchestrator that
      holds the context partition, forms no finding and writes no severity.
      Reviewer: Fable 5.1, tier checked at selection, spawned by that
      orchestrator. Neither is a barred session (d4a0fcf3, 74f2b8cd,
      4c65083c and what it started). The sibling is held out of the worktree
      until act 1 is committed. The item's "waits for the principal's explicit
      permission for Fable work" is met by that drain order.
