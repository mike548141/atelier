# Cold pass — the staged diff read by its structure

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-17 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/800-rule-4-cold-pass-queued-staged-diff-structural-reader.md`.
**Why it earns a review:** the three blocking guards that keep credentials, conflict markers
and personal data out of a commit — in this public repo and in every child, on the hook plane —
now read what a commit adds through one new parser, which also decides when a commit is refused
outright (exit 2). A reader that mis-attributes or drops a line is a silent false negative on
those guards; one that refuses a legitimate diff blocks every commit of that shape.

## Spawn provenance

- **Author of the work under review:** the 2026-10-16 queue run whose intent record is dated
  2026-10-16 07:03 UTC (an Opus orchestrator with dispatched workers; the pointer counts the
  worker's output as the run's authorship). The landing commit's trailer names a Sonnet model,
  the merge's an Opus model. Not opened here.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched on 2026-10-17 by the
  Mike-opened Fable review session working in the worktree `atelier-review-1017`, on Mike's
  2026-10-16 answer that a fresh Opus session writes these briefs. It authored none of the delta.
  It is **off-tier for review, disclosed: it forms no finding and writes no severity**, and it
  stops after this brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that passes rule 4's
  criterion. The reviewer repeats its own provenance in its verdict.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This brief-writer read: the
  four queue pointers it was assigned (160/780–810) and, as a shape example, the 160/500 pointer
  with its claim line; the delta lists of eight neighbouring pointers (160/700, 720, 730, 760,
  820, 830, 850, 860); the landing commit's and merge's subjects, `--stat`, diff **and message
  bodies** (the author's own account); the subjects and `--stat` of later commits on the same
  files; `REVIEW.md` rules 1–4; three user-local templates — the ask halves of the 2026-10-16
  expected-toolbox brief and of the 2026-10-16 **scanner-rule-gates brief, whose delta is two of
  this pass's files** (`leakscan.py`, `secretscan.py`), and the whole expected-toolbox sibling,
  seeded questions included (another pass's framing); HEAD greps of `tools/` for every staged-diff
  reader and `--staged` flag, and `tools/floor.py`'s hook and CI arguments; the commissioning
  item's head line; filename-level greps of `docs/reviews/` (no file there opened); and its
  harness-loaded memory index and instruction files (one-line notes, some about these guards'
  history). It did not open the intent record, `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md` or any file under `docs/reviews/`. Its orchestrator passed it an
  instruction set and no evaluative content about the delta; what the orchestrator read is its
  own to disclose in its claim. Everything evaluative is in the sibling.

## What the work is

Landing commit and merge (diff the commit; review the paths at HEAD, `8acfff1` or later):

- `39a74b9` (2026-10-16 08:11 UTC) — tools: read the staged diff by its structure, not by how a
  line looks (115/280); landed in merge `ef75803` (2026-10-16 08:15 UTC)

Delta paths: `tools/report.py` (`STAGED_DIFF_CMD`, `_HUNK_RX`, `DiffReadError`,
`STAGED_DIFF_FAILURES`, `parse_added_lines`, `staged_added`, the module docstring's new
sentence), `tools/secretscan.py`, `tools/conflictscan.py` and `tools/leakscan.py` (each one's
`staged_added_lines` and the `except` in `_main`), their tests `tools/test_report.py`,
`tools/test_secretscan.py`, `tools/test_conflictscan.py`, `tools/test_leakscan.py`, and
`tools/README.md` (the shared-reader paragraph).

**Later commits on the same files — not this delta; do not attribute them to it.**
`tools/report.py` is unchanged since the merge; confirm that.

- `f4afb7a` (2026-10-16 15:28 UTC) — tools: conflictscan and leakscan report a staged finding at
  its real file line (its own pass, 160/830); it changes how two of the three callers use the
  reader's line numbers
- `1c24781`, `72a68cc`, `e3e8a4f` (2026-10-16) — touch `tools/README.md` or `tools/test_report.py`
  outside this delta's hunks (160/810, 850, 840)

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests and live
behaviour. The lenses organise it; they do not bound it. Non-goals are the only narrowing and are
themselves reviewable.

Derive, from git's documented diff format and from `git diff` itself rather than from the
delta's tests (`EVIDENCE.md` § 15 is the reason), every shape `git diff --cached --unified=0`
can emit under `STAGED_DIFF_CMD`, and compare each with what `parse_added_lines` does. Pay
attention to:

- **Header shapes.** New, deleted, renamed, copied, mode-changed, type-changed, binary,
  submodule, symlink and empty files; quoted and non-ASCII paths; a path containing ` b/`, a
  newline or a tab; `/dev/null` on either side.
- **Hunk shapes.** Omitted counts, zero counts (`+0,0`, `-n,0`), `\ No newline at end of file`
  on either side, a hunk header carrying function context, the last hunk of the diff.
- **Bytes.** Undecodable bytes, a lone CR, CRLF files, form feed, NEL and the Unicode line
  separators inside a line, a NUL.
- **Repository state and configuration.** A diff taken mid-merge, mid-rebase or mid-cherry-pick
  with unmerged paths; user, repo and `.gitattributes` settings that change what `git diff`
  prints (prefixes, colour, external diff drivers, text conversion, rename and copy detection,
  `diff.relative`, word-diff, `core.quotePath`). Which does `STAGED_DIFF_CMD` pin, and which can
  still reach the parser?
- **The fail-closed path.** Every input that raises `DiffReadError`: which of them git can
  actually emit for a legitimate commit, and what the hook plane does on exit 2 (does it block,
  and does the message tell the committer what to do).
- **The three callers.** Each lost its own loop and filter, and `secretscan` its own fallback
  for a header without the `b/` prefix; check each caller's downstream use, path filters,
  ignore globs and line numbers at landing, and say what `f4afb7a` later changed.
- **Cost.** The reader now holds the whole staged diff as bytes and every added line in a list;
  measure it on a large staged change, against the house's bounded-guard rules.

**Non-goals:** the guards' detection rules themselves (their patterns, gates and term lists),
which other passes own. How the reader feeds them is in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. The central one:
   that a hunk's counts locate its last line whatever the line's text says. Others: that every
   line git writes outside a hunk is safe to ignore; that pinning prefixes in the command removes
   the configuration surface; that refusing an unknown shape is always the safe failure.
2. **Correctness & quality.** Read `parse_added_lines`, `staged_added` and all three callers
   whole; diff `39a74b9`. Build a shape table: shape, what git emits, what the reader yields or
   raises, and a reproducing fixture wherever they differ from a correct reading. Check whether
   the tests' fixtures were produced by real `git diff` runs or written by hand, and whether each
   posed-header test fails on `39a74b9^`.
3. **Completeness / harvest.** `tools/README.md`'s description of the reader and of the three
   guards' staged planes; `docs/method/GUARDS.md`'s claims about what the hook plane catches;
   every other guard with a staged plane (`board.py`, `harvestscan.py`, `publishscan.py`,
   `blockscan.py`, `floor.py`) and whether any still parses diff text by its look.
4. **Security & privacy** — mandatory. This lens is the subject: hunt the staged change whose
   added line a guard does not see, or sees under the wrong file. Build counter-examples from
   synthetic values only — never a real credential, term-list entry or personal detail — and
   never quote one in the verdict. Also check denial of service: a staged change that makes the
   reader refuse every later commit, or run unbounded. `/security-review` is discharged by
   grounds (a landed delta; the pending diff is not the work) — say so, and deliver the
   code-altitude read by hand against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest tools.test_report tools.test_secretscan tools.test_conflictscan
  tools.test_leakscan -v`; `python3 tools/secretscan.py --selftest`, `python3
  tools/conflictscan.py --selftest`, `python3 tools/leakscan.py --selftest`
- the shape table, driven: in a scratch repository under your scratchpad, stage each shape and
  run the three guards with `--staged` at `39a74b9^`, `39a74b9` and HEAD; compare stdout, stderr
  and exit code
- the posed-header hole, reproduced on `39a74b9^` and shown closed on `39a74b9`, with a synthetic
  value
- the hook plane end to end in that scratch repository (`.githooks/pre-commit` with this repo's
  tools), including one exit-2 case
- the floor on both planes at HEAD; the full Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only git is fine.
  Scratch repositories, staged fixtures and older checkouts go in a private clone under your
  session scratchpad, named by your prefix. Never open another `docs/reviews/2026-10-16-*` or
  `docs/reviews/2026-10-17-*` file — it is another pass's framing.
- One heavy process at a time on a shared machine: the full suite at most once, in the
  foreground; fixtures sized to finish in minutes, under `nice`. Never point a scanner at any
  other repo on the machine.
- `/security-review` reads the session's pending diff: discharge it by grounds for this landed
  delta, or keep the tree clean whenever you spawn it.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ English. Never quote
  a secret, placeholder token, email address or personal detail — this repo is PUBLIC; describe
  and locate instead. Counter-example lines in the verdict are described by shape, not pasted,
  where they would trip the guards on commit.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer, this brief's sibling
`docs/reviews/2026-10-17-0930-staged-diff-structure-cold.deferred.md`, the landing commit's and
merge's message bodies (read subject, stat and diff only), and the commissioning item `280` in
`docs/roadmap/115-guardrail-architecture-mike-commissioned/`.

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/800-rule-4-cold-pass-queued-staged-diff-structural-reader.md
--also-exclude docs/reviews/2026-10-17-0930-staged-diff-structure-cold.deferred.md
--also-exclude
docs/roadmap/115-guardrail-architecture-mike-commissioned/280-an-added-line-can-pose-as-a-diff-header-in-secretscan.md
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then append your
verdict below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier,
what you read), per-lens answers, the standing checklist V1–V7 each answered or discharged with
grounds, the shape table, findings with stable IDs (prefix `SX`: `SX1`, `SX2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger, and a follow-up checklist. Then STOP and commit phase 1 unrevised before opening
the sibling.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict: per-finding notes
against the seeded questions and the intent record, any finding formed at reconcile marked as
such, and the overall line restated. Never revise phase-1 text. Then fold the sibling in below
the reconcile and delete it.

Findings on self-authored doctrine are the principal's to decide (rule 3; a guard is doctrine by
function): record all, apply nothing; counsel per finding is welcome, labelled and kept beneath
it.

---

## Verdict — phase 1, written cold before the sibling was opened

**Written:** 2026-10-18T00:00Z (`date -u`). **Reviewer:** Fable 5.1, model id `claude-fable-5-1`.
**Overall:** PASS-WITH-FINDINGS — 0 MAJOR · 5 MODERATE · 2 minor · 3 note.

The reader itself is correct on every shape git 2.43.0 emitted under the pinned command: thirty-two
driven shapes, no misattribution, no dropped line, the posed-header hole closed end to end through
a real `git commit`. The findings sit around the reader: one new refusal of a legitimate diff that
the fail-closed path introduces, and four pre-existing holes in what the pinned command asks git
for, which this delta single-sourced and documented without closing.

### Provenance (rule 4, V7)

- **Spawn.** I was spawned by a Mike-opened Claude Code **cloud** session running `claude-fable-5-1`
  as orchestrator (it opened on `claude-opus-5`; Mike switched it to Fable before any claim or
  pass). That session authored none of the delta or this brief and was not started or instructed by
  their authors. It forms no finding and writes no severity; it holds the `.deferred.md` sibling
  outside the checkout at a path I was not given, commits this phase-1 file before releasing the
  sibling, and received one operational note from Mike's watching session (model, queue scope,
  container facts, merge instruction — no evaluative content about any delta). The claim line in
  the queue pointer discloses the same shape; I have not opened the pointer.
- **Tier.** Fable 5.1 (`claude-fable-5-1`), checked at selection; the stop clause did not fire.
- **Where I worked.** The shared checkout `/home/user/atelier`, branch
  `claude/review-work-briefs-adj6ad`, HEAD `0aff4d8` = `origin/main`; no worktree exists in this
  cloud container. I ran no writing git command there. Every probe, fixture repository, extracted
  tool tree and log lives under `/home/user/scratch/SX/`. Older tool trees came from
  `git archive 39a74b9^ tools` and `git archive 39a74b9 tools` run read-only in the checkout.
- **Container facts that bear.** One checkout; no sibling repos, no estate root, no `~/.claude/`, no
  `gh`, no GitHub API from the shell; python3 3.13, node v22, git 2.43.0; no git man pages (a
  minimised image: `/usr/share/man` holds none), so the diff format was derived by **driving the
  live binary**, not by reading its documentation. The checkout was **shallow** when I started
  (graft root `c824287`); the orchestrator unshallowed it mid-pass and I re-ran every history step
  (ledger). The hook plane's leakscan needs a user-local term list this container lacks, so the
  floor's hook plane reds on leakscan by design (board `115/350`); the CI plane is the honest plane
  here, and I ran both. Nothing the brief asked for needed another repo or a live platform read, so
  nothing is relayed.
- **What I read, in order.** `REVIEW.md` whole; this brief whole; `00-APEX.md` once; then the
  delta as `git diff 39a74b9^ 39a74b9` with subjects and `--stat` via `git show --stat --format=%s`
  (no message body opened); `tools/report.py` whole and the four tools' staged readers and `_main`
  staged branches at HEAD; the four test files' delta hunks and their post-merge hunks;
  `tools/floor.py` (registry, `_render`, exit handling, `Result.failed`); `.githooks/pre-commit`;
  `.github/workflows/ci.yml`; `tools/README.md` (reader paragraph and the post-merge diff);
  `CHANGELOG.md` lines 55–100; `docs/method/GUARDS.md` (opening and a grep for hook-plane claims);
  `docs/method/EVIDENCE.md` §15; `.atelier-floor.json`; `tools/test_precommit.py` lines 1–230;
  `tools/harvestscan.py`, `board.py`, `publishscan.py`, `blockscan.py` at their git reads; board
  items `115/300` and `115/310` whole (sibling items, not barred by the brief — disclosed because
  each mentions `report.staged_added`; both were read after my findings were formed from probes).
- **Exposure, disclosed.** `tools/coldsweep.py` ran once with the brief's three `--also-exclude`
  paths and without `--include-barred`; its hit list printed the `ROADMAP.md` index line for this
  pass's pointer (title and path only). While the checkout was shallow, `git log` on the graft root
  printed the subject line of `c824287`, a review commit of another pass (subject only; nothing
  opened). I opened no `docs/reviews/2026-10-1*` file but this one, no `drafts/`, `withdrawn/`,
  `ROADMAP-DONE.md`, `SESSIONS.md`, `docs/sessions/`, the pointer, the sibling, item `280`, or any
  commit message body.
- **`/security-review`.** Discharged by grounds: the work is a landed delta and the session's only
  pending change is this brief, which is exactly the SL2 shape the scanner must not read. The
  code-altitude read was done by hand against the OWASP catalogue (lens 4).

### The shape table

Every row was driven with real `git diff` under `STAGED_DIFF_CMD` (git 2.43.0) in a scratch
repository, parsed by HEAD's `parse_added_lines`, and compared with hand-derived truth. "guards"
is what `secretscan`/`conflictscan`/`leakscan --staged` did on the three tool trees (old =
`39a74b9^`, new = `39a74b9`, HEAD) where I planted a synthetic finding. Log:
`/home/user/scratch/SX/shapes.log`, `probes.py`, `hook_e2e.log`.

| Shape | git emits | reader | guards / note |
|---|---|---|---|
| new file | `--- /dev/null`, `+++ b/…`, `@@ -0,0 +1,N @@` | N lines, right | — |
| empty new file | `new file mode` + `index` only; no `+++`, no hunk | nothing (right) | name never scanned — SX5 |
| deleted file | nothing (`D` filtered) | nothing | — |
| pure rename | `similarity index 100%`, `rename from/to`; no `+++` | nothing (right) | new name never scanned — SX5 |
| rename + edit | `rename from/to`, `--- a/old`, `+++ b/new`, hunk | lines under new name | right |
| copy (`diff.renames=copies`) | `copy from/to`, `+++ b/copy`, hunk | lines under copy | right |
| mode only | `old mode`/`new mode`, no hunk | nothing | — |
| mode + content | mode lines, `index` without mode, hunk | right | — |
| typechange file→symlink | **nothing** (`T` filtered) | nothing | target unseen — SX3 |
| typechange symlink→file | **nothing** (`T` filtered) | nothing | **secret, marker, term unseen, all trees** — SX3 |
| new symlink | `new file mode 120000`, one `+` line, `\ No newline` | target as line 1 | leakscan finds a term in it |
| binary new file | `Binary files /dev/null and b/… differ` | nothing | name never scanned — SX5 |
| text under tracked `-diff` | `Binary files … differ` | nothing | **secret unseen, all trees** — SX4 |
| textconv driver | converted text | converted lines | transform reaches the guards — SX4 |
| external diff driver | ordinary diff (`--no-ext-diff` pins) | right | pinned |
| paths: tab, `"`, `\`, newline | `+++ "b/…"` C-quoted (quotePath=false still quotes these) | unquoted, right | — |
| path with ` b/` or a space | `+++ b/x b/y.md<TAB>` | right | trailing tab stripped |
| non-ASCII path | raw bytes (quotePath pinned) | right | — |
| non-UTF-8 path byte | raw byte | path with U+FFFD, lines right | ignore globs may not match; old tools crashed |
| omitted/zero counts | `@@ -2 +2 @@`, `@@ -6 +5,0 @@`, `@@ -10 +9,2 @@` | right | — |
| `\ No newline` either side | after the last `-`/`+` line | ignored (right) | — |
| function context on `@@` | `@@ -30,0 +31 @@ k29` | right | — |
| CRLF file / lone CR in line | `+one\r`; `+a\rb` | one CR stripped; lone CR kept | right |
| FF, VT, FS, NEL, U+2028 in line | one `+` line each | not split | right |
| NUL after 8 KiB | text diff, `+a\x00b` | right | git's binary heuristic not tripped |
| posed `+++ b/…`, `++ "b/…"`, `++ /dev/null`, posed `diff --git`, posed `@@` | all inside the hunk | all kept under the real path | **old: secretscan missed; new/HEAD: found** |
| `diff.interHunkContext=5` | one fused hunk with ` ` context lines | right (context counted) | — |
| fused hunk + `diff.suppressBlankEmpty` | an **empty** context line | **DiffReadError** | **exit 2, all three guards** — SX1 |
| `GIT_DIFF_OPTS=-u3` (env) | context lines **despite `--unified=0`** | right; with suppressBlankEmpty → DiffReadError | SX1 |
| `diff.noprefix`, `mnemonicPrefix` | `a/`, `b/` (pinned) | right | pinned |
| `color.ui/diff=always` | no colour (pinned) | right | pinned |
| `diff.algorithm/indentHeuristic/wordRegex` | ordinary | right | inert |
| `diff.relative=true` at root | full paths | right | inert at the hook's cwd — SX8 |
| submodule, `diff.submodule=short` | `+Subproject commit …` | one line | — |
| submodule, `diff.submodule=diff` | nested `diff --git a/sub/inner.md …` with context | right, full paths | a bonus — SX8 |
| mid-merge, unmerged path elsewhere | the resolved file's hunk only (`U` filtered) | right | `git commit` refuses before hooks anyway |
| hand-typed malformed bytes (the delta's six refusal fixtures) | n/a | DiffReadError | git emits none of these |

### Lens 1 — approach and assumptions

The load-bearing assumptions, named before any other reading, and attacked:

1. **A hunk's counts locate its last line whatever the text says.** Holds. xdiff writes the body
   from the counts, and every shape above fits them, including fused hunks and `GIT_DIFF_OPTS`
   context. The one break is not in the counts: `diff.suppressBlankEmpty` changes how a context line
   is *spelled* (empty instead of one space), so the invariant "every body line starts with `+`,
   `-`, ` ` or `\`" is a git-config-dependent claim, and the reader treats a legitimate spelling as
   a malformed diff (SX1). The assumption as stated in the comment block is right; the code encodes
   a stronger one.
2. **Every line git writes outside a hunk is safe to ignore.** Holds for correctness of the lines
   read. Its cost is that header-only files — empty, renamed without edit, binary, typechanged —
   never surface a path, and leakscan's path-name rule depends on the path surfacing (SX5).
3. **Pinning prefixes in the command removes the configuration surface.** Partly. Pinned and
   proven inert: `diff.noprefix`, `diff.mnemonicPrefix`, colour, `diff.external` and per-driver
   `command`, `core.quotePath`, `diff.context`. Still reaching the parser: a tracked `-diff`
   attribute (binary, hides content), `diff.<driver>.textconv` (transforms content — `--no-ext-diff`
   does not cover it), `diff.interHunkContext` and `diff.suppressBlankEmpty` (SX1), the
   `GIT_DIFF_OPTS` environment variable (which git documents as *overriding* a command-line
   `--unified`, and does), `diff.relative`, `diff.submodule`. The brief's question "which does
   `STAGED_DIFF_CMD` pin, and which can still reach the parser" is answered by the table.
4. **Refusing an unknown shape is always the safe failure.** Not when the shape is legitimate. A
   refusal on this plane is a blocking guard's exit 2 on every commit of that shape, and the hook's
   tail then prints the one line a stuck committer can act on: `git commit --no-verify`, which
   bypasses the *whole* floor, not the one guard. Fail-closed is right for a diff git could not
   have written; for a diff git did write under a user's configuration, the safe failure is to pin
   the configuration away (one `-c`) and, where refusal remains, to say what to check.
5. **The brief's account of what the work is.** Accurate. "Three blocking guards … now read what a
   commit adds through one new parser" is what the delta does; the pre-existing holes the brief
   lists as questions are real and are not this delta's regressions.

Is this the right problem, solved the right way? Yes on the problem: a `+++`-by-look test on a
blocking guard was a silent false negative, and reading by structure is the right fix. The
counts-based reader is small, right, and tested against real git. The way falls short in one
respect: the delta argued its diff filter in the docstring ("R is in the filter on purpose") and
pinned the command in one place, but did not ask what else the filter drops (`T`) or what else the
configuration can do to the text (SX3, SX4), which is exactly the audit a single-sourced command
invites.

### Lens 2 — correctness and quality

- **`parse_added_lines` is correct on every real shape driven**; its refusal branches are reachable
  only by the hand-typed fixtures and by SX1. The `+` branch's `path is not None` guard is an
  internal-consistency check (a `+` under `+++ /dev/null` cannot occur) and falls through to the
  refusal; fine.
- **The posed-header hole is closed, reproduced on `39a74b9^` and shown closed on `39a74b9` and
  HEAD**, with synthetic values: old secretscan `blocked: false, []`; new/HEAD `blocked: true,
  [(posed.md, 3)]`. Old leakscan found the planted line but **under the posed path** (`docs/…`, line
  1) — the attribution half of the defect — and old conflictscan missed its marker. Through a real
  `git commit` with the tracked hook: old tools let the posed commit be blocked only by leakscan's
  misattributed hit, HEAD blocks it as secretscan and leakscan on the real file.
- **The delta's tests discriminate.** HEAD's four posed-header test classes against the `39a74b9^`
  tools: 8 failures, 22 errors (the report tests error on the missing functions); on HEAD, 442 tests
  in the four modules pass. Fixtures: `ParseAddedLinesTest` drives real `git diff` for every shape
  test; the two refusal tests are hand-typed bytes, which is right (git emits none of them) and is
  stated in their names — the class docstring's "Fixtures are REAL `git diff` output" is true of the
  shape tests and should not be read onto the refusal tests. The EVIDENCE §15 bar — an authority
  outside the code — is met by driving git, which is the external system the belief is about.
- **An improvement the delta did not claim:** the old reader used `text=True` (strict decode), so
  a non-UTF-8 byte in staged content raised `UnicodeDecodeError` — a traceback and exit 1, a block
  by crash with nothing actionable. HEAD decodes with `replace` and scans the line.
- **Later commits are not this delta's.** `tools/report.py` blob `d02c417` is identical at
  `ef75803` and HEAD (confirmed twice: by blob id while shallow, by `git log ef75803..HEAD` after
  the unshallow, which is empty). `f4afb7a` changed conflictscan and leakscan from
  `dict[str, str]` (lines joined, line numbers discarded via `_lineno`) to
  `dict[str, list[tuple[int, str]]]` fed to `scan_lines`, so both now report the reader's real line
  number; HEAD's blobs for both files equal `f4afb7a`'s output (`2757a92`, `49d7b9c`), so nothing
  else touched them. At landing, the two callers discarded the line number the reader yields and
  numbered findings by position among added lines — a defect `115/300` found the same day; not this
  delta's regression (the old code did the same), but the delta plumbed a correct number through
  and two of three callers dropped it on the floor.
- **CHANGELOG's "staged output is byte-identical on a realistic change set"** re-run: old vs new
  tools on a four-file, multi-hunk fixture (a secret in hunk 1, a marker in hunk 2, a term in hunk
  3, a spaced name, a rename): human and `--json` output byte-identical for all three guards.
- **Downstream use at HEAD.** Path filters: prefix match on repo-relative paths plus exact match;
  absolute paths refused (unchanged). Ignore globs: applied per path after the reader (unchanged).
  Line numbers: secretscan always used them; conflictscan and leakscan since `f4afb7a`. leakscan
  also scans each path *name* — only for paths that have added lines (SX5).
- **Quality notes.** secretscan's `staged_added_lines` docstring still narrates the in-function hunk
  tracking the delta removed; the R-filter rationale and the 115/280 story are each now stated in
  four places (SX7).

### Lens 3 — completeness and harvest

- `tools/README.md`'s reader paragraph is accurate and matches the code. `CHANGELOG.md`'s entry
  matches (and its byte-identity claim re-ran clean). `docs/method/GUARDS.md` makes **no** claim
  about what the hook plane catches — it governs findings after they fire — so there is nothing
  there to reconcile; the only prose claims about staged cover live in the tools' own docstrings
  and `tools/README.md`.
- **No other guard parses diff text by its look**: `harvestscan` reads `--numstat` counts only;
  `publishscan` reads `--name-only -z`; `board` and `blockscan` read blobs from the index; `floor`
  reads none. Board item `115/300`'s "No other guard consumes the reader" also holds (grep).
- What the delta should have covered and did not: the filter's `T` (SX3) and the attribute/textconv
  surface (SX4), both of which the brief's own derivation list reaches in a few minutes of driving
  git; the header-only path problem the structural reader is now in a position to solve (SX5); the
  cost question (SX6), which the module's own neighbours (020/370, 020/380) make a standing rule.
- The hook copy `tools/pre-commit.sample` equals `.githooks/pre-commit` (diff clean).

### Lens 4 — security and privacy

The subject of this pass. Hunted: the staged change whose added line a guard does not see, or sees
under the wrong file. Found three ways to *not see* (all pre-existing, all reaching the public
remote through a real `git commit` in my scratch child, all caught afterwards by the CI plane's
whole-tree secretscan but **not** by any plane for a leakscan term, whose list exists only on the
hook): a typechange (SX3), a tracked `-diff` attribute (SX4), and the path name of a header-only
file (SX5). Found one way to *refuse* a legitimate commit on all three guards (SX1). Attribution to
the wrong file: none on any real shape — the posed-header class is closed. Denial of service: a
staged change cannot make the reader refuse *later* commits (no state persists), but the reader
holds the whole diff and every line in memory, ~6× the diff's size per guard, three guards in
sequence (SX6). Code altitude against the OWASP catalogue, for this work's class (a local CLI
parsing a trusted tool's output): no shell (argv list), no file opened by a parsed path (paths are
dict keys and glob inputs only — no traversal surface), anchored regex (no catastrophic
backtracking), decode with `replace` (no exception path from bytes), no network. Two notes: the
refusal message echoes up to 60 characters of a staged line to stderr (SX9); a path containing a
newline is printed raw in a finding line (cosmetic, pre-existing). Privacy at design altitude: the
reader itself adds no collection; the `-diff` hole is a privacy defect of the plane because
leakscan's full cover is hook-only.

### Standing checklist V1–V7

- **V1 — no claim stronger than its evidence.** Three claims exceeded theirs: leakscan's call-site
  comment that "a leak in a NEW file's name reaches the remote by the same commit as one in its
  body" is false for an empty, renamed or binary new file (SX5); the implicit claim that pinning
  the command removes the configuration surface (SX1, SX4); secretscan's stale docstring (SX7).
  Every other claim I met re-ran true.
- **V2 — re-run every live-proven claim.** Done; ledger below. All re-ran true except as V1 says.
- **V3 — changed rule swept to every mirror site.** README, CHANGELOG, the three callers' comments
  and the hook copy agree; `docs/method/` has no mirror of the staged-plane rule. Discharged.
- **V4 — one fact, one home.** The R-filter rationale and the 115/280 explanation each live in four
  unstamped copies (SX7, minor).
- **V5 — no internal contradiction.** secretscan's docstring describes hunk tracking that now lives
  in `report` (SX7). Otherwise the work agrees with itself and its siblings.
- **V6 — security and privacy on every review.** Lens 4 above; scanner discharged by grounds.
- **V7 — rule-4 provenance in brief and verdict.** The brief states it; repeated above.

### Findings

Severity: MAJOR = a silent false negative or a refusal this delta *introduces* on a blocking guard,
or a wrong load-bearing assumption; MODERATE = a real hole or refusal on the guards' plane that the
delta single-sourced or could have closed but did not introduce; minor = quality; note = recorded
for the record. Counsel is the reviewer's and is labelled; rule 3 applies — record all, apply
nothing.

**SX1 — MODERATE — The fail-closed path refuses a legitimate diff under one user setting, on all
three guards.** With `diff.suppressBlankEmpty=true` and any source of context lines — the config
`diff.interHunkContext=N` (fuses hunks closer than N lines even at `--unified=0`), or the
environment variable `GIT_DIFF_OPTS=-uN`, which git applies *over* the command line's
`--unified=0` (driven: a `-u3` env produced six-line hunks against the pinned `-U0`) — an empty
context line reaches the reader, `kind == ""` matches no branch, and `DiffReadError` fires. Driven
through the floor's hook plane on a two-edit change around a blank line: `secretscan`, `leakscan`
and `conflictscan` each print `git diff failed: diff line 8 does not fit its hunk's counts: ''`
and exit 2; the floor prints `BLOCKED by: secretscan, leakscan, conflictscan`, adds for secretscan
`🔴 declares an advisory count and printed none — the count contract has drifted` (a misdiagnosis
of the exit-2), then the findings advice and the `--no-verify` bypass. Nothing names the setting.
The same change with the two settings removed landed cleanly; the same change on the `39a74b9^`
tools passed (the old reader ignored lines it did not understand). Why MODERATE and not MAJOR: two
uncommon knobs must coincide, and `-U0` output is otherwise free of context. Why not minor: when
they coincide every fused-hunk commit is refused by three blocking guards with a message that
steers to a floor-wide bypass. *Counsel:* add `-c diff.suppressBlankEmpty=false` to
`STAGED_DIFF_CMD` — verified to close both routes with no parser change (the reader already counts
` ` lines); optionally `-c diff.interHunkContext=0` and drop `GIT_DIFF_OPTS` from the child's
environment so the plane is `-U0` as designed; add a regression test that sets the two configs;
and see SX2 for the message.

**SX2 — minor — The exit-2 message carries no remedy, and the floor misreads it.** `git_diff_failed`
prints the exception text; the hook's tail speaks of findings that do not exist and offers the
bypass; the board line for secretscan blames a drifted count contract. This is the EP9 class the
hook's own comments name (the only actionable line is the bypass). *Counsel:* give `DiffReadError`
a committer-facing sentence (what the reader expected, which settings and environment variables
alter `git diff` output, how to see the raw diff), and have the floor recognise `rc == 2` before
reading an advisory count.

**SX3 — MODERATE — `--diff-filter=ACMR` drops a typechange, so a file that replaces a symlink is
never scanned.** A symlink replaced by a regular file holding a secret, a conflict opener and a
term: the pinned command emits **nothing** (status `T` is filtered before git splits the pair), all
three guards exit 0 on the old, new and HEAD trees, and a real `git commit` through the tracked hook
**landed** it; the CI plane's whole-tree secretscan found it afterwards, but a leakscan term has no
plane left to catch it on. The reverse (file → symlink) hides the new target the same way. Pre-
existing filter; the delta single-sourced it and argued `R` in the docstring without `T`.
*Counsel:* `--diff-filter=ACMRT` — verified: git then emits a `deleted file mode` block
(`+++ /dev/null`, `-` lines) and a `new file mode` block, and the reader yields the new file's
lines correctly with no change.

**SX4 — MODERATE — A tracked `-diff` attribute, or a textconv driver, decides what the guards see.**
`.gitattributes` with `*.env -diff` staged in the same commit as `x.env` holding a secret: git
prints `Binary files … differ`, the reader (rightly) yields nothing, all three guards exit 0 on all
three trees, and a real `git commit` **landed** it (CI whole-tree caught secretscan's half later;
leakscan terms never). `diff.<driver>.textconv` (user or repo-local config, not stageable)
transforms the content the reader sees — `--no-ext-diff` does not disable textconv (driven: an
upper-casing driver reached the parser). Pre-existing; this is the surface the delta's "pins the
diff prefixes" framing left unexamined. *Counsel:* `--text` forces `-diff` files back to text
(verified: the secret became visible) at the cost of genuinely binary files arriving as text lines —
pair it with the tree plane's NUL-in-first-8-KiB test on the yielded text, or accept the cost;
`--no-textconv` restores raw content (verified) but also removes the *extra* cover a textconv for
PDF or DOCX would give, so this half is a choice to record rather than an obvious fix.

**SX5 — MODERATE — leakscan's path-name cover on the hook plane is false for header-only files.** An
empty new file, a pure rename, or a new binary whose **name** carries a term produces no added
line, so the path never enters `staged_added_lines()` and `scan_path_name` never sees it; all three
trees exit 0. The call-site comment ("G2 on the hot path too: a leak in a NEW file's name reaches
the remote by the same commit as one in its body") claims cover the plane does not have (V1). A
photograph or export named after a person is exactly leakscan's case, and its term list exists
only on this plane. Pre-existing (the old code filtered `if lines` and saw no `+++` for these
shapes); the structural reader already parses the `diff --git`, `rename to` and `Binary files`
headers that name these paths. *Counsel:* have `staged_added` (or a sibling) also return the set
of paths the diff touches — from the headers it already reads, or from
`git diff --cached --name-only -z --diff-filter=ACMRT` — and have leakscan scan every path name;
correct the comment either way.

**SX6 — MODERATE — The staged plane is unbounded, and the delta kept it so.** On a 27.5 MB staged
file (400 000 lines): `git diff` alone peaks at 78 MB; each guard's `--staged` run peaks at
172 MB on HEAD (old: 193/155/156 MB for secretscan/conflictscan/leakscan) against ~20 MB for the
same content on the whole-tree plane, which the house bounded by ruling (020/370, 020/380: "it
should not matter how much it scans"). `parse_added_lines` is a generator, but `staged_added`
captures the whole diff with `subprocess.run(capture_output=True)` and materialises `list(...)`,
and each caller then builds a dict of every line; no line-length cap applies (the tree plane caps
a line at ~4 MB). Three guards run in sequence, so the peak is per guard, not summed. Not a
regression (−20 MB, +16 MB, +16 MB), but the reader was the one place to make this plane stream.
*Counsel:* `Popen` the diff and consume the generator file by file; cap a line as
`_iter_numbered_lines` does; measure with the existing `memprobe` harness as `test_conflictscan.
BoundedMemory` does for the tree plane.

**SX7 — minor — Stale and quadruplicated prose (V4, V5).** secretscan's `staged_added_lines`
docstring still says "Each `@@ … @@` hunk header now resets the real new-file line counter, and
every added or context line advances it" — true in effect, but describing code the delta moved to
`report`. The R-filter rationale appears in `report.staged_added` and all three callers; the 115/280
explanation in `report`'s comment block and all three callers; none is stamped as a copy. *Counsel:*
one home each (the reader), pointers from the callers.

**SX8 — note — Configuration observed, no defect.** `diff.relative=true` is inert at the hook (git
runs hooks from the work-tree root), but a hand run of `--staged` from a subdirectory would be
narrowed silently; `--no-relative` pins it for free. `diff.submodule=diff` makes the guards scan
submodule content under full paths — a bonus, recorded so nobody "fixes" it. A non-UTF-8 byte in a
path decodes to U+FFFD, so an ignore glob for that exact name will not match; content is scanned.
Also observed: `git -c` beats repo and global config, so every pin above is robust; only
`GIT_DIFF_OPTS` beats the command line, and only the environment can scrub it.

**SX9 — note — The refusal echoes staged content.** `DiffReadError` messages carry `line[:60]!r`.
On the hook that is the committer's terminal; if floor output is ever captured (CI logs,
`floorfleet`) a refused line's first 60 characters go with it. Advisory.

**SX10 — note — Test-source observation.** `test_line_separators_inside_a_line_do_not_split_it`
carries a literal U+2028 in its source (so the test does cover the Unicode separator the docstring
names; `str.splitlines()` on the file cuts that line, which is how I noticed). Robust as a test,
fragile to editors; the `" "` escape would be safer.

### Re-run ledger

| Claim or step | How | Result |
|---|---|---|
| Model/tier | runtime identity | Fable 5.1, `claude-fable-5-1` |
| `report.py` unchanged since the merge | blob ids `ef75803:` vs `HEAD:` (while shallow); `git log ef75803..HEAD -- tools/report.py` (after unshallow) | identical `d02c417`; empty log |
| Delta commits reachable | `merge-base --is-ancestor` ×8 | all NOT ancestors while shallow (graft `c824287`); **all ancestors after the orchestrator's unshallow** |
| Later commits on the delta's files | `git log ef75803..HEAD -- <9 paths>` after unshallow | exactly `f4afb7a`, `1c24781`, `72a68cc`, `e3e8a4f` and their merges, as the brief says |
| HEAD callers = `f4afb7a`'s output | blob ids | equal (`2757a92`, `49d7b9c`) |
| Four unit modules | `python3 -m unittest tools.test_report tools.test_secretscan tools.test_conflictscan tools.test_leakscan` | 442 tests OK |
| Three `--selftest`s | by path | OK ×3 |
| Posed-header tests fail on `39a74b9^` | HEAD's test files against `git archive 39a74b9^ tools` | 8 failures, 22 errors |
| Posed hole: open on old, closed on new/HEAD | `--staged --json` on a synthetic fixture | old secretscan not blocked; new/HEAD blocked at the real line; old leakscan blamed the posed path |
| Shape table, three trees | `shapes.py` (32 shapes) + `probes.py` | table above |
| Hook plane end to end | tracked hook via `core.hooksPath`, real commits | clean lands; secret blocked; posed blocked on HEAD; exit-2 case blocked by all three; typechange and `-diff` cases **landed** |
| Exit-2 committer view | floor hook plane, fused-hunk fixture | three `git diff failed` lines, a false "count contract has drifted" line, findings advice, bypass |
| Floor, CI plane at HEAD | `python3 tools/floor.py --plane ci --root .` | rc 0 (secretscan 23 advisory; leakscan cover-not-guaranteed) |
| Floor, hook plane at HEAD | `--plane hook --root . --tools tools`, no term list | rc 1, `BLOCKED by: leakscan` only — the expected red (`115/350`) |
| Full Python suite, once | `unittest discover -s tools -p 'test_*.py'`, foreground, `nice` | 1916 tests OK in 174 s |
| Instruments suite, once | `node --test instruments/*.test.js` | 447 tests, 0 fail |
| CHANGELOG byte-identity | old vs new, realistic fixture, human + JSON | identical, all three guards |
| Cost | 27.5 MB staged, `ru_maxrss` per run | table in SX6; log `cost.log` |
| Old reader on non-UTF-8 bytes | old secretscan `--staged` | `UnicodeDecodeError` traceback, exit 1; HEAD exit 0 |
| Remedies | `probes.py` | `ACMRT` parses; `--text` reveals; `--no-textconv` restores; one `-c` closes SX1 both routes |
| Git documentation on this machine | `find /usr/share/man …` | none; derived from git 2.43.0 live |

### Follow-up checklist (for the principal to decide; nothing applied)

- [ ] SX1/SX2 — pin `diff.suppressBlankEmpty=false` (and consider `interHunkContext=0`, scrub
      `GIT_DIFF_OPTS`); give the refusal a remedy; teach the floor board about `rc == 2`.
- [ ] SX3 — `--diff-filter=ACMRT`, with a typechange test on both directions.
- [ ] SX4 — decide `--text` (and the binary test on yielded lines) and whether textconv is cover or
      a hole; record the decision in the reader's comment block.
- [ ] SX5 — surface header-only paths to leakscan's name scan; correct the call-site claim.
- [ ] SX6 — stream the staged diff; bound per line; a `BoundedMemory` test for the staged plane.
- [ ] SX7 — one home for the filter and 115/280 rationale; refresh secretscan's docstring.
- [ ] SX8–SX10 — record; no action required unless the principal wants `--no-relative` for free.

### Reconcile

**Written:** 2026-10-18T00:30Z, after phase 1 was committed as `5f3e3b8` and the orchestrator
released the sibling. Opened at this step, in this order: the sibling; the queue pointer
(`160/800`); the commissioning item `115/280`; the intent record
`docs/sessions/2026-10-16-0703-queue-run-after-the-sizescan-ruling.md`; the landing and merge
message bodies; and, of the prior verdicts the sibling names, the three that have *run*
(`2026-09-25-0715-staged-plane-check-cold`, `2026-09-25-0715-secretscan-stream-pathscan-roots-cold`,
`2026-10-04-2215-linear-line-reader-cold`), read by grep for the surfaces my findings touch and
then at the passages found. The three `2026-10-16-1551-*` files the sibling lists are **unrun
briefs of live sibling passes**; I left them closed — they hold no verdict to reconcile with, and
their asks are another pass's framing. Phase-1 text above is unrevised.

**Against the seeded questions.**

1. *textconv not pinned* → **SX4** found it independently and drove it: an upper-casing driver
   reached the parser under `--no-ext-diff`. The sibling's sharper framing — a hostile tracked
   `.gitattributes` plus local config — is right that the attribute alone cannot name a textconv
   command (that lives in config), but the attribute alone *can* hide a file outright with
   `-diff`, which is the stageable half and the one I rate.
2. *`diff.relative`* → **SX8**: inert at the hook because git runs hooks from the work-tree root
   (driven at the root: both files present); a hand run from a subdirectory would narrow silently;
   `--no-relative` is free.
3. *`T` filtered* → **SX3**, driven in both directions, through a real commit, with the remedy
   verified. The sibling's parenthesis ("the filter predates this delta; the reader carries it")
   is the severity reasoning I used.
4. *lossy path decode* → **SX8**: the U+FFFD path is a dict key and a glob input only; no caller
   passes a parsed path back to git (checked all three `_main`s), so the only effect is an ignore
   glob for that exact name failing to match while the content is still scanned.
5. *legitimate shapes refused* → the three the sibling names are all fine (unmerged paths are
   filtered and `git commit` refuses before hooks anyway; a submodule prints one `Subproject` line
   or, under `diff.submodule=diff`, a well-formed nested diff; function context on `@@` is matched
   by the anchored prefix). The refusal that *is* reachable is **SX1**, which the seeded list did
   not reach: a presentation setting, not a repository state.
6. *callers feeding non-`STAGED_DIFF_CMD` text* → none in production; the only other feeders are
   `test_report.raw_diff` (the same command minus the filter, same prefixes) and the six
   hand-typed refusal fixtures. Discharged.
7. *the equivalence claim's change set* → the record does not list it (the commit body says "a
   realistic change set"; the item says "a realistic scratch change set"); I re-ran my own
   (four files, five shapes, three planted findings): byte-identical. It does not and cannot cover
   the brief's whole shape list, and for the shapes in SX3–SX5 "identical" means identically
   absent on both sides — a true statement that is not cover.

**Against the intent record and the commissioning item.** The record's `115/280` entry matches
what I found: the shared reader had the hole; the orchestrator reproduced old-clean/new-blocked
(so did I, on all three guards); `115/300` was filed from the same probe (I describe `f4afb7a`'s
effect above). Its **memory note** — "the reader holds the staged diff in memory, as the old code
did, so this is no regression against the bounded-memory rule. Streaming that plane would be a
separate item" — agrees with SX6's measurement and reasoning on both counts; SX6 stands at
MODERATE because the plane, not the delta, is what a committer meets. The item's "1,859 Python and
411 Node tests pass" has become 1916 and 447 at HEAD, all passing. The commissioning item's ask
("check whether the shared reader has the same hole inside a hunk") was answered; nothing in it
asked about the filter or the attribute surface, so SX3–SX5 are harvest, not scope-miss.

**Against the commit bodies.** Both are accurate accounts. The landing body's "the command pins
`--src-prefix=a/ --dst-prefix=b/ --no-ext-diff` so a user's `diff.noprefix` / `mnemonicPrefix`
cannot change the header shape" is true and is exactly the breadth it claims; what it does not
claim (and SX4/SX1 cover) is the rest of the configuration surface. Its test list ("multi-file,
rename, quoted and non-ASCII paths, new, deleted, binary, mode change, no newline, CRLF") is
what `ParseAddedLinesTest` drives — confirmed, and the posed-header tests fail on the old code as
it says.

**Against the prior verdicts.** The 2026-10-04 linear-line-reader pass's **LN1 (MAJOR)** — the
staged plane never scanned lines after a separator because `splitlines` split on CR, FF, NEL and
the Unicode separators — carried the counsel "decode the diff as bytes … split on LF only … treat
`+++ ` as a header only before the first hunk header of a file; pin each separator … with a
staged-plane test". This delta is that counsel built, and my shape table re-drives every
separator LN1 named: all kept on one line. Its **LN5 (minor)** — a staged file that is not valid
UTF-8 crashes all three guards — is the "improvement the delta did not claim" in lens 2: closed
here by `errors="replace"`. Neither closure is recorded against LN1/LN5 in the records I opened;
that bookkeeping is the principal's and the applier's, noted for the follow-ups. The 2026-09-25
passes concern the whole-tree bound (26.3 MB measured there) and the board/harvest planes; nothing
in them contradicts SX6, which measures the *staged* plane the bound never covered.

**Against the sibling's overlap list.** `160/760` owns `diff_header_path`/`unquote_c`: I drove
every quoted shape through them and found no defect, so nothing here reaches that pass. `160/830`
(`f4afb7a`): described in lens 2; HEAD's two callers are byte-for-byte its output. `160/720`/`730`
share files; no finding of mine is about the gates or the report contract.

**Finding formed at reconcile.**

**SX11 — note (formed at reconcile) — The unbounded staged plane was known and not filed.** The
intent record says "streaming that plane would be a separate item", and the run's close lists what
it filed (`115/290`, `115/300`) — no such item. A lesson that changes nothing was not harvested
(`00-APEX.md`, *Harvest, then encode*). SX6 is where it should land; this note records that the
author saw it first.

**Overall line, restated:** PASS-WITH-FINDINGS — 0 MAJOR · 5 MODERATE · 2 minor · 4 note (SX11
added at reconcile). Headline unchanged: SX1.

## Deferred material — folded in at the verdict

*The sibling `2026-10-17-0930-staged-diff-structure-cold.deferred.md`, verbatim (its own H1 kept),
folded here at phase 2 and deleted from the tree, per `REVIEW.md` rule 1 (split for the duration,
merged at rest).*

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
