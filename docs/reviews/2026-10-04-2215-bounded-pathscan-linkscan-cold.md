# Cold pass — pathscan and linkscan stream and cap

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-10-04 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/640-rule-4-cold-pass-queued-bounded-pathscan-linkscan.md`.
**Why it earns a review:** two enforced guards were rewritten to read in a
stream and to stop reporting at a cap; a guard that caps can exit green past the
cap, and a streamed reader can miss what a whole-file reader found across a
chunk boundary.

## Spawn provenance

- **Author of the work under review:** the 2026-10-03 queue run (an Opus
  orchestrator with dispatched workers) that landed the commits named under
  *What the work is*. This brief-writer was not that session, was neither
  started nor instructed by it, and has edited none of the delta's paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-10-04 UTC
  with the prompt "Do all cold reviews and any other work dependent on fable",
  on the Fable tier (`claude-fable-5-1`), orchestrating six rule-4 passes (code,
  design and doctrine passes from a seventeen-pointer queue; the principal sized
  this sitting to the weekly allowance he had left). It wrote this brief from
  the queue pointer, the landing commits' subjects and file lists, and the delta
  paths' names; it did not open the intent record or any prior verdict on these
  surfaces.
- **Who takes the review:** a fresh Fable subagent (`claude-fable-5-1`) spawned
  by the brief-writer with this brief as its only framing. It is not the
  author's session and was not instructed by the author. The reviewer repeats
  its own provenance in the verdict.
- **Orchestration shape, disclosed per rule 4:** reviewer-plus-orchestrator. The
  orchestrator holds the `.deferred.md` sibling outside the worktree and outside
  the harness scratchpad, commits the reviewer's phase-1 findings unrevised,
  then releases the sibling's text by message; the reviewer appends a reconcile
  section; the orchestrator folds the sibling in and updates the pointer. The
  orchestrator forms no finding and writes no severity. Both seats are Fable, so
  the off-tier clause is not invoked; the shape is stated anyway so the record
  is auditable.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material it met before
  writing): the tail of the `docs/SESSIONS.md` index (entries of 2026-09-25 to
  2026-10-03), which includes the authoring run's own one-paragraph summary of
  its work and the 2026-10-03 review session's summary naming finding MC1 in one
  line; every queued `⏳` pointer in section 160 in full (each is refs-only); the
  brief half of `docs/reviews/2026-10-03-0357-manifest-checkpoints-cold.md`
  (lines 1–140, no verdict text) as a formatting template; the landing commits'
  subjects and `--stat` file lists (never the diffs); its own cross-session
  memory notes, which carry the principal's standing words on exceptions and
  guards; and, as doctrine at onramp, `docs/method/ECONOMICS.md` § the
  self-check and the headings of `docs/method/REVIEW.md`. Everything evaluative
  it knows about this delta is in the sibling, not here.

## What the work is

Landing commits (diff these; review the paths at HEAD, `3d4fd9d` or later):

- `c1a3856` (2026-10-03) — pathscan: stream files and cap findings
- `d64c019` (2026-10-03) — linkscan: cap findings, memoise link resolution,
  linear reader
- `87f984f` (2026-10-03) — both: always print the over-cap count
- merge `6b1dc9a` carries the first two. ⚠️ `acb2c78` / `e5b44fe` (pathscan
  brace expansion) and `643cf80` (shared allow-marker grammar) touch the same
  files and are **outside** this delta — reviewed separately

Delta paths:

- `tools/pathscan.py`, `tools/linkscan.py`
- `tools/test_pathscan.py`, `tools/test_linkscan.py`
- the two tools' paragraphs in `tools/README.md`

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether each guard finds, at HEAD, every finding its pre-delta self found — run
both versions (parent of `c1a3856` and HEAD, in a scratch clone) over the repo's
own tree and over fixtures you build, and diff the findings and exit codes.
Fixtures: a finding that straddles any chunk or buffer boundary the streaming
introduces; a very long single line; a file with no trailing newline; CRLF and
lone-CR line ends; invalid UTF-8 and a BOM; a file of only NULs; an allow marker
and its target on either side of a boundary; a file larger than any size
threshold. For the cap: whether the exit code is still red when findings exceed
it, whether the count printed past the cap is true, whether a cap of findings
can hide a different file's findings, and whether the cap is a grounded number
or a fitted one. For linkscan's memoised resolution: whether a cached answer can
be wrong for a second link (relative links from different directories, anchors,
case-insensitive filesystems, a target created or removed during the run).
Whether the README paragraphs say what the tools do. **Non-goal:** the
brace-expansion and allow-marker changes named above.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Streaming presumes no finding needs more context than the reader holds; a cap
   presumes the reader of the output needs only "there are more". Test both
   against how the hook, CI and the floor's renderer actually consume these
   tools' output.
2. **Correctness & quality.** Read both tools and both test files whole. Diff
   the three commits. Run both test files, both `--selftest`s and the full suite
   once. Run the parent-versus-HEAD differential in *Scope* and record it. Time
   each tool on one large generated file and say whether the bounded-memory
   claim holds (measure peak RSS, do not infer it).
3. **Completeness / harvest.** `tools/README.md`, `docs/method/GUARDS.md`, the
   scanner registry in `tools/floor.py`, and any other guard that shares the
   reader or the cap helper. Is the cap's behaviour documented where a child
   would look, and do the other bounded guards cap the same way?
4. **Security & privacy** — mandatory. A guard that can be made to go quiet is a
   security defect. Check whether a committed file can push real findings past
   the cap, hide a finding behind a boundary, or make the tool exit 0 on error
   (unreadable file, decode error, exception in the stream). The house scanner
   is discharged by grounds (landed delta; the pending diff is other passes'
   drafts and this brief) — say so, and deliver the code-altitude read by hand,
   against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- both tools' test files and `--selftest`; the full Python suite once,
  foreground
- the parent-versus-HEAD differential over the repo tree and your fixtures
- peak memory and wall time on one large generated file, both versions
- the floor on both planes at HEAD

## House rules for this run

- You work in the shared review worktree
  `/Users/mike/worktrees/atelier-review-1004` (branch `review-1004`), read-only
  except for THIS brief file. Other sessions are live on this machine and in the
  primary checkout — touch nothing there. Other reviewers are working there at
  the same time on their own briefs; never open another
  `docs/reviews/2026-10-04-2215-*` file — it is another pass's framing.
- Run **no git command that writes** in the worktree (no add, commit, stash,
  checkout, worktree, reset, clean). Read-only git (`log`, `show`, `diff`,
  `blame`, `branch -r`) is fine. Mutation probes, checkouts of older commits,
  scratch children and scratch linked worktrees go in your own clone: `git clone
  <worktree> <scratchpad>/<PREFIX>/probe` under the session scratchpad, named by
  your prefix so parallel reviewers do not collide.
- One heavy process at a time on this machine: run the full Python suite
  (`python3 -m unittest discover -s tools`, in the foreground, ~minutes) at most
  once, never scan any tree outside the worktree or your scratch clone, and
  never point a scanner at the machine's other repos.
- `/security-review` is **discharged by grounds** for this batch: it reads the
  session's pending diff, which in the shared worktree is other passes' unstaged
  drafts, and this is a landed-delta review. State that line in your lens-4
  answer and deliver the code-altitude read by hand, checked against the OWASP
  catalogue where the work has a code surface.
- Dates in your verdict are absolute ISO-8601 from `date -u` (the hook-plane
  `datescan` reds relative words such as "yesterday" or "next week" tree-wide,
  and would block the orchestrator's commit). Wrap prose at ≤ 100 columns. NZ
  English. Never quote a secret, a placeholder token, an email address or any
  personal detail — this repo is PUBLIC; describe, don't quote.
- Review deep, not fast. A finding needs a probe or a re-driven claim behind it,
  not reasoning alone; a clean lens needs the trail that earned it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held by the orchestrator outside the worktree under the rule-1 split and released only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/640-rule-4-cold-pass-queued-bounded-pathscan-linkscan.md`
(it carries the author's own lens hints), and:

- `docs/reviews/2026-09-25-0715-bounded-guard-layer-cold.md`,
  `docs/reviews/2026-09-25-0715-secretscan-stream-pathscan-roots-cold.md`,
  `docs/reviews/2026-10-03-0448-pathscan-brace-expansion-cold.md`,
  `docs/reviews/2026-10-03-0357-shared-allow-marker-grammar-cold.md`
- every item under `docs/roadmap/110-estate-duplication-exception-audit-mike/`
  and `docs/roadmap/115-guardrail-architecture-mike-commissioned/`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-1004 --also-exclude
docs/roadmap/160-doctrine-review-owed/640-rule-4-cold-pass-queued-bounded-pathscan-linkscan.md
--also-exclude docs/roadmap/110-estate-duplication-exception-audit-mike
--also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `BP`: `BP1`, `BP2`, …) and severities (MAJOR / MODERATE
/ minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger with the commands and their results, and a follow-up checklist.
Then STOP and report to the orchestrator that phase 1 is written. Do not open
the sibling (it is not in the tree); do not edit the queue pointer, the board,
or any file but this one.

**Phase 2.** On receipt of the sibling's text, append `### Reconcile` beneath
your verdict: per-finding notes against the seeded questions and the intent
records, any finding formed at reconcile marked as such, and the overall line
restated. Never revise phase-1 text. The orchestrator folds the sibling in below
your reconcile.

The author is not the taker, so record every finding and apply nothing; counsel
on fixes is welcome, labelled as counsel.

---

## Verdict — phase 1 (written 2026-10-04T23:32Z)

**Overall: PASS-WITH-FINDINGS — 0 MAJOR · 4 MODERATE · 5 minor · 1 note.**

The delta does what it set out to do on the shapes it was built for: on the repo's own tree
and on every ordinary fixture the findings and exit codes equal the parent's, the window
ownership rule loses and invents nothing at any alignment tried, the over-cap count is true
and the exit code stays red past the cap. Four things stand against a clean pass. One is a
quiet-direction regression this delta introduced in pathscan (BP1). Two are the same class of
defect already sitting in enforced guards that share the reader, outside this delta's diff
(BP2, BP3). One is that the memory bound the work advertises is not a bound (BP4).

### Provenance

- **How spawned:** a subagent started by the batch orchestrator with this brief file as its
  only framing, finding prefix `BP`, told to do phase 1 and stop. I am not the author's
  session and was neither started nor instructed by it. I am not the brief-writer.
- **Tier:** Fable, `claude-fable-5-1`, as the harness reports it for this session.
- **What I read:** this brief; `tools/pathscan.py` and `tools/linkscan.py` whole at HEAD;
  the full diffs of `c1a3856`, `d64c019` and `87f984f` for the two tools and the README; the
  added test names in both test files and the test bodies my mutation probes pointed at;
  the linkscan and pathscan entries and the output-consumption code in `tools/floor.py`;
  `.githooks/pre-commit` and the two workflow files by grep; the cap comments in
  `tools/leakscan.py` and `tools/secretscan.py`; `docs/method/GUARDS.md` by grep only.
- ⚠️ **Exposure, disclosed:** `git show` printed the three landing commits' message bodies,
  which carry the author's own account of why and the author's measurements. I treated every
  figure in them as a claim to re-drive, and the ledger below is my own numbers. My session
  context also carries one-line index entries from cross-session memory saying that fourteen
  guards were streamed and capped on 2026-09-20 and that the principal wants guards to
  stream and exceptions to be narrowest-scope; I opened no memory file.
- **Barred material:** none opened. No file under the barred roadmap sections, no records,
  no prior verdict, no other `2026-10-04` brief. I ran no tree-wide sweep of `docs/`, so
  `coldsweep.py` was not needed; every grep was scoped to `tools/`, the hook, the workflows
  or `docs/method/GUARDS.md`.
- **Where I worked:** a scratch clone and three linked scratch checkouts under the session
  scratchpad (`BP/probe` at `df3451f`, `BP/parent` at `55536f5` = parent of `c1a3856`,
  `BP/delta` at `87f984f`). The worktree's HEAD moved under me during the pass (`7f8e67d`,
  then `df3451f`, then `ba52df6`), all review commits. The four delta tool and test files are
  byte-identical between `87f984f` and `df3451f`, and the three out-of-delta commits the
  brief names are all ancestors of the parent, so parent-versus-`87f984f` is exactly the
  delta. Nothing in the worktree was written but this file; no Python ran there.

### Lens 1 — approach and assumptions

Load-bearing assumptions, named before testing:

1. *No finding needs more context than one window holds.* True for the token or link itself
   (ownership rule, verified at 160 offsets and 21 paddings, no loss, no duplicate in
   pathscan). **False for the line-level context** the scanners also use: fence state, the
   stub cue, the allow marker, code-span parity. That is BP1, BP3 and BP5.
2. *A physical line is what `\n` delimits.* The parent's pathscan used `str.splitlines()`,
   which also breaks on lone CR, form feed, NEL, U+2028 and others. The delta keeps that for
   ordinary lines and drops it for windowed ones (BP1) and shifts line numbers (BP6).
   linkscan's reader, which predates this delta, never had it (BP2).
3. *A finding costs about 1 KiB, so a count cap is a byte cap.* Borrowed from guards whose
   findings hold a redacted excerpt. These two hold the whole matched text (BP4).
4. *The reader of capped output needs only "there are more".* Checked against the consumers:
   `floor.py` reads these two tools' exit code only and streams their text through
   untouched (the captured `advisory:` count contract is not set for either). So the hook,
   CI and the floor board are all correct past the cap: red stays red. The human reader is
   the one short-changed, when one file's flood hides another file's findings (BP7).
5. *The filesystem does not change during a run* (both memos). Reasoned, not probed: nothing
   in either scan writes, and the parent already cached heading slugs and directory
   listings on the same premise. I record no finding.

### Lens 2 — correctness and quality

- Both test files pass (142 and 84 tests), both `--selftest`s pass, the full suite passes
  once (1,669 tests, 377.9 s).
- **Differential, parent versus delta tip.** Identical findings, exit codes and marker
  counts on: the repo tree (six invocations across both tools); a finding straddling the
  1 MiB read-chunk boundary at 27 alignments; no trailing newline and empty files; CRLF and
  small lone-CR files; a BOM; invalid UTF-8, including a multibyte sequence split across the
  chunk boundary at six offsets; a 2 MiB file of NULs and NUL-laced lines; a 2.7 MiB single
  line of 40,000 distinct findings at twelve paddings (pathscan) and nine (linkscan); one
  finding at each of 160 offsets around the window cut and chunk end; the same link text
  from three directories with anchors, wrong case, root-relative and escaping forms (94
  findings both sides, on a case-insensitive volume).
- **Differences found:** BP1 (lone CR in a windowed stretch), BP5 (marker or stub cue in a
  different window from its target), BP6 (line numbers after form feed or NEL), and the
  documented one-pass blanking residual (two extra findings on nested shapes past 16 KiB,
  loud direction, as the README says).
- **The memoised resolution** is keyed on `(directory, link path)` and everything
  `_resolve_link` computes depends on the linking file only through its directory, so a
  cached answer cannot be wrong for a second link; the per-link anchor is still checked
  each time. Mutating the key to the path alone is killed by the tests.
- **The rewritten `_strip_inline_code`** equals the parent's on 300,000 random strings.
- **Mutation probes, 18.** Fourteen killed. Four survived: two are effectively equivalent
  (the per-line dedupe masks a dropped overlap-edge test; an overflow-only JSON state cannot
  occur in a real run), two are real gaps (BP8).
- **Memory and time, measured** (peak RSS from `/usr/bin/time -l`, 3.14 interpreter):

  | file | tool | parent | delta |
  |---|---|---|---|
  | 89 MiB, short clean lines | pathscan | 95.7 s, 589 MiB | 52.4 s, 22 MiB |
  | 89 MiB, short clean lines | linkscan | 70.3 s, 25 MiB | 8.5 s, 22 MiB |
  | 191 MiB of 200 KB lines | pathscan | killed 150 s, 818 MiB | 42.5 s, 88 MiB |
  | 191 MiB of 200 KB lines | linkscan | killed 120 s, 221 MiB | 16.7 s, 57 MiB |
  | 101 MiB, no newline | pathscan | killed 100 s, 420 MiB | 22.6 s, 30 MiB |
  | 101 MiB, no newline | linkscan | killed 100 s, 198 MiB | 8.1 s, 55 MiB |
  | 114 MiB, 1,200 fat findings | pathscan | 33.8 s, 715 MiB | 30.1 s, 609 MiB |
  | 114 MiB, 1,200 fat findings | linkscan | 17.0 s, 612 MiB | 13.4 s, 610 MiB |

  The claim holds on the first six rows and fails on the last two (BP4). The linkscan total
  on the no-newline file is also short of the links written, which is what led to BP3.

### Lens 3 — completeness and harvest

- `tools/README.md` carries a paragraph per tool and both say what the cap does. Gaps: the
  per-window scope of markers and stub cues (BP5) and the lone-CR behaviour (BP1) are not
  among the named residuals, and "resolved once per scan" holds only to the 50,000-entry
  memo bound (BP10).
- `docs/method/GUARDS.md` says nothing about caps, bounds or streaming (grep for cap, capped,
  bounded, stream: no hit). A child reading doctrine rather than the tool README does not
  learn that five guards stop listing at 50,000 (BP10).
- `tools/floor.py` needed no change: both tools are consumed by exit code.
- **Do the other bounded guards cap the same way?** Same constant, same counter name, same
  summary fragment, same always-printed zero. Not the same in substance: leakscan,
  secretscan and conflictscan hold redacted or excerpted findings, so their per-finding size
  is bounded and the 1 KiB premise is true for them; these two hold unbounded text (BP4).
- **Other guards sharing the reader.** The `\n`-only chunked reader is in linkscan,
  leakscan, conflictscan and datescan by grep. I probed linkscan and leakscan and both go
  green on a lone-CR file that their LF twin reds (BP2). conflictscan, datescan and
  secretscan are unprobed.

### Lens 4 — security and privacy

`/security-review` is **discharged by grounds** for this batch: it reads the session's
pending diff, which in the shared worktree is other passes' unstaged drafts, and this is a
landed-delta review. The code-altitude read below is by hand against the OWASP catalogue.

- **Can a committed file push real findings past the cap?** Yes for the *listing*, no for
  the *verdict*: exit code and total stay true (BP7).
- **Can a committed file hide a finding behind a boundary?** Yes. BP1 (pathscan, this
  delta), BP2 and BP3 (enforced siblings, before this delta).
- **Exit 0 on error?** No. An unreadable file exits 2 in both tools on both versions; a
  dangling symlink or a symlink loop named as a path exits 2; a directory named like a
  Markdown file and a symlink loop met during the walk are skipped and the remaining
  findings still red; decode errors are replaced and the file is still scanned; pathscan's
  error path returns 2 even under `--warn`.
- **Injection (A03):** neither tool shells out, evaluates or formats input into a command.
- **Access control / traversal (A01):** linkscan refuses a target outside the root before it
  reads any heading from it. pathscan will `stat` a `..`-led token outside the root; that is
  an existence test only, reads no content, and predates the delta.
- **Insecure design (A04):** the quiet-direction findings above.
- **Logging and monitoring (A09):** marker suppressions and over-cap counts are printed
  every run. Stub-cue suppressions are not tallied at all (before the delta), which is what
  makes the stub-cue half of BP1 traceless.
- **Resource exhaustion:** BP4 (memory) and BP9 (time). Both fail loud, not quiet.
- **Privacy:** the delta adds no personal data, and my fixtures and this verdict quote none.

### Findings

**BP1 — MODERATE — pathscan treats a windowed stretch as one line, so non-LF line ends
inside it stop meaning anything; a red scan can turn green.** The parent split the whole
text with `splitlines()`. The delta does that only for a segment that is both first and
final; a stretch of 256 KiB or more between `\n` bytes is yielded as raw windows with one
line number, one fence verdict (taken on the first window), and the stub cue and allow
marker tested against the whole window. On a 2.6 MiB Markdown file with lone-CR line ends
and 60,000 one-per-line ghost paths (parent: 60,000 findings on 60,000 lines, exit 1):

| variant | parent | delta |
|---|---|---|
| plain | 60,000 findings, lines 1–60,000 | 60,000 counted, every one at line 1 |
| a three-line fenced block at the top | 60,000, exit 1 | **0 findings, exit 0** |
| one line saying TODO | 59,999 | 38,683 — 21,316 gone, nothing tallied |
| one line with an allow marker | 59,999, 0 by marker | 38,684 — 21,315 "by marker" |

`_iter_file_content_lines`' docstring says line numbers and fence state "match the old
reader exactly"; no test covers the shape. Held below MAJOR by two facts: the input is
exotic (lone-CR or similar, and at least 256 KiB without an LF), and pathscan is wired
warn-only, so no build changes colour. It should not survive a flip to blocking.
*Counsel:* split each window on the same separators `splitlines()` uses and carry fence
state and line count through, or refuse the windowed path for a stretch that contains them.

**BP2 — MODERATE — outside this delta, same class, enforced guards: the shared `\n`-only
reader widens one line-scoped allow marker to a whole lone-CR file.** Formed under lens 3.
linkscan at HEAD on a nine-line file: the CRLF twin gives 2 findings, exit 1, 1 by marker;
the lone-CR twin gives "clean", exit 0, 4 by marker. The parent behaves identically, so
this predates the delta. leakscan at HEAD on a five-line file with one rule-scoped marker on
line 2 and an unmarked email-shaped address on line 4: LF twin 1 finding, exit 1; lone-CR
twin clean, exit 0, 2 by marker. A lone-CR file that opens with a fence silences linkscan
entirely (0 findings, exit 0, both versions). The suppression is counted, which is the only
trace. A line-scoped exception becoming file-scoped runs against the house rule that an
exception is the narrowest unit. Not MAJOR on my reading because it needs a line-end
convention nobody produces by accident and gives a committer nothing a per-line marker
would not; whoever owns those guards' reviews may weigh the leak guard differently.
conflictscan, datescan and secretscan are unprobed.

**BP3 — MODERATE — outside this delta's diff, inside its claims: linkscan drops a whole
window's links when the window cut lands inside a code span.** Each window is stripped of
inline code on its own, so a window that starts inside a span pairs every later backtick
the wrong way round and blanks the prose between spans. Controlled probe, one 1.3 MiB line,
5,000 distinct broken links each preceded by a short code span: cut outside any span, 5,036
reported (36 are overlap duplicates); cut inside a span, **37 reported**; parent identical.
This is why the 101 MiB no-newline run above reports 1,299,176 links where 1,700,000 were
written. The reader's own residual note says nothing is dropped silently, and the README
sentence this delta added says the headline total stays true; on an overlong line neither
holds, and the total is also inflated by links counted twice in the overlap (40,124 for
40,000). Exit stayed 1 in my probes only because other windows still held findings.
*Counsel:* carry the open-span state across windows, or strip code spans before windowing.

**BP4 — MODERATE — the memory bound is a count, not a bound.** `scan_file` says peak
memory is "bounded by a constant however large the file or its longest line", the cap
comment says "~50 MiB of findings regardless of input size", the README says "bounded on
any single file". A 114 MiB file of 1,200 lines, each one ghost path and one same-file
anchor about 50 KB long, holds 609 MiB (pathscan) and 610 MiB (linkscan) with 1,200 findings
— 2.4% of the cap. Ordinary findings cost 404 and 282 bytes each (traced heap at a full
cap), so the number is safe for ordinary input; it was reused from guards whose findings
are redacted excerpts, and the premise that makes it a byte budget there does not transfer
to a `Finding` that holds the whole target twice. The cap is therefore grounded for the
siblings and borrowed here. Failure is loud (an out-of-memory kill), not quiet.
*Counsel:* truncate `target` and `detail` to a fixed length, as the siblings' excerpts do;
then the claim is true as written.

**BP5 — minor — an allow marker or stub cue now reaches only its own window.** On a
1.3 MiB line with the target at one end and the marker or TODO at the other, pathscan
reports 4 findings the parent exempted and linkscan 1 (marker after the link; marker before
still exempts, because the per-line map persists). Loud direction. `check_file`'s docstring
says the verdict is "the one the old end-of-file pass reached", which is untrue here, and
the README names no such residual.

**BP6 — minor — pathscan line numbers moved for files with a form feed, NEL, VT or similar
immediately before `\n`.** The parent counted that pair as two line ends; the delta counts
one. A form feed on its own line shifts every later finding up by one (fixture: line 25
became 17). 724 of 20,000 random small files differ in line numbers only; none differ in
findings. The new numbers agree with an editor's, so this is arguably a correction, but the
docstring claims an exact match and the commit's byte-identity was shown on atelier's tree
only.

**BP7 — minor — the cap is run-wide and first-come in walk order, so one file's flood
removes another file's findings from the listing and from `--json`.** 60,000 findings in
one file and one in another: with the names one way round the single finding is listed,
the other way round it is absent from both outputs and the over-cap line names no file.
Count and exit code are true. For pathscan, wired warn-only, the listing is the whole
signal. *Counsel:* print a per-file count for findings past the cap; that stays constant
space per file.

**BP8 — minor — test gaps the mutation probes exposed.** Re-taking the fence verdict on
every window survives (no test has a continuation window that starts with a fence run).
Setting the exact-blanking threshold to zero survives (nothing pins nested blanking on an
ordinary line, the behaviour the comment says is "untouched"). No test covers BP1's shape
or BP5's.

**BP9 — minor — outside the diff, inside the purpose: pathscan's scheme-URL pattern is
still quadratic on a long run of dotted or hyphenated words.** A single line of a two-byte
letter-dot unit: 20 KB 0.5 s, 40 KB 1.5 s, 80 KB 5.5 s, same on the parent; the pattern
alone reproduces it. Extrapolated to one 1 MiB window that is of the order of a quarter of
an hour. "One huge file stays flat" does not hold for time on this shape; a committed file
can stall the hook. Loud, not quiet.

**BP10 — note — documentation drift.** (a) pathscan's module docstring still says it is not
in the floor registry; it has an entry. Before this delta. (b) The README's "resolved
against the disk once per scan" is true up to 50,000 memo entries. (c) `GUARDS.md` does not
mention that five guards cap their listing. (d) linkscan's total counts a link in a window
overlap twice; before this delta, and now printed under a sentence saying the total is true.

### Re-run ledger

All commands ran in the foreground from the scratch area `BP/` (clone `probe` at `df3451f`,
`parent` at `55536f5`, `delta` at `87f984f`), one heavy process at a time.

| what | command (abridged) | result |
|---|---|---|
| pathscan tests | `unittest discover -s tools -p test_pathscan.py` | 142 OK |
| linkscan tests | `unittest discover -s tools -p test_linkscan.py` | 84 OK |
| selftests | `pathscan.py --selftest`, `linkscan.py --selftest` | both OK, exit 0 |
| full suite, once | `unittest discover -s tools` | 1,669 OK, 377.9 s |
| floor, hook plane | `floor.py --plane hook --root . --tools tools` | exit 0 |
| floor, ci plane | `floor.py --plane ci --root .` | exit 0 |
| repo-tree differential | `tree.py`: 4 pathscan + 2 linkscan invocations | all identical |
| repo-tree human output | parent, delta, HEAD, both tools | differ only by the zero field |
| fixture differential | `diffharness.py` (10 groups), `ll2.py` | see lens 2, BP1, BP5, BP6 |
| lone-CR siblings | linkscan and leakscan at HEAD, LF/CRLF vs CR twins | BP2 |
| code-span parity | `parity2.py`, parent vs delta | 5,036 vs 37, both versions |
| cap hides a file | `fx/cap`, `fx/cap2`, human and `--json` | BP7; exit 1, total 60,001 |
| per-finding cost | `persize.py`, tracemalloc at a full cap | 404 B and 282 B |
| memory and time | `measure.py`, four files, both versions | table in lens 2 |
| stripper fuzz | `fuzz.py`, 300,000 strings | 0 differences |
| reader fuzz | `fuzz.py`, 20,000 small files | 0 finding diffs, 724 line-only |
| mutation probes | `mutate.py`, 18 mutants | 14 killed, 4 survived |
| error paths | unreadable, loop, dangling, dir-as-file | exit 2 or findings, never 0 |
| pathological lines | `redos.py`, 8 shapes × 3 sizes | one quadratic (BP9) |

Floor detail at `df3451f`: linkscan enforced and green; pathscan warn-only with 2 findings
on its floor scope and 45 on its default scope, the same on the parent, none from this
delta; secretscan 22 advisory; leakscan green with the cover note the ci plane always
prints.

Not done, said plainly: I did not probe conflictscan, datescan or secretscan for BP2's
class; I did not test a target created or removed mid-run; I did not run the author's
500 MB sizes, only 89 to 191 MiB; BP9's quarter-hour figure is extrapolated from three
measured sizes, not run.

### Follow-up checklist

- [ ] BP1 — make pathscan's windowed path honour the line ends `splitlines()` honours, or
      correct the docstring and name the residual; add the lone-CR fixture as a test.
- [ ] BP2 — give the lone-CR class its own board item against the shared reader; probe
      conflictscan, datescan and secretscan before sizing it.
- [ ] BP3 — carry code-span state across linkscan's windows; correct the "nothing is
      dropped silently" and "total stays true" sentences until then.
- [ ] BP4 — bound the size of a held finding in both tools, or restate the three claims as
      "bounded for findings of ordinary length".
- [ ] BP5 — name the per-window marker and stub-cue scope in both README paragraphs and fix
      `check_file`'s docstring.
- [ ] BP6 — correct the "match the old reader exactly" claim.
- [ ] BP7 — decide whether the over-cap line should name files.
- [ ] BP8 — add the two missing pins.
- [ ] BP9 — board item for the scheme-URL pattern.
- [ ] BP10 — four documentation corrections.

Phase 1 ends here. I have not opened the sibling, the queue pointer or the board.

### Reconcile

Written 2026-10-04T23:37Z, after the orchestrator committed phase 1 unrevised (`ed54c8b`)
and released the sibling's text by message. Phase-1 text above is untouched.

**What I opened for this phase, and only this:** the commissioning item `110/120`; items
`110/100`, `110/140` and `115/220` in full, the rest of those two sections by grep; the
queue pointer; the intent record `docs/sessions/2026-10-03-0144-…` by grep (it gives this
work one line, "pathscan and linkscan stream and cap", so the commit messages and `110/120`
are the real intent record); the four released prior verdicts by grep for my finding
classes, reading the findings that matched (BL3, BL7, SP3, SP7, SP9, PX7). Nothing else.

**The principal's words** (`110/100`, quoted there): a guard "should not try and load a
whole file or all results into memory, it needs to continually close work as it opens new
work", and an exception is to be "as narrow an exception as possible". The brief-writer's
recollection matches the first; the second bears on BP2 and BP5.

**The commissioning item's acceptance:** "Output must stay identical on atelier's tree, and
both must hold flat memory on the synthetic files." Both are met on my re-run: the tree
differential is identical bar the deliberate known-zero field, and my four author-shaped
rows are flat (22 to 88 MiB against 198 MiB to 818 MiB and rising). My sizes were 89 to
191 MiB, not the item's 200 and 500 MB, so I confirm the shape of its table, not its cells.

#### Seeded questions

1. *Does the cap satisfy "never all results" without turning a red into a green?* On the
   second half, yes, with the trail behind it: the exit code and the headline read the true
   total on every path, two mutants that read the held list instead are killed, and the cap
   is charged after the allow-marker subtraction (the lesson of SP3 part ii, applied here —
   two mutants that reverse the order are killed). No cap path I could build turns red to
   green. On the first half, only for results of ordinary size: the cap counts findings and
   each finding holds unbounded text, so 1,200 results held 609 MiB (BP4). The reds that do
   turn green in this pass come from the reader, not the cap (BP1, BP2, BP3).
2. *Is the over-cap count a known zero on every output path?* Yes. Re-driven at reconcile
   on ten paths: both tools × clean and findings × human and `--json`, plus pathscan
   `--warn` in both forms; the field is present once on each. The paths with no field are
   the exit-2 error paths and `--selftest`, which print no summary at all, and a
   `render_human` call with no tally, which no command line reaches.

#### Per finding

- **BP1 — new; stands at MODERATE.** Nothing in the released surfaces mentions lone CR,
  `splitlines` semantics or any non-LF line end in a streamed reader (grep across both
  roadmap sections, the intent record and all four verdicts: no hit). SP7 (2026-09-25)
  recorded that pathscan read files whole; this delta is that fix, and BP1 is what the fix
  cost. `110/120` lists three named residuals and this is not among them.
- **BP2 — new as a recorded finding; predates this delta; stands at MODERATE.** The
  released verdicts on the layer that introduced the shared reader (the `BL` and `SP`
  passes of 2026-09-25) probed window straddles, truncation and caps, and neither probed
  line-end conventions. So the class has sat unrecorded since the readers were streamed.
  Read against the principal's own words on narrowness it is a plain breach: one
  line-scoped marker becomes file-scoped with no record that it widened. I weighed raising
  it to MAJOR on that ground and hold it at MODERATE for consistency with how this house
  has rated nearer cases in the same layer — SP2 (an unreadable file became a clean pass)
  and BL1 (a real finding past a truncation point exits 0) were both MODERATE and both
  easier to reach than a lone-CR file. It needs its own board item; it is not this delta's
  to fix.
- **BP3 — half recorded, half new; stands at MODERATE.** The double count in linkscan's
  overlap is BL3 (2026-09-25, minor), whose follow-up "add dedupe to linkscan's windowed
  path" is still open at HEAD: my 40,124-for-40,000 is that defect re-measured. The dropped
  window — a cut inside a code span blanking the links after it — is recorded nowhere I was
  released to read. PX7 (2026-10-03) is line-local backtick parity in pathscan's command
  skip, a different mechanism. `115/220` already says linkscan's fence state is "guard
  business logic riding inside the reader"; code-span state is a second instance of the
  same thing and belongs in that decision.
- **BP4 — new for these two tools; stands at MODERATE.** The 50,000 figure is grounded
  where it was derived (secretscan's own comment records a measured cost per finding) and
  BL7 already asked for ceilings to be grounded in the record's shape. The item's
  acceptance is met; what fails is the unconditional wording in the docstring, the cap
  comment and the README, and the principal's "all results into memory" for a file of long
  findings. The item's after-column (46 to 52 MB) is consistent with mine on its shapes.
- **BP5 — known class, new instances; stands at minor.** SP9 (2026-09-25, note) recorded
  the same per-window scope of markers in secretscan and asked for a sentence beside the
  window constant. This delta brought the class to pathscan and to linkscan's subtraction
  without that sentence.
- **BP6 — new; stands at minor.**
- **BP7 — known class; stands at minor.** SP3 part i (2026-09-25, MODERATE) is the same
  starvation inside secretscan, where it could hide a *blocking* finding behind advisory
  ones. Here every finding is one kind and the exit code is unaffected, hence minor.
- **BP8 — new; stands at minor.** Same family as SP4 (mechanisms shipped without a direct
  test); this delta did ship direct tests, and the gaps are the specific ones named.
- **BP9 — new; stands at minor.** `110/130` covers regex cost per byte in leakscan and
  secretscan only; pathscan's scheme-URL pattern is not in it, nor in `110/120`'s residuals.
- **BP10 — stands as a note.** Part (d) is BL3 again; part (c) is BL4's class (bounds
  documented in one README section of fourteen); parts (a) and (b) are new.
- **BP11 — note (formed at reconcile).** `110/120` says its three named residuals are "in
  the README". One is. The pathscan paragraph names the 16 KiB one-pass blanking; neither
  paragraph names that a token over 4 KiB can be lost at a window cut, nor that linkscan's
  basename index still scales with tree size (grep of `tools/README.md` for either: no
  hit). The first of those is a quiet-direction residual a child would want to read.

#### Overall, restated

**PASS-WITH-FINDINGS — 0 MAJOR · 4 MODERATE (BP1–BP4) · 5 minor (BP5–BP9) · 2 notes
(BP10, BP11; BP11 formed at reconcile).** No phase-1 severity moved. In the delta proper:
BP1, BP4, BP5, BP6, BP7, BP8, BP11. Outside its diff and owed their own items: BP2, BP3's
dropped-window half, BP9. Already on record elsewhere: BP3's double count (BL3), the
classes behind BP5 (SP9) and BP7 (SP3), and two parts of BP10 (BL3, BL4).

Follow-up added at reconcile:

- [ ] BP11 — name the 4 KiB token and basename-index residuals in the README paragraphs, or
      correct `110/120`'s "in the README".

## Deferred material — folded in at reconcile

# Deferred material — bounded-pathscan-linkscan (open only after your findings are durably written)

Sibling of `docs/reviews/2026-10-04-2215-bounded-pathscan-linkscan-cold.md`
under REVIEW.md rule 1's split; held by the orchestrator outside the worktree.
Folded into the brief below the verdict when the verdict lands.

## Intent records

- `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md` — the
  authoring run's account. **Not opened** by the brief-writer.
- `docs/roadmap/110-*/120-pathscan-and-linkscan-are-unbounded-on-one-big-file.md`
  — the commissioning item. **Not opened.**
- The principal's standing words on guards, known to the brief-writer from its
  own memory and not from this run: guards never load whole files or all
  results.

## Prior verdicts and barred items on the same surfaces

- `docs/reviews/2026-09-25-0715-bounded-guard-layer-cold.md`,
  `docs/reviews/2026-09-25-0715-secretscan-stream-pathscan-roots-cold.md`,
  `docs/reviews/2026-10-03-0448-pathscan-brace-expansion-cold.md`,
  `docs/reviews/2026-10-03-0357-shared-allow-marker-grammar-cold.md`
- every item under `docs/roadmap/110-estate-duplication-exception-audit-mike/`
  and `docs/roadmap/115-guardrail-architecture-mike-commissioned/`

## The queue pointer's own lens hints — the author's seeded questions, verbatim

The pointer carries no lens paragraph — refs only.

## Brief-writer's seeded questions (a floor, never a fence)

Generate your own before reading these; a question you did not think of is a
prompt to re-read the surface, not an agenda.

1. Does the cap satisfy the principal's "never all results" without ever turning
   a red into a green?
2. Is the over-cap count a known zero when unreached, on every output path, as
   the third commit claims?
