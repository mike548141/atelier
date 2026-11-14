# Cold pass — `quotescan`, a quote of the principal on commits touching his prompt, and `leakscan --messages`

**Board:** `docs/roadmap/160-doctrine-review-owed/1420-rule-4-cold-pass-queued-quotescan.md`
**Status:** BRIEF ONLY, not run. Written 2026-11-14 UTC by a headless Opus 5.5 brief-writer
(`cclive` lists it as session `5b3a35e9`). Queued, waiting on the principal's explicit approval of
Fable work; this brief is not that approval.

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Size of this pass:** small to medium. Two landing commits. `b74cd5ef` adds `tools/quotescan.py`
(222 lines) and `tools/test_quotescan.py` (188), a 17-line floor registry entry, 11 lines of floor
tests, a 24-line README section and an 11-line changelog entry (plus a 3-line `test_namescan.py`
hunk). `49f3d407` adds 68 lines to `tools/leakscan.py` (the `--messages` mode), 74 to
`tools/test_leakscan.py`, an 8-line `FORBIDDEN_FLAGS` change in `tools/floor.py`, 4 lines of floor
tests, an 11-line README section and a 9-line changelog entry. The quotescan entry's `declares=`
block from the later commit `ba55be27` is read too. The shared message reader both call
(`tools/commitmsg.py`, 149 lines) is read as a dependency.
**Why it earns a review:** both are guard code registered in, or reachable from, the floor every
child repo floats on. `quotescan` is the only mechanical guard on changes to the principal's own
text (the run prompt the queue-run command executes), and on **2027-05-31** it starts to block
commits by itself, with no edit. `leakscan --messages` is the tool a repo is told to use to size a
history rewrite before it goes public, a one-way step. The worst failures are **false clears**: a
quote check any pair of quotation marks satisfies, so "the prompt change carries his say-so" reads
true when it carries nobody's words; a commit or message the scan never read, counted as clean; and
a "read-only" sizing tool that under-counts, so a repo goes public believing its history is smaller
a job than it is. The second worst is **a leak through the check**: a message sweep whose input is
the private term list printing a term into a log.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `d0ca5d24`,
  2026-11-09 UTC, and the worker it dispatched (per the queue pointer). The author queued this pass
  and does not take it.
- **Who wrote this brief:** a headless brief-writer (`claude-opus-5-5`; `cclive` lists it as session
  `5b3a35e9`), started 2026-11-14 UTC by an estate health sweep, orchestrator session `58027096`
  (Opus), on the principal's instruction that a brief is written for every review known to be owed
  (Mike, 2026-11-14, verbatim: *"include all briefs are written where we know a fable review is
  required"*). Neither wrote any of this delta. **Off-tier for review, disclosed: the brief-writer
  forms no finding and writes no severity**, and stops after writing. It ran no review and used no
  Fable model.
- **Barred from running this pass:** session `5b3a35e9` and session `58027096` (whoever writes a
  brief does not run it), and session `d0ca5d24` with everything it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `58027096`: the
  item number, the pointer's opening sentence, and the rules of the sweep. It carried no framing of
  the work. The brief-writer had no contact with the author session or its worker.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md`; **the queue pointer whole**; **the intent
  records `160/900`, `320/810` and `320/550` whole**, including the author's landing notes on all
  three; the delta through `tools/coldsweep.py --commit` (no commit body was printed: stats were
  read with `--format='%h %s'`); `tools/quotescan.py`, `tools/test_quotescan.py`, the quotescan
  entry in `tools/floor.py` and `tools/commitmsg.py` lines 79–160 at HEAD; the test names of
  `test_leakscan.CommitMessages`; commit subjects through `git log`; the sibling brief
  `2026-11-14-0239-namescan-private-names-branches-titles-cold.md` and the first 60 lines of its
  `.deferred.md` (read for house form). It opened **no prior verdict**, and printed no
  `leakscan --messages` excerpt (its run was read through `--json` as counts by rule). Its harness
  also loaded user-level and repo instruction files and a memory index, which hold private context
  this brief does not carry. Everything evaluative it formed is in the sibling.

## The acceptance test

**`quotescan`.** An earlier cold pass on the queue-run command raised `QK1`, summarised on its
board item as: *the command runs the local clone's working tree, so uncommitted prompt text executes
with no commit, hook, test or review having seen it.* Its first counsel (the command reads only the
committed prompt) was applied separately and has its own pass (`160/1060`, a non-goal here). Its
**second counsel**, the one this builds, is recorded as: *a floor check that every commit touching
the prompt quotes his say-so*. The prompt is `docs/method/session-open/session-open-prompt.md`; the
item records that four units of his own text had been cut from it in 2026-09 without his say-so,
and were later restored on his answer.

The principal's words that commissioned the build, 2026-11-09, quoted on `320/810` (an answer,
asked which of six candidate checks to build): *"all six, warnings at first and then move to
blocking action. With a staggered turn on of each so they dont all hit at once"*. One of the six is
"a quote of him on commits touching his prompt". Those words fix three things only: the check is
built, it warns first, and it then blocks on a staggered date. **The date, 2027-05-31, is the run's
choice, not his**, and the delta says so. No ruling of his fixes what counts as "his say-so" or
"a quote": judge whether the build's reading of it serves the harm.

**`leakscan --messages`.** A hand-up finding from a child, `320/550`: *no floor scanner reads a
commit message, so a term that is caught in files lands unflagged in a message body*; a private
repo later made public publishes every message verbatim on the day of the flip. Its proposal, part
(a): *a `--messages` mode over `git log` for the same rule sets (local terms, structural shapes,
secret shapes), runnable at the pre-flip gate over all pushed refs, where it is the difference
between knowing the size of the rewrite and finding out after.* Part (b), the same rules on the
commit-message plane, is **not built**, by the delta's own account; that is a non-goal of this
pass, but whether the delta describes the gap truthfully is in scope.

## What the work is

Two landing commits on `main`, and two later commits that touch the delta. First confirm your tree
has them:

```
for c in b74cd5ef 49f3d407 ba55be27 2a6d7a41; do git merge-base --is-ancestor $c HEAD || echo "MISSING $c"; done
```

Nothing may print. If something does, merge `origin/main` into the review branch before starting,
because a tree without the delta has nothing to review. Read each commit body-free:

```
python3 tools/coldsweep.py --root . --commit b74cd5ef \
  --path tools/quotescan.py --path tools/test_quotescan.py --path tools/floor.py \
  --path tools/test_floor.py --path tools/test_namescan.py --path tools/README.md \
  --path CHANGELOG.md
python3 tools/coldsweep.py --root . --commit 49f3d407 \
  --path tools/leakscan.py --path tools/test_leakscan.py --path tools/floor.py \
  --path tools/test_floor.py --path tools/README.md --path CHANGELOG.md
python3 tools/coldsweep.py --root . --commit 2a6d7a41 --path tools/leakscan.py
```

Plain `git show` (and `git show --stat`) is barred: it prints the message body before the diff, and
reading is atomic (rule 1). Always pass `--path`: both landing commits also edit board items, which
are barred below. `2a6d7a41` is a comment-only change near G3 in `leakscan.py`, read to confirm it
does not touch the mode. For `ba55be27`, read only the `quotescan` entry's `declares=` block in
`tools/floor.py` at HEAD.

Review `tools/quotescan.py`, `tools/test_quotescan.py`, the `--messages` path in
`tools/leakscan.py` (`_main`'s argument and dispatch, `AUTHOR_TRAILER_RX`, `scan_messages`,
`report_messages`) and `test_leakscan.CommitMessages` at HEAD, and read what they call as far as
they depend on it: `tools/commitmsg.py` (`read_message`, `clean`, `comment_char`, `staged_files`,
`commits`, `commit_files`, `pushed_range`, `_event_base`), `leakscan.scan_text` and its excerpt
redaction, `allowmarker.marker_rx` and `allowmarker.present`, `report.safe_text`,
`report.broken` and `report.guarded_main`, `floor.FORBIDDEN_FLAGS` and `.githooks/commit-msg`.
On 2026-11-14 UTC no commit after `b74cd5ef` had touched either quotescan file, and none after
`49f3d407` had touched `tools/commitmsg.py` or `.githooks/commit-msg`. Confirm what has landed
since:

```
git log --oneline b74cd5ef..HEAD -- tools/quotescan.py tools/test_quotescan.py
git log --oneline 49f3d407..HEAD -- tools/leakscan.py tools/test_leakscan.py tools/commitmsg.py .githooks/commit-msg
git log --oneline b74cd5ef..HEAD -- docs/method/session-open/session-open-prompt.md
```

## What the delta claims (extracted, not evaluated)

**`quotescan`**

- **What it asks:** a commit that carries a path in `GUARDED` (one today, the prompt) has, in its
  message, a double-quoted span of two or more words, straight or curly, or a `>` line; inline code
  is removed first. Or a reasoned `quotescan:allow: <reason>` line.
- **What it does not claim:** that the quotation is real or is his. "It reads the form, never whose
  words they are" (`320/080`'s problem). The registry's `purpose_gap` says the same.
- **What it reads:** on the message plane, the message git hands the `commit-msg` hook and the
  paths staged in the index git has set for the hook, so a path-scoped commit sees only what it
  named; a message-only amend carries no guarded path. On the CI plane, every commit in the pushed
  range and the paths each changed.
- **The date cannot be moved:** `QUOTE_WARN_UNTIL` (2027-05-31) is compared with the UTC clock;
  no flag, environment variable or config key moves it. Before it a message-plane finding exits 0;
  on and after it, exit 1 unless `--warn`. The CI plane only reports, at any date.
- **A bare marker exempts nothing;** a mechanical edit (a renamed link, a reflow) is what the
  marker is for.
- **A broken scan is not a pass:** an unreadable range exits 2.
- **Measured at landing:** "19 commits touch the prompt, 8 carry a quote (42%)", "about 1 in 120
  commits meets it"; a fleet probe by exit code, date patched: 21 of 21 exit 0 on the landing
  date (2026-11-10) and on the flip date, and only atelier holds the path. "Tests: 14".
- **The registry tells the truth:** no hook template, `--warn` on CI only, an advisory form a
  child may declare, the advisory-count line printed on every run, zero included, and `MSG_CHECKS`
  naming it.

**`leakscan --messages`**

- **What it reads:** every commit message in `REVS` (default every ref, `--all`), whole bodies,
  through "the same rule sets as a file". Authorship trailers (`Co-Authored-By:` and four others)
  are skipped, as published identity.
- **Read-only:** it reports and exits 0 whatever it finds; 2 if the log cannot be read. It takes
  no paths, and neither `--staged` nor `--binary-entries`.
- **A marker in a message exempts nothing** (`honour_markers=False`).
- **A child cannot reach it:** `--messages`, `--message-file` and `--range` join
  `FORBIDDEN_FLAGS`, so a child's `flags` cannot turn a floor run into a guaranteed pass.
- **Measured at landing:** "Over atelier's 2,302 messages: 4 hits in 3 messages (3 structural,
  1 term)"; "2,198 of the first run's 2,200 hits" were one authorship email before trailers were
  skipped.
- **Part (b) not built, and why:** leakscan "has no advisory form, so it would block every message
  body from day one with no warn-first period".

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour on this machine. The lenses organise it; they do not bound it. Anything not named a
non-goal is in scope.

**Non-goals:** the commit-message plane itself (`.githooks/commit-msg`, `floor.py --plane msg`,
`tools/commitmsg.py` as a design), which is `160/1390`'s pass; `namescan` (`160/1410`); the
queue-run command reading only the committed prompt, QK1's first counsel (`160/1060`); `320/550`
part (b), unbuilt; the other checks of `320/810`; and the floor-wide declarations work of
`ba55be27` beyond the quotescan entry. Each is read here only as far as this delta depends on it.
A defect in a shared helper that changes this delta's result is in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, then attack at least
   these by probe:
   - **QA1.** A quotation's **form** is meaningful evidence of the principal's say-so (the item's
     first question: "whether any quotation marks at all satisfy it"). Probe what satisfies
     `QUOTE_RX` and `BLOCKQUOTE_RX`: a quoted file name or error string, a quoted command, two
     separate one-word quotes on one line, a quotation of someone else or of the old prompt text,
     a `>` line from a pasted email or diff, a quote inside the subject. Then ask whether a check
     the author can always satisfy by typing two quotation marks answers QK1 at all, and whether
     the warn-only period and the date change that answer.
   - **QA2.** The commit is the right place to read his say-so. The harm in QK1 is prompt text
     executing that no commit, hook or review has seen; this reads commits. Probe the routes by
     which the prompt changes without the hook seeing a guarded path: a clone without the
     `commit-msg` hook, `--no-verify`, a merge commit that brings in a prompt change, a rebase or
     cherry-pick that rewrites messages, a rename or move of the prompt, an edit through a
     symlink or a second path to the same text.
   - **QA3.** The CI plane reads every commit in a pushed range. Probe merges (`commit_files` uses
     `git diff-tree` without `-m`), a shallow clone, a force-push, and what happens when
     `commit_files` cannot read a commit: is that a finding, a broken scan, or silence?
   - **QA4.** `GUARDED` is the right set: one path, "the only file the record calls his text".
     Check that claim against the tree (is any other file his text, by the repo's own records?).
   - **QA5.** `leakscan --messages` applies "the same rule sets as a file". Compare against
     `320/550`'s proposal (local terms, structural shapes, **secret shapes**) and against what
     leakscan's file mode does with the same text (`--staged`, the ignore file, the disabled-rule
     list, local-term loading and `--require-terms`). Probe with a synthetic term list and a
     synthetic history.
   - **QA6.** `--messages` is read-only and reports only its own findings (the item's second
     question). Probe whether any spec can make `git log` write (an option-shaped `REVS`, for
     example `--output=<path>`), whether `nargs="?"` swallows a following positional or flag,
     whether file-mode tallies or warnings leak into its report, and whether exit 0 on hits can be
     mistaken for "clean" by any caller in the floor.
   - **QA7.** Skipping authorship trailers loses nothing. Probe a trailer-shaped line that carries
     a term or a private address, and the case-insensitive prefix match.
   - **QA8.** The 2027-05-31 flip is safe for every repo in scope on the day, and the date cannot
     move.
2. **Correctness & quality.** Diff each commit; drive both tools against scratch repos you build,
   with a synthetic term list of your own, and quotescan with the date patched across the flip.
   Re-measure every figure the delta states (19, 8, 42%, "1 in 120", 2,302, "4 hits in 3
   messages", 21 of 21). Record each overclaim against the text that makes it: the module
   docstring, help text, README sections, floor entry comment, `why` and `declares=` block, and the
   `CHANGELOG.md` entries. Check the tests would fail on a broken change: mutate a scratch copy,
   never the worktree.
3. **Completeness / harvest.** Every surface that states the same fact (V3): does any doctrine,
   README or skill text still say no scanner reads a commit message, or describe either tool's
   cover more widely than it is? One home (V4); no contradiction between docstring, README, floor
   comment and code (V5). Compare with siblings' conventions (allow-marker grammar, advisory-count
   line, broken-scan exits, warn-first date constants, `attribscan`, which also reads a form of
   quotation). Is `quotescan` listed wherever the other message-plane checks are?
4. **Security & privacy** — mandatory. `leakscan --messages` reads the private term list over
   every message on every ref: check that no term, nor an identifying slice of one, reaches
   stdout, stderr or `--json`, and what its excerpt redaction actually redacts. Check
   terminal-control and bidi sanitising on every printed field of both tools (excerpt, `where`,
   paths, the pushed-range note, git's own error text echoed through `report.broken`). Check
   option injection through `--range` and `REVS`, which are handed to `git log`. Check what a
   hostile message (huge, binary, NUL or `\x01` bytes, which `commitmsg` uses as separators) does
   to the parser and the regexes. Check the `GITHUB_EVENT_PATH` read on the CI plane. Check against
   OWASP ASVS input-handling, output-encoding and logging items, checked, not recalled.
   `/security-review` reads the session's pending diff, not this delta: aim it only at a scratch
   clone holding the delta as pending changes, or discharge it by grounds.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once on 2026-11-14 UTC, from the worktree
root unless it says otherwise, in the foreground, under a load average near 5.5 on this machine;
its results are held in the sibling. Read exit codes explicitly. `python3` on `PATH` is 3.14.6 and
git is 2.50.1 on this machine.

- `cd tools && python3 -m unittest test_quotescan; echo $?`
- `cd tools && python3 -m unittest test_leakscan.CommitMessages; echo $?`
- `cd tools && python3 -m unittest test_floor.MsgPlaneTest; echo $?`
- `python3 tools/quotescan.py --selftest; echo $?`
- `python3 tools/quotescan.py --range HEAD --root . --warn` (every commit in history: the
  landing's "19 touch, 8 carry a quote", re-measured; compare with
  `git log --format=%h -- docs/method/session-open/session-open-prompt.md | wc -l`, and with
  `--full-history`)
- `python3 tools/quotescan.py --range pushed --root . --warn; echo $?`
- `python3 tools/quotescan.py --range nosuch..HEAD --root . --warn; echo $?`
- `python3 tools/floor.py --plane msg --list --root . | grep quotescan`
- `python3 tools/leakscan.py --messages --root . --json` read **as counts only** (messages read,
  messages with findings, findings by rule, `scanned_local_terms`); never print the findings list
- `python3 tools/leakscan.py --messages nosuch..HEAD --root . >/dev/null 2>&1; echo $?`
- The changelog's fleet claim for quotescan: a probe by exit code over every local child checkout,
  on your run date and with the date patched to 2027-05-31. Read-only; report counts only.

Use `cd tools && python3 -m unittest test_<name>`, never the dotted `tools.test_<name>` form, which
raises `ModuleNotFoundError` here. Run the tools from your worktree, never by bare name from `PATH`.

## House rules for this run

**Live systems:** read-only. The runs over this repo's history and the fleet probe over local child
checkouts are reads, and both are in scope. A `leakscan --messages` run over a child checkout is a
read too, but report it by count only. Any probe that would write to a real repo or forge
(staging, committing, pushing, installing a hook, editing a board, rewriting history) is **NOT
RUN**: build the case in your scratchpad (scratch repos, a synthetic term list, a scratch copy of
the tool with the date patched) and say which probes you could not build.

- **The machine's term list is private, and so are this repo's message hits.** Run the tools with
  it where a probe needs real coverage, but never open, print, quote or count-by-term it, and
  never write a term anywhere. `leakscan --messages` over a real repo prints redacted excerpts:
  read it through `--json` as counts by rule, and never paste an excerpt or a commit id of a hit.
  Probes of output leaks use a synthetic list you write in your scratchpad. If a real run's output
  shows anything that looks like a term, stop, record the finding by shape only, and do not paste
  the output.
- Never print a secret, and quote no line from a child repo. This repo is PUBLIC: report child
  results by count only, and name no child, host, client or private path.
- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions are live on this machine: touch nothing outside your worktree and scratchpad, and delete
  your scratch repos and fixtures when you finish.
- No git command that writes in the worktree beyond committing this one file at the end of each
  phase (or handing it to an orchestrator to commit). Never mutate the worktree's `tools/`.
- One heavy process at a time, foreground, long timeout, `uptime` first.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Skip the session-log step of the repo's read order: `docs/SESSIONS.md` is barred (below).
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/` (the earlier pass that raised `QK1` included), the queue pointer above,
this brief's sibling `docs/reviews/2026-11-14-0322-quotescan-and-leakscan-messages-cold.deferred.md`,
the four delta commits' message bodies, the pointer of QK1's first-counsel pass (`160/1060`), and
the three intent records whole:
`docs/roadmap/160-doctrine-review-owed/900-rule-4-cold-pass-queued-queue-run-carries-the-brief.md`,
`docs/roadmap/320-child-filed-findings-via-pointing-up/810-build-six-checks-warn-first-staggered.md`
and
`docs/roadmap/320-child-filed-findings-via-pointing-up/550-no-scanner-reads-a-commit-message-body.md`.
Each carries the author's landing account under the finding and the proposal, and reading is
atomic, so none can be read in part. What you need from them is quoted in *The acceptance test*
above.

The delta's own text carries the author's account of why (the docstrings, the README sections and
the floor entry's comment above all); it is the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1420-rule-4-cold-pass-queued-quotescan.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/900-rule-4-cold-pass-queued-queue-run-carries-the-brief.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1060-rule-4-cold-pass-queued-queue-run-reads-the-committed-prompt.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/810-build-six-checks-warn-first-staggered.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/550-no-scanner-reads-a-commit-message-body.md \
  --also-exclude docs/reviews/2026-11-14-0322-quotescan-and-leakscan-messages-cold.deferred.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, the
assumptions QA1–QA8 and your own, and the re-run list. Append your verdict below a `---` divider in
THIS file: provenance repeated (how you were spawned, your tier, what you read, the UTC day you ran
on), per-lens answers, the standing checklist V1–V7 each answered or discharged with grounds, each
load-bearing assumption damaged or confirmed with its probe, a per-commit ledger (`b74cd5ef`,
`49f3d407`, `ba55be27`, `2a6d7a41`: read body-free yes/no, findings by id), findings with stable IDs
(prefix `QT`: `QT1`, `QT2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit bodies;
append `### Reconcile` beneath your verdict: per-finding notes against the sibling and the author's
account, any finding formed at reconcile marked as such, and the overall line restated. Never revise
act-1 text. Then fold the sibling in below the reconcile and delete it.

**Who applies a finding.** Both tools are self-authored guard code; `quotescan` will block commits
on its date and guards the principal's own text, so this is doctrine by function (rule 3): **the
author applies nothing on its own**. Record all findings; they are the principal's to decide, after
a plain-language account. Counsel per finding is welcome, labelled as counsel and kept beneath it,
and a finding that bears on whether the 2027-05-31 flip should happen as built says so in its first
line.
