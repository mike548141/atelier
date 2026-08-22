# 2026-08-22 · 0026 UTC · The pointing-up cold pass, run — upheld with conditions

**Tier:** Fable. **Worktree:** `pointing-up-cold-0822`.
**Commission:** Mike's standing prompt, *"do any reviews and fable dependent
work."* This session ran docker-heap's log-target cold pass first (recorded in
that repo's log), then took `310/050` — the one queued pointer with an unrun
brief — as the criterion-passing session the brief was waiting for: author of
neither the delta (`f9eda42`, 2026-08-18) nor the brief (2026-08-21), started
and instructed by neither, tier checked at selection, no orchestrator.

## The verdict

**UPHELD-WITH-CONDITIONS** — appended below the brief's `---` in
`docs/reviews/2026-08-21-0820-pointing-up-cold.md`, deferred sibling folded
and deleted per the lifecycle. The route is sound and already exercised as
designed (section `320` is the live proof); the block fixes are byte-honest
and propagating; the ten-child count re-derived exactly. Five findings,
none applied (rule 3 — the ruling round is Mike's):

- **PU-1 · MAJOR — the corrected rule still prescribes a path-blind check.**
  `CONCURRENCY.md` § *The trigger* prescribes `git diff --cached -U0 | grep
  '^@@'` two sentences before this delta's own clause that "the paths it
  shows that you never staged are the point". The pipe shows **no paths** —
  demonstrated live with an alien staged file whose entire trace is an
  anonymous `@@ -0,0 +1 @@`. The stamped block (plain `git diff --cached`)
  is now more correct than its canonical source — the exact inversion the
  section teaches against. The confusion is in the author's model, not a
  typo: the intent session record asserts the pipe "covers precisely that
  case" while the section README states the command without the pipe.
  Claim 1's "the house had no gap" therefore overreaches: coverage in
  principle, obscured in operation. Item `030`'s shed note repeats it.
- **PU-2 · MODERATE — the anonymising veil is defeated by its own section.**
  § *The instance* says "a private child"; item `040`, same section, same
  commit, quotes Mike naming `cbom` and the revert. One hop joins them, in
  the doctrine that teaches "carry the class, never the repo". The naming
  is Mike's own word, so this is framed as his ruling to make — keep the
  naming and drop the veil, or scrub the linkage — not a leak to attribute.
- **PU-3 · MODERATE** — route step 1 is machine-shaped: the live exercise
  used the channel (child sends, parent files), the text describes only the
  direct write, and a child with neither a sibling checkout nor a channel
  has no route at all. Three shapes deserve a sentence each.
- **PU-4 · minor** — "self-removing" is a hope until `020` lands; the
  section's closing honesty doesn't reach the word doing the work in step 3.
- **PU-5 · minor** — `pins.py` run from a worktree reported "1 of 1 not
  current" with a silently wrong CWD-relative denominator, tripped by this
  pass's own grounding; `floorfleet.py` from the same directory was correct.

## Discipline notes, stated against myself

- **Early exposure, disclosed in the verdict:** the `.deferred.md` sibling
  was read at queue triage, before the item was taken — in the same batch
  read that opened the brief. Findings landing on seeded angles are marked
  `[seeded angle]` in the verdict; the pass does not claim independence
  from the seeded questions.
- What the exposure did **not** touch: the intent records and the prior
  verdicts stayed closed until the findings were durably committed
  (`49d326e`), and PU-1 — the pass's one MAJOR — sits on no seeded angle.
- Verification ran where the claims lived: the fleet sweep by hand across
  every sibling's `CLAUDE.md` (ten at the delta's date — seven still
  defective at 2026-08-22, `faves` cleared 2026-08-18, `cbom` and `docker-heap`
  2026-08-21, both clearing phrase **and** pointer), the pre-fix template
  at `f9eda42^` for byte-honesty, the `-U0` pipe in a throwaway repo, the
  whose-rule test against three real estate lessons, and the child's own
  history for the incident's outline (existence, not content — its lane).

## What is owed, and by whom

⏳ **The ruling round is Mike's**: PU-1 and PU-2 are the conditions; PU-3,
PU-4 and PU-5 are backlog-shaped. Item `040` (the cbom revert) stays
blocked exactly as he sequenced it — on this cycle closing, which is now
the ruling round, not the pass. Applying any decided finding to doctrine is
its own edit and, per REVIEW.md's application rules, earns its own pass by
a hand that authored neither the doctrine nor this verdict.
