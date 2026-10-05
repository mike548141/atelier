- [~] 🔎 **pointerscan still walks the whole tree, harness worktrees included** (claimed 2026-10-05-1239, wt: atelier-qr-115-250)
      `[S][tools]`. Found 2026-10-05 by a queue run's hand run of
      `pointerscan --root . .` at the primary checkout. It reported four
      findings, every one from a sibling session's linked worktree under
      `.claude/worktrees/`: that worktree's copy of an item, not this tree's.
      Its file discovery is a bare `rglob("*.md")` with a short skip list,
      so it never got `110/110`'s fix (guards walk only what git could
      commit) or `020/160`'s linked-worktree skip. `reviewscan`,
      `blockscan` and `harvestscan` were checked the same way and showed no
      worktree paths. CI is unaffected, because a CI checkout has no nested
      worktrees. The hook plane reads staged files. So the harm is a hand
      run or a session's own check counting other sessions' items, which is
      the miscount `130/020` exists to prevent.
      **The work:** route pointerscan's directory walk through the shared
      `tools/filewalk.py` (or the tracked-file listing the other guards
      use), with a test that a linked worktree nested in the root is not
      read.
