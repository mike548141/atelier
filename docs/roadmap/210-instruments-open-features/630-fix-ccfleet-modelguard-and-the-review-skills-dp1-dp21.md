- [x] 🔧 **Fix `ccfleet`, `modelguard`, the reference queue and the review skills: findings
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
      🔒 CLAIMED 2026-11-26T01:57Z (time corrected from `date -u` at close; the claim commit wrote 02:05Z) (wt: `atelier-cd-dp-*`, one per worker) by principal-opened
      session 5e236e34 (`atelier-cd`, Opus 5.5), to build all of `DP1`–`DP21`, MODERATEs first,
      and land them before step D of `450/010` row 2. Workers each in their own worktree: `mg`
      (`tools/modelguard.py`: `DP1`, `DP9`, `DP10`, `DP21`), `cf` (`instruments/ccfleet` and its
      manual: `DP2`–`DP6`, `DP13`, `DP17`, `DP18`, `DP20`, the `check` half of `DP7`, the manual
      half of `DP11`), `sk` (the reference queue's `take`, the skills, `REVIEW.md`,
      `pointerscan`: `DP7`, `DP8`, `DP11`, `DP12`, `DP14`–`DP16`, `DP19`, the prompts' half of
      `DP2`). No Fable work: this session briefs and runs no review of these fixes.
      ✅ **Done 2026-11-26 UTC** (session 5e236e34, `atelier-cd`): all 21 applied, MODERATEs
      first, by four Opus workers, merged in one integration branch. Workers: `mg`
      (`a72a84f8`, `2e1a6b87`), `cfa` (`b296f17e`, `54621c8b`, `acea648e`), `cfb` (`3244ca7f`,
      `b9d094a1`), `sk` (`9fc276f9`..`73edeb34`); each fix's test was seen failing on the
      unfixed code or a hand-applied mutant first. The merge joined the two `ccfleet` workers:
      four old pins moved to `DP3`/`DP4`'s contract, resume's `END` line given the same fields
      as a pass's, *THREATS* bounded to `DP13`'s rule. Whole suite at the landing head: tools
      3,551 OK, instruments 307 OK, node 754 pass; `blockscan` clean. Departures from the
      counsel, for any re-check to weigh:
      - `DP1`: the first half of the counsel only. tmux options stop at the command word, and
        all seven rows are denied again; "any `claude` word after tmux is a launch" was not
        built, since it would deny `tmux new -d docker logs claude` and `tmux send-keys 'cd
        claude' Enter`, which both hooks passed. The bare-word pass is named in the docstring.
      - `DP2`: a closing sentence after `RESULT:` still reads UNKNOWN, on purpose: it looks
        the same as a quoted template block followed by prose. The prompts now forbid it.
      - `DP4`: both the setting and the environment variable, since the documentation does
        not say whether `--settings` honours the key; not tried in a live session.
      - `DP13`: the time bound is the worktree's age, since `ccfleet` never sees the claim's.
      - `DP15`: `review_model=` is on the `END` line and in `<log>.end`, not in the result
        file, whose header parser a new field would break.
      - `DP17`: a dry drain still reads an ordinary exit 1 from `next` as "not sealed"; a
        crash, a timeout or exit 126/127 now ends as a queue error. Telling a refusal from a
        failure needs a refusal code in the queue contract.
      - `DP18`: a private session keeps an import inside a sentence as text, where Claude Code
        would load the file (named in *THREATS*).
      The review pointer is `160/1870`, queued at the landing commit and waiting on his
      decision; no Fable work started.
