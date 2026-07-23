# Billing state belongs to the marginal token, not the model

**Status**: draft • **Date**: 2026-07-23
**Review**: queued — the ⏳ pointer in `docs/ROADMAP.md` (economics rework,
rule-4 cold pass; this record is the intent record, delta `dadde1d`)

## Context

`ECONOMICS.md` opened on a two-pool split — a plan-included model builds, a
usage-billed model reviews — and the build-layer template hard-coded the
mapping ("Fable (usage-billed: real money)"). In July 2026 the provider moved
the capable model *into* the operator's subscription: included up to a capped
share of the weekly allowance, usage-billed past the cap, and drawing the
shared allowance down faster than other models. The two-pool binary was no
longer true, and — more importantly — it had let a billing fact masquerade as
the *reason* for the tier split, when the principal's position is that the
split is a risk argument that must survive any billing change.

Three principal rulings (Mike, 2026-07-23) set the shape:

1. On tier selection under capacity pressure: *"If we can use cheaper to
   operate models that is great in all situations, not just when the tank is
   empty. But we never decay the quality or integrity of the work because the
   tank is low, we either stop/delay the work or I choose to pay usage fees."*
2. On capability limits: a model finding work beyond its capability *"needs to
   fail noisily, not silently so another model can take up the work. Or all
   models failing/incapable coming to me."*
3. On the cheaper tiers: adopted the third seat — sub-agent fan-out on the
   cheapest tier that genuinely does the read, and a per-run trial of a
   stepped-down executor for routine, well-floored queue items.

## Decision

1. **Billing state is a property of the marginal token, not the model.** Three
   states — plan-included, plan-included-capped, usage-billed — read off the
   current plan, never off habit; plus **draw-down rate** as a first-class
   concept inside the plan pool.
2. **Risk assigns the seats; billing only prices them.** The capable-tier-
   reviews / workhorse-builds split is owned by the tiered-authority section
   (a risk argument) and survives billing changes; the match-model-to-the-job
   section prices the assignment.
3. **The cap is a stop-or-pay boundary, never a down-tier trigger.** Crossing
   into usage billing is spend beyond the plan (AUTONOMY's confirm floor): the
   session stops at a safe point, records, and hands the principal the
   delay-or-pay choice. Capacity is never an input to tier selection.
4. **Hand-ups are noisy and the ladder ends at the principal.** A model past
   its depth fails visibly — states what exceeded it, records, routes up
   (workhorse → capable tier → principal). Silent stalls and quietly degraded
   attempts are the forbidden failure mode.
5. **The third seat.** Fan-out sub-agents run on the cheapest tier that
   genuinely does the work, in every capacity state; the queue-run executor
   seat may step down a tier for routine, well-floored items, trialled per run
   and kept only on the floor's evidence.

## Consequences

- `docs/method/ECONOMICS.md`: pool sections rewritten (states + draw-down
  rate), self-check renamed to the marginal-cost self-check with two guards
  (dear-meter builds; silent cap-crossing), tiered-authority gains the two
  hard edges, the orchestrated-run split gains the third seat.
- `docs/build/templates/docs/ECONOMICS.md`: "Who does what" re-grounded
  (Fable plan-included/premium-draw/capped; Sonnet/Haiku seat; hand-up line)
  so children inherit the corrected floor.
- Cross-references to the old section name updated in `REVIEW.md` and
  `CONCURRENCY.md`.
- Estate-specific numbers (the plan's name, the cap share, prices) stay
  person-local in the operator's private estate-root repo, per this doctrine's
  own boundary; this record deliberately carries none of them.
- Self-authored doctrine ⇒ REVIEW rule 4: the cold review is queued as a `⏳`
  pointer for a non-author to take; these edits are not trusted until it
  closes.
