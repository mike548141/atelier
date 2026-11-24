- [ ] 🎯 🔥 **Fix `ccfleet`, `fleet-sweep`, `review-drain` and `modelguard`: findings FL1–FL25 of
      the `160/1450` cold pass.** The principal's answer, 2026-11-22 UTC, verbatim: *"Fix all as
      advised (Recommended)"* (the option text is quoted on `160/1450`). Apply every finding as
      the verdict counsels:
      [`docs/reviews/2026-11-20-0813-ccfleet-fleet-sweep-review-drain-modelguard-cold.md`](../../reviews/2026-11-20-0813-ccfleet-fleet-sweep-review-drain-modelguard-cold.md)
      (act 1, reconcile, and the additions it makes to act-1 findings). The MAJORs first: FL1
      (never read a nonzero exit or error as a clean end; never force-remove a worktree holding
      uncommitted work) and FL2 (a dry run writes no launched list; an early end takes the pick
      back off it). The judgement calls as counselled: FL8 adoption scoped to the repos the
      config lists, with `create-repo`'s owner check as a further exemption, and a prompt that
      carries it out; FL11 "unsure means the local route", and the order stated for when no
      lapse is near; FL10 a threat section, an example without the bypass mode, a `check` line
      when one is set; FL18 the approval rule is the adopter's setting, not generic doctrine;
      FL21 both skills stay shipped.
      *Then, in order:* FL20's canary, one pass on a throwaway repo cut off on purpose and
      resumed; then ask the principal for the Fable re-check pass (rule 4: a session that wrote
      none of the fixes, briefed fresh). The estate's drain switch (`450/010` row 2) waits for
      that re-check to come back clean.
      *Who may not:* the authors barred on `160/1450` may fix (the bar is on reviewing), but the
      fixing session neither briefs nor runs the re-check.
      ✅ **Fixes landed 2026-11-23** (queue run c7a1e36e; two Opus workers,
      one on the `ccfleet` code, one on the two skills and `modelguard`,
      reconciled into one account and read by the run before landing).
      Every finding FL1–FL25 is applied as counselled, FL21 by confirming
      no change; the five judgement calls went the reviewer's way. Beyond
      the counsel, each stated in the commits: a stop word the session
      printed (BUDGET EXHAUSTED) is honoured even on an error end; a session
      gets its id up front (`--session-id`) rather than being looked up
      later; a review the principal has tied to a route by name does not
      spill until he rules (the spill question is written as open in the
      skill); `modelguard` fails closed after an unknown head, so a rare
      harmless command such as `docker run --name claude img` is refused.
      Tests: 79 `test_ccfleet`, 6 `test_modelguard` (41 bypass shapes denied,
      26 lookups passed), 55 `test_templates`, 12 single-source. Commits on
      `main` from the one that rewrites `modelguard` through the one that
      makes the skills say what the code does.
      ✅ **FL20 canary ran 2026-11-23** (a Sonnet worker; a throwaway repo
      with a local bare origin, a fake queue script, four Haiku sessions
      under `acceptEdits`, nothing on GitHub). PASS on the three cases it
      could make live: a pass cut off at `session_timeout_minutes: 1` ended
      `rc=124 result=TIMEOUT` with its session id on START and END though it
      printed nothing, its claim held and its worktree KEPT; `ccfleet
      resume` of that session by id ended DONE, its commit landed on the
      origin, the claim was released and the worktree removed; a clean DONE
      that left an uncommitted file was KEPT ("1 uncommitted or untracked
      path(s)"). Not testable here, as FL20 also named: a usage-capped end,
      a resumed session messaging its subagent, a reboot or driver death
      mid-run, and the `drain` loop itself. Two findings filed as
      `210/560`. The canary first ran the primary checkout's copy, 17
      commits stale, and switched to `main`'s; the primary was then
      fast-forwarded, so the fixed `modelguard` hook is now the live one.
      🎯 **Owed to the principal:** approval for the Fable re-check of
      `160/1450` (rule 4: a session that wrote none of the fixes, briefed
      fresh; not this run, which dispatched them). The estate's drain
      switch (`450/010` row 2) waits for it to come back clean.
      💬 **Answered 2026-11-23 ~12:35 UTC (session c7a1e36e, AskUserQuestion), his pick:** *"Approve one pass (Recommended)"*, to:
      approve one Fable re-check of the fixes (option text: *"One Fable review
      of the ccfleet, skills and modelguard fixes, run on the laptop's weekly
      budget by a fresh session that wrote none of them."*). An answer, not a
      ruling. Exactly that one pass plus its Opus brief, on the next
      `160/1450` re-check; c7a1e36e dispatched the fixes, so it neither
      briefs nor starts it: a fresh session does.
      💬 **Answered 2026-11-24 ~04:20 UTC (session edf25bd3, AskUserQuestion), his pick:** *"Wait, review the new build (Recommended)"*
      (option text: *"Hold the re-check until the build lands, then run it once over the fixes AND the new plan/run commands. One Fable review covers what your drain will actually use; your drain then switches straight after a clean result. Cost: /fable-drain stays in use until then (it may miss Monday 30 Nov). Widens the approved review's scope."*) An answer, not a ruling. So the approved `160/1450` re-check is
      held until `180/210` and `450/020` land, then briefed once over the
      `210/470` fixes plus the new `review plan` / `review run` commands, by
      a session that wrote none of them; the drain switch (`450/010` row 2)
      follows a clean result.
