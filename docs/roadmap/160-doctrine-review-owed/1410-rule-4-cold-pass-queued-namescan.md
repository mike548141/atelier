- [ ] 🎯 **Rule-4 cold pass queued: `namescan`, private names in branch names and commit titles, warn-first (`160/360` NP2, `320/810`).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/namescan.py`, `tools/test_namescan.py`, its registry entry in `tools/floor.py` — the commit that adds it, on `main`.
      *Questions worth the pass's time:* whether its name sources can leak through the check itself; whether a private repo's own name in its own history is correctly out of scope.
      *Intent record:* `160/360`, `320/810`.
      📝 BRIEF WRITTEN 2026-11-14 by session 51ccf0f9 (Opus 5.5), a headless
      brief-writer started by an estate health sweep, orchestrator session
      58027096: `docs/reviews/2026-11-14-0239-namescan-private-names-branches-titles-cold.md`,
      with its `.deferred.md` sibling. Neither session may run the pass. Review NOT
      run. The pass waits for a criterion-passing cold Fable session and the
      principal's explicit permission for Fable work.
      ✅ PASS RAN 2026-11-15 UTC in Mike's weekly Fable drain: a Fable 5.1
      reviewer, spawned by a headless Opus 5.5 orchestrator started by drain
      session 21a271a5 (off-tier, held the partition, formed no finding).
      Verdict **FAIL**, 14 findings: 2 MAJOR (NS1, NS2) · 4 MODERATE (NS3–NS6)
      · 4 minor (NS7–NS10) · 4 note (NS11–NS14, two formed at reconcile).
      Verdict, reconcile and folded sibling:
      `docs/reviews/2026-11-14-0239-namescan-private-names-branches-titles-cold.md`.
      *Standing MAJORs, both bearing on the 2027-05-03 flip:* NS1, the match
      cannot see a listed name in the shapes a branch name takes (`_`, digits,
      case changes, multi-word terms); NS2, pull-request titles, refs named at
      push and rebase or cherry-pick replays are read nowhere the term list
      lives, and the claim sites do not say so.
      🎯 *Owed to Mike (rule 3: the author applies nothing; every finding is
      his to rule).* Plainly: this check is meant to stop a private repo's or
      client's name showing up in a public repo's branch names or commit
      titles, and on 2027-05-03 it starts blocking commits by itself. The
      review found it misses the commonest branch-name spellings and never
      looks at pull-request titles, while its wording suggests full cover.
      Options: (a) fix NS1 and state NS2's gaps before the flip date, keeping
      the date; (b) hold the flip until NS1 and NS2 are fixed; (c) let it flip
      as built. Recommendation (the reviewer's counsel): (a), with NS3–NS10 as
      one follow-up batch. Nothing is applied until he rules.
      *Routing:* fixes are atelier tool work (`tools/namescan.py`,
      `tools/commitmsg.py`, `PROPAGATION.md` NS10); NS6 (two forge-public
      children undeclared) is a floor scope-key item; NS7 and NS8 touch
      shared helpers that `quotescan` inherits.
