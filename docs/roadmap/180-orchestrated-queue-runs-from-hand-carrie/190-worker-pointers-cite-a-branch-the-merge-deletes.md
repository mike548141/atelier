- [ ] 🔎 **A worker's review pointer cites its own branch or pre-merge
      hashes, which the orchestrator's merge then rewrites or deletes.**
      Found 2026-11-03 by queue run 4c65083c at its own merges. Five
      workers each wrote the `⏳` pointer for their lane in their last
      commit, as briefed. Three named the delta as "the commits on the
      `qr-4c65-…` branch", and one named a part-2 commit by its worktree
      hash. The orchestrator landed every lane by rebasing onto `main`, so
      the hashes changed and the branches were deleted at teardown: four
      pointers cited refs that no longer resolved, and a cold reviewer
      would have met them first. Fixed by hand in two commits the same
      hour. **Shapes:** the dispatch brief tells a worker to cite its delta
      by path and by the item it closes ("the commit that closes `NNN/NNN`"),
      never by branch or hash; or the orchestrator writes every pointer at
      the merge, where the final hashes exist. The second matches landing
      = queuing better, since the merge is the landing.
