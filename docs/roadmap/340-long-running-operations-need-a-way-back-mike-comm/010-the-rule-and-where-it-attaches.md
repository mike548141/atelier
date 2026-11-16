- [ ] **Name the rule, and attach it to the undo principle rather than beside
      it.** The house already says *do not do what you cannot undo*. The extension:
      **an operation long enough to be interrupted needs a defined behaviour for
      being interrupted** — before it is started, not after it fails.
  - [ ] **Three questions, and they are answerable in advance for any long
        operation.** Proposed as the shape of the rule:
    - [ ] **Does it survive the operator going away?** Detached, supervised, or
          restartable — a foreground process over an SSH connection is none of
          those. ⚠️ **Check what the host actually offers rather than assuming**;
          the surfacing case found `tmux` present, `screen` absent, and
          `systemd-run` present but outside the agent's own grant — so the right
          answer differed by *who was driving*.
    - [ ] **Can it resume without redoing the work?** And, more sharply: **can an
          interruption leave something that looks finished but is not?** Resumption
          is an efficiency question; that second half is a correctness one.
    - [ ] **How is completion PROVEN, not assumed?** A verification pass that runs
          whether or not the operation reported success — because the interesting
          case is the one where it reported nothing at all.
  - [ ] 🔑 **The generalisation worth keeping, because the next instance will not be
        a file copy.** The same shape covers a long migration, a bulk API job, a
        multi-hour build, a batch of writes to a third party, and any agent loop
        that runs longer than the session that started it. **The question is not
        "is this reversible" but "what does half of this look like, and would I be
        able to tell?"**
  - [ ] ⚠️ **Do not turn this into a checklist that fires on everything.** Most
        operations are short and their interruption is obvious and harmless. The
        rule should attach to a *threshold* — plausibly "longer than a session, or
        touching data whose loss is not recoverable from elsewhere" — and the
        threshold is the part to get right, because a rule that applies to every
        command is one people learn to skip.
  - [ ] **Where it lives.** It extends an existing principle rather than opening a
        new one, so it belongs with the undo rule, not in a new section. One
        paragraph, with the three questions as its body.
      - 🔀 Tidied 2026-11-16 (C0554, verified high; Mike approved 2026-11-16):
        not an ask of Mike. He commissioned the long-running-operations rule
        (the section's title); naming it and attaching it to the undo principle
        (line 1) is agent work. Nothing above was changed; the original text is
        as it was. To revert: delete this line (its commit is listed in
        `docs/sessions/2026-11-16-0534-asks-tidy-applied.md`).
      - 🔀 2026-11-16 (C0554): removed the 🎯 marker from this item's first line,
        because this ask is not Mike's (tidy line above). Original: that line
        began `- [ ] 🎯`. To revert: git revert this repo's marker commit (listed
        in `docs/sessions/2026-11-16-0534-asks-tidy-applied.md`).
