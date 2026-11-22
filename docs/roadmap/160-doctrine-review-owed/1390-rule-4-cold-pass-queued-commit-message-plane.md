- [ ] 🎯 **Rule-4 cold pass queued: the commit-message plane: a `commit-msg` hook and `floor.py --plane msg` (`320/810`).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, first of its kind, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `.githooks/commit-msg`, `tools/commit-msg.sample`, `tools/commitmsg.py`, the plane handling and refused flags in `tools/floor.py`, `skills/create-repo/SKILL.md`, `docs/method/GUARDS.md`, `tools/README.md` — the commit that adds the hook, on `main`.
      *Questions worth the pass's time:* whether the fail-closed hook can stop a commit for a reason a user cannot clear; whether a child can pass the boundary through `flags`.
      *Intent record:* `320/810`, `320/550`.
      📝 BRIEF WRITTEN 2026-11-14 by session 3e2239de (Opus 5.5), a headless
      brief-writer started by an estate health sweep, orchestrator session
      58027096: `docs/reviews/2026-11-14-0258-commit-message-plane-cold.md`,
      with its `.deferred.md` sibling. Neither session may run the pass. Review NOT
      run. The pass waits for a criterion-passing cold Fable session and the
      principal's explicit permission for Fable work.
      🔒 2026-11-22T21:07Z: claimed for the Fable pass by a headless per-pass
      orchestrator, session 21422696 (Opus 5.5, rule-4 off-tier orchestrator:
      it holds the partition and forms no finding), started by drain session
      eca14b23; the reviewer is a Fable 5.1 subagent, tier checked at
      selection. Neither is barred by the brief. The approval this item waits
      for is his drain order of 2026-11-23, verbatim: *"Start a fable drain or
      whatever it is called now. Target 100% of weekly budget by 11.30am NZT
      todat"*. The held-back sibling is partitioned out of the review tree
      until act 1 is committed.
      ✅ PASS RAN 2026-11-22 UTC (Fable 5.1 reviewer; orchestrator session 21422696
      for drain session eca14b23; act 1 `74d733a0`). Verdict **FAIL —
      1 MAJOR, 2 MODERATE, 4 minor, 2 notes** (MP1–MP9; MP9 formed at reconcile), in
      `docs/reviews/2026-11-14-0258-commit-message-plane-cold.md`.
      **Standing MAJOR, MP1:** a title or line that starts with the comment character (`#`) is
      read by neither plane, because the reader strips those lines as git's editor cleanup does,
      while `-m`/`-F` commits keep them; such a commit lands unread.
      🎯 **Owed to the principal (rule 3: plane is doctrine by function, the author applies
      nothing).** One bulk ask, recommendation first: *approve fixing MP1–MP9 as the reviewer's
      counsel says, in a fresh build session, then a Fable re-check of MP1–MP3 before the
      2027-05-03 and 2027-05-31 flips (Recommended)*; or rule per finding; or hold. MP1–MP3 bear
      on whether those flips should happen on the plane as built: MP1 (MAJOR, above); MP2
      (MODERATE) a child's `flags: ["--help"]` turns a msg check into a silent exit 0; MP3
      (MODERATE) a child's `scope` with a missing path skips a msg check, exit 0. Minor: MP4
      refusal untested, MP5 hook's `python3` guard lacks pre-commit's remedy, MP6 GUARDS.md omits
      the paths the plane misses, MP7 four mirror sites; notes MP8, MP9.
      Routing: the fixes are atelier build work (`tools/commitmsg.py`, `tools/floor.py`,
      `.githooks/commit-msg`, docs); nothing routes to a child.
