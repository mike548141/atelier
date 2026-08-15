- [ ] 🎯 **Build a before-plane — the guardrail class that acts at the moment of
      decision, which is empty in atelier and reaches no child.** Measured
      2026-08-15 across the whole guardrail surface, not just scanners: **21
      mechanisms act after an act** — at commit, at CI, at review, at audit —
      and **5 act before it**. Of those five, four are prose an agent may simply
      not read, with nothing observing that it didn't. The one mechanical
      before-guard in the estate is `worktree.py` refusing to create a worktree
      inside an iCloud path: it makes the wrong thing impossible rather than
      reportable, which is the shape the whole class needs.
      **Why this is the structural answer to the directive-doctrine aim.** The
      policy-as-code section records Mike's aim that doctrine be directive as
      well as enforced, and files its unowned half as *a guard fires after the
      act, on a choice already made*. That half has no carrier because there is
      nowhere for a before-mechanism to live. The harness plane — a hook firing
      at session start, or before a tool call — is the only place a mechanism
      can sit between a decision and the act. atelier has built there exactly
      once, and that build was ruled harmful and unwired.
      **What is empty, verified 2026-08-15:** no agent definitions, no
      plugin-level hooks directory, no distributed permission set. The one
      artefact in the class is a permission allowlist template that is
      deliberately never committed, in atelier or in any child. Nothing in this
      class reaches a child in either direction.
      **The design lesson is already paid for.** The withdrawn reply gate's own
      post-mortem carries it: a hook that fires *after* the output cannot undo
      it. A before-plane build must sit before the act, not after, and that
      distinction is what the one failed attempt bought.
      **Sequencing:** this is item 1 of the four-part shape in the section
      README, and the other three are cheaper. It is queued first because it is
      the only thing that could ever mechanise the two items below.
