- [x] **BUILT 2026-10-18** (wt: atelier-qr-210-280)
      **`ccclose` prints the identifiers block, ready to paste.** `RECORD.md`
      now asks every session's detail record and closing message to end with
      an identifiers block (`180/080`, 2026-10-18): session id, model and
      window; commits; PRs; board items and reviews queued; worktrees and
      branches; agents; other repos written to. `ccclose` already reads most
      of these fresh (session id, window, commits in the window, PRs, agents)
      but prints them as checks, not as the block. A `--identifiers` form
      printing the block in `RECORD.md`'s order would make it a copy rather
      than a recollection, which is the rule's point. Filed, not started, by
      the session that wrote the rule. Not idea-only: it is ready to build.

  **Closed 2026-10-18** (commits `4142efb`, `8b30ee6`). `ccclose
  --identifiers` prints only the block, in `RECORD.md`'s order, with every
  field on every run (`none`, or `by hand — <why>`). PRs and worktrees
  created are read from the session's own commands, because a merged PR and
  a removed worktree leave nothing to find later. Board items are grouped
  completed, created, claimed and still open, and ⏳ reviews created, read
  from the session's commits. Agents are listed uncapped. Worktree paths
  under the home directory print as `~/…`, so the block can go into a public
  record (`--json` keeps them absolute). Built by a Sonnet worker, with the
  home-path change by the orchestrator. Instruments suite 475/475 at the
  rebased head. Cold pass: `160/920` widens to these commits.
