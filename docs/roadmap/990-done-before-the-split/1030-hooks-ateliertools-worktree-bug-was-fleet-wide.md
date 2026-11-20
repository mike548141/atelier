- [x] **hooks.atelierTools worktree bug was fleet-wide — 2026-07-19.** 9 more
      children carried the relative path (every worktree commit blocked by the
      fail-closed hook); all 10 set absolute, and the **source fixed** —
      `create-repo` step 6 now absolutises the path it stamps. (Resolves the shed
      entry's "Worth checking on other children" above.)
