- [x] 🔧 **Fix `ccfleet`, the review skills, `modelguard` and the reference queue: findings
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
      🔒 CLAIMED 2026-11-25T11:25Z (claimed 2026-11-25-1125, wt: atelier-f9-*) by principal-opened
      session b04df0da (`atelier-f9`, Opus 5.5), the build session of step A on `450/010` row 2.
      It orchestrates worker subagents in worktrees and lands their fixes; it neither briefs nor
      runs the Fable re-check (step C), and queues only its pointer.
      💬 **Answered 2026-11-25 ~11:30 UTC (session b04df0da, `atelier-f9`,
      AskUserQuestion; an answer, not a ruling)**, on `PK7`, whose counsel was only to put it
      to him: asked whether words typed after `/atelier:session close` that would skip a step
      are obeyed, his pick: *"Obey, but say so (Recommended)"* (option text: *"Your typed
      words can skip a step; the close names which step was skipped and that you asked.
      Benefit: your word wins, as the rest of the house rules say. Risk: a dropped or mistyped
      word could skip the record check, but the close says so in plain sight, so you'd see
      it."*). Applied in `001d9b42`.
      Note: this item's claim lines landed inside `932a0185` (another session's close commit
      on the shared checkout staged them with its own); the claim is as written above.
      ✅ **Done 2026-11-25 UTC (session b04df0da, `atelier-f9`):** all 32 applied as counselled,
      the MODERATEs first. `DV1`, `DV3`, `DV7` (M5), `DV11`, `PK1`–`PK5`: `422b5b5c`..`afa9aec7`
      (Opus worker). The skill texts, `DV2`–`DV4`, `DV6`–`DV10`, `PK6`–`PK10`, `PK14`–`PK16`,
      `PK18`: `b7a3a694`..`1c3488ad`, `db4984c1` (Sonnet worker, and this session). `PK13`,
      G6, `PK15` (`tools/README.md`), `PK21`: `9d52835a`..`127f3fef` (Sonnet worker). The
      ccfleet minors and notes, `DV2`, `PK9`–`PK12`, `PK14`, `PK16`, `PK17`, `PK19`, `PK20`:
      `3c824d40`..`36ec7901` (Opus worker). The changelog (`DV5`, `PK15`) and the rest of
      `PK15` land with this close. Two places the fix departs from the letter of the counsel,
      for the re-check to weigh: `PK4` also accepts a `RESULT:` line that closes a block
      holding `REPO:`, since the fleet prompts put `REPO:` first and the counsel's "directly
      above" alone would read every sweep as UNKNOWN; `DV4` took `run.md`'s "no read of this
      skill" route, since ccfleet fills no `{ATELIER}` for the review prompts. Full tools suite
      on 3.14: 3,499 tests, one failure (a spellscan memory-bound test that passes alone, under
      load); `test_ccfleet` 152 OK on 3.9 and 3.14. The re-check is queued as `160/1820`.
