- [~] ⏳ **Rule-4 cold pass queued: `nz-phone` passes a bracketed byte field (`320/850`), and `secretscan`'s assigned rule takes both spellings (`320/840`).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/leakscan.py`, `tools/secretscan.py`, their tests, `tools/README.md`, `CHANGELOG.md` — the commit that closes `320/850`, on `main`.
      *Questions worth the pass's time:* whether a real number can pass as a byte field; whether the second spelling can exempt a line it should not.
      *Intent record:* `320/850`, `320/840`.
      📝 BRIEF WRITTEN 2026-11-14 by a headless Opus 5.5 brief-writer (session c8eba849,
      started by an estate health sweep, orchestrator session 58027096; neither authored this
      delta): `docs/reviews/2026-11-14-0229-phone-byte-field-assigned-rule-spelling-cold.md`,
      with its `.deferred.md` sibling. The delta is one commit, `57719bfa`; its two code regions
      are unchanged at HEAD, and the brief asks the pass to judge it as landed and as it stands.
      The 30-checkout fleet probe is NOT RUN unless the spawning session supplies read-only child
      checkouts. Pass size: small. Review NOT run: it waits for a criterion-passing cold Fable
      session and the principal's explicit permission for Fable work. Neither named session may
      run it.
      🔒 CLAIMED 2026-11-15T19:57Z UTC for the cold pass, in Mike's weekly Fable drain
      (his `/fable-drain` order, 2026-11-16 06:53 NZDT; approval lapses at the
      reset, 2026-11-15 23:00 UTC). Orchestrator: a headless Opus 5.5 session
      started by drain session 21a271a5, a rule-4 off-tier orchestrator that
      holds the context partition, forms no finding and writes no severity.
      Reviewer: Fable 5.1, tier checked at selection, spawned by that
      orchestrator. Neither is a barred session (c8eba849, 58027096, d0ca5d24
      and what it started). The sibling is held out of the worktree until act 1
      is committed. The 30-checkout fleet re-run is NOT RUN: no child checkouts
      are supplied. The item's "waits for the principal's explicit permission
      for Fable work" is met by that drain order.
