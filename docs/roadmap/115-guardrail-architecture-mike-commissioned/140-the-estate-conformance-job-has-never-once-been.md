- [ ] 🔥 **The scheduled estate conformance job has never once been green — 19
      runs, 19 failures, zero successes.** Verified directly 2026-08-15 against
      the run history, not inferred: every scheduled run from 2026-07-28 to
      2026-08-14 ended `failure`. This is the daily job Mike ruled and paid for
      with a fine-grained token, built to assert the full claim — that every
      repo calls the floor **and** that its floor is green. It has been red
      every day since it was built, and no record acts on it.
      **Why this is the sharpest finding of the commission.** The enumerator
      exists precisely because propagation had been decaying unnoticed, and its
      own doctrine says enumeration is *"cheap to re-run, which is what makes
      them true rather than a one-off audit"*. The enumerator is now decaying
      the same way it was built to prevent, and it is worse than the original
      failure: a job nobody reads is indistinguishable from no job, except that
      it looks like cover.
      **A plausible cause is not a verified one.** The job gates on the full
      claim and several child floors are red, which is sufficient to explain a
      red result but is not confirmation — run conclusions were read, not logs.
      Diagnosing it is the first step, not an assumption to build on.
      **The general shape, which outlives this instance:** a scheduled control
      that fails silently is a guardrail with an inverted sign. It consumes the
      attention budget of a control while providing none of the cover, and it
      suppresses the alarm that its own absence would have raised. Whatever
      else is built from this section, something must make a standing red
      **reach a person** — which is item `100`'s territory, since no
      commit-time or CI-time gate can see a job that is failing elsewhere.
