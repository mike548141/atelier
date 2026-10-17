- [x] **`ccmail` sent the operator to `ccmail --auth`, a client-ID setup he
      didn't need, and sessions relayed it.** Filed and fixed 2026-10-17
      from a private child's session, at Mike's direct ask: *"you should be
      running the ccmail command or improving it so it does not ask me for
      things like client ID each time I run it"*. He had been sent through
      it at least twice.
      - **Cause:** with the delegation route configured, a lapsed cloud
        login needs only `gcloud auth login`. But `--status` printed the
        empty keychain route as `❌ … fix: ccmail --auth`. The
        no-route error said the same. And `--auth` began the client-ID flow
        without checking delegation first. Sessions read the two "fix" lines
        as a two-step recipe and handed both over.
      - **Fixed:**
        - With delegation configured, the empty keychain route prints as
          `➖ not set up — not needed`, with no fix offered, and the no-route
          error offers only `gcloud auth login`.
        - Plain `--auth` checks delegation first. If it's live, it says so
          and exits 0. If it has lapsed, it names `gcloud auth login` and
          exits 1. Either way it prompts for nothing.
        - Setting up the fallback beside delegation stays possible, but as a
          deliberate act: `--auth --fallback`. The man page's case for a
          lapse-proof fallback is kept, not removed.
        - Help text and man page updated, plus 4 tests (30 pass).
      - **The lesson, for the house to weigh:** a status line that prints a
        `fix:` for a route the operator doesn't need is an instruction
        sessions will relay. An optional route's absence should print as
        neutral, not as a failure with a fix.
      review: owed. This is an instrument change by a session that also
      filed the item (rule 4).
