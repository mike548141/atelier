- [ ] ⏳ **Rule-4 cold pass queued: the `DP` fixes to `ccfleet`, the reference queue,
      `modelguard`, `pointerscan`, `REVIEW.md` and the review, work and fleet skills
      (`210/630`).** The authoring session (5e236e34, `atelier-cd`, Opus 5.5, principal-opened
      by `/atelier:work run`, whose four workers wrote the fixes) queues this and neither
      briefs nor takes it.
      ✅ **Approved 2026-11-26 ~03:20 UTC (session 5e236e34, `atelier-cd`, AskUserQuestion), his
      pick verbatim:** *"Before the drain (Recommended)"* (option text: *"One Fable review this
      week, by a fresh session, before Monday 12:00 NZDT. Benefit: keeps your 24 Nov rule that
      new drain code is reviewed before a drain uses it; these fixes change how a paid review's
      verdict is read. Risk: spends weekly Fable budget now, and if it finds a major problem,
      Monday falls back to the old /fable-drain."*). Exactly this one pass plus its Opus brief,
      by a fresh session that wrote none of the fixes, before 2026-11-29 23:00 UTC; it does not
      lift the general Fable hold. 5e236e34 and its four workers neither brief nor run it. It
      also covers `210/640` (the `DP17` leftover), which lands first.
      💬 **When it runs, his answer 2026-11-26 ~08:45 UTC (session a2aeebc8, `atelier-51`,
      AskUserQuestion).** First his words, verbatim, correcting that session's close, which had
      called this review a step before the drain: *"I have already ruled that we are not waiting
      for this review to complete before we use the code at the next drain. However I have also
      approved a review, but I worry that we are stuck in a loop of review - fix --review -- fix
      without proof of actual failures i.e. risks rather than issues"*. Asked when it runs and when
      a finding is fixed from now on, his typed answer, verbatim: *"run it as part of the drain"*.
      So this pass runs in the 2026-11-29 drain, among its other passes; it gates nothing. Its brief
      is owed before the drain, by a session that wrote none of the fixes. His concern about fixing
      risks before an actual failure is recorded here; the rule for when a finding is fixed was
      not answered, so the verdict's findings go to him as before.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code and doctrine re-check, per `method/REVIEW.md` rule 4: each of
      `DP1`–`DP21` against its fix, and what the fixes changed besides.
      *Delta, scoped to paths:* `instruments/ccfleet`, `instruments/test_ccfleet.py`,
      `instruments/test_ccfleet_dp.py`, `instruments/man/ccfleet.1`,
      `instruments/fixtures/review_queue_reference.py`, `tools/modelguard.py`,
      `tools/test_modelguard.py`, `tools/fixtures/claude-help-2.1.302.txt`, `tools/README.md`,
      `tools/pointerscan.py`, `tools/test_pointerscan.py`, `tools/test_subject_skills.py`,
      `tools/test_work_run_single_source.py`, `skills/**`, `docs/method/REVIEW.md`,
      `CHANGELOG.md`, and for `210/640` also `skills/review/run.md` and `docs/roadmap/210-*/640-*`:
      every commit on `main` after `c0f6501b` up to and including the commit that closes
      `210/640`.
      *Intent records:*
      [`../210-instruments-open-features/640-a-dry-drain-tells-a-queue-refusal-from-a-failure.md`](../210-instruments-open-features/640-a-dry-drain-tells-a-queue-refusal-from-a-failure.md),
      [`../210-instruments-open-features/630-fix-ccfleet-modelguard-and-the-review-skills-dp1-dp21.md`](../210-instruments-open-features/630-fix-ccfleet-modelguard-and-the-review-skills-dp1-dp21.md);
      the findings:
      [`../../reviews/2026-11-25-1920-dv-pk-fixes-recheck-cold.md`](../../reviews/2026-11-25-1920-dv-pk-fixes-recheck-cold.md).
      🔒 CLAIMED 2026-11-26T10:37Z (claimed 2026-11-26-1037, wt: brief-160-1870-1037) by headless
      session 664efda7 (`atelier-fc`, Opus 5.5), started by principal-opened session a2aeebc8
      (`atelier-51`, Opus 5.5) at the principal's pick, for brief-writing only: the brief and its
      held-back sibling, no pass run. Neither session wrote any part of the delta.
