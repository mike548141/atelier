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

## Owed

- **Cold pass on the two new bullets** — doctrine text, so the wording earns an
  un-briefed review (the principles themselves are the principal's decision).
  ROADMAP item added under *Doctrine — review-owed*.
- Children inherit via normal pin bumps; no fleet retrofit.
