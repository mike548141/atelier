- [ ] 🎯 **Rule-4 cold pass queued: the exception-register design, redrafted
      on its failed pass's counsel (`160/650`, `110/100`).** The authoring session (a
      principal-opened Opus 5.5 queue run, session 722ac2e2, 2026-11-09, in
      its ruling round, which dispatched the worker that wrote it) queues
      this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      Best run after he answers the ADR's four open questions.
      *Pass type:* design cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:*
      `docs/decisions/2026-10-03-0641-the-exception-register.md`,
      `docs/decisions/README.md` — the file at HEAD on `main`, not the redraft
      commit alone: the ADR was reworked to one central file after the redraft
      (`c687e446` then `7c2beaea`, both 2026-11-09; `160/650`). Read the
      current file.
      *Questions worth the pass's time:* whether the both-forms transition
      really keeps every child green; whether the provenance record can be
      forged cheaply; whether XR1–XR16 are each closed as claimed.
      *Intent record:*
      [`650-rule-4-cold-pass-queued-exception-register-design.md`](650-rule-4-cold-pass-queued-exception-register-design.md).
      *Brief:*
      `docs/reviews/2026-11-09-0153-exception-register-redraft-cold.md`,
      written 2026-11-09 UTC by session `d16dc612`, a headless Opus 5.5
      brief-writer started by `74f2b8cd` (neither may run it); its
      held-back sibling holds one pointer block, 3 questions and 2
      facts. *Size:* large. The pass waits for his approval of Fable.
      2026-11-09: his four answers are in (`160/650`; the ADR's
      open-questions section), so the *best run after* note above is
      met.
      🔒 CLAIMED 2026-11-16T06:12Z by headless orchestrator session (Opus 5.5, a rule-4 off-tier
      orchestrator: it holds the context partition, forms no finding and writes no
      severity), started by drain session 1e053526 (Opus 5.5) under the principal's API-credit
      drain order of 2026-11-16, verbatim: *"I want to use things other than my weekly budget
      to clear as many fable reviews as possible like using fable drain. I thought we could
      start by using up all the API credits I have."* That order is the approval of Fable this
      item waits for. Reviewer: a fresh Fable 5.1 session, tier checked at selection; not
      started or instructed by any barred session (722ac2e2 and its workers, d16dc612,
      74f2b8cd). Sibling held out of the tree until act 1 is committed.
      ✅ PASS RAN 2026-11-16 UTC, Fable 5.1 reviewer spawned by the headless orchestrator: act 1
      `7076d6c3`, act 2 reconciled, sibling and review log folded into
      `docs/reviews/2026-11-09-0153-exception-register-redraft-cold.md`.
      Verdict: FAIL, 1 MAJOR, 2 MODERATE, 3 minor, 5 notes (ERD4 re-rated to a note at
      reconcile; ERD11 formed at reconcile). 13 of the 16 prior findings closed as claimed; the
      open edges left on XR2, XR4 and XR6 are ERD2, ERD3 and ERD1. Converging, not closed.
      Standing MAJOR: ERD1, the frozen-record `store` class turns about 330 marker lines in
      live record stores into an uncounted, rule-wide, directory-wide exemption, against his
      "only that string should be excluded". Design by function, so every finding is the
      principal's to rule (rule 3); nothing applied.
      🎯 Owed asks for the principal (plain briefing; one question, bulk-approvable):
      - ERD1 (MAJOR): the migration plan lets whole folders of records skip a check with no
        count, far wider than the one-line exceptions they replace. Options: (a) per-file
        entries at the exact string, written by the helper; (b) a folder entry with an expected
        count; (c) a folder entry that covers only files older than a set commit.
        Recommended: (a), the reviewer's counsel, as it keeps his "only that string".
      - ERD2 (MODERATE): "live", "superseded" and "retired" entries are never defined, so the
        stale check would block forever after any entry is replaced. Recommended: add the one
        paragraph the reviewer drafted.
      - ERD3 (MODERATE): whole-file entry kinds have no way to say which rules they cover.
        Recommended: define a loudly listed `*` rule for those kinds, or require a per-rule
        expected count.
      - Minors and notes ERD4–ERD11 (a fact fix, a parent-repo pointer form, a staleness check
        on commit, newline counting, trailing newline, Q1's two readings put with acceptance,
        a CHANGELOG entry, duplicate live entries flagged): recommended, approve the
        reviewer's counsel as a bundle with the three above.
      Routing: on his word, a fresh session revises the ADR
      `docs/decisions/2026-10-03-0641-the-exception-register.md`; a material revision of
      ERD1–ERD3 earns a further cold pass before he rules on acceptance.
