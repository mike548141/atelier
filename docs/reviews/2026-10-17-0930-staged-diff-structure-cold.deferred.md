# Sibling to the staged-diff structural reader cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-17-0930-staged-diff-structure-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-17 UTC by the Opus brief-writer named in the brief's provenance; it
forms no finding. Fold this file in below the reconcile and delete it at phase 2.

## Intent and commissioning records

- Intent record: `docs/sessions/2026-10-16-0703-queue-run-after-the-sizescan-ruling.md` —
  **not opened by the brief-writer**.
- Commissioning board item (head line seen, never read whole): `115/280` (an added line can pose
  as a diff header in secretscan's staged plane, found 2026-10-05 by the `260` worker).
- The landing commit's message body (read by the brief-writer): it describes the hole (an added
  line whose text begins `++ ` prints as `+++ …`, moved attribution of later lines to a posed
  name and was itself dropped, so a posed ignored name hid real lines on a blocking guard); says
  `diff_header_path` narrowed *what* counts as a header but not *where*, so conflictscan and
  leakscan had the hole too; gives the counts-based design and its reason ("the counts are what
  git used to write the body"); lists the fail-closed cases; says two further forging inputs were
  closed (byte split on newline only; prefixes and `--no-ext-diff` pinned against a user's
  `diff.noprefix` or `mnemonicPrefix`, noting secretscan used to accept any prefix as written);
  and claims old-against-new staged output byte-identical on "a realistic change set" except for
  the posed case, with the whole-tree planes identical.
- The merge's message body: the orchestrator read the diff, re-ran the four test files and
  reproduced the hole independently (old clean, new blocked) before merging; rebuilt fresh after
  a 07:35 UTC crash.

## Prior verdicts on these surfaces (named by filename grep, not opened, not exhaustive)

- `docs/reviews/2026-09-25-0715-staged-plane-check-cold.md`
- `docs/reviews/2026-09-25-0715-secretscan-stream-pathscan-roots-cold.md`
- `docs/reviews/2026-10-04-2215-linear-line-reader-cold.md`
- `docs/reviews/2026-10-16-1551-git-quoted-paths-cold.md` — an unrun 2026-10-16 brief on
  `diff_header_path`, which this reader calls (another pass's framing)
- `docs/reviews/2026-10-16-1551-shared-report-contract-cold.md` and
  `docs/reviews/2026-10-16-1551-scanner-rule-gates-cold.md` — unrun 2026-10-16 briefs on the same
  files; the brief-writer read the latter's ask half as a template (disclosed in the brief)

## The pointer's own lens hints

None. The pointer is refs-only.

## Overlap with sibling passes of this batch

- 160/760 (git-quoted paths, `115/260`) owns `diff_header_path` and `unquote_c`; this reader
  depends on both.
- 160/830 (staged findings at their real line, `f4afb7a`) changed how conflictscan and leakscan
  use this reader's line numbers.
- 160/720 (scanner gates) and 160/730 (report contract) share `leakscan.py`, `secretscan.py` and
  `report.py`.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. `STAGED_DIFF_CMD` pins `--no-ext-diff` but not `--no-textconv`. A `.gitattributes` diff
   driver with a text conversion configured would change what `git diff --cached` prints for a
   file's added lines. Can a committer, or a hostile tracked `.gitattributes` plus local config,
   make a guard scan converted text instead of the bytes being committed?
2. `diff.relative` in git config restricts `git diff` to the current directory and makes paths
   relative to it. The command does not pass `--no-relative`. If the hook or a caller runs from a
   subdirectory, are files outside it silently absent from the scan?
3. `--diff-filter=ACMR` leaves out `T` (type change). Is a file changed from a symlink to a
   regular file with new content scanned? (The filter predates this delta; the reader carries it.)
4. Headers and lines are decoded with `errors="replace"`. With `core.quotePath=false`, a path
   holding an invalid UTF-8 byte arrives raw and is decoded lossily: does the attributed path
   still match ignore globs, path filters and later `git` arguments?
5. Every `DiffReadError` is exit 2 on a blocking guard. Is there any legitimate staged change git
   prints in a shape the reader refuses (unmerged paths mid-merge, a submodule, a hunk header
   with unusual function context), so that every commit of that shape is refused until someone
   edits the tool?
6. The old secretscan accepted any header prefix "as written"; the new reader refuses a header
   that is not `b/…` or `/dev/null`. The pin makes that safe for git's own output. Is any caller
   or test feeding the parser text not produced by `STAGED_DIFF_CMD`?
7. The equivalence claim rests on one "realistic change set". What did it contain, and does it
   cover the header and hunk shapes listed in the brief's *Scope*?
