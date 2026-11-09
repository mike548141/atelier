- [x] 🎯 **Rule-4 cold pass queued: personal data held by purpose, with
      recorded exceptions (`200/100` C11).** The run authored this itself.
      The rule is in Mike's own words, and the placement and wording around
      it are the run's. It was queued at landing, and the run neither takes
      it nor spawns a reviewer for it. *Tier:* Fable, the principal-named
      review tier, checked at selection. *Pass type:* doctrine cold pass,
      per `method/REVIEW.md` rule 4. *Delta, scoped to paths:*
      `docs/build/REPO-STANDARD.md`, `docs/build/templates/CLAUDE.md`,
      `docs/build/templates/CONTRIBUTING.md` and `CLAUDE.md` (the
      personal-data constraint in each). It landed on `main` on 2026-10-03.
      *Intent record:*
      [`../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`](../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md).
      `[~]` **CLAIMED 2026-10-04 2215 UTC for the review run** (wt: review-1004;
      brief `docs/reviews/2026-10-04-2215-pii-by-purpose-cold.md`) by a
      Mike-opened `claude-fable-5-1` session ("Do all cold reviews and any other
      work dependent on fable") that authored none of the delta. Shape,
      disclosed per rule 4: reviewer-plus-orchestrator, both seats Fable — this
      session writes the refs-only brief and holds the `.deferred.md` sibling
      outside the worktree; a fresh Fable subagent it spawns forms every finding
      and severity. The sibling, the intent record and prior verdicts stay
      unopened by the reviewer until its phase-1 findings are committed.
      Provenance and exposure go in the verdict.
      - [ ] 🛑 **The pass RAN 2026-10-04 and the cycle stays OPEN — a MAJOR
            stands.** The rule-4 Fable cold pass (taker: a fresh
            `claude-fable-5-1` subagent under a `claude-fable-5-1` orchestrator
            — the shape disclosed in the claim above; the sibling, the intent
            record and prior verdicts opened only after the phase-1 findings
            were committed) returned PASS-WITH-FINDINGS — 2 MAJOR / 6 MODERATE /
            2 minor / 1 note →
            [`2026-10-04-2215-pii-by-purpose-cold.md`](../../reviews/2026-10-04-2215-pii-by-purpose-cold.md)
            (sibling folded in and deleted). PI1: the public repo's hard
            constraint says each personal-data exception is declared where it
            appears, but the account name stands on 27 lines with no inline
            declaration and the leak guard passes it unmarked. Findings are the
            principal's to decide (rule 3); nothing was applied.
      💬 **Mike's answer, 2026-11-09 (to options queue run 722ac2e2 offered,
      re-put with their impacts after he said he did not understand them; an
      answer, not a ruling):** *"Honest claim + only you grant"* — the offered
      option read: reword the claim to "listed in one place" (true today),
      add a test that keeps that list matching the files, and add a rule that
      in a public repo only he grants a personal-data exception, in his own
      words, so the scanner refuses any other excuse (PI1, PI2 on the
      reviewer's counsel); the other findings take the reviewer's counsel.
      ✅ **DONE 2026-11-09 — APPLIED** by queue run 722ac2e2 (a Sonnet worker,
      read by the orchestrator before landing), per Mike's answer above: PI1
      — the "declared where it appears" claim is replaced by one closed list,
      `docs/PERSONAL-DATA.md` (PD1–PD5), kept true by
      `tools/test_personal_data.py`; PI2 — in a public repo only the
      principal grants a personal-data exception, in his own words, and a
      marker is not a grant (`REPO-STANDARD.md`, `CLAUDE.md`, both child
      templates); PI3–PI10 as counselled; no scanner behaviour changed.
      **Not done, for him:** a scanner that enforces the closed list (it
      would need a per-repo visibility key and start warn-only, since
      several private children carry many personal-data markers); whether
      the rule moves into the stamped floor block; the private-repo grant
      wording ("the principal's order for the work is the grant"), which is
      the worker's reading of his 2026-10-03 words. Two MAJORs stood, so the
      application's cold pass is queued as `160/1120`.
      💬 **Mike's answer, 2026-11-09 (to options queue run 722ac2e2 offered; an
        answer, not a ruling):** *"Ordering the work is permission"* (re-put in plain terms after *"I dont understand"*): in a private repo, the principal's order for the work is the grant for the personal data that work needs, and the session notes that it judged so. Confirms the wording `REPO-STANDARD.md` carries.
      ✅ **The scanner landed 2026-11-09 (slice 3 of `320/810`):**
      `tools/pdlistscan.py`, for repos declaring `"visibility": "public"`,
      warning until 2027-03-08. Whether the rule moves into the stamped floor
      block stays open.
