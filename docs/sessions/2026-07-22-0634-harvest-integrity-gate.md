# 2026-07-22 · 0634 UTC · Harvest-integrity gate built — sizescan checks the archive; tri-state ruled (Fable, wt: harvest-integrity-gate)

## Trigger and ratification

IR5's incident (an un-harvested `[x]` redding the floor) led Mike to ask
whether anything would catch the inverse — live work accidentally sitting in
ROADMAP-DONE. Answer was no; the first manual grep found a real instance.
Mike ratified the counselled build: **"I like this idea of embedding it into
the CI"** — extend sizescan, so the floor's existing `sizescan --check` step
carries it fleet-wide with zero workflow changes.

## What landed (delta `0bdccf3`)

- **Archive-integrity gate**: the named archive stores (`*-DONE.md`,
  `*-ARCHIVE.md`) now gate under `--check` on live state markers —
  `[ ]` / `[~]` / `⏳` list items — same fail-safe contract as cold content;
  never size-metered; `sizescan:allow` header hatch honoured; fenced and
  prose mentions immune (same bullet-anchored grammar as the cold gate).
- **Scope bound, per Mike**: state coherence only — the gate never verifies
  `[x]` delivery; that overhead stays with review.
- **On a hit, the output prescribes conduct**: investigate (children,
  session log, code) → recommend to the principal (flip with a dated
  disposition note, or un-harvest) → never silently fix.
- **Tests**: suite 302→314; the new `HarvestIntegrity` class encodes Mike's
  own four-situation taxonomy (top-level live item; live parent over done
  children; live parent with mixed children; stray live child under a done
  parent) — line-based counting covers all four. Selftest gains the archive
  cases. Live repo scan green.

## Design rulings taken mid-build (Mike, in-conversation)

1. **Box grammar is a work-owed tri-state**: `[ ]` owed · `[~]` underway ·
   `[x]` no more work owed — delivered, superseded, or declined, with the
   disposition in the item's own dated note. This superseded the captured
   `[-] dropped` counsel; legend + ROADMAP-DONE header updated.
2. **Five-state extension proposed** (`[-]` declined, `[^]` superseded) —
   builder counselled **against** (the bracket answers one machine-checked
   question; dispositions need prose anyway; extra states are a second copy
   of one fact — the drift class two cycles just caught) and recorded it as
   an open 🎯 question on the ROADMAP for Mike to confirm or overrule. The
   build implements the tri-state either way; `[-]`/`[^]` would be additive.

## Review status — queued, not spawned

The gate is policy-as-code (doctrine by function) and this session authored
it, so per REVIEW.md rule 4 it neither takes nor spawns the review: the `⏳`
**Harvest-integrity gate cold pass** pointer is queued refs-only for a
non-author. The obvious attack surfaces are the reviewer's to find cold.

## State at close

Delta + records on `main`; suite 314 green; floors green (secret / leak /
link hooks per commit; sizescan `--check` rc=0 at HEAD); worktree put away.
