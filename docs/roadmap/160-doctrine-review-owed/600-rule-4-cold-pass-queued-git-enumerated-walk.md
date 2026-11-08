- [x] 🎯 **Rule-4 cold pass queued: the file walk enumerates through git
      (`110/110`).** The run authored this itself (its dispatched workers'
      output counts as the run's authorship). It was queued at landing, and
      the run neither takes it nor spawns a reviewer for it. *Tier:* Fable,
      the principal-named review tier, checked at selection. *Pass type:*
      code cold pass, per `method/REVIEW.md` rule 4. *Delta, scoped to
      paths:* `tools/filewalk.py` and `tools/test_filewalk.py`. It landed on
      `main` on 2026-10-03, in merge `bd9bd49`.
      *Intent record:*
      [`../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`](../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md).
      `[~]` **CLAIMED 2026-10-04 2215 UTC for the review run** (wt: review-1004;
      brief `docs/reviews/2026-10-04-2215-git-enumerated-walk-cold.md`) by a
      Mike-opened `claude-fable-5-1` session ("Do all cold reviews and any other
      work dependent on fable") that authored none of the delta. Shape,
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
            PASS-WITH-FINDINGS — 0 MAJOR / 1 MODERATE / 6 minor / 4 note →
            [`2026-10-04-2215-git-enumerated-walk-cold.md`](../../reviews/2026-10-04-2215-git-enumerated-walk-cold.md)
            (sibling folded in and deleted). GW1: tracked files under ten
            skip-named directories are never yielded, so the whole-tree plane
            never reads a secret committed there; inherited from the parent
            walk, and now pinned by a test. Findings are the principal's to
            decide (rule 3); nothing was applied.
      💬 **Mike's answer, 2026-11-09 (to options queue run 722ac2e2 offered,
      after he asked for and read a one-line summary of each; an answer, not
      a ruling):** *"Approve all 17"* — the reviewer's counsel applied as
      written on this item and sixteen others with no serious finding, each
      closing when applied, with no new Fable re-check; scanner changes
      tested against every child before landing.
      ✅ **DONE 2026-11-09 — APPLIED** by queue run 722ac2e2 (a Sonnet worker,
      read by the orchestrator before landing), per his bulk approval: GW1 per guard: `secretscan`, `leakscan` and `conflictscan` read tracked files under skip-named folders; GW2–GW6, GW8–GW10 as counselled; GW7 and GW11 routed. Probed over every child: one tracked compiled file newly seen, which warns until the G3 cut-off.
      No serious finding stood, so the cycle closes here.
