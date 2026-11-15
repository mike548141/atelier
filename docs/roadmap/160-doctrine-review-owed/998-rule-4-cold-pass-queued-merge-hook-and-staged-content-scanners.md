- [ ] 🎯 **Rule-4 cold pass queued: the `pre-merge-commit` hook, the repo-local
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
      ✅ PASS RAN 2026-11-15 UTC (acts 1 and 2, Fable 5.1 reviewer; orchestrator as
      claimed, formed no finding): **PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE
      · 3 minor · 4 notes**, verdict and reconcile in the brief, act 1 committed
      `8df76523` before the sibling opened; sibling folded in and removed.
      No MAJOR stands; the hook plane's live behaviour held end to end.
      🎯 The principal's to rule (rule 3, nothing applied): **HS1** MODERATE,
      the `GUARDS.md` "measured on git 2.50.1" table is wrong for
      `cherry-pick --continue` and `rebase -i` reword and omits
      `merge --ff`/`pull`/`am`; **HS2** MODERATE, the five `--staged` readers
      skip `refuse_other_repo` and pass clean over another repo's index by
      hand; **HS3** MODERATE, `staged_paths` lacks the `160/800` pins, so
      `reviewscan --staged` from a subdirectory under `diff.relative` passes a
      record with no review line; **HS4** minor, ignore files read from disk
      in staged mode; **HS5** minor, four mutations leave the tests green;
      **HS6** minor, a stale `filewalk.py` sentence. HS7–HS10 notes.
      The reviewer's counsel per finding is in the brief's follow-up list.
      Routing: on approval, one fix item for HS2, HS3, HS5 and HS6 (code and
      tests) and HS1, HS4 (doctrine text); a change to `GUARDS.md` is
      doctrine, so it earns its own rule-4 pass. At reconcile
      HS2 and HS3 were re-attributed to the later `160/950` and `160/800`
      sweeps missing these five readers, not to this delta's author.
