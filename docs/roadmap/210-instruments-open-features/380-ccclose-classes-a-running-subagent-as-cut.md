- [~] (claimed 2026-11-09-1242, wt: atelier-qr-d0ca-instr, session d0ca5d24) 🔎 **`ccclose` classes a subagent that is still running as "cut
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
