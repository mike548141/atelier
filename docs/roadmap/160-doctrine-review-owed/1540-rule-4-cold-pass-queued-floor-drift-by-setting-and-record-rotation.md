- [ ] ⏳ **Rule-4 cold pass queued: the floor's drift check finds atelier by
      the hooks' tools setting, never `../` (`320/180`), and a reading cost,
      never a length, owes the session index a rotation (`115/330`).** The
      authoring session (queue run 78ca9153, Opus 5.5, principal-opened,
      2026-11-16 UTC, which dispatched the worker that wrote it) queues this and
      does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection; the
      pass waits for his explicit permission for Fable work.
      *Pass type:* doctrine cold pass, per `method/REVIEW.md` rule 4; the floor
      region is copied verbatim into every child.
      *Delta, scoped to paths:* `docs/method/PROPAGATION.md` (point 4 and the
      floor's *Source & drift* bullet), `docs/build/templates/CLAUDE.md`,
      `skills/create-repo/SKILL.md`, `tools/README.md`, `tools/test_estate.py`,
      `CHANGELOG.md`, and `docs/method/RECORD.md` § *The session log*: the
      commit that closes `320/180`, on `main`.
      *What to test hardest:* the command now depends on `hooks.atelierTools`
      (or `$ATELIER_TOOLS`) being set, measured absolute in all 22 children on
      2026-11-16; with it unset git fails loud on `/`, which must never read as
      current; whether `ATELIER_ESTATE_ROOT`, rejected here as unset
      everywhere, was the better key; the rotation trigger is the house's
      reading, not a ruling, and must not smuggle back a size limit.
