- [x] 🔧 **Fix `ccfleet`, the subject skills, `modelguard` and `/atelier:session close`:
      findings RK1–RK29 of the `160/1790` cold pass, as the reviewer advised; the four on the
      drain's path first, before Monday 2026-11-30's drain.** The principal's picks, 2026-11-25
      UTC (session 4a34637a, AskUserQuestion; answers, not rulings, option text quoted on
      `160/1790`): *"Fix all as advised (Recommended)"* and *"Small Fable check, then switch
      (Recommended)"*. Apply every finding as the verdict counsels:
      [`docs/reviews/2026-11-24-2141-ccfleet-recheck-and-subject-action-review-plan-cold.md`](../../reviews/2026-11-24-2141-ccfleet-recheck-and-subject-action-review-plan-cold.md)
      (act 1, the reconcile's additions, and `RK29` formed there), judgement calls taken the
      reviewer's way (`RK1` how an action's text loads, `RK7` where the seal's contract lives,
      `RK8` what the plan's cost column means, `RK29` narrowing the routers' `allowed-tools`).
      **Order:** (1) the drain path: `RK2` (the per-pass prompt's template path) and `RK5` (a fold
      after the reset), then `RK12`'s check that the real config still grants its sessions what
      they need (estate-side, read-only), then ONE canary pass on the real config; (2) one small
      Fable cold pass over the drain-path fixes only, by a fresh session that built none of them,
      before Monday's drain uses the new commands (his pick; it does not lift the general Fable
      hold beyond that one pass); (3) the remaining findings. The build session queues the
      small pass's pointer in its landing commit and neither briefs nor runs it.
      🔒 CLAIMED 2026-11-25T03:56Z (claimed 2026-11-25-0356, wt: atelier-c3) by session
      0ee74059 (`atelier-c3`, Opus 5.5, principal-opened by `/atelier:work run`): part (1)
      first, the drain-path fixes `RK2` and `RK5`, `RK12`'s read-only check and one canary,
      landing before 2026-11-29 23:00 UTC; then part (3). It neither briefs nor runs the small
      Fable pass; it queues that pass's pointer in the drain-path landing commit.
      ✅ **Part 1, the drain path, landed 2026-11-25** (session 0ee74059). `RK2`: the
      reviewer-prompt template moved from `run.md` into `orchestrator-prompt.md` (its
      one home, under *THE REVIEWER PROMPT*), so a pass in another repo reads no file
      outside its worktree; `fold-prompt.md` points at nothing outside its steps.
      `RK5`: `ccfleet` refuses new work at `reset_utc` but runs a fold (`run --in
      --item`) as it runs a `resume`; manual, help line and Mode 2 say so; a new test
      fails on the old code. **`RK12`, the real drain config, read-only** (`ccfleet
      check`, both review prompts): its sessions run in the bypass permission mode, so
      the config grants what they need (the reverse of `RK12`'s risk; the mode is the
      estate's choice, and `check` names it); its `pass_prompt` still names the
      retired `skills/review-drain/` path, so every pass would be refused at launch:
      already queued in the estate root's own board, not fixed from here (work lands
      in the repo it changes); its `take` records no session id (`RK21`, part 3).
      **Canary**, one pass: a copy of the real config with its grant fields kept
      verbatim and its repo, queue, models and reset replaced (a throwaway repo with
      a local origin, a stand-in queue, the cheapest model for both orchestrator and
      reviewer, so no review-tier spend and no real claim). `result=DONE`, claim
      taken with the session id, released, `ended` called, worktree removed; the
      orchestrator read no file outside its worktree and filled the reviewer prompt
      from its own (`RK2` holds live); act 1, fold and review log landed on the
      origin. It found one more drain-path defect, fixed in the same commit: the
      Agent tool takes a tier alias (`fable`, `opus`, `sonnet`, `haiku`) and refuses
      a full model id, which the example config and `run.md` gave for
      `REVIEW_MODEL`; the canary's orchestrator recovered by retrying with the alias,
      a real pass might not. The real config already uses the alias. The small
      Fable pass is queued as `160/1800`, neither briefed nor run here.
      ✅ **Part 3, the remaining findings, landed 2026-11-25** (session 0ee74059; four
      Opus workers in their own worktrees, merged and re-tested by the run). Every one
      of `RK1`, `RK3`, `RK4`, `RK6`–`RK29` is applied as counselled, judgement calls
      the reviewer's way. `modelguard` (`fc922383`): `RK9` a `claude` after an unknown
      head counts only when a session flag or a prompt follows, and the refusal says
      how to rephrase; `RK15` the nine shapes denied; the harness's `Workflow` route
      documented as unguarded. Skills (`4a9318b7`, `9b4a8f8f`): `RK1` and `RK29` each
      router grants only a read of the plugin's own files, its menu call and the
      read-only git reads its actions name, pinned by test; a headless probe with no
      user-level settings ran `/atelier:session close` end to end where it was refused
      before; `RK19` the eleven named mutations now fail the tests; `RK12`'s fleet
      prompts stop BLOCKED on a refused read rather than inlining long, changing texts;
      `RK13`, `RK14`, `RK20`, `RK22`, `RK27` as worded. `ccfleet` lifecycle
      (`53203833`, `2d8e05e3`): `RK3` the first line beginning `RESULT:` with a shape
      line; `RK4` the session's process id recorded and `resume` refused while it
      lives; `RK6`, `RK16`, `RK17`, `RK24`, `RK25`, `RK26` with tests that fail on the
      old code. `ccfleet` grant and contract (the commit after them): `RK7` the seal's
      contract stated and a reference queue shipped; `RK8` the history counts resumes
      and folds and splits by repo and model, and says it measures no review size;
      `RK10` the instruction file is guarded, a public repo's launch refused by default
      (`instructions_guard: warn` to go on with a line per name); `RK11`, `RK12`,
      `RK18`, `RK21`, `RK23`, `RK28`. Risks moved, named in the commits: a refused
      claim held by a dead session is now skipped quietly; the live-session check
      rests on `ps` showing the session id; two digest pins make the router and close
      texts change only with their digest. The part-3 cold pass is queued as
      `160/1810` and waits for the principal's permission for Fable work. **Owed by
      the estate root** (hand-down, not done here): its drain config's `pass_prompt`
      path, and a choice on `instructions_guard` before a public repo's next pass,
      since its user-level instruction file names private names.
