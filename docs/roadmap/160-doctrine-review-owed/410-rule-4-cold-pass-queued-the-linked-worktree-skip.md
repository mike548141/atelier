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
      `[~]` **CLAIMED 2026-09-25 0705 UTC for the review run** (wt:
      review-batch-0925; brief
      `docs/reviews/2026-09-25-0715-linked-worktree-skip-cold.md`) by a
      Mike-opened `claude-fable-5-1` session ("Please deliver all fable
      dependent work, and work that would be best delivered using fable") that
      authored none of the delta. Shape, disclosed per rule 4:
      reviewer-plus-orchestrator, both seats Fable — this session writes the
      refs-only brief and holds the `.deferred.md` sibling outside the worktree;
      a fresh Fable subagent it spawns forms every finding and severity. The
      sibling, the intent record and prior verdicts stay unopened by the
      reviewer until its phase-1 findings are committed. Provenance and exposure
      go in the verdict.
      - [ ] 🎯 **The pass RAN 2026-09-26; the cycle CLOSES on this pass (no
            MAJOR) — what remains is decided into the backlog.** The rule-4
            Fable cold pass (taker: a fresh `claude-fable-5-1` subagent under a
            `claude-fable-5-1` orchestrator — the shape disclosed in the claim
            above; the sibling, the intent record and prior verdicts opened only
            after the phase-1 findings were committed) returned
            PASS-WITH-FINDINGS — 0 MAJOR · 2 MODERATE · 5 minor · 3 note →
            [`2026-09-25-0715-linked-worktree-skip-cold.md`](../../reviews/2026-09-25-0715-linked-worktree-skip-cold.md)
            (sibling folded in and deleted). LW1 (MODERATE): reviewscan never
            got the skip — its rglob walks into a nested harness worktree and,
            on the hook plane, blocks the primary session's commit on a sibling
            worktree's uncommitted draft brief (probed live); LW2 (MODERATE):
            the same hole in coldsweep, whose rule-2 bar is computed on the
            relative path so a nested worktree's copy of a barred verdict prints
            as an ordinary hit; LW10 (minor) formed at reconcile — the file-ness
            cost was never put to the principal. Findings are the principal's to
            decide (rule 3); nothing was applied.
