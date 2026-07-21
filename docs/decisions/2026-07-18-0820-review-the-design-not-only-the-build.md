# Review the design, not only the build

**Status**: draft • **Date**: 2026-07-18

## Context

The principal ruled (2026-07-18), after a `ros` session declined to queue a
review on the grounds that the work "was roadmap capture with no code":

> "Fable reviewers are just as much, if not more so, to test our thinking,
> assumptions, decisions and architecture. Not just code… reviewing things
> before we build them helps us reduce rework and improve the quality of the
> things we do build."

Two constraints forced the shape of the fix rather than the fix itself.

**1. The scope rule already existed, in three places, and still failed.**
`REVIEW.md` already made structural work and doctrine-by-function reviewable
and already named lens 1 (approach & assumptions) the most important lens. The
`ros` repo's own review policy carried an approach+assumptions clause. That
session's memory carried the 2026-07-15 correction verbatim — an incident where
a reviewer dismissed a committed-direction expansion as *"zero source code, so
nothing my verdict should have covered."* The session had all three and reached
for "no code, so no review" anyway. A fourth written copy would be the exact
category error `PROPAGATION.md` names: *a doctrine that is read is not a
doctrine that is complied with.*

**2. The gap was the framing, not the rule.** Every prior formulation is
phrased around *a change* — "whether a **change** earns a review", "match the
gate to the cost of being wrong". That grammar presupposes the work exists. An
agent holding a design rather than a diff finds every sentence shaped for the
diff and concludes the answer is no. The doctrine's framing encoded a
late-review default that its own lens 1 contradicts.

What was genuinely absent was the **timing/economics claim**: review as an
*input* to building, not only a gate after it.

## Decision

Add a section to `method/REVIEW.md` — *Review the design, not only the build —
the earliest review is the cheapest* — placed after the risk-calibration
section and before the inline-vs-batched section, since it answers **when in
the lifecycle** rather than by what mechanism. It states:

1. Review is an input to building. A wrong premise caught at design time costs
   a paragraph; caught after the build it costs the build and everything
   stacked on it. Lens 1 has the most to bite on *before* the code exists.
2. A captured feature, ratified design, or structural decision earns a review
   in its own right — reviewability is not conferred by containing code.
3. The framing trap is named explicitly, so a future reader understands why the
   rule failed despite being written.
4. **Enforcement is structural**: where a repo records design or direction
   durably, each record carries a review line — a queued pointer or an explicit
   `review: not warranted — <grounds>`. **Omission is the bug**, because a
   silent absence reads identically to nobody having considered it.

Risk calibration is unchanged: this widens *what* is reviewable and *when*,
never the ceremony. Most design records will honestly carry "not warranted".

## Rejected

- **Restating the scope rule more forcefully (a fourth copy).** The rule was
  present in three accessible places at the moment it was broken. More prose
  addressing a compliance failure is the costume, not the doctrine.
- **Leaving it to memory / per-repo instructions.** The `ros` session had it in
  memory. Memory is background context; it did not bind.
- **A mechanical hook or validator.** Considered and deferred, not rejected on
  merit: there is no reliable trigger for "an agent is about to decline a
  review", and a lint that demands a review line on every roadmap heading would
  fire on prose and be trained away. If the convention proves insufficient in
  practice, a per-repo lint on design-record sections is the next rung — a
  question for the reviewer of this delta.
- **Requiring a review of every design record.** Over-ceremony; the calibration
  rule already governs, and forcing briefs onto routine notes would crowd out
  the work. The requirement is a *stated judgement*, not a review.

## Consequences

- Declining a review becomes a visible act with recorded grounds — challengeable
  by a reviewer or the principal. A blank is not challengeable.
- Design-time review becomes the default position rather than an exception an
  agent must argue for, which is the rework reduction the principal asked for.
- Repos inheriting `method/` inherit the convention; each needs a place to put
  the review line (in `ros` this is the ROADMAP feature section).
- Cost is one line per design record, paid when the thought is cheapest.
- ⚠️ Residual risk, named not solved: the convention is still a *convention*.
  It fails the same way if an agent simply never writes the line — the
  improvement is that its absence is now legible in the artifact, where before
  it was indistinguishable from a considered decision.

## Provenance

Delta authored by Opus 4.8 (`ros` session 2026-07-18, the same session whose
failure grounds incident 2 — so the author is implicated in the case the
doctrine now cites). Self-authored doctrine ⇒ `REVIEW.md` rule 4: the author
queues a `⏳` pointer and writes no brief; a non-author spawner takes it.
The `ros`-side application of the same ruling is committed at `55d0d51`
(`CLAUDE.md` + ROADMAP review policy).

**Addendum 2026-07-19 (applied-batch pass, G3, discretionary):** Decision
bullet 4's "Enforcement is structural" was subsequently qualified in
`REVIEW.md` — structural in *intent*, still conventional in *fact* until the
record templates carry the `review:` field (cold-pass F6; the artefact item is
queued in the ROADMAP).

**Addendum 2026-07-21 (the artefact landed):** the Rejected section's deferred
question — a per-record lint as the next rung — was answered **yes** by the
0407 reviewer (F6) and is now built: the record templates carry the `review:`
field and `tools/reviewscan.py` reds a post-2026-07-21 decision record that
omits the line, scoped to decision records only (the roadmap-heading lint this
record rejected stays rejected). Deliberation and boundary in
`2026-07-21-0744-review-line-artefact.md`; `REVIEW.md`'s qualification is
narrowed to per-surface honesty accordingly. This record's Rejected section already carries that
honesty; this line saves a reader the inference.
