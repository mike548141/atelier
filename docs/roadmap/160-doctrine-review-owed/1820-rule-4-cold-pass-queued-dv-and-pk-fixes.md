- [ ] 🎯 **Rule-4 cold pass queued: the `DV` and `PK` fixes to `ccfleet`, the reference
      queue, `modelguard`, `pointerscan` and the review and close skills (`210/620`).** The
      one Fable re-check the principal approved on `210/620`, step C of `450/010` row 2.
      The authoring session (b04df0da, `atelier-f9`, Opus 5.5, principal-opened by
      `/atelier:work run`, whose three workers wrote the fixes) queues this and neither briefs
      nor takes it.
      *Tier:* Fable, the principal-named review tier, checked at selection. Approved: exactly
      this one pass plus its Opus brief, by a fresh session that wrote none of the fixes
      (`210/620`, his pick *"Before, plus re-check"*); it does not lift the general Fable hold.
      *Pass type:* code and doctrine re-check, per `method/REVIEW.md` rule 4: each of
      `DV1`–`DV11` and `PK1`–`PK21` against its fix, and what the fixes changed besides.
      *Delta, scoped to paths:* `instruments/ccfleet`, `instruments/test_ccfleet.py`,
      `instruments/man/ccfleet.1`, `instruments/ccfleet.example.json`,
      `instruments/fixtures/review_queue_reference.py`, `instruments/README.md`,
      `tools/modelguard.py`, `tools/test_modelguard.py`, `tools/pointerscan.py`,
      `tools/test_pointerscan.py`, `tools/README.md`, `skills/**`,
      `tools/test_subject_skills.py`, `tools/test_session_close_single_source.py`,
      `CHANGELOG.md`: every commit on `main` after `932a0185` up to and including the
      commit that lands this pointer.
      *Intent record:*
      [`../210-instruments-open-features/620-fix-ccfleet-and-the-review-skills-dv1-dv11-pk1-pk21.md`](../210-instruments-open-features/620-fix-ccfleet-and-the-review-skills-dv1-dv11-pk1-pk21.md);
      the findings:
      [`../../reviews/2026-11-25-0720-rk-drain-path-fixes-cold.md`](../../reviews/2026-11-25-0720-rk-drain-path-fixes-cold.md)
      and
      [`../../reviews/2026-11-25-0721-rk-part-3-fixes-ccfleet-modelguard-subject-skills-cold.md`](../../reviews/2026-11-25-0721-rk-part-3-fixes-ccfleet-modelguard-subject-skills-cold.md).
      🔒 CLAIMED 2026-11-25T19:20Z (claimed 2026-11-25-1920, wt: brief-160-1820-1915) by headless
      session 43d5be30 (`atelier-1d`, Opus 5.5), started by principal-opened session 01c055e5
      (Opus 5.5), for brief-writing only: the brief and its held-back sibling, no pass run.
      Neither session wrote any part of the delta; 01c055e5 orchestrates the pass once the brief
      lands and forms no finding.
      **Brief written 2026-11-25 UTC:**
      `docs/reviews/2026-11-25-1920-dv-pk-fixes-recheck-cold.md`, pinned at `6a44b08e`,
      finding prefix `DP`. Its held-back sibling (20 questions, 14 facts) is held
      user-local, outside the repo, every worktree and every scratchpad; the orchestrator
      is told where, never by the brief.
      🔓 2026-11-25T19:46Z: session 43d5be30 releases its claim. The pass is open for one fresh
      Fable reviewer under off-tier orchestrator 01c055e5, which forms no finding; `b04df0da`, its
      three workers and `43d5be30` are barred from running it.
      🔒 CLAIMED 2026-11-25T20:40Z (wt: atelier-4c-dp, branch `atelier-4c-dp-pass`) by
      principal-opened session 01c055e5 (`atelier-4c`, Opus 5.5), to run the pass. **Off-tier
      orchestrator, disclosed (rule 4):** it spawns one fresh Fable reviewer, holds the context
      partition, releases the held-back sibling after act 1 is committed and commits the records;
      it forms no finding and writes no severity. It wrote no part of the delta or the brief.
      **Verdict 2026-11-25 UTC: PASS-WITH-FINDINGS, 0 MAJOR, 5 MODERATE, 11 minor, 5 notes**
      (`DP1` to `DP21`), in
      [`../../reviews/2026-11-25-1920-dv-pk-fixes-recheck-cold.md`](../../reviews/2026-11-25-1920-dv-pk-fixes-recheck-cold.md):
      one Fable reviewer under off-tier orchestrator 01c055e5, act 1 at `785fa79e`, reconcile and
      folded sibling below it. Of the 32 earlier findings: 30 fixed, `DV10` partly fixed (`DP16`),
      `PK13` fixed with a regression beside it (`DP1`, `DP21`). The reviewer's counsel: the drain
      is safe to run from these commands, once the changelog's adopter actions and the private
      config points are made first. With no MAJOR, step C of `450/010` row 2 is met. Every
      finding is the principal's to rule; nothing is applied. The held copy of the sibling was
      deleted after the fold was checked byte for byte.
      🔓 2026-11-25 UTC: session 01c055e5 releases its claim.
      💬 **Answered 2026-11-25 ~21:45 UTC (session 01c055e5, AskUserQuestion)**, his pick on when
      to fix the findings: *"Fix all now, before Monday"*; then his ruling, verbatim, quoted in
      full on `210/630`: *"This code is ready to use for the drain so we can continue to switch
      over to it"*. Queued as `210/630`; step D of `450/010` row 2 goes ahead on this code.
