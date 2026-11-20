- [x] **Backfill the sidecars for already-archived transcripts — measured to be
  FREE, and this item exists to verify that rather than to build it (Mike asked
  2026-07-28).** `archiveOnce` walks the whole live tree each run and
  `shouldArchive` returns true whenever no mirror exists, so the first ordinary
  run after the capture class lands takes every sidecar still on disk — no new
  code, no flag, no separate pass.
