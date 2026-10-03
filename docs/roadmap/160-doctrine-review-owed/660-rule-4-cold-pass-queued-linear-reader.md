- ⏳ **Rule-4 cold pass queued: the linear line reader in three guards
      (`110/140`).** The run authored this itself (its dispatched workers'
      output counts as the run's authorship). It was queued at landing, and
      the run neither takes it nor spawns a reviewer for it. *Tier:* Fable,
      the principal-named review tier, checked at selection. *Pass type:*
      code cold pass, per `method/REVIEW.md` rule 4. *Delta, scoped to
      paths:* the line readers and their tests in
      `tools/{leakscan,secretscan,conflictscan}.py` and
      `tools/test_{leakscan,secretscan,conflictscan}.py`. It landed on
      `main` on 2026-10-03.
      *Intent record:*
      [`../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`](../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md).
