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
      this item's own framing.** Its worker, told in its dispatch prompt *and in
      capitals* to write nothing anywhere, wrote **five** files: one into its
      own session's scratchpad and four into **bare `/tmp`** under generic names
      (`floor_old.txt`, `prop_new.md`) — a namespace with no per-session
      component at all. So it is not a namespace problem and it is not only an
      inheritance problem: **a prohibition does not bind, and the fallback
      escapes the project entirely.** The clause drafted before that arrived ("a
      path unique to itself") would not have described the failure measured.
      🛑 **A wrong attribution was published here for about an hour, and the
      correction is kept rather than swept.** Two files found in the
      per-project scratchpad parent *during* the measurement were attributed to
      that peer — by it, confidently, on three consistent signals: timing one
      minute after a legitimate write of its own, matching content shape (a
      canonical/substituted floor pair), and a plausible actor (a worker that
      had just performed exactly that task). A transcript check the next hour
      falsified it: the files belonged to a **third** session doing the same
      pin-bump verification by nearly the same method at the same time, and the
      peer's own worker had written elsewhere. The first version of this record
      and of the doctrine clause rested on that attribution.
      🔑 **The transferable failure is the one the peer named against itself:**
      three consistent signals and **no disconfirming check**. The settling test
      — grep its own transcript for the filenames — was one command and was
      never run before the claim was asserted. *Agreement is not corroboration
      when neither party has opened the source.* Both sessions agreed; neither
      had looked.
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
      ✅ **Hypothesis killed, on the peer's own check.** The cwd-reversion
      explanation offered for the escapes is **dead for this instance**: every
      one of the five writes used an **absolute** path in a shell that had
      already `cd`'d, so no relative resolution was involved. The clause keeps
      *absolute* as a requirement on the independently-observed cwd hazard, and
      says explicitly that these escapes are not evidence for it. Recording a
      dead hypothesis rather than a plausible one left standing was the
      agreement between the two sessions, and the peer paid it in the direction
      that cost itself. Rule-4 `⏳` at `160/380`; the run may not take it.
