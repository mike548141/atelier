# timestamps are UTC at rest, local on presentation; foreign data kept as-is

**Status**: accepted • **Date**: 2026-07-15

## Context

Dates and times are scattered across the repo — session and ADR filenames,
`SESSIONS.md` entries, CHANGELOG, ADR bodies — and nowhere did we state which
zone they're in. Two implicit regimes had grown up side by side: machine
timestamps that cross the CI boundary were already forced to UTC (SIGNING's
`Z`-anchoring, born from the dogfood bug where a bare `valid-after` read in the
runner's local zone rejected every signed commit as "not yet valid"), while
every human-facing stamp — the `HHMM` in a record identifier, a date in prose —
was implicitly the author machine's local NZ time. A reader or peer adopter in
another zone has no way to tell which stamps are theirs to reinterpret and which
are already anchored. Mike asked (2026-07-15) whether we say anywhere what zone
we use. We don't, and "a human assumes their local zone" only holds while every
reader shares one — which a shareable repo can't assume.

This ADR is itself the first identifier under the rule it sets: its `1327` is
UTC, while the authoring machine's wall clock already read 2026-07-16. The gap
*is* the reason for the rule.

## Decision

The general rule — declare a default frame, label deviations — lives in
`method/CONVENTIONS.md`; time is its worked instance, decided here.

- **UTC at rest.** Every timestamp atelier *authors* to storage, a file, or a
  record is UTC. This generalises SIGNING's `Z`-anchoring from signing
  timestamps to all authored timestamps: the CI scar becomes the house rule.
- **Local, and labelled, on presentation.** A timestamp shown to a human is
  converted to the reader's zone, and carries its zone when the zone could be
  doubted (per CONVENTIONS' label-on-deviation rule — not tattooed on every
  value).
- **Record identifiers go UTC forward.** From this ADR on, the `HHMM` in
  session and ADR identifiers is UTC (`date -u`). A key belongs in the canonical
  zone — globally unambiguous, and it sorts correctly across zones, where a local
  key does not. Existing files keep their names: no retro-rename, exactly the
  stance the identifier migration took (ADR 2026-07-13). The boundary is this
  ADR; mixed local/UTC identifiers coexist in history, as designed.
- **Foreign data is kept as-is (a precedence, not an exception).** Data we don't
  own — an external party's records landing in a data lake — is stored
  unmodified; its source zone is recorded as *metadata alongside*, never by
  rewriting the payload. When "preserve data we don't own" collides with "store
  UTC at rest," preservation wins: integrity and verifiability outrank
  normalisation. ELT, not ETL. The kept data is then a labelled deviation from
  the UTC default, and the zone-metadata is its label.

## Rejected

- **Store local time at rest:** the CI dogfood already proved it breaks silently
  across zones; a record read in a zone other than the author's is un-anchorable.
- **Normalise foreign data to UTC on ingest (ETL):** destroys the received
  bytes' integrity and verifiability, and spends transform effort on data we
  didn't author and whose source may be authoritative in its own zone.
  Keep-as-is plus zone-metadata (ELT) preserves both.
- **Retro-rewrite existing local stamps/identifiers to UTC:** churn for no gain
  — it breaks references and rewrites history the record forbids (RECORD is
  append-only). Forward-only, boundary at this ADR.
- **Keep identifiers local:** a filename is a key, not prose; a key read in
  another zone is ambiguous and sorts wrong.

## Consequences

- New session/ADR identifiers derive `HHMM` from `date -u`. A UTC stamp won't
  match the author's wall clock near local midnight — expected, not a defect
  (this ADR is the first example).
- SIGNING's `Z`-anchoring is now a special case of the general at-rest rule, not
  a standalone quirk; the two stay consistent.
- Foreign-data ingestion must carry a zone-metadata field. Absent it, the data
  is an *unlabelled* deviation — a defect by CONVENTIONS' rule, not a shrug.
- No existing file is renamed. History carries both regimes across the boundary,
  and the record says which is which.
- Time is the first worked instance of `method/CONVENTIONS.md`; currency,
  encoding, date-format and locale are declared there under the same rule.
