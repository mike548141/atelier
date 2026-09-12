- [ ] **The mechanisable form of it:** any claim about *current state* comes
      from a fresh read, never from context. `RECORD.md` already says this for
      one case — the all-clear is the pushed floor run, not the local scan —
      and the general rule is the same shape. A close-out that is mechanical
      rather than narrative is the concrete change.
  - [ ] 🎯 **Mike's own close-out checklist, verbatim (2026-09-12), as the
        acceptance shape for the tool this item wants:** *"maybe we make some
        code that every session uses when I ask it to close out the session.
        Giving me standard outputs like transcript ID etc. but also check for
        what I mean by leaving things clean and tidy e.g. worktrees closed up;
        branches and PR's merged; docs updated like session log, roadmap etc;
        no work arounds when issues come up like contention on commits;
        defects/learnings/evidence/assumptions recorded"* — plus, stated
        separately: he often specifies close-out checks in past turn/mid-turn
        prompts (e.g. are questions and decisions recorded) that a mechanical
        tool should be reading for, not relying on him to repeat each time.
        Each named check already has doctrine behind it (`RECORD.md` § the
        close declaration, `CONCURRENCY.md` worktree/claim rules,
        `EVIDENCE.md`) — the gap this item names is that nothing *runs* the
        checklist; a session currently narrates compliance rather than
        proving it from a fresh read.
  - [ ] 🤔 **A related, separate idea from the same message, filed here rather
        than as its own item because it is about the SAME mechanism, not a
        new one:** *"I think we should be using models like sonnet and haiku
        more - maybe as an orchestrator? ... Could be as subagents, for doing
        standard tasks like roadmap management, session logs, interacting
        with me etc."* `ECONOMICS.md` § *One doctrine, tiered authority*
        already assigns mechanical fan-out work below the workhorse tier —
        this narrows that general rule to a concrete candidate: whatever tool
        answers the bullet above (session close-out, roadmap bookkeeping,
        session-log writing) is a plausible first thing to run on a cheaper
        tier rather than the principal session itself. Not scoped further
        here — which tier, and whether "interacting with me" belongs on a
        cheaper tier at all, is a design call this item's build should make,
        not a conclusion reached in the filing.
