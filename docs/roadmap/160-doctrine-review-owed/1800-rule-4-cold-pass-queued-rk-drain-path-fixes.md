- [ ] ⏳ 🔥 **Rule-4 cold pass queued (due before Monday 2026-11-30 NZ drain, which starts the evening of 2026-11-29 UTC): the RK drain-path fixes, `RK2` and `RK5`, with
      the canary's `REVIEW_MODEL` correction (`210/600` part 1).** The small Fable
      check the principal picked on `160/1790` (*"Small Fable check, then switch
      (Recommended)"*, an answer, not a ruling): one pass over the drain-path fixes
      only, before Monday 2026-11-30's drain uses the new commands. It does not lift
      the general Fable hold beyond that one pass. The authoring session
      (0ee74059, `atelier-c3`, Opus 5.5, principal-opened by `/atelier:work run`)
      built the fixes, ran the canary, and queues this; it neither briefs nor runs
      it.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code and prompt cold pass, per `method/REVIEW.md` rule 4, by a
      fresh session that built none of the fixes.
      *Delta, scoped to paths:* `skills/review/orchestrator-prompt.md`,
      `skills/review/fold-prompt.md`, `skills/review/run.md` (§ *Mode 2*, § *The
      reviewer prompt*, § *The variables the prompts need*), `instruments/ccfleet`
      (`run_one`'s reset check, the `reset_utc` help line),
      `instruments/man/ccfleet.1` (`reset_utc`), `instruments/test_ccfleet.py`
      (`test_a_fold_runs_after_the_reset_and_new_work_does_not`),
      `instruments/ccfleet.example.json` (`REVIEW_MODEL`): the commit citing
      `210/600` part 1, on `main`.
      *Intent record:*
      [`../210-instruments-open-features/600-fix-ccfleet-subject-skills-and-modelguard-rk1-rk29.md`](../210-instruments-open-features/600-fix-ccfleet-subject-skills-and-modelguard-rk1-rk29.md);
      the findings:
      [`../../reviews/2026-11-24-2141-ccfleet-recheck-and-subject-action-review-plan-cold.md`](../../reviews/2026-11-24-2141-ccfleet-recheck-and-subject-action-review-plan-cold.md)
      (`RK2`, `RK5`, `RK12`).
      🔒 CLAIMED 2026-11-25T07:05Z (claimed 2026-11-25-0705, wt: brief-160-1800-0704) by headless
      session 4da4abc0 (Opus 5.5), started by principal-opened session 14c2530d
      (`atelier-e7`, Opus 5.5), for brief-writing only: the brief and its held-back
      sibling, no pass run. Neither session wrote any part of the delta; 14c2530d
      orchestrates the pass once the brief lands and writes no part of it.
      **Brief written 2026-11-25 UTC:**
      `docs/reviews/2026-11-25-0720-rk-drain-path-fixes-cold.md`, pinned at `6ddbead2`,
      finding prefix `DV`. Its held-back sibling (16 questions, 14 facts) is held
      user-local, outside the repo, every worktree and every scratchpad; the orchestrator
      is told where, never by the brief.
      🔓 2026-11-25T07:23Z: session 4da4abc0 releases its claim. The pass is open for a fresh Fable
      reviewer under orchestrator 14c2530d; `0ee74059`, its workers and `4da4abc0` are
      barred from running it.
