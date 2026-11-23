- [~] 🔥 **Fix `ccfleet`, `fleet-sweep`, `review-drain` and `modelguard`: findings FL1–FL25 of
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
      *(claimed 2026-11-23 UTC, session c7a1e36e, wt: none · at: FL20 canary)*
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
      **Still owed here, in order:** the FL20 canary (running, local only,
      Haiku sessions); then the ask for the Fable re-check of `160/1450`,
      🎯 the principal's.
