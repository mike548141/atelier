- [ ] 🎯 **Rule-4 cold pass queued: pathscan and linkscan stream and cap
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
      `[~]` **CLAIMED 2026-10-04 2215 UTC for the review run** (wt: review-1004;
      brief `docs/reviews/2026-10-04-2215-bounded-pathscan-linkscan-cold.md`) by
      a Mike-opened `claude-fable-5-1` session ("Do all cold reviews and any
      other work dependent on fable") that authored none of the delta. Shape,
      disclosed per rule 4: reviewer-plus-orchestrator, both seats Fable — this
      session writes the refs-only brief and holds the `.deferred.md` sibling
      outside the worktree; a fresh Fable subagent it spawns forms every finding
      and severity. The sibling, the intent record and prior verdicts stay
      unopened by the reviewer until its phase-1 findings are committed.
      Provenance and exposure go in the verdict.
      - [ ] 🎯 **The pass RAN 2026-10-04; the cycle CLOSES on this pass (no
            MAJOR) — what remains is decided into the backlog.** The rule-4
            Fable cold pass (taker: a fresh `claude-fable-5-1` subagent under a
            `claude-fable-5-1` orchestrator — the shape disclosed in the claim
            above; the sibling, the intent record and prior verdicts opened only
            after the phase-1 findings were committed) returned
            PASS-WITH-FINDINGS — 0 MAJOR / 4 MODERATE / 5 minor / 2 note →
            [`2026-10-04-2215-bounded-pathscan-linkscan-cold.md`](../../reviews/2026-10-04-2215-bounded-pathscan-linkscan-cold.md)
            (sibling folded in and deleted). BP1: pathscan now reads any stretch
            of 256 KiB or more without an LF as one line, so a lone-CR file with
            a fence at the top went from 60,000 findings and exit 1 to none and
            exit 0. BP2 (a line-scoped allow marker silences a whole lone-CR
            file in enforced linkscan and leakscan) predates the delta and is
            new on record. Findings are the principal's to decide (rule 3);
            nothing was applied.
