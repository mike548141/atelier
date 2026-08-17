- [ ] **`board --check` reads the worktree, not the staged plane.** The check
      compares worktree item files against the worktree index, so a commit
      staging an item edit without the rebuilt index is caught only when the
      two agree on disk — the same seam harvestscan closed as HV4 (its hook
      question is the INDEX: what is this commit about to make true?). Bring
      the check to the staged plane the same way. Stated as a residual in
      `tools/README.md` and the tool's docstring at birth.
      **FUNDED 2026-08-17 (Mike's BS1 ruling, `290-ruling-round-…/050`):** build
      the staged-plane check **and** a `rebuild` source flag that regenerates
      from the index rather than the worktree (BS1 counsel (b)); name the flag
      in CONCURRENCY CF3 at landing; code cold pass queued at landing.
