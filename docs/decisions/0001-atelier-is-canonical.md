# 0001 — atelier is canonical; children point up

**Status**: accepted • **Date**: 2026-07-10

## Context

The doctrine was born inside `ros` (§0 apex, PRINCIPLES, model economics) and
extracted here. Two live copies of the apex existed the day atelier shipped —
an active DRY breach — and every future extraction would recreate the question:
when the two texts differ, which one is true? The foundation review flagged the
breach; a rule was needed before more content moved.

## Decision

**atelier holds the canonical text of all house doctrine.** A child repo (ros,
faves, any future project) carries only: an inlined safety floor (so the floor
binds even if atelier is never read), a pointer + SHA pin, and its own
*bearings* — repo-specific applications and case-law that narrow or append.
Children point up; the parent never points down for truth. On conflict the
child is wrong until the conflict is resolved upward (layer-override rule,
`method/PROPAGATION.md`). First instance: ros §0 shrunk to floor + pointer the
same day; ros PRINCIPLES trimmed to bearings + case-law on 2026-07-10.

## Rejected

- **ros stays canonical, atelier mirrors:** inverts the sharing goal — a peer
  adopting the doctrine would depend on Mike's private estate repo; and ros's
  copy is entangled with tiki specifics.
- **Per-doc canonicality (each doc lives where it was born):** no single answer
  to "where is the truth"; every reader needs a routing table; drift between
  homes is invisible.
- **Full duplication with sync discipline:** N copies is the
  divergence-by-neglect problem DRY forbids; "keep them in sync" is a promise,
  not a mechanism.

## Consequences

Extraction has a defined end-state per doc (general statement up, bearings
stay). Children get smaller and more specific. The cost: a child session that
needs the general statement must open atelier — accepted, because the inlined
floor covers the safety-critical subset and the fat pointer covers the rest on
demand.
