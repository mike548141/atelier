- ⏳ **Rule-4 cold pass queued: publishscan's round-2 denylist
      (`260/040`).** The run authored this itself (its dispatched workers'
      output counts as the run's authorship). It was queued at landing, and
      the run neither takes it nor spawns a reviewer for it. *Tier:* Fable,
      the principal-named review tier, checked at selection. *Pass type:*
      code cold pass, per `method/REVIEW.md` rule 4. *Delta, scoped to
      paths:* `tools/publishscan.py`, `tools/test_publishscan.py` and
      publishscan's section of `tools/README.md`. It landed on `main` on
      2026-10-03, in merge `a91d9b6`.
      *Intent record:*
      [`../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`](../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md).
