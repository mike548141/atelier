# Cold pass — cctranscript's archive-pool speedup

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this pass's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-10-03 0357 UTC; the review runs under the
orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:** `docs/roadmap/160-doctrine-review-owed/440-rule-4-cold-pass-queued-the-archive-pool-speedup.md`.
**Why it earns a review:** cctranscript is the instrument every usage, cost and provenance question in this estate is answered with; a speedup that changes how it finds and opens archived transcripts changes what every later measurement sees.

## Spawn provenance

- **Author of the work under review:** the 2026-10-03 queue run (an Opus
  orchestrator with dispatched workers) that landed the commits named under
  *What the work is*. This brief-writer was not that session, was neither
  started nor instructed by it, and has edited none of the delta's paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-10-03 with
  the prompt "Do all cold reviews and any other work dependent on fable", on
  the Fable tier (`claude-fable-5-1`), orchestrating six rule-4 passes queued
  by that run. It wrote this brief from the queue pointer, the landing commits'
  subjects and `--stat` file lists, and the delta paths' names; it did not open
  the intent record.
- **Who takes the review:** a fresh Fable subagent (`claude-fable-5-1`) spawned
  by the brief-writer with this brief as its only framing. It is not the
  author's session and was not instructed by the author. The reviewer repeats
  its own provenance in the verdict.
- **Orchestration shape, disclosed per rule 4:** reviewer-plus-orchestrator. The
  orchestrator holds the `.deferred.md` sibling outside the worktree and
  outside the harness scratchpad (subagents can read the scratchpad), commits
  the reviewer's phase-1 findings unrevised, then releases the sibling's text by
  message; the reviewer appends a reconcile section; the orchestrator folds the
  sibling in and updates the pointer. The orchestrator forms no finding and
  writes no severity. Both seats are Fable, so the off-tier clause is not
  invoked; the shape is stated anyway so the record is auditable.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material it met before
  writing): the authoring run told this session over the cross-session channel
  that the pointer existed and named its subject in a phrase; nothing else from
  that run was read. Earlier in the same sitting this session commissioned
  read-only inventories of the board's open items and of every verdict in
  `docs/reviews/`, for a ruling round; the summaries it received include prior
  findings on the surfaces under review. Those summaries are author-side
  framing this pass must meet cold; every line of them that bears on this delta
  has been moved to the sibling and kept out of this brief. The brief-writer
  also read the 2026-09-25 batch's staged-plane brief as a formatting template,
  the session index entries of 2026-09-19 to 2026-10-01, and, as doctrine at
  onramp, `docs/method/REVIEW.md`, `docs/method/00-APEX.md` and
  `docs/method/COMMUNICATION.md` § *Asking for a ruling* at HEAD.

## What the work is

Landing commits (diff these; review the paths at HEAD, `17c75a9` or later):

- `6cbf33f` (2026-10-03) — merge of `0a15b93`: cctranscript batches the dataless stat and sniffs a gzip prefix (board `210/050`)

Delta paths:

- `instruments/cctranscript` — the pool walk, the batched stat, the gzip sniff
- `instruments/cctranscript.test.js` — its tests

Neither `instruments/man/cctranscript.1` nor `instruments/README.md` changed; whether the behaviour they describe still holds is yours to establish.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Driven, not read: build a scratch transcript pool with plain `.jsonl`, gzipped `.jsonl.gz`, a gzipped file with the wrong extension, a plain file whose first bytes happen to match a gzip prefix, an empty file, an unreadable file and a dangling symlink; run every subcommand (`--list`, `--search`, `--json`, the by-day and by-model reports) at the parent of the landing commit and at HEAD in a scratch clone and diff the outputs byte for byte. Re-measure any timing claim the code or tests make. Check memory on a multi-gigabyte pool if the "stream" wording in the commit subject is load-bearing. **Non-goal:** the board item that commissioned the speedup.

## The four lenses

1. **Approach & assumptions.** A batched stat presumes the pool is stable between the stat and the read: find the shape where a file appears, vanishes or is rewritten in between, and record what the tool reports. A prefix sniff presumes two bytes decide the format: find the input that lies.
2. **Correctness & quality.** Read all of `instruments/cctranscript` and its test file. Run `node --test instruments/*.test.js`, the man-page superset test if one exists, `--help`, and every state in *Scope*. Check exit codes against the man page's EXIT STATUS.
3. **Completeness / harvest.** Every surface that describes how the tool finds and opens transcripts: the man page, `instruments/README.md`, the module header, `--help`, `CHANGELOG.md`. Does each still describe what the code does?
4. **Security & privacy** — mandatory. The tool opens files named by a directory walk and prints their contents. Check path handling for symlinks out of the pool, a filename with a leading `-`, and what a crafted gzip header can make it read or allocate. The house scanner is discharged by grounds (landed delta; the pending diff is this brief) — say so, and deliver the code-altitude read by hand, against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `node --test instruments/*.test.js` (foreground, once)
- `instruments/cctranscript --help`; the man page's option superset test
- every state in *Scope*, at the landing commit's parent and at HEAD

## House rules for this run

- You work in the shared review worktree `/Users/mike/worktrees/atelier-review-430`
  (branch `review-430-1003`), read-only except for THIS brief file. Other
  reviewers are working there at the same time on their own briefs; never open
  another `docs/reviews/2026-10-03-*` file — it is another pass's framing. Run
  **no git command that writes** there (no add, commit, stash, checkout,
  worktree, reset, clean). Read-only git (`log`, `show`, `diff`, `blame`) is
  fine. Mutation probes, scratch children and checkouts of older commits go in
  your own clone: `git clone /Users/mike/worktrees/atelier-review-430
  <scratchpad>/CP/probe` under the session scratchpad, named by your
  prefix so parallel reviewers do not collide.
- One heavy process at a time on this machine: run the full suite at most once,
  in the foreground with a long timeout; if a memory-probe test times out, note
  it as environmental and re-run that test file alone before recording it.
  Never scan any tree outside the worktree or your scratch clone, and never
  point a scanner at the machine's other repos. Other sessions are live on this
  machine and in this repo's primary checkout; touch nothing there.
- `/security-review` is **discharged by grounds**: it reads the session's
  pending diff, which here is other passes' drafts and this brief, and this is a
  landed-delta review. State that line in your lens-4 answer and deliver the
  code-altitude read by hand.
- Dates in your verdict are absolute ISO-8601 from `date -u` (the hook-plane
  `datescan` reds relative words such as "yesterday" or "next week" and would
  block the orchestrator's commit). Wrap prose at ≤ 100 columns. NZ English.
  Never quote a secret, a placeholder token, an email address, a private
  repo's name or any personal detail — this repo is PUBLIC; describe, don't
  quote.
- Review deep, not fast. A finding needs a probe or a re-driven claim behind it,
  not reasoning alone; a clean lens needs the trail that earned it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held by the orchestrator outside the worktree under the rule-1 split and released only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/440-rule-4-cold-pass-queued-the-archive-pool-speedup.md`
(it carries the author's framing and this pass's claim line), and:

- `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md` (the
  intent record)
- the board item `docs/roadmap/210-*/050-*.md` (the commission)
- the verdict `docs/reviews/2026-08-15-1032-cctranscript-search-cold.md`
- `docs/roadmap/160-doctrine-review-owed/010-*.md` (carries that verdict's outcome line)

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-430 --also-exclude
docs/roadmap/160-doctrine-review-owed/440-rule-4-cold-pass-queued-the-archive-pool-speedup.md
--also-exclude docs/roadmap/210-instruments-open-features --also-exclude docs/roadmap/160-doctrine-review-owed <pattern>` — rule 2's
default bar plus the items above; `--include-barred` only with disclosure in
the verdict. Reading the *delta* is never barred: the code, its tests, the
README entries and the registry are the subject. What is barred is the author's
narrative of why, and the verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `CP`: `CP1`, `CP2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, a re-run ledger with the commands and their results, and a
follow-up checklist. Then STOP and report to the orchestrator that phase 1 is
written. Do not open the sibling (it is not in the tree); do not edit the queue
pointer, the board, or any file but this one.

**Phase 2.** On receipt of the sibling's text, append `### Reconcile` beneath
your verdict: per-finding notes against the seeded questions and the intent
record, any finding formed at reconcile marked as such, and the overall line
restated. Never revise phase-1 text. The orchestrator folds the sibling in below
your reconcile.

Findings are the principal's to decide (rule 3): record all, apply nothing;
your counsel per finding is welcome, labelled as counsel and kept beneath the
finding.

---

## Verdict — CP (phase 1)

**Written:** 2026-10-03, 04:03–04:25 UTC (`date -u`).
**Reviewer provenance:** `claude-fable-5-1` on the Fable tier, a fresh subagent spawned by the
brief-writer with this brief as its only framing. Not the author's session (the 2026-10-03 queue
run), not instructed by it, and it edited none of the delta's paths. Read for this pass: this
brief; the delta (`6cbf33f`, first parent `2c8c3b0`, merged commit `0a15b93`) as a diff and as
both files whole at the landing commit and at the parent; `instruments/man/cctranscript.1`;
the cctranscript sections of `instruments/README.md`; the head of `CHANGELOG.md`;
`.githooks/pre-commit`, `tools/floor.py` and `.github/workflows/ci.yml` for floor invocations;
grep-level reads of `instruments/ccrepo` and `instruments/ccarchive` for the sibling pattern
(lens 3). Not opened: the deferred sibling, any other `docs/reviews/2026-10-03-*` file, the queue
pointer, any board item, `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, any prior
verdict. No tree-wide grep was run, so `coldsweep.py` was not needed. All mutation probes ran in
the session scratchpad under `CP/`: a clone of this worktree with checkouts of `2c8c3b0`
(`parent`) and `6cbf33f` (`landing`), synthetic pools, and the captured outputs. No git command
that writes was run in the review worktree.

### Where the delta was reviewed, and why not at the worktree's HEAD

The brief says to review the paths "at HEAD, `17c75a9` or later". The review worktree's HEAD is
`4ff8de5` on `review-430-1003`, and `git merge-base --is-ancestor 6cbf33f HEAD` returns 1: the
branch forked from `main` at `2c8c3b0`, one commit *before* the landing merge. The worktree's
`instruments/cctranscript` has the pre-delta `isDataless(p)` and full-gunzip `cwdFromLog`, and
its test file has none of the four new tests (`grep -c 'gunzipHead\|statFlagsBatch'` is 0 for
both; 6 and 9 at `6cbf33f`). `17c75a9` and `6cbf33f` are reachable only from `main` and
`origin/main`. The delta is identified by SHA, so this pass reviewed it at `6cbf33f` in the
scratch `landing` checkout; the consequence for the floor reproduction is recorded under CP1 and
in the re-run ledger.

### Lens answers

**1. Approach & assumptions.** The batched stat moves the dataless check from immediately
before each read to before the whole walk. For a file that *appears* in between: not in `found`,
not listed, same as the parent. For one that *vanishes*: the map says "not dataless", `statSync`
for mtime fails to 0, `cwdFromLog` returns null, and `--list` then crashes in
`firstUserPromptText` exactly as the parent does (CP4). For one *evicted* in between: it is read
and faulted back, where the parent's just-in-time stat would have skipped it — one file, not a
bulk download, and unforceable in a probe, so recorded as reasoning (CP8). For one *rewritten*:
no effect; the flags do not change. The lens's second premise does not describe this code: no
magic bytes are sniffed, format is still decided by the `.gz` extension exactly as before, and
"prefix" means a prefix of the *compressed* bytes inflated with `Z_SYNC_FLUSH`. The question that
does apply — can a compressed prefix inflate to something other than the full inflation's prefix
— was probed with eight shapes (a 100 KB `FNAME` header longer than the first prefix read; a
two-member gzip whose 64 KB prefix cuts 4 bytes into member 2's header; a member followed by
trailing garbage beyond the prefix; a 1000:1 high-ratio body; an incompressible body that forces
the doubling path; a small file; a file whose cwd sits past 64 KB; a macron-named file). Every
one gave a byte-identical 64 KB text prefix to the parent's full gunzip, and both throw
identically on the two wrong-extension lies (plain text named `.gz`; a plain file whose first two
bytes are the gzip magic). No lie was found. One genuine lie was found on the *stat* side: a path
`stat` parses as an option (CP2), and a filename containing a newline (CP3).

**2. Correctness & quality.** Both files read whole at `6cbf33f`. `node --test
instruments/*.test.js` ran once in the review worktree (277 pass, 0 fail, 0 skipped — the
pre-delta suite, see CP1); `node --test instruments/cctranscript.test.js` then ran once at the
landing commit (82 pass, 0 fail, 0 skipped; the four new tests ran, the darwin gate open). The
only instrument files differing between the worktree HEAD and `6cbf33f` are the two delta files,
so the pair of runs covers the suite at the landing commit. `--help` exits 0 and the superset
drift test passes; `mandoc -T lint` on the man page exits 0. Every subcommand the tool has
(`--list`, `--list --json`, `--search`, `--search --json`, `--search --tools`, render by UUID,
render by explicit `.gz` path, `--list` on an explicit path, the simulate-dataless seam, the
live-store route under an overridden HOME, and eight exit-status cases) was driven over the
synthetic pools at the parent and at the landing commit: 46 runs a side, 138 files compared,
every stdout and every exit code byte-identical; the only differences are stack-trace line
numbers inside the six crash cases. The brief's "by-day and by-model reports" are not
cctranscript subcommands (`--help` shows render, `--list`, `--search` only); they were not run.
Exit codes against the man page's EXIT STATUS: 0 for help, list and a no-hit search; 1 for a
missing path, an unmatched UUID, an unknown repo, `-n` past the pool and no sessions for the
directory; 2 for a malformed `--since` — all as documented. Two divergences, both pre-existing:
a trailing `--search` with no value renders a transcript and exits 0 where the page says 2
(CP9), and a listing that meets a file it cannot inflate or open dies with a raw stack trace
(CP4). The timing claims re-measured: 960 per-file `stat` spawns took 6.8 s (7.1 ms a spawn) and
the batched form 46 ms; `--list --all` over a 960-mirror synthetic pool went from 13.1 / 10.6 s
at the parent to 4.5 / 3.0 s at the landing commit with byte-identical output. The code
comment's "~15 ms a spawn, ~15 s for 960" is the same order at twice the figure on this machine
and is labelled approximate; not a defect. Test quality: the doubling path is genuinely
exercised (the `incompressible` case makes two reads, 64 KB then 128 KB); the chunk test writes
850 files under the OS tmpdir and, like every other test in the file, never removes them (10
`mkdtempSync`, 0 `rmSync`) — a pre-existing pattern this delta extends.

**3. Completeness / harvest.** Surfaces that describe how the tool finds and opens transcripts:
the module header ("Listing never reads an iCloud-evicted mirror ... rendering one chosen session
may") — still true; the man page (`--from-archive`, FILES, NOTES on eviction) — still true, and
it never described the mechanism, so nothing went stale; `instruments/README.md` lines 59 and
501 (a `--list` "peeks" and "never faults iCloud-evicted bytes back") — still true; `--help` —
unchanged, no new flag to add. The one surface that does not reflect the change is
`CHANGELOG.md`, which has no 2026-10 entry at `6cbf33f` (CP6). The sibling instruments still
carry the pattern this delta replaced: `instruments/ccrepo` has the same one-spawn-per-file
`statFlags` (line 584) and the same full-gunzip `cwdFromLog` (line 695); `instruments/ccarchive`
has the per-file `statFlags` (line 425). The commit body names the remaining cost honestly
(`firstUserPromptText` still inflates every local mirror whole) and leaves it for its own item;
the memory measurement below confirms that is where the listing's footprint now sits (CP7).

**4. Security & privacy.** `/security-review` is discharged by grounds: it reads the session's
pending diff, which here is other passes' drafts and this brief, and this is a landed-delta
review. Hand read at code altitude against the OWASP catalogue. *Injection (A03):* every spawn is
`execFileSync` with an argv array and no shell; a path cannot inject a command. A path beginning
with `-` is reachable only through a relative `--dest` or `$CCARCHIVE_DEST` (walked paths are
`path.join(dest, repoDir, file)`; the explicit route goes through `path.resolve`), and when it
is, `stat` reads it as an option and the whole chunk fails closed to "not dataless" (CP2) — the
guard fails *open* for eviction, nothing executes. The parent's per-file call failed the same way
for each such path. *Path handling / access control (A01):* the walk follows symlinks with no
containment — a `.jsonl.gz` symlink pointing outside the pool is listed and rendered (probed,
`h9-escape`); identical at the parent; the dest is a directory the user chose on their own
machine and the tool reads only what that user can read, so the trust boundary is the dest, and
this is recorded, not found against. *Resource exhaustion (A04, A05):* no `maxOutputLength` is
set on any `gunzipSync`, before or after. The delta *bounds* the cwd sniff: on a crafted 200 KB
file that inflates to 200 MB, `gunzipHead` returned 67 MB from the 64 KB prefix (RSS delta 129 MB)
against the parent's whole-file inflate (sniff alone: 448 MB RSS at the parent, 173 MB at the
landing commit). The listing's peak is unchanged (655 MB against 654 MB) because
`firstUserPromptText` still inflates the whole file (CP7). *Crafted gzip header:* a 100 KB `FNAME`
field and a header cut by the prefix boundary both inflate identically to the parent (lens 1).
*Environment trust:* `stat` resolves through `PATH`, as before. *Disclosure:* the tool prints
transcript text by design and the delta adds no new output path. No secret, token or personal
datum appears in the delta or its tests; every fixture is synthetic.

### Findings

**CP1 · MODERATE** — The review worktree does not contain the delta. `review-430-1003` forked
from `main` at `2c8c3b0`, one commit before the landing merge `6cbf33f`, so "review the paths at
HEAD" in this brief points at pre-delta code, and a floor run in the worktree exercises the
pre-delta suite without anything failing to say so. The first suite run of this pass did exactly
that (277 pass) and only the direct-function probe exposed it (`cc.gunzipHead is not a
function`). Recovered by reviewing at `6cbf33f` in a scratch checkout. This is a defect of the
brief and the worktree set-up, not of the delta.
*Counsel:* any sibling pass run from this worktree whose landing commit postdates `2c8c3b0` has
the same gap; the orchestrator should check each one's SHA with `merge-base --is-ancestor`
against the branch HEAD before trusting a floor run made there, and the brief template should
name the landing SHA as the review point rather than HEAD.

**CP2 · minor** — `statFlagsBatch` is not isolated per path the way its comment claims ("a
failed path (stderr, no line) cannot shift the rest"). A path that `stat` parses as an option —
every walked path when `--dest` or `$CCARCHIVE_DEST` is relative and begins with `-` — makes
`stat` exit with "illegal option" and the entire 400-path chunk returns empty, so every mirror in
that chunk reads as not dataless and a `--list` would fault back every evicted mirror in the
archive. Probed: a relative `-pool/a.jsonl.gz` in the same chunk as a good absolute path left
both absent (chunk size 0); `stat -f '%f\t%N' -- <path>` handles it. The parent's per-file call
failed identically for each such path, so the exposure is not new; the batch widened the blast
radius from one path to the chunk and the comment overclaims.
*Counsel:* pass `--` before the paths and resolve the dest to absolute in `archiveRoot()`; both
are one-line changes.

**CP3 · note** — A mirror whose file name contains a newline splits the `%N` output line; the
path is absent from the map and read as not dataless (probed: `new\nline.jsonl.gz` absent, the
tab-named and macron-named files present). The parent's single-path call did not depend on the
name. ccarchive names mirrors by UUID, so only a hand-placed file can carry a newline; recorded
for completeness.

**CP4 · minor (pre-existing)** — `--list` loses the whole listing, with a raw Node stack trace
and exit 1, on the first mirror `readLogText` cannot inflate or open: plain text named `.gz`,
a gzip-magic-led plain file, an empty file, a mode-000 file, a dangling symlink. The human form
prints one blank line then dies; `--json` prints nothing. Exit 1 is numerically inside the man
page's EXIT STATUS but its described meaning ("cannot select a session") does not cover this,
and a stack trace is not a message. Identical at the parent (the delta did not cause it), and
the delta made `cwdFromLog` robust to every one of these shapes while `firstUserPromptText`,
three lines below it in `runList`, has no guard. `--search` already handles the same files
gracefully with an `unreadable` counter. A truncated mirror left by an interrupted iCloud sync is
the realistic trigger.
*Counsel:* wrap the first-prompt read per row the way search does, print a marker in the column,
and count the rows in the footer.

**CP5 · note** — The simulate seam bypasses the batch (`CCARCHIVE_SIMULATE_DATALESS ? undefined
: statFlagsBatch(...)`), so the existing `--list` eviction contract tests never execute the
batched path through `archiveSessions`; the batch is covered by its two unit tests (map equals
per-file flags; chunking past 400) and the lookup semantics in `isDataless(p, flagMap)` are
pinned by nothing in-tree. Probed by hand: present-with-bit → evicted, absent → not evicted,
seam set → seam wins over an empty map. Real eviction through the walk is unforceable, as before.
*Counsel:* one test passing a hand-built `Map` through `sessionRecord` would pin the lookup.

**CP6 · note (harvest)** — `CHANGELOG.md` has no entry for this change and no 2026-10 entry at
all at `6cbf33f`. The repo's pattern is one entry per queue-run batch, so this may be owed by the
run's close rather than the commit; recorded so the harvest is countable.

**CP7 · note** — The "stream" wording in the commit subject is not load-bearing and the memory
check was run anyway: `--list --all` over three ~100 MB-text mirrors peaked at 486 MB (parent)
and 484 MB (landing), and at 655 / 654 MB on the crafted high-ratio file — unchanged, because
`firstUserPromptText` still inflates each mirror whole. Memory is per-file, not per-pool, at
both commits; a multi-gigabyte pool costs no more than its largest mirror. The cwd sniff alone
dropped from 448 MB to 173 MB. The commit body names this residual honestly and leaves it for
its own item; `gunzipHead` is the obvious tool for it, with the caveat that the first *user*
line is not guaranteed inside 64 KB, so a fall-through to the full read is needed.

**CP8 · note (reasoned, not probed)** — Batching opens a window between the dataless check and
the read that the parent's just-in-time stat did not have: a mirror iCloud evicts during the
walk is read and faulted back. The cost is one file's bytes, not a bulk download, and eviction
cannot be forced in a probe. Recorded as the one assumption the batch adds.

**CP9 · minor (pre-existing, off-delta)** — `--search` as the last argument with no value
renders the latest transcript and exits 0 at both commits (`takeValue` returns `undefined`,
`doSearch` is false, the CLI falls through to `runTranscript`). The man page's EXIT STATUS says
`--search` with no term exits 2, and the suite checks only `--search ''`. Found while checking
exit codes against the page as the brief asks; unrelated to the delta.
*Counsel:* treat `argv.includes('--search')` as the mode switch and let `runSearch` report the
missing term, which the test for `--search ''` already covers.

### Overall

**PASS-WITH-FINDINGS** — 0 MAJOR · 1 MODERATE · 3 minor · 5 notes. The delta does what its
commit says: the dataless signal is unchanged in meaning, one spawn per 400 paths replaces one
per file, the cwd sniff reads a bounded compressed prefix and falls back to the strict gunzip
once the prefix is the whole file, and across 46 driven runs a side the output is byte-identical
to the parent while the 960-mirror listing runs about three times faster. Every finding against
the code is minor or a note, and three of the four code findings pre-date the delta. The one
MODERATE is about the review's own footing, not the work: this worktree never held the delta.

### Re-run ledger

- `node --test instruments/*.test.js` — review worktree, HEAD `4ff8de5`, foreground, once:
  277 pass / 0 fail / 0 skipped, 20.1 s. **Pre-delta suite** (CP1); the four new tests absent.
- `node --test instruments/cctranscript.test.js` — scratch checkout of `6cbf33f`, foreground,
  once: 82 pass / 0 fail / 0 skipped, 12.5 s; `statFlagsBatch` ×2 and `gunzipHead` ×2 ran.
  `git diff --stat 4ff8de5 6cbf33f -- instruments/` lists only the two delta files, so the two
  runs together cover the suite at the landing commit.
- `mandoc -T lint instruments/man/cctranscript.1` — exit 0 (floor's own invocation, `ci.yml`
  line 124). `node instruments/cctranscript --help` — exit 0; the superset drift test passed in
  both suite runs.
- Floor invocations lifted from `.github/workflows/ci.yml` lines 107, 114 and 124; the hook
  plane (`.githooks/pre-commit` → `tools/floor.py`) runs no node tests, so the hook was not the
  surface for this delta.
- Subcommand matrix (`run-matrix.sh`): 46 runs a side at `2c8c3b0` and `6cbf33f` over pools
  `clean` (8 shapes incl. long-header, cut-member, trailing-garbage, macron name, a plain
  `.jsonl` and an `_external/` dir, both correctly skipped), `hostile` (adds plain-text-as-gz,
  magic-led plain, empty, mode 000, dangling symlink), each hostile shape alone, a symlink out
  of the pool, a live store under an overridden HOME, and eight exit-status cases. `diff -r`
  after normalising the checkout path: 138 files, differences only in stack-trace line numbers
  of the six crash cases; all stdout and all exit codes identical.
- Direct probes (`probe-fns.js`, landing module required, parent's full gunzip as control):
  8/8 shapes prefix-identical; doubling path takes reads of 64 KB then 128 KB on the
  incompressible case; newline-named path absent from the batch map, tab- and macron-named
  present; leading-dash relative path empties its whole chunk, `--` fixes `stat`; seam and map
  precedence as read; `gunzipHead` on the 200 MB / 200 KB file returned 67 MB, RSS +129 MB.
- Timing (`timing.sh`, sequential, `/usr/bin/time -l`, loaded machine): 960 per-file `stat`
  spawns 6,805 ms (7.1 ms each) against 46 ms batched; `--list --all` over 960 synthetic mirrors
  13.10 / 10.59 s parent against 4.46 / 2.95 s landing, byte-identical output, max RSS 120–127 MB
  both; `--list --json` 9.37 against 5.94 s, identical; `--search` 13.46 against 6.18 s. Memory:
  three ~100 MB-text mirrors 486 against 484 MB; crafted high-ratio mirror 655 against 654 MB
  (listing), 448 against 173 MB (cwd sniff alone).
- No `coldsweep.py` run: no grep touched any barred path (greps were confined to
  `instruments/`, the three floor files and `CHANGELOG.md`).

### Follow-up checklist

- [ ] CP1 — orchestrator: verify each sibling pass's landing SHA is an ancestor of the review
      branch before trusting its worktree floor run; brief template to name the SHA, not HEAD.
- [ ] CP2 — `--` before the paths in `statFlagsBatch`; absolute dest in `archiveRoot()`; fix the
      isolation comment.
- [ ] CP4 — guard `firstUserPromptText` per row in `runList`, marker + footer count.
- [ ] CP5 — a `sessionRecord` test with a hand-built flag map.
- [ ] CP6 — CHANGELOG entry at the run's close.
- [ ] CP7 — the `firstUserPromptText` prefix read, as the commit body already proposes.
- [ ] CP9 — make a bare trailing `--search` exit 2 as the man page says.
- [ ] CP3, CP8 — no action proposed; recorded.

Phase 1 ends here. Reconcile follows on receipt of the sibling's text.
