# Cold pass — licenscan's advisory tier, and the floor reading its count

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-17 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/840-rule-4-cold-pass-queued-licenscan-advisory-tier.md`.
**Why it earns a review:** a publish gate that may never be softened by a child now
lets a class of its findings through with exit 0, the floor's board gains a count read
back from that gate's output, and two registry docstrings that say what may be softened
were rewritten. All of it reaches every child at its next run.

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
  message body** (the author's own account, with a principal quote); the merge's
  re-merge diff, including its two code hunks; the subject, `--stat` **and message
  body** of the later commit on the same files (another pass's subject); two
  2026-10-16 briefs in full as templates; `docs/reviews/` filenames and
  filename-level greps (no prior verdict opened); the title lines of the
  commissioning board items; grep-hit lines naming licenscan in `docs/build/`; and
  its harness-loaded memory index. It did not open the intent record,
  `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md` or
  `docs/method/REVIEW.md`. What its orchestrator read is the orchestrator's to
  disclose; it passed on an instruction file, three templates and a list of taken
  prefixes, and no evaluative content. Everything evaluative is in the sibling.

## What the work is

Landing commit (diff it; review the paths at HEAD, `b50db0c` or later):

- `e3e8a4f` (2026-10-16 15:35 UTC) — licenscan: make the warning real, and make two
  guard descriptions true; landed in merge `6acefc9` (2026-10-16 15:41 UTC)

**The merge is part of the delta.** Beyond board and record files, `6acefc9` itself
edits `tools/licenscan.py` and `tools/README.md` (a date in each); read it with
`git show --remerge-diff 6acefc9 -- tools/`.

Delta paths: `tools/licenscan.py` (the *two responses* docstring, the exit-code
table, `RESPONSE_*`, `ADVISORY_SEVERITIES`, `ADVISORY_COUNT_PREFIX`, `Finding`'s
`response` and `blocks`, `Report.blocking`/`advisory`, `advisory_count_line`,
`_render_advisory`, `render_human`, the `--json` fields, the exit code, the
selftest), `tools/floor.py` (licenscan's `advisory_count=True` and the docstrings of
the module and `Scanner` about what may be softened), `tools/pathscan.py` (its
STATUS docstring), `tools/test_licenscan.py`, `tools/test_floor.py`,
`tools/test_report.py`'s licenscan pins, and `tools/README.md`'s licenscan section.

**Later commit on the same files — not this delta; do not attribute it to it.**

- `dc0ed0e` (2026-10-16) — floor: scope the advisory count to its scanner, pin
  three more unsoftenable checks (its own pass, 160/860); it rewrites the count
  reader this delta first relied on and touches one comment in `tools/licenscan.py`

Review the count path at HEAD; to judge this delta as landed, run `e3e8a4f` too.
The commit's parent is `2e2da81`, the base of two sibling commits (`f4afb7a`,
`72a68cc`) that also touch `tools/README.md` and, for one, `tools/test_report.py`.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests
and live behaviour. The lenses organise it; they do not bound it. Non-goals are the
only narrowing and are themselves reviewable.

Enumerate every finding licenscan can raise at HEAD — each kind, the severity each
code path assigns, and the response it therefore gets — and compare that list with
every place that states which findings block (module docstring, README tables,
selftest, tests, `floor.py`'s comments). Then every caller that reads licenscan's
exit code or `--json`: the floor on both planes, CI, any publish or pre-flip gate,
`docs/build/REPO-STANDARD.md`'s publish-time use, a child's hook; for each, what it
did with a `medium` finding before and what it does now. Check that the advisory
count line is printed on every path that can exit 0 or 1 (and what happens at exit
2), that the floor reads it from the right scanner's output, and what the board shows
when the line is missing. On `floor.py`: the docstrings now name an exception to
"boundary checks have no advisory form" — check the registry entry that exception
points at, and whether "may never be softened" still has one meaning across the
registry, `docs/build/templates/CONTRIBUTING.md` and `docs/method/GUARDS.md`. On
`pathscan.py`: check each fact its new STATUS text states against the registry and
`ci.yml`. **Non-goals:** the principal's choice that the warning be real (quoted in
the delta) — but which findings were placed in the advisory class, and how, is in
scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Among them: that severity is the right key for response; that "a severity not
   named advisory blocks" is fail-safe in practice; that a count line on stdout is
   a sound contract between two tools; that an advisory nobody is forced to read
   is still a control.
2. **Correctness & quality.** Read `tools/licenscan.py` whole at HEAD and diff
   `e3e8a4f` plus the merge's hunks. Build the kind → severity → response → exit
   table from the code, not the prose, and set it beside each prose table. Check
   whether the new tests would fail on `e3e8a4f^` for the reason each test names,
   and whether the `--json` change keeps every old field's meaning.
3. **Completeness / harvest.** Every surface still calling these findings a
   "warn", or stating licenscan's exit codes or what it blocks: the README's other
   sections, `docs/build/`, `docs/method/`, the templates, `CHANGELOG.md`, skills.
   Every surface listing which checks may be softened, against the registry at
   HEAD.
4. **Security & privacy** — mandatory. Licence findings are a publication-safety
   boundary for a public repo. Hunt for a finding that a person would want to stop
   a publish but that now exits 0 — an unknown declaration hiding a copyleft
   licence, a custom LICENSE, a dual-licence expression, an allow-marker reach —
   and for any way a file's content can change the board's count (the line is read
   back from output that echoes repo-controlled paths and messages). Fixtures from
   synthetic values only. `/security-review` is discharged by grounds (a landed
   delta; the pending diff is not the work) — say so, and deliver the code-altitude
   read by hand against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest discover -s tools -p 'test_licenscan.py' -v`, the same for
  `test_floor.py`, `test_report.py` and `test_pathscan.py`; `--selftest` for
  `licenscan`, `floor` and `pathscan`
- licenscan at `e3e8a4f^`, `e3e8a4f` and HEAD in a scratch clone, over synthetic
  fixture repos covering every kind in your table: compare stdout, exit code and
  `--json`
- the floor's board on a fixture with advisory licence findings, at `e3e8a4f` and
  at HEAD (so `dc0ed0e`'s change is not charged to this delta)
- the floor on both planes at HEAD; the full Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only
  git is fine. Fixture repos, older checkouts and probes go in a private clone
  under your session scratchpad, named by your prefix.
- One heavy process at a time on a shared machine: the full suite at most once, in
  the foreground. Never point a scanner at any other repo on the machine — the
  delta's estate-wide blast-radius claim is not re-driven that way; reason about it
  from fixtures.
- `/security-review` reads the session's pending diff: discharge it by grounds for
  this landed delta, or keep the tree clean whenever you spawn it.
- Never open another `docs/reviews/2026-10-17-*` brief — it is another pass's
  framing.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ
  English. Never quote a secret, placeholder token, email address or personal
  detail — this repo is PUBLIC; describe and locate instead.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer, this
brief's sibling `docs/reviews/2026-10-17-0955-licenscan-advisory-tier-cold.deferred.md`,
the message bodies of `e3e8a4f` and `dc0ed0e` (read subject, stat and diff only),
the queue pointer `160/860`, and items `290` and `320` in
`docs/roadmap/115-guardrail-architecture-mike-commissioned/` (the commissioning
item, and a follow-up filed at the same merge).

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/840-rule-4-cold-pass-queued-licenscan-advisory-tier.md
--also-exclude docs/reviews/2026-10-17-0955-licenscan-advisory-tier-cold.deferred.md
--also-exclude
docs/roadmap/160-doctrine-review-owed/860-rule-4-cold-pass-queued-advisory-count-per-scanner.md
--also-exclude
docs/roadmap/115-guardrail-architecture-mike-commissioned/290-three-guards-describe-a-response-tier-their-code-lacks.md
--also-exclude
docs/roadmap/115-guardrail-architecture-mike-commissioned/320-three-small-floor-test-and-contract-gaps.md
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never
barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, the standing
checklist V1–V7 each answered or discharged with grounds, the kind → response
table, findings with stable IDs (prefix `LA`: `LA1`, `LA2`, …) and severities
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

## Verdict — phase 1 (written 2026-10-18T00:20Z; sibling not opened)

**Overall: PASS-WITH-FINDINGS — 1 MAJOR · 1 MODERATE · 5 minor · 3 note.** The blocking
set did not move and every claim the delta makes about the `high` tier reproduces. What
moved to exit 0 is wider than the prose says: the `medium` label bundles "judged benign"
with "cannot judge", so every licence id and family mix the tool does not model now passes
the gate (LA1). The board leg the tier ships with can be set to any number by a committed
file at HEAD (LA2).

### Provenance (V7)

- **Reviewer:** this verdict was formed by a Claude Code subagent running as **Fable 5.1**
  (`claude-fable-5-1`) — the tier the principal named (ruling 2026-08-04), checked at
  selection. The rule-4 stop clause did not bite.
- **Spawn:** dispatched by a Mike-opened Claude Code **cloud** session (`claude-fable-5-1`,
  orchestrating; it opened on `claude-opus-5` and Mike switched it to Fable before any claim
  or pass). That session authored none of the delta and none of this brief, and was not
  started or instructed by their authors. It forms no finding and writes no severity. It
  holds the `.deferred.md` sibling outside the checkout at a path I was not given, commits
  this phase-1 text before releasing the sibling, and received one operational note from
  Mike's watching session (model, queue scope, container facts, merge instruction — no
  evaluative content about any delta). The claim line in the queue pointer discloses the
  same shape; I have not opened the pointer.
- **Author of the work:** the queue run whose intent record is dated 2026-10-16 15:01 UTC
  (an Opus orchestrator with dispatched workers; the trailer names a Sonnet model). Not
  opened. I had no contact with it.
- **Brief-writer:** an Opus subagent, off-tier for review, disclosed above; I did not
  interact with it.

### What I read, and every exposure

Read in order: `docs/method/REVIEW.md` whole; this brief whole; `docs/method/00-APEX.md`
once. Then the delta: `git show --stat --format=%s` for `e3e8a4f`, `6acefc9`, `dc0ed0e`
(subjects and stats only); `git diff e3e8a4f^ e3e8a4f` (the landing diff); `git show
--remerge-diff --format=%s 6acefc9 -- tools/` (the brief's command with the body suppressed
— the brief's own spelling would have printed the message body); `git diff dc0ed0e^
dc0ed0e` (to know what is *not* this delta). At HEAD, whole: `tools/licenscan.py`,
`tools/report.py`, `tools/test_licenscan.py`, `docs/method/GUARDS.md`,
`docs/build/templates/CONTRIBUTING.md`, `.githooks/pre-commit`,
`.github/workflows/ci.yml`, `.atelier-floor.json`, `.licenscanignore`, `commands/scan.md`.
In part: `tools/floor.py` (docstring, `Scanner`, the registry, the count reader, `plan`,
`run`, `render`, `Result`), `tools/README.md` (the blind-spot list and the licenscan
section), `tools/pathscan.py` (STATUS docstring), `tools/secretscan.py` (its two-response
docstring and render), `tools/test_floor.py` / `tools/test_report.py` / `tools/
test_pathscan.py` (the delta's hunks and the licenscan pins), `docs/build/REPO-STANDARD.md`
(the licenscan lines), `CHANGELOG.md` lines 25–75, `docs/build/README.md` lines 34–42,
`docs/build/templates/workflows/floor.yml` lines 15–55, `docs/decisions/0008-…` lines
188–212, `docs/method/CONVENTIONS.md` (the time row). Blobs at older commits via `git show
<sha>:<path>` (never a commit body): `tools/README.md` at `2e2da81`; `tools/floor.py` at the
four `tools/floor.py` commits dated 2026-08-04..08 (for LA3).

Exposures, disclosed:

1. Before switching to `coldsweep.py` I ran one **filename-only** search (`files_with_
   matches`) for `licenscan` over the whole tree. It listed the *names* of barred files —
   two sibling `docs/reviews/2026-10-17-*` briefs, the `160/840` and `160/860` pointers,
   `docs/SESSIONS.md`, `docs/ROADMAP-DONE.md`, 25 session logs, one `drafts/` and one
   `withdrawn/` file. Names only; I opened none. Every content search after that went
   through `tools/coldsweep.py` with the brief's five `--also-exclude` paths; the sweep
   reported 413 files excluded as rule-2 barred. `--include-barred` was never used.
2. The harness injected `docs/build/templates/CLAUDE.md` into my context as a reminder
   (a template, not barred). Noted for completeness.
3. `git log --oneline -1` on the clone printed the subject of the branch's latest commit,
   which names another pass's verdict (`review(RN)…`). Subject only; not opened.
4. `docs/decisions/0008-…` lines 188–212 carry an ADR amendment that cites a prior pass's
   finding ID and severity (AP2) — an ADR, not a verdict file, and not barred by
   `coldsweep`; read for the "may never be softened" list (lens 3). Disclosed because it
   is a prior pass's framing reaching me through a record.
5. `CHANGELOG.md` lines 53–64 are the author's own account of this delta (not barred).
   Its estate-wide claim is treated in V2 below.

Not read in phase 1: the message bodies of `e3e8a4f` and `dc0ed0e`; the intent record;
items `115/290` and `115/320`; pointers `160/840` and `160/860`; the sibling; anything under
`docs/reviews/` other than this file; `docs/SESSIONS.md`, `docs/sessions/`,
`docs/ROADMAP-DONE.md`.

### Container facts that bear on this pass

Cloud container: one full, unshallowed clone at `/home/user/atelier`, **no worktrees, no
sibling repos, no estate root, no `~/.claude/`**; `gh` present but its token invalid. So:
the CHANGELOG's "across 29 repos" claim and the brief's estate-wide blast-radius claim
**cannot be re-driven here** and are marked *not re-driven here (relayed)*; nothing was
pointed at any other repo (none exists here). Scratch: `/home/user/scratch/LA/` — a private
clone (`clone/`), tool trees extracted with `git archive` at `2e2da81` (`at-parent/`) and
`e3e8a4f` (`at-landing/`), 26 synthetic fixture repos (`fx/repos/`), and copies of the
delta's tests laid over the parent tools (`probe-tests/`). No git command that writes ran in
`/home/user/atelier`; `git status` there shows nothing of mine. The floor's hook plane needs
a user-local leakscan term list this container lacks (board `115/350`), so the hook plane
reds on leakscan by design; the CI plane is the honest plane here. Both were run over the
private clone, not the shared checkout, because scanner output echoes file content and the
shared tree held other reviewers' dirty briefs.

### Lens 1 — Approach & assumptions

Load-bearing assumptions, named by me before reading the brief's list, then attacked:

- **A. Severity is the right key for response.** False as implemented. `GUARDS.md` § *What
  a finding is assessed on* says the field named `severity` "came to hold confidence", and
  licenscan's `medium` is exactly that mixture: for a permissive header in a permissive
  repo it means *low impact*; for `unknown-declaration` / `unknown-license` it means *low
  identification confidence, impact unknown*. Keying `response` on the label flips both at
  once. `GUARDS.md` also rules that **undeclared axes default to worst-case** — the
  unknown-impact bucket should default to block, and the delta sends it to exit 0. → LA1.
- **B. "A severity not named advisory blocks" is fail-safe.** True for severity *values*
  (probed: an unclassified `low` blocks) and beside the point for licence *ids*: the
  fail-open is not an unknown severity but an unknown id or family mix, which the code
  labels `medium` by construction (`_judge`, `compatibility`). → LA1.
- **C. A count line on stdout is a sound contract between two tools.** Sound only if the
  scanner never echoes repo-controlled text in the same shape after the line. licenscan
  echoes declaration values and paths unneutralised, and the delta prints the advisory block
  *after* the count line. At HEAD that is a spoof. → LA2.
- **D. An advisory nobody is forced to read is still a control.** The delta's answer is the
  board leg (E6b). That leg is the thing LA2 defeats; absent LA2, the leg is real: the board
  shows `🟡 N advisory finding(s)` on both planes (probed, fixtures F06, F13).
- **E. The pre-delta "warn" vocabulary identified the right set.** Not examined by the
  delta: `compatibility()` has returned `"warn"` for every cross-family mix it does not
  model since the tool was written, and the delta inherited that set as the advisory class
  rather than deciding it. The brief's non-goal protects the ruling that the warning be
  real, not the membership of the warning. → LA1.
- **F. The two docstring corrections are true at HEAD.** `floor.py`'s publishscan exception
  is true (registry: `advisory=["--warn", …]`, with its stated adoption-aid reason). The
  pathscan STATUS text is true in every fact but one date. → LA3.

### Lens 2 — Correctness & quality

**Kind → severity → response → exit, built from `tools/licenscan.py` at HEAD** (every
row probed live with a synthetic fixture; `parent` is `e3e8a4f^`):

| Kind · source | Severity | Response | Exit HEAD | Exit parent | Probe |
|---|---|---|---|---|---|
| `no-license` | high | block | 1 | 1 | F02 |
| `unknown-license` (LICENSE body unreadable), no `--expect` | medium | advisory | **0** | 1 | F03, F17 |
| `unknown-license` + `--expect` (the floor's shape) | medium + `expect-mismatch` high | block | 1 | 1 | F03, F17 (X) |
| `expect-mismatch` | high | block | 1 | 1 | F12 |
| `mismatch` · metadata ≠ LICENSE | high | block | 1 | 1 | F05 |
| `mismatch` · header, permissive ≠ permissive | medium | advisory | **0** | 1 | F06 |
| `mismatch` · header, permissive into copyleft | medium | advisory | **0** | 1 | F22 |
| `mismatch` · header, copyleft into copyleft (other family/version) | medium | advisory | **0** | 1 | F21, F24, F25 |
| `incompatible` · header, copyleft into permissive | high | block | 1 | 1 | F07, F23 |
| `incompatible` · header, copyleft under a custom LICENSE | high | block | 1 | 1 | F08 |
| `unknown-declaration` · metadata id not in the tables | medium | advisory | **0** | 1 | F09, F16, F18 |
| `unknown-declaration` · dual expression | medium | advisory | **0** | 1 | F10 |
| `unknown-declaration` · badge id not in the tables | medium | advisory | **0** | 1 | F19 |
| `unknown-declaration` · **SPDX header id not in the tables** | medium | advisory | **0** | 1 | F11 |
| config error (unreasoned ignore glob, bad root) | — | — | 2, no count line | 2 | F20 |

Set beside the prose: the docstring and README describe the advisory class as "a
permissive header differing from the repo licence, a LICENSE or declaration the scan cannot
read as a known SPDX id". Rows F11, F21, F24, F25 are in the class and outside that
description (LA4). The blocking row set matches the prose exactly; no `high` case moved.

**Tests fail on the parent for the reasons they name.** The delta's `TwoResponses` class
laid over the parent's `licenscan.py`: 8 fail / 2 error / 1 pass — the three exit-code tests
fail on `0 != 1`, the count-line tests on the line's absence, the headline test on `✗`
present, the JSON tests on `KeyError: 'blocked'` and the `response` attribute missing; the
one pass is `test_copyleft_poison_still_blocks`, a regression pin meant to pass on both.
`test_floor.py` at `e3e8a4f` over the parent tools: `…matches_licenscans_real_output` and
`…board_carries_licenscans_count` fail on `0 != 1`, `…registry_declares_who_carries_a_count`
on the missing `advisory_count`; `…blocking_licence_finding_still_fails_the_floor` passes
(regression pin). `test_report.py`'s licenscan pin fails on the missing count line. All as
the tests claim.

**`--json` keeps every old field's meaning.** `clean` still means nothing found at all
(F06: `clean=false, blocked=false`); `repo_license*`, `findings` unchanged; `blocked`,
`counts`, `response` added. A consumer reading `clean` for a green tick cannot be fooled
by an advisory-only run. ✓

**Render.** Both heads, both remediation paragraphs and the advisory block share no
wording (probed: no `✗`, no "Publish blocked" in an advisory-only run). The count line is
printed on every exit-0 and exit-1 path (F01, F02, F06, F13); at exit 2 nothing is printed
to stdout and the floor records `-1` (F20) — see LA6 for what the board then says.

**One overclaim in the code comment** (LA8): `response` is "derived from `severity`, so the
two can never disagree" — it is derived once in `__post_init__`; probed: assigning
`severity = "high"` after construction leaves `response == "advisory"`.

### Lens 3 — Completeness / harvest

Surfaces that state licenscan's exit codes, what blocks, or call the `medium` findings a
"warn", swept with `coldsweep.py` (`licenscan`, `warn`, `advisory`): the delta updated
`licenscan.py`'s docstring, the README licenscan section, `CHANGELOG.md` and the tests, and
left four mirror sites stale or contradictory (LA5). The "may never be softened" set is one
meaning across the registry (`advisory=None` on seven checks), `floor.py`'s module and
`Scanner` docstrings, the CONTRIBUTING template (the same seven names), and — from
`dc0ed0e`, not this delta — `test_floor.UNSOFTENABLE` and the floor selftest. ADR 0008's AP2
amendment lists six (it predates conflictscan, 2026-09-18) — a dated record, not a live
contradiction. `GUARDS.md` uses "advisory" for the child-declared check-level deferment;
the delta's `Scanner` docstring now says explicitly that `advisory_count` is a different
thing. Consistent.

What already existed and was duplicated rather than used: `tools/report.py` is the
single-source home for "common report lines" (115/080 part 3), and the delta copied
secretscan's `advisory_count_line` verbatim instead (LA7).

The pathscan STATUS rewrite: five facts checked against the registry, `ci.yml` and git;
four hold, one date does not (LA3).

### Lens 4 — Security & privacy

`/security-review` **discharged by grounds**: it reads the session's pending diff, and
this is a landed delta — my tree had no pending diff of the work; its exclusions also bar
markdown, so a clean pass over the prose half would be definitionally empty. The
code-altitude read was done by hand. I attempted to consult the OWASP Top 10 catalogue
live (`owasp.org/Top10/`); the proxy refused the tunnel (403), so the categories were
applied from the 2021 list as recalled, and I say so rather than claim a checked
catalogue. Against them: **A03 Injection** — output injection (CWE-117/CWE-116): a
declaration value or a file path with an embedded newline is echoed verbatim into a line
another tool parses → LA2 (live at HEAD). **A08 Software and data integrity** — a control
(the board count) derived from parseable prose rather than a structured channel → LA2
counsel. **A09 Logging and monitoring failures** — the board's wrong diagnosis at exit 2 →
LA6. **A05 Misconfiguration** — an unreasoned ignore glob fails closed at exit 2 ✓. A01,
A02, A04, A06, A07, A10: no authentication, cryptography, network, dependency or SSRF
surface in this delta. Subprocesses are argv lists, never a shell ✓. File reads are capped
at 8 MiB and streamed (pre-existing) ✓. Fixtures: every licence body, id and header in my
probes is fictional or a bare SPDX id; no real project's content was used.

Design altitude — the hunt the brief asked for, "a finding a person would want to stop a
publish but that now exits 0": found, eight shapes, all probed (LA1). Privacy: licenscan
prints paths and declaration text from the scanned repo only; nothing new is collected.
Threat enumeration at build time: the delta's docstrings reason about the count contract's
drift case (a missing line) and not about its spoof case (a forged line) — the half that
`dc0ed0e` then found for paths and that LA2 finds for declaration values and newlines.

### Standing checklist V1–V7

- **V1 — No claim stronger than its evidence.** Four claims exceed their mechanism: the
  advisory class as described vs as coded (LA4); "cannot quietly vanish" for the board
  count (LA2); "the two can never disagree" (LA8); "since 2026-08-05" (LA3).
- **V2 — Re-run every live-proven claim.** Ledger below. Everything re-drivable here was
  re-driven and reproduces. The CHANGELOG's "across 29 repos: 6 go red to green, 2 stay
  red, none goes the other way" is **not re-driven here (relayed)** — no sibling repo
  exists in this container; the fixtures reproduce the direction (medium-only repos go
  red → green; `high` stays red) but not the count.
- **V3 — A changed rule swept to every mirror.** Four sites missed (LA5).
- **V4 — One fact, one home.** The count-line wording lives in two scanners and a third time
  in the floor's regex (LA7); mechanically pinned, so minor.
- **V5 — No internal contradiction.** README "not the per-commit hook" vs the registry's
  hook template (LA5 iii); "friction" vs exit 0 (LA5 i, iv); `✓ … clean` head vs `clean:
  false` (LA9). The softenable set is one meaning everywhere live (lens 3).
- **V6 — Security & privacy.** Run; LA2 is a confirmed security finding with a severity and
  a recurrence-prevention step (lens 4 above and LA2).
- **V7 — Provenance.** Stated in the brief; repeated above.

### Findings

**LA1 — MAJOR (lens 1 / lens 4, design altitude). The advisory class is the `medium`
label, and `medium` bundles "judged benign" with "cannot judge"; every licence id and
family mix the tool does not model moved from exit 1 to exit 0.**
Evidence (all at HEAD, each exit 1 at `e3e8a4f^`): F10 a dual-licence expression in
metadata; F11 an SPDX header carrying a copyleft id outside the sixteen the tables know
(the probe used `EUPL-1.2`; `CDDL-1.0`, `OSL-3.0`, `SSPL-1.0`, `GPL-1.0`, `LGPL-2.0`,
`MPL-1.1`, `EPL-1.0`, `CC-BY-SA-4.0` are the same shape); F18 a metadata declaration of
such an id against an Apache LICENSE; F19 the same in a README badge; F17 a copyleft
LICENSE body the signatures do not recognise, scanned without `--expect` (the `commands/
scan.md` and README "pre-publish scrub" path — under the floor `--expect` still blocks it,
F17 X); F21 a `GPL-2.0-only` header in a GPL-3.0 repo; F24 a GPL-3.0 header in an MPL-2.0
repo; F25 an AGPL-3.0 header in a GPL-3.0 repo. The last three are real incompatibilities
the tool's own docstring says it "does not encode", and they now carry the same response as
a stray MIT header. The mechanism: `_judge` labels any id `normalise_spdx` cannot resolve
`medium`, and `compatibility` returns `"warn"` for every cross-family mix except
copyleft-into-permissive; the delta then equates `medium` with "reported, never a gate".
Doctrine: `GUARDS.md` — "undeclared axes default to worst-case", and "assessment is not
response" — the field being keyed on holds confidence for half its members. The pre-delta
text gave this bucket its teeth with "friction, never a false pass"; the delta read
"friction" as "warn" and did not ask which members had earned it. The brief's non-goal (the
ruling that a warn be real) is not challenged; which findings are the warn is, and the
brief puts that in scope.
*Counsel (the reviewer's, labelled; the principal decides):* (a) split the class at the
confidence boundary — `unknown-declaration` from an `spdx-header` source, and every
copyleft-into-copyleft / weak-into-strong header mix, block; `unknown-license` blocks when
no `--expect` is given; permissive-into-permissive and permissive-into-copyleft stay
advisory. Small code change in `_judge`/`compatibility` (or a second set beside
`ADVISORY_SEVERITIES` keyed on kind+source), tests exist to extend. (b) widen the id tables
and keep the design — buys coverage, does not close the class. (c) accept as built, and
rewrite the README blind-spot list and `commands/scan.md` to say the standalone gate no
longer stops on a licence it cannot read. Recommendation: (a); it keeps the ruling (a real
warn) and restores the worst-case default where the tool is guessing.

**LA2 — MODERATE (security; lens 4, code altitude). At HEAD a committed file can set the
board's licenscan advisory count to any number, including zero.**
Evidence: F15 — a `pyproject.toml` whose `license = "…"` value contains a newline followed
by the count line's exact wording; F26 — a file whose *name* does the same. Both are
echoed verbatim into the advisory block, which the delta prints *after* the real count
line; `floor.py` at HEAD takes the **last** matching whole line (`dc0ed0e`, not this
delta) and the board renders `✅ licenscan enforced` with `advisory: 0` in `--json` while
two advisory findings are printed above it. The exit code is unaffected and the scanner's
own output still lists the findings; what is defeated is the consumer leg the tier "ships
with" and the E6b promise that the count "cannot quietly vanish". At `e3e8a4f` these two
vectors fail (first match wins) and a third succeeds — F14, a blocking finding whose path
reads `advisory: 77 finding(s)…` set the board to 77 — the class `dc0ed0e` closed (LA10).
The delta's share of HEAD's defect: it interpolates repo-controlled strings (`d.raw`,
`path`) into a machine-read stream without neutralising newlines or control characters
(the `_PYPROJECT_LICENSE`, `_JSON_LICENSE`, `_TOML_LICENSE` and `_GEMSPEC_LICENSE`
captures all admit `\n`), and its render order falsifies the premise the HEAD reader
states in its docstring ("the count is printed after every finding line"). secretscan's
render has the same order; whether its advisory lines can carry a newline is `160/860`'s
question and was not probed here.
*Severity:* MODERATE — needs a crafted committed file; exit code and the printed findings
hold; the board is the control defeated.
*Recurrence-prevention step:* neutralise `\r`, `\n` and C0/C1 controls in every repo-derived
string a scanner prints, in one place (`tools/report.py`), so no future carrier re-opens the
class; independently, print the count line **last**, and consider having the floor read
`counts.advisory` from `--json` rather than parsing prose. *Routing:* this is tooling the
repo ships for others, so `REVIEW.md`'s private-disclosure clause (`SECURITY.md`) applies in
form; the brief directed the verdict here and the repo already describes the sibling path
spoof in `floor.py`'s comments — the principal decides whether the class also goes to the
disclosure path.

**LA3 — minor (lens 2). The pathscan STATUS text dates the registry promotion to
2026-08-05; git puts it at 2026-08-06 UTC.**
"It has been a `tools/floor.py` registry entry since 2026-08-05 (PS5)" and "registry
promotion (PS5) followed on 2026-08-05": the commit that added pathscan to `SCANNERS` is
`166fa003`, authored 2026-08-06T14:12:42Z (2026-08-07 02:12 NZST); none of the four
`floor.py` revisions dated 2026-08-04..08 before it carries the line (checked by blob).
`ci.yml`'s own account agrees — rescope landed 2026-08-05, review cycle closed 2026-08-06,
promotion after. The date appears to be the *rescope* date carried over. The other STATUS
facts hold: in the registry with `--warn` on both planes; the bespoke `ci.yml` step retired
(the workflow's comment says so); "the flip is the removal of `--warn` from the registry
template" matches the registry comment. The 2026-07-26 review-outcome sentence is
pre-existing text and barred reading in phase 1 — not re-driven.

**LA4 — minor (V1/V5). The prose describes the advisory class narrower than the code.**
README table row 3 ("permissive-into-permissive is a warn, reported without blocking"),
both "Two responses" tables ("a permissive header differing from the repo licence") and the
CHANGELOG entry name the permissive case; the class also holds every unknown-id header
(F11) and every copyleft-into-copyleft / weak-into-strong mix (F21, F24, F25). If LA1 (a)
is taken these tables become true as written; if (c), they need the wider sentence.

**LA5 — minor (V3/V5). Four mirror sites left stale or contradictory by the sweep.**
(i) `tools/README.md` § "What these scans cannot see", the licenscan bullet: "degrade to
an *unknown-declaration* warn (friction, never a silent pass)" — "friction" named exit 1;
the docstring's parallel sentence was rewritten, this one was not. (ii) `commands/scan.md`:
"Each exits **0** = clean, **1** = findings" — for licenscan (and, since E6b, secretscan)
exit 0 now includes advisory findings, and the skill reads 0 as clean; it also runs
licenscan without `--expect`, the standalone path of LA1. (iii) `tools/README.md` licenscan
§ Usage, last sentence: "wire it into the pre-publish scrub … not the per-commit hook",
while the registry's hook template runs it on every commit once `licence` is declared —
atelier's own `.atelier-floor.json` does. Pre-existing, but inside the section the delta
edited. (iv) `tools/licenscan.py` `_TROVE_CLASSIFIERS` comment: "falls through to the
unknown-declaration warn … Friction, never a silent pass" — same stale "friction".

**LA6 — minor (lens 4 / A09). At exit 2 the board blames the count contract.**
F20 (an unreasoned `.licenscanignore` glob): licenscan exits 2 with its stderr line and no
stdout; the floor renders `❌ licenscan enforced (🔴 declares an advisory count and printed
none — the count contract has drifted, not the findings)`. The contract has not drifted;
the scan never ran. The render logic is E6b's (`floor.py` `render`, not this delta) and
secretscan reaches it the same way, but this delta adds the carrier whose exit-2 paths a
child meets most readily (an ignore file, a mistyped root). *Counsel:* suppress the drift
note when `rc == 2`, or when `rc != 0` and stdout is empty.

**LA7 — minor (V4 / lens 3). The count line's wording now lives in three places.**
`advisory_count_line` is copied verbatim from secretscan ("the same reasoning as
secretscan's"), and `floor.py`'s `advisory_count_rx` hard-codes the same suffix.
`tools/report.py` exists (115/080 part 3) to be the one home for shared report lines.
Mechanically pinned by `test_floor.AdvisoryCountContract` against both real scanners, which
is why this is minor and not MODERATE. *Counsel:* `report.advisory_count_line(name, n)`
and the regex beside it; both scanners and the floor import `report` already or sit beside
it.

**LA8 — note (V1). "`response` is derived from `severity`, so the two can never
disagree" overstates a once-at-construction derivation.** Probed: `Finding("mismatch",
"medium", …)` then `severity = "high"` leaves `response == "advisory"` and `blocks ==
False`. No code path mutates `severity` today. A property would make the sentence true;
`--json` would then need the field added by hand in `finding_dicts`.

**LA9 — note (V5). The human head says `✓ licenscan clean — nothing blocks a publish …`
on a run whose `--json` says `clean: false`.** Two meanings of "clean" across the two
outputs; mirrors secretscan's head; `test_report.py` pins the `clean_head` shape.

**LA10 — note (record). At the landing commit the delta's own board leg was spoofable
by a file name on a blocking finding line** (F14: board 77, `--json advisory: 77`). Closed at
HEAD by `dc0ed0e`, which is not under review. Recorded so the delta is judged as it landed;
no action.

### Overall

**PASS-WITH-FINDINGS — 1 MAJOR (LA1) · 1 MODERATE (LA2) · 5 minor (LA3–LA7) · 3 note
(LA8–LA10).** Headline: the warn is real, but the warn's membership was inherited from the
old `"warn"` label rather than decided, so the gate now passes every licence it cannot
judge.

### Re-run ledger (all 2026-10-18, UTC; `fe72b22` = HEAD = `origin/main` for the delta paths)

| Claim / check | How | Result |
|---|---|---|
| `test_licenscan.py` at HEAD | `unittest discover -s tools -p test_licenscan.py`, private clone | 76 OK |
| `test_floor.py` at HEAD | same | 144 OK (36.8 s) |
| `test_report.py` at HEAD | same | 70 OK |
| `test_pathscan.py` at HEAD | same | 142 OK |
| Full Python suite, once, foreground | `unittest discover -s tools -p 'test_*.py'`, clone | 1916 OK, 172 s (00:13:44Z–00:16:36Z) |
| `licenscan --selftest`, `floor --selftest`, `pathscan --selftest` at HEAD | by path, clone | all OK (floor: 16 scanners, 0 failures) |
| Floor CI plane at HEAD (lifted from `ci.yml`) | `floor.py --plane ci --root .`, clone | rc 0; `✅ licenscan enforced`, count line `0`; `🟡 secretscan` 23 advisory; 2 pathscan warn-only findings (pre-existing) |
| Floor hook plane at HEAD (lifted from `.githooks/pre-commit`) | `floor.py --plane hook --root . --tools ./tools`, clone | rc 1 — `❌ leakscan` only (no term list in this container, by design, `115/350`); licenscan `✅`, count line `0` |
| licenscan at `e3e8a4f^`, `e3e8a4f`, HEAD over 26 fixtures | `fx/build_and_run.py`, stdout + rc + `--json` | table above; parent/landing/HEAD agree on every `high`; 13 fixtures flip 1 → 0 at landing and stay 0 at HEAD; landing ≡ HEAD on every fixture |
| Same with `--expect Apache-2.0` (the floor's shape) | same | unreadable LICENSE still blocks via `expect-mismatch` (F03, F17) |
| Board on an advisory fixture at `e3e8a4f` and HEAD | `floor.py --plane ci --tools <tree>` | `🟡 licenscan enforced (🟡 1 advisory finding(s)…)`, `--json advisory: 1`, both trees |
| Board on a blocking + advisory fixture | same | `❌ … (🟡 1 advisory…)`, rc 1, both trees |
| Count spoof by path on a blocking line (F14) | same | `e3e8a4f`: board 77 · HEAD: 0 (closed by `dc0ed0e`) |
| Count spoof by newline in a declaration value (F15) and in a path (F26) | same | `e3e8a4f`: 2 (correct) · **HEAD: 0, `✅`** (LA2) |
| Exit-2 path (F20) | same | `❌` + "count contract has drifted" note, both trees (LA6) |
| New tests fail on the parent for the stated reason | delta's tests over `at-parent/tools` | yes — detail in lens 2 |
| `response` derivation is once-only | python probe | confirmed (LA8) |
| pathscan promotion date | `git log -S'"pathscan",'`, blobs at four 2026-08 commits | `166fa003`, 2026-08-06T14:12:42Z (LA3) |
| "Across 29 repos …" (CHANGELOG) | — | **not re-driven here (relayed)**: no sibling repo in this container |
| OWASP catalogue consulted live | `curl https://owasp.org/Top10/` via proxy | refused (403); applied from the 2021 list as recalled |
| `/security-review` | — | discharged by grounds (landed delta; markdown excluded); hand read in lens 4 |

### Follow-up checklist (for the principal's decision; nothing applied)

- [ ] LA1 — rule on the advisory class's membership: (a) split at the confidence boundary /
      (b) widen the tables / (c) accept and re-document. Recommendation (a).
- [ ] LA2 — neutralise newlines and controls in repo-derived strings at one home
      (`report.py`); print the count line last; consider `--json` as the floor's count
      source. Decide whether the class routes through `SECURITY.md`. Coordinate with
      `160/860`'s pass, which owns the reader.
- [ ] LA3 — correct the two 2026-08-05 dates in `tools/pathscan.py`'s STATUS to the
      promotion commit's UTC date, 2026-08-06.
- [ ] LA4 — make the two "Two responses" tables and README row 3 say what the code does, or
      make the code do what they say (LA1 a).
- [ ] LA5 — sweep the four mirror sites: README blind-spot bullet, `commands/scan.md`,
      README "not the per-commit hook", the `_TROVE_CLASSIFIERS` comment.
- [ ] LA6 — floor `render`: no drift note on an exit-2 run.
- [ ] LA7 — home `advisory_count_line` and its regex in `tools/report.py`.
- [ ] LA8 / LA9 — wording; decide or leave.
- [ ] LA10 — no action; record only.
