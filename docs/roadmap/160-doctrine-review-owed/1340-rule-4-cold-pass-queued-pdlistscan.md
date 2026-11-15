- [ ] 🎯 **Rule-4 cold pass queued: `pdlistscan`, personal data in a public repo stands only where the closed list names it (`160/630`, slice 3 of `320/810`).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/pdlistscan.py`, `tools/test_pdlistscan.py`, its registry entry in `tools/floor.py`, `tools/README.md` — the commit that adds `tools/pdlistscan.py`, on `main`.
      *Questions worth the pass's time:* whether a repo with no visibility key is rightly out of scope; whether a listed string in a file its entry does not name can be missed.
      *Intent record:* `160/630`, `320/810`, `260/050`.
      📝 BRIEF WRITTEN 2026-11-14 by session fb2c22e6 (Opus 5.5), a headless
      brief-writer started by an estate health sweep, orchestrator session
      58027096: `docs/reviews/2026-11-14-0238-pdlistscan-closed-list-cold.md`,
      with its `.deferred.md` sibling. Neither session may run the pass. Review NOT
      run. The pass waits for a criterion-passing cold Fable session and the
      principal's explicit permission for Fable work.
      🔒 CLAIMED 2026-11-15T19:53Z UTC for the cold pass, in Mike's weekly Fable drain
      (his `/fable-drain` order, 2026-11-16 06:53 NZDT; approval lapses at the
      reset, 2026-11-15 23:00 UTC). Orchestrator: a headless Opus 5.5 session
      started by drain session 21a271a5, a rule-4 off-tier orchestrator that
      holds the context partition, forms no finding and writes no severity.
      Reviewer: Fable 5.1, tier checked at selection, spawned by that
      orchestrator. Neither is a barred session (fb2c22e6, 58027096, d0ca5d24
      and what it started). The sibling is held out of the worktree until act 1
      is committed. The fleet probe over local child checkouts is read-only and
      reported by count and exit code only, naming no child. The item's "waits
      for the principal's explicit permission for Fable work" is met by that
      drain order.
      ✅ PASS RAN 2026-11-15 UTC (Fable 5.1 reviewer, both acts; sibling folded into
      `docs/reviews/2026-11-14-0238-pdlistscan-closed-list-cold.md`). Verdict **FAIL**:
      2 MAJOR (PN1, PN2), 4 MODERATE (PN3 to PN6), 4 minor (PN7, PN8, PN9, PN13), 4 notes
      (PN10, PN11, PN12, PN14); PN13 and PN14 formed at reconcile. Probes, re-runs and the
      fleet probe are in the verdict; the fleet is reported by count only.
      🛑 Standing MAJORs. PN1: a public repo that declares no visibility is out of scope and
      the floor's cross-check only goes partial, never red, so such a repo is unguarded; two
      public children were in that state on the day. PN2: a list written in any shape but
      atelier's exact grammar parses to zero entries and the run reports clean.
      🎯 Owed to Mike (rule 3: every finding is on self-authored guard code; none is applied
      by the building session). Plain ask, recommendation first:
      (1) PN1, how a repo comes into scope. Options: keep the declared visibility as the only
      key and make "nothing declared but GitHub says public" red in the floor; or let CI use
      GitHub's own answer, keeping the declaration for the offline hook. Recommended: both,
      ruled with the overlapping queued pass `160/1180` in view.
      (2) PN2: approve that an unreadable or empty list fails loud (a broken scan, not a clean
      one) and that children get a list template. Recommended: yes.
      (3) PN4: the standard says a repo with no list holds no exceptions; the scanner makes a
      missing list a blocking finding. Which rule stands? Recommended: decide one and sweep the
      standard, the child template and the scanner to match before the 2027-03-08 flip.
      (4) Approve PN3, PN5, PN6, PN7, PN8, PN9 and PN13 as one queued build item (narrow the
      exemption, refresh the stale fleet record and board a dated probe before the flip, read
      markers through leakscan's grammar, the minors). Recommended: yes. PN10, PN11 are
      floor-wide and go on the board against their class; PN12, PN14 are notes.
      Routing: the fixes are atelier build work for a fresh session (not the authoring queue
      run d0ca5d24); a re-pass triggers when they land.
