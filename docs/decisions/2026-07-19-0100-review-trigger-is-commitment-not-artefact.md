# The review trigger is commitment, not artefact — fix the framing at source

**Status**: draft • **Date**: 2026-07-19

**review**: ⏳ queued — extends the open cycle on
`2026-07-18-0820-review-the-design-not-only-the-build.md` (`30c9cd9`), whose
cold pass has not yet run. Self-authored doctrine, and this delta's author is
also the prior delta's applier ⇒ REVIEW rule 4 binds: pointer queued, **no brief
written**, the non-author taker writes it and reviews both deltas as one.

## Context

The 2026-07-18 change (above) diagnosed the defect correctly — every formulation
of the review-scope rule was phrased around *a change*, grammar that presupposes
the work already exists, so an agent holding a design never saw itself in the
text. Then it fixed the diagnosis in the wrong place.

The principal's steer, 2026-07-19:

> "We should fix the source of the problem upstream rather than adding more and
> more mitigations downstream to mitigate the problem."

Two findings from a sweep of `method/` and `build/templates/` made the case
concrete:

**1. The correction never reached the artefacts that carry it.** The amendment
landed in `method/REVIEW.md` only. `build/templates/docs/reviews/README.md` —
the file `create-repo` stamps into every child repo, and the one an agent
actually reads at the moment it decides whether to queue a review — still
carried a trigger list that was 3-for-3 diff-shaped, and still affirmatively
exempted *"a doc line"* as not review-worthy. That template is named in
`REVIEW.md` as one of the three places the correct rule "already sat" when the
`ros` session broke it on 2026-07-18. It was not the correct rule. It was the
broken formulation, propagating by template into every repo in the fleet.

**2. That file was an unmarked fork, and that is the real upstream defect.**
`templates/CLAUDE.md` carries an explicit header — *"this is a stamped copy, not <!-- pathscan:allow: record shorthand for docs/build/templates/, kept verbatim in an accepted record -->
a second source"* — naming `PROPAGATION.md` as canonical. The reviews template
carried no such marker. It pointed up for the *lifecycle* while silently
restating the *trigger* and the *brief format* as if they were its own. So it
was a second source, unmarked, free to drift — and it did. This is precisely the
N-copies shape `PROPAGATION.md` rejects ("rebuilds the divergence-by-neglect
problem DRY forbids"), reproduced inside the doctrine that forbids it.

The tell that the first fix was downstream: correcting the grammar would have
required patching five separate locations, and the *next* framing correction
would require five more.

## Decision

Fix the trigger at its source, then make the downstream copies point at it.

1. **Re-key the trigger on commitment, not artefact** (`method/REVIEW.md`,
   *Whether work earns a review at all*). The question becomes *what will come
   to rest on this once it is trusted* — which parses identically whether the
   reader holds a paragraph, a plan, or a patch. The heading loses "a change".
   This is the upstream fix: a design-holder is now inside the grammar at the
   point of asking, rather than being rescued by a later section.

2. **Shrink the downstream explanation.** The *Review the design* section's
   "why the framing was the trap" paragraph existed to rescue a reader the
   previous wording had already turned away. With the trigger fixed, it states
   the lifecycle claim and hands the correction upstream. It also now carries
   the general rule, which is the transferable part: *when a written rule keeps
   being broken, suspect its framing before its enforcement — restating it
   louder assumes non-compliance, where checking the grammar asks whether the
   rule was ever findable from where the reader stood.*

3. **Convert the reviews template from fork to pointer.** It gains the
   stamped-copy header `templates/CLAUDE.md` already uses, naming <!-- pathscan:allow: record shorthand for docs/build/templates/, kept verbatim in an accepted record -->
   `method/REVIEW.md` canonical and recording *why* — with the 2026-07-18 drift
   as the worked example. Its trigger becomes the one commitment question plus a
   thin floor; calibration is explicitly the parent's call. The brief format is
   made fillable by work that isn't built yet (`Build` → `Subject`; `Scope`
   points at a design record where no diff exists; `Real-world check` →
   `Grounding`, which for a design asks what would have to be true and how to
   check it cheaply). The "trivial edits" carve-out keeps its point but loses
   *"a doc line"*, and gains the opposite: prose is not routine by virtue of
   being prose.

4. **Follow the noun where it co-owns.** `MODEL-ECONOMICS.md`'s ceremony
   proportionality and `templates/CONTRIBUTING.md`'s review line are re-nouned <!-- pathscan:allow: record shorthand for docs/build/templates/, kept verbatim in an accepted record -->
   and point at `REVIEW.md` for the trigger rather than implying their own.

## Rejected

- **Patch the grammar in all five places.** The option on the table before the
  principal's steer. It is the mitigation-stacking the steer names: five copies
  corrected, five copies still free to drift, and no reason the sixth divergence
  would be caught any faster than this one was (four days, and only because a
  sweep went looking).
- **Delete the *Review the design* section as now-redundant.** Rejected: it
  carries the principal's ruling, two grounded incidents, and the structural
  review-line remedy. Fixing the trigger makes it shorter, not unnecessary.
- **Land it on `main` alongside the in-flight session.** Rejected on discovery:
  another session held staged changes to `ROADMAP*`, `SESSIONS.md` and
  `tools/sizescan.py` mid-turn. Moved to worktree
  `atelier-review-trigger-commitment` per `CONCURRENCY.md`.

## Consequences

- The next framing correction to the review trigger propagates by pin bump
  instead of by a five-file sweep. That is the whole return on this change.
- The reviews template now *narrows nothing and contradicts nothing* — it
  compresses. Adopters who diverge from it will diverge visibly, because the
  header says what it is.
- **Not done, and owed:** the structural remedy the 2026-07-18 change promised —
  every durable design record carrying a `review:` line — still has no artefact.
  No ADR template, decisions README, or ROADMAP template has the field, so the
  templates continue to manufacture the blank the rule declares to be the bug.
  This record carries the line by hand (top of file) as the worked example; the
  template change is queued, not made, to keep this delta reviewable as one
  thing.
- **Also owed:** the `⏳` ROADMAP entry for the 2026-07-18 cycle needs its delta
  extended to name these files, so the cold reviewer sees one delta rather than
  two. Deliberately not done in this branch — the queue is edited in place on
  `main` (`CONCURRENCY.md` § Claiming work) and `main` was mid-commit in another
  session.

## Addendum (2026-07-19) — the ros-incident attribution corrected

The cold pass (F4, ruled fixed by the principal) disproves one strand of
§Context: the incident repo has **never carried** `docs/reviews/README.md`, so <!-- pathscan:allow: the sentence says the repo has never carried this file — the scanner has no negation axis -->
the stamped template cannot have misled the 2026-07-18 session — REVIEW.md's
"three places" are the repo's own review policy, REVIEW.md itself, and session
memory (the 2026-07-18 intent record states them correctly). The drifted-fork
finding stands for the children that *do* carry the file, and the fork→pointer
conversion stands with it; what falls is only the causal embellishment ("the
one an agent actually reads… the reason the amendment never reached the
fleet"), which `4c17f59`'s immutable commit message also carries.
