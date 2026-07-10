# 0005 — atelier goes public (named worked example)

**Status**: accepted • **Date**: 2026-07-10 • **Supersedes**: 0003

## Context

0003 chose private-first: harden on a real peer adoption, restructure the
person-local specifics, *then* go public. Two of its premises did not hold the
way it expected. The peer-of-two never became a peer-of-three — no real external
adopter materialised to collect the friction 0003 was waiting for. And a full
publication-readiness audit (2026-07-10) found the thing that would make
publishing *unsafe* is genuinely absent: no health, family, finance, address,
pet, or medication terms in tracked content or history (all scan zero); leakscan
clean whole-tree; secretscan clean over all 44 commits; licenscan
`--expect Apache-2.0` green. The hard boundary atelier was built to — *no
personal data, ever* — held. Data-safe is not the same as publication-*ready*,
but it moves the decision from "is it dangerous?" to "is the framing right?".

Mike's call (2026-07-10): publish now, as a **named worked example** — keep the
doctrine grounded in a real principal (Mike) and a real estate (`ros`/`tiki`)
rather than sanitising it into an abstract voice, and make it adoptable by
*telling adopters they are the principal*, not by pretending it never had one.

## Decision

**atelier goes public** at `mike548141/atelier`, Apache-2.0, as a named worked
example. The staged path 0003 described is consciously collapsed: public *is*
the mechanism for real-adopter friction, not a reward withheld until after it.

Three things change with the flip:

1. **Voice — named, not genericised.** The doctrine stays addressed to Mike as
   the worked-example principal. A README framing note makes the adopter's move
   explicit: *you* are the principal; Mike is the instance you read to learn the
   shape, then instantiate as yourself. Named grounding is more honest and more
   legible than abstraction — a principle reads truer anchored to a real
   decision than floated free of one.
2. **Grounding — provenance, not broken links.** The docs cite `ros`/`tiki`
   ~214× as their evidence base; those repos stay private. A README note frames
   these as *provenance* — the private original atelier was extracted from —
   so a public reader reads them as "where this came from", not a dead link.
3. **The floor moves.** "Making it public is a floor action, confirm" (CLAUDE.md,
   AUTONOMY) is now *spent* — this ADR is that confirmation. The live floor
   becomes: the repo is public, so the leak boundary binds on **every commit**
   (the pre-commit scan hook is no longer a private-repo nicety), and *widening
   further* — an announcement, a package, a plugin bundle — is the next
   deliberate act, not this one.

## Rejected

- **Keep waiting for a private peer adoption (0003 as written):** the peer never
  came; continuing to wait trades a real harvest (public friction, actual
  strangers reading it) for a hypothetical one. The audience-of-two problem is
  better *solved* by publishing than *guarded against* by not.
- **Genericise the voice before publishing:** rewriting every "tell Mike the
  truth" into "tell the principal the truth" abstracts away the grounding that
  makes the doctrine credible, for a privacy gain that scanning shows is unneeded
  (the name is attribution, not sensitive data). Named-worked-example keeps the
  authenticity and shifts the adoption cost to a framing note.
- **Rewrite git history to a generic identity first:** the content is scan-clean,
  so the only thing history exposes is Mike's own name + email on his own
  commits — accepted knowingly. A history rewrite is irreversible effort spent
  hiding authorship the author is content to own.

## Consequences

Publication is irreversible in practice — a clone taken while public cannot be
un-taken; Mike's name and personal email are frozen onto 44 commits; the session
log's working-relationship narrative (including that a private `numen` repo
exists) is now readable by anyone. All accepted. In exchange atelier gets what
0003 was waiting for — real external readers — and the original CI-scan
distribution problem dissolves: child repos can now fetch the public scanners
instead of needing a secret or a vendored copy. The leak boundary is now
load-bearing on every commit, not a pre-publish nicety; the scan hook earns its
keep continuously. Supersede *this* ADR only to reverse course (re-privatise) —
which un-taking clones cannot actually achieve.
