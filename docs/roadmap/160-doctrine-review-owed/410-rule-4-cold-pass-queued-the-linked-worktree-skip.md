- ⏳ **Rule-4 cold pass queued — the linked-worktree skip across eleven
      scanners (`020/160`, E9).** Self-authored by the run (its dispatched
      worker's output is the run's authorship); queued at landing, and the run
      neither takes nor spawns it. *Tier:* Fable, the principal-named review
      tier — checked at selection; a session that cannot honour the bar stops
      rather than takes. *Pass type:* code cold pass, per `method/REVIEW.md`
      rule 4. *Delta — scoped to paths:* the `_walk_files` pruning line in
      `tools/{secretscan,leakscan,conflictscan,linkscan,sizescan,datescan,`
      `wrapscan,spellscan,pathscan,licenscan,stampscan}.py` and the
      `LinkedWorktreeSkipped` class in each of their eleven `test_*.py`
      siblings. Landed on `main`, 2026-09-20.
      **The lenses that matter most here:** whether pruning on **file-ness**
      alone is the right trade, given it also prunes any directory holding an
      ordinary file named `.git` — the worker documented and tested that cost
      rather than hiding it, so the question is whether the cost was the
      principal's to accept rather than a worker's; whether eleven
      independently-edited copies of one line are already identical, which is
      checkable by diff and is `115/080`'s whole argument; whether anything
      *should* be scanned inside a linked worktree that is now silently
      skipped, since the fix makes a real surface invisible rather than merely
      deduplicating it; and whether the two planes' exemption claims hold —
      that a file argument never reaches `_walk_files` and that `--staged`
      routes through the git-diff path — which were verified by reading the
      code here rather than by a probe on every one of the eleven.
      *Intent record:*
      [`../../sessions/2026-09-20-1053-queue-run-the-loose-ends.md`](../../sessions/2026-09-20-1053-queue-run-the-loose-ends.md).
