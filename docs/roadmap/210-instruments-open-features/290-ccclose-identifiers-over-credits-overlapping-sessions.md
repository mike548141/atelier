- [~] 🔎 **`ccclose --identifiers` over-credits work from overlapping
      (claimed 2026-10-18-0503, wt: atelier-qr-210-290)
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
