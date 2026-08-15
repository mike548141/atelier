- [ ] **What actually reaches a child, measured 2026-08-15 — and it is about
      1% of the doctrine.** The commission asked about outcomes in the children,
      and this is the half the first pass never looked at. Enforcement
      propagation genuinely works: **18 of 18 floors wired**, by call rather
      than copy, exactly as its decision record intended. A registry line added
      here is live estate-wide on the next push, with no child edit. That is the
      one carrier in good health.
      **Everything else propagates badly or not at all.**
      **Pins: 16 of 17 stale**, nine of them roughly five weeks back. The pin
      is pull-based by design — it makes staleness observable, not enforced —
      and almost nobody has pulled.
      **The stamped floor block: 8 children are missing three of its seven
      concerns outright**, and their apex bullet predates two later clauses.
      Unchanged a week after the audit that first measured it. Worse, **only 4
      of 17 children stamp their copy at all**, so the drift-checker built to
      watch exactly this is structurally blind to the other 13.
      **Directive doctrine: about 56 lines reach a child's context at session
      start, against roughly 5,620 lines in `docs/method/`.** Everything else —
      data protection, secrets, guards, evidence, review, economics — is
      reachable only by a pointer someone chooses to follow, from a pin that in
      16 of 17 cases is weeks out of date.
      **The harness plane: nothing.** No child holds hooks, skills or agent
      definitions. And the plugin that carries the skills is **not installed on
      this machine at all**, so the surfaces meant to deliver guardrails into a
      session are delivering none.
      **The consequence, stated plainly:** half the fleet is running a safety
      floor that omits concurrency discipline entirely, and no mechanism will
      tell them. Fixing the pins is a sweep; fixing the *class* means deciding
      whether a stale pin should be able to fail something, which is a doctrine
      question and Mike's.
