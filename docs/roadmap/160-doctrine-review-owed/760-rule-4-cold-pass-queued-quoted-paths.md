- [ ] ⏳ **Rule-4 cold pass queued: guards read git-quoted paths
      (`115/260`, `260/120`).** The run authored this itself (its dispatched
      workers' output counts as the run's authorship). It is queued at
      landing, and the run neither takes it nor spawns a reviewer for it.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4. *Delta,
      scoped to paths:* `tools/report.py`, `tools/conflictscan.py`,
      `tools/leakscan.py`, `tools/secretscan.py`, `tools/board.py`,
      `tools/harvestscan.py`, `tools/publishscan.py`, their tests and
      `tools/README.md`, from `c1cef10` and `4dfaf8d` to the merges that
      landed them on `main` on 2026-10-05. *Intent record:*
      [`../../sessions/2026-10-05-1120-queue-run-closes-and-builds.md`](../../sessions/2026-10-05-1120-queue-run-closes-and-builds.md).
