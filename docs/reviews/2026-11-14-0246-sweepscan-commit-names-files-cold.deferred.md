# Held back — `sweepscan`: where sibling worktrees exist, a commit names its files (warn-only, no date)

Opened only once the reviewer's own findings are durably written (`REVIEW.md` rule 1). A floor,
never a fence. Written by the brief-writer (`cclive` lists it as session `b769469b`), which did not
author the delta. Nothing here is a finding: these are questions, and facts read off the machine.

## The pointer's own questions

1. Is `GIT_INDEX_FILE` a reliable signal on every commit path?
2. Can the marker be set and forgotten?

## The brief-writer's questions

3. The filing's central lesson is that a correct number already on screen among about a hundred
   floor lines stopped nothing, so more printed text is the wrong fix. A warn-only check with no
   date adds one more line to the same wall. What, concretely, makes this line read where the
   `publishscan` count was not? If nothing does, is the delta the filing's fix or the fix the filing
   rejected?
4. The principal's words were "warnings at first and then move to blocking action", and the plan's
   **Shape** is a dated constant per check. The delta sets no date. Was that a departure the delta
   was entitled to make on its own measurement, and was it put to him as a decision before or after
   it landed (fact 1)?
5. The measurement counts a commit's *form*. The incident is a commit that carried a *foreign*
   path. The figures say how often a session took the whole index, not how often that swept a
   peer's work. Does "fires on most commits, so it is noise" follow, or does it measure the cost of
   the rule rather than its yield? Does anything in the delta make the yield measurable later?
6. The docstring says "measured on git 2.x"; the intent record says git 2.50. Was any other version
   measured? A child CI image or an older local git would be the place a renamed temporary index
   silently turns every named commit into a whole-index warning, or the reverse.
7. `sweepscan`'s own `_git` inherits the hook's environment, including `GIT_DIR` and
   `GIT_INDEX_FILE`, while `tools/filewalk.py` deliberately drops them for its git calls (fact 3).
   Does `git -C <root> worktree list`, `rev-parse` or `diff --cached` ever answer for a different
   repo or index than the one being committed, in a linked worktree, under a relative `GIT_DIR`,
   or when a tool commits with a custom `GIT_INDEX_FILE`?
8. `replaying()` treats any present `MERGE_HEAD`, `CHERRY_PICK_HEAD`, `REVERT_HEAD` or `REBASE_HEAD`
   as "replaying commits already written". A fresh commit made at an interactive rebase's `edit`
   stop sees `REBASE_HEAD` (fact 4); so does a commit after a `cherry-pick -n` the author finishes
   by hand. Are those replays? Can a stale ref left by an abandoned operation silence the check?
9. Set-and-forgotten: the marker can come from a shell profile, a harness `env` setting, or a parent
   session's environment that every worker it spawns inherits. The clean line names the marker; does
   that line reach the session through `floor.py`'s output on a clean hook run, or is a clean
   warn-only check summarised away? Does any surface count marker use? The tests strip the marker
   from fixture environments (fact 5): the author anticipated an inherited one.
10. The `plan()` change drops the `is_local` condition, so it now governs every registry entry with
    no form on a plane, core or local. Before, a core entry with `ci=None` was dropped from the CI
    plan silently. Did any core entry other than `sweepscan` rely on that, at landing or since, and
    does `floorfleet` or any report that lists states read the new `skipped` correctly?
11. No document under `docs/method/` names `sweepscan` or `ATELIER_WHOLE_INDEX` (fact 2). The
    house's concurrency doctrine tells sessions how to commit; this repo's own onramp and many
    launch prompts say "stage explicit paths", which is a whole-index commit. Is the rule the check
    enforces written anywhere a session reads before it commits, and does the doctrine tell it to do
    the thing the check warns about (V3, V4)?
12. The proposal's limit (c): `git worktree list` is a proxy. The harness nests worktrees inside the
    repo, and every cold reviewer adds one. Is a check that is always in scope in this repo still
    measuring concurrency at all here, and does the `declares=` block added later
    (`grounding=Unmet(...)`, `purpose_gap`) state the gap the delta itself should have stated?

## Facts read off the machine

Read 2026-11-14 UTC at `461fdf92`, git 2.50.1, Python 3.14.6.

1. The principal answered on 2026-11-12 UTC, two days after the landing, from options the authoring
   run offered: 💬 *"Warn, measure first (Recommended)"*. The record files it as an answer, not a
   ruling, and owes a count of how often a whole-index commit really swept another session's work
   before blocking is put to him again (`320/060`, the landing notes from line 71).
2. `grep -rln "sweepscan\|ATELIER_WHOLE_INDEX"` over the tree (records aside) finds only
   `tools/sweepscan.py`, `tools/test_sweepscan.py`, `tools/floor.py`, `tools/test_floor.py`,
   `tools/README.md`, `CHANGELOG.md`, the board index, and three board items (`320/060`,
   `320/810`, `115/120`). Nothing under `docs/method/` or `skills/`.
3. `tools/filewalk.py` line 127 defines
   `_GIT_ENV_DROP = ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_PREFIX")`, with the comment
   that hooks export them. `sweepscan._git` passes no `env=`. `floor.py` runs each scanner with no
   `env=` (line 2854 at HEAD), so the hook's environment reaches `sweepscan` whole.
4. Probe in a throwaway repo with a hook printing what it sees: a plain commit in a linked worktree
   gets `GIT_INDEX_FILE=<repo>/.git/worktrees/<name>/index` and an absolute `GIT_DIR`; `commit
   --amend -a` gets `index.lock`; `commit -o <path>` gets `next-index-<pid>.lock`; a new file
   committed at an interactive rebase's `edit` stop runs `pre-commit` with `REBASE_HEAD` present.
   The brief-writer ran no `sweepscan` judgement over these; it only recorded what the hook saw.
5. `tools/test_sweepscan.py`'s `_git` pops `GIT_DIR`, `GIT_INDEX_FILE`, `GIT_WORK_TREE` and
   `ATELIER_WHOLE_INDEX` from every fixture command's environment. No test sets the marker in the
   parent environment and checks what a nested commit reports.
6. In the brief-writer's own worktree, `git worktree list --porcelain` listed 5 worktrees while
   other health-sweep sessions were live, so `sweepscan` would have warned on a whole-index commit
   there. `ba55be27` (after the delta) added the entry's `declares=` block, whose `purpose_gap` reads
   "the check sees the commit's form, and a named foreign path still lands".
