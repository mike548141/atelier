- [ ] 🎯 **Rule-4 cold pass queued: git resolves a staged scan's positional
      scope, and an unknown one is refused (`160/950`, QS1 applied).** The
      staged-positional reader every staged guard shares now asks git what a
      scope names. The authoring session (a principal-opened Opus 5.5 queue
      run, session 722ac2e2, 2026-11-09, in its ruling round, which
      dispatched the Sonnet worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/report.py` (`resolve_staged_scope`),
      `tools/secretscan.py`, `tools/leakscan.py`, `tools/conflictscan.py`,
      `tools/floor.py` (comments), their tests and the five other scanners'
      scope tests, `tools/test_pins.py`, `tools/README.md`, `CHANGELOG.md` —
      the commit that applies `160/950`'s QS1, on `main`, 2026-11-09.
      *Questions worth the pass's time:* whether any spelling still lets a
      staged secret past (symlinks, submodules, a scope naming a removed
      directory); whether refusing an unknown scope can strand a child.
      *Intent record:*
      [`950-rule-4-cold-pass-queued-staged-positional-reader.md`](950-rule-4-cold-pass-queued-staged-positional-reader.md).
      📝 BRIEF WRITTEN 2026-11-09 by session 84e3aa7f (Opus 5.5), a headless
      brief-writer started by coordinating session 74f2b8cd:
      `docs/reviews/2026-11-09-0126-git-resolved-staged-scope-cold.md`, with
      its `.deferred.md` sibling. Neither session may run the pass. Review NOT
      run. The pass waits for a criterion-passing cold Fable session and the
      principal's explicit permission for Fable work.
      🔒 CLAIMED 2026-11-15T21:50Z UTC for the cold pass, in Mike's weekly Fable drain (his
      `/fable-drain` order, 2026-11-16 06:53 NZDT; approval lapses at the reset,
      2026-11-15 23:00 UTC). Orchestrator: headless Opus 5.5 session 12fb7359,
      started by drain session 21a271a5, a rule-4 off-tier orchestrator that holds
      the context partition, forms no finding and writes no severity. Reviewer:
      Fable 5.1, tier checked at selection, spawned by that orchestrator. Neither
      is a barred session (722ac2e2 and what it started, 84e3aa7f, 74f2b8cd). The
      sibling is held out of the worktree until act 1 is committed. The item's
      "waits for the principal's explicit permission for Fable work" is met by
      that drain order.
      ✅ PASS RAN 2026-11-15 UTC (Fable 5.1, both acts; act 1 `aa68389e`):
      **PASS-WITH-FINDINGS** — 0 MAJOR, 2 MODERATE, 3 minor, 4 notes; unchanged at
      reconcile. No standing MAJOR. Verdict, folded sibling and review log in
      `docs/reviews/2026-11-09-0126-git-resolved-staged-scope-cold.md`.
      🎯 Mike's to rule (rule 3): **GS1** (MODERATE) — the README says eight staged
      scanners refuse a `--root` for another repo; only three do, so five read "clean"
      over the wrong index on a hand run. Same code defect as `998`'s HS2. Recommended:
      rule once with HS2; add the one-line `refuse_other_repo` call to the five.
      **GS2** (MODERATE) — CHANGELOG and `report.py`'s docstring say no declared scope is
      turned away; a declared directory with no tracked file is refused at the hook, as
      his "Keep it" answer accepted. Recommended: correct the three surfaces to the
      ruling. **GS3** (minor) — the refusal text calls that case a spelling fault and names
      no config file; recommended: one clause, and the floor naming `.atelier-floor.json`.
      **GS4** (minor) — `GIT_DIR` moves both sides of the other-repo check; recommended:
      reword the docstring and README. **GS5** (minor) — the child `CONTRIBUTING.md`
      template is silent on the spelling rule; recommended: add one clause. GS6–GS9 are
      notes (accept as residuals, or as counselled). Routing: atelier `tools/` and
      `docs/build/templates/` work; children pick it up at their next floor run.
