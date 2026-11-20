- [x] **ccarchive: restore from archive — full + delta** — built 2026-07-22
  (wave-1 queue run, `9ca1425`): `--restore` (full) + `--restore --delta`
  (audit's mutated/pruned/renamed buckets), `--dry-run`/`--force`/`--json`
  reused. Content-first safety: `grown` never a target (byte-prefix check,
  so even a full restore can't drop a live tail); diverged+newer live
  refuses unless `--force` (loud); zip-slip containment; additive only
  (renamed restores the OLD path, never deletes the live rename —
  documented choice). Suite 46→63 ccarchive / 109 instruments green,
  re-proven post-merge; live fixture run exercised every exit path. Man page
  + README updated per the CLI-docs standard.
