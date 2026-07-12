# Coordination-free record identifiers

**Status**: accepted • **Date**: 2026-07-13

## Context

A child repo (ros) running parallel sessions hit a session-number collision:
two sessions each computed "next NN" from their own stale view, produced
differently named files carrying the same number, and git raised no conflict —
the duplicate surfaced only on human read-through. The first fix (`e93e731`,
same day) kept the counters and added an allocation discipline: allocate late,
provisional until pushed, first landed wins. Mike then ruled the running
number carries no meaning beyond chronology — which the date already gives —
and extended the ruling past session logs to ADRs and every similar series.

## Decision

Record identifiers are built from facts the session already owns — **date +
slug**, plus start time (`HHMM`) where same-day order matters (session logs) —
never from a shared next-N counter. New record series take the same form.
Existing numbered files (ADR `0001`–`0007`, session files through `52`) keep
their names and their citations; the record is append-only and history is
never renumbered.

## Rejected

- **Counters + allocation discipline (the same-day first fix):** works, but
  pays a standing discipline to keep a shared resource unique when no shared
  resource is needed, and the silent-collision class survives wherever the
  discipline slips. Kept only as the interim rule for repos still carrying
  legacy counters.
- **Keep `NNNN` for ADRs as a citation convention:** "ADR 0005" is a handy
  handle, but a date+slug is as citable and a better grep key; the repo's own
  reviews had already drifted to date+slug in practice; one scheme beats two.
- **Locking or number-reservation schemes:** rejected on arrival —
  `CONCURRENCY.md`'s KISS line (contention is a signal to sequence, never to
  build locking).

## Consequences

- The silent-collision class is structurally gone: the worst case is two
  sessions wanting the same *filename*, which is a visible, trivial git
  conflict — the append-tail case CONCURRENCY already handles.
- Identifiers are safe to allocate at session open and cite immediately; the
  interim counter discipline binds only where a legacy counter remains.
- Cross-references name records by date + slug; old `ADR NNNN` citations still
  resolve because legacy files keep their names.
- Children adopt via their normal pin bumps; the child doctrine block's
  Concurrency line carries the compressed rule.
