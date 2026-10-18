- [x] **DONE 2026-10-18** (wt: atelier-qr-210-290)
      🔎 **`ccclose --identifiers` over-credits work from overlapping
      sessions, and reads ⏳ anywhere in an item.** Found by the session that
      shipped it (2026-10-18, `210/280`), on its own close. Its first real
      block listed 115 commits; the session's own commits on `main` were 88.
      The rest came from a cloud review session working at the same time:
      its branch commits, and the squash merge of PR #119. The board line
      credited that session's `115/360` as created. And it listed `210/280`
      under "⏳ review items created" because that item's close note mentions
      ⏳. Both are the window heuristic the tool already prints, but the
      block is meant to be pasted as fact.
      **Shapes to weigh:** read the ⏳ marker only from an item's state line;
      count commits only on the integration branch's first-parent line, and
      leave out squash merges of PRs the session did not run `gh pr merge`
      on. The session's own SHAs cannot come from its transcript when it
      commits with `-q`, which this house does.
      ✅ **Fixed 2026-10-18, `0462173` and `621d18b`.** Both shapes built,
      one weighed differently. The ⏳ marker is read only from an item's
      state line, outside code spans (board.py's own grammar). Commits are
      credited as fact only on positive evidence: the subject appears in a
      `git commit`/`git merge` command of the session or a subagent, or the
      commit is the squash merge of a PR the session ran `gh pr merge` on.
      A squash merge the session did not run is left out. Everything else
      dated in the window prints on its own "unconfirmed" line, and board
      movement follows the same tiers. First-parent as the rule was
      rejected: it drops a worktree session's own branch commits and does
      nothing about a peer's direct pushes to `main`. Probed on its own
      session: 10 credited, 9 unconfirmed (the peer's 8 and one of this
      run's, committed by a worker with `-F <file>`), and the peer's two
      closed items moved to the unconfirmed board line. 58 ccclose tests
      green. Residue filed at `210/310`; cold pass queued at `160/960`.
