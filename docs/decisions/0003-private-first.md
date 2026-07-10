# 0003 — private-first: harden on a real peer before any public release

**Status**: accepted • **Date**: 2026-07-10

## Context

atelier exists to be shared — that ambition shapes its hardest constraint (no
personal data, ever). So why not public from birth? Decided by Mike at repo
creation ("private-to-CEL first") and reaffirmed in the ROADMAP's sharing
sequence.

## Decision

**Private-first.** The repo lives at `mike548141/atelier`, visibility PRIVATE.
The path to public is staged: one real peer adoption (CEL, then a client org)
hardens the doctrine first; the practice/instance restructure of AUTONOMY and
STORAGE (person-local specifics → marked worked-examples) and the
scrub-and-fresh-export pass happen before any public release. Making the repo
public — or widening its audience at all — is a floor action: Mike's decision,
never the agent's.

## Rejected

- **Public from birth:** shareability is untested — the doctrine has an
  audience of two, and text that works for Mike+Claude may be illegible to a
  peer (their confusion is the harvest a private adoption collects safely).
  Practice docs still carry person-local worked examples that read fine
  privately but would ship as noise or mild leak publicly. And publication is
  irreversible in practice — a scrubbed re-export can't unpublish what a clone
  already took.
- **Public but obscure (unlisted/no announcement):** all of the exposure, none
  of the deliberateness; still forfeits the staged hardening.

## Consequences

Routine pushes are safe (a push is not publication) and the standing
commit/push grant applies cleanly. The doctrine gets a real adopter's friction
before strangers see it. The cost: no external contributions or scrutiny yet —
accepted while the audience-of-two problem is the bigger risk. Supersede this
ADR when the public release actually happens.
