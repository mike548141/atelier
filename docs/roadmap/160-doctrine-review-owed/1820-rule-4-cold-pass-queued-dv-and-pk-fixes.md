- [ ] ⏳ **Rule-4 cold pass queued: the `DV` and `PK` fixes to `ccfleet`, the reference
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
