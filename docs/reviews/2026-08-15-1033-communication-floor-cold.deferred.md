# Deferred — the communication floor cold pass

*Sibling of `2026-08-15-1033-communication-floor-cold.md`. Open only after the
reviewer's own findings are durably written (REVIEW.md rule 1). Fold in below
the verdict and delete this file when the verdict lands.*

## References withheld from the brief

- **Intent records:** `docs/sessions/2026-08-09-0848-communication-enforced.md`
  (the build, the measurement, the ruling on the reply-plane numbers, and the
  P5 addendum in `docs/SESSIONS.md` at 1012 UTC) and
  `docs/sessions/2026-08-10-0036-plainscan-repo-plane-rescope.md` (the
  rescope's ruling and delivery). Their one-line entries sit in
  `docs/SESSIONS.md`.
- **The queue pointers:**
  `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/300-generalise-the-finding-don-t-just-fix-this-doc.md`
  and the rescope pointer in that section's `README.md` (§ *COMMUNICATION.md
  enforced — the first census finding, worked*). The section narrative around
  them is the author's account of the aim, the measurement, and P5.
- **Neighbouring open items** (the author's own follow-ups — read as the
  author's account, not settled scope): the flaky Stop-hook tests
  (`docs/roadmap/120-…/010-…`), the repo-plane numbers still unruled
  (`020-…/260-…`), *watch the live hook for two failure modes*
  (`020-…/280-…`), and *carry P5's finding into part (b)* (`020-…/270-…`).
- **Prior verdicts** — reconcile only, never anchor:
  `docs/reviews/2026-07-12-communication.md` (the doctrine's first cold pass;
  its enforcement clause dates from that cycle) and
  `docs/ROADMAP-DONE.md` § *The communication floor*.

## The brief-writer's seeded questions

Written by a non-author cold session from the delta alone. A floor, never a
fence — the reviewer's own findings come first.

1. **The rescope's exclusion list versus the doctrine's words.**
   `RECORDS_GLOBS` names three paths. The doctrine says records are excluded
   because they are "append-only history written for the next session's
   agent". Which other files in this repo meet that description and are not
   excluded (`docs/reviews/` verdicts? `docs/decisions/`?), and which excluded
   file does the principal in fact read (`SESSIONS.md`'s tail is in the
   onramp order)? Is the list drawn on the stated ground, or on the three
   files that carried the most findings?
2. **The correction's own claim about itself.** The rewritten clause says
   "anything a machine can decide without judgement … is checkable". P3's
   35-word (repo) and 45-word (reply) caps are house calls with no published
   authority. Is a number the house picked "decidable without judgement", and
   does the doctrine own that honestly at the point of use?
3. **Fail-open on the principal's reading surface.** Every other gate fails
   closed. The hook fails open with a stated trade. Test the trade's edge:
   what fails it open in practice (engine path missing, `ATELIER_TOOLS`
   unset, Python 3.9 vs the repo's Python), how would anyone know it had
   failed open, and does the two-failure-modes follow-up cover this?
4. **The state file.** `~/.claude/.plain-reply-state.json` with a six-hour
   TTL, keyed by session id, was shared with the running install and across
   tests until `b879b02`. What does it hold, is any reply text persisted in
   it, and does the give-up path let an unreadable reply through silently
   after N blocks — the exact defect class the hook exists to stop?
5. **The tally as evidence.** 7,817 → 4,440 is the rescope's headline. Both
   numbers are advisory findings on a warn-only plane. Does removing 3,377
   warnings nobody was reading change anything the principal experiences,
   and is the number in the doctrine text a measurement or an ornament?
6. **The recitation on the repo plane.** `beaf240` capped the recitation and
   kept the tally. On the ci plane the offending line is printed into a
   public Actions log. Is that a leak path for a private repo's prose under
   the same registry, and does the cap bound it?
7. **The flake.** Two Stop-hook tests were flaky in the full-suite run and
   passed alone; the state-file override was the fix. Is the flake gone at
   HEAD (run the suite several times), and did the fix remove the cause or
   the symptom?
