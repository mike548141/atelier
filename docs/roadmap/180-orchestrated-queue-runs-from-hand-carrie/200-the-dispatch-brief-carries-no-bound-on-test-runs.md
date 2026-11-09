- [ ] 🔎 **The dispatch brief binds scratch, worktree and kills, and says nothing about
      how much of the test suite a worker may run at once.** Queue run d0ca5d24,
      2026-11-09 UTC: four workers, each told to run the full suite as `RECORD.md`'s
      bar asks, drove the machine to a load of 310 on 12 cores within minutes. A peer
      session raised it. Told mid-flight to run only their own test modules under
      `nice`, the run carried on at a load of 10 to 25. **The cost of that fix, also
      measured:** a change to a shared file's contract slipped past module-only runs
      twice (`tools/test_allowmarker.py` pins every scanner importing the shared
      module, and each new scanner's worker did not run it). CI caught the first one
      on `main`; the orchestrator caught the second before landing.
      **Shape to consider:** a `session-open/dispatch-brief.md` line, with its
      grounding row, saying a worker runs the test modules for what it changed, and
      the orchestrator or CI owns the full suite, one at a time. And the list of
      modules that pin shared contracts (`test_allowmarker`, `test_report`,
      `test_templates`, `test_floor`), which a change to a shared file adds to its
      own run. It is doctrine and touches `RECORD.md`'s full-suite bar, so it wants
      care rather than a one-line patch.
