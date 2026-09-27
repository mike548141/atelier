- [ ] **HAND-UP from a private child (faves) — a clean worktree plus a pushed
      HEAD says "nothing unpushed", not "the agent has stopped", and reading it
      as the latter can destroy a live worker's working directory.**

  **The class.** In an orchestrated queue run, an orchestrator that decides a
  worker is finished by inference from git — `git status --short` empty **and**
  `git rev-parse HEAD` at the worktree `==` `git rev-parse origin/<branch>` —
  is measuring "nothing uncommitted, nothing unpushed". It is not measuring
  "has stopped": verification, re-reads and report-writing all happen after
  the last push and leave no trace in either signal. Tearing the worktree down
  on that inference (`git worktree remove`) destroys the directory a still-
  running agent is standing in.

  **Where this touches the house text (quoted at `origin/main`, this pin).**
  `CONCURRENCY.md` line 250: *"Delete a worktree when its branch lands
  (`git worktree remove`); stale worktrees are the concurrency equivalent of a
  leaked file handle."* Says *when its branch lands* — silent on how the
  orchestrator learns that, which is exactly the gap the incident fell into.
  § *Orchestrated queue runs* says a worker "builds and commits in its own
  worktree and hands back — the merge to `main`... stays the orchestrator's,
  which reads the work it is endorsing before the merge lands", and separately
  that "a run never starts or instructs its own successor" — neither line
  states what signal marks a worker's hand-back as complete enough to reclaim
  its worktree.

  **The incident.** faves session `faves-b1`, 2026-09-07: three workers, each
  briefed to commit, push and stop without merging. Two of three hit this —
  the orchestrator's git check passed while a worker was still re-verifying on
  its own worktree, and the directory vanished mid-run. Nothing was lost (both
  agents diagnosed the resulting failures as teardown artefacts, not
  regressions) — the near-miss is the finding, not the outcome.

  **The child's ruling (2026-09-07, not a house ruling — the child's own
  fix, offered here for atelier to weigh, not to adopt as-is).** The
  principal took the more robust of two options over the narrower "delay
  teardown" fix: every worker brief now requires an explicit terminal marker
  as the agent's last act. The child also notes the marker's hole: a crashed
  agent never sends one, so it can prove *done* but never *not done* — the
  harness's own completion notification is what covers that case. Working
  rule that resulted: merging from `origin/<branch>` early is safe; teardown
  (`git worktree remove` + branch deletion) waits for the completion
  notification; the marker is what makes the worker's own report trustworthy
  in between.

  **Evidence the marker approach was tried again.** faves session `40d6dea4`
  (2026-09-27) briefed three workers with a required final line,
  `WORKER DONE: <branch>@<sha>`. Reported here only as briefed — no outcome
  claimed.

  **Options, offered — no recommendation:**
  1. Add a teardown-waits-for-completion-notification rule to § *Orchestrated
     queue runs* (or beside line 250) — cheapest, closes the gap this section
     already almost states. Risk: still leans on the harness always delivering
     that notification, which this text does not itself verify.
  2. Add a required terminal marker to the dispatch-prompt obligations, beside
     the scratch-directory clause already there — gives the orchestrator a
     positive signal instead of an absence. Risk: costs a line in every brief,
     and (per the child's own note) proves *done*, never *not done*, so it
     cannot stand alone.
  3. Both — the notification as the backstop for a crashed worker, the marker
     as what makes an in-progress worker's own report trustworthy before that
     notification lands. Risk: none beyond doing both, but is two changes
     where the house may want one canonical answer.
  4. Leave it — the harness completion notification already exists and the
     dispatch section already tells an orchestrator to read the work before
     merging. Risk: the *destroy-while-running* failure mode is the same one
     that already hit two of three workers in one run; leaving it says nothing
     changed the odds.
