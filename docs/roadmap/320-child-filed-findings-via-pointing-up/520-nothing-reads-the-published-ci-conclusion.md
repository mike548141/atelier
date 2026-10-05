- [ ] 🔎 **Hand-up: nothing at session open, or before "verified", reads the
      repo's published CI conclusion** `[S][doctrine][tools]`. Handed up by a
      child's queue run on 2026-10-05 over the cross-session channel, under
      `PROPAGATION.md` § *Pointing up*. **Evidence, as the child reported
      it:** the child's GitHub CI was red for about four weeks, across dozens
      of pushes and several orchestrated runs, and no session noticed. It
      was found only because a worker went looking (`gh run list`,
      `gh run view --log-failed`). There were two stacked causes. A type-check
      step failed, which masked a test failure behind it. That test failure
      came from a CLI library forcing terminal output when `GITHUB_ACTIONS`
      is set, so local suites were always green: the class in memory as
      env-gated test failures. The floor hook runs no type-check, and nothing
      at session open reads CI state. So "suites green locally, floor green"
      read as healthy while the published gate was red. The child has fixed
      both causes and carries its own record.
      **The gap:** no house rule says a session reads the repo's CI
      conclusion at open, or before it declares work verified. The
      session-open steps cover git and pin drift only. The child named two
      possible shapes and evidenced neither: a session-open `gh run list`
      check in the child block, or a floor advisory that reports the last CI
      conclusion for HEAD's parent. atelier's own close discipline already
      reads the pushed floor run (memory: *the all-clear is the pushed floor
      run*), so the rule exists in practice here and is missing from the
      shared doctrine. Whether it becomes doctrine, and in which shape, is
      for the ruling round.
