- [x] **ccarchive: iCloud dataless-file awareness** — built 2026-07-22
  (wave-3 queue run, `12794d6`): `SF_DATALESS` read via BSD `stat -f %f`
  (Node exposes no `st_flags` — investigated incl. bigint stats),
  classifier **verified against a real evicted file** in the live archive,
  `stat` proven non-faulting. `--verify`/`--audit` skip evicted files into a
  distinct `evicted`/undetermined bucket (never a failure, never mis-read as
  missing/corrupt; success line says "every *checked* transcript"); opt-in
  `--materialise` reads them deliberately; `--restore` still faults content
  back by design (documented); manifest/backfill writes proven non-faulting.
  Honest residual: the end-to-end skip on a *live* eviction is
  seam-simulated, not exercised — nothing was evicted to test. Suite
  109→116 (118 instruments-wide post-merge). The `--json` audit contract
  gains the `evicted` array — consistent-awareness call endorsed at merge.
