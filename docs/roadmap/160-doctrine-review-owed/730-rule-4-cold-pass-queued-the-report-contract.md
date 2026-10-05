- [ ] ⏳ **Rule-4 cold pass queued: the shared exit and reporting contract
      (`115/080` part 3).** The run authored this itself (its dispatched
      worker's output counts as the run's authorship). It is queued at
      landing, and the run neither takes it nor spawns a reviewer for it.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4. *Delta,
      scoped to paths:* `tools/report.py`, `tools/test_report.py`,
      `tools/README.md`, and the fourteen scanners it converted under
      `tools/`, from `ffabef3` to the merge that landed it on `main` on
      2026-10-05. *Intent record:*
      [`../../sessions/2026-10-05-1120-queue-run-closes-and-builds.md`](../../sessions/2026-10-05-1120-queue-run-closes-and-builds.md).
