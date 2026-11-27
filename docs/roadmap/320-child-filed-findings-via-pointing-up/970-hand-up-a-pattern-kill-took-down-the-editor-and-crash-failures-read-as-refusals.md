- [ ] 🎯 **Hand-up: a pattern kill took down the editor and every session in it, though `CONCURRENCY.md` already forbids it; and after the crash, sessions read failed prompts as the principal's refusals.** Reported 2026-11-28 by a private child's orchestrating session, class only <!-- wrapscan:allow: a state line carries the whole state in one line so the index reads true -->

      A hand-up from a private child, under `PROPAGATION.md` § *Pointing up*.
      Two findings, one incident. Measured; one instance each.

      **1. The kill rule held as text and failed in use, a second time.**
      `CONCURRENCY.md` § *The machine is shared too* says a kill is scoped by
      the PID the session launched, never by a pattern, *"and the dispatch
      prompt says so"* (from `320/700`). An orchestrator dispatched a
      headless worker whose prompt did not say so. The worker, stopping its
      own test run, tried to scope by user instead and ran
      `pkill -f 'pytest' -U $(id -u)`. macOS's BSD `pkill` stops reading
      options at the first pattern, so `-U` and the uid became two more
      patterns, and with `-f` they matched nearly every process of the
      principal's whose command line holds either. Three seconds later the
      editor's log shows its whole process tree (network and shared
      processes, every extension host, the pty host, every window) exiting
      with code 15. Every interactive session on the box died mid-work
      overnight. Reproduced harmlessly afterwards with `pgrep`: the same
      argument order matched 18 live editor helpers; options first matched
      none. No data was lost (the child checked every worktree and backed up
      the scratch folders).
      **What it shows:** the rule was right; it bound nobody, because the
      dispatcher forgot to name it and the worker's own attempt at scoping hit
      a platform trap the doctrine does not mention. The child has queued a
      session-wide guard (a pre-command hook refusing kill-by-name, among
      other things) on its own board.
      **Asked:** (a) the doctrine names the BSD option-order trap beside the
      rule (options before patterns; `pgrep` only to list, then kill by
      PID); (b) the kill rule joins the shared list of things a worker must
      never do that the fleet prompts carry (`115/540`), so a dispatch cannot
      forget it; (c) whether the house wants the enforcement as a shared hook
      in `tools/` beside the model and secret guards (`020/460`'s policy as
      code), rather than each child building its own.

      **2. After the crash, failed prompts were read as the principal's
      refusals.** The headless and editor-hosted agent processes outlived
      their windows for up to an hour with no route to the principal, who was
      asleep. Every permission prompt and question box in that time failed,
      surfacing as "user doesn't want to take this action", "stop and wait",
      "you declined" or "Stream closed". Four sessions treated these as his
      answers: one stopped work awaiting "your word" on edits he never saw,
      one put a "refusal" on his close list, one stopped a run he had asked
      for, one told him his answers were missing. None was written onto a
      board item as his ruling, by luck rather than rule.
      **Asked:** a doctrine line, likely in `COMMUNICATION.md` or
      `AUTONOMY.md`: a denial or a failed question that arrives while the
      principal is known to be away, or after the host has crashed, is
      *unreached*, not his answer; it is recorded as unreached and put to him
      again, never cited as his refusal.
