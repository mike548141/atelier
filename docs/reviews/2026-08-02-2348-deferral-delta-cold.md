# Cold pass — the deferral delta (`3acf7d2`)

- **Subject** — the rewrite of the review-deferral mechanism: `method/REVIEW.md`
  rules 1–2 and lifecycle steps 1/3 (deferred material moves from a
  below-the-divider section to a sibling `.deferred.md`, folded back at
  verdict), `skills/review-brief/SKILL.md`, the reviews template README,
  `tools/reviewscan.py` + `tools/test_reviewscan.py` (the mechanical half),
  and the registry `why` in `tools/floor.py`. Landed `3acf7d2`, 2026-07-29,
  by the 1418 session (Opus 5). Built, shipped, floor-wired.
- **Type** — self-authored doctrine plus its enforcing validator: rule-4
  class at its purest — this delta rewrites the very rules that govern how
  this review is being run.
- **Scope** — the `3acf7d2` diff and the six surfaces at HEAD; the doctrine
  argument itself (is the atomic-reading diagnosis right, is the sibling-file
  cure sound); the validator's actual bite; the fold-back lifecycle.
- **Spawn provenance** — rule 4: brief written by the taker, a Fable session
  Mike started 2026-08-02 and pointed at the queue; the author session
  neither started nor instructed it. Cold from the refs-only pointer; the
  shared intent record stays unopened until all four verdicts are committed.
  Caveat as disclosed in the two sibling verdicts: a sweep surfaced the
  author's `SESSIONS.md` index entry mid-pass-1, which includes an account of
  this delta (the unfollowable-rule diagnosis, the SL2 side-channel history,
  the deliberate no-lint-on-fold-back choice, "verified against all 76
  briefs", "driven live red-then-green"). Each exposed claim is treated as an
  assertion to attack. One structural advantage: this session has *operated
  under* the delta all day — the brief/verdict cycle now running is a live
  exercise of the rule under review.
- **Load-bearing assumptions to challenge**
  1. The diagnosis: the old below-the-divider deferral was *unfollowable*
     (reading is atomic), not merely unfollowed — and the sibling-file cure
     actually changes that, rather than moving the temptation one `ls` away.
  2. The honesty boundary: the doctrine claims the split makes early exposure
     "a deliberate act that leaves a trace" and only a context partition is
     structural — is that stated everywhere the mechanism is described, or
     does any surface still overclaim?
  3. The validator bites on the author at write time: a brief with a deferred
     section and no verdict below it reds; correct behaviour (fold-back after
     verdict; a verdict-bearing brief) stays green; the claimed
     red-then-green proof reproduces at HEAD.
  4. The no-lint-on-fold-back choice (reviewscan does not police that the
     sibling was folded in) does not leave a silent hole: an unfolded
     `.deferred.md` orphan after close would violate the one-file-at-rest
     rule with nothing watching.
  5. The six surfaces agree — no seventh surface still teaches the
     below-the-divider form.
- **Grounding to re-run** — reviewscan selftest + suite; a hand-built brief
  driven red (deferred section, no verdict) then green; the orphan case; the
  76-brief corpus claim re-swept at HEAD.
- **Non-goals** — the recurrence-ladder PROPAGATION sections (own pass);
  publishscan (own pass); rule 4's spawn criterion itself (predates this
  delta; in scope only where the delta's edits touched its wording).
- **Security scanner** — `/security-review` cannot reach a landed
  markdown+python delta with no pending diff; discharged on those grounds.
  The security lens runs manually — this delta's surface *is* an
  information-flow control (what a reviewer may read when), so lens 4 runs at
  design altitude on the flow itself, plus code altitude on the validator.
