- ⏳ **Rule-4 cold pass queued: pathscan and linkscan stream and cap
      (`110/120`).** The run authored this itself (its dispatched workers'
      output counts as the run's authorship). It was queued at landing, and
      the run neither takes it nor spawns a reviewer for it. *Tier:* Fable,
      the principal-named review tier, checked at selection. *Pass type:*
      code cold pass, per `method/REVIEW.md` rule 4. *Delta, scoped to
      paths:* `tools/pathscan.py`, `tools/linkscan.py`, their test files,
      and their `tools/README.md` paragraphs. It landed on `main` on
      2026-10-03, in merge `6b1dc9a`.
      *Intent record:*
      [`../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`](../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md).
