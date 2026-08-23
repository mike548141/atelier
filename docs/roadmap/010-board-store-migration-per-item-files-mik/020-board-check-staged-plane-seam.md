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
      **The interim wording to retire at landing (BW6, ruled 2026-08-23):**
      the staged-plane residual is spelled on five surfaces, each to be
      re-worded or dropped when this check lands — `tools/board.py` (the
      hook clause in § *Why the index is committed and checked* and the
      merged § *STATED RESIDUAL*) · `tools/README.md` § **board** ·
      `docs/method/CONCURRENCY.md` § *On a split board* ·
      `docs/roadmap/README.md` (the preamble qualifier) · the 2026-08-23
      amendment at the foot of the board-store ADR. This item's landing
      commit sweeps them; nothing machine-checks the unwind, so the list
      lives here where the work is funded.
