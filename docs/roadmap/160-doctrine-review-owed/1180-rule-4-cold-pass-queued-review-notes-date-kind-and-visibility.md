- [ ] 🎯 **Rule-4 cold pass queued: held-back review notes leave the shared
      scratch (`160/380`), a dated rule carries a readable kind (`160/450`),
      and a repo declares its visibility (`260/050`).** The authoring session
      (a principal-opened Opus 5.5 queue run, session 722ac2e2, 2026-11-09, in
      its ruling round, which dispatched the Sonnet worker that wrote them)
      queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code and doctrine cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `docs/method/CONCURRENCY.md`,
      `docs/method/REVIEW.md`, `docs/method/GUARDS.md`,
      `docs/method/PROPAGATION.md`, `docs/build/REPO-STANDARD.md`,
      `docs/build/templates/CONTRIBUTING.md`, `skills/review-brief/SKILL.md`,
      `tools/floor.py`, `tools/floorfleet.py`, `tools/coldsweep.py`, their
      tests, `tools/README.md`, `.atelier-floor.json`, `CHANGELOG.md` — the
      commits that close those three items, on `main`, 2026-11-09.
      *Questions worth the pass's time:* whether a reviewer can still reach
      held-back notes; whether an unlabelled date read as a mandate strands
      a child; whether the cross-check can pass while a repo is public.
      *Intent record:* the three items named above.
      *Brief:*
      `docs/reviews/2026-11-09-0153-review-notes-date-kind-and-visibility-cold.md`,
      written 2026-11-09 UTC by session `d16dc612`, a headless Opus 5.5
      brief-writer started by `74f2b8cd` (neither may run it); its
      held-back sibling holds one pointer block, 3 questions and 2
      facts. *Size:* large. The pass waits for his approval of Fable.
      🔒 CLAIMED 2026-11-16T08:16Z by headless orchestrator session (Opus 5.5, a rule-4 off-tier
      orchestrator: it holds the context partition, forms no finding and writes no
      severity), started by drain session 1e053526 (Opus 5.5) under the principal's API-credit
      drain order of 2026-11-16, verbatim: *"I want to use things other than my weekly budget
      to clear as many fable reviews as possible like using fable drain. I thought we could
      start by using up all the API credits I have."* That order is the approval of Fable this
      item waits for. Reviewer: a fresh Fable 5.1 session, tier checked at selection; not
      started or instructed by any barred session (722ac2e2 and its workers, d16dc612,
      74f2b8cd). Sibling held out of the tree until act 1 is committed.
      ✅ PASS RAN 2026-11-16 (act 1 `70359809`, reconcile and fold after it), Fable 5.1
      reviewer under the headless orchestrator above: **PASS-WITH-FINDINGS**, 0 MAJOR ·
      3 MODERATE · 5 minor · 2 note (`RNV1`–`RNV10`); whole suite 3,134 tests OK. No MAJOR
      stands. Verdict, reconcile, folded sibling and review log are in the brief.
      🎯 *Owed to the principal (rule 3: every finding is his; nothing applied):*
      `RNV2` (MODERATE) is a real ask: four dated advisories across the fleet carry no kind,
      and the new rule reads an unlabelled date as a mandate, though the one date class he
      ruled on (C1b) is a default. Options: (a) he labels each of the four (one item listing
      them with origin); (b) until labelled, the floor says "kind not recorded" with no
      mandate reading; (c) keep the mandate reading only for dates not C1b-derived.
      Reviewer's counsel: (a), with (b) or (c) meanwhile, his call which. `RNV1` (MODERATE):
      the CI visibility check is handed no token, so its live read is dead for private
      repos; counsel wires `GITHUB_TOKEN` into the reusable floor step and names the
      answer's source. `RNV3` (MODERATE): the fleet board does not read `visibility`
      (12 of 22 repos undeclared, unseen); counsel teaches `floorfleet.py` the key.
      Minors `RNV4`–`RNV8` and notes `RNV9`–`RNV10` are one-line fixes listed in the brief's
      follow-up checklist; bulk approval fits them. *Routing:* fixes land in atelier
      (`tools/floor.py`, `tools/floorfleet.py`, `.github/workflows/floor.yml`,
      `docs/method/GUARDS.md`, `create-repo`); a change to the floor workflow reaches every
      child's next CI run.
