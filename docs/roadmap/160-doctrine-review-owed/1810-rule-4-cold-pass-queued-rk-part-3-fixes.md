- [x] 🎯 **Rule-4 cold pass queued: the RK part-3 fixes to `ccfleet`, `modelguard`
      and the subject skills (`210/600` part 3).** The fixes for `RK1`, `RK3`, `RK4`,
      `RK6`–`RK29` of the `160/1790` verdict change a tool that runs paid passes
      unattended, the hook every session's launches meet, and the grants every
      `/atelier:` command carries, so they earn their own pass. The authoring session
      (0ee74059, `atelier-c3`, Opus 5.5, principal-opened by `/atelier:work run`,
      whose four Opus workers wrote the fixes) queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection; the pass
      waits for his explicit permission for Fable work (the one pass he picked on
      `160/1790` is `160/1800`, the drain path only).
      *Pass type:* code and doctrine cold pass, per `method/REVIEW.md` rule 4, by a
      session that wrote none of the fixes.
      *Delta, scoped to paths:* `instruments/ccfleet`, `instruments/test_ccfleet.py`,
      `instruments/man/ccfleet.1`, `instruments/ccfleet.example.json`,
      `instruments/fixtures/review_queue_reference.py`, `tools/modelguard.py`,
      `tools/test_modelguard.py`, `skills/**`, `.claude-plugin/*`, `CHANGELOG.md`,
      `docs/method/MECHANISMS.md`, `tools/test_subject_skills.py`,
      `tools/test_session_close_single_source.py`: the commits citing `210/600`, on
      `main`, after `a1cc5f2d`.
      *Intent record:*
      [`../210-instruments-open-features/600-fix-ccfleet-subject-skills-and-modelguard-rk1-rk29.md`](../210-instruments-open-features/600-fix-ccfleet-subject-skills-and-modelguard-rk1-rk29.md);
      the findings:
      [`../../reviews/2026-11-24-2141-ccfleet-recheck-and-subject-action-review-plan-cold.md`](../../reviews/2026-11-24-2141-ccfleet-recheck-and-subject-action-review-plan-cold.md).
      💬 **Answered 2026-11-25 ~05:40 UTC** (session 0ee74059, AskUserQuestion; an answer,
      not a ruling), his pick *"Approve one pass now"* (option text: *"One Fable pass on this
      week's budget, run by a fresh session soon, ahead of the drain. Spends weekly Fable
      budget now."*). Exactly that one pass plus its Opus brief, by a fresh session that wrote
      none of the fixes (0ee74059 and its workers may neither brief nor run it). It does not
      lift the general Fable hold.
      🔒 CLAIMED 2026-11-25T07:06Z (claimed 2026-11-25-0706, wt: brief-160-1810-0704) by
      headless session 075cdcd9 (`atelier-e0`, Opus 5.5), started by principal-opened
      session 14c2530d (`atelier-e7`, Opus 5.5). Scope: write the brief and its held-back
      sibling only; no pass run, no reviewer started or instructed.
      **Briefed 2026-11-25 UTC (session 075cdcd9, `atelier-e0`, Opus 5.5, started by
      14c2530d):** `docs/reviews/2026-11-25-0721-rk-part-3-fixes-ccfleet-modelguard-subject-skills-cold.md`,
      pinned at `6ddbead2`, finding prefix `PK`. It takes in every commit after `a1cc5f2d` on
      this item's paths, not only those citing `210/600`: `fc922383` (`modelguard`) and
      `9b4a8f8f` (the changelog) cite neither, and `f4360a79` (`210/610`, closed with no pass of
      its own) rewrote the instructions-file guard after this pointer was written; `a1cc5f2d`
      is read for context, under `160/1800`. The held-back sibling is user-local; the
      orchestrator is told where. The brief-writer formed no finding and does not start the
      pass, which stays `⏳` for one fresh Fable reviewer on the approval above.
      🔓 2026-11-25 UTC: session 075cdcd9 releases its brief-writing claim.
      💬 **Answered 2026-11-25 ~07:30 UTC** (session 14c2530d, AskUserQuestion; an answer, not a
      ruling), asked whether the unreviewed `f4360a79` (`210/610`) joins this pass, his pick
      *"Add it to the part-3 pass (Recommended)"* (option text: *"The part-3 review (the other
      approved pass, not yet started) widens to cover this change too. Benefit: reviewed before
      Monday, and that pass already covers ccfleet. Cost: that one Fable pass gets a bit bigger
      (about 300 changed lines). Still one pass."*). The brief already takes it in, so no
      widening was needed: still one pass.
      🔒 CLAIMED 2026-11-25T07:43Z (claimed 2026-11-25-0743, wt: atelier-e7-pk) by principal-opened session
      14c2530d (`atelier-e7`, Opus 5.5) for the one Fable pass. Off-tier orchestrator,
      disclosed: it holds the context partition, commits the records and releases the held-back
      sibling after act 1; it forms no finding and writes no severity. It authored no part of the
      delta and no part of the brief. The reviewer is one fresh Fable subagent.
      **Verdict 2026-11-25 UTC: PASS-WITH-FINDINGS, 0 MAJOR, 5 MODERATE, 12 minor, 4 notes**
      (`PK1` to `PK21`), in
      [`../../reviews/2026-11-25-0721-rk-part-3-fixes-ccfleet-modelguard-subject-skills-cold.md`](../../reviews/2026-11-25-0721-rk-part-3-fixes-ccfleet-modelguard-subject-skills-cold.md):
      one Fable reviewer under off-tier orchestrator 14c2530d, act 1 at `a247f7f0`, reconcile and
      folded sibling below it. It also reviews `f4360a79` (`210/610`), per his answer above. The
      live launches were NOT RUN (a synthetic config directory has no sign-in); the reviewer
      re-drove those claims by reading the installed CLI instead, and says so. Every finding is
      the principal's to rule; nothing is applied. The held copy of the sibling was deleted after
      the fold was checked.
      🔓 2026-11-25 UTC: session 14c2530d releases its claim.
      💬 **Answered 2026-11-25 UTC** (session 14c2530d, AskUserQuestion; an answer, not a
      ruling), on both verdicts' findings together: *"Fix all as advised (Recommended)"*. The
      fixes are queued as `210/620`.
