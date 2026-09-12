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
    - [ ] 🔎 **Widened same day into a general model-router question, checked
          against a named source before answering — 2026-09-12.** *"Would we
          be able to create a model router as code that is both effective and
          efficient? So that when I start a session... it will use other
          models as subagents on pieces of work"*, against
          [Anthropic's own model-selection guidance](https://academy.claude.com/tutorials/choosing-the-right-claude-model),
          then: *"Essentially make advice like that link policy as code."*
          **Fetched and read, not assumed.** The page names two decision
          axes — task complexity and rate-limit/cost efficiency — with clean
          task-type→model examples (e.g. "summarizing articles → Haiku") that
          **are** the codable half. It also names an axis that explicitly
          resists coding: "genuinely needs sustained thinking" is its own
          phrase for a judgement call, and its own fallback is *"if you're
          not sure, start with Sonnet [and test]."* So the honest answer to
          "would we be able to" is **half yes** — a static task-type→tier
          table is real policy-as-code; the complexity judgement is not
          mechanisable by this source's own admission.
      - [ ] 🔑 **What closes the other half is already this doc's own
            doctrine, just not run as code.** `ECONOMICS.md` § *One doctrine,
            tiered authority* already states the rule in full — cheapest
            model that genuinely does the work, verifiability as the safety
            test, and *"a smaller model that hits [structural work] logs and
            hands up rather than improvising past its depth"* (§ *Two hard
            edges*, "hand-ups are noisy"). A router built as **table +
            enforced escalation** — not table alone — is what makes cheap
            routing *effective*, since the table only needs to be right on
            average when a wrong guess is caught and bounced up rather than
            silently shipped degraded.
      - [ ] 📎 **The dispatch mechanism already exists; only the policy layer
            is missing.** A subagent launch already takes a `model`
            parameter naming the tier — the gap is that an orchestrating
            session chooses it by inference each time (this doc's whole
            premise: doctrine directive first, enforced second), not that no
            mechanism exists to act on a router's decision.
      - [ ] 🤔 **Not scoped to a build.** Recorded per Mike's own instruction
            the same session not to spend remaining budget building it —
            candidates for whoever picks this up: a lookup table keyed on
            task-type keywords with the escalation clause as a hard
            requirement, not an optional add-on; or a thinner version that
            only auto-fills the model parameter's *default* and leaves an
            explicit override always available. Which, and how the table
            gets validated against drift as Anthropic's own guidance
            changes, is unscoped here.
