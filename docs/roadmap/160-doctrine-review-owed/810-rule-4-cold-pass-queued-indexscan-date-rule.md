- [ ] ⏳ **Rule-4 cold pass queued: indexscan's date rule (`320/430`).** The
      run authored this itself (its dispatched worker's output counts as the
      run's authorship). It is queued at landing, and the run neither takes
      it nor spawns a reviewer for it. *Tier:* Fable, the principal-named
      review tier, checked at selection. *Pass type:* code cold pass, per
      `method/REVIEW.md` rule 4. *Delta, scoped to paths:*
      `tools/indexscan.py`, `tools/test_indexscan.py`,
      `tools/test_allowmarker.py`, `tools/test_report.py` and
      `tools/README.md`, commit `1c24781` and merge `da3227d`, landed on
      `main` on 2026-10-16. *Intent record:*
      [`../../sessions/2026-10-16-0703-queue-run-after-the-sizescan-ruling.md`](../../sessions/2026-10-16-0703-queue-run-after-the-sizescan-ruling.md).
