# Cold pass — `quotescan`, a quote of the principal on commits touching his prompt, and `leakscan --messages`

**Board:** `docs/roadmap/160-doctrine-review-owed/1420-rule-4-cold-pass-queued-quotescan.md`
**Status:** PASS RAN, act 1 written 2026-11-15 UTC by a Fable 5.1 cold reviewer under a rule-4
off-tier orchestrator (verdict below the divider: PASS-WITH-FINDINGS, 1 MAJOR, 4 MODERATE, 5 minor,
2 notes). Act 2 (reconcile against the held sibling) pending its release. Brief written 2026-11-14
UTC by a headless Opus 5.5 brief-writer (`cclive` lists it as session `5b3a35e9`); run under the
principal's weekly Fable drain order of 2026-11-16 NZDT.

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

---

## Verdict — act 1 (cold pass, 2026-11-15 UTC)

**Overall: PASS-WITH-FINDINGS — 1 MAJOR, 4 MODERATE, 5 minor, 2 notes (QT1–QT12).** Both tools
do what their code says; the MAJOR is that the quote check, as built, does not serve the harm QK1
names, and its 2027-05-31 flip to blocking should not happen as built unless the principal rules
otherwise after the account below. `leakscan --messages` is a sound sizing tool with three read
gaps (two latent in this repo, one hostile-input), and one "read-only" hole reachable from the
command line only.

### Provenance (rule 4, V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), tier checked at selection. Worktree
  `/Users/mike/worktrees/fable/atelier-160-1420-1921/atelier`, branch detached at `76ae64e5`
  (the claim commit); the four delta commits are ancestors (checked with `merge-base
  --is-ancestor`, nothing printed). Run day 2026-11-15 UTC (`date -u`), 19:23–19:45.
- **Spawn chain:** a headless orchestrator session (Opus 5.5) started this reviewer; that
  orchestrator was itself started by drain session `21a271a5` (Opus 5.5), running the principal's
  weekly Fable drain order (he invoked `/fable-drain` on 2026-11-16 06:53 NZDT). Both are rule-4
  off-tier orchestrators: they hold the context partition, form no finding and write no severity.
  Neither is the brief-writer `5b3a35e9`, the sweep `58027096`, the author run `d0ca5d24`, nor
  anything the author run started.
- **What the orchestrator told me, in substance (process only):** the worktree and brief paths;
  read the brief in full and `REVIEW.md`; the partition (the `.deferred.md` sibling removed from
  the worktree and held elsewhere, not to be sought anywhere); the barred list; `coldsweep` for
  every sweep and commit read; write only this file, act 1 below a divider, Status line updated;
  no commit, push or write in the worktree, scratch under the session scratchpad, deleted at the
  end; no GUI; `/usr/bin/python3` for my own scripts and the worktree's tools by path; never print a
  secret or the machine's term list, read real `--messages` runs as counts by rule; live systems
  read-only (his words of 2026-11-09 quoted); `nice -n 10`, one suite at a time, `uptime` first;
  atelier is public, orchestrators by session id only, child results by count; end with the
  VERDICT/TALLY/PATH lines and stop until act 2 is released. It carried **no question about the
  delta, no pointer to where the risk lives, and no request about any finding**. No contact from
  any other session during the pass.
- **What I read:** this brief whole; `docs/method/REVIEW.md` whole; the three commits through
  `coldsweep --commit` with `--path` scoped to the non-board files (no board file, no message
  body); `tools/quotescan.py`, `tools/test_quotescan.py`, `tools/commitmsg.py`,
  `.githooks/commit-msg`, `tools/commit-msg.sample` whole; `tools/leakscan.py` lines 455–640,
  950–1100 and 3095–3460; `tools/allowmarker.py` lines 1–200; `tools/report.py` by function;
  `tools/floor.py` the quotescan entry at HEAD, `FORBIDDEN_FLAGS`/`forbidden_flags`, `MSG_CHECKS`,
  `_render`, `plan`, `commit_msg_hook_note`; `tools/namescan.py` its JSON/render block;
  `tools/attribscan.py` its regexes; `tools/README.md` lines 15–40, 636–650, 1984–2049,
  2572–2580; `docs/method/GUARDS.md` § *Which commits the hook plane reaches*;
  `.github/workflows/floor.yml` by grep; `commands/`, `skills/` listings; OWASP ASVS 5.0 V1 and
  V16 through a Haiku fetch agent (items quoted under lens 4). **Not read:** `docs/SESSIONS.md`,
  `docs/sessions/`, `docs/ROADMAP-DONE.md`, any prior verdict, the queue pointer, the three intent
  records, the sibling, any commit body. Every sweep ran through `coldsweep` with the brief's
  `--also-exclude` set; no `--include-barred`. The brief's coldsweep line names the sibling under
  `docs/roadmap/`, which matches nothing; the sibling is under `docs/reviews/`, which the default
  set bars anyway.
- **Exposure, disclosed:** my harness loaded user-level and repo instruction files and a memory
  index before the brief; none of it describes this delta. `coldsweep` printed the three commits'
  **subjects** (unavoidable with `--commit`) and the names of the board files it left out.
- **`/security-review`:** discharged by grounds. It reads the session's pending diff; this
  worktree's only pending change is the deliberately removed sibling, and the delta is landed.
  Lens 4 was worked by hand instead, below.

### The acceptance test, answered

**`quotescan`.** QK1's second counsel asks for a floor check that a commit touching the prompt
*quotes his say-so*. The build checks that the message carries the *shape* of a quotation. The two
differ exactly where QK1's harm lives: a change to his text that nobody authorised carries, by
definition, nobody's words, and a shape test cannot tell a quotation of him from a quoted file
name, a quoted error string, or a quotation of the old prompt text being removed (QA1, probed).
Warn-only, the check is a reminder, and a reminder costs nothing. Blocking, it costs only the
honest committer (a wrapped three-line quotation of him fails the regex; two one-word quotes on
one line pass), so the flip turns a harmless prompt into a gate that stops the wrong people. The
delta is candid that it reads the form; the floor entry's `why` ("carries his words") and the
README heading are not.

**`leakscan --messages`.** Part (a) is built as described: whole bodies, every ref, the file-mode
rule sets, read-only, exit 2 when the log cannot be read. Three classes of line are never read
(`#`-leading lines and anything after a scissors line; whole trailer-shaped lines; text after a
`\x01` byte), and an option-shaped spec makes "read-only" false. Part (b)'s "not built, and why" is
truthfully stated (leakscan has no advisory form) and the README says the mode is not on the
message plane. The sizing figure reproduces by rule shape.

### Lens 1 — approach and assumptions (QA1–QA8 and my own)

Load-bearing assumptions I named before reading the brief's list: (i) the form of a quotation is
evidence; (ii) the commit message is where say-so lives; (iii) `git diff-tree <sha>` lists what a
commit changed; (iv) a committed message needs the same cleaning as a hook's message file; (v) a
trailer line is identity and nothing else; (vi) `git log <spec>` is a read; (vii) the record
separator cannot occur in a message; (viii) one path is his text.

- **QA1 — DAMAGED.** `carries_quote` battery (22 cases, scratch): QUOTE a quoted file name with a
  space, a quoted error string, a quoted command, two one-word quotes on one line (the span
  *between* them matches), a quotation of someone else, a quotation of the old prompt text, a `>`
  line from a pasted diff, a `>` line from an email reply, a quote in the subject alone, an empty
  `" "`, a JSON snippet, a two-line wrapped quote. NOT a quote: a three-line wrapped quotation, a
  single-quoted or curly-single-quoted span, a quote across a blank line, inline code, a fenced
  block. Real history (counts only): of the 8 prompt commits the tool reads as quoted, 5 are
  satisfied by a 2–3-word span and 3 by 4+ words; of the 10 it reads as unquoted, 1 carries a
  double-quoted quotation wrapped over three or more lines and 2 carry a single-quoted multi-word
  span. A check the author can satisfy by typing two quotation marks does not answer QK1; the
  warn-only period makes that harmless, the date makes it harmful. → QT1.
- **QA2 — partly confirmed.** The msg plane reads the index git set for the hook (confirmed by a
  real hook in scratch: a path-scoped commit sees only what it named; the delta's amend claim
  holds, Q6). Routes around it, probed: `--no-verify` commits (Q7); a clone with no hook (the
  floor prints `commit_msg_hook_note` once, read); a message-only amend of a prompt commit drops
  the quote and the hook sees no guarded path (Q6; → QT6); a rebase or cherry-pick (no hook,
  `GUARDS.md` table, read); a move of the prompt is reported once as a deletion and the new path
  is unguarded after (Q4, by design); an edit through a symlink shows as the target path and is
  caught (Q5). Each lands on the CI plane, which only reports.
- **QA3 — DAMAGED.** `commit_files` runs `diff-tree` without `-m`: a merge commit lists no paths
  (scratch Q1b: a merge that edits the prompt itself is clean). On any git failure it returns `[]`
  (Q2): silence, not exit 2. Real history: `git log -- <prompt>` lists 19 commits, 1 a merge in
  which the prompt differs from every parent; the tool reads 18. A depth-1 clone's boundary commit
  "touches" every file under `--root` (Q3); atelier's workflow uses `fetch-depth: 0`, so not live.
  A force-push falls back to `HEAD^..HEAD` with a note (read). → QT5, QT12.
- **QA4 — confirmed.** A sweep for "his text / his words / the principal's prompt" across the tree
  (coldsweep, barred set excluded) finds the prompt named as the run prompt (`README.md`) and his
  words quoted inside doctrine, ADRs and the personal-data list, none of which is "his text" as a
  file. No second copy of the prompt's opening lines exists outside
  `docs/method/session-open/`. One path is the honest set.
- **QA5 — partly confirmed.** The mode runs the term list, the structural rules, `--disable`,
  `--require-terms` and the empty-list warning exactly as file mode (I4; `scanned_local_terms`
  false with a warning). `.leakscanignore` is path-based and cannot apply. **Secret shapes** are
  secretscan's, not leakscan's: `320/550`'s proposal named them and the delta does not say they are
  out of scope. Three line classes are never read (QT2, QT3, QT9).
- **QA6 — DAMAGED.** `--messages=--output=<path>` reaches `git log` as an option: it wrote a file
  and reported `0 finding(s) in 0 of 0` at exit 0 (I1). The bare form `--messages --output=…` is
  refused by argparse (P6). `nargs="?"` swallows no following flag (P7); a path positional is
  refused, exit 2 (P8). The report carries no file-mode tally (read). The JSON `clean` is
  "no findings" and the text head says "Read-only: this never blocks": exit 0 cannot be mistaken
  for clean by a reader, and `FORBIDDEN_FLAGS` keeps it from a child's `flags` (I checked
  `forbidden_flags` judges `--x=y` by name). → QT4.
- **QA7 — DAMAGED.** `AUTHOR_TRAILER_RX` drops whole lines by prefix, anywhere in the body, any
  case, leading whitespace allowed: a `Co-Authored-By:` naming a second person, and a body line
  `reviewed-BY:` carrying an address and a term, are never read (P3, P3b). Real history: 2,237
  trailer lines skipped, scanned apart: email hits only, one redacted identity, no other rule. The
  skip loses nothing in this repo at this commit; the design loses the class the repo's own hard
  constraint names (any other person's name). → QT3.
- **QA8 — confirmed, with a wording gap.** `QUOTE_WARN_UNTIL` is a constant compared with the UTC
  clock; `--warn` is absent from the msg template and forbidden in a child's `flags`. Fleet probe
  (scratch copy of `tools/`, `_utc_today` patched to 2027-05-31; the worktree untouched): 22 child
  checkouts discovered, 0 archived, 0 hold the guarded path; `--range HEAD^..HEAD --warn` and
  `--message-file` on the live index, both dates: 22 of 22 exit 0 on each. The CI plane exits 0 by
  construction and the msg plane trivially where the path is absent, so the probe shows the flip is
  a no-op for every child; it is not evidence about the one repo that holds the path. A repo's
  `advisory` declaration selects the `--warn` template and the block never happens: dated,
  visible, and not what "no config key moves it" suggests. → QT7(e).

### Lens 2 — correctness and quality

- Re-run ledger below: every brief line reproduces; 14 + 7 + 10 tests OK, selftest OK.
- **Re-measured figures.** "19 touch, 8 carry a quote (42%)": `git log -- <prompt>` gives 19
  (`--full-history` 39, 21 of them merges); the tool reads 18 touching, 8 quoted, 10 unquoted
  (44%); `--range HEAD` reports 10 findings. "1 in 120": 19 of 2,335 commits on HEAD is 1 in 123.
  "2,302 messages, 4 hits in 3 (3 structural, 1 term)": 2,343 messages across all refs (2,335 on
  HEAD), 4 findings in 3 messages, by rule 2 email, 1 nz-address, 1 local-term; reproduced by
  shape. "21 of 21": 22 of 22 (one more checkout discovered). "Tests: 14": 14.
- **Mutation (scratch copy, suites unchanged).** quotescan: one-word quotes accepted, flip day
  `<=`, bare marker accepted, `GUARDED` emptied, range plane ignoring paths, inline code kept — all
  six fail the suite. leakscan `CommitMessages`: trailer skip removed, markers honoured, unreadable
  log read as clean — all fail; **survive:** `messages_with_findings` counting findings not
  messages, and the `--all` default changed to `HEAD`. → QT10.
- **Overclaims**, each against the text that makes it. → QT7.
- Hostile input: a 2 MB single-line message scans in 0.4 s; a `\x01` byte truncates (QT9);
  control and bidi characters in an excerpt are dropped (`safe_text`, P9); git's error text goes
  through `report.broken`, which strips controls (the `nosuch..HEAD` line, re-run).

### Lens 3 — completeness and harvest

- **V3 sweep.** No surface still says no scanner reads a commit message except the hand-up item's
  own title in the board index (barred, by file name only). The README's "What these scans cannot
  see" (line 15 block) does not mention messages; the `--messages` subsection sits under leakscan
  and says plainly it is not on the message plane. `quotescan` sits beside `namescan` on every
  surface that lists it (`tools/README.md`, `commitmsg.py`, `floor.py`, `test_floor.py`,
  `test_allowmarker.py`) except `tools/test_precommit.py`, which names namescan as the example
  that warns before its date; a one-check example, not a list. No doctrine, skill or template
  lists the message-plane checks, so none is missing one.
- **Conventions.** Marker grammar via `allowmarker` with `SEP_ANY_SPACE`, as siblings;
  advisory-count line printed with the zero; broken-scan exit 2 (except QT4/QT5's silences);
  `QUOTE_WARN_UNTIL` four weeks after `NAME_WARN_UNTIL` (2027-05-03 + 28 days, checked). The README
  heading carries "warning until" like `attribscan`, `namescan`, `pdlistscan`. `attribscan`'s
  `_QUOTE_RX` accepts any two characters between quotes and is used to *downgrade* a claim, not to
  satisfy a gate; `quotescan` is the first sibling where the form opens a gate. The hook and its
  sample are byte-identical (stamped copy, V4).
- Harvest missed: the exception register's `ref` pattern (a tracked path to the record holding
  his words) already exists as the house's way of pointing at say-so; the quote check does not use
  it (counsel under QT1).

### Lens 4 — security and privacy (V6; ASVS 5.0 items fetched, not recalled)

- **Command execution** (ASVS V1.2.5, "operating system calls use parameterized OS queries"):
  every git call is a list, no shell. **Option injection** (V1.3.3, "data being passed to a
  potentially dangerous context is sanitized beforehand"): the user spec is passed unsanitised and
  `git log` takes it as an option in the `=` form (QT4); the CI plane's base comes from the event
  file, validated by `SHA_RX` with the all-zero SHA refused, and `pushed`/`HEAD^..HEAD` are
  constants; `GITHUB_EVENT_PATH` is read once, JSON errors caught.
- **Output encoding and log injection** (V1.1.2; V16.4.1, "logging components appropriately
  encode data to prevent log injection"): quotescan prints a 12-character sha, constant paths, a
  constant note; leakscan `--messages` prints the sha, a line number, a rule name and a redacted
  excerpt through `safe_text` (P9: escape and bidi characters dropped); `report.broken` strips
  controls from git's stderr. No printed field carries raw message text.
- **Sensitive data in output** (V16.2.5, "may only be logged by being hashed or masked"): a term
  excerpt is `term:` plus two characters; structural excerpts are redacted (P5, JSON path too,
  which no test covers); a term never reaches stdout, stderr or JSON in the probes; my real run
  was read as counts by rule and nothing else. The private term list is read by path and never
  printed.
- **Design altitude.** The tool reads every ref's message against the private list on a developer
  machine and prints redacted hits: the exposure is the operator's terminal, as for file mode. The
  trailer skip is the one *privacy* design defect: it treats every trailer-shaped line as public
  identity (QT3).
- **Hostile input:** QT9 (`\x01`), 2 MB line fine, NUL cannot be in a git message.

### Standing checklist V1–V7

- **V1** — not held: the "19 touch, 8 carry a quote" figure, the exit-code claim, the `why`, the
  fleet claim and the "no config key" sentence each say more than the code does (QT7).
- **V2** — every live-proven claim re-run (ledger below); all reproduce by shape, figures moved
  with history (QT7a is a measure mismatch, not a stale proof).
- **V3** — swept (lens 3); no stale mirror found.
- **V4** — one home for message reading (`commitmsg`); the hook and sample are a stamped pair.
  The cleaning rule has one home and is misapplied from it (QT2).
- **V5** — the docstring ("reads the FORM") contradicts the floor `why` and README heading
  ("carries his words") (QT7c). The README's exit-code line contradicts `commit_files`'s silence
  (QT7b). Cross-references checked for the rule reached: `160/900` QK1 and `320/810` are quoted
  in the brief's acceptance test and match the docstring's account; `320/080` ("the corpus
  problem") is named by the docstring only and was left unread as a board item outside scope.
- **V6** — lens 4 above, `/security-review` discharged by grounds.
- **V7** — provenance above; the brief's provenance section and this one agree.

### Findings

**QT1 — MAJOR — Bears on the flip: the check reads a shape, not his say-so, and on 2027-05-31 the
shape starts blocking.** Grounds: QA1 battery and real-history counts above. The build is honest
that it reads the form; the item's harm (unauthorised changes to his text) is untouched by a form
test, since an unauthorised change carries no words of his and the check cannot tell. Warn-only it
is a reminder; blocking it stops a committer who wrapped a real quotation and passes one who quoted
a file name. *Counsel:* keep it warn-only with no date until a check that reads say-so exists; or
replace the form with a reference the house already uses, the exception register's `ref` shape (a
tracked path, or a board item id plus a date, to the record holding his words), which a reviewer
can follow and a shape test cannot fake; at minimum require the span be four or more words, allow
single and multi-line quotes, and exclude a span that is also the old prompt text.

**QT2 — MODERATE — `commitmsg.commits()` cleans already-committed messages with `#` as comment
char, so `#`-leading lines and anything after a scissors line are never scanned.** Grounds: P1
(term on a `# heading` line: 0 findings), P2 (term after a scissors line: 0), Q8 (a quote on a `#`
line is lost on quotescan's CI plane). Git's cleanup ran at commit time; `-m` and `-F` keep `#`
lines as content. Real history: 38 such lines in 17 of 2,343 messages are unread; scanned apart
they carry 0 findings, so the gap is latent here. *Counsel:* in `commits()` use `%B` as git gives
it; `clean()` belongs to the hook's file only.

**QT3 — MODERATE — The authorship-trailer skip drops any trailer-shaped line, anywhere, whatever
it carries.** Grounds: P3 (a second person's name and address in `Co-Authored-By:`: 0 findings),
P3b (an indented, mixed-case `reviewed-BY:` body line with an IPv4 and a term: 0). "Published
identity" is true of the author's own trailer; the repo's hard constraint forbids any other
person's name, and that is what a co-author trailer carries. Real history: 2,237 trailer lines,
email hits of one identity only, so nothing lost at this commit. *Counsel:* skip only the known
identity (exempt the author's exact address, or scan trailers with `email` disabled for that
value), or scan everything and let the one identity be the known, counted noise.

**QT4 — MODERATE — An option-shaped spec makes "read-only" false and reports clean.** Grounds: I1
`--messages=--output=<path>` and I2 `--range=--output=<path>`: `git log` wrote the file; leakscan
reported `0 finding(s) in 0 of 0` and exit 0, quotescan "clean". A `--since=` spec would read
nothing and report clean the same way. Reach: the command line only; a child's `flags` cannot
(`FORBIDDEN_FLAGS` judges `--x=y` by name, checked) and CI passes constants. ASVS V1.3.3.
*Counsel:* refuse a user spec that starts with `-` (the `--all` const is the tool's own, not the
user's), or pass `--end-of-options` before a user spec; treat `0 of 0` with a non-empty spec as a
note, not a clean line.

**QT5 — MODERATE — The CI plane cannot see a merge commit's own change, and a `diff-tree` failure
is silence.** Grounds: Q1b (a merge that edits the prompt itself: clean), Q2 (`commit_files` on
an unreadable sha: `[]`). Real history: 1 of the 19 prompt commits is a merge in which the prompt
differs from every parent; the tool reads 18. Rebased, cherry-picked and merged commits are
exactly the ones only CI reads (`GUARDS.md`). *Counsel:* `diff-tree -m` (paths changed against
any parent) and raise on a non-zero exit so `scan_range` exits 2.

**QT6 — minor — Bears on the flip: a message-only amend removes the quote and the hook sees no
guarded path.** Grounds: Q6 through a real hook. Commit with a quote, `commit --amend -m` without
it: the final message carries no quote, only CI (report-only) sees it. The docstring calls the
amend reading right; on the blocking plane it is a two-command route around the block.
*Counsel:* record it in the docstring and README as a known route, beside `--no-verify`; a hook
cannot tell an amend apart.

**QT7 — minor — Overclaims, each against its text.** (a) Docstring, README and CHANGELOG: "19
commits touch the prompt, 8 carry a quote (42%)" states `git log`'s count as the tool's measure;
the tool reads 18 and cannot see the 19th (QT5). (b) README and docstring "Exit codes … `2` the
scan is broken" against `commit_files` returning `[]` and an option-shaped spec reading nothing at
exit 0 (QT4, QT5). (c) Floor `why` "carries his words" and README heading against the docstring's
"reads the FORM". (d) CHANGELOG "21 of 21 exit 0 … on the flip date": true by construction on
both planes where the path is absent; evidence of a no-op for children, not of safety for the
repo that holds the path (now 22 of 22). (e) Docstring "no flag, environment variable or config
key moves it": the date does not move; a repo's `advisory` declaration keeps the check warn-only
past it, dated and visible. Say so.

**QT8 — minor — Two meanings of `clean` in one delta's JSON.** quotescan's `"clean": not blocks`
is true with findings in the warn period and always on the CI plane (Q9: `clean true, findings 1`);
leakscan `--messages`'s `"clean": not findings`. quotescan follows namescan, so the split is
between the message-plane checks and leakscan. *Counsel:* name the field `blocking` and drop
`clean`, or define `clean` once in `report.py`.

**QT9 — minor — A `\x01` byte in a message truncates it silently.** Grounds: P4, P4b: text after
the byte is never scanned and the message still counts as read. The record separator is a byte
git allows in a message. Real history: 0 such messages. *Counsel:* `git log -z` with a format
free of `%x01`; NUL cannot occur in a message, so it is the one safe separator.

**QT10 — minor — Test gaps.** No test pins the `--all` default or `messages_with_findings` as a
count of messages (both mutants survive); none covers the JSON excerpt (P5 shows it redacted),
a `#`-leading or trailer-shaped body line carrying a term (QT2, QT3), a merge on the range plane
(QT5), or a message-only amend (QT6). quotescan's suite caught every mutant tried.

**QT11 — note — `--all` reads stashes, remote-tracking refs and unpushed branches** (P13: a
stash message with a term counted), a conservative over-count against `320/550`'s "all pushed
refs", and it misses refs not fetched. The README's "every ref" is accurate; the sizing use case
wants the pushed set named.

**QT12 — note — A depth-1 clone's boundary commit "touches" every file** (`--root`; Q3), so a
shallow CI would report every push as an unquoted prompt change. atelier's workflow fetches full
history; a child that overrides depth would see noise, never a false clear.

### Per-commit ledger

- `b74cd5ef` — read body-free: yes (`coldsweep --commit`, 7 files, no board file). Findings:
  QT1, QT5, QT6, QT7a–e, QT8, QT10, QT12.
- `49f3d407` — read body-free: yes (`coldsweep --commit`, 6 files, no board file). Findings:
  QT2, QT3, QT4, QT8, QT9, QT10, QT11.
- `ba55be27` — read: the quotescan `declares=` block at HEAD only. Findings: QT7c (the `why`;
  the `purpose_gap` is honest).
- `2a6d7a41` — read body-free: yes (`coldsweep --commit`, `tools/leakscan.py` only). Findings:
  none; a G3 comment, not the mode.
- `tools/commitmsg.py` (shared dependency, in `49f3d407`'s tree): QT2, QT5 and QT9 live there.

### Re-run ledger (2026-11-15 UTC, load 4.6–11.4, `nice -n 10`, one at a time)

- `test_quotescan` — Ran 14 tests, OK.
- `test_leakscan.CommitMessages` — Ran 7 tests, OK.
- `test_floor.MsgPlaneTest` — Ran 10 tests, OK.
- `quotescan.py --selftest` — `selftest OK — quotescan`, exit 0.
- `quotescan.py --range HEAD --root . --warn` (read as JSON) — 10 findings, exit 0; beside it
  `git log --format=%h -- <prompt> | wc -l` gives 19 and `--full-history` 39.
- `quotescan.py --range pushed --root . --warn` — clean, note "no pushed range known: reading
  HEAD only", exit 0.
- `quotescan.py --range nosuch..HEAD --root . --warn` — `git log … failed`, exit 2.
- `floor.py --plane msg --list --root . | grep quotescan` — `quotescan enforced fleet decl 1/5`,
  exit 0.
- `leakscan.py --messages --root . --json` (counts only) — 2,343 messages read, 3 with findings,
  4 findings (email 2, nz-address 1, local-term 1), `scanned_local_terms` true, exit 0.
- `leakscan.py --messages nosuch..HEAD --root .` — exit 2.
- Fleet probe by exit code, both dates — 22 checkouts, 0 archived, 0 hold the path, 22 of 22
  exit 0 on both planes.
- `floor.py --plane msg` end to end over this worktree — namescan and quotescan clean, both
  `enforced`, exit 0.

NOT RUN (would write to a real repo): a real `git commit` through the floor's hook in this
worktree; a real amend; a real merge. Each was built in a scratch repo instead (Q1–Q9).

### Follow-up checklist (the principal decides; the author applies nothing — rule 3)

- [ ] QT1 — rule on the 2027-05-31 flip: keep warn-only, change the check to read a reference,
      or flip as built with the costs above in front of him.
- [ ] QT2 — stop cleaning committed messages in `commitmsg.commits()`.
- [ ] QT3 — narrow the trailer skip to the known identity.
- [ ] QT4 — refuse or escape an option-shaped spec; stop reading `0 of 0` as clean.
- [ ] QT5 — `diff-tree -m` and fail closed in `commit_files`.
- [ ] QT6 — document the amend route beside `--no-verify`.
- [ ] QT7 — correct the five texts (18 not 19; exit-code line; `why`; fleet claim; "no config
      key").
- [ ] QT8 — one meaning of `clean` across the floor's JSON.
- [ ] QT9 — NUL-separated log format.
- [ ] QT10 — pin the `--all` default, the message count, the JSON excerpt, and the QT2/QT3/QT5/QT6
      shapes in tests.
- [ ] QT11, QT12 — a sentence each in the README.

Scratch repos, fixtures and the scratch copy of `tools/` were deleted at the end of act 1; nothing
of them is kept. Act 2 follows on release of the sibling.
