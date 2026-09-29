- [ ] 🎯 **Talk first — the channel as a session's first preference, with git
      and the concurrency rules behind it — Mike commissioned, 2026-09-29.**
      His words: *"The first preference should be for any claude session to
      communicate directly with another rather than rely on git, concurrency
      rules etc... Talking to each other allows them to understand the
      situation properly and negoitate a way forward"*.
  - [ ] 🔑 **What this changes: the order, not the parts.** `CONCURRENCY.md`
        today leads with the git-shaped mechanisms (worktree, claim line,
        rebase) and adds § *The channel* as the thing that catches what they
        cannot. The ask inverts the order of reach: a session that meets
        another session's work — a dirty tree, a `[~]` claim, a branch it does
        not recognise, a held host — **asks the owner first** and falls back to
        the rules only when no one answers.
  - [ ] 🔎 **The means already exists and crosses repos today.** Measured at
        filing: the harness's peer listing showed seven live peers from this
        atelier session — sessions in five other repos plus two opened outside
        any repo — each addressable by name. So talk-first is not blocked on
        new machinery, and it reaches exactly the cross-repo case `360/020`
        says has no shared view.
  - [ ] ⚖️ **The tension to resolve, not to paper over.** Law 1 of § *The
        channel* says *message is awareness; artefact is authority* — a
        negotiated agreement reserves nothing until it is written down. Read
        together with Mike's ask, the likely reconciliation is: **talk to
        decide, write to hold** — the conversation reaches the agreement, the
        artefact (claim, commit, record) is what makes it survive either
        session's death. But that is this item's reading, not a ruling, and
        the cost clause (§ *Re-run, don't reason* — two of four recorded rounds
        existed only to correct the earlier two) still applies to a negotiation.
  - [ ] 🤔 **Open questions for the design pass:** what a session does when
        the owner is idle, gone, or a closed session whose claim outlived it
        (§ *Surviving an interrupted session* then governs); whether
        talk-first binds the onramp read order (`CLAUDE.md` step 1 — *"assume
        another session may be live"* — becomes *ask who is*); and whether the
        floor clause `020` is carrying to the children needs the same
        re-ordering.
  - [ ] 📎 **Related, not duplicated:** `360/020` (cross-repo awareness —
        this item is its cheapest first answer), `360/010` (naming what you
        launch — talk-first needs an owner to ask), `280/040` (the channel can
        contaminate review independence — talk-first must not reach a cold
        reviewer).
