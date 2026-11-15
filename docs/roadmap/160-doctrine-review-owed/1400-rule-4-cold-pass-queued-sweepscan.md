- [ ] 🎯 **Rule-4 cold pass queued: `sweepscan`, commits name their files, warn-only with no date (`320/060`).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/sweepscan.py`, `tools/test_sweepscan.py`, its registry entry in `tools/floor.py` — the commit that adds it, on `main`.
      *Questions worth the pass's time:* whether `GIT_INDEX_FILE` is a reliable signal on every commit path; whether the marker can be set and forgotten.
      *Intent record:* `320/060`, `320/810`.
      📝 BRIEF WRITTEN 2026-11-14 by a headless Opus 5.5 brief-writer (session b769469b,
      started by an estate health sweep, orchestrator session 58027096; neither authored this
      delta): `docs/reviews/2026-11-14-0246-sweepscan-commit-names-files-cold.md`, with its
      `.deferred.md` sibling. The delta is one commit, `f9def52d`; `tools/sweepscan.py` and its
      tests are unchanged at HEAD, and the registry entry has gained a `declares=` block since.
      The transcript measurement and the fleet probe are NOT RUN unless the spawning session
      grants read-only access. Pass size: small. Review NOT run: it waits for a
      criterion-passing cold Fable session and the principal's explicit permission for Fable
      work. Neither named session may run it.
      🔒 CLAIMED 2026-11-15T19:39Z UTC for the cold pass, in Mike's weekly Fable drain
      (his `/fable-drain` order, 2026-11-16 06:53 NZDT; approval lapses at the
      reset, 2026-11-15 23:00 UTC). Orchestrator: a headless Opus 5.5 session
      started by drain session 21a271a5, a rule-4 off-tier orchestrator that
      holds the context partition, forms no finding and writes no severity.
      Reviewer: Fable 5.1, tier checked at selection, spawned by that
      orchestrator. Neither is a barred session (b769469b, 58027096, d0ca5d24
      and what it started). The sibling is held out of the worktree until act 1
      is committed. The orchestrator grants the brief's two conditional reads,
      read-only and reported as counts and exit codes only, naming no child.
      The item's "waits for the principal's explicit permission for Fable
      work" is met by that drain order.
      ✅ PASS RAN 2026-11-15 UTC (Fable 5.1 reviewer, both acts; sibling folded into
      `docs/reviews/2026-11-14-0246-sweepscan-commit-names-files-cold.md`). Verdict
      **FAIL**: 1 MAJOR (SV1), 3 MODERATE (SV2, SV3, SV4), 2 minor (SV5, SV6), 8 notes;
      no finding formed at reconcile. The signal itself holds: the index-file form table
      reproduced on every commit form, in the main checkout and a linked worktree, and the
      floor wiring, the `plan()` change and the broken-scan exit all confirmed.
      🛑 Standing MAJOR, SV1: the "replaying" exemption reads `REBASE_HEAD`, which git leaves
      behind after a hand-resolved rebase finishes, so every later ordinary commit prints a
      clean "replaying" line and the check is silently off for good in that checkout. No
      checkout read on the day had such a stale ref, so nothing is silenced today.
      🎯 Owed to Mike (rule 3: all six are findings on self-authored guard code; none is
      applied by the building session). Plain ask, recommendation first:
      (1) Approve fixing SV1 (test the rebase state folder instead of the ref, plus a
      conflict, continue, fresh-commit test), SV2 (a clean `merge --no-ff` warns when the
      code says it is exempt), SV5 and SV6 as one queued build item. Recommended: yes.
      (2) SV3: the marker `ATELIER_WHOLE_INDEX` is named in no doctrine, skill or template and
      nothing records its use. Options: write when it is legitimate into the concurrency
      doctrine and count its use in the hook summary, or leave it undocumented. Recommended:
      write it down and count it.
      (3) SV4: the check fires in any repo with more than one worktree, including commits
      whose index no other worktree can touch, so the "fires on most commits, so no
      blocking date" grounding measures a wider set than the risk. His earlier pick of
      "warn, measure first" (2026-11-12 UTC) was made without SV1, SV2 or this point in
      front of him. Options: narrow the trigger to the shared-index case and re-measure
      before any date, or keep the current scope. Recommended: narrow and re-measure,
      re-briefing him when the owed yield count lands.
      Routing: the fixes are atelier build work for a fresh session (not the authoring queue
      run d0ca5d24); a re-pass triggers when they land.
