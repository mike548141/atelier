# Session — the guard governance frame, and a ruling Mike put back on the table

- **Date:** 2026-08-02, 2340 UTC
- **Model:** Opus 5 (1M context), inline on `main`
- **Ask:** record an open action to re-think the block-vs-advise model from
  base, and queue a cold pass on the origin problem before any design

## What happened

Mike returned to E6d's escalate-only ruling — impact may raise a finding's
response, never lower it — and said that on further thought he is not sure it
was the right call. He was explicit about the handling: **keep the ruling as it
stands**, record an open action to re-think the idea from the beginning, and
start with a cold Fable reviewer of the origin problem and possible solutions.

He then gave a finer decomposition than the one E6d encodes, and a list of
concepts that turned out to be a governance model rather than a set of notes.

## What is actually new here

**The three-term split.** E6d tiers on confidence × impact. Mike separates
identification-confidence from the *probability* of harm and the *impact* of
harm, given the identification is true. E6d collapses the last two. The
distinction is real: a correctly-identified credential can carry low probability
of harm — already rotated, expired, scoped to nothing — which is a different
question from how bad the harm would be.

**The frame.** DRY for policy-as-code; a child cannot reduce a shared guard but
may reason about exclusions and acceptance; declare acceptance or deferment;
report a false positive; resolve vs scope vs soften; and the side-stepping
family — a guard not wired, overruled, or ignored. Six items already open on
this board are instances of it: the repo-local seam's zero adopters, C2's
seventeen advisories, E1–E4's ad-hoc false-positive discoveries, Track A's
scope fail-opens, C4's unobserved `--no-verify`, and the advisory that never
expires. Nobody had named the class they share.

## Honest notes

**None of the account below is in the queued pointer.** The pointer is refs
only, per this file's ceiling and the third instance of that breach recorded on
2026-07-28.

- **No candidate model is written into the roadmap entry, deliberately.** Mike
  asked for the review to run on the origin problem *and possible solutions*,
  which is an invitation to sketch. Sketching would steer the pass — the exact
  breach this repo has now recorded three times and funded a forcing function
  against. The solution space is left to the reviewer; the entry states the
  problem and the vocabulary and stops.
- **The frame is Mike's, and the mapping is mine.** He named the concepts; the
  claim that six existing roadmap items are instances of them is an agent's
  synthesis and is labelled as such in the entry. If the mapping is wrong it is
  wrong in a way that makes the frame look better-grounded than it is, which is
  the failure direction worth naming.
- **A prior ruling of his is now doubted, and the doubt is the useful signal.**
  The E6 intent pass's own EI3 had already declined to pre-rule the matrix
  shape, calling it a proposal owed to Mike at build pickup. His doubt and the
  reviewer's reservation landed on the same spot independently, which is
  better evidence that the spot is soft than either alone.
- **Unswept, and carried forward for the third time:** whether `leakscan`
  reaches the personal-data half of Mike's stated intent as `secretscan`
  reaches the credential half. Flagged 2026-07-29, endorsed as real open work
  by the E6 intent pass, still not done.

## State at close

Records-only; nothing built, nothing reverted. E6d stands unchanged. F1 is
open and its cold pass queued. Batches 2 and 3 of the verdict walk-through
remain unstarted.
