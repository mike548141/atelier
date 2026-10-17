- [ ] 🔎 **Hand-up: a dispatched worker cannot keep a long check in the foreground, so a dispatch prompt that says "run the gate in the foreground" asks for something the harness will not do** `[S][doctrine]`. Handed up by a private child's orchestrated queue run on 2026-10-17, under `PROPAGATION.md` § *Pointing up*. A suspicion of a missing rule, with two measured instances; no fix proposed. <!-- wrapscan:allow: a state line carries the whole state in one line so the index reads true -->

      **What was measured.** The child's queue run had five worker lanes
      live at once. Its `make check` took 19½ minutes under that load
      (1,171 s, read from the run's own output). The harness's shell tool
      caps a foreground command at 600 s and, past it, moves the command to
      the background by itself. The completion notice then goes to the
      orchestrating session, not the worker. Two of the five workers, each
      briefed in writing to run the gate in the foreground, stopped and
      reported "waiting for the gate" until the orchestrator told them to
      read their own output file. The orchestrator's own gate run hit the
      same cap.

      **Why it may be doctrine, not a local quirk.** `CONCURRENCY.md` §
      *Orchestrated queue runs* already makes the dispatch prompt carry one
      obligation the harness forces (an explicit, unique scratch directory,
      because the harness does not namespace scratch per agent). This looks
      like a second of the same kind: a worker has to be told to poll its
      own long-running output, because nothing will notify it. The child had
      a local note saying "foreground", and it was wrong under load.

      **What the child changed locally** (its own memory, not doctrine): a
      worker brief now says to redirect a long check's output to a file
      ending in an exit-code line, and to poll that file itself if the
      command is moved to the background.

      **Not claimed:** that the 600 s figure is fixed across harness
      versions (it is the tool's stated maximum in this session); or that
      fewer lanes would always keep the gate under it.
