- [ ] **`board --check` reads the worktree, not the staged plane.** The check
      compares worktree item files against the worktree index, so a commit
      staging an item edit without the rebuilt index is caught only when the
      two agree on disk — the same seam harvestscan closed as HV4 (its hook
      question is the INDEX: what is this commit about to make true?). Bring
      the check to the staged plane the same way. Stated as a residual in
      `tools/README.md` and the tool's docstring at birth.
