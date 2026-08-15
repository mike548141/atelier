- [ ] 🎯 **Fleet rollout of the split board — per-repo, Mike's call.** atelier
      is the worked example (board-store ADR 2026-08-15); `ros` (5,213-line
      board), `shed` (3,125) and `faves` (1,853) are the repos paying the
      monolith cost daily. Gated on this cycle's review closing. Per repo:
      run the migration split, adopt the board floor check (already reaches
      every child via the registry — passes as out-of-scope until the
      directory exists), and carry each repo's own conventions across.
      Rollout order and timing are Mike's to rule.
