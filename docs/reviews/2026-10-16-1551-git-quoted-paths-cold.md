# Cold pass — guards read git-quoted paths

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/760-rule-4-cold-pass-queued-quoted-paths.md`.
**Why it earns a review:** git rewrites some file names before printing them, and
a guard that parses the rewritten form either misses the file or reads the wrong
name. This delta changed how four blocking guards and two board tools read
paths from git, on the staged plane every commit passes through; a residual miss
is a commit no guard read.

## Spawn provenance

- **Author of the work under review:** the queue run whose intent record is dated
  2026-10-05 11:20 UTC (an Opus orchestrator with dispatched workers; the pointer
  counts the workers' output as the run's authorship). Not opened here.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched by a
  Mike-opened Opus queue-run session (id prefix `abe96d8d`) on 2026-10-16 UTC, on
  Mike's answer that day that a fresh Opus session writes these briefs. It
  authored none of the delta. It is **off-tier for review, disclosed: it forms no
  finding and writes no severity**, and it stops after this brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that
  passes rule 4's criterion. The reviewer repeats its own provenance in its
  verdict.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This
  brief-writer read: the queue pointer in full; both landing commits' subjects,
  `--stat`, the `report.py` diff and publishscan's plane hunk, **and both message
  bodies** (the author's own account); the subjects and `--stat` of later commits
  on the same files; `REVIEW.md` rules 1–4, the four lenses, the checklist and the
  lifecycle; the ask halves of two 2026-10-04 briefs as templates; `docs/reviews/`
  filenames and filename-level greps (no prior verdict opened); the names, not
  contents, of the commissioning board items — including a later item whose
  filename describes a defect on this surface; and its harness-loaded memory
  index. Its orchestrator read the `docs/SESSIONS.md` index tail through
  2026-10-16 (including the authoring run's one-paragraph summary) and the
  2026-10-16 session record's close section, and passed on no evaluative content
  beyond the pointer list and a one-line note naming a later shared staged-diff
  reader and staged real line numbers. Everything evaluative is in the sibling.

## What the work is

Landing commits (diff these; review the paths at HEAD):

- `c1cef10` (2026-10-05 18:56 UTC) — publishscan: read the tip and staged planes
  NUL-delimited (260/120); landed in merge `e71d40c` (2026-10-05 18:58 UTC)
- `4dfaf8d` (2026-10-05 21:52 UTC) — tools: read git's quoted paths correctly in
  the staged-plane guards (115/260); landed in merge `68e9baf` (2026-10-05
  21:53 UTC)

Delta paths: `tools/report.py` (`unquote_c`, `diff_header_path`, `nul_paths`),
`tools/conflictscan.py`, `tools/leakscan.py`, `tools/secretscan.py`,
`tools/board.py`, `tools/harvestscan.py`, `tools/publishscan.py`, their tests
(`test_report.py`, `test_conflictscan.py`, `test_leakscan.py`,
`test_secretscan.py`, `test_board.py`, `test_harvestscan.py`,
`test_publishscan.py`) and `tools/README.md`.

**Later commits on the same surfaces — not this delta; do not attribute them to
it.** The staged-diff path in three of these guards was rewritten after landing,
so the delta's header reader may no longer be the code that runs. Review the
delta's own claims at the landing commits and at HEAD, and say which a finding
rests on:

- `39a74b9` (2026-10-16) — read the staged diff by its structure, not by how a
  line looks (115/280): a shared staged-diff reader in `report.py`
  (`parse_added_lines`, `staged_added`) now used by conflictscan, leakscan and
  secretscan
- `f4afb7a` (2026-10-16) — conflictscan and leakscan report a staged finding at
  its real file line
- `f9ccba8`, `72a68cc`, `1c24781`, `e3e8a4f` (2026-10-16) — edit pins in
  `test_report.py` for sizescan, indexscan and licenscan, not the path readers

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests
and live behaviour. The lenses organise it; they do not bound it. Non-goals are the
only narrowing and are themselves reviewable.

For every place in the six tools where a path comes from git, at HEAD: which git
command, with `-z` or not, with `-c core.quotePath=false` or not, through which
reader. Then drive file names through each plane in a scratch repo: non-ASCII
(composed and decomposed forms), a space, a trailing space, a tab, a newline, a
double quote, a backslash, a leading dash, a name that is only digits, bytes that
are not UTF-8, a name beginning `b/` or containing ` b/`, and a file whose added
content line begins `++ b/` (it prints as `+++ b/…` in a diff). Repeat under
repository and user config the guards do not pin: `diff.noprefix`,
`diff.mnemonicPrefix`, `diff.srcPrefix`/`dstPrefix`, `color.diff=always`,
`diff.external`, `core.precomposeUnicode`. For each: is the file read, under its
real name, and does a planted marker, leak or secret in it get reported? Whether
`unquote_c`'s UTF-8 `replace` decoding and `nul_paths`' surrogate-escape decoding
give the same string for the same non-UTF-8 name, and whether either can then be
opened. Whether publishscan's own NUL reader and `report.nul_paths` are two
readers of one thing. **Non-goal:** the choice to read the staged header with
`core.quotePath=false` rather than a `-z` path list joined to the diff.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Among them: that git's quoting rules are exactly the set `unquote_c` undoes;
   that the default `b/` prefix is the only one a guard will meet; that a
   trailing TAB on a header always and only marks a name with a space.
2. **Correctness & quality.** Read the three helpers, each call site, and the new
   tests whole; diff both commits. Build the per-plane, per-name table above at
   the landing merges and at HEAD. Check that the tests fail on the pre-change
   code as the commit bodies say, and that the fixtures pin the git config they
   depend on.
3. **Completeness / harvest.** Every other place in `tools/` and `instruments/`
   that reads paths from git output without `-z` (`grep -n "ls-files\|diff
   --cached\|ls-tree\|--name-only" tools/*.py instruments/*`); `tools/filewalk.py`;
   `tools/README.md`'s description of the planes. Did the fix reach every reader
   of the class, or only the ones the triggering case touched?
4. **Security & privacy** — mandatory. A file name is attacker-controlled input
   to a guard: hunt the name that makes a blocking guard skip a file, read a
   different file, or crash into an exit code that passes. Check that names are
   never passed to a shell and that a leading dash cannot become a git option.
   `/security-review` is discharged by grounds (a landed delta; the pending diff
   is not the work) — say so, and deliver the code-altitude read by hand against
   the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest tools.test_report tools.test_conflictscan
  tools.test_leakscan tools.test_secretscan tools.test_board
  tools.test_harvestscan tools.test_publishscan -v` at HEAD, and at `68e9baf` in
  a scratch clone
- the "fails on old code" claim: the new tests run against `c1cef10^` and
  `4dfaf8d^` in a scratch clone
- the byte-identity claim, re-driven on this repo's tree and staged planes only
  (the commits' sibling-repo runs are not re-run — never point a scanner at other
  repos on the machine; say so)
- each touched tool's `--selftest`; the floor on both planes at HEAD; the full
  Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only
  git is fine. Fixture repos with hostile names, config variations and older
  checkouts go in a private area under your session scratchpad, named by your
  prefix; never set global git config.
- One heavy process at a time on a shared machine: the full suite at most once, in
  the foreground. Never point a scanner at any other repo on the machine.
- `/security-review` reads the session's pending diff: discharge it by grounds for
  this landed delta, or keep the tree clean whenever you spawn it.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ
  English. Never quote a secret, placeholder token, email address or personal
  detail — this repo is PUBLIC; describe and locate instead.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer, this
brief's sibling `docs/reviews/2026-10-16-1551-git-quoted-paths-cold.deferred.md`,
the commissioning items `260` and `280` in
`docs/roadmap/115-guardrail-architecture-mike-commissioned/`, and `120` in
`docs/roadmap/260-sharing-public-since-2026-07-10-adr-0005/` (each barred as a
section).

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/760-rule-4-cold-pass-queued-quoted-paths.md
--also-exclude docs/reviews/2026-10-16-1551-git-quoted-paths-cold.deferred.md
--also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned
--also-exclude docs/roadmap/260-sharing-public-since-2026-07-10-adr-0005
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never
barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, the standing
checklist V1–V7 each answered or discharged with grounds, the per-plane name
table, findings with stable IDs (prefix `QP`: `QP1`, `QP2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line
with counts, a re-run ledger, and a follow-up checklist. Then STOP and commit
phase 1 unrevised before opening the sibling.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict:
per-finding notes against the seeded questions and the intent record, any finding
formed at reconcile marked as such, and the overall line restated. Never revise
phase-1 text. Then fold the sibling in below the reconcile and delete it.

Findings on self-authored doctrine are the principal's to decide (rule 3; a
guard is doctrine by function): record all, apply nothing; counsel per finding is
welcome, labelled and kept beneath it.

---

# Verdict — 2026-10-17 UTC

## Provenance (repeated, V7)

- **Reviewer:** a fresh `claude-fable-5-1` subagent (the principal-named tier, ruling
  2026-08-04), spawned 2026-10-17 UTC by a Fable orchestrator that authored none of
  the delta and none of this brief, held the deferred sibling out of reach, and forms
  no finding. The reviewer formed every finding and every severity below.
- **Worktree:** `atelier-review-1017` (branch `review-1017`, HEAD `8acfff1`, which
  carries every delta on `main`). No writing git command was run there. Fixture
  repos, config variations and the older checkouts (`68e9baf`, `e71d40c`, `c1cef10^`,
  `4dfaf8d^`) live in a private clone under the session scratchpad, folder `QP/`.
- **Interrupted and resumed:** the pass was cut by an API rate limit on 2026-10-17 and
  resumed in the same agent transcript; no state was lost (every probe below ran in
  this transcript and its outputs are in the `QP/` scratch area).
- **What was read:** this brief; `REVIEW.md` whole; the two landing diffs
  (`c1cef10`, `4dfaf8d` — code and tests) and the six tools' git-reading call sites at
  HEAD; `report.py`, `floor.py` (registry and the scanner launch), `filewalk.py`,
  `.githooks/pre-commit`, `.github/workflows/ci.yml`, `.atelier-floor.json`,
  `tools/README.md` §`report.py`; commit **subjects and `--stat` only** — the landing
  commits' message bodies stayed closed (barred until phase 2); `instruments/ccclose`
  around its `git log --name-only` reader. No prior verdict, no `SESSIONS.md`, no
  session record, no `ROADMAP-DONE.md`, no queue pointer, no sibling, no commissioning
  item was opened. The tree sweep ran through `coldsweep.py` with the brief's four
  `--also-exclude` paths and **without** `--include-barred` (65 hits, 442 files barred).
- **Exposure, disclosed:** a `git log` of the delta's files `4dfaf8d..HEAD` printed
  merge and commit *subjects* (dates and one-line titles), which name board items by
  number. Nothing evaluative was read. The full Python suite exceeded the harness's
  foreground limit and was moved to the background *by the harness*, not by me; its
  output file was read after it completed (exit 0).

## Lens 1 — approach and assumptions (named first, then attacked)

The delta's load-bearing assumptions, as I name them:

1. *git's quoting is exactly the set `unquote_c` undoes.* **Holds.** git's `quote.c`
   writes `\a \b \f \n \r \t \v \\ \"` and three-digit octal for everything else; the
   raw `+++` headers captured from real git for fourteen hostile names (table below)
   used no other spelling.
2. *The default `b/` prefix is the only one a guard will meet.* **False at the landing
   commit** — `diff.noprefix`, `diff.mnemonicPrefix` and `diff.srcPrefix/dstPrefix`
   all change it, and git reads them from the user's config. True at HEAD only because
   `39a74b9` pinned `--src-prefix=a/ --dst-prefix=b/` eleven days later (QP2).
3. *A trailing TAB on a header always and only marks a name with a space.* **Holds**
   for git 2.50: the TAB appeared after `sp ace.md`, `trail .md`, `x b/y.md` and the
   quoted `say "hi".md`, and did not appear after `tab<TAB>name.md` or
   `endtab<TAB>.md` (a tab inside a name is always written `\t`, so the whole header
   is quoted and `rstrip("\t")` cannot eat it). A trailing *space* survives.
4. *Unstated: the process runs with the repo as its working directory.* The staged
   diff is `git diff --cached` with no `-C root` — in the delta's argv and in HEAD's
   `STAGED_DIFF_CMD`. False whenever a guard is run by hand with `--root` elsewhere
   (QP1).
5. *Unstated: git's output is UTF-8 text.* The delta's `-c core.quotePath=false` makes
   a non-UTF-8 name arrive as raw bytes, and the landing commit read it with
   `text=True` (QP3).
6. *Unstated: a `+++` line is a header wherever it appears.* False — an added line
   `++ b/x` prints as `+++ b/x`; the docstring named the hazard and the narrow test did
   not close it (QP4; closed by `115/280`, not this delta).

**The non-goal** (header read with `core.quotePath=false` rather than a `-z` path list
joined to the diff) is reviewable and I reviewed it: it fences off the one design that
would have avoided both the raw-byte crash (QP3) and the lossy spelling (QP6). I accept
it at HEAD because the structural reader now decodes bytes with `replace` and the
staged guards never open a file by the name they read — but the fence sat exactly
where the delta's residual risk was, so it is recorded here rather than waved through.

## Lens 2 — correctness and quality

Everything re-run, not read (ledger at the end). The delta does what its subjects
claim for every name git C-quotes, on every plane it touched, at the landing merges
and at HEAD. What it did not do: pin the git configuration it depends on (QP2), handle
the raw bytes its own flag lets through (QP3), or test either. Its "fails on old code"
claim reproduces for the real reason, not only by import error (ledger).

### Per-plane, per-name table

Fixture: a fresh repo under an isolated `GIT_CONFIG_GLOBAL` (user config never
touched), each name staged with a planted conflict marker, a synthetic secret-shaped
token and a private-key header, then each guard run `--staged --json` from the repo
root. `HIT` = reported under its real name. The non-UTF-8 name was placed in the index
with `git update-index --cacheinfo` (APFS refuses it on disk). The posed row is an
ordinary file whose *content* holds a line `++ b/evil`. git 2.50.1, Python 3.14.

| name (staged plane) | pre-delta `4dfaf8d^` (s / l / c) | landing `68e9baf` | HEAD |
|---|---|---|---|
| `café/n.md` (NFC) | miss / miss / miss | HIT | HIT |
| `café/d.md` (NFD on disk; index holds NFC) | miss / miss / miss | HIT | HIT |
| `sp ace.md` | miss / wrong name (kept TAB) ×2 | HIT | HIT |
| `trail .md` (trailing space) | miss / wrong name ×2 | HIT | HIT |
| `tab<TAB>name.md` | miss ×3 | HIT | HIT |
| `nl<LF>x.md` | miss ×3 | HIT | HIT |
| `say "hi".md` | miss ×3 | HIT | HIT |
| `back\slash.md` | miss ×3 | HIT | HIT |
| `-dash.md` | miss / HIT / HIT | HIT | HIT |
| `12345` | miss / HIT / HIT | HIT | HIT |
| `b/inner.md` | miss / HIT / HIT | HIT | HIT |
| `x b/y.md` | miss / wrong name ×2 | HIT | HIT |
| `中文.md` | miss ×3 | HIT | HIT |
| `endtab<TAB>.md` | miss ×3 | HIT | HIT |
| content line `++ b/evil` | attributed to `evil` ×3 | attributed to `evil` ×3 | HIT |
| non-UTF-8 byte in name | s: **traceback**; l, c: miss | **traceback ×3, no report** | reported, lossy (U+FFFD) |

(s = secretscan, l = leakscan, c = conflictscan. Pre-delta secretscan already carried
`-c core.quotePath=false` and so already crashed; pre-delta secretscan "miss" on the
plain names is the same crash hiding them — without the non-UTF-8 name it reports
them.)

| `-z` planes (`ls-files`, `ls-tree`) | pre-delta | landing | HEAD |
|---|---|---|---|
| harvestscan `list_markdown` WORKTREE / INDEX / HEAD | 8 of 15 names missing | all 15 listed, all readable | same |
| board `_index_sections` (INDEX) | 6 of 15 items | all 15, content read | same |
| publishscan `--staged`, never-publish file under each name | — | 15 of 15 | 15 of 15 |
| non-UTF-8 name on `-z` planes | — | listed; `git show :path` round-trips; WORKTREE unreadable (cannot exist on APFS) | same |

| git config the guards do not pin | landing `68e9baf` (s / l / c) | HEAD |
|---|---|---|
| `diff.noprefix=true` | s: names wrong (quotes kept); **l, c: every real file missed** | all HIT |
| `diff.mnemonicPrefix=true` | s: names wrong (`i/` kept); **l, c: every real file missed** | all HIT |
| `diff.srcPrefix`/`dstPrefix` | not run at landing (same mechanism as above) | all HIT |
| `color.diff=always`, `color.ui=always` | HIT (`--no-color` already pinned) | all HIT |
| `diff.external=<script>` | **exit 0, nothing reported, ×3 — fail-open** | all HIT |
| `core.precomposeUnicode=false` | — | all HIT |
| `core.quotePath=false` (user) | — | all HIT |
| `diff.relative=true` (cwd = root) | — | all HIT |

Under `diff.noprefix` at landing the only reason the exit code was 1 at all was the
posed `evil` header and `b/inner.md` (read as `inner.md`); a repo without those names
would have exited 0 with planted secrets staged.

### The byte-identity claim

Re-driven on this repo's tree and staged planes only, in the private clone (three
paths staged: a root file, a method doc, one new file), old scanner against new:
publishscan tip and staged (`c1cef10^` vs `e71d40c`), secretscan, leakscan
(structural-only, an empty term file) and conflictscan `--staged`, `board --check
--staged`, `harvestscan --staged --only-bulk-deletes` (`4dfaf8d^` vs `68e9baf`) —
**byte-identical output and exit code in all eight pairs.** The commits' sibling-repo
runs were not re-run: no scanner was pointed at any other repo on this machine.

## Lens 3 — completeness and harvest

Every git path reader in `tools/` at HEAD: `report.STAGED_DIFF_CMD` → structural
reader (three guards); `ls-files -z`/`ls-tree -z` → `nul_paths` (board, harvestscan);
`ls-files -z`, `diff --cached --name-only -z`, `log --name-only -z` → publishscan's own
`_nul_tokens`/`_decode`; `ls-files -z` → `filewalk` (`os.fsdecode`, predates the
delta). `blockscan.git_show` takes paths from its own map, not from git. So the fix
reached every *tool* reader. It did not reach `instruments/ccclose`, which reads
`git log --name-only` without `-z` and tests `startsWith('docs/method/')` (QP5).
`tools/README.md`'s plane prose is accurate at HEAD. V3: no mirror of the `+++ b/`
rule exists outside `tools/` (grep of `docs/method`, `docs/build`, `skills`,
`commands`, `.github`, `pre-commit.sample`: none).

## Lens 4 — security and privacy

`/security-review` **discharged by grounds**: it reads this session's pending diff,
which is other reviewers' drafts and the orchestrator's partition, not the landed
delta. Read by hand against OWASP Top 10 (2021) at code altitude:

- **A03 injection:** no shell anywhere on these paths; every git call is a list argv;
  `git show :<path>` puts the name after a colon so a leading dash cannot become an
  option (verified: `-dash.md` HIT on every plane); tests stage with `--`. Clean.
- **A01 broken access / path traversal:** names from git are repo-relative and git
  never emits `..`; harvestscan's WORKTREE read is `root / rel`. Clean.
- **A04 insecure design — fail-open paths:** found two. A guard whose `--root` is not
  its working directory reads another repo's index and passes (QP1, open). At landing,
  `diff.external` emptied the diff and all three guards passed (QP2, closed at HEAD).
  A crash exits 1 (blocks) and `DiffReadError` exits 2 (blocks): fail-closed by code,
  though QP3's crash reported nothing.
- **A09 logging — output injection:** a name carrying an ESC byte reaches the terminal
  raw in the three guards' human output (live: `red<ESC>[31m.md` printed unstripped by
  conflictscan at HEAD); publishscan strips controls, `floor.py` strips them from
  config. The repaint class the repo already closed for config (C1F3) is open for
  file names (QP9).
- **Privacy:** no new data collected or printed beyond the path already in the report.

## Standing checklist V1–V7

- **V1** — the `diff_header_path` docstring at landing claimed its narrow test defends
  against posed `++ …` lines; it does not (QP4). Otherwise claims match evidence.
- **V2** — every live claim in scope re-run (ledger). One did not survive as stated:
  "read git's quoted paths correctly in the staged-plane guards" was true only under
  default diff config (QP2).
- **V3** — no mirror sites; discharged (lens 3).
- **V4** — two `-z` readers with different decoding (QP6); otherwise one home.
- **V5** — secretscan's docstring at HEAD still says *this parser* strips the TAB and
  passes `quotePath=false`, while the parsing lives in `report.py` (QP7). Landing text
  agreed with itself.
- **V6** — done above; `/security-review` discharged by grounds.
- **V7** — provenance stated in the brief and repeated above.

## Findings

**QP1 — MODERATE (open at HEAD; pre-existing, carried through the delta's own lines).**
The staged diff is read from the process's working directory, not from `--root`. All
three boundary guards (secretscan, leakscan, conflictscan) run `git diff --cached`
with no `-C root`, in the delta's argv and in HEAD's `STAGED_DIFF_CMD`;
`report.staged_added()` takes no root at all. Live at HEAD and pre-delta: a fixture
full of planted secrets, markers and a key header, `--staged --root <fixture>` run from
another repo with a clean index → exit 0, zero findings, three times. The hook plane
is safe (git sets cwd to the work-tree root); `floor.py` passes no `cwd` either, so
`floor.py --plane hook --root <other repo>` by hand is the reachable case, and
board/harvestscan/publishscan already use `-C root` on the same plane. *Counsel:* give
`staged_added` a `root` parameter and prepend `-C root`; one test that runs a guard
from a foreign cwd.

**QP2 — MAJOR at the landing commit `4dfaf8d`; closed at HEAD by `39a74b9` (not this
delta) except one untested leg.** The delta's header reader accepted only `b/` and the
guards did not pin the diff's prefixes or disable external diff. Under
`diff.noprefix=true` or `diff.mnemonicPrefix=true` leakscan and conflictscan missed
*every* real staged file (lens-2 table); under `diff.external` all three exited 0
having read nothing — a fail-open on blocking boundary guards, reachable by a common
user setting, shipped 2026-10-05 and unflagged until 2026-10-16. The delta's new tests
passed on the author's machine because they ran under the author's config, which they
did not isolate or pin. At HEAD `STAGED_DIFF_CMD` pins `--no-color --no-ext-diff
--src-prefix=a/ --dst-prefix=b/` and `test_report.py` pins `noprefix` and
`mnemonicPrefix`; **no test pins `--no-ext-diff` or `--no-color`**, the two legs that
fail open rather than wrong-name. *Counsel:* a regression test per pinned flag, set in
the fixture repo's config; record the class ("a guard's git invocation pins every
config that changes its output shape") where guard-building rules live.

**QP3 — MODERATE at landing; closed at HEAD by `39a74b9`; residue in QP6.** Adding
`-c core.quotePath=false` to leakscan and conflictscan made a non-UTF-8 byte in a
staged name arrive raw, and the landing code read it with `text=True`: all three
guards died with a `UnicodeDecodeError` traceback, exit 1, **no findings printed for
any file** (secretscan already had this since `320/290`). Fail-closed by exit code,
silent about the fifteen other staged files. The delta's tests pinned `unquote_c` on
`\377`, the octal spelling git writes only under `quotePath=true` — a spelling the
guards can never receive, while the spelling they do receive crashed the process.
*Counsel:* a staged-plane test with an index-injected non-UTF-8 name (the fixture
technique above works without touching the disk).

**QP4 — minor (landing; closed at HEAD by `115/280`).** `diff_header_path`'s docstring
said a looser test "would take an added line whose text is `++ …` for a header",
implying the narrow one does not; an added line `++ b/evil` prints as `+++ b/evil` and
passed it, moving every following line's attribution to `evil` on all three guards at
landing (table). Not this delta's commission, but a claim it made and did not test.

**QP5 — minor (open; lens-3 harvest).** `instruments/ccclose` reads
`git log --name-only` without `-z` and tests the path with `startsWith('<dir>/')`. git
C-quotes a non-ASCII or control-character path there (verified: a `docs/method/` file
with an accent prints as a quoted, octal-escaped string), so a doctrine or tool change
under such a name is not counted as touched and the "reviews queued where owed" check
can pass falsely. Read from the code; ccclose itself was not run (it is an installed
instrument and the rules bar bare runs; a by-path run needed a window and a board).
*Counsel:* `-z` plus NUL splitting, or strip and unquote.

**QP6 — note (answers the brief's two decoding questions).** For the same non-UTF-8
name, the staged header reader yields U+FFFD (lossy; `parse_added_lines` decodes with
`replace`, and `unquote_c` would too) while `nul_paths` yields a surrogate-escaped
string that round-trips into a later `git show` (verified on INDEX and HEAD planes).
Two spellings of one name; harmless today because the three staged guards never open a
file by name — they key, filter and print only. publishscan has its own third reader
(`_nul_tokens` + `_decode`: `replace` plus control-stripping), so there are two `-z`
readers of one thing (V4), differing in exactly the undecodable case. *Counsel:*
one reader, surrogate-escape everywhere, and sanitise at the print seam (QP9).

**QP7 — note (HEAD; rests on `39a74b9`'s sweep, not this delta).** secretscan's
`staged_added_lines` docstring still describes *this parser* stripping the TAB and
passing `quotePath=false`; both now live in `report.py`.

**QP8 — minor (landing; largely closed at HEAD).** The delta's new staged-plane tests
did not isolate or pin the git config they depended on, so a user's `diff.noprefix`
would have failed them — and, worse, the guards — without the failure naming why. The
publishscan tests pinned `core.quotePath=true` and are the model. At HEAD the command
pins and `test_report.py` pins two of the four settings (QP2's residue).

**QP9 — minor (open; security, A09 class).** A staged file name carrying terminal
control bytes is printed raw by secretscan, leakscan and conflictscan's human output
(live at HEAD). publishscan strips controls from names and `floor.py` from config
(C1F3, FR3); the file-name surface of the same class is open on three blocking guards.
*Counsel:* strip or escape at `render_human`, as publishscan does.

## Overall

**PASS-WITH-FINDINGS — 1 MAJOR · 2 MODERATE · 4 minor · 2 note.**

The MAJOR rests on the landing commit and is closed at HEAD by a later commit; what
remains open of it is a regression test. The open defects at HEAD are QP1 (cwd, not
`--root`), QP5, QP9 and the test gaps. The delta fixed the class it named, on every
plane it named, byte-identically for clean trees — and left the git configuration and
byte handling around its own change unpinned.

## Re-run ledger

| claim / check | how | result |
|---|---|---|
| seven touched test modules at HEAD | `python3 -m unittest tools.test_report … tools.test_publishscan` | 578 tests OK |
| same at the landing merge `68e9baf` | scratch checkout | 550 tests OK |
| new tests fail on pre-change code `4dfaf8d^` | the six test files copied over the parent tree | 26 run, 27 failures + 29 errors: the behavioural ones fail on the real defect (quoted names "not found in {}", `-z` lists differ, board staged ≠ disk); `test_report` fails by missing helpers |
| new publishscan tests fail on `c1cef10^` | same | 2 of 3 fail (`0 != 1`); the clean-non-ASCII test passes on old code, as a regression guard should |
| byte-identity, tree and staged planes | eight old/new pairs on the private clone | byte-identical, exit codes equal |
| `--selftest` × conflictscan, leakscan, secretscan, board, harvestscan, publishscan | by path | all exit 0 |
| floor, hook plane, HEAD | `floor.py --plane hook --root .` (empty staged set) | exit 0, all enforced |
| floor, CI plane, HEAD | `floor.py --plane ci --root .` | exit 0; secretscan 23 advisory (expected), pathscan 2 warn-only (pre-existing, unrelated), leakscan structural-only as designed |
| full Python suite, once | `unittest discover -s tools` | 1916 tests OK in 636 s (moved to background by the harness at its 600 s foreground limit; read after completion) |
| hostile-name fixture | `QP/drive.py`, 14 names + posed content + index-injected non-UTF-8 | tables above; HEAD, landing, pre-delta, 9 config variants |
| cwd probe | guards `--staged --root <fixture>` from another repo | exit 0, 0 findings, ×3 at HEAD and pre-delta |
| ESC-in-name probe | conflictscan `--staged`, human output | control bytes printed raw |
| `coldsweep` | brief's four excludes, no `--include-barred` | 65 hits / 595 files, 442 barred |
| node instrument tests | — | **not run**: the delta touches no instrument; the floor run above was `floor.py`'s two planes, not the whole `ci.yml` |

Machine note: load averages 4–6 throughout, 22 at the end of the full suite (other
sessions live); one heavy process at a time, all under `nice -n 10`.

## Follow-up checklist (for the principal's decision; nothing applied)

- [ ] QP1 — `staged_added(root)` with `-C root`; one foreign-cwd test.
- [ ] QP2 — regression tests for `--no-ext-diff` and `--no-color`; record the
      "pin every output-shaping config" class for guards.
- [ ] QP3 — a staged-plane test with an index-injected non-UTF-8 name.
- [ ] QP5 — `ccclose`: `git log --name-only -z`.
- [ ] QP6 — one `-z` reader; surrogate-escape in the header reader too.
- [ ] QP7 — secretscan docstring points at `report.py`.
- [ ] QP9 — strip control bytes from reported paths in the three guards' human output.
- [ ] Phase 2: open the sibling, reconcile, fold.
