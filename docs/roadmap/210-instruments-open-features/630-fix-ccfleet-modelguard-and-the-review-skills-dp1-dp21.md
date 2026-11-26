- [ ] 🔧 **Fix `ccfleet`, `modelguard`, the reference queue and the review skills: findings
      `DP1`–`DP21` of the `160/1820` re-check, as the reviewer counselled; the MODERATEs first.**
      The findings:
      [`docs/reviews/2026-11-25-1920-dv-pk-fixes-recheck-cold.md`](../../reviews/2026-11-25-1920-dv-pk-fixes-recheck-cold.md)
      (act 1 and its reconcile; `DP21` formed at reconcile). **Order:** the MODERATEs `DP1`–`DP5`,
      then the minors `DP6`–`DP16`, then the notes `DP17`–`DP21`. Every finding is self-authored
      doctrine by function for whoever wrote the fixes it answers, so this item's build session
      is the author of its own fixes and neither briefs nor runs any review of them.
      💬 **Answered 2026-11-25 ~21:45 UTC (session 01c055e5, `atelier-4c`, AskUserQuestion; an
      answer, not a ruling)**, his pick: *"Fix all now, before Monday"* (option text: *"Fix them
      this week. Benefit: Monday runs on tighter code. Risk: the fixes change the drain's code
      after its review, so Monday falls back to the old /fable-drain unless another Fable
      re-check is run and comes back clean in time, which is more Fable budget this week."*).
      ⚖️ **His ruling, the same ask's follow-up, verbatim** (asked whether to approve one more
      Fable re-check of these fixes before the drain): *"Given the low severity of the findings I
      am ruling that * This code is ready to use for the drain so we can continue to switch over
      to it * That we will fix the findings we know about * If those fixes cause work that then
      requires another review we can decide if that review is run in the interim or waits until
      the next drain, but I wont decide that until we have completed the fixes"*.
      **Read as** (the session's reading, put to him at its close): step D of `450/010` row 2
      goes ahead on the reviewed code; these fixes are built now; no Fable re-check of them is
      approved, and whether one runs before the drain or after it is his to decide once they are
      done, so a pointer for it is queued in `160` at the landing commit, waiting on him. His
      pick on `210/620` that nothing lands on the drain's paths between a clean re-check and
      the drain is read as set aside by this ruling for these fixes alone. 🚩 So the fixes can
      reach the drain unreviewed: land them before step D's first-use dry run, or after the
      drain, never during it, and say which.
