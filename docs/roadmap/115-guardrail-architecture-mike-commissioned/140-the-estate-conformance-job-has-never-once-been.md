- [x] 🔥 **The scheduled estate conformance job has never once been green — 19
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

      ✅ **Diagnosed 2026-10-05, from the logs this time, not the run
      conclusions** (queue run, Opus 5.5). The job is not broken. It is
      reporting real reds correctly. The last 60 scheduled runs all ended
      `failure`. The latest (2026-10-04) read every enrolled repo with **0
      unreadable**, and found every repo wired with a current shim. The
      failure comes from three children whose own floors are red on their
      default branch, each on a **blocking secretscan finding of its own**.
      One of the three has not run its floor since 2026-09-03. So the
      plausible cause in the text above is now the verified one, and the job
      is doing the job it was built for.

      What remains is not this item's. Clearing each child's red is that
      child's work, in its own session; the per-repo detail belongs in the
      private estate root, not in this public record. Making a standing red
      **reach a person** is `100`'s territory, as this item already said, and
      `100` awaits Mike. Reported to Mike in this run's close.
