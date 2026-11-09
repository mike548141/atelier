# Held back — the estate root, the reader-side fix and the two-step ask

Opened only once the reviewer's own findings are durably written (`REVIEW.md` rule 1). A floor,
never a fence. Written by the brief-writer, session `9bb1b984`, which did not author the delta.

## The pointer's own questions

1. Can a reviewer that skips the log still be primed another way?
2. Does any text still lean on the withdrawn rule?

## The brief-writer's questions

3. Sweep for the withdrawn rule across every surface, not only the eight files the delta touched:
   the child template's other blocks, skills, `docs/method/session-open/`, the instruments' docs,
   and the floor's own guards. What still says "never by name"?
4. The sentence `Bind the property, not the role` lost its `— public —`. With the rule it summarised
   gone, what does it now bind, and is it still true of anything?
5. The join ("the name beside what the repo holds") is said to stay barred, and the idea of a term
   list is dropped. Is any guard able to see that join, or is it now prose only? Compare with the
   account of why the stricter rule failed: the same text says a rule of that shape was breached at
   least five times.
6. A child's stamped copy of the floor bullet says the old thing until its next pin bump. Does the
   old copy now contradict the parent in a way that makes a child session do the wrong thing in the
   window? `AUTONOMY.md`'s pre-flip scrub: does it still have an object, now the name is allowed?
7. `REVIEW.md` cites `CLAUDE.md` step 4 and the child template's step 3 by number. `3312cdbd`, in
   the same day's landings, added a step to `CLAUDE.md`'s read order. Do the numbers still point at
   the step they name, in every copy?
8. Which spawn prompts exist that say "read everything first": the queue-run prompt, the session-open
   prompt, the review-brief skill's template, the API pass harness a private repo holds (by type
   only)? Does the reader-side rule reach each, or only the ones the delta edited?
9. The fix "cannot be forgotten by a writer". Rule 2 also says the spawn prompt and the brief say
   so. Is that a writer-side duty returning under another name?
10. The accepted residuals (board index, commit subjects, queue-run opening prompt, branch names):
    is the list complete? A hand-up PR title, read at open under the step `3312cdbd` added, is a
    further read before the brief. Is it on the list?
11. "A session cannot see which display mode the harness is in": does any harness expose it? What
    happens to the two-step rule in a headless run, where there is no device, and in a turn the
    principal interrupts between the account and the device?
12. The apex now points at the scaling sentence. Is the scaling sentence compatible with "always, in
    every view" for a one-line clarification?
13. `coldsweep --commit`: `--path` accepts git pathspec magic. Can `:(top)`, `:/`, `:!` or a glob
    reach a barred path, with the closing line still reporting it as left out? What about a rename
    out of a barred directory, a merge commit (first parent only), a commit whose subject paragraph
    spans lines, and a repository with an external diff driver or `diff.noprefix` set?
14. Does the board-store default hide a delta whose subject IS a board file, with exit 0 and a
    closing line a reader skims? Compare its output for `436273ba` with raw `git diff`.
15. `tools/coldsweep.py` is the instrument the brief tells you to read the delta with, and it is in
    the delta. Cross-check one of the three commits with `git diff <sha>^1 <sha>`, which prints no
    message body.
16. `GUARDS.md` gains a "when it was granted" clause on a restatement "as the board records it, not
    verbatim". Is that grounded enough for a doctrine change, under the repo's ground-everything
    rule? It is a C5 finding, carried in a commit about naming.

## Facts held back

- **Re-run lines, 2026-11-09 UTC, machine load about 9 at the start, run from the worktree root
  (the `cd tools` line from `tools/`).** `python3` was 3.14.6. `coldsweep --selftest` exit 0;
  `test_coldsweep test_templates` 104 tests, exit 0; `floor.py --plane ci --root .` exit 0, with
  `pathscan` warn-only findings; the full `unittest discover -s tools` under `nice`: 2,718 tests in
  about 647 s, OK, exit 0.
- **Interpreter:** under `/usr/bin/python3` (3.9.6) `test_floor` and `test_floorfleet` exit 1 with
  `TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'`; the other named test files
  and every `--selftest` exit 0 there. The brief's lines use the `PATH` interpreter for that reason.
  The brief-writer did not trace the source of the error.
- **Not re-run by the brief-writer:** the 2026-07-28 name census and any figure in `CHANGELOG.md`.
