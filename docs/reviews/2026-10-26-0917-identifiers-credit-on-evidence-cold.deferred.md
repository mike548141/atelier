# Sibling to the identifiers credit-on-evidence cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-26-0917-identifiers-credit-on-evidence-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-26 UTC by the Opus 5.5 brief-writer named in the brief's
provenance; it forms no finding and writes no severity. Fold this file in below the reconcile
and delete it at phase 2.

## Intent records

Both read in full by the brief-writer. Neither quotes the principal.

- `docs/roadmap/210-instruments-open-features/290-ccclose-identifiers-over-credits-overlapping-sessions.md`
  — lines 2–16: the problem as found by the session that shipped the identifiers block (counts
  from its first real block against its own commits, a concurrent cloud session's branch
  commits and squash merge, a board item wrongly credited, a `⏳` read from a close note), and
  the shapes to weigh. Lines 17–31: the authors' closing account (what was built, one shape
  weighed differently and why first-parent was rejected, the probe on its own session with
  counts, the test count, the residue filed as `210/310`).
- `docs/roadmap/210-instruments-open-features/310-ccclose-cannot-read-a-commit-message-from-a-file.md`
  — lines 2–15: the `-F <path>` gap, said to err the safe way, with shapes to weigh. Lines
  16–27: the closing account (the write-matching rule, path equality, the `$VAR` rule, latest
  write wins, the stated limits, one commit moved by the probe, test counts).
- The three commit bodies — not read by the brief-writer.

## Re-run results held back from the brief

Run once by the brief-writer, 2026-10-26, from its worktree root at `2f6dbf6`, in the
foreground, on this machine (12 cores, load near 7 at the time):

1. `coldsweep --commit` on each of the three commits: exit 0 each, closing "message body not
   read" line present, 0 barred files touched.
2. `node --test instruments/ccclose.test.js`: exit 0, 65 tests, 65 pass.
3. `node --test instruments/*.test.js`: exit 0, 492 tests, 492 pass. (The `210/310` record
   gives 489 at `e78b6f1`; later instruments commits outside this delta may account for the
   difference. Not checked.)
4. `mandoc -T lint -W style instruments/man/ccclose.1`: exit 0, no output. The CI form at
   default level: exit 0. `awk 'length > 80'` prints one line (line 418, 143 bytes, inside a
   `.nf` example block); `git log -L418,418` names `4eda680` as its last change, outside the
   delta.
5. wrapscan over the five paths: exit 1, 6 findings (2 in `instruments/README.md`, 4 in
   `instruments/ccclose.design.md`); `git blame` puts all 6 on commits outside the delta.
   spellscan: exit 0. leakscan `--require-terms`: exit 0, local term list present.
6. `git log --oneline e78b6f1..HEAD -- <five paths>`: empty.
7. Floor, ci plane: exit 0 (secretscan 23 advisories, leakscan cover not guaranteed on this
   plane, four warn-only scanners), as designed.
8. `ccclose --help`: exit 0.
9. Live re-drive on the authoring session's transcript, counts only:
   - by id prefix (`--session 8e498ef1`) from the worktree root: exit 0, but "no transcript
     found", so every field fell to "by hand";
   - by the transcript's path: exit 0. Commits confirmed 34 (not unbroken), unconfirmed 21,
     left out 0. Board, confirmed: completed 6, created 11, claimed 0, `⏳` review 5.
     Board, unconfirmed only: completed 4, created 12. Agents 7, all reported.
   The authoring session's window covers its whole queue run, not only this delta's work.
   The brief-writer derived no ground truth and forms no view on these counts.

## Prior verdicts on nearby surfaces (named by filename, not opened, not exhaustive)

- `docs/reviews/2026-10-18-0506-close-covers-subagents-cold.md` — `160/920`, the earlier
  commits to the same files.
- `docs/reviews/2026-10-17-1010-ccclose-close-checker-cold.md` — named in a shape example; the
  name suggests the original close checker.

## The pointer's own lens hints

It names the worst failure (a block pasted as fact) and the boundary against `160/920`.
Nothing else.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. Subject equality is the whole key. House subjects recur (`board: …`, `docs: session
   record …`). Does a peer's commit with a subject the session also used get credited, and
   are two commits with one subject both credited?
2. A commit command that made no commit (hook refusal, nothing to commit) still adds its
   subject to the evidence. Combined with question 1, is that an over-credit path?
3. The command regex scans the whole command string. Does `git commit -m "x"` inside an
   `echo`, a heredoc being written to a file, a `grep` pattern or a commit message's own text
   yield evidence?
4. Git's `%s` is the first *paragraph* joined with spaces, while the tool takes the first
   *line* of the message. A message whose first paragraph spans two lines would then never
   match: an under-credit the "errs the safe way" framing does not cover. Same question for
   leading whitespace, comment cleanup, `$'…'` quoting and escaped quotes.
5. Rebased or cherry-picked copies carry the same subject. With a pre-rebase branch still in
   `--branches --remotes`, are both copies credited?
6. Merge routes other than `gh pr merge` (`gh pr merge --auto` completing later, `gh api`, the
   web UI, a separate worker session): are their squash merges left out with a reason line
   that reads as fact ("merge not run by this session")?
7. A session commit whose subject ends `(#n)` for another reason, on the first-parent line and
   without readable evidence, is "left out" as a squash merge rather than "unconfirmed". Is
   that an under-credit hidden behind a stated reason?
8. A left-out squash merge counts for nothing on the board, even on the unconfirmed line. If
   the peer's branch commits are gone from all refs, is that board movement dropped from the
   block entirely, with no line saying so?
9. `RECORD.md` asks for commits "its workers' included". Workers dispatched as separate
   sessions, not subagents, leave no subagents-directory evidence. Do their commits fall to
   unconfirmed, and does the doctrine's queue-run shape make that the common case?
10. The confirmed-only board reduce computes the final state from confirmed commits only. An
    item the session claimed and a peer then closed would read as "claimed and left open".
11. The `⏳` reading: `STATE_LINE` and code-span stripping against `tools/board.py`'s
    `STATE_RE` and `CODE_SPAN_RE`, and a re-queued `⏳` (flag on both old and new first line)
    not counted.
12. The file tier ignores Edit-tool changes and `sed` rewrites after the last Write, and the
    "parent's unordered use" of a subagent's file credits regardless of time order.
13. Silent paths: the subagent reader's `catch {}` and skipped unparseable lines shrink the
    evidence with no note in the block.
14. Security: whether `GIT_MSG`'s nested quantifier can be driven to long backtracking by a
    crafted command, and whether a path the file tier resolves from a transcript (it expands
    `$VAR` from literal assignments) is ever used to read from disk.
15. The README says a squash merge counts when "the session merged" it; the code also requires
    the first-parent line and treats a true `Merge pull request #n` commit the same way. Do the
    three docs agree with each other and with the code on that?
16. The id-prefix lookup found no transcript from a worktree root (result 9). Pre-delta
    behaviour, probably, but it decides whether a session following `RECORD.md` from a
    worktree gets any block at all.
