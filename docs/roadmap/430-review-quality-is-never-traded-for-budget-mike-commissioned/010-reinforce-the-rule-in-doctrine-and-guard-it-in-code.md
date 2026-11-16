- [ ] **Reinforce in doctrine that a review is never cut down to fit a
      budget, and guard it in code where a guard can reach**
      `[M][doctrine][code]`. Mike commissioned this, 2026-10-04. Verbatim:

      > I don't think the following point is well understood as several
      > sessions are offering to decay brief and review work to save money.
      > Add a job to the board to reinforce the following point in the
      > doctrine and make it policy as code if we can find a way to do so
      > e.g. how to write a brief and the review process in macro and micro
      >
      > My point:
      > "Remember that review work / sessions are never allowed to down grade
      > the integrity or quality of the review process to meet a budget.
      > Quality is more important than cost.
      > If we run out of budget then we will resume the work when the budget
      > replenishes"

      **The filing session's reading, beneath his words and not a
      substitute for them.** Budget may decide how many reviews run and
      when. It never decides how a review is run. When the allowance runs
      out, the work pauses and resumes after it replenishes.
      **Evidence, one instance measured.** The session that filed this
      offered him, in a structured ask on 2026-10-04, an option to share
      one reviewer across several small queued passes "for roughly 15–25%
      of a week" in place of one reviewer per pass. He did not take it and
      then stated the rule. He reports several sessions doing the same; the
      filing session has seen only its own, so the count across sessions is
      unmeasured.
      **What the house says today, and where it pulls the other way.**
      - `ECONOMICS.md` § the self-check: the cap never moves work
        down-tier, and at the cap the choice is delay or pay. That covers
        the reviewer's tier. It does not cover a review's shape, depth or
        brief.
      - `ECONOMICS.md` § *Match the ceremony to the risk* calls review
        gates spend, to be applied in proportion to the cost of being
        wrong. A session under a tight allowance can read that as licence
        to thin a review. The two need reconciling: risk sets whether a
        review is owed and of what kind; once owed, budget does not shrink
        it.
      - `REVIEW.md` says how a review runs and has no sentence on budget.
      **Owed, not built:**
      - (a) the doctrine wording and its home, quoting him. Candidates:
        `REVIEW.md` (a rule beside rule 4), `ECONOMICS.md` (both sections
        above), and the review-brief skill, which is where a brief-writer
        is reading at the moment the temptation arises.
      - (b) a definition of the process that may not be decayed, at both
        scales he names. Macro: one fresh reviewer per pass, the named
        tier, the brief-and-sibling split, both phases, every re-run on
        the list. Micro: what a brief must contain. Without a stated
        whole, "downgrade" has nothing to be measured against.
      - (c) policy as code, as far as a guard can reach. Candidates only,
        none chosen: `reviewscan` requiring a brief's fixed parts (the four
        lenses, a re-run list, the deferred-reading bar, spawn provenance
        with the tier); one brief per queue pointer and one verdict per
        brief; a verdict's re-run ledger covering every line of the
        brief's re-run list; a paused pass recorded as paused, never
        closed. What a guard cannot see is an offer made in conversation,
        so that half stays with the wording at the point of use.
      - (d) the resume path: how a pass that stops at the cap is recorded
        and picked up, so pausing is the easy route.
      **Review.** This is doctrine about review written by sessions that
      run reviews, so its wording earns a rule-4 pass before it binds.
      🚫 2026-11-02: a design-pass brief on this item was written and
      WITHDRAWN by Mike the same night, before any pass ran: the line above
      asks only for a pass on the wording once it exists. Kept at
      [withdrawn/2026-11-01-1154-review-never-thinned-for-budget-cold](../../reviews/withdrawn/2026-11-01-1154-review-never-thinned-for-budget-cold.md).
      - 🔀 Tidied 2026-11-16 (C0557, verified high; Mike approved 2026-11-16):
        not an ask of Mike. He commissioned this on 2026-10-04 in his own words
        (lines 3-16); what is owed (line 41 on) is the doctrine wording and its
        guards, agent work. The brief he withdrew (lines 63-66) was for a design
        pass, not a question to him. Nothing above was changed; the original
        text is as it was. To revert: delete this line (its commit is listed in
        `docs/sessions/2026-11-16-0534-asks-tidy-applied.md`).
      - 🔀 2026-11-16 (C0557): removed the 🎯 marker from this item's first line,
        because this ask is not Mike's (tidy line above). Original: that line
        began `- [ ] 🎯`. To revert: git revert this repo's marker commit (listed
        in `docs/sessions/2026-11-16-0534-asks-tidy-applied.md`).
      🔒 CLAIMED 2026-11-16T11:02Z (claimed 2026-11-16-1102, wt: qr-78ca-review) by queue-run
      session 78ca9153 (Opus 5.5, principal-opened).
      🧩 2026-11-16 (queue run 78ca): slice 1 of (a) landed. `docs/method/REVIEW.md`,
      the paragraph *Budget decides how many reviews run and when, never how a
      review is run*, quotes his words and points at `ECONOMICS.md` § *Know the
      marginal cost of the running model* for the tier version instead of
      repeating it. Still owed: `ECONOMICS.md` and the review-brief skill
      wording, (b) the macro and micro definition, (c) the guard in code, (d)
      the resume record, and the rule-4 pass on the wording.
