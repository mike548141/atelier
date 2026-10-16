- [ ] ⏳ **Rule-4 cold pass queued: staged findings at their real line
      (`115/300`).** The run authored this itself (its dispatched worker's
      output counts as the run's authorship). It is queued at landing, and
      the run neither takes it nor spawns a reviewer for it. *Tier:* Fable,
      the principal-named review tier, checked at selection. *Pass type:*
      code cold pass, per `method/REVIEW.md` rule 4. *Delta, scoped to
      paths:* `tools/conflictscan.py`, `tools/leakscan.py`, their tests
      and `tools/README.md`, commit `f4afb7a` and its merge, landed on
      `main` on 2026-10-16.
      *Intent record:*
      [`../../sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md`](../../sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md).
