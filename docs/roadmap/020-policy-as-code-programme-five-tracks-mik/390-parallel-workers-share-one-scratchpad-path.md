- [x] 🔎 **Parallel workers in one run share a scratchpad path, and one
      silently overwrote another's script mid-measurement** — reported by a
      `020/380` worker 2026-09-20, from its own experience, while three
      workers probed memory in parallel.
      **What happened:** the worker wrote a probe script under the session
      scratchpad, a peer worker wrote its own script to the same path, and
      the first worker's later invocations **ran the peer's script instead of
      its own** without any error. It noticed, moved to a private path under
      its own temp directory, and re-ran everything — so nothing measured in
      that batch rests on the collision.
      **Why it is worth an item rather than a shrug.** The harm here was nil
      because both scripts were measurement-only and the worker caught it.
      The same collision on a *write* script is a worker committing another
      worker's work, and the failure is silent by construction: a path that
      exists and runs looks identical to your own. The run pattern
      (`CONCURRENCY.md` § *Orchestrated queue runs*, *Waves*) explicitly
      sanctions concurrent workers, and gives each its own **git worktree** —
      the isolation stops at the repo boundary and does not extend to the
      scratchpad they all reach.
      **Owed:** establish what is actually shared (measure it — the harness's
      scratchpad path per subagent, not an assumption), then either give each
      worker a path of its own or say in the dispatch doctrine that a worker
      writes scratch files only under a path it has made unique to itself.
      Cheap either way; the value is that the next collision is not silent.
      ---
      ✅ **MEASURED AND CLOSED 2026-09-20.** The measurement the item asked for
      ran against a live run's three concurrent workers rather than an
      assumption: subagent workers get **no scratch directory of their own** —
      all three wrote into the orchestrating session's single scratchpad,
      unnamespaced, beside the orchestrator's own files.
      🔑 **A peer session in a child volunteered the instance that falsified
      this item's own framing.** Its worker wrote three files one minute apart —
      the first into its own session's scratchpad, the next two into the
      **shared parent directory every project's scratchpad hangs off**. So it is
      not a namespace problem: a worker does not reliably inherit its parent's
      scratchpad, and the within-run and cross-project cases are one mechanism
      at two radii. The clause drafted before that arrived ("a path unique to
      itself") would not have described the failure actually measured.
      *Corroboration found by accident and worth more than the probe:* the same
      shared directory holds `msg`/`msgB`/`msgD`/`msgE`, one earlier atelier
      sitting's commit messages — a session hand-disambiguating inside a shared
      namespace, which is what people do when the namespace will not do it for
      them.
      **Delivered:** `docs/method/CONCURRENCY.md` § *Orchestrated queue runs*,
      the paragraph after *What a worker inherits is bounded* — a dispatch
      prompt requires each worker to write scratch under a path both
      **absolute** and **unique** to it, absolute because a relative write after
      a `cd` resolves against whatever the shell's cwd has become. Written as a
      prompt obligation, not a mechanism, because the scratch path is the
      harness's to allocate; the clause names its own expiry.
      ⚠️ **Deliberately not established:** *why* the two files escaped. A cwd
      that moved between writes fits the evidence and is not evidence. The
      hypothesis went to the peer, which holds the only transcript that can
      settle it. Rule-4 `⏳` at `160/380`; the run may not take it.
