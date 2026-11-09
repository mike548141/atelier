- [ ] ⏳ **Rule-4 cold pass queued: leakscan's rules that are off report
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
