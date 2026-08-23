- [ ] 🔎 **`/security-review` reads the *session's* pending diff, not the path
  it is aimed at — three reproductions in one review batch (2026-08-15).**
  Three concurrent rule-4 reviewers, each told to aim the house security
  scanner at their own scratch clone, each had it scan the shared worktree's
  dirty state instead. What it printed into their contexts was another
  pass's brief and `.deferred.md` sibling (the reply-gate pass, whose brief
  and sibling were being written in the same worktree at the time) — the SL2
  channel class (`REVIEW.md` § lens 4) for the third, fourth and fifth
  live instances. No reviewer's *own* sibling was exposed (the orchestrator
  had moved all four out of the tree before spawning), and every reviewer
  disclosed the exposure in its verdict; the cross-pass leak was to a
  different subject, so no finding was anchored on it — but the mechanism is
  now established rather than suspected: **the scanner has no path
  argument that overrides its notion of "pending changes", and in a shared
  worktree "pending" means every session's uncommitted work.** REVIEW.md's
  existing caution ("never run it over a brief or other deferred material
  before findings are committed") assumes the reviewer controls what is
  pending; under the orchestrator-partition shape it does not. Counsel, not
  decided: (a) the batch preamble should tell reviewers the scanner is
  discharged by grounds under the partition shape unless the worktree is
  clean at the moment of aiming — the orchestrator can guarantee that only
  by committing before every spawn and writing nothing while reviewers run;
  or (b) REVIEW.md lens 4's reach paragraph names this shape explicitly.
  Verdicts recording the instances:
  [`reviews/2026-08-15-1030-board-store-migration-cold.md`](../../reviews/2026-08-15-1030-board-store-migration-cold.md),
  [`reviews/2026-08-15-1032-cctranscript-search-cold.md`](../../reviews/2026-08-15-1032-cctranscript-search-cold.md),
  [`reviews/2026-08-15-1033-communication-floor-cold.md`](../../reviews/2026-08-15-1033-communication-floor-cold.md).
