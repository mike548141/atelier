- [x] 🔎 **`ccclose` classes a subagent that is still running as "cut
      mid-flight".** Found by the `160/900` cold pass (QK12) and filed by
      queue run 722ac2e2 on 2026-11-09 when it applied that pass. A close
      check that reads a live agent as cut tells the session the agent is
      dead when it is not, so a teardown can go ahead under a running worker
      (the hazard `CONCURRENCY.md` § *Orchestrated queue runs* guards against
      with its three-leg teardown rule). **Shape:** tell *still running* from
      *cut* (a running agent has no terminal notice yet and its transcript is
      still growing), and print it as its own state rather than either
      *reported* or *cut*. Evidence and the reviewer's wording:
      `docs/reviews/2026-10-18-0517-queue-run-carries-the-brief-cold.md`,
      QK12.
      - **DONE 2026-11-09** (queue run d0ca5d24): `instruments/ccclose` has a
        fourth agent state, *still running*: no end recorded, the agent's last
        record under `FRESH_MS` (ten minutes) old by the clock, and no parent
        record more than ten minutes after it. The bound is measured, not
        invented: of 881,904 gaps between consecutive records in 3,587 real
        agent logs, 99% are 83 s or less and 99.9% are 600 s or less, which is
        also the longest one foreground command may run. A dead agent reads as
        running for that long and the line says how long ago it last wrote.
        Running fails the check, like cut, since a close under a working agent
        is the hazard, but no longer calls a live agent dead. Resumed agents
        are judged the same way. The summary line, `--json` counts, the
        identifiers block, `instruments/ccclose.design.md` and
        `instruments/man/ccclose.1` carry it; pinned in
        `instruments/ccclose.test.js`. A real run on the queue run's own
        session read its four live agents as running and its four finished
        ones as reported.
