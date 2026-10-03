- ⏳ **Rule-4 cold pass queued: `stampscan --require-stamps` and
      `blockscan`'s unmapped-heading report (`320/130`, `320/340`).** The run
      authored this itself (its dispatched workers' output counts as the
      run's authorship). It was queued at landing, and the run neither takes
      it nor spawns a reviewer for it. *Tier:* Fable, the principal-named
      review tier, checked at selection. *Pass type:* code cold pass, per
      `method/REVIEW.md` rule 4. *Delta, scoped to paths:*
      `tools/stampscan.py`, `tools/test_stampscan.py`, `tools/blockscan.py`,
      `tools/test_blockscan.py`, and those two tools' entries in
      `tools/README.md`. It landed on `main` on 2026-10-03, in merges
      `3cb2f64` and `33b3c5f`.
      *Intent record:*
      [`../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`](../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md).
