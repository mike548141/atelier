- [ ] ⏳ **Rule-4 cold pass queued: sizescan's size advisory removed
      (`115/270` c).** The run authored this itself (its dispatched worker's
      output counts as the run's authorship). It is queued at landing, and
      the run neither takes it nor spawns a reviewer for it. *Tier:* Fable,
      the principal-named review tier, checked at selection. *Pass type:*
      code and doctrine cold pass, per `method/REVIEW.md` rule 4. *Delta, scoped to
      paths:* `tools/sizescan.py`, `tools/test_sizescan.py`,
      `tools/test_report.py`, `tools/README.md`, `docs/method/RECORD.md`, and
      comments in `tools/pins.py` and `tools/blockscan.py`, commit `72a68cc`
      and its merge, landed on
      `main` on 2026-10-16.
      *Intent record:*
      [`../../sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md`](../../sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md).
