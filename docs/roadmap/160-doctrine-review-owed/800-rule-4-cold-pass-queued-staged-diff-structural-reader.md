- [ ] ⏳ **Rule-4 cold pass queued: the staged diff read by its structure
      (`115/280`).** The run authored this itself (its dispatched worker's
      output counts as the run's authorship). It is queued at landing, and
      the run neither takes it nor spawns a reviewer for it. *Tier:* Fable,
      the principal-named review tier, checked at selection. *Pass type:*
      code cold pass, per `method/REVIEW.md` rule 4. *Delta, scoped to
      paths:* `tools/report.py`, `tools/secretscan.py`, `tools/conflictscan.py`,
      `tools/leakscan.py`, their tests and `tools/README.md`, commit
      `39a74b9` and merge `ef75803`, landed on `main` on 2026-10-16.
      *Intent record:*
      [`../../sessions/2026-10-16-0703-queue-run-after-the-sizescan-ruling.md`](../../sessions/2026-10-16-0703-queue-run-after-the-sizescan-ruling.md).
