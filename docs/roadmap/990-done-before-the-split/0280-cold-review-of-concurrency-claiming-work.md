- [x] **Cold review of CONCURRENCY "Claiming work"** — RAN 2026-07-13, un-briefed
      (reviewer chose its own attack surface): **PASS-WITH-FINDINGS**, verdict +
      decision in `reviews/2026-07-13-concurrency-claiming-work.md`. Core
      mechanism live-verified sound; **1 MAJOR · 4 MEDIUM · 2 LOW**. Mike ruled
      **all seven [fixed]**, applied same day. The MAJOR was real: the section
      gated claiming to worktree-mode, whose only reliable trigger is the
      principal's say-so — exactly the condition the grounding incident broke —
      so it wouldn't have fired in the case it was built for. Fix (option A,
      decouple): claiming now keys on **selection from the shared queue**, claim
      commit lands on `main` before branching. MEDIUMs: bundled lines serialise
      (fan-out needs per-leaf lines); adjacent one-line claims raise a trivial
      keep-both conflict (live-verified, "silent everywhere else" was false);
      put-away gained the `[~]`→`[ ]` reversion; tracker-based adopters pointed
      at the assignee primitive. LOW: timestamp demoted to a tiebreak.
      **Applied-batch cold pass owed** (above).
