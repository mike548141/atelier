- [ ] 🎯 **Rule-4 cold pass queued: `attribscan`, an attribution to the principal carries his words (`320/100`, slice 2 of `320/810`).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, first of its kind, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/attribscan.py`, `tools/test_attribscan.py`, its registry entry in `tools/floor.py`, `tools/README.md` — the commit that adds `tools/attribscan.py`, on `main`.
      *Questions worth the pass's time:* whether a generic use of the word *ruled* will be noise on the flip date; whether a citation that resolves to nothing passes as evidence.
      *Intent record:* `320/100`, `320/810`.
      📝 BRIEF WRITTEN 2026-11-14 by session a18861ae (Opus 5.5), a headless
      brief-writer started by an estate health sweep, orchestrator session
      58027096: `docs/reviews/2026-11-14-0210-attribscan-unquoted-attribution-cold.md`,
      with its `.deferred.md` sibling. Neither session may run the pass. Review NOT
      run. The pass waits for a criterion-passing cold Fable session and the
      principal's explicit permission for Fable work.
      ✅ PASS RAN 2026-11-15 UTC in Mike's weekly Fable drain: a Fable 5.1
      reviewer, spawned by a headless Opus 5.5 orchestrator started by drain
      session 21a271a5 (off-tier, held the partition, formed no finding).
      Verdict **FAIL**, 16 findings: 1 MAJOR (AT1) · 5 MODERATE (AT2–AT6)
      · 6 minor (AT7–AT11, AT15) · 4 note (AT12–AT14, AT16 formed at
      reconcile). Verdict, reconcile and folded sibling:
      `docs/reviews/2026-11-14-0210-attribscan-unquoted-attribution-cold.md`.
      *Standing MAJOR, bearing on the 2027-02-08 flip:* AT1, the grammar and
      evidence test cannot tell supported from unsupported attributions well
      enough to block (about 3 in 27 paraphrased attributions fire, and an
      unrelated quote or board id nearby clears one); the author's own
      measurement under `320/100` reached the same conclusion.
      🎯 *Owed to Mike (rule 3: the author applies nothing; every finding is
      his to rule).* Plainly: this check flags a record that says Mike decided
      something without quoting or citing him, and on 2027-02-08 it starts
      blocking commits by itself in every child. The review found it works as
      a warning but, as built, would block some honest records (long quotes,
      moved or split files) and pass invented ones worded differently; the
      CI cover also has holes (AT4 advisory form reads nothing on CI, AT5 a
      push is judged by its last commit only), and AT6 prints file paths
      unsanitised. Options: (a) keep the date as built; (b) stay warn-only
      and re-date after AT1–AT5 are fixed and cold-reviewed; (c) whole-tree
      report only, no flip. Recommendation (the reviewer's counsel): (b).
      Nothing is applied until he rules.
      *Routing:* fixes are atelier tool work (`tools/attribscan.py`, its
      tests, the floor entry); AT6 is a shared path renderer in
      `tools/report.py` (sweeping `leakscan` too); AT8 repairs `CHANGELOG.md`
      headings; a fix to AT1–AT5 lands with its own cold pass.
