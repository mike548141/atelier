# Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-09-0126-ladder-floor-cold.md` (`REVIEW.md` rule 1). Written
2026-11-09 UTC by session `84e3aa7f`, the brief-writer, which authored none of the delta. Open this
only after act 1 is committed. Everything here is a floor, never a fence, and none of it is a
finding.

## The queue pointer's questions (author-written, verbatim)

> whether the passage contradicts any rung of the ladder or the >2 promotion rule; whether 'value
beats cost' is followable.

## The brief-writer's own questions

1. "A check not built is a decision with its reason recorded": recorded where, by whom, for the
rules that already exist?
2. `115/170`'s words answered a different question (capping guard work). Do they carry the weight
the passage rests on them?
3. Where else does the house state when a rule earns a check (`GUARDS.md`, `ECONOMICS.md`,
`PRINCIPLES.md`, a skill)? Sweep for mirrors (V3).
4. The passage says recurrence is "the usual way", while a sentence elsewhere states a threshold.
Compare wording, not intent.
5. The landing commit and the pointer commit are separate (`4458a157`, then `034ecd70`).

## What the brief-writer ran, and what it got

- `floor`: at c132cc1c: hook exit 0, ci exit 0. pathscan reports 3 findings, warn-only:
  docs/method/EVIDENCE.md:427, docs/method/session-open/session-open-prompt.md:13 and
  docs/method/session-open/template-history.md:10 (paths that do not exist from the repo root).
