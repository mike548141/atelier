- ⏳ **Rule-4 cold pass queued: `stampscan --require-stamps` and
      `blockscan`'s unmapped-heading report (`320/130`, `320/340`).** The run
      authored this itself (its dispatched workers' output counts as the
      run's authorship). It was queued at landing, and the run neither takes
      it nor spawns a reviewer for it. *Tier:* Fable, the principal-named
      review tier, checked at selection. *Pass type:* code cold pass, per
      `method/REVIEW.md` rule 4. *Delta, scoped to paths:*
      `tools/stampscan.py`, `tools/test_stampscan.py`, `tools/blockscan.py`,
      `tools/test_blockscan.py`, and those two tools' entries in
      `tools/README.md`. It landed on `main` on 2026-10-03, in merges
      `3cb2f64` and `33b3c5f`.
      *Intent record:*
      [`../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`](../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md).
      `[~]` **CLAIMED 2026-10-03 0158 UTC for the review run** (wt:
      `atelier-review-430`, branch `review-430-1003`; brief
      `docs/reviews/2026-10-03-0158-cover-switch-unmapped-headings-cold.md`)
      by a Mike-opened `claude-fable-5-1` session ("Do all cold reviews and any
      other work dependent on fable") that authored none of the delta and was
      not started or instructed by the authoring run. Shape, disclosed per rule
      4: reviewer-plus-orchestrator, both seats Fable — this session writes the
      refs-only brief and holds the `.deferred.md` sibling outside the worktree
      and outside the harness scratchpad; a fresh Fable subagent it spawns forms
      every finding and severity. Disclosed exposure: the authoring run told
      this session, over the cross-session channel, that the pointer existed and
      named the two features; nothing else from it was read. The sibling, the
      intent record and prior verdicts stay unopened by the reviewer until its
      phase-1 findings are committed. Provenance and exposure go in the verdict.
      - [ ] 🎯 **The pass RAN 2026-10-03 and the cycle CLOSES on it (0 MAJOR);
            CU1–CU10 await Mike's ruling round.** The rule-4 Fable cold pass
            (taker: a fresh `claude-fable-5-1` subagent under a
            `claude-fable-5-1` orchestrator — the shape disclosed in the claim
            above; the sibling, the intent record and prior verdicts opened only
            after the phase-1 findings were committed) returned
            PASS-WITH-FINDINGS — 0 MAJOR · 1 MODERATE · 6 minor · 3 note →
            [`2026-10-03-0158-cover-switch-unmapped-headings-cold.md`](../../reviews/2026-10-03-0158-cover-switch-unmapped-headings-cold.md)
            (sibling folded in). With the switch off, stampscan's output is
            byte-identical to the pre-delta tool. CU1 (MODERATE):
            `--require-stamps` certifies that some stamp was compared, not that
            the floor is stamped — a tree with the floor copy unstamped and one
            unrelated stamp passes, so `320/130`'s landing note overstates the
            cover precondition on `020/110`. CU3: the collapsed "top-level"
            count includes four `###` headings. CU6: `--check` reads map paths
            with no root confinement. CU9 (note, converging with FV3): no wired
            caller passes the switch and a child cannot use it until ST3. The
            collapse does not hide the case `320/340` was filed for, and neither
            change alters an exit code for a repo that was green. Findings are
            the principal's to decide (rule 3); nothing was applied.
