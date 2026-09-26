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
      `[~]` **CLAIMED 2026-09-25 0705 UTC for the review run** (wt:
      review-batch-0925; brief
      `docs/reviews/2026-09-25-0715-bounded-guard-layer-cold.md`) by a
      Mike-opened `claude-fable-5-1` session ("Please deliver all fable
      dependent work, and work that would be best delivered using fable") that
      authored none of the delta. Shape, disclosed per rule 4:
      reviewer-plus-orchestrator, both seats Fable — this session writes the
      refs-only brief and holds the `.deferred.md` sibling outside the worktree;
      a fresh Fable subagent it spawns forms every finding and severity. The
      sibling, the intent record and prior verdicts stay unopened by the
      reviewer until its phase-1 findings are committed. Provenance and exposure
      go in the verdict.
      - [ ] 🎯 **The pass RAN 2026-09-26; the cycle CLOSES on this pass (no
            MAJOR) — what remains is decided into the backlog.** The rule-4
            Fable cold pass (taker: a fresh `claude-fable-5-1` subagent under a
            `claude-fable-5-1` orchestrator — the shape disclosed in the claim
            above; the sibling, the intent record and prior verdicts opened only
            after the phase-1 findings were committed) returned
            PASS-WITH-FINDINGS — 0 MAJOR · 2 MODERATE · 6 minor · 5 note →
            [`2026-09-25-0715-bounded-guard-layer-cold.md`](../../reviews/2026-09-25-0715-bounded-guard-layer-cold.md)
            (sibling folded in and deleted). BL1 (MODERATE): datescan, spellscan
            and wrapscan, all enforced on both planes, exit 0 on a finding past
            the 8 KiB per-line cap and the truncation shows only in the prose
            tally, so a cap turns a blocking guard green; BL2 (MODERATE): the
            hook plane every commit runs is unbounded — leakscan and
            conflictscan --staged still buffer the whole staged diff, so the
            CHANGELOG's every-guard claim overclaims (blame confirms the run's
            own close commit wrote it); BL13 (note) formed at reconcile.
            Findings are the principal's to decide (rule 3); nothing was
            applied.
