# Cold pass — the linear line reader in three guards

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-10-04 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/660-rule-4-cold-pass-queued-linear-reader.md`.
**Why it earns a review:** the line reader in the secret, leak and
conflict-marker guards was rewritten for speed; these are the guards a public
repo's every commit depends on, and a reader that splits or joins lines
differently changes what they see without any test of theirs noticing.

## Spawn provenance

- **Author of the work under review:** the 2026-10-03 queue run (an Opus
  orchestrator with dispatched workers) that landed the commits named under
  *What the work is*. This brief-writer was not that session, was neither
  started nor instructed by it, and has edited none of the delta's paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-10-04 UTC
  with the prompt "Do all cold reviews and any other work dependent on fable",
  on the Fable tier (`claude-fable-5-1`), orchestrating three rule-4 passes
  (code passes from a seventeen-pointer queue; the principal sized this sitting
  to the weekly allowance he had left). It wrote this brief from the queue
  pointer, the landing commits' subjects and file lists, and the delta paths'
  names; it did not open the intent record or any prior verdict on these
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

- `55426a1` (2026-10-03) — leakscan: linear line reader
- `633f6e9` (2026-10-03) — secretscan: linear line reader
- `b5cc3c4` (2026-10-03) — conflictscan: linear line reader
- ⚠️ `643cf80` (shared allow-marker grammar) touches the same files and is
  **outside** this delta — reviewed separately

Delta paths:

- the line readers in `tools/leakscan.py`, `tools/secretscan.py`,
  `tools/conflictscan.py`
- their tests in `tools/test_leakscan.py`, `tools/test_secretscan.py`,
  `tools/test_conflictscan.py`

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether each new reader yields exactly the lines, line numbers and byte offsets
the old one did, for every input — extract old and new readers (parent of each
commit against HEAD, in a scratch clone) and run them differentially over the
repo's tree and over generated inputs: empty file; no trailing newline; CRLF,
lone CR, mixed; a line longer than every buffer; a line ending exactly on each
buffer boundary and one byte either side; a multi-byte UTF-8 character and a
CRLF pair split across a boundary; invalid UTF-8; NULs; a BOM; form feeds,
vertical tabs and the Unicode line separators that `str.splitlines` honours and
a byte split on newline does not. Property-test it with random inputs and random
chunk sizes if the chunk size can be injected. Then at tool level: seed a
fixture secret, a fixture term and a conflict marker at each of those positions
and confirm each guard still finds it with the right line number, and that an
allow marker still binds to the same line. Whether the three readers are one
function or three copies, and if copies, whether they differ. Whether the
linear-time claim holds — measure it. **Non-goal:** the allow-marker grammar
change named above, and what the guards' patterns match.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   "Linear, same output" is two claims; the tests may prove the first and assume
   the second. Establish what definition of a line each guard needs (its
   findings quote line numbers and its allow markers bind by line) and whether
   the new reader keeps it.
2. **Correctness & quality.** Read the three readers and their tests whole. Diff
   the three commits. Run the three test files, the three `--selftest`s and the
   full suite once. Run the differential and the tool-level seeding in *Scope*
   and record a table. Time old against new on a large many-line file and on one
   enormous line.
3. **Completeness / harvest.** Every other guard that reads lines (`grep -n` for
   the reader's name and for per-line slicing across `tools/`): which still
   carry the old shape, and is that recorded anywhere a reader of
   `tools/README.md` would find? Do the README paragraphs for the three guards
   still describe them?
4. **Security & privacy** — mandatory. These are the secret and leak guards of a
   public repository. Any input on which the new reader yields less than the old
   is a way to commit a secret unseen: hunt for it specifically, including an
   attacker-chosen line ending or boundary position. Use fixture strings you
   invent that are not real credentials and never quote them in the verdict. The
   house scanner is discharged by grounds (landed delta; the pending diff is
   other passes' drafts and this brief) — say so, and deliver the code-altitude
   read by hand, against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- the three test files and `--selftest`s; the full Python suite once, foreground
- the old-versus-new reader differential, with the input classes in *Scope*
- the tool-level seeding at boundary positions, all three guards
- old-versus-new timing on two large generated files
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
`docs/roadmap/160-doctrine-review-owed/660-rule-4-cold-pass-queued-linear-reader.md`
(it carries the author's own lens hints), and:

- `docs/reviews/2026-09-25-0715-bounded-guard-layer-cold.md`,
  `docs/reviews/2026-09-25-0715-secretscan-stream-pathscan-roots-cold.md`,
  `docs/reviews/2026-10-03-0357-shared-allow-marker-grammar-cold.md`
- every item under `docs/roadmap/110-estate-duplication-exception-audit-mike/`
  and `docs/roadmap/115-guardrail-architecture-mike-commissioned/`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-1004 --also-exclude
docs/roadmap/160-doctrine-review-owed/660-rule-4-cold-pass-queued-linear-reader.md
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
with stable IDs (prefix `LN`: `LN1`, `LN2`, …) and severities (MAJOR / MODERATE
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

## Verdict — phase 1 (2026-10-04 UTC)

**Overall: PASS-WITH-FINDINGS — 1 MAJOR, 1 MODERATE, 3 minor, 4 notes.**

The delta itself is clean: the new reader yields exactly what the old one did on
every input I could construct, in all three guards, and the speed-up is real.
The MAJOR is not in the three commits. It is in the hook plane's own line
splitter, which the reader never touches, and it was found by doing what lens 4
asks: hunting an attacker-chosen line ending through each guard's planes.

### Provenance

- **How I was spawned:** a subagent started by the batch orchestrator named in
  *Spawn provenance*, with this brief as the only framing, plus house
  instructions (prefix `LN`, phase 1 only, foreground runs, touch no other
  repo). I am not the author's session and was not instructed by it.
- **Tier:** Fable (`claude-fable-5-1`), checked at start.
- **What I read:** this brief; the three landing commits in full (messages,
  code and test diffs); the three guards' readers, scan loops, staged-diff
  parsers, binary check and CLI at HEAD; the added `ReaderLinear` test classes;
  `tools/allowmarker.py` (grep only); the reader functions of the other
  streaming guards; `tools/README.md` by grep and four short excerpts;
  `.githooks/pre-commit`; `tools/floor.py --help`; `.github/workflows/ci.yml`
  by grep.
- ⚠️ **Exposure, disclosed:** the landing commits' messages are the author's
  own account (they name board item numbers, a claimed byte-identity check and
  timings). They are part of the delta, so reading them is not barred, but they
  are narrative and I re-drove each claim rather than leaning on it. One
  `coldsweep` hit returned the title line of this pass's own queue pointer in
  `docs/ROADMAP.md`. I opened nothing under the *Deferred reading* bar, no
  prior verdict, and no other `2026-10-04-2215-*` file. No `--include-barred`.
- **Where the probes ran:** a clone of the worktree under the session
  scratchpad (`LN/probe`, at `f1a667b`), the pre-delta `tools/` extracted from
  `55426a1^` beside it (`LN/old`), and throwaway git repositories under the
  same directory for the staged plane. The worktree was only read.
- **One deviation:** every `leakscan` run I made passed `--terms` with a
  one-term scratch list, so the machine-local term list was never read and
  nothing from it can appear here. Fixture strings were invented, assembled at
  run time, and are not quoted.

### Lens 1 — approach and assumptions

Load-bearing assumptions, named before reading the tests:

1. *Same lines.* Walking an offset and cutting once per chunk yields the same
   `(lineno, text, is_final)` triples as cutting per line. **Holds** — see the
   differential in lens 2.
2. *Same windows.* The window test and the overlap tail see the same `pending`
   as before, because the single cut happens before the window check.
   **Holds** — mutation M4 (cut moved after the window check) is killed, and
   the differential covers it at seven constant sets.
3. *Same memory bound.* `pending` is no longer shrunk while a chunk is walked,
   but it never exceeded window plus one chunk at the top of the walk in the
   old shape either. **Holds** — the `BoundedMemory` tests pass in the full
   suite.
4. *"Linear" is new.* **Only loosely** — LN8.
5. *The reader is the guards' line definition.* **False for the hook plane**,
   which never calls it — LN1, LN3.

What a line is, per guard and plane, established by reading and by probe:

| Plane | Splits on | Used by |
| --- | --- | --- |
| tree (CI, `--root`) | LF only; CR kept in the text | the reader, all three |
| staged (hook) | universal newlines, then `str.splitlines` | all three |
| `scan_text` helper | `str.splitlines` | selftests, unit tests |

The reader keeps the definition the old reader had (LF only), so line numbers
and allow-marker binding on the tree plane are unchanged by this delta. For
`conflictscan`, LF-only is also git's own definition, so it is the right one.
The three definitions disagree with each other, and that disagreement is where
LN1 lives.

### Lens 2 — correctness and quality

**The three readers are three copies, not one function.** With comments and
docstrings stripped, the three `_iter_numbered_lines` bodies hash identically
(31 code lines each). They differ only in comment text. The tests add three
further copies of the old loop as oracles (LN6).

**Reader differential, old (`55426a1^`) against new (HEAD):**

| Input set | Cases | Old ≠ new | Spec model ≠ new |
| --- | --- | --- | --- |
| 49 generated classes × 6 small constant sets × 3 guards | 882 | 0 | 0 of 209 |
| the same classes at the real constants × 3 guards | 147 | 0 | 0 of 43 |
| 40,000 random inputs, random chunk/window/overlap × 3 | 120,000 | 0 | 0 of 28,816 |
| every tracked file in the tree (933 files, 170,084 lines) × 3 | 2,799 | 0 | — |

The generated classes are the brief's list: empty; no trailing newline; CRLF,
lone CR, mixed; a line longer than every buffer; a line ending on the chunk,
double-chunk and window boundaries and one byte either side; two- and
four-byte characters at every offset across a chunk boundary; a CRLF pair split
across a boundary; invalid and truncated UTF-8, including at a chunk edge;
NULs before and after the binary check's reach; UTF-8 and UTF-16 BOMs; form
feed, vertical tab, the C0 separators, NEL and the two Unicode line separators.
The spec model is an independent whole-file decode split on LF; it is compared
only where no window was cut. My first model disagreed 5,515 times; the fault
was mine (it applied the binary check to the whole file where the reader
applies it to the first chunk), and after correcting the control it agrees
everywhere. Across guards the three copies agree with each other on every case.

**Tool-level seeding, old CLI against new CLI, real constants, tree plane:**
178 cells (four fixtures — a secret shape, a structural leak shape, a local
term, a conflict opener — at up to 51 positions each). Output, stderr and exit
code were identical old-to-new in all 178. Against expectation:

| Position class | Result |
| --- | --- |
| first line; last line with no newline; CRLF file | found, right line |
| line ending / starting at the chunk boundary, ±1 byte | found, right line |
| fixture straddling the 1st and 2nd chunk boundary (3 offsets each) | found |
| after 20,000 and after 150,000 short lines | found, lines 20001 / 150001 |
| after a four-byte character split by a chunk; after invalid UTF-8 | found |
| line after an overlong line; after a line of exactly W and W−1 chars | found, line 2 |
| overlong line: fixture across the window cut, in the overlap, at the end | found once |
| after CR, FF, VT, FS, NEL, U+2028 inside one LF-line | found, LF line number |
| allow marker on the same line (also straddling a chunk) | suppressed |
| allow marker on the previous or the next line only | not suppressed |
| NUL in the first 8 KiB | file skipped; NUL later: scanned |

Three cells missed my expectation and all three were my expectation, not the
tools: a bare allow marker does not cover a local-term hit (the grammar wants
the scoped form; non-goal), and a conflict opener placed after a BOM is not at
column 0 (git writes the marker before the BOM, so the case is unreal).
Recorded behaviours, identical old-to-new: LN7.

**Tests.** The three test files pass (136, 159 and 41 tests), the three
selftests pass, and the full suite passes once (1,669 tests, 388 s). Mutating
the reader in the scratch clone, nine mutants per guard: eight are killed by
`ReaderLinear` alone, including reverting to the per-line re-slice; one
survives the whole test file in all three guards (LN4).

**Timing** (this machine, Python 3.14.6, one process at a time):

| Measure | Old | New |
| --- | --- | --- |
| reader only, 50 MB of 80-char lines | 17.8 s | 0.29 s |
| reader only, 100 MB of 80-char lines | 31.9 s | 0.36 s |
| reader only, 50 MB of 16-char lines | 83.3 s | 0.99 s |
| reader only, 100 MB of 16-char lines | 160.5 s | 1.75 s |
| reader only, one 100 MB line (24 windows) | 0.07 s | 0.07 s |
| `conflictscan` CLI, 50 MB of 80-char lines | 15.0 s | 1.3 s |
| `secretscan` CLI, same file | 38.4 s | 22.8 s |
| `leakscan` CLI, same file, one-term list | 37.1 s | 21.7 s |
| three CLIs, one 50 MB line | 0.7 / 17.2 / 17.3 s | 0.7 / 18.7 / 15.8 s |

The commit messages' figures for `conflictscan` and `secretscan` reproduce
within noise. The `leakscan` figure (65 s to 52 s) does not reproduce as
absolute numbers with my one-term list, but the saving does (about 15 s in
both), which is what the reader accounts for.

### Lens 3 — completeness and harvest

- Six other guards still carry the per-line re-copy the delta removed — LN2.
  `linkscan` and `pathscan` already carry the offset walk.
- `tools/README.md` describes the three guards' bounded reading in terms the
  delta does not change (streamed, windows for an overlong line), so those
  paragraphs still hold. It says nothing about reader speed for any guard, and
  nothing about the hook plane's different line splitting (LN1). Its standing
  residual says a binary file is skipped "on the first NUL byte"; the check is
  a NUL in the first 8 KiB, and a NUL after that does not skip the file (LN9).

### Lens 4 — security and privacy

`/security-review` is **discharged by grounds** for this batch: it reads the
session's pending diff, which in the shared worktree is other passes' drafts
and this brief, and this is a landed-delta review. The code-altitude read was
done by hand against the OWASP catalogue:

- **Injection / command execution:** the delta adds no subprocess, shell, eval
  or path construction. Clean.
- **Insecure design — a guard that yields less:** the hunt the brief asks for.
  On the tree plane there is no input on which the new reader yields less than
  the old (tables above). On the hook plane there are inputs on which the
  guards see less than the tree plane does — **LN1**.
- **Resource consumption:** memory bound unchanged and still test-pinned; time
  improved. One enormous line costs the same as before.
- **Integrity failures / logging:** findings' excerpts, counts and exit codes
  are byte-identical old-to-new. A broken staged scan exits with the findings
  code, not the broken-scan code — LN5.
- **Sensitive data in tests:** the added tests use plain filler bytes; no
  credential-shaped fixture was added.
- **Privacy:** nothing personal in the delta.

### Findings

**LN1 — MAJOR — the pre-commit plane of `secretscan` and `leakscan` never scans
text that follows a CR, form feed, vertical tab, C0 separator, NEL or Unicode
line separator on an added line, nor any added line that begins with two plus
signs.** *Not introduced by this delta; found under lens 4.* The staged path
does not use the reader. It runs `git diff --cached` with text-mode decoding
(which turns every lone CR into LF) and then `str.splitlines()` (which also
splits on FF, VT, FS, GS, RS, NEL, U+2028 and U+2029). Every fragment after
such a split no longer starts with the diff's plus sign and is dropped. An
added line whose own text begins with two plus signs arrives as three and is
taken for a file header or skipped. Probe, same content on both planes, per
guard: a control line is found on both; the fixture after each of seven
separators is found by the tree plane (exit 1) and passes the staged plane
(exit 0, zero findings); the same for a line beginning with two plus signs,
with or without a following space — 9 of 9 bypasses in each of the two guards.
A whole file saved with CR-only line endings is the unadversarial case: the
hook scans its first line and nothing else. CI's tree plane does catch all of
these, but this repository is public and a push is the publication, so CI
reports the secret after it has left. `tools/README.md`'s standing residual
does not name this class and no test pins either behaviour. `conflictscan` has
the same parser but its markers are LF-line-anchored, so I found no miss
there. I cannot tell from unbarred material whether an earlier pass recorded
this; that is for reconcile.
*Counsel:* decode the diff as bytes with `errors="replace"` and split on LF
only, as the reader does, so both planes share one definition of a line; treat
`+++ ` as a header only before the first hunk header of a file; pin each
separator and the two-plus case with a staged-plane test in both guards.

**LN2 — MODERATE — the harvest stopped at three: six more guards carry the
same per-line re-copy.** `reviewscan`'s reader is the old loop verbatim;
`datescan`, `wrapscan`, `spellscan`, `stampscan` and `sizescan` re-slice the
remaining decoded chunk once per line inside their `feed` helper, which is the
same cost. Measured on 12.5 MB of 16-char lines: 16 to 18 s each in those six,
against 0.2 s in `conflictscan`, 0.5 s in `linkscan` and 0.6 s in `pathscan`.
Three of the six run enforced on both floor planes. The commit messages frame
the work as porting `linkscan`'s fix to the guards that had the loop, and
nothing a reader of `tools/README.md` or the unbarred tree can find records
the remaining six (`coldsweep` for the shape: 0 hits). It may be recorded
under the barred board sections; reconcile will say.

**LN3 — minor — the commit messages' "byte-identical for `--staged`" proves
nothing about the reader.** The staged path never calls
`_iter_numbered_lines`, so its output could not have changed. All three
messages cite it beside the tree-plane check as evidence of equivalence. The
tree-plane half of the claim I re-drove and it holds (human and JSON output
and exit code identical, all three guards, on the clone's tree).

**LN4 — minor — the equivalence test is thinner than its docstring.** It runs
eleven fixed inputs at one constant set (64 / 300 / 20) with no random inputs,
no separator other than LF and CRLF, no NUL and no BOM. With a 64-byte chunk
`pending` grows 256 → 320 and never equals the 300 window, so the mutant that
changes the window test from "at least" to "more than" survives the whole test
file in all three guards. The linearity check uses one 340 KB file, smaller
than one read chunk, so it proves the bound within a chunk and not across
chunks. The delta did not change the window test, and my differential covers
the gap for this delta; the pin is what is thin.

**LN5 — minor — a staged file that is not valid UTF-8 crashes all three guards
with a traceback and exit code 1.** Text-mode decoding of the diff raises
`UnicodeDecodeError`. It fails closed, which is right, but exit 1 is these
tools' "findings" code where 2 is "a broken scan", and the contributor sees a
stack trace and no remedy. Pre-existing; same root as LN1 and closed by the
same counsel.

**LN6 — note — three identical reader copies and three identical oracle
copies, with nothing that fails if one drifts.** The commit messages say the
merge decision is owned elsewhere; recorded so reconcile can check that it is.

**LN7 — note — recorded tree-plane behaviours, all identical old-to-new.** An
allow marker binds to the whole LF-line, so a marker before a CR, form feed or
U+2028 suppresses a hit after it that an editor may draw on a different line.
On an overlong line, `secretscan` and `leakscan` bind a marker only within its
own window (fails closed); `conflictscan` binds it across windows (by design,
its finding is decided on the first window). The docstrings still call the
pre-streaming reader's `splitlines` behaviour "identical"; for files holding
those separators the line numbers changed at that earlier change, not here.

**LN8 — note — "linear" overstates the before.** The old reader was already
linear in file size (4.4, 8.4, 17.8, 31.9 s for 12.5 to 100 MB): its per-line
cost was bounded by the fixed chunk. The commit bodies say "quadratic in lines
per chunk", which is accurate; the subject lines and test class name read as a
complexity-class change. What landed is a constant factor of about 50 to 90 in
the reader, and 1.6 to 11 times at tool level.

**LN9 — note — README wording on the binary skip.** "Skipped silently on the
first NUL byte" should read as a NUL within the first 8 KiB; a text file with
one early NUL is skipped whole by both planes (git also calls it binary), a
later NUL is not. Pre-existing and disclosed in kind, imprecise in extent.

### Re-run ledger

All in the scratch clone at `f1a667b` unless stated; exit codes read directly.

| Command | Result |
| --- | --- |
| `python3 tools/floor.py --plane hook --root . --tools tools` | exit 0 |
| `python3 tools/floor.py --plane ci --root .` | exit 0 |
| `python3 tools/{leakscan,secretscan,conflictscan}.py --selftest` | exit 0 × 3 |
| `python3 -m unittest test_leakscan` (in `tools/`) | 136 tests, OK |
| `python3 -m unittest test_secretscan` | 159 tests, OK |
| `python3 -m unittest test_conflictscan` | 41 tests, OK |
| `python3 -m unittest discover -s tools -p 'test_*.py'` (once) | 1,669 tests, OK, 388 s |
| reader differential (`diff_readers.py`) | 121,029 runs, 0 old≠new |
| same, spec model after control fix | 29,068 checked, 0 mismatches |
| tree differential, 933 tracked files × 3 guards | 0 mismatches |
| reader body hash across the three guards | identical |
| tool-level seeding (`seed_tools.py`), old CLI vs new CLI | 178 cells, 0 differ |
| old CLI vs new CLI on the clone's tree, human and `--json` | identical × 6 |
| staged-plane probe (`staged_probe.py`), 13 cases × 2 guards | 18 bypasses (LN1) |
| staged non-UTF-8 probe, 3 guards | exit 1, traceback × 3 (LN5) |
| mutation run (`mutate.py`), 9 mutants × 3 guards | 24 killed, 3 survive (LN4) |
| timing (`timing.py`), reader and CLI, old vs new | table in lens 2 |
| other guards' readers, 12.5 MB of 16-char lines | table in LN2 |
| `coldsweep` for the remaining old-shape readers | 0 hits |

Not re-run: the authors' `--staged` identity check on atelier's own index (the
staged path does not touch the reader — LN3), and their 50 MB `leakscan`
timing with the machine-local term list (deliberately not read).

### Follow-up checklist

- [ ] LN1 — one line definition for both planes of `secretscan` and
      `leakscan`; staged-plane tests for each separator and the two-plus line;
      name the class in the README residual until it is closed. Mike's call on
      urgency: it is a live gap on the commit path of a public repository.
- [ ] LN2 — port the offset walk to the six remaining readers, or record why
      not where a README reader will find it.
- [ ] LN3 — keep the vacuous `--staged` evidence out of any later record that
      quotes these commits.
- [ ] LN4 — add a random-input equivalence case, an exact-window case and a
      multi-chunk linearity case.
- [ ] LN5 — broken staged scan exits 2 with a remedy line, not a traceback.
- [ ] LN6 — confirm at reconcile that the copies' merge decision has an owner.
- [ ] LN7, LN8, LN9 — wording only; fold into the next edit of those surfaces.

### Reconcile — written 2026-10-04 (22:51 UTC), after phase 1 was committed (`2e46e4a`)

**What I opened at release, and only this:** the queue pointer (`160/660`); the
commissioning item `110/140` in full and the head of `110/130`; `115/220` in
full and `115/080` by grep; the intent record
`docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md` by grep
and two excerpts; and the four released verdicts by grep for each finding's
class, with the passages that hit read in context (BL2 in the bounded-guard
pass; the RC1 references in the allow-marker pass). I did not read those four
verdicts whole, so "not recorded" below means "no hit for the class in the
released surfaces", not a full reading. The sibling carried no author lens
paragraph. No phase-1 text was revised.

**The intent record** gives this work one line (`110/140`: the linear line
reader, listed as closed). The substance is in the commissioning item, which
asks for exactly three things: port `linkscan`'s reader into the three guards
with constants kept; output byte-identical on atelier's tree; the large private
repository re-timed. The first two I re-drove and they hold. The third I could
not and did not try: the house rules bar me from every other repository, so
the item's private-repo timings stand on the author's word alone.

**Seeded question 1 — is any one reader subtly different from the other two?**
No. Answered in phase 1 before the question was seen: the three bodies hash
identically once comments are stripped, and the three copies agreed with each
other on all 121,029 differential runs.

**Seeded question 2 — did the tests compare old against new, or only assert
new against expectations written beside it?** Old against new, genuinely: each
test file embeds the pre-change loop as an oracle and asserts list equality,
and the linearity check also requires the oracle to *fail* the bound, so it
cannot pass vacuously. Mutation confirms it bites (24 of 27 killed). The
weakness is breadth, not kind — LN4 stands as written.

**Per finding:**

- **LN1 (MAJOR) — new; stands.** No released surface records it. Its nearest
  neighbours, both on the same staged parser and both still open, are:
  **RC1** (2026-09-25, MAJOR, unruled), which I know only through the
  allow-marker verdict's summary of it — the staged parser accepts only one
  literal header shape — and **BL2** (2026-09-25, MODERATE), which records that
  the staged path buffers the whole diff and splits it twice. Neither names
  the separator class or the two-plus line: RC1 is about which *files* the
  parser recognises, BL2 about *memory*; LN1 is about which *text on a
  recognised added line* is thrown away. The allow-marker pass's reconcile
  notes the staged parser was left untouched "for part 3" of `115/080`, and
  that part is still owed and unclaimed. So the staged parser now carries two
  unruled MAJORs and a MODERATE from three separate passes, with one unbuilt
  vehicle named for all of them. That accumulation is the thing to put in
  front of the principal, in plain words: the commit-time secret check has a
  known-weak front door and the fix has no owner.
  The phase-1 statement that this predates the delta is confirmed: none of
  the three landing commits touches `staged_added_lines`.
- **LN2 (MODERATE) — new; stands, and sharpened.** `110/140`'s own text says
  "the three guards that still carry it", which my measurement falsifies: six
  more carry the same cost. `115/220` does record the five truncation readers
  as a separate mechanism with identical constants, but as a consolidation
  question, not as a speed defect, and `reviewscan`'s reader appears in
  neither. Nothing on the released board owns the remaining six.
- **LN3 (minor) — stands, and it travelled.** `110/140`'s close note repeats
  the claim as "byte-identical for all nine guard × mode runs". Three of those
  nine are the staged mode, which cannot exercise the reader. Six are evidence.
- **LN4 (minor) — stands.** See seeded question 2.
- **LN5 (minor) — new in this form.** The staged-plane-check pass has a
  sibling finding on a *different* tool's staged reader decoding by process
  locale (SG5); no released surface records the crash in these three guards.
- **LN6 (note) — answered.** The merge decision has an owner: `115/220`, open,
  framed as a decision awaiting the principal. The commit messages' pointer to
  it is accurate. Nothing further.
- **LN7 (note) — stands.** The secretscan-stream pass compared per-line against
  whole-file over the tree and found them identical; that tree holds no file
  with the unusual separators, so it could not have seen the line-number shift
  I describe. No conflict between the two results.
- **LN8 (note) — stands, and the board says it more strongly than the
  commits.** `110/140`'s title says the reader "costs quadratic time". Measured,
  the old reader's time was linear in file size. `110/140` also predicted the
  reader was "the likely first cause" of the two slow guards and then recorded
  honestly that the prediction was half right; my tool-level timings agree
  with that correction (regex time dominates in `secretscan` and `leakscan`).
- **LN9 (note) — stands.** The intent record notes, under a different item,
  that the staged plane never sees binaries even by name; consistent with what
  I recorded and already held for the principal there.

**Findings formed at reconcile:** none. Reconcile changed no severity.

**Overall, restated: PASS-WITH-FINDINGS — 1 MAJOR, 1 MODERATE, 3 minor,
4 notes.** The delta under review is correct and does what it was asked to do.
The MAJOR and the MODERATE are both about what sits *next to* it: a commit-time
gap in the secret and leak guards that this work did not create, and six
readers the same fix did not reach.

## Deferred material — folded in at reconcile

# Deferred material — linear-line-reader (open only after your findings are durably written)

Sibling of `docs/reviews/2026-10-04-2215-linear-line-reader-cold.md` under
REVIEW.md rule 1's split; held by the orchestrator outside the worktree. Folded
into the brief below the verdict when the verdict lands.

## Intent records

- `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md` — the
  authoring run's account. **Not opened** by the brief-writer.
- `docs/roadmap/110-*/140-the-line-reader-re-slices-per-line.md` and
  `110-*/130-*.md` — the commissioning items. **Not opened.**

## Prior verdicts and barred items on the same surfaces

- `docs/reviews/2026-09-25-0715-bounded-guard-layer-cold.md`,
  `docs/reviews/2026-09-25-0715-secretscan-stream-pathscan-roots-cold.md`,
  `docs/reviews/2026-10-03-0357-shared-allow-marker-grammar-cold.md`
- every item under `docs/roadmap/110-estate-duplication-exception-audit-mike/`
  and `docs/roadmap/115-guardrail-architecture-mike-commissioned/`

## The queue pointer's own lens hints — the author's seeded questions, verbatim

The pointer carries no lens paragraph — refs only.

## Brief-writer's seeded questions (a floor, never a fence)

Generate your own before reading these; a question you did not think of is a
prompt to re-read the surface, not an agenda.

1. Three commits, three files: is any one reader subtly different from the other
   two?
2. Did the workers' tests compare old against new output, or only assert the new
   output against expectations written alongside it?
