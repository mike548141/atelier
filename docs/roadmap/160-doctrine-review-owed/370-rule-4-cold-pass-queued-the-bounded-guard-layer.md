- ⏳ **Rule-4 cold pass queued — the bounded-guard-layer conversion: fourteen
      tools streamed, capped or measured, plus the measurement harness they
      all rest on.** Self-authored by the run (its dispatched workers count as
      the run's authorship), queued at landing; the run neither takes nor
      spawns it. *Tier:* Fable, the principal-named review tier — checked at
      selection; a session that cannot honour the bar stops rather than
      takes. *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta — scoped to paths:* `tools/memprobe.py` and
      `tools/test_memprobe.py` (the isolation rewrite) · the streaming
      conversion in `tools/leakscan.py`, `conflictscan.py`, `sizescan.py`,
      `datescan.py`, `wrapscan.py`, `spellscan.py`, `linkscan.py`,
      `reviewscan.py`, `pathscan.py`, `licenscan.py`, `stampscan.py` · the
      size-gate additions in `tools/blockscan.py`, `pins.py`,
      `floorfleet.py`, `signfleet.py` · every corresponding `test_*.py`
      `BoundedMemory` class. Landed on `main`, 2026-09-20; separate from
      `160/350`, which covers the first two scanners only.
      **The lenses that matter most here:** whether any per-line window or
      per-file cap can silently drop a finding a reader needed (each is meant
      to count and report, never truncate quietly); whether the caps'
      groundings are in the file *class* rather than fitted to a measurement;
      and whether ten copies of `_walk_files` have already drifted from each
      other on the day they were written.
      *Intent record:*
      [`../../sessions/2026-09-19-0038-queue-run-the-morning-rulings.md`](../../sessions/2026-09-19-0038-queue-run-the-morning-rulings.md).
