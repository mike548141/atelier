# Sibling to the ADR 0008 boundary-amendment cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-17-0955-adr-0008-boundary-amendment-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-17 UTC by the Opus brief-writer named in the brief's provenance; it
forms no finding. Fold this file in below the reconcile and delete it at phase 2.

## Intent and commissioning records

- Intent record: `docs/sessions/2026-10-16-0703-queue-run-after-the-sizescan-ruling.md` —
  **not opened by the brief-writer**.
- Commissioning board items (single grep lines seen, never read whole): `140/020` (ADR 0008's
  clause is now closer to true), the `140` section README (the platform half of AP1 applied on
  2026-08-09), `140/010` (the machine-check half), and `160/090` — the pointer of the earlier pass
  whose findings AR1, AR2 and AR8 this delta answers; one of its lines records AR1 answered on
  2026-10-16 and AR2 to AR7 still standing.
- The landing commit's message body (read by the brief-writer): it says Mike was re-briefed on
  AR1 and AR8 (the 2026-08-23 amendment denied a ruleset active since 2026-08-09), quotes his
  answer as "land draft and drop bypass", says the ruleset now has no bypass actor, read back, so
  signed commits bind every account, and that AP1 stays open because the owner can still edit the
  ruleset.

## Prior verdicts on these surfaces (named by filename grep, not opened, not exhaustive)

- `docs/reviews/2026-07-26-2215-adr0008-enforcement-propagation-cold.md`
- `docs/reviews/withdrawn/2026-07-26-0647-adr0008-called-not-copied-cold.md`
- `docs/reviews/2026-07-28-0123-track-a-application-cold.md`
- `docs/reviews/2026-08-09-0824-ep-application-cold.md` — names AP1
- `docs/reviews/2026-09-25-0715-ap-rulings-applied-cold.md` — names AR1; the likely source of
  AR1, AR2 and AR8

## The pointer's own lens hints

"with a live platform read" in the pass type, and the delta naming the ruleset's
`bypass_actors` beside the ADR section. Otherwise refs-only.

## Overlap with sibling passes of this batch

None of this run's other passes touches ADR 0008 or the ruleset. AR2 (the boundary row does not
read the bypass list) is open on 160/090's cycle and is restated in the delta as "still open";
a finding here that repeats it should say so rather than re-raise it.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. The section is a snapshot of platform state written as doctrine. Nothing in git re-reads
   `bypass_actors`, and the machine check explicitly does not. If the owner re-adds a bypass
   later, which surface goes false, and what notices? Is this the same "stale sentence as
   authority" shape AR8 recorded, rebuilt one layer down?
2. "In force for every account, the owner's included" sits beside "the owner account can still
   edit or delete the ruleset". Is the first phrase true in any sense an attacker cares about, and
   does a reader of the leg list alone come away with the right strength?
3. With `required_signatures` and no bypass, which write paths to `main` now fail? Platform-merged
   PRs are signed by the platform's key, not the trust list in `SIGNING.md`; does `signscan`'s
   trust list accept those, and does the hand-up-PR landing path still work?
4. "Review on the registry — post-hoc" is listed as a leg of the control. Is a review that never
   gates the push a control on supply-chain exposure, or a record of it? Does the section's own
   word "post-hoc" do enough?
5. "Before the change, 30 of the 30 latest commits on `main` were verified": a window chosen at
   the time of writing, with no re-run recorded. Is it evidence that turning on enforcement was
   safe, and what about older history and other refs?
6. The section says it was landed "on Mike's answer … after he was re-briefed". Is that answer a
   ruling or an answer (see the board's 420/020 discipline), and does the ADR's wording claim
   more than the quoted words carry?
7. "Public visibility, under which every push is published and can be inspected" is offered as a
   control on the owner account. Does publication detect anything before every child's CI has
   already run the pushed code?
