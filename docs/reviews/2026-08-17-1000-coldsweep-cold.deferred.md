# Deferred material — coldsweep.py (open only after your findings are durably written)

Sibling of `2026-08-17-1000-coldsweep-cold.md` under REVIEW.md rule 1's split.
Fold into the brief below the verdict and delete this file when the verdict
lands.

## Intent records

- `docs/roadmap/290-ruling-round-2026-08-17-the-cold-run-find/040-build-the-cold-sweep-guard.md`
  — the principal's ruling ("Build a guard") in his own selected wording, and
  the author's application note. **Not opened by the brief-writer.**
- `docs/sessions/2026-08-17-0710-cold-run-two-passes-one-brief-rulings.md` —
  the building session's account. **Not opened by the brief-writer.**
- The `docs/SESSIONS.md` index entry for the ruling round. ⚠️ **Read by the
  brief-writer**, at onramp — see the disclosure in the brief.

## Prior verdicts on the same surfaces

The three recorded instances of the exclusion defect live in verdicts, not in
doctrine. The brief-writer did not re-open them to confirm which; from the
index entries read at onramp, the third instance was recorded during the
2026-08-17 0710 cold run. Start with:

- `docs/reviews/2026-08-17-0622-authority-absolute-cold.md` (AA) and
  `docs/reviews/2026-08-15-1126-reply-gate-unwired-cold.md` (RG) — the two
  passes run in that session; one of them carries the third instance in its
  provenance or its follow-ups. AA11 is the adjacent finding about a brief
  ordering its reviewer into barred material.
- `docs/reviews/2026-08-15-1030-board-store-migration-cold.md` and the other
  2026-08-15 passes, and the 2026-08-09 batch (`2026-08-09-08xx-*-cold.md`),
  for the first two instances — search their provenance sections for the
  exclusion pattern they used and whether it applied.
- `docs/reviews/2026-08-05-1320-f1-guards-allowances-cold.md` — the pass on
  `GUARDS.md`'s block-vs-advise model, if your altitude counsel reaches
  whether a soft instrument is a guard at all.

Verify at reconcile that the tool's selftest corpus corresponds to the
instances as those verdicts actually describe them; the brief's *What the
work is* takes the author's word for that.

## Brief-writer's seeded questions (a floor, never a fence)

Generate your own before reading these. Treat a question you did not think of
as a prompt to re-read the surface, not as an agenda — and note that the
brief-writer read the commit message and the pointer's lens-1 hint, so these
questions inherit some of the author's framing.

1. `BARRED` is a tuple in code; rule 2's barred set is prose in `REVIEW.md`.
   The rule-2 edit says "the exclusion is now the tool's default" without
   naming the set. Which is canonical, and what happens when the doctrine
   adds a barred surface (a `.deferred.md` sibling, a board item under
   review) that the tuple does not carry? Is `--also-exclude` a hatch or the
   place the real bar now lives?
2. `walk()` skips symlinks. On this estate a nested harness worktree
   (`.claude/worktrees/…`) is a real directory containing a full second copy
   of `docs/`, including `docs/reviews/`. Is a worktree's `docs/reviews/`
   barred (its parts begin `.claude`, `worktrees`, `<name>`, `docs`,
   `reviews`), and does the tool sweep a sibling worktree's uncommitted
   verdict? Probe it.
3. The provenance line goes to stdout. `coldsweep 'X' | wc -l` and
   `if coldsweep 'X'; then` disagree about whether the run "matched". Which
   contract did the author intend, and does the README's "drops into a
   pipeline" claim survive?
4. `--include-barred` sets `barred = ()`, which also drops `--also-exclude`
   entries. Is that intended? A reviewer widening the sweep to *records* while
   still needing to exclude the *board item under review* cannot express it.
5. The selftest builds a corpus of five files and asserts counts. Which of
   the "three real instances" does each assertion reduce to — and is there an
   assertion for the instance where the exclusion *did* apply but a reviewer's
   second tool did not honour it?
6. The tool never reads `.atelier-floor.json`, which is where a child declares
   its records path. Does a child with records elsewhere get a bar of the
   wrong four paths and a provenance line that says the sweep was clean?
7. Rule 2 says a wide sweep is not forbidden, an undisclosed one is. The tool
   prints the disclosure; nothing carries it into the verdict. Is the
   disclosure a property of the run or of the record, and which one did the
   ruling ask for?
8. The pointer's own hint: the guard makes the safe path easier but does not
   make the unsafe path fail. Take the hint as a claim to test, not a
   conclusion — is there a cheap thing that *would* make a bare `grep -r`
   over the records fail for a reviewer session, and if there is, why did
   the build not choose it? Counsel, labelled.
