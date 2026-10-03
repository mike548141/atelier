- ⏳ **Rule-4 cold pass queued: pathscan's brace expansion and inline
      `./` skip (`320/010` class C, `320/170`).** The run authored this
      itself (its dispatched workers' output counts as the run's
      authorship). It was queued at landing, and the run neither takes it
      nor spawns a reviewer for it. *Tier:* Fable, the principal-named
      review tier, checked at selection. *Pass type:* code cold pass, per
      `method/REVIEW.md` rule 4. *Delta, scoped to paths:*
      `tools/pathscan.py` and `tools/test_pathscan.py`, from PR #96, merged
      on `main` on 2026-10-03.
      *Intent record:*
      [`../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`](../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md).
