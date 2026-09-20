- [ ] 🔎 **Parallel workers in one run share a scratchpad path, and one
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
