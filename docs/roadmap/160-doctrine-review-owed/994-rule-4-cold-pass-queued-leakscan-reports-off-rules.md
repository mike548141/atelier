- [ ] 🎯 **Rule-4 cold pass queued: leakscan's rules that are off report
      without blocking, and the narrowed EI6 asymmetry (`115/090`).** This
      is first-of-kind work on the personal-data boundary: a response tier
      in leakscan, and the doctrine sentence it narrows. So the authoring
      session (a principal-opened Opus 5.5 queue run, session 4c65083c,
      2026-11-03, which dispatched the Opus worker that wrote the code and
      the text) queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code and doctrine cold pass, per `method/REVIEW.md`
      rule 4.
      *Delta, scoped to paths:* `tools/leakscan.py`,
      `tools/test_leakscan.py`, `tools/leakscan.off-rules.design.md`,
      `tools/floor.py`, `tools/test_floor.py`, `tools/README.md`,
      `docs/method/SECRETS.md`, `CHANGELOG.md` (the commits that land
      `115/090`'s leakscan build, on `main`, 2026-11-03; widened by the
      commit that closes `115/370`, the same section's stale lead).
      *Intent records:*
      [`../115-guardrail-architecture-mike-commissioned/090-give-every-guard-a-second-dial-mike-s-2026-07.md`](../115-guardrail-architecture-mike-commissioned/090-give-every-guard-a-second-dial-mike-s-2026-07.md),
      [`../../reviews/2026-07-29-1243-e6-intent-cold.md`](../../reviews/2026-07-29-1243-e6-intent-cold.md).
      📝 BRIEF WRITTEN 2026-11-09 by session d4a0fcf3 (Opus 5.5, headless,
      started by coordinating session 74f2b8cd; neither authored this delta):
      `docs/reviews/2026-11-09-0207-leakscan-off-rules-cold.md`, with its
      `.deferred.md` sibling. Pass size: medium. Review NOT run: this pass
      waits for a criterion-passing cold Fable session and the principal's
      explicit permission for Fable work. Neither named session may run it.
      🔒 CLAIMED 2026-11-15T19:35Z UTC for the cold pass, in Mike's weekly Fable drain
      (his `/fable-drain` order, 2026-11-16 06:53 NZDT; approval lapses at the
      reset, 2026-11-15 23:00 UTC). Orchestrator: a headless Opus 5.5 session
      started by drain session 21a271a5, a rule-4 off-tier orchestrator that
      holds the context partition, forms no finding and writes no severity.
      Reviewer: Fable 5.1, tier checked at selection, spawned by that
      orchestrator. Neither is a barred session (d4a0fcf3, 74f2b8cd,
      4c65083c). The sibling is held out of the worktree until act 1 is
      committed. The item's "waits for the principal's explicit permission
      for Fable work" is met by that drain order.
      ✅ PASS RAN 2026-11-15T20:40Z UTC (Fable 5.1 reviewer, acts 1 and 2; act 1
      committed `b7cd9648` before the sibling opened; sibling folded into
      the brief). Verdict: **PASS-WITH-FINDINGS — 0 MAJOR · 1 MODERATE
      (LO1) · 3 minor (LO2, LO3, LO7) · 4 notes (LO4, LO5, LO6, LO8).** No
      standing MAJOR: the blocking set did not shrink, the pin holds and the
      exit code moved in no repository re-run. Verdict:
      `docs/reviews/2026-11-09-0207-leakscan-off-rules-cold.md`.
      🎯 Owed to Mike (rule 3: guard text is doctrine by function, so every
      finding is his to rule; nothing applied). Plain briefing: since this
      build, a repo that switches off one of leakscan's checks no longer
      hides the hits, it just stops them blocking. The rules on "lowering a
      check" say such a step needs a reason, an end date and a line in the
      fleet view, but still class switching a check off as "not a
      lowering", and the open question `020/170` was left undecided.
      LO1 (MODERATE): rule `020/170` with `--disable` named. Options: (a)
      treat it as a lowering, so it gets an end date and shows in the fleet
      view; (b) keep it a permanent, reasoned choice because the hits still
      report, and say so in the guard rules. Reviewer's counsel lists both;
      recommended (orchestrator's reading of the counsel, not a finding):
      (a), the stricter one, since it is the personal-data boundary.
      Then bulk-approve the small fixes: LO2 qualify one CHANGELOG line
      (or let `160/1420` carry it); LO3 add staged-plane and image-metadata
      tests for a disabled rule; LO7 assert every structural rule is
      pinned; LO4 pin the refusal wording; LO6 tidy a docstring; LO8 add a
      correcting line beside the wrong count (2,662 vs 2,652). LO5 needs
      no action. Routing: fixes go to a fresh atelier session after his
      word; LO1 to `020/170`.
