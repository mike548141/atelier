- [ ] 🔥 **Fix `ccfleet`, `fleet-sweep`, `review-drain` and `modelguard`: findings FL1–FL25 of
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
