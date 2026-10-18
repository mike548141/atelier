# Cold pass — staged findings reported at their real file line in conflictscan and leakscan

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-17 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/830-rule-4-cold-pass-queued-staged-real-line-numbers.md`.
**Why it earns a review:** it changes the data shape two blocking guards scan on the
pre-commit hot path — the guard that keeps personal data out of a public repo and the
guard that keeps conflict markers out of every child — and every child's hook runs
it at its next commit.

## Spawn provenance

- **Author of the work under review:** the queue run whose intent record is dated
  2026-10-16 15:01 UTC (an Opus orchestrator with dispatched workers; the pointer
  counts the workers' output as the run's authorship; the commit's trailer names a
  Sonnet model). Not opened here.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched on
  2026-10-17 by the Mike-opened Fable review session working in worktree
  `atelier-review-1017`, on Mike's 2026-10-16 answer that a fresh Opus session writes
  these briefs. It authored none of the delta. It is **off-tier for review,
  disclosed: it forms no finding and writes no severity**, and it stops after this
  brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that
  passes rule 4's criterion. The reviewer repeats its own provenance in its
  verdict.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This
  brief-writer read: the four queue pointers it was assigned (160/820–850) in full,
  and 160/500 in full as the shape of an append line; the first lines of pointers
  160/790, 160/800 and 160/860; the landing commit's subject, `--stat`, diff **and
  message body** (the author's own account); the merge's re-merge diff stat (board
  and record files only); the subjects and `--stat` of later commits on the same
  files; two 2026-10-16 briefs in full as templates, one of them for a neighbouring
  leakscan pass (its list of later commits names this delta); `docs/reviews/`
  filenames and filename-level greps (no prior verdict opened); the title lines of
  the commissioning board items; single grep-hit lines from `tools/secretscan.py`
  and `tools/report.py` locating the staged readers; and its harness-loaded memory
  index. It did not open the intent record, `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md` or `docs/method/REVIEW.md`. What its orchestrator read is
  the orchestrator's to disclose; it passed on an instruction file, three
  templates and a list of taken prefixes, and no evaluative content. Everything
  evaluative is in the sibling.

## What the work is

Landing commit (diff it; review the paths at HEAD, `b50db0c` or later):

- `f4afb7a` (2026-10-16 15:28 UTC) — tools: conflictscan and leakscan report a
  staged finding at its real file line; landed in merge `a1ba8c8` (2026-10-16
  15:31 UTC), whose own changes beyond the commit are board and record files only

Delta paths: `tools/conflictscan.py` (the new `scan_lines`, `scan_text` as its
wrapper, `staged_added_lines`, the staged branch of `_main`), `tools/leakscan.py`
(`scan_lines`'s and `scan_text`'s docstrings, `staged_added_lines`, the staged
branch of `_main`), `tools/test_conflictscan.py`, `tools/test_leakscan.py`, and the
staged-diff paragraph of `tools/README.md`.

The commit's parent is `2e2da81`, the same base as two sibling commits merged after
it (`e3e8a4f`, `72a68cc`, each its own pass); both also touch `tools/README.md`.
It builds on `39a74b9` (2026-10-16, the shared staged-diff reader
`report.staged_added`, its own pass). No later commit touches either guard file at
the time of writing; confirm at your HEAD and review the paths there.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests
and live behaviour. The lenses organise it; they do not bound it. Non-goals are the
only narrowing and are themselves reviewable.

Derive, from `report.staged_added` at HEAD, exactly which number it yields for an
added line, and test the claim "its real line number in the file the commit
produces" across diff shapes: a line below unchanged lines; two and more hunks;
hunks that also delete lines; a new file; a deleted file; a rename with edits; a
mode-only change; a file with no trailing newline; CRLF content; a git-quoted path;
an added line that looks like a diff header; a binary file. For each guard, what
the staged plane now reports and what it reported at `f4afb7a^`. Then the
behaviour beyond the number: does any rule in either guard read neighbouring
lines, carry state across lines, or depend on line 1 (a header-scoped marker, a
file-level allow, conflictscan's open-conflict state), and did handing it
non-consecutive line numbers change what it finds, not only where? Does the path
filter and `.leakscanignore`/glob handling see the same set as before? The README
now speaks for "all three guards": check the third against its code. The
whole-blob `scan_text` wrappers remain for other callers: who still calls each,
and with what numbering? **Non-goals:** the shared reader itself (`39a74b9`'s
pass) — but whatever this delta assumes about it is in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Among them: that only the reported number changes; that what held for a joined
   blob holds for a list of numbered pairs; that the whole-tree plane is untouched
   because it never used the staged reader.
2. **Correctness & quality.** Read both guards' staged paths and their tests whole;
   diff `f4afb7a`. Build a table of the diff shapes above against each guard:
   expected line, reported line at `f4afb7a^`, at `f4afb7a`, at HEAD. Check
   whether the new tests construct real staged diffs or hand-built pairs, and
   whether they would fail on the old code for the reason the test names.
3. **Completeness / harvest.** `tools/README.md` and each guard's module
   docstring; any doc in `docs/method/` that describes how a staged finding is
   located; other scanners with a staged plane that still number by blob; the
   `--json` output of both guards (does a consumer read `line`?).
4. **Security & privacy** — mandatory. These are blocking guards: hunt for any
   input on which the change makes either guard miss a finding it caught before,
   or report it against a line a person would not look at. Build fixtures from
   synthetic values only — never a real term-list entry or personal detail, and
   never quote one in the verdict. `/security-review` is discharged by grounds (a
   landed delta; the pending diff is not the work) — say so, and deliver the
   code-altitude read by hand against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest discover -s tools -p 'test_conflictscan.py' -v`, the same
  for `test_leakscan.py` and `test_report.py`; `python3 tools/conflictscan.py
  --selftest` and `python3 tools/leakscan.py --selftest`
- the staged plane, re-driven: in a scratch clone, stage each diff shape from
  *Scope* with synthetic findings and run both guards' staged mode at `f4afb7a^`,
  `f4afb7a` and HEAD; compare stdout, stderr, exit code and `--json`
- the "whole-tree output byte-identical" claim: both guards at `f4afb7a^` and
  `f4afb7a` over the repo tree and a fixture tree with findings
- the floor on both planes at HEAD; the full Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only
  git is fine. Staged fixtures, older checkouts and probes go in a private clone
  under your session scratchpad, named by your prefix — never stage anything in
  the review worktree.
- One heavy process at a time on a shared machine: the full suite at most once, in
  the foreground. Never point a scanner at any other repo on the machine.
- `/security-review` reads the session's pending diff: discharge it by grounds for
  this landed delta, or keep the tree clean whenever you spawn it.
- Never open another `docs/reviews/2026-10-17-*` brief — it is another pass's
  framing.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ
  English. Never quote a secret, placeholder token, email address or personal
  detail — this repo is PUBLIC; describe and locate instead. Fixture lines in the
  verdict are described by shape, not pasted, where they would trip the guards on
  commit.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer, this
brief's sibling `docs/reviews/2026-10-17-0955-staged-real-line-numbers-cold.deferred.md`,
the landing commit's message body (read subject, stat and diff only), and items
`300` and `310` in `docs/roadmap/115-guardrail-architecture-mike-commissioned/`
(the commissioning item, and a finding filed at the same merge on a neighbouring
behaviour).

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/830-rule-4-cold-pass-queued-staged-real-line-numbers.md
--also-exclude docs/reviews/2026-10-17-0955-staged-real-line-numbers-cold.deferred.md
--also-exclude
docs/roadmap/115-guardrail-architecture-mike-commissioned/300-two-staged-guards-report-the-wrong-line-number.md
--also-exclude
docs/roadmap/115-guardrail-architecture-mike-commissioned/310-conflictscan-open-conflict-state-runs-across-hunks.md
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never
barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, the standing
checklist V1–V7 each answered or discharged with grounds, the diff-shape table,
findings with stable IDs (prefix `RN`: `RN1`, `RN2`, …) and severities (MAJOR /
MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with
counts, a re-run ledger, and a follow-up checklist. Then STOP and commit phase 1
unrevised before opening the sibling.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict:
per-finding notes against the seeded questions and the intent record, any finding
formed at reconcile marked as such, and the overall line restated. Never revise
phase-1 text. Then fold the sibling in below the reconcile and delete it.

Findings on self-authored doctrine are the principal's to decide (rule 3; a
guard is doctrine by function): record all, apply nothing; counsel per finding is
welcome, labelled and kept beneath it.

---

## Verdict — phase 1 (RN)

Written 2026-10-17, read begun 23:39 UTC, verdict written 23:55 UTC (`date -u`).
Reviewer prefix `RN`. Phase 1 only: the sibling `.deferred.md` is unopened.

### Provenance (rule 4, V7)

- **Reviewer:** this session, running as Fable 5.1 (`claude-fable-5-1`), the
  tier the principal named (ruling 2026-08-04). Tier checked at selection; the
  stop clause did not fire.
- **Spawn:** dispatched by a Mike-opened Claude Code **cloud** session
  (`claude-fable-5-1`, orchestrating; it opened on `claude-opus-5` and Mike
  switched it to Fable before any claim or pass). That orchestrator authored
  none of the delta or this brief and was not started or instructed by their
  authors. It forms no finding and writes no severity; it holds the sibling
  outside the checkout at a path I was not given, commits this phase-1 file
  before releasing the sibling, and received one operational note from Mike's
  watching session (model, queue scope, container facts, merge instruction —
  no evaluative content about any delta). The claim line in the queue pointer
  discloses the same shape (pointer unopened by me before phase 2).
- **Author of the work:** the 2026-10-16 queue run named above; I did not
  open its intent record, the landing commit's message body, or any record.
- **Checkout:** `/home/user/atelier`, branch `claude/review-work-briefs-adj6ad`,
  HEAD `0aff4d8` = `origin/main`. Shared with other reviewers; I edited only
  this file and ran no writing git command there.

### What I read, and what I did not (exposure disclosure)

Read: `docs/method/REVIEW.md`, this brief, `docs/method/00-APEX.md`; the delta
via `git diff f4afb7a^ f4afb7a` and `git show --stat --format=%s` (subject and
stat only, body unread); `tools/conflictscan.py`, `tools/leakscan.py`,
`tools/report.py`, `tools/secretscan.py` (staged path and engine),
`tools/test_conflictscan.py` and `tools/test_leakscan.py` whole,
`tools/test_report.py` § `ParseAddedLinesTest`, the floor registry in
`tools/floor.py`, `.githooks/pre-commit`, `.github/workflows/ci.yml`,
`tools/README.md` §§ shared reader and conflictscan, `docs/method/GUARDS.md`
head and grep hits. Exposures beyond the delta, disclosed: `CHANGELOG.md`
lines 60–80 (the delta's own changelog entry — the author's account, not
barred by the brief, read before findings were formed); commit **subjects**
of other passes' review commits in `git log --graph` output (titles only, no
body, no verdict file); one grep-hit line from the non-barred board item
`320/290`; the orchestrator's note naming board items `115/350` and `130/030`
by number. The cold sweep ran with the brief's four `--also-exclude` paths
and without `--include-barred`: 56 hits over 644 files, 410 files excluded as
rule-2 barred. No prior verdict, no `docs/sessions/`, no `SESSIONS.md`, no
`ROADMAP-DONE.md`, no queue pointer, no item `300`/`310`, no other
`2026-10-16-*`/`2026-10-17-*` brief, no `drafts/`/`withdrawn/` was opened.

### Container facts that bear on this pass

- Cloud container, one checkout, no worktrees, no sibling repos, no estate
  root, no `~/.claude/`, no `gh`, no GitHub API from the shell. Nothing the
  brief asks needed any of these; no claim is marked *relayed* for that reason.
- **The checkout was shallow when I started** (`.git/shallow` held one graft,
  `c824287`): `f4afb7a` then read as *not* an ancestor of HEAD (reachable only
  through older remote-tracking refs) and `git log <sha>..HEAD -- tools/`
  listed the graft commit as "touching" every tool file. I verified the
  delta's presence at HEAD by content, not ancestry: `tools/conflictscan.py`,
  `leakscan.py`, `report.py`, `secretscan.py`, `test_conflictscan.py`,
  `test_leakscan.py` are **byte-identical** between `f4afb7a` and HEAD
  (`cmp`). The orchestrator then unshallowed the checkout (an operational
  note, no evaluative content) and I re-ran the history steps at 23:56 UTC:
  `f4afb7a` and the merge `a1ba8c8` are ancestors of HEAD; **no commit after
  `f4afb7a` touches any of the six guard paths**; only `tools/README.md` and
  `tools/test_report.py` moved, in the two sibling commits the brief names
  (`e3e8a4f`, `72a68cc`) and their merges — subjects read, bodies unread. The
  `test_report.py` hunks are sizescan/licenscan line pins, not the staged
  reader. The brief's "no later commit touches either guard file" holds at
  this HEAD. My private clone and worktrees were made before the unshallow
  and are still shallow; every probe in this verdict used objects they hold
  (`2e2da81`, `f4afb7a`, HEAD), so none needed re-running.
- Private clone and worktrees for the older checkouts: `/home/user/scratch/RN/
  clone` (HEAD), `/home/user/scratch/RN/old` (`2e2da81` = `f4afb7a^`),
  `/home/user/scratch/RN/new` (`f4afb7a`), fetched from the shared checkout's
  refs. All staged fixtures live under `/home/user/scratch/RN/fx/`; nothing was
  staged in the shared checkout.
- The hook plane's leakscan refuses here by design (no term list); I ran both
  planes and say which below.
- OWASP catalogue: `WebFetch` of the OWASP Top 10 page failed on DNS
  (`owasp.org` not resolvable through the proxy). The code-altitude threat
  list below is from memory of that catalogue and is named as such, not as a
  checked consult.

### Lens 1 — Approach & assumptions

Load-bearing assumptions, named by me before the brief's list was weighed:

1. **The reader's number is the real new-file line for every diff shape git
   emits under `--unified=0`.** Attacked by re-driving fourteen shapes
   (table, lens 2). Holds for all of them.
2. **Only the reported number changes** — same lines scanned, same rules,
   same exit codes, same tally. Holds everywhere except one input class
   (RN1): an added line whose own text contains a character `str.splitlines`
   treats as a line break. The old staged plane split it into two pseudo-
   lines and could flag a marker that is not at column 0 of any real line;
   the new plane sees one line and does not. The whole-tree plane never
   flagged it either, so the change moves the staged plane into agreement
   with the tree plane — a correction, but a behaviour change the record
   calls a pure re-numbering.
3. **What held for a joined blob holds for a list of numbered pairs.** For
   leakscan every rule is per-line and the allow-marker is per-line: holds.
   For conflictscan the open-conflict state runs across the pairs in order,
   exactly as it ran across the joined blob: holds, and the pre-existing
   consequence (state carried across unchanged, unseen lines) is unchanged —
   RN3.
4. **The whole-tree plane is untouched.** It never called the staged reader;
   re-driven byte-for-byte (lens 2): holds.
5. **Unstated: the staged reader reads the index of the `--root` repo.** It
   does not — it reads the index of the process cwd (RN2, pre-existing). The
   hook plane is unaffected because git runs hooks at the top level; the
   delta's own tests pass only because they `chdir` into the fixture repo.

Design altitude: reporting the line in the file the commit produces is the
right target — it is the line a person opens. No cheaper alternative gives
that. The brief's account of what the work is matches the diff.

### Lens 2 — Correctness & quality

**Diff-shape table.** Each shape is a real scratch repo with a committed base
and a staged change; findings are synthetic (a conflict opener/closer/
separator; a private-key header; a made-up word in a synthetic term list; an
AWS-access-key-shaped token). Columns are the reported `line` at each tool
version; `cs` = conflictscan, `ls` = leakscan, `ss` = secretscan. Exit code
was 1 wherever a finding is listed and 0 where none; `--json` `line` equalled
the human line in every run; `new` and `HEAD` stdout were byte-identical in
every run (the guard code is identical).

| shape (guard: kinds)                          | expected | f4afb7a^ | f4afb7a | HEAD |
|-----------------------------------------------|----------|----------|---------|------|
| below 4 unchanged lines (cs opener)           | 5        | 1        | 5       | 5    |
| same file (ls key-header / term / aws)        | 6/7/8    | 2/3/4    | 6/7/8   | same |
| same file (ss key-header / aws)               | 6/8      | 6/8      | 6/8     | 6/8  |
| two hunks, 20 lines apart (cs opener, closer) | 5, 27    | 1, 3     | 5, 27   | same |
| two hunks (ls key-header ×2)                  | 6, 28    | 2, 4     | 6, 28   | same |
| hunks that also delete lines (cs)             | 4, 11    | 1, 2     | 4, 11   | same |
| hunks that also delete lines (ls)             | 12       | 3        | 12      | 12   |
| new file (cs / ls)                            | 2 / 3    | 2 / 3    | 2 / 3   | same |
| deleted file (both)                           | none     | none     | none    | none |
| rename with edits, 20 base lines (cs / ls)    | 21 / 22  | 1 / 2    | 21 / 22 | same |
| pure rename (both)                            | none     | none     | none    | none |
| mode-only change (both)                       | none     | none     | none    | none |
| no trailing newline, before and after (cs/ls) | 4 / 5    | 2 / 3    | 4 / 5   | same |
| CRLF file (cs opener, separator / ls)         | 3, 4 / 5 | 1, 2 / 3 | 3, 4 / 5| same |
| five git-quoted paths: tab, non-ASCII, quote, |          |          |         |      |
|   backslash, space (cs / ls, each)            | 3 / 4    | 1 / 2    | 3 / 4   | same |
| posed `++ b/…`, `+++ b/…`, `diff --git`,      |          |          |         |      |
|   `@@` lines as added text (cs / ls)          | 3, 8 / 5 | 3, 8 / 5 | same    | same |
| binary file carrying the shapes (both)        | none     | none     | none    | none |
| allow-marker on the line (both)               | exempt   | exempt   | exempt  | same |
| positional prefix filter `a` (both)           | a/ only  | a/ only  | a/ only | same |
| ignore-glob dir (both)                        | skipped  | skipped  | skipped | same |
| leak in a new file's name (ls, line 0)        | 0        | 0        | 0       | 0    |
| opener in hunk 1, setext-shaped seven-`=`     |          |          |         |      |
|   line in hunk 2, 20 lines apart (cs)         | 5, 27 sep| 1, 3 sep | 5, 27   | same |
| seven-`=` line first, opener in hunk 2 (cs)   | 27 only  | 3 only   | 27 only | same |
| committed closer between staged opener and    |          |          |         |      |
|   staged seven-`=` line (cs, staged)          | see RN3  | 1, 3 sep | 1, 15 sep| same|
|   same repo, whole-tree plane (cs)            | 1, 5 clo | 1, 5 clo | 1, 5 clo| same|
| added line = text + FF/VT/NEL/U+2028/bare CR  |          |          |         |      |
|   + opener on the same physical line (cs)     | tree: none| 2 (flag)| none    | none |
|   same (ls key-header)                        | 2        | 4        | 2       | 2    |

Reading of the posed-header row: the new file's added lines coincide with its
file lines, so old and new agree there by construction; the reader's
posed-header handling is `115/280`'s and is unchanged. The "expected" in the
first column is the real file line I derived by hand from the fixture before
running anything.

**Tests.** The three new `StagedRealLineNumbers` tests per guard build real
staged diffs with `git` in a temp repo (not hand-built pairs). Run against the
old code (copied beside `f4afb7a^`'s tools), they fail for the reason they
name: `(5, …)` expected, `1` reported; `5, 26` expected, `1, 2` reported; and
the `staged_added_lines()` assertions fail on shape (`str` versus list of
pairs). `test_a_new_file_still_reports_from_line_one` passes on the old code
too — correct for a regression guard, and its name says "still". The updated
`StagedPosedHeader` assertions fail on old code on shape only; the
posed-header behaviour itself is unchanged. One comment over-explains: the
second-hunk test says 20 unchanged lines exceed "a hunk's context", but under
`--unified=0` every change is its own hunk regardless of distance — harmless.
No guard-level test pins the staged plane against the tree plane on the
embedded-separator input (RN1); the reader's own behaviour there is pinned in
`test_report.py`.

**Docs.** `tools/README.md` § shared reader states the new behaviour and
names "all three guards" — true: secretscan already numbered this way
(`320/290`) and the table shows all three agreeing at HEAD. The conflictscan
README section's staged paragraph is about scope, not numbering, and stays
correct. `CHANGELOG.md` carries the entry. Module docstrings describe the new
shape; two small inaccuracies in RN4.

### Lens 3 — Completeness / harvest

- Other registry scanners on the staged plane: `publishscan` (`--name-only`,
  no lines), `board --check --staged` (reads the index tree, no line
  findings), `harvestscan --staged --only-bulk-deletes` (counts). None numbers
  lines from a staged blob; the three guards were the whole class and all
  three now agree.
- `--json` consumers of `line`: none in `tools/floor.py`, `floorfleet.py` or
  `instruments/`. The human report is the only consumer.
- `scan_text` wrappers: conflictscan's is called by the test suite only (not
  the selftest — RN4); leakscan's by `scan_path_name` (numbering a single
  path string from 1, then rewritten to 0), the selftest and the test suite.
  Both still number from 1, which is right for their callers.
- `docs/method/` says nothing about how a staged finding is located; nothing
  to sweep there. `docs/build/` templates and skills: no staged-plane line
  wording.
- Harvest: RN2 — the shared reader ignores `--root` for the git invocation.
  Pre-existing; in scope only as an assumption this delta makes about the
  reader. I could not check the barred stores for a prior filing; the
  non-barred board index and item files show none.

### Lens 4 — Security & privacy

`/security-review` **discharged by grounds**: this is a landed delta; the
session's pending diff is this brief, and aiming the scanner at it would feed
a review brief into the reviewer (the SL2 caution). Code-altitude read by
hand. Threats for this class (a blocking pre-commit guard parsing git output),
from memory of the OWASP Top 10 since the catalogue page did not resolve:

- *Crafted input to the parser* (added text posing as a header, a hunk or a
  file; hunk counts that do not fit; a header prefix that is not git's): the
  reader fails closed with exit 2 and the posed-header shapes are re-driven
  above. Unchanged by this delta and inherited correctly.
- *Path handling* (C-quoted names, spaces, tabs, quotes, backslashes): re-driven
  across five spellings; findings keyed by the real path at the real line.
- *Injection into subprocesses*: argv is a fixed tuple with no user input; no
  shell. The positional prefix filter is a string compare; absolute paths are
  refused.
- *Fail-open on a scan that covers nothing*: RN2 names a pre-existing route
  (wrong cwd) that exits 0 under `--root <other repo>`; the hook plane does
  not take it. RN1 names the one input where this delta's exit code moves
  from 1 to 0, bounded by the tree plane's identical blind spot.
- *Disclosure in the report*: conflictscan prints the matched marker line
  verbatim (harmless by construction); leakscan redacts; no new data flow,
  no network, nothing written outside stdout.
- *Privacy*: all fixtures synthetic; the term list stays machine-local; the
  test files' fixture git identity is RFC 2606 with reasoned allow-markers
  (pre-existing pattern). No personal data enters.

No finding on this lens rises above RN1/RN2 as already stated.

### Standing checklist V1–V7

- **V1 — No claim stronger than its evidence.** One: "only the number
  changes; no … exit code moves" (docstring and changelog) is false on the
  embedded-separator input class — RN1 (minor). "Whole-tree output
  byte-identical" and "all three guards report at that line" both hold.
- **V2 — Re-run every live-proven claim.** Done; ledger below. Every claim in
  the delta's surfaces reproduces except the RN1 qualifier.
- **V3 — Changed rule swept to every mirror.** README shared-reader paragraph,
  changelog, both module docstrings, both `staged_added_lines` docstrings
  updated; secretscan already said it; no `docs/build/` or skill mirror
  exists for this fact. Discharged.
- **V4 — One fact, one home.** The "real line" fact is stated in the README
  paragraph and in each guard's `staged_added_lines` docstring with a
  `115/300` pointer; the shared reader's docstring is the home. Acceptable
  stamped copies; nothing contradictory. Discharged.
- **V5 — No internal contradiction.** RN4: conflictscan's `scan_text`
  docstring names a caller it does not have (note). Otherwise consistent.
- **V6 — Security & privacy.** Lens 4 above; `/security-review` discharged by
  grounds; catalogue consult not possible here, said so.
- **V7 — Spawn provenance in brief and verdict.** Brief § *Spawn provenance*
  and this verdict's first section. Discharged.

### Findings

**RN1 — minor.** The record says only the reported number changed; on one
input class the exit code changes too. An added line whose own text contains
a form feed, vertical tab, NEL, U+2028 or a bare CR before a conflict marker
was, at `f4afb7a^`, split by `str.splitlines` into two pseudo-lines and the
marker flagged (at a wrong number); at `f4afb7a` and HEAD the line reaches
`scan_lines` whole, the marker is not at column 0, and nothing is flagged —
exit 1 → 0. The whole-tree plane (`_iter_numbered_lines`, LF-only) reports
nothing on the same file at every version, so the delta moves the staged
plane into agreement with the tree plane and with git's own line model; the
old catch was an accident of `splitlines`. For leakscan the same input keeps
its finding (the structural rules are not anchored) and only the number moves
to the correct one. Realistic exposure: a CR-only (classic Mac) file whose
markers follow a CR rather than an LF — rare, and already invisible to the
CI backstop. Evidence: probe `embedded_separators`, five separators, both
guards, three versions, staged and tree. Why it is a finding: the docstring
(`conflictscan.py` § `scan_lines`, "only the number … changed") and the
changelog ("no … exit code moves") are stronger than the evidence, and no
guard-level test pins the two planes' agreement on this class. *Options for
the principal:* (a) accept, qualify the two sentences, and add the input to
each guard's staged tests as a plane-agreement pin; (b) make a bare CR a line
break on both planes (wider change, touches the 110/140 reader, not
recommended by this pass). Recommendation: (a).

**RN2 — minor (pre-existing; harvest).** `--staged` reads the index of the
process cwd, not of `--root`: `report.staged_added()` runs `git diff --cached`
with no `cwd` and no `-C`. Probe: with a staged marker in repo A and nothing
staged in repo B, `conflictscan --staged --root A` run from B prints "clean"
and exits 0; run from A with `--root B` it reports A's finding under B's
ignore globs. From a non-repo cwd it fails closed (exit 2). The hook plane is
unaffected (git runs hooks at the top level and `floor.py` inherits cwd), so
no commit is unguarded today, but the advertised CLI form silently scans the
wrong repo — the silent-success class the absolute-path refusal exists to
close. Not introduced by `f4afb7a`; identical at `f4afb7a^`; shared by all
three guards through the reader this delta assumes reads the `--root` repo.
In scope under the brief's "whatever this delta assumes about the reader".
The delta's tests pass only because every staged test `chdir`s into its
fixture repo. One-line fix in the shared reader (`cwd=root` or `-C root`),
inherited by three guards; may already be on the board — I could not read the
barred stores to check.

**RN3 — note (pre-existing, confirmed unchanged).** conflictscan's
open-conflict state runs across added lines that are not consecutive in the
file, and never sees an unchanged closer. Probe: a staged opener at line 1, a
closer already committed at line 5 (unchanged, so absent from the diff), and
a staged setext-shaped seven-`=` line at 15 — the staged plane flags the
separator at 15 while the tree plane, seeing the closer, does not; the old
code flagged the same separator at "line 3". The delta's docstring states
this honestly ("exactly as before: only the number … changed"), and the real
number now points a person at the actual line, which makes the over-flag
easier to recognise. The brief names a board item filed at the same merge on
a neighbouring behaviour (`115/310`, unread here, title only); if that is
this class, this note corroborates it rather than adding to it.

**RN4 — note.** Two docstring inaccuracies: `conflictscan.scan_text` says
"(the selftest and the test suite use it)" — the selftest calls `scan_paths`
and `main`, never `scan_text`; `leakscan.scan_lines` lists `scan_text`'s
callers as "the path-name scan and the test suite", omitting the selftest,
which does call it. Plus the second-hunk test comment's reasoning about hunk
context under `--unified=0` (lens 2). Cosmetic.

### Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 0 MODERATE · 2 minor · 2 note.**
The fix does what it claims on every diff shape git emits, the tree plane is
byte-identical, the tests are real-git and discriminating; the two minors are
one over-stated "only the number changed" sentence on a contrived input class
(RN1) and a pre-existing cwd-not-`--root` assumption about the shared reader
(RN2). Findings are the principal's to decide (rule 3); nothing applied.

### Re-run ledger

| claim / check                                        | result at HEAD                     |
|------------------------------------------------------|------------------------------------|
| `unittest … test_conflictscan.py -v`                 | 51 tests OK                        |
| `unittest … test_leakscan.py -v`                     | 152 tests OK                       |
| `unittest … test_report.py -v`                       | 70 tests OK                        |
| `conflictscan/leakscan/secretscan --selftest`        | all `selftest OK`, rc 0            |
| new staged tests against `f4afb7a^` code             | cs 4/7 fail, ls 3/7 fail, for the  |
|                                                      | named reasons (1 vs 5; shape)      |
| staged plane re-driven, 20 shapes × 3 versions       | table above; new == HEAD bytes     |
| "whole-tree output byte-identical" (old vs new)      | identical: human + `--json`, over  |
|                                                      | the repo tree (clean) and a fixture|
|                                                      | tree (5 cs / 3 ls findings)        |
| "all three guards report at that line" (README)      | ss 6/8 = ls 6/8 at HEAD            |
| `floor.py --plane ci --root .`                       | rc 0; one warn-only pathscan hit,  |
|                                                      | unrelated (an ADR's unbuilt path)  |
| `floor.py --plane hook --root .`                     | rc 1: leakscan red by design (no   |
|                                                      | term list); cs/ss green            |
| full Python suite, once, foreground                  | 1916 tests OK, 178 s               |
| `node --test instruments/*.test.js`, once            | 447 tests, 431 pass, 0 fail        |
| `/security-review`                                   | discharged by grounds (lens 4)     |
| OWASP catalogue consult                              | not possible here (DNS); from      |
|                                                      | memory, named as such              |
| `coldsweep.py` with the brief's exclusions           | 56 hits / 644 files; 410 barred    |
| ancestry + later-commit checks, re-run after the     | f4afb7a, a1ba8c8 ancestors of HEAD;|
| checkout was unshallowed (23:56 UTC)                 | no later commit on any guard path  |

Logs and probe: `/home/user/scratch/RN/logs/`, `/home/user/scratch/RN/probe.py`.

### Follow-up checklist (for the principal's decision; nothing applied)

- [ ] RN1 — rule on option (a) or (b); if (a), qualify the `scan_lines`
      docstring and the changelog sentence, and add the embedded-separator
      input to both guards' staged tests as a plane-agreement pin.
- [ ] RN2 — rule whether `report.staged_added` takes the root; check the
      board for a prior filing before opening a new item.
- [ ] RN3 — no action from this pass; corroboration for the neighbouring item
      if it covers this class.
- [ ] RN4 — two docstring touch-ups and one test comment, when next in the
      files.

### Reconcile

Phase 2, begun 2026-10-17 23:57 UTC after the orchestrator committed phase 1
as `74a7053` and released the sibling into the tree. Opened for this step:
the sibling, the queue pointer `160/830`, the intent record
`docs/sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md`
(§§ `115/300`, `115/310`), board items `115/300` and `115/310`, and the
landing and merge commit bodies. The four prior verdicts the sibling names
by filename were **not** opened: none is on this delta (two are on the shared
reader and leakscan's gates, two are older), and no finding here rests on
them. Phase-1 text above is unrevised. **No finding was formed at
reconcile.**

**Against the seeded questions.**

1. *Open-conflict state across hunks; `115/310`.* This is RN3. The record
   shows the delta carried it forward knowingly (docstring: "exactly as
   before"), the worker filed it, a state-reset fix (`d79492b`) was built and
   **rejected on evidence** before merge: in the commonest real case — a bad
   merge staged against `HEAD` — the "ours" lines between opener and
   separator are unchanged context, so a reset at any gap loses the true
   separator. My probes agree with that reasoning from both sides: the
   `opener-then-setext` shape reproduces `310`'s false separator (now at its
   true line, 27), and the `committed-closer-between` shape is the mirror
   image, where the unseen context line is the closer. The false separator
   only ever stands beside a genuine opener that already blocks, as `310`'s
   closure says. Yes: a finding's line is now right while its cause may sit
   in another hunk — and `310`'s own closing note ("a separator reported
   with its hunk") is the shape that would say so. RN3 stays a note and
   corroborates the closure; nothing to add.
2. *Does any leakscan rule read line 1, adjacency or the previous line?* No
   — lens 1 assumption 3 and the `scan_lines` read: allow scope, shadows and
   validators are computed per line; no state crosses lines; nothing keys on
   line 1. Confirmed, no finding.
3. *Is secretscan's number the reader's number on every shape?* At HEAD it
   is the same number by construction — secretscan has consumed
   `report.staged_added` since `115/280` — and the probe shows all three
   guards agreeing on the below-unchanged shape at every version. The
   README's "all three guards" holds.
4. *Tests by hand or real git?* Real git, in a temp repo, for every staged
   test (lens 2). They test the claim.
5. *Path-name scan numbered from 1 through `scan_text`?* `scan_path_name`
   rewrites the line to 0 and the human report prints "in the path name";
   meaningful and consistent with body findings (lens 3). No finding.
6. *Whole-tree byte-identity: by construction or by fixture?* By
   construction: the tree plane runs `_scan_file` → per-physical-line
   `_line_finding`/`scan_lines` and never calls the staged reader or
   `scan_text`, and `_line_finding` is untouched by the delta. The author's
   fixture evidence is therefore confirmatory, not load-bearing; I re-ran it
   anyway (ledger) because a recorded proof is re-run, not read.

**Against the intent record and the commit bodies.**

- The commit body's "no output format, rule, exit code or JSON field moves"
  is the sentence RN1 qualifies: on the embedded-separator class the exit
  code does move (1 → 0), toward agreement with the tree plane. Everything
  else in that paragraph reproduces.
- `115/300`'s close says the new tests fail on the old code "four of six,
  with the two new-file controls passing on both". My run against
  `f4afb7a^`: four of six fail (two per guard), the two new-file controls
  pass — an exact match.
- `115/300` and the intent record report one suite failure at a machine load
  of about 300 (`test_pins.BoundedMemory`), re-checked at the close. At this
  HEAD, on a quiet container: 1916 tests, 0 failures. The suite grew by 19
  tests since; nothing in the delta's surfaces changed.
- `115/300`: "No other guard consumes the reader" — true at HEAD (lens 3).
- RN2 (staged mode reads the cwd's index, not `--root`'s) appears nowhere in
  the intent record, `115/300`, `115/310` or either commit body, and a search
  of the now-readable stores (`ROADMAP-DONE.md`, every item file, every
  session record) finds no prior filing; `010/110` (relative path arguments
  resolve against `--root`, closed 2026-08-23) is the tree plane's cousin
  and does not cover the staged `git diff` invocation. RN2 therefore stands
  as a new harvest item. By the sibling's own split ("a defect in the number
  the reader yields belongs there; how this delta consumes it belongs
  here") its home is the shared reader, `160/800`'s surface — which repo the
  reader reads is the reader's business. Routing is the principal's call;
  recorded here because this delta's tests and docstrings assume the answer.
- RN4: nothing in the seeded material bears on it. Stands.

**Overlap with sibling passes.** `160/800` is where RN2's fix would land;
`160/840` and `160/850` touch `tools/README.md` only in other paragraphs
(verified: the README diff after `f4afb7a` does not touch the shared-reader
paragraph this delta edited); `160/720` reviews the gates inside the
`scan_lines` this delta now feeds — the gates are necessary-condition
pre-filters and the staged plane changes nothing about what reaches them.

**Overall line, restated:**
**PASS-WITH-FINDINGS — 0 MAJOR · 0 MODERATE · 2 minor · 2 note.**
No finding formed at reconcile; severities unchanged.

## Deferred material — folded in at the verdict

*The sibling `docs/reviews/2026-10-17-0955-staged-real-line-numbers-cold.deferred.md`,
folded in at phase 2 and deleted, per `REVIEW.md` rule 1 ("split for the
duration, merged at rest"). Text verbatim; its `##` section headings are
nested one level (`###`) so they sit under this heading, nothing else
changed.*

# Sibling to the staged-real-line-numbers cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-17-0955-staged-real-line-numbers-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-17 UTC by the Opus brief-writer named in the brief's provenance; it
forms no finding. Fold this file in below the reconcile and delete it at phase 2.

### Intent and commissioning records

- Intent record: `docs/sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md` —
  **not opened by the brief-writer**.
- Commissioning board item (title line seen, never read whole): `115/300` (conflictscan and
  leakscan report the wrong line number). Filed at the same merge: `115/310` (conflictscan's
  open-conflict state runs across staged hunks).
- The landing commit's message body (read by the brief-writer): on the staged plane both guards
  joined a file's added lines into one blob numbered from 1, so a finding pointed at the wrong
  line, though it still blocked; "secretscan already numbered by hunk"; `report.staged_added`
  already yielded the real number and both guards discarded it; "Only the number a finding is
  reported at changes: no output format, rule, exit code or JSON field moves"; conflictscan's
  open-conflict state "still runs through the added lines in order, as before"; two new tests
  per guard fail on the old code; whole-tree output byte-identical on the repo and on a fixture.

### Prior verdicts on these surfaces (named by filename grep, not opened, not exhaustive)

- `docs/reviews/2026-08-09-0826-e7-leakscan-build-cold.md`
- `docs/reviews/2026-09-25-0715-staged-plane-check-cold.md`
- `docs/reviews/2026-10-16-1551-git-quoted-paths-cold.md` — the staged path reader, 160/760
- `docs/reviews/2026-10-16-1551-scanner-rule-gates-cold.md` — leakscan's gates, 160/720 (its
  brief was one of this brief-writer's templates)

### The pointer's own lens hints

None beyond "its dispatched worker's output counts as the run's authorship". Refs-only.

### Overlap with sibling passes of this batch

- 160/800 (`39a74b9`, the shared staged-diff reader in `tools/report.py`) is this delta's
  foundation and is briefed by this run's other brief-writer. A defect in the number the reader
  yields belongs there; how this delta consumes it belongs here.
- 160/840 (`e3e8a4f`) and 160/850 (`72a68cc`) branched from the same base and also edit
  `tools/README.md`; the merges were sequential.
- 160/720 (scanner gates) reviews leakscan's `scan_lines` gate checks at HEAD, the same function
  this delta now feeds from the staged plane.

### Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. "Only the number changes": conflictscan's open-conflict state used to run across a joined
   blob and now runs across numbered pairs from several hunks, unchanged. 115/310, filed at the
   same merge, suggests that state crossing hunks is itself a defect. Did the delta knowingly
   carry it forward, and is a finding's line now right while its cause is a line in another hunk?
2. Does any leakscan rule or marker check look at line 1, line adjacency, or "the previous line"
   (a preceding-line allow, a header-only scope)? With real numbers, line 1 of the staged input
   may no longer be line 1 of the file.
3. The README paragraph now says "all three guards" report at the real line. Is secretscan's
   per-hunk numbering the same number as `report.staged_added`'s, on every diff shape?
4. Do the new tests build the numbered pairs by hand, or stage a real diff through git? If by
   hand, they test the plumbing, not the claim.
5. leakscan's staged path also runs the path-name scan through `scan_text`, numbered from 1 —
   is that line number meaningful to a reader, and is it consistent with the body findings now?
6. The whole-tree "byte-identical" evidence was taken by the author on one repo and one fixture.
   Is the whole-tree plane provably untouched by construction, making that evidence unnecessary,
   or does it rest on the fixture?
