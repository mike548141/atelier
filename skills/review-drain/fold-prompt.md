# Fold: finish an interrupted review pass (no review-tier work)

You are finishing the non-review remainder of a cold review pass that a review drain started in `{REPO}` and a usage limit cut off. The principal's words on finishing started work, verbatim: {APPROVAL}

So: you run NO review-tier model and spawn NO subagent. You form no finding, write no severity and change no reviewer text. You do only orchestrator work: commit, fold, flip the board item, rebuild the board, land. Drain session {BY} started you; it wrote neither the brief nor the subject.

The pass: `{REPO}:{ITEM}`, brief `{BRIEF}`, in the worktree `{WT}`; the held sibling's copy is at `{HELD}`. Procedure reference: the atelier `review-drain` skill and its `orchestrator-prompt.md`, step 7. Read this repo's CLAUDE.md for its board tool and gates. Read the brief in full before folding.

1. The reviewer's act 1 and act 2 text is already in the brief file (act 2 may be uncommitted). Do not edit the reviewer's prose except for form-only gate fixes (wrap, date or spelling markers on verbatim quotes), and say what you changed in the fold preface.
2. Append the held sibling's text VERBATIM below the final verdict under the heading "Deferred sibling, folded below the verdict (orchestrator, {DATE})", with a one-paragraph preface: held out of the tree by the orchestrator until act 1 was committed; released to the reviewer for act 2; folded here by a fold-only session after the drain's orchestrator hit the usage limit, with no review-tier run. Read the held copy only to copy it.
3. Remove the sibling from git and fix the brief's own link or pointer to it.
4. Fix a stale Status line (form only).
5. Flip the board item `[~] ⏳` -> `[ ] 🎯` (or the repo's equivalent), replacing the claim line with: PASS RAN (date), verdict, tally, the standing MAJOR(s) one line each, the findings that are the principal's to rule (from the verdict's own words), and routing. The principal's rulings are owed asks on the item; never decide them.
6. Rebuild the board index per the repo's CLAUDE.md. Stage explicit paths only; read `git diff --cached` in full before each commit; commit with output to a log file and check the exit code; never pipe `git commit`.
7. {LANDING} Verify the commit is on the mainline; cite hashes only after the rebase.
8. Absolute paths and `git -C`; never `cd`. Never print a secret. No GUI apps. No live systems.

Do NOT remove the worktree, release the queue claim, or delete the held copy: the launcher does that. Finish with: RESULT (DONE/FAILED), item, the final verdict and tally as the reviewer wrote them, the principal's rulings owed (one line), commit hashes on the mainline, and anything that broke.
