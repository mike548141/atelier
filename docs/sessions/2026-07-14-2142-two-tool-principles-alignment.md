# 2026-07-14 · 2142 — two tool principles codified; economics + review alignment confirmed (Fable)

Mike brought two practices he wanted "represented in the right place in atelier
for the child repos to use", plus two alignment questions ("does this match the
doctrine?").

## Codified — two new bullets in `PRINCIPLES.md` §2 (Structure)

Both are Mike's decided practice (2026-07-14), placed beside their siblings
(loose coupling, Unix philosophy); the wording is the agent's:

- **Human-readable output carries a machine-readable twin.** Any tool we build
  that prints for a human must also offer the result machine-readable (`--json`
  + honest exit codes). The Unix-philosophy bullet already carried this as
  spirit; it is now a hard rule with a stated scope (tools whose output can
  feed a program; an inherently interactive surface like a web UI is out of
  scope, though its backing service still earns an API). Omitting the machine
  surface is the choice needing a stated reason.
- **A commodity sub-feature sits behind a swappable seam.** Building a minimal
  in-house version of something the market ships full-featured (PKI CA, secret
  store, web server, hypervisor) is legitimate — it keeps "out of the box"
  true — but it goes behind a pluggable seam so a mature product can replace
  it without touching the core. Case: the plan for `tiki`'s PKI CA, honestly
  labelled a designed direction, not a shipped seam.

## Alignment check (no doctrine change needed)

- **Model economics** — Mike's framing (balance capability against cost in the
  wide sense: money, credits, time, effort, quality) matches
  `MODEL-ECONOMICS.md` (match model to job/risk, two spend pools, ceremony
  proportional to cost-of-wrong) and precedence rule 6. One nuance reported to
  Mike: doctrine treats *quality of outcome* as tradeable only within low-risk
  work with a mechanical gate holding the floor — cost never buys down
  honesty/safety/correctness (cost is the lowest rung).
- **Review** — Mike's framing (widest-possible challenge; fresh, capable,
  impartial, independent, plural reviewer; no fox guarding the hen house;
  principal can overrule) matches `REVIEW.md` near-verbatim: lens 1
  approach-and-assumptions, the independence rules (framing leaks through the
  ask), and the decision step (`[rejected: grounds]` for code; the principal
  decides doctrine findings).

## Addendum — two more, same turn's follow-up

Mike added *API first* and *responsive mobile-first web apps*. Both land as §2
bullets beside the first two — they are the same family (how a product faces
its clients), and each is placed with its grounding stated at its true
strength:

- **API first — the UI is one client among many.** The machine-twin rule at
  the service layer: capabilities land behind an API before any surface rides
  them. Grounding is honest about being *consumption-side today* — `tiki`
  drives RouterOS exclusively through its REST API (the principle from the
  client's chair); producing our own services API-first is adopted standing
  practice, first intended case the planned orchestration layer.
- **One responsive web app, mobile-first.** Framed as DRY at the presentation
  layer — a separate mobile edition is two surfaces asserting one truth,
  diverging from the fork. Labelled: adopted standing practice, **no shipped
  worked case in the fleet yet**; the first web surface built becomes the case
  (stub-don't-fabricate applied to grounding).

## Owed

- **Cold pass on the four new bullets** — doctrine text, so the wording earns
  an un-briefed review (the principles themselves are the principal's
  decision). ROADMAP item under *Doctrine — review-owed*, widened from two to
  four.
- Children inherit via normal pin bumps; no fleet retrofit.
