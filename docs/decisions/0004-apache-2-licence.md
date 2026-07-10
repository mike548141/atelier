# 0004 — Apache-2.0, matching the house standard

**Status**: accepted • **Date**: 2026-07-10

## Context

The licence landed at scaffold (commit `4dce8cd`) via the `create-repo` house
convention rather than a fresh deliberation; this ADR records the reasoning
that holds it, so a future session doesn't re-litigate from silence. The repo
is mixed-content: doctrine prose (`docs/`) *and* working code (`tools/`
leakscan, secretscan, worktree) — and it is publication-bound (ADR 0003).

## Decision

**Apache-2.0 for the whole repo**, one licence, same as every other house repo
(ros, faves, rpi — verified 2026-07-10). Code-friendly (explicit patent grant,
well understood by orgs that would adopt this), permissive enough that a peer
org can take the doctrine and adapt it privately, and uniform across the
estate so the A11 licence-consistency pre-publish gate has one rule to check.

## Rejected

- **CC-BY for docs (dual-licence with Apache for tools/):** arguably more
  idiomatic for prose, but two licences in one small repo is complexity
  without a customer — the adopters we expect are engineering orgs for whom
  Apache is the frictionless default, and the doctrine/tooling boundary is
  porous (doctrine text gets embedded in tool output and CLAUDE.md blocks).
- **MIT:** no patent grant; and it would break licence uniformity across the
  house repos for no gain.
- **Proprietary/no-licence while private:** would make the eventual publish a
  licensing event on top of a scrubbing event; stamping the intended licence
  from birth means every commit is already cleanly licensed.

## Consequences

Any future contribution or peer adoption inherits clear terms; the pre-publish
gate checks consistency, not policy. The cost: Apache-2.0's attribution
requirements are mild but real for adopters who fork the doctrine — accepted.
