- [ ] 🔧 **Fix `ccfleet`, the review skills, `modelguard` and the reference queue: findings
      `DV1`–`DV11` of the `160/1800` cold pass and `PK1`–`PK21` of the `160/1810` cold pass, as
      each reviewer advised; the MODERATEs first.** The principal's pick, 2026-11-25 UTC (session
      14c2530d, AskUserQuestion; an answer, not a ruling), verbatim: *"Fix all as advised
      (Recommended)"* (option text: *"A fresh build session fixes all of them the way each
      reviewer suggested, starting with the 7 medium ones. Benefit: closes the gaps that only
      bite when something else also goes wrong, like a killed pass or a bad setting. Cost: Opus
      build time. A small Fable re-check would then be owed, and would wait for your
      approval."*). Apply every finding as its verdict counsels:
      [`docs/reviews/2026-11-25-0720-rk-drain-path-fixes-cold.md`](../../reviews/2026-11-25-0720-rk-drain-path-fixes-cold.md)
      and
      [`docs/reviews/2026-11-25-0721-rk-part-3-fixes-ccfleet-modelguard-subject-skills-cold.md`](../../reviews/2026-11-25-0721-rk-part-3-fixes-ccfleet-modelguard-subject-skills-cold.md)
      (act 1, the reconcile, and `DV11` and `PK21` formed there). **Order:** the MODERATEs
      `DV1`, `DV3`, `PK1`–`PK5`, then the minors and notes. Both reviewers counselled that the
      2026-11-30 drain may run before these land; none is a precondition for it. Afterwards a
      Fable re-check of the fixes is owed, queued in `160-doctrine-review-owed`, waiting on the
      principal's approval.
      💬 **Answered 2026-11-25 ~08:30 UTC (session 0b4f93ef, `atelier-86`,
      AskUserQuestion; an answer, not a ruling), his pick:** *"Before, plus
      re-check"* (option text: *"Land all fixes and run their Fable re-check
      before Monday, then switch. Benefit: Monday runs on the most robust code.
      Cost: another Fable pass this week, and a real risk it isn't done in time,
      so Monday falls back to /fable-drain."*). So: these fixes land AND their
      Fable re-check comes back with no MAJOR before the drain starts
      (2026-11-29 23:00 UTC); only then does the drain switch (`450/010` row 2,
      after shed's `020/1040`). That approves exactly ONE Fable re-check pass
      over this item's fixes, plus its Opus brief, by a fresh session that wrote
      none of them; it does not lift the general Fable hold. If either misses
      the drain's start, Monday runs on `/fable-drain` and the switch waits
      for the gap after it. Nothing may land on the drain's paths between a
      clean re-check and the drain.
