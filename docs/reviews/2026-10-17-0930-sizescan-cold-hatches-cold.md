# Cold pass — no hatch silences sizescan's cold-content gate, and the gate lists the items

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-17 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/790-rule-4-cold-pass-queued-sizescan-cold-content-hatches.md`.
**Why it earns a review:** `sizescan --check` runs on both floor planes in this repo and in every
child. The delta removes every exemption from its cold-content gate, makes a `.sizescanignore`
glob stop skipping hot-path files, and adds a per-item listing with a run-wide cap. A guard is
doctrine by function (rule 3), and this one changes what every child's commit can pass.

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
  bodies** (the author's own account, including a blast-radius measurement); the subjects and
  `--stat` of later commits on the same files; `REVIEW.md` rules 1–4; three user-local
  templates — the ask halves of the 2026-10-16 expected-toolbox and scanner-rule-gates briefs and
  the whole expected-toolbox sibling, seeded questions included (another pass's framing); HEAD
  greps of `tools/sizescan.py`, `tools/floor.py`'s registry, `.sizescanignore`, and short HEAD
  excerpts of `docs/method/GUARDS.md` and `RECORD.md`; the commissioning item's head line;
  filename-level greps of `docs/reviews/` (no file there opened); and its harness-loaded memory
  index and instruction files (one-line notes, some about the guards' history and how children
  receive scanner changes). It did not open the intent record, `docs/SESSIONS.md`,
  `docs/sessions/`, `docs/ROADMAP-DONE.md` or any file under `docs/reviews/`. Its orchestrator
  passed it an instruction set and no evaluative content about the delta; what the orchestrator
  read is its own to disclose in its claim. Everything evaluative is in the sibling.

## What the work is

Landing commit and merge (diff the commit; review the paths at HEAD, `8acfff1` or later):

- `f9ccba8` (2026-10-16 08:09 UTC) — sizescan: no hatch silences cold content, and the gate
  names the items (115/270); landed in merge `ccfad42` (2026-10-16 08:12 UTC)

Delta paths: `tools/sizescan.py` (the module docstring's hatch section, `ALLOW_MARKER`'s comment,
`FINDING_KINDS`'s comment, `_TITLE_CHARS`, `_COLD_LEAD`, `MAX_MATERIALIZED_FINDINGS`, `ColdItem`,
`_item_title`, `Finding.cold_listed` and `cold_hatches`, `_scan_file_metrics`' item slots,
`iter_candidates`' `evaluate_ignored`, `_cold_hatches`, `scan_paths`, `_suppression_line`,
`render_human`, the `--json` fields, the selftest), `tools/test_sizescan.py`,
`tools/test_report.py` (two line pins and the finding-ID round trip's `unexemptable`),
`tools/pointerscan.py` (one docstring heading) and `tools/README.md` (the sizescan section).

**Later commits on the same files — not this delta; do not attribute them to it.** The first
rewrote much of `sizescan.py` on top of this delta (`_cold_hatches` became `_inert_hatches`,
among others). Review the delta as it landed, then say which of its parts are live at HEAD and
whether any later change altered their behaviour.

- `72a68cc` (2026-10-16 15:28 UTC) — sizescan: remove the size advisory, and name the hatches it
  leaves inert (115/270 c); merged in `da85210` (its own pass, 160/850)
- `39a74b9`, `1c24781`, `f4afb7a`, `e3e8a4f` (2026-10-16) — touch `tools/README.md` or
  `tools/test_report.py` outside this delta's hunks (160/800, 810, 830, 840)

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests and live
behaviour. The lenses organise it; they do not bound it. Non-goals are the only narrowing and
are themselves reviewable.

Probe, at least:

- **Every hatch against every file class, at landing.** Hatches: an unscoped `sizescan:allow`
  header, each scope (`cold-content`, `size-advisory`, `harvest-integrity`, an unknown scope), a
  marker with no reason, a marker past the header window, a `.sizescanignore` glob. File classes:
  a metered hot-path file with and without `[x]` items, an archive store, a root-only file outside
  the root. For each, at `f9ccba8^` and at `f9ccba8`: gated or not, advisory or not, what the
  report and `--json` say, and which suppression count moves.
- **What `evaluate_ignored` now reads.** Which files were skipped before and are read now; the
  repo's own `.sizescanignore` entries and what the gate does with the files they match at HEAD;
  how the scanner's file walk and the glob interact.
- **The listing and its cap.** The run-wide slot budget across files and argument order; the
  true count against the listed count; the over-cap line and the `cold_items_over_cap` field;
  the 60-character title, the 85-column claim, multi-byte and control characters in an item's
  text as printed; the unbalanced-fence second pass.
- **The suppressed line.** `files_by_glob` now counts differently; say what the number means at
  landing and at HEAD, and whether two runs stay comparable (`GUARDS.md` rule b).
- **The principal's words.** Separate the quoted ruling in the module docstring from the code
  and wording around it; say where the surrounding text or the behaviour narrows, widens or
  re-reads it, and check the date the docstring gives it.
- **Reach.** `sizescan --check` is in `tools/floor.py`'s registry on both planes. Say how and
  when a child receives this change, and what a child that relied on a hatch now sees. Measure
  only in this repo and in scratch fixtures; never run a scanner over another repo.

**Non-goals:** the principal's ruling that no hatch exempts cold content and that the gate list
the completed items (quoted in the delta). Its encoding, the wording around it, the tests and the
behaviour are in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Ask whether a
   gate with no exemption at all fits `docs/method/GUARDS.md`'s exemption rules, and whether
   reading ignored files to gate them keeps the meaning of an ignore file.
2. **Correctness & quality.** Read `scan_paths`, `iter_candidates`, `_scan_file_metrics` and the
   new tests whole; diff `f9ccba8`. Record the hatch × file-class table from *Scope*. Check
   whether each new test fails on `f9ccba8^` and whether its fixtures were derived from the code
   or from the ruling.
3. **Completeness / harvest.** `tools/README.md`'s sizescan section; `docs/method/GUARDS.md` and
   `docs/method/RECORD.md` where they speak of sizescan or cold content; `CHANGELOG.md`; any
   template, skill or doc that tells a repo to use a hatch for a flat log; the finding-ID round
   trip in `tools/test_report.py`.
4. **Security & privacy** — mandatory. The listing now prints item text from tracked files into
   hook output and public CI logs: check terminal-control and escape sequences, length bounds and
   memory bounds on adversarial input. Build counter-examples from synthetic values only.
   `/security-review` is discharged by grounds (a landed delta; the pending diff is not the work)
   — say so, and deliver the code-altitude read by hand against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest tools.test_sizescan tools.test_report -v`; `python3 tools/sizescan.py
  --selftest`; `python3 tools/pointerscan.py --selftest`
- `python3 tools/sizescan.py --check --root . .` and the same with `--json`, exit codes read
  explicitly
- the hatch × file-class table, driven at `f9ccba8^`, `f9ccba8` and HEAD in a scratch clone over
  synthetic fixtures, comparing stdout, stderr and exit code
- the cap, driven with a synthetic tree whose completed items exceed it across several files
- the floor on both planes at HEAD; the full Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only git is fine.
  Probes and older checkouts go in a private clone under your session scratchpad, named by your
  prefix. Never open another `docs/reviews/2026-10-16-*` or `docs/reviews/2026-10-17-*` file — it
  is another pass's framing.
- One heavy process at a time on a shared machine: the full suite at most once, in the
  foreground; fixtures sized to finish in minutes, under `nice`. Never point a scanner at any
  other repo on the machine.
- `/security-review` reads the session's pending diff: discharge it by grounds for this landed
  delta, or keep the tree clean whenever you spawn it.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ English. Never quote
  a secret, placeholder token, email address or personal detail — this repo is PUBLIC; describe
  and locate instead.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer, this brief's sibling
`docs/reviews/2026-10-17-0930-sizescan-cold-hatches-cold.deferred.md`, the landing commit's and
merge's message bodies (read subject, stat and diff only), and the commissioning item `270` in
`docs/roadmap/115-guardrail-architecture-mike-commissioned/`.

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/790-rule-4-cold-pass-queued-sizescan-cold-content-hatches.md
--also-exclude docs/reviews/2026-10-17-0930-sizescan-cold-hatches-cold.deferred.md
--also-exclude
docs/roadmap/115-guardrail-architecture-mike-commissioned/270-three-defects-found-adding-finding-ids.md
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then append your
verdict below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier,
what you read), per-lens answers, the standing checklist V1–V7 each answered or discharged with
grounds, the hatch × file-class table, findings with stable IDs (prefix `HX`: `HX1`, `HX2`, …)
and severities (MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line
with counts, a re-run ledger, and a follow-up checklist. Then STOP and commit phase 1 unrevised
before opening the sibling.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict: per-finding notes
against the seeded questions and the intent record, any finding formed at reconcile marked as
such, and the overall line restated. Never revise phase-1 text. Then fold the sibling in below
the reconcile and delete it.

Findings on self-authored doctrine are the principal's to decide (rule 3; a guard is doctrine by
function): record all, apply nothing; counsel per finding is welcome, labelled and kept beneath
it.

---

# Verdict — phase 1 (cold, before the sibling)

**Written 2026-10-17 23:38 to 2026-10-18 00:01 UTC** (`date -u`; the verdict landed on disk at
00:00:53 UTC on 2026-10-18 and these wrap fixes a minute later), reviewer prefix `HX`. Review of
the paths at HEAD `0aff4d8` (= `origin/main`), the delta diffed as `f9ccba8^..f9ccba8`.

## Provenance (repeated, rule 4 / V7)

- **Reviewer model:** Fable 5.1 (`claude-fable-5-1`), the principal-named tier; checked at
  selection by the orchestrator and confirmed by this session before any read.
- **Spawn:** a Mike-opened Claude Code **cloud** session (`claude-fable-5-1`, orchestrating; it
  opened on `claude-opus-5` and Mike switched it to Fable before any claim or pass) dispatched
  this reviewer. That session authored none of the delta or this brief and was not started or
  instructed by their authors. The orchestrator forms no finding and writes no severity; it holds
  the `.deferred.md` sibling outside the checkout at a path not given to me, commits this phase-1
  file before releasing the sibling, and received one operational note from Mike's watching
  session (model, queue scope, container facts, merge instruction — no evaluative content about
  any delta). It sent this reviewer one further operational note mid-pass (the checkout had been
  unshallowed; re-run history steps) — no evaluative content. The queue pointer's claim line
  discloses the same shape; I have not opened the pointer.
- **Author of the work:** per the brief, a 2026-10-16 queue run (Opus orchestrator, dispatched
  worker; landing trailer names a Sonnet model, the merge an Opus model). Not opened; the
  commit bodies are phase-2 reading and were not printed (`git show --stat --format=%s` and
  `git diff <sha>^ <sha>` only; `git show <sha>:<path>` for blobs).
- **Container facts that bear on this verdict:** a cloud container with **one checkout, no
  worktrees, no sibling repos, no estate root**, no `~/.claude/`, no `gh`, no GitHub API from the
  shell, and **no outbound DNS for the OWASP/CWE hosts** (both fetch attempts failed). So: the
  CHANGELOG's 30-repo blast-radius claim and anything about children is *not re-driven here
  (relayed)*; the hook plane's leakscan reds by design (no user-local term list, board `115/350`);
  the catalogue check for lens 4 is **recalled, not consulted** (stated at HX2). The checkout was
  a **shallow clone (52 commits, graft root `c824287`) when this pass began**: the delta's commits
  existed as objects but `merge-base --is-ancestor` and `log <sha>..HEAD` misfired; snapshots were
  taken from the object store with `git archive`. After the orchestrator's note the checkout was
  unshallowed (1779 commits) and every history step was re-run and reproduces; the snapshots were
  diffed against the commit blobs and are byte-identical (re-run ledger, item 17).
- **Worktree:** none. Work was done read-only in the shared checkout
  `/home/user/atelier` (branch `claude/review-work-briefs-adj6ad`); every probe, snapshot and
  fixture lives under `/home/user/scratch/HX/`. No git command that writes was run in the
  checkout. This brief is the only file edited.
- **What I read:** `REVIEW.md` rules 1–4, lenses, V1–V7 and the re-run section; this brief;
  `00-APEX.md` once; the delta diff on all five paths; `tools/sizescan.py` at HEAD whole and the
  `f9ccba8^`/`f9ccba8` snapshots (the `scan_paths` archive branch and `SIZE_REFERENCE` at
  landing); `tools/test_sizescan.py` at HEAD whole and at `f9ccba8`; `tools/test_report.py`'s
  sizescan pins and the finding-ID round trip (both versions); `tools/allowmarker.py` whole;
  `tools/filewalk.py` and `tools/report.py` excerpts; `tools/floor.py`'s `Scanner`/`Advisory`/
  `Scope` dataclasses, the sizescan registry entry, the `Config` validation and the selftest's
  soften/re-baseline pins; `tools/test_floor.py` sizescan lines; `tools/pointerscan.py`'s
  docstring; `tools/coldsweep.py`'s docstring; `tools/board.py`'s render of done items;
  `docs/method/GUARDS.md` whole; `docs/method/RECORD.md` lines 50–75 and 225–290;
  `tools/README.md` lines 675–775 (HEAD); `CHANGELOG.md` lines 36–110 (unbarred, but note: this
  includes the author run's own entry for `115/270` a–b, read before the probes ran — the
  blast-radius sentence is the one claim it seeds); `.atelier-floor.json`; `.sizescanignore`;
  `.gitignore` (worktree lines); `.githooks/pre-commit`; `.github/workflows/ci.yml` (first 200
  lines) and `floor.yml` (lines 80–115); `docs/build/templates/workflows/floor.yml` lines
  30–100; `docs/build/templates/docs/ROADMAP.md`; `docs/ROADMAP.md` (the generated index, lines
  1–40);
  and one unbarred board item that a sweep hit, `docs/roadmap/110-…/100-two-granularities-…md`
  lines 105–135 (an exception audit; it names `sizescan:budget`, not this delta).
- ⚠️ **Exposure, disclosed.** Four `tools/coldsweep.py` runs with the brief's three
  `--also-exclude` paths (patterns: the hatch spellings; flat-log phrases; `2026-10-05`; a
  fragment of the quoted ruling). The `2026-10-05` sweep printed one-line hits from board items
  under `docs/roadmap/{020,030,110,115,130,160}/…` (not `115/270`, not `160/790`); the one from
  `115/330` quotes the "Remove it" ruling of 2026-10-16 (the later commit's, not this delta's). No
  `docs/reviews/*`, `docs/sessions/*`, `docs/SESSIONS.md`, `docs/ROADMAP-DONE.md`, the pointer,
  item `270` or the sibling was opened. No `--include-barred`. `/security-review` was not run
  (discharged by grounds, lens 4).

## Lens 1 — approach and assumptions

**Load-bearing assumptions, named first and then attacked:**

1. *"A hatch that cannot exempt should be accepted and named, not refused."* The delta reads a
   `sizescan:allow` or a `.sizescanignore` glob, lets it stand, and prints that it did nothing
   (landing: "present — it cannot exempt cold content"; HEAD: "present and inert"). The
   alternative GUARDS.md names for a state a scanner does not offer is a **config error** (floor
   doctrine: "Asking for an advisory state a scanner does not offer is an error, not a silent
   downgrade"). Accept-and-name is defensible — a refusal would red every child carrying a stale
   marker on a clean board — but it is a choice, and it leaves the ignore file meaning something
   other than "ignore" for one kind (**HX3**).
2. *"Nothing silences the cold-content gate."* True at the scanner (every marker spelling and the
   glob, verified in the table). **False at the plane the gate runs on**: `floor.py` gives
   sizescan an `advisory` form (drop `--check`), its selftest pins that sizescan "can
   re-baseline", a child may `disable` it with a reason, and the child `floor.yml` template tells
   an adopter to "declare the hygiene checks advisory in `.atelier-floor.json` while you do". A
   repo in that state runs a flat running log past a reporting-only gate — the state the quoted
   ruling forbids — and the delta's docstring, README and CHANGELOG do not name the lane
   (**HX1**).
3. *"Reading an ignored file to gate it keeps the meaning of an ignore file."* It does not, and
   the governing doctrine was not swept: GUARDS.md § *Granularity* lists the ignore-file glob as
   the path-level mechanism for every guard, § *Acceptance* calls "an ignore-file glob for a
   scanner's own test fixtures" a legitimate acceptance, and `allowmarker.load_ignore_globs`
   describes a glob as "the widest allowance a scanner grants — a whole path, every rule,
   indefinitely". For sizescan's cold-content kind none of that holds now; a tracked fixture
   `ROADMAP.md` carrying `[x]` lines has no acceptance at line, glob or scope level (**HX3**).
4. *"The gate encodes the ruling."* The gate detects completed `[x]` list items, outside balanced
   fences, in files named `ROADMAP.md` (root or anywhere not under a store-named or non-content
   directory), among tracked and untracked-not-ignored files. That is **narrower than the
   ruling's words** ("I don't want any of my repo's to run a flat running log"): a running log
   under any other name, or as prose under open items, is outside it. The docstring says so
   plainly ("Cold content is looked for in `ROADMAP.md` only"; prose-shaped cold content "caught
   at review, never measured"), so the narrowing is declared, not hidden. Where the surrounding
   text **widens** the ruling is the "Nothing silences…" heading (HX1). Two silences the text
   does not count as hatches: a `ROADMAP.md` under `archive/`, `intake/`, `sessions/`… is skipped
   unread and unnamed (a scope decision in the docstring, but not on the suppressed line — rule b
   asks that a scope reduction be named), and a gitignored one is never walked (correct: it
   cannot be committed). Under the split board the generated index renders done items as `✅`,
   never `[x]` (`board.py`), so the gate can only fire on a monolithic board — consistent with
   the ruling's "new method" clause: the gate is the nudge toward the split.
5. *"Does a gate with no exemption fit GUARDS.md?"* Yes, conditionally: GUARDS § *The fourth
   requirement* allows forbid-the-act **if declared**. The delta declares it in the module
   docstring; the eventual home GUARDS names (the registry `why`, beside the cheap-failure /
   forbid-the-act slot once `115/120` lands) still reads "current-truth files stay honest;
   archive stores hold no live state" and carries no such declaration. The remedy is lossless
   (harvest), so the failure the gate forces is cheap either way.
6. *The brief's own framing* ("the delta removes every exemption from its cold-content gate") is
   the author-side account of scope: it is true of the scanner's two mechanisms and silent on the
   floor's (HX1). Its re-run line for the test modules is unrunnable as written (HX6).

## Lens 2 — correctness and quality

The mechanism does what the delta says for marker and glob, at landing and at HEAD, across the
table below; the gate's exit contract is unchanged; the listing is correct by line and text,
including fenced lines, the unbalanced-fence second pass (items re-listed from pass two only),
ordered and `+`/`*` bullets, nested items, and the empty-text sentinel. The cap holds run-wide
and the true count survives it (probe: 60,003 items across three files → 50,000 listed, 10,003
counted, `cold_items_over_cap` 10,003, exit 1, 0.7 s, ~43 MB RSS at both landing and HEAD).

**Red before, green after.** The landing test file (87 tests) run against the pre-delta tools:
10 failures and 9 errors, all in `Hatches`, `ColdItemListing` and `ScopedMarker` — exactly the
tests the delta added or changed; against the landing tools: 87 OK. The two `test_report.py`
pins fail on pre-delta and pass at landing. At HEAD, from `tools/`: 160 OK; full suite 1916 OK.
**Fixtures:** the behavioural assertions (gated, counts, exit codes) follow the ruling; the hatch
strings (`".sizescanignore glob"`, `"… header (unscoped)"`) follow the code — acceptable for
report wording, and they would catch a silent rename. Two gaps: no test drives the listing with
control characters (HX2), and the "85 columns" test measures code points (HX5).

**What is live at HEAD, and what the later commit changed.** `tools/sizescan.py` and
`tools/test_sizescan.py` at HEAD are byte-identical to `72a68cc` (115/270 c, its own pass
`160/850`). Live from this delta unchanged: `_TITLE_CHARS`, `_COLD_LEAD`,
`MAX_MATERIALIZED_FINDINGS`, `ColdItem`, `_item_title`, `Finding.cold_listed`/`cold_hatches`,
`_scan_file_metrics`'s item slots, `iter_candidates`'s `evaluate_ignored` (same body), the
listing and over-cap lines in `render_human`, the `--json` fields `cold_listed`, `cold_hatches`,
`cold_items_over_cap`, the `test_report.py` `unexemptable` round trip, and the `pointerscan.py`
heading. Changed by `72a68cc`: `_cold_hatches` became `_inert_hatches` (now names every
non-exempting hatch on every hot-path file, plus a leftover `sizescan:budget`); the hatch note
reads "present and inert"; `files_by_glob` counts archive stores only and `files_allowed` counts
only a marker that exempts an archive store, with everything else moved to a new "inert
hatch(es)" tally (this resolves HX4); the size advisory, `reference_for` and `_STORE_HINT` are
gone, so "a glob quiets the size advisory" is no longer a behaviour. The README and CHANGELOG at
HEAD describe the HEAD behaviour and match the code line for line where I checked (note wording,
JSON fields, cap wording). `docs/method/RECORD.md` mentions the gate and the 2026-10-05 ruling on
size limits but carries no statement about hatches (fine: one home).

**The principal's words.** The quoted ruling (module docstring, landing and HEAD) is dated
2026-10-05; the CHANGELOG entry for this delta and `RECORD.md` give the same date for the same
day's rulings. The primary record (`115/270`) is barred until phase 2; checked there. The code
reads the quote's "it" as *an exemption for cold content* — the question the pre-delta docstring
invited ("For a repo that deliberately keeps, say, a flat session log") — which is the natural
reading. See lens 1 item 4 for where the encoding narrows and where the prose widens.

**The suppressed line (brief's question).** Landing: `files_by_glob` = archive stores skipped
+ hot-path files the glob matched *whether or not they were then gated*; `files_allowed` = every
reasoned marker, exempting or not. HEAD: `files_by_glob` = archive stores skipped only;
`files_allowed` = markers that exempted an archive store; a new `inert hatch(es)` part carries
the rest. Pre-delta `files_by_glob` was always 0 (the counter was never incremented — verified;
the CHANGELOG says so). Same tree, same label, three numbers across the three versions, so runs
either side of 2026-10-16 08:12 and 15:28 UTC do not compare (HX4); runs on one version do.

**Reach (brief's question).** Children do not vendor the tools (ADR 0008). CI: the child
template floats `uses: …/floor.yml@main` and the reusable workflow checks atelier out at
`atelier-ref`, default `main` — so every child's CI ran this delta on its first push after the
merge at 2026-10-16 08:12 UTC, with no child action. Hook: when the machine's atelier clone
(`hooks.atelierTools` / `ATELIER_TOOLS`) is next updated. A child that relied on an unscoped
`sizescan:allow` or a glob over a `ROADMAP.md` with `[x]` items goes red on that commit and push
with the items listed and the hatch named; its lanes are harvest, or the floor `advisory` (HX1).
The CHANGELOG's "no exit code changes in any of 30 repos" is the author's measurement — relayed.

**Walk and glob.** `filewalk` enumerates `git ls-files --cached --others --exclude-standard` in
a work tree, so a gitignored path is never a candidate and a linked worktree (a `.git` *file*)
is pruned. This repo's one `.sizescanignore` entry (`.claude/worktrees/**`) is therefore reached
by neither version — gitignored and pruned — which is why `sizescan --check --root . .` prints
`0 file(s) by .sizescanignore · 0 inert hatch(es)` at HEAD rather than naming it inert. Outside a
work tree `os.walk` order decides which items fall past the cap (probe: `b/`, `a/` listed before
`docs/` under one path argument); inside one, `ls-files` order (sorted) makes it deterministic.

## Lens 3 — completeness and harvest

- `tools/README.md`: swept at landing and again at HEAD; matches the code. `CHANGELOG.md`:
  swept (two entries). `GUARDS.md` and `allowmarker.py`'s ignore-file docstring: **not swept**
  (HX3). The registry `why`: not updated (lens 1 item 5, folded into HX1's counsel).
- No template, skill or doc tells a repo to use a hatch for a flat log (sweep: the hatch
  spellings outside `tools/` occur only in `CHANGELOG.md` and the `110/100` audit). The child
  `ROADMAP.md` template is a sizescan candidate (its directory parts are not store names) and
  carries no `[x]` line — clean at HEAD by `--json`.
- The finding-ID round trip in `test_report.py` gained `unexemptable=("cold-content",)` and
  asserts the ID survives the marker while the archive-store ID still clears — correct at
  landing and HEAD (probe rows and the 160-test run).
- The floor-level softening lane for sizescan predates the delta (C1, ruled 2026-07-28) and was
  not revisited by it — the completeness gap behind HX1.
- A seventh local copy of `MAX_MATERIALIZED_FINDINGS = 50_000` where `report.py` already takes
  the cap as a parameter (HX7, V4).

## Lens 4 — security and privacy

**`/security-review`: discharged by grounds.** It reads the session's pending diff, which here is
the other reviewers' briefs, not this landed delta; and its exclusions bar markdown, so even a
targeted run would be definitionally empty on three of the five paths. Not run. **Catalogue
consultation: attempted and failed** — `cwe.mitre.org` and `owasp.org` both unresolvable from
this container. The class below is therefore **recalled**: OWASP Top 10:2021 A03 Injection,
CWE-117 (improper output neutralisation for logs) and CWE-150 (improper neutralisation of
escape, meta or control sequences); CWE-400/770 for the resource bound. Design altitude: the
delta exposes no new data (item titles are already public in a public repo's `ROADMAP.md`) and
collects nothing; its one new surface is **echoing tracked-file text into the hook's terminal and
the CI log**. Code altitude, probed with synthetic items at landing and HEAD (`probe_adversarial`):
ESC-led SGR, erase-line/cursor-up and OSC sequences, a C1 CSI byte (U+009B), backspace, BEL, DEL
and bidi overrides (U+202E) all reach the human report **verbatim** — `_item_title` collapses only
`str.isspace()` characters, which covers CR/TAB/VT/FF/FS–US/NEL and not these (**HX2**). The JSON
path is safe (`json.dumps` escapes). Length and memory bounds hold: a 100 KB single-line item is
truncated at 8 KiB on read and to 60 characters on print; the cap bounds held items (~43 MB RSS
at 60,003 items). No secret, personal datum or path outside the fixture trees was printed by any
probe; fixtures are synthetic.

## Standing checklist V1–V7

- **V1 — no claim stronger than its evidence.** Bites: "Nothing silences the cold-content gate"
  (HX1); "the same bound … derived there" (HX7); "a hatch is never silently ignored" (HX8).
- **V2 — re-run every live-proven claim.** Done; ledger below. One claim relayed, not re-driven
  (the 30-repo blast radius) — no sibling repos here.
- **V3 — swept to every mirror site.** README and CHANGELOG yes; GUARDS.md and the allowmarker
  ignore-file docstring no (HX3); registry `why` no (HX1 counsel). Templates carry no hatch text.
- **V4 — one fact, one home.** The ruling has one verbatim home (docstring) and paraphrases
  elsewhere — fine. The cap number has seven homes (HX7).
- **V5 — no internal contradiction.** HX1 (registry/template vs docstring), HX3 (GUARDS vs
  tool), HX4 (landing tally vs its own finding, resolved at HEAD).
- **V6 — security and privacy.** Run, above; HX2.
- **V7 — spawn provenance in brief and verdict.** Both present; the brief's provenance names the
  brief-writer's off-tier status and exposure, and this verdict repeats the reviewer's.

## Hatch × file-class table (re-driven; 108 trees, three snapshots)

Legend: `G` gate fires (exit 1 under `--check`) · `A` size advisory printed (exit 0) · `Aq`
advisory quieted · `N` hatch named on the finding · `I` named/counted inert · `X` exempt or
skipped, nothing printed · `–` never a candidate · `s1` counted "by sizescan:allow header" ·
`g0`/`g1` the "by .sizescanignore" count. Each cell is `pre→landing→HEAD`. Classes: hot
`docs/ROADMAP.md` (2 × `[x]` + 400 open lines), hot `docs/SESSIONS.md` (400 lines, no `[x]`),
archive `docs/ROADMAP-DONE.md` (one live `[ ]`). A fourth class, nested `sub/README.md` (a
root-only name outside the root), is `–` in every cell of every version and is omitted.

| hatch | hot ROADMAP.md | hot SESSIONS.md | archive store |
|---|---|---|---|
| none | G A→G A→G | A→A→X | G→G→G |
| unscoped header | X s1→G Aq N s1→G N I | X s1→X s1→I | X s1→X s1→X s1 |
| `:cold-content` | A s1 (gate off)→G A N s1→G N I | A s1→A s1→I | G s1→G s1→G I |
| `:size-advisory` | G Aq s1→G Aq s1→G N I | X s1→X s1→I | G s1→G s1→G I |
| `:harvest-integrity` | G A s1→G A s1→G N I | A s1→A s1→I | X s1→X s1→X s1 |
| unknown scope | X s1→G Aq N s1→G N I | X s1→X s1→I | X s1→X s1→X s1 |
| no reason | G A→G A→G | A→A→X | G→G→G |
| past the window | G A→G A→G | A→A→X | G→G→G |
| `.sizescanignore` glob | X g0→G Aq N g1→G N I g0 | X g0→X g1→I g0 | X g0→X g1→X g1 |

Reading it: the delta closes every marker spelling and the glob for cold content (column 1,
landing and HEAD all `G`); the glob keeps skipping an archive store (column 3, last row); a
reasonless or body marker is silently inert in every version (rows 7–8); at landing a
`cold-content`/`harvest-integrity` scope and a hot-file glob are counted as suppressions while
suppressing nothing or while the file is gated (HX4); at HEAD those become `I`. The nested
root-only file is never read, so a hatch there is invisible in every version.

## Findings

**HX1 — MODERATE — "Nothing silences the cold-content gate" is true at the scanner and false at
the floor, and the delta does not say so.** `tools/floor.py` registers sizescan with an
`advisory` form (`--root {root} {scope}`, "drop --check"); its selftest pins `sizescan can
re-baseline`; `Config` admits `disabled` for it with a reason; and
`docs/build/templates/workflows/floor.yml` tells an adopting repo to "declare the hygiene checks
advisory in `.atelier-floor.json` while you do". A child so declared keeps a flat running log
with the gate reporting only — the state the quoted ruling forbids — and nothing in the
docstring, `tools/README.md` or `CHANGELOG.md` names this lane; a reader is told nothing silences
the gate. The lane predates the delta (C1, ruled 2026-07-28; GUARDS § *Adoption*) and is
declared, reasoned, expiring and estate-visible, so it may well be the governed deferment the
doctrine intends — but that is a fork the delta resolved silently by not mentioning it (apex:
surface a genuine dilemma). *Why not MAJOR:* the mechanism built is correct for its two named
hatches and the floor lane is prior ruled design; the defect is the overclaim and the withheld
fork. The principal may weigh it higher.
*Counsel (reviewer's, for the principal):* (a) minimum — change the absolute to "no marker and
no ignore glob", and add one sentence naming the floor `advisory`/`disabled` lane as the one
declared, expiring way a repo can soften this gate, in the docstring and README; (b) if the
ruling's "never" is meant literally — move sizescan to the cannot-soften set (`advisory=None`),
with the registry `why` carrying the forbid-the-act declaration GUARDS asks for, and accept that
a child whose board already carries `[x]` items meets a first red whose remedy is lossless;
(c) keep `advisory` but require the `review-by` the new spelling already demands and have
`floorfleet` render a softened sizescan distinctly. I would take (a) now and put (b) to the
principal as the question the ruling leaves open.

**HX2 — MODERATE — the new listing echoes tracked-file text to the terminal and CI log without
neutralising control or escape sequences.** Probed with synthetic items at landing and HEAD: an
item carrying erase-line and cursor-up sequences prints as a line that, on a VT-style terminal,
visually removes the finding line above it; SGR colour, OSC (title-set), a C1 CSI (U+009B),
backspace, BEL, DEL and a bidi override (U+202E) all print verbatim. `_item_title` collapses only
`str.isspace()` characters. The `--json` path is safe. Reach: the hook plane scans the whole tree,
so one contributor's item renders in every other contributor's pre-commit output; CI runs on
`pull_request`. Impact is low — output spoofing; the exit code is unaffected — but the surface
is new to this delta and the brief named it. Class (recalled, not consulted — see lens 4):
CWE-117 / CWE-150 under OWASP A03. **Severity:** MODERATE. **Recurrence prevention:** neutralise
Unicode categories `Cc` and `Cf` (keeping the ellipsis) in `_item_title`, preferably as a shared
`report.safe_text()` so every scanner that echoes file content shares one neutraliser — none of
`report.py`, `secretscan`, `leakscan`, `linkscan`, `spellscan` or `pathscan` does so today, so the
class is estate-wide and this delta added one more echo path; pin it with a synthetic-ESC test.
Not a disclosure-path item: it alters nothing a tool decides, only what a reader sees.

**HX3 — MODERATE — reading an ignored hot-path file to gate it changes what `.sizescanignore`
means, and the governing doctrine was not swept.** GUARDS.md § *Granularity* lists the ignore-file
glob as the path-level mechanism for every guard; § *Acceptance* names "an ignore-file glob for a
scanner's own test fixtures" a legitimate acceptance; `allowmarker.load_ignore_globs` calls a
glob "the widest allowance a scanner grants — a whole path, every rule, indefinitely". After this
delta a glob over a hot-path file exempts the size advisory only (landing) or nothing (HEAD), the
file is read and gated, and the one acceptance case GUARDS names — a tracked fixture `ROADMAP.md`
with `[x]` lines — has no lane at line, glob or scope level; the two silences left (the floor
lane, HX1; a move under a store-named directory such as `archive/` or `intake/`) are not named as
hatches, and the directory skip is not reported on the suppressed line (rule b, "names any scope
reduction"). V3/V5: GUARDS.md and the allowmarker docstring still describe the old meaning.
*Counsel:* either (i) say in GUARDS.md that an ignore glob is a path acceptance for every kind
except one named kind, add the fixture remedy (fence the `[x]` lines, or name the file otherwise)
to the sizescan docs, and name the store-directory skip on the suppressed line; or (ii) make a
`.sizescanignore` glob that matches a hot-path file a config error (exit 2), the way an
unreasoned glob is — fail noisy at the declaration. HEAD's inert-naming is honest, so (i) is the
smaller change; (ii) is the one GUARDS' own floor wording points at.

**HX4 — minor — at landing the suppressed line counted things it had not suppressed; resolved
at HEAD by `72a68cc`.** Table rows: a `.sizescanignore` glob over a gated `ROADMAP.md` printed
"1 file(s) by .sizescanignore" beneath the gated finding on that very file; a `cold-content` or
`harvest-integrity` scope on a roadmap, which exempted nothing, printed "1 file(s) by
sizescan:allow header". Rule (b) asks the tally to count what was suppressed. The later commit
moved both to an "inert hatch(es)" part and narrowed `files_by_glob` to archive stores, so at
HEAD the tally is coherent. Comparability: same tree, same label, three numbers across the three
versions (pre 0 by a pre-existing bug the delta fixed and the CHANGELOG records; landing 1;
HEAD 0 + 1 inert) — runs across 2026-10-16 08:12–15:28 UTC do not compare; runs on one version
do. Record only; nothing live.

**HX5 — minor — "fits the house 85-column limit" is by code point, not display column.**
`_TITLE_CHARS` caps characters and `test_report_lists_every_item_within_85_columns` asserts
`len(ln) <= 85`; a 60-character CJK title renders at 137 columns (probe). `wrapscan` measures the
same way and says so, so this is the house convention and the README's "60 characters" is
accurate; the comment at `_TITLE_CHARS` and the test's name say "columns". Also theoretical: a
line number of nine or more digits pushes a full title to 86 even by code points. *Counsel:* say
"characters" in the comment and test name, or truncate by East Asian width; no behaviour change
needed.

**HX6 — note (on the brief) — the re-run line for the test modules is unrunnable as written.**
`python3 -m unittest tools.test_sizescan tools.test_report -v` from the repo root imports
`tools.test_sizescan`, whose `import sizescan` finds nothing on `sys.path` (`ModuleNotFoundError`,
verified); `test_report` runs because it adds `tools/` itself. The suite runs via `discover -s
tools` (CI) or from `tools/`. A reviewer following the brief verbatim reports a red that is not
one. For the brief-writers' checklist.

**HX7 — note — the cap is borrowed, not derived, and its bite here is output, not memory.** The
docstring says 50,000 is "the same bound every other scanner puts on the findings it builds
(… derived there)"; `leakscan` derives it from ~1 KiB per finding and a ~50 MiB budget, while
sizescan's own comment puts an item at ~100 B, so the shared number is a convention with a ~5 MiB
budget here. Memory holds (probe), but at the cap the human report is 50,023 lines / 1.9 MB into
the hook or CI log — bounded by the memory cap, not by any output bound. A seventh local copy of
the constant where `report.cap_part`/`over_cap_line` already take it as a parameter (V4,
pre-existing pattern). *Counsel:* reword "derived there"; decide whether a per-file listing bound
is wanted.

**HX8 — note — "a hatch is never silently ignored" has two by-design exceptions.** A marker with
no reason (GUARDS rule c) and a marker past the 15-line header window (F2) are silently inert in
every version (table rows 7–8); both are deliberate ("a mention, not a hatch"), and neither is a
hatch in the docstring's own definition, but the sentence reads as absolute. Say "no reasoned
header hatch". Related, trivial: an item whose text is literally `(no text)` prints identically
to an empty one.

**HX9 — note — the delta carries one unrelated hunk.** `tools/pointerscan.py`'s docstring
heading "TWO FAILURES, ONE PARSE" → "THREE FAILURES, ONE PARSE". The body already listed three
(the third added 2026-10-05, `130/020`), so the fix is right and is live at HEAD unchanged, but
it is outside the commit's subject and the brief's "what the work is" — commit-small hygiene.

## Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE · 2 minor · 4 note.** The mechanism does what it
claims for every marker spelling and the glob, at landing and at HEAD, and its tests are real
(red before, green after); the headline finding is that the absolute "nothing silences the
cold-content gate" is false at the floor, where a child may declare sizescan advisory or
disabled and the house template tells adopters to do so, and the delta neither says so nor
surfaces the fork (HX1). Findings on this guard are the principal's to decide (rule 3); nothing
has been applied.

## Re-run ledger

1. `python3 tools/sizescan.py --selftest` (HEAD) → `selftest OK`, exit 0.
2. `python3 tools/pointerscan.py --selftest` → `ok (0 failure(s))`, exit 0.
3. `python3 -m unittest tools.test_sizescan tools.test_report -v` from the repo root →
   `test_report` 71 OK; `test_sizescan` **ImportError** (HX6). From `tools/`:
   `python3 -m unittest test_sizescan test_report -v` → 160 tests OK, 12.9 s.
4. `python3 tools/sizescan.py --check --root . .` → clean, exit 0, tally `0 · 0 · 0 · 0`;
   `--check --json --root . .` → `clean: true`, `cold_items_over_cap: 0`, `inert_hatches: []`,
   exit 0.
5. Hatch × file-class table: 9 hatches × 4 classes × 3 snapshots = 108 fixture trees, each run
   twice (`--check`; `--check --json`); stdout, stderr (all empty), exit codes recorded
   (`/home/user/scratch/HX/table.out`). Table above.
6. Cap: 3 × 20,001 `[x]` items (60,003) at landing and HEAD, one path argument and three in a
   chosen order → listed 50,000, counted 60,003, `cold_items_over_cap` 10,003, exit 1,
   0.64–0.73 s, peak RSS 43–45 MB; over-cap line and tally part present; human output 50,023
   lines / 1.9 MB.
7. Adversarial listing: 13 synthetic items (SGR, erase/cursor, OSC, C1 CSI, BS, BEL, DEL, bidi,
   70 CJK, 100 combining, `(no text)`, empty, 100 KB line) at landing and HEAD → control and
   format characters pass through the human report (HX2); JSON escaped; widths as in HX5; exit 1.
8. Landing test file vs pre-delta tools (from `tools/`): 87 ran, **10 failures + 9 errors**, all
   in the delta's tests; vs landing tools: 87 OK. Landing `test_report` sizescan pins: 2 fail on
   pre-delta, 2 OK at landing.
9. Floor, CI plane: `python3 tools/floor.py --plane ci --root .` → exit 0; `sizescan ✅
   enforced`; 12.7 s. (pathscan warn-only reports one unrelated stale path in an ADR;
   secretscan 23 advisory.)
10. Floor, hook plane: `python3 tools/floor.py --plane hook --root . --tools tools` → exit 1,
    **BLOCKED by leakscan** — the user-local term list is absent in this container, by design
    (board `115/350`); every other check including `sizescan ✅`; 9.0 s. The CI plane is the
    honest plane here.
11. Full Python suite, once, foreground: `python3 -m unittest discover -s tools -p 'test_*.py'`
    → **1916 tests OK**, 182 s.
12. Instruments suite: **not run** — no instrument is in the delta and the brief did not list it.
13. CHANGELOG claims "no exit code changes in any of 30 repos" (this delta) and "28 advisory lines
    gone, 2 inert hatches named" (the later commit) → **not re-driven here (relayed)**: no sibling
    repos in this container. CHANGELOG claim "the `.sizescanignore` count … before always printed
    0" → **re-driven, true** (table, pre-delta glob rows).
14. The ruling's wording and date (2026-10-05) → unbarred echoes agree (CHANGELOG, RECORD.md);
    the primary record `115/270` is barred until phase 2 → **deferred to the reconcile**.
15. OWASP / CWE catalogue → two fetches attempted, both failed (DNS); the class is recalled and
    marked so (lens 4, HX2).
16. `/security-review` → not run; discharged by grounds (lens 4).
17. Git history: at start the checkout was shallow (52 commits); `merge-base --is-ancestor` on
    `8acfff1`/`ccfad42` and `log f9ccba8..HEAD` misfired. Snapshots were taken from the object
    store (`git archive f9ccba8^`/`f9ccba8`; HEAD from the tree). After the orchestrator's
    unshallow note (23:55 UTC): all six commits are ancestors of HEAD; `log f9ccba8..HEAD` on the
    delta files lists `72a68cc` (sizescan, tests) and `39a74b9`, `1c24781`, `f4afb7a`, `e3e8a4f`
    plus their merges (README, test_report), as the brief says; the merge `ccfad42` has parents
    `e8aa6f7 f9ccba8` and is faithful (empty diff to `f9ccba8` on the delta paths); all three
    snapshots diff empty against their commit blobs; `pointerscan.py` at HEAD equals `f9ccba8`.
18. `tools/coldsweep.py` × 4 with the brief's three `--also-exclude` paths; exclusion sets printed
    and disclosed above; no `--include-barred`.

## Follow-up checklist (for the principal's decision; nothing applied)

- [ ] HX1 — rule on the floor lane: wording fix (a), cannot-soften (b), or (c); registry `why`
      to carry the forbid-the-act declaration either way.
- [ ] HX2 — neutralise `Cc`/`Cf` in echoed text, preferably once in `report.py`; synthetic-ESC
      test; sweep the other echo paths as a class.
- [ ] HX3 — sweep GUARDS.md § *Granularity*/§ *Acceptance* and the allowmarker ignore-file
      docstring; name the fixture remedy; decide read-and-name vs config error; name the
      store-directory skip on the suppressed line.
- [ ] HX4 — record only (resolved at HEAD); CHANGELOG could note the relabel window.
- [ ] HX5 — "characters" in comment and test name, or width-aware truncation.
- [ ] HX6 — brief-writers: give the suite's real invocation (`discover -s tools`, or run from
      `tools/`).
- [ ] HX7 — reword "derived there"; decide on an output bound; consider one home for the cap.
- [ ] HX8 — "no reasoned header hatch".
- [ ] HX9 — note for commit hygiene; nothing to change.
- [ ] Phase 2 — check the ruling's date and words against `115/270`; verify the intent record's
      account against the table; reconcile with the sibling's seeded questions.

### Reconcile

**Written 2026-10-18 00:04–00:20 UTC**, after the orchestrator committed phase 1 as `7bbb5c2` and
released the sibling. Opened at this step, in this order: the sibling; the queue pointer
`160/790`; the commissioning item `115/270`; the message bodies of `f9ccba8` and `ccfad42`; the
intent record `docs/sessions/2026-10-16-0703-queue-run-after-the-sizescan-ruling.md`; the board
commit `fd63df8` (subject, body, stat); the session record that received the ruling,
`docs/sessions/2026-10-05-1120-queue-run-closes-and-builds.md` (its headings and close); the
prior verdicts the sibling names, by grep and short excerpt only (`2026-07-14-2048` F2/F3 and
`2026-07-20-2040` SR1), to reconcile, never to anchor; `docs/method/EVIDENCE.md` §13 whole. No
phase-1 text above is revised. Two findings are formed here and marked as such.

**Against the intent record and the commit bodies.** The author's account matches what the
table shows for the two mechanisms it names: marker and glob stop exempting cold content, the
hatch is named, items are listed, the `files_by_glob` zero was a pre-existing bug fixed inside
the delta (the body says "it now counts every ignored candidate" — which is the relabel HX4
records). Neither the record, the item, nor either body mentions the floor's `advisory`/
`disabled` lane or the ignore file's doctrinal meaning, so HX1 and HX3 are not pre-empted by the
author's framing and were not seeded by it. The item's history adds one fact that bears on HX1:
the question put to the principal offered "allow it, with a reason" or "never allow it" — the
floor lane was not in the account he ruled on, and he added, in the same answer, that he was
"not sure what other files / content sizescan is used for". Under `00-APEX.md` the ruling stands
and is open to challenge on the briefing, raised to him by re-briefing: HX1's counsel (b) is
that re-brief. The principal may weigh HX1 above MODERATE on that ground; its recorded severity
is not revised here. Genealogy worth one line: the "none of which silences the cold-content
gate" sentence that item `270` found contradicting the code was first written into the README by
a review-fix (SR1, 2026-07-20) while the code kept exempting — the prose outran the mechanism
once already on this exact sentence; HX1 is the same shape one plane up.

**Against the seeded questions.**

1. *Nested worktree `ROADMAP.md` under `.claude/worktrees/`.* Probed with a real git fixture in
   three variants at landing and HEAD (`/home/user/scratch/HX/probe_worktree.py`). (A) the real
   harness shape — gitignored and carrying a `.git` *file* — is never walked: clean, `0 file(s)
   by .sizescanignore`, `0 inert`, both versions. (B) `.git` file only, tracked: pruned by the
   linked-worktree skip, clean. (C) a plain nested directory, tracked, no `.git` file: **read
   and gated** (exit 1) at both versions — at landing with `1 file(s) by .sizescanignore` printed
   beneath the gated finding (HX4's shape), at HEAD with the glob named inert. So the repo's own
   `.sizescanignore` entry protects this repo's commit in no variant: the protection is
   `.gitignore` plus the `.git`-file prune, and the entry's comment ("lets another session's
   mid-flight tree gate this one's commit") describes a guarantee the glob no longer gives for
   `ROADMAP.md`. New finding **HX10** below.
2. *Slots spent and `cold_over_cap` charged before a file is dropped.* No, by construction at
   both versions: `_scan_file_metrics` counts cold items and fills slots only when the basename
   is in `COLD_CHECKBOX_FILES` (`ROADMAP.md`), so an archive store — blanket-marked or not — and
   every other hot-path file return `cold = 0`, `items = []`; and a `ROADMAP.md` with `cold > 0`
   always yields a finding (landing: `if cold or over`, and `reference_for` is never `None` for
   a basename in `SIZE_REFERENCE`, which `ROADMAP.md` is; HEAD: `elif cold:`). The cap probe's
   sums agree: 60,003 counted across the three findings, exactly 50,000 listed.
3. *`files_by_glob` claiming a suppression that did not happen.* Yes at landing — HX4, with the
   table rows; resolved at HEAD by `72a68cc`.
4. *The ruling's date.* The ruling was the "last device question" at the close of the queue run
   that opened 2026-10-05 11:20 UTC (its session record says so); the board commit that recorded
   it verbatim, `fd63df8`, is 2026-10-06 03:49 UTC. The item, the session record, the CHANGELOG,
   `RECORD.md` and the docstring all say 2026-10-05, so the house's records agree with
   themselves. Whether the device answer itself arrived before 2026-10-06 00:00 UTC no artefact I
   can read pins — the record gives no clock time for the answer — so I cannot say whether the
   date at rest is the UTC date `CONVENTIONS.md` asks for or the local one; the principal knows.
   Not a finding: consistent across every home, with one residual named.
5. *The README paraphrase beside the quote.* Two shifts. The paraphrase turns a want about the
   principal's repos ("I don't want any of my repo's to run a flat running log") into a universal
   ("no repo keeps a flat running log") — a widening on a public tool other estates adopt. And
   both the docstring's quotation and the paraphrase stop at "standalone file": the answer on the
   item continues with the declared uncertainty about what else sizescan covers, the
   fail-noisily sentence (built as part b) and the no-arbitrary-limits sentence (built as part c
   and quoted separately in the HEAD docstring). The omission that matters is the uncertainty
   sentence — the one that bears on HX1 and HX3's scope questions. Folded into HX1's reconcile
   note above; no separate finding.
6. *Exit-code-only blast radius versus `EVIDENCE.md` §13.* §13 does say it: "a scanner delta
   compares per-finding output, never totals — identical counts can hide one finding swapped for
   another (the principal's ruling, 2026-08-23)". The commit body compares exit codes over 30
   repos ("29 stay 0; 1 was already 1 under both"), a total of totals, and the one repo already
   red is precisely where a swap would hide. New finding **HX11** below.
7. *Escape sequences and bidi controls reaching the log.* HX2 — formed and probed before the
   sibling was opened; the sibling asked the same question. The house's answer, by its own lens-4
   rule, is yes: the surface is new, the fix is a line, and the class reaches every scanner that
   echoes tracked text.
8. *A template, skill or child-facing doc still teaching `sizescan:allow` for a flat log.* None
   found (lens 3; sweep). The 2026-07-14 origin verdict's F3 shows the hatch *was* designed for
   exactly that case (a child whose session log was "flat-by-declared-design"), so a child that
   still kept one would be the child this delta reds; the author's 29/30-repo measurement says
   none did at the time — relayed, not re-driven (HX11 on the measurement's rung).

**Overlap with sibling passes.** `160/850` (`72a68cc`) rewrote this surface the same day: HX4 is
this delta's and is resolved by that commit; HX1, HX2, HX3, HX5, HX7 and HX8 survive it unchanged
and therefore bear on `160/850`'s delta as well (HEAD's `sizescan.py` is that commit's); HX9 is
this delta's alone. `160/750` (`115/080`): the `covers` rule under which an unknown scope is a
blanket is what this delta names as a hatch and HEAD names inert — consistent. `160/730`:
`report.cap_part` and `report.over_cap_line` are called correctly; the cap *number* is each
scanner's own copy (HX7). The prior verdicts named in the sibling raise neither the floor lane nor
the ignore-glob meaning (grep), so HX1 and HX3 are new.

**Findings formed at reconcile.**

**HX10 — minor (formed at reconcile) — this repo's own `.sizescanignore` entry no longer does
what its comment says.** The entry `.claude/worktrees/**` is commented as the thing that stops a
sibling session's mid-flight `ROADMAP.md` from gating this repo's commit. Since this delta a glob
cannot stop a `ROADMAP.md` from gating (seeded Q1, variant C: read and gated at both versions);
the real protection is `.gitignore` plus `filewalk`'s `.git`-file prune (variants A and B), both
older than the entry's claim. At HEAD the entry is not even named inert, because the walk never
reaches a file it matches, so no run will ever tell a reader. An instance of HX3 in atelier's own
tree, and of V1 (a comment stronger than its mechanism). *Counsel:* reword the comment to say the
entry covers archive stores only and that `.gitignore` and the worktree prune are what keep a
sibling's tree out — or remove the entry.

**HX11 — minor (formed at reconcile) — the blast-radius claim stopped a rung short of the one
the doctrine names for a scanner delta.** `EVIDENCE.md` §13: "a scanner delta compares
per-finding output, never totals". The landing commit's body, the item and the intent record
compare exit codes over 30 repos, and the one repo "already 1 under both" is exactly where a
swapped finding — a hatch-exempted roadmap newly gated beside an already-gated one — would leave
the code at 1 and the claim intact. The per-finding comparison was cheap (`--json` ids per file,
old versus new) and the output change the delta makes is in the listing lines, not in which
files or kinds fire, so the comparison would not have been noisy. Not re-driven here (no sibling
repos). *Counsel:* record the rung stopped at per §1, or re-run the comparison per file and kind
and record it on the item; nothing in this verdict depends on the claim.

**Overall line, restated:** **PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE · 4 minor · 4 note**
(HX1–HX3 MODERATE; HX4, HX5, HX10, HX11 minor; HX6–HX9 note). The headline stands: "nothing
silences the cold-content gate" is true at the scanner and false at the floor, the fork was not
surfaced, and the principal ruled "never" on an account that did not name the floor lane.

## Deferred material — folded in at the verdict

*The sibling `docs/reviews/2026-10-17-0930-sizescan-cold-hatches-cold.deferred.md`, verbatim,
folded in here on 2026-10-18 and deleted from the tree, per `REVIEW.md` rule 1 "split for the
duration, merged at rest".*

# Sibling to the sizescan cold-content hatches cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-17-0930-sizescan-cold-hatches-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-17 UTC by the Opus brief-writer named in the brief's provenance; it
forms no finding. Fold this file in below the reconcile and delete it at phase 2.

## Intent and commissioning records

- Intent record: `docs/sessions/2026-10-16-0703-queue-run-after-the-sizescan-ruling.md` —
  **not opened by the brief-writer**.
- Commissioning board item (head line seen, never read whole): `115/270` (three defects found
  while adding finding IDs, found 2026-10-05 by the `080` finding-ID worker). The pointer scopes
  this pass to its parts (a) and (b); part (c) is 160/850's subject.
- A neighbouring board commit, subject only: `fd63df8` (2026-10-06 03:49 UTC) — "board: Mike's
  ruling on sizescan, verbatim, on 115/270 — three builds owed".
- The landing commit's message body (read by the brief-writer): it restates the ruling as
  "nothing may exempt the cold-content gate, since no repo should keep a flat running log" and
  "a check which finds done work must report the specific items"; describes (a) and (b) as the
  brief's *What the work is* lists them; reports a side effect found on the way (`files_by_glob`
  always printed 0 because `iter_candidates` never appended to the list it was handed); and
  gives a blast radius: `sizescan --check` run old and new over every git repo on the authoring
  machine, one at a time, with no repo changing exit code and one already failing under both.
- The merge's message body: the orchestrator read the diff and re-ran the targeted tests before
  merging; the work was rebuilt fresh after a 07:35 UTC crash.

## Prior verdicts on these surfaces (named by filename grep, not opened, not exhaustive)

- `docs/reviews/2026-07-14-2048-lean-files-sizescan-cold.md` — sizescan's origin
- `docs/reviews/2026-07-19-0407-review-trigger-sizescan-combined-cold.md`
- `docs/reviews/2026-07-20-2040-size-rebalance-cold.md`
- `docs/reviews/2026-07-22-0819-harvest-integrity-gate-cold.md`
- `docs/reviews/2026-10-03-0357-shared-allow-marker-grammar-cold.md` — the marker grammar
- `docs/reviews/2026-10-16-1551-marker-kinds-finding-ids-cold.md` — an unrun 2026-10-16 brief on
  the scoped kinds this delta changes (another pass's framing)

## The pointer's own lens hints

None. The pointer is refs-only.

## Overlap with sibling passes of this batch

- 160/850 (size advisory removed, `72a68cc`) rewrote this delta's surface the same day. Findings
  on code that 160/850 replaced belong to the landed delta here, and to 160/850 only if they
  survive its change; say which.
- 160/750 (marker kinds and finding IDs, `115/080`) introduced the scoped kinds, including the
  `cold-content` scope this delta makes inert.
- 160/730 (the shared report contract) owns `report.over_cap_line` and `report.cap_part`, which
  this delta calls.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. This repo's own `.sizescanignore` matches the harness worktrees nested under `.claude/`, with
   a comment saying their roadmap copies must not gate this repo's commit. With
   `evaluate_ignored`, a glob no longer skips a hot-path file. Does a nested worktree's
   `ROADMAP.md` (or another metered file) now get read and gated from this repo's root, unless
   the file walk excludes it on its own? Probe it with a fixture.
2. In `scan_paths`, slots are spent and `cold_over_cap` is charged before the checks that drop a
   file (a blanket-marked archive store, a file with no reference). Can the over-cap count and
   the spent slots include items of files that produce no finding?
3. `files_by_glob` now counts ignored hot-path files that are still gated. Does "N file(s) by
   .sizescanignore" on the suppressed line now claim a suppression that did not happen?
4. The docstring dates the ruling 2026-10-05; the board commit that recorded it verbatim is
   timestamped 2026-10-06 03:49 UTC. Is the docstring's date a local date stored at rest
   (CONVENTIONS: UTC at rest)?
5. The README paraphrase ("no repo keeps a flat running log; the board is a list of work and its
   state, and the detail lives in a standalone file") sits beside the verbatim quote in the
   module. Does either narrow or widen the quote?
6. The blast radius was measured on exit codes only. `EVIDENCE.md` §13 says a scanner delta
   compares per-finding output, never totals. Does an exit-code-only comparison meet that?
7. Item text is printed raw into hook output and CI logs. A completed item carrying a terminal
   escape sequence, or a bidirectional-control character, would reach the log unaltered. Is that
   the house's concern for a tool whose input is the repo's own tracked text?
8. Does any template, onboarding skill or child-facing doc still tell a repo it may keep a flat
   log behind `sizescan:allow`, now that the hatch exempts nothing from the gate?
