# Cold pass — indexscan, a hand-kept index names every file it maps

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/700-rule-4-cold-pass-queued-indexscan.md`.
**Why it earns a review:** a new floor guard registered in `tools/floor.py`, which
every child runs at `main` on its next CI run; it defines its own declaration
grammar, its own exemption marker and its own notion of "listed", and the house
adopted it on four of its own indexes in the same landing.

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
  passes rule 4's criterion. The reviewer repeats its own provenance (who spawned
  it, its tier, any orchestration shape) in its verdict.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This
  brief-writer read: the queue pointer in full; the landing commits' subjects,
  `--stat` and diffs of the delta paths, **and their message bodies** (the
  author's own account); the subjects and `--stat` of later commits on the same
  files; the merge's combined diff for `docs/SESSIONS.md` lines 3–13 only;
  `REVIEW.md` rules 1–4, the four lenses, the checklist and the lifecycle; the ask
  halves of two 2026-10-04 briefs as templates; `docs/reviews/` filenames and
  filename-level greps (no prior verdict opened); the names, not the contents, of
  the commissioning board items; and its harness-loaded memory index (one-line
  notes, some about these guards' history). Its orchestrator read the
  `docs/SESSIONS.md` index tail through 2026-10-16 (including the authoring run's
  one-paragraph summary) and the 2026-10-16 session record's close section, and
  passed on no evaluative content beyond the pointer list and a one-line note that
  some guard files changed later. Everything evaluative is in the sibling.

## What the work is

Landing commits (diff these; review the paths at HEAD):

- `8d10487` (2026-10-05 12:19 UTC) — tools: add indexscan — a hand-maintained
  index names every file it maps; landed in merge `5600b0e` (2026-10-05 12:26 UTC)

Delta paths (the pointer's list): `tools/indexscan.py`, `tools/test_indexscan.py`,
`tools/floor.py` (the new registry entry), `tools/README.md` (the catalogue
section, plus the index's own declaration and two allow markers at lines 3–5),
`tools/test_allowmarker.py`, `tools/test_mixed_root.py`, and the declaration and
allow-marker lines in `docs/decisions/README.md`, `instruments/README.md` and
`docs/SESSIONS.md`. Note a fact of the landing: the ten `indexscan:allow` lines in
`docs/SESSIONS.md` (lines 4–13) are absent from both parents of `5600b0e` and
first appear in the merge itself (`git show --cc 5600b0e -- docs/SESSIONS.md`).

**Later commits on the same surfaces — not this delta; do not attribute them to
it.** Review the delta's own claims at HEAD and say which commit a finding rests
on:

- `ffabef3` (2026-10-05) — single-source the scanners' exit contract and report
  lines; converted indexscan's report and exit lines (its own pass is 160/730)
- `1c24781` (2026-10-16) — indexscan flags an index line dated before the file it
  links (320/430); adds a second finding kind and a scoped marker form
- `e3e8a4f` (2026-10-16) — licenscan's warning made real; touches `tools/floor.py`

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests
and live behaviour. The lenses organise it; they do not bound it. Non-goals are the
only narrowing and are themselves reviewable.

Build declared indexes in a scratch clone and compare what the guard reports with
what you judge correct. Cases: an index that maps `.` and lives in that directory;
`dir=` with `..` that stays inside `--root`, and one that escapes through a
symlink; a mapped directory that is gone, empty, or a file; `match=` and
`exclude=` lists with spaces, commas inside a glob, brackets, and case
differences on a case-insensitive filesystem; a subdirectory entry and a file
entry of the same stem; an entry named only inside a fenced block, inside an
indented code block, inside an HTML comment, or in a link with a `#fragment`, a
`?query`, percent-encoding, angle brackets or a title; a reference-style link
whose definition is in another file; an entry named by a passing mention in
prose; two declarations in one file mapping the same directory; a declaration
split across two lines; `before=` with an impossible date and with entries whose
leading date is malformed; an allow marker whose entry name contains a space; a
marker for an entry outside every `match=`. For each: listed, unlisted, exempt,
stale, or exit 2 — and is that the right answer? Whether the opt-in claim holds:
does an undeclared child tree pass with exit 0 and say it checked nothing, on both
planes, and does any file in a child's tree become a declaration by accident?
**Non-goals:** the ruling that chose one generic opt-in check over a
decisions-only build, and the separate ruling owed on flipping it to blocking.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Among them: that "any link or code span anywhere counts as listed" is the right
   looseness for the unlisted direction; that leaving listed-but-missing to
   `linkscan` and `pathscan` leaves no gap (check those guards' scope at HEAD —
   `pathscan` is warn-only); that warn-only on both planes still "makes the failure
   cheap", as the floor entry declares under the fourth requirement in
   `docs/method/GUARDS.md`.
2. **Correctness & quality.** Read `indexscan.py` and its tests whole; diff
   `8d10487`. Drive every case in *Scope* and record a table. Check the exit-2 set
   in the docstring against the code, and that `--warn` never downgrades exit 2.
   Check the line-chunking path for long lines, and the stale-allow logic when two
   markers name the same entry.
3. **Completeness / harvest.** The four adopted indexes at HEAD: is each
   declaration right for what that index actually catalogues, and is every allow
   marker's stated cause still open? (`tools/README.md` lines 4–5 point at two
   open findings by ID — check they still stand by filename-level grep only, and
   open the verdicts only after phase 1.) Does `tools/README.md`'s catalogue
   section agree with the code, and do `docs/method/GUARDS.md` and the floor's
   other descriptions name the new guard where they list guards?
4. **Security & privacy** — mandatory. The guard reads every Markdown file in a
   tree it does not trust and resolves paths a committed file chooses. Probe
   `dir=` and link targets for escape outside `--root` (`..`, absolute paths,
   symlinks, `file:` and other schemes), regex cost on adversarial lines, and
   whether its output can echo file names from outside the repo. `/security-review`
   is discharged by grounds (a landed delta; the pending diff is not the work) —
   say so, and deliver the code-altitude read by hand against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest tools.test_indexscan tools.test_allowmarker
  tools.test_mixed_root -v`, and `python3 tools/indexscan.py --selftest` if the
  guard has one (check `--help`)
- the landing claims: decisions and instruments indexes clean; the tools
  catalogue's two gaps allow-marked; the session index's unlisted count — re-run
  `python3 tools/indexscan.py --root <tree> .` at `8d10487`, at `5600b0e` and at
  HEAD in a scratch clone, and say which numbers reproduce
- the undeclared-tree pass: a fresh scratch repo with no declaration, both planes
- `python3 tools/floor.py --list --plane hook` and `--plane ci`, then the floor on
  both planes at HEAD; the full Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there (no add,
  commit, stash, checkout, worktree, reset, clean); read-only git is fine.
  Probes, older checkouts and scratch trees go in a private clone under your
  session scratchpad, named by your prefix.
- One heavy process at a time on a shared machine: the full suite at most once, in
  the foreground. Never point a scanner at any other repo on the machine.
- `/security-review` reads the session's pending diff: discharge it by grounds for
  this landed delta and do the code-altitude read by hand, or keep the tree clean
  whenever you spawn it.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ
  English. Never quote a secret, placeholder token, email address or personal
  detail — this repo is PUBLIC; describe and locate instead.
- Reading `docs/SESSIONS.md` is barred (below) except lines 3–13, the delta's own
  declaration and markers: read them with `sed -n '3,13p' docs/SESSIONS.md` and
  nothing wider. Running the guard prints session file names; that is permitted.
  Disclose both in your verdict.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md` (save the
carve-out above), `docs/sessions/`, every prior verdict in `docs/reviews/`, the
queue pointer, this brief's sibling
`docs/reviews/2026-10-16-1551-indexscan-guard-cold.deferred.md`, and the
commissioning items, barred with their whole board sections so no path runs past
the column budget:

- item `010` in `docs/roadmap/200-anti-slop-invariant-registry-promote-rec/`
- item `430` in `docs/roadmap/320-child-filed-findings-via-pointing-up/`

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/700-rule-4-cold-pass-queued-indexscan.md
--also-exclude docs/reviews/2026-10-16-1551-indexscan-guard-cold.deferred.md
--also-exclude docs/roadmap/200-anti-slop-invariant-registry-promote-rec
--also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never
barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, the standing
checklist V1–V7 each answered or discharged with grounds, findings with stable IDs
(prefix `IX`: `IX1`, `IX2`, …) and severities (MAJOR / MODERATE / minor / note),
an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger with
commands and results, and a follow-up checklist. Then STOP and commit (or have
your orchestrator commit) phase 1 unrevised before opening the sibling.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict:
per-finding notes against the seeded questions and the intent record, any finding
formed at reconcile marked as such, and the overall line restated. Never revise
phase-1 text. Then fold the sibling in below the reconcile and delete it.

Findings on self-authored doctrine are the principal's to decide (rule 3): record
all, apply nothing; counsel per finding is welcome, labelled and kept beneath it.

---

## Verdict — phase 1 (reviewer IX, 2026-10-17 UTC)

### Provenance, repeated

- **Reviewer:** a fresh `claude-fable-5-1` subagent — the Fable tier the principal names for
  cold passes (ruling 2026-08-04), checked at selection. Spawned 2026-10-17 UTC by a Fable
  orchestrator that authored none of the delta and none of this brief, holds the context
  partition, and forms no finding (REVIEW.md rule 4, the reviewer-plus-orchestrator shape,
  disclosed here before the findings). The brief was written 2026-10-16 UTC by an Opus
  brief-writer, off-tier and disclosed in it; it formed no finding.
- **Worktree:** `/Users/mike/worktrees/atelier-review-1017`, branch `review-1017`, HEAD
  `bee847f` (descends from `8acfff1`). No git command that writes was run there. Probes,
  the older checkouts (`8d10487`, `5600b0e`) and scratch repos ran in a private clone and
  fixture trees under this session's scratchpad, named `IX-*`.
- **What I read:** this brief; `docs/method/REVIEW.md` rules 1–4, the four lenses, the
  re-run rule and the V1–V7 checklist; `tools/indexscan.py` at HEAD and at `8d10487`;
  `tools/test_indexscan.py`; the `indexscan` registry entry and argument parser in
  `tools/floor.py`; `tools/README.md` lines 1–12 and the catalogue section (1140–1240);
  `docs/method/GUARDS.md` lines 27–70; `docs/decisions/README.md` and
  `instruments/README.md` lines 1–5; `CHANGELOG.md` lines 86–96 and 144–156; excerpts of
  `filewalk.py`, `allowmarker.py`, `report.py`, `linkscan.py` and `pathscan.py` by grep;
  the floor invocations in `.githooks/pre-commit` and `.github/workflows/ci.yml`;
  `.atelier-floor.json`.
- ⚠️ **Exposure, disclosed.** (1) `docs/SESSIONS.md` lines 3–13 only, by `sed -n '3,13p'`,
  the carve-out; the guard run at `8d10487` printed ten session file names, which I
  redacted from the ledger below. (2) `git show 8d10487 -- <small delta paths>` printed
  that commit's **message body** before the diff — a barred item I met unintentionally;
  I did not read `5600b0e`'s body (subject and `--stat` only). One finding (IX6) touches
  what that body claims; it is grounded on the re-run numbers and the brief's stated fact,
  not on the body. (3) The cold sweep printed filenames of the other 2026-10-16 passes'
  briefs and of two board items (`115/080`, `160/810`); none opened. (4) The shared
  scratchpad listing showed other reviewers' prefixed file names; none opened. No prior
  verdict, session record, roadmap-done entry, queue pointer or sibling was opened.
  `--include-barred` was not used.

### Lens 1 — approach and assumptions

Load-bearing assumptions, named first and then tested:

1. **"Listed-but-missing is already guarded by `linkscan` and `pathscan`, so only the
   unlisted direction is added."** False for two of the four indexes the house adopted.
   `tools/README.md` and `instruments/README.md` name their entries by inline code span
   (`` ## `wrapscan.py` `` headings, table cells), not by link. With `tools/wrapscan.py`
   removed in the clone: `linkscan --root . .` exit 0 (clean); `pathscan` on the floor's
   atelier scope exit 0 with no mention of it; `pathscan` aimed straight at
   `tools/README.md` reports its 5 pre-existing findings and still no mention (a bare
   `name.py` span is not a path candidate for it); `indexscan` clean. The same for the
   instrument folder `instruments/ccclose` removed: all three silent. So the drift the
   docstring says is "already guarded, and NOT re-checked here" is unguarded on the
   catalogue kind — **IX1**.
2. **"Any link or code span anywhere counts as listed."** Holds as the right looseness
   for a warn-only, adoption-first guard: no catalogue is forced into one layout. Its cost
   is visible in the house's own adoption: `instruments/install` is "listed" only by a
   passing mention in prose (`instruments/README.md` line 130), with no catalogue row —
   the guard cannot tell a row from a mention, by design (**IX7**, note).
3. **"Warn-only on both planes still makes the failure cheap."** Holds. GUARDS.md's fourth
   requirement is a declaration about the guard's *shape* — survivable bad event plus a
   built recovery, versus forbidding the act — not about its wiring. The bad event (an
   unlisted file) commits; the recovery is one index line, named at the causing commit.
   Warn-only is the adoption-first pattern `pathscan` set and the flip is a separate
   ruling, kept out of scope by the brief's non-goal, which fences no risk I found.
4. **"Opt-in per index cannot red a child."** Holds on both planes (probe D, probe 29) —
   with one cheap edge: a verbatim copy of the README's example line outside a fence is a
   live declaration (**IX9**, note).
5. **The brief's account of the work** matches the delta: `8d10487` is the whole guard;
   `ffabef3` and `1c24781` are later and are attributed below where a finding rests on
   them. Non-goals (the option-C ruling; the flip) are legitimate narrowings.

### Lens 2 — correctness and quality

Read whole at HEAD and at `8d10487`; the `8d10487` → HEAD diff is the report-contract
single-sourcing (`ffabef3`) and the date rule (`1c24781`). Cases driven in fixture trees
(`IX-probe.py`, `IX-probe2.sh`, `IX-probe3.sh`; outputs kept beside them):

| # | Case | Result | Right? |
|---|---|---|---|
| 01 | `dir=.`, index inside | unlisted `b.md`; index excluded | ✅ |
| 02 | `dir=..` staying inside root | unlisted found | ✅ |
| 03 | `dir=../..` escaping | exit 2, located | ✅ |
| 04 | `dir=link`, symlink to outside root | outside file names echoed as `unlisted` | ❌ IX2 |
| 05 | link into that symlink | entry counted listed; symlink not an entry (os.walk) | ⚠️ note |
| 06/08 | dir gone / dir is a file | `missing-dir` ("does not exist" for a file) | ✅ / wording |
| 07 | dir empty | clean, 0 entries | ✅ |
| 09 | `match=*.md, *.py` (space) | exit 2 (`'*.py' is not key=value`) | ✅ |
| 10 | `match={a,b}.md` | clean, **0 entries mapped** | ❌ IX5 |
| 11 | `match=[ab].md` | works | ✅ |
| 12 | `A.md` on disk, `a.md` linked | unlisted (exact name) | ✅ (Linux CI truth) |
| 13 | `tool/` and `tool.md` | the directory reported, the file listed | ✅ |
| 14 | fenced link only | unlisted | ✅ |
| 15 | indented code block | counts as listed | ⚠️ IX8 |
| 16 | link inside an HTML comment | counts as listed | ⚠️ IX8 |
| 17 | `#frag`, `?q`, `%20`, title | listed; `<x/e f.md>` with a space **unlisted** | ⚠️ IX8 |
| 18 | ref-def in another file | unlisted (index reads only itself) | ✅ |
| 19 | passing mention in prose | listed | ✅ by design |
| 20 | two declarations, same dir | one finding; `entries` tally 4 for 2 files | ⚠️ IX5 |
| 21 | declaration split over two lines | exit 2, clear message | ✅ |
| 22 | `before=2026-02-30` | exit 2 | ✅ |
| 23 | `2026-13-45-x.md` under `before=` | string-compared; here unlisted | harmless |
| 24 | marker entry with a space | `stale-allow` on the first word + unlisted | ✅ |
| 25 | marker outside every `match=` | `stale-allow` | ✅ |
| 26 | two markers, same entry | second silently ignored, **never stale** | ❌ IX3 |
| 27 | one marker, same name in two dirs | exempts both (`by_marker` 2) | ❌ IX3 |
| 28 | `allow:unlisted:` / `allow:bogus:` | both act as the unscoped marker | ⚠️ IX4 |
| 29 | undeclared tree | exit 0, "checked nothing" | ✅ |
| 30 | README example copied outside a fence | live declaration → `missing-dir` | ⚠️ IX9 |
| 31 | `file:`, `https:`, `/etc/…` targets | none listed; nothing outside root read | ✅ |
| 32 | `before=` and the date rule | `before=` does not shield a dated line | consistent |
| 33 | span first-word resolution | `one.py --flag` listed; `x/two.py` ≠ `two.py` | ✅ |
| 34 | 1 MiB line, link + marker past the cut | both still found | ✅ |
| 35–39 | adversarial lines (50k `-->`, 200k `[`, 200k spans, 300k text) | all < 1 s | ✅ |
| 40 | target outside `--root` | exit 2, absolute path on stderr | acceptable |

Exit-2 set in the docstring against the code: malformed / unknown-key declaration, `dir=`
outside root (textual only — IX2), bad `before=`, unreasoned ignore glob (`guarded_main`),
missing path, plus an unreadable file; `--warn` reaches `report.exit_code` only after every
one of these has returned, so it never downgrades 2 (pinned by
`test_config_errors_exit_2_even_under_warn`, re-run green). Chunking: fences and
declarations are decided at line start only; references and unlisted markers are read on
every chunk; the date rule reads line starts only, so a `date-mismatch` marker past 1 MiB
is invisible — negligible, the straddling link remains the named residual. Tests are
honest and read real behaviour; the one overclaim is the `ListedButMissingIsLinkscans`
docstring ("pinned so the deferral cannot rot silently"), which pins the link case only —
part of IX1.

### Lens 3 — completeness and harvest

- **The four declarations at HEAD.** Decisions `dir=. match=*.md exclude=template.md`:
  the directory holds only `.md` files and no subdirectory — right. Tools `match=*.py
  exclude=test_*.py`: right for a catalogue of checks; `blockscan_map.json`,
  `leakscan-terms.example.txt` and `pre-commit.sample` sit outside it, defensibly.
  Instruments `match=* exclude=*.test.js,*.design.md,fixtures,man`: right in shape; the
  `install` entry is satisfied by a mention, not a row (IX7). Sessions `match=*.md`, no
  `before=`: all 217 files are named or marked.
- **Allow markers.** `tools/README.md` lines 4–5 (FW2, AM5): both consumed, not stale, at
  HEAD — the mechanical proof the entries have not landed; the two review files exist by
  filename (2026-09-25 file-walk, 2026-10-03 allow-marker grammar), not opened.
  `docs/SESSIONS.md` lines 4–13: ten permanent exemptions for records-only captures, each
  carrying why / who / session / "not a ruling" / when — compliant in form; whether
  exempting (rather than listing or moving) is the right answer is **IX6**.
- **Catalogue vs code.** `tools/README.md` §`indexscan.py` agrees with the code on grammar,
  "listed", exit codes and wiring; it restates "one marker exempts one entry", which IX3
  shows is not what the code does. GUARDS.md names no guard by name, so nothing is owed
  there; `floor.py --list` names it on both planes; the CHANGELOG carries both entries;
  no template under `docs/build/` lists guards. Mirror sweep discharged.
- **Later commits, attributed.** `ffabef3` only re-plumbed output; `1c24781` added the
  date rule and the scoped marker (IX4 rests on it); `e3e8a4f` and `dc0ed0e` touched
  `floor.py` without changing this entry.

### Lens 4 — security and privacy

`/security-review` is **discharged by grounds**: the delta landed on 2026-10-05; this
session's pending diff is the other reviewers' draft verdicts, which the scanner would feed
back to me. Read by hand against OWASP Top 10 (2021):

- **A01 broken access control / path traversal** — `_norm` contains `dir=` and link
  targets textually (`..`, leading `/`), but `_entries` walks `root / mapped` without
  resolving it, so a committed symlink escapes: probe 04 and probe A (a git repo, both the
  tool and the floor's hook plane) printed the names of files outside `--root`. Names, not
  contents; warn-only; needs commit access — **IX2 (MODERATE)**, with its prevention step.
- **A03 injection** — no shell, `eval`, SQL or template; file names are printed raw (a
  name carrying terminal escapes would reach a log — shared with every scanner, not
  raised).
- **A05 misconfiguration** — a glob that matches nothing passes silently (IX5).
- **A06 components** — stdlib only. **A08 integrity** — reads committed text; follows no
  scheme (`file:`, `https:` skipped, probe 31), no network. **A09/A10** — prints mapped
  entry names only; no SSRF surface.
- **Regex cost** — five adversarial shapes at 200–400 KB each under 1 s; physical lines
  are chunked at 1 MiB.
- **Design altitude** — nothing over-collected; the guard echoes file names of the
  directories an index opted into, which on a public repo are public already and on a
  private child stay in its CI log.

### The standing checklist

- **V1** — bites: IX1 (docstring and test docstring claim cover that does not exist),
  IX3 ("exactly one entry"), IX6 (the landing's account vs the landed state).
- **V2** — re-run, all reproduce: 10 unlisted at `8d10487` (decisions and instruments
  clean, 2 by marker); clean at `5600b0e` (12 by marker); clean at HEAD (272 entries, 254
  dated lines, 12 by marker, 44 by `exclude=`); selftest; the three test modules; the
  floor on both planes; the undeclared tree on both planes. See the ledger.
- **V3** — swept: README catalogue, registry, CHANGELOG, tests; no doctrine or template
  lists guards by name. Discharged.
- **V4** — the grammar and exit codes are stated in the docstring and restated in the
  README, the house pattern for every scanner; no second original. Discharged.
- **V5** — bites: IX1 (docstring vs the house's own catalogues), IX3 (README/docstring vs
  behaviour), IX8 (`opt_in=False` on an entry headed "OPT-IN PER INDEX" — two meanings).
- **V6** — run; IX2.
- **V7** — provenance stated in the brief and above.

### Findings

**IX1 — MAJOR.** The delta's scope rests on "listed-but-missing is already guarded by
`linkscan` (enforced) and `pathscan`, a third copy would be a second original" (docstring
lines 10–14, `tools/README.md` 1144–1147, `test_indexscan.py` class
`ListedButMissingIsLinkscans`). For an index that names entries by code span — the
catalogue kind, two of the four the house adopted — no guard fires: with `tools/wrapscan.py`
deleted, `linkscan` exit 0, `pathscan` silent on the floor scope and silent when aimed at
`tools/README.md` itself (a bare `name.py` span is not a path candidate for it),
`indexscan` clean; identically for `instruments/ccclose`. The pin test covers the link
case only, so its "cannot rot silently" is also an overclaim. Rests on `8d10487`.
*Counsel:* either (a) `indexscan` checks the reverse for the spans it already resolves —
a span that matches a declaration's `match=` by name yet resolves to no entry is the
ghost, one more set difference in `_references` — or (b) the docstring, README and pin
test narrow the deferral to *linked* indexes and say the catalogue kind is unguarded.
Doctrine by function (a floor guard): Mike's call.

**IX2 — MODERATE (security; recurrence step owed).** `dir=` containment is textual only.
A committed symlink inside the repo pointing outside `--root` is walked, and the outside
directory's file names are printed as `unlisted` findings — reproduced in a plain tree
(probe 04) and in a git repo through the floor's hook plane (probe A). Exposure is names
only, warn-only, and needs commit access, so MODERATE not MAJOR. Rests on `8d10487`.
*Recurrence prevention:* resolve `base` in `_entries` and require it under
`root.resolve()`, else `ConfigError` ("resolves outside --root", exit 2, as the textual
case already does); one test with a symlink. The same resolve-then-contain check belongs
in every scanner that joins a committed path to `--root` — worth a one-line check of the
siblings when it lands.

**IX3 — minor.** The allow map is keyed by entry *name*, first marker wins
(`discover`, `allows.setdefault`). So a second marker naming the same entry is silently
ignored and never reported `stale-allow` (probe 26), and one marker exempts a same-named
entry in every directory the index declares (probe 27, `by_marker` 2) — contrary to
"one marker exempts exactly one entry (rule a)" in the docstring and the README. Rests on
`8d10487`. *Counsel:* key by `(declaration, name)` and report a duplicate as stale.

**IX4 — minor.** `discover` keeps every scoped marker whose kind is not `date-mismatch`
as an unscoped one: `indexscan:allow:unlisted:` and `indexscan:allow:bogus:` both
exempted an unlisted entry (probe 28). A misspelt date kind therefore silently becomes an
unlisted exemption. Undocumented. Rests on `1c24781`, not the delta; the marker-kinds
pass (`160/750`) may already hold the class — recorded here because it is this guard's
parser. *Counsel:* accept `""` and `date-mismatch` only; anything else is `stale-allow`.

**IX5 — minor.** A declaration whose globs match nothing passes clean with "0 entries
mapped": `match={a,b}.md` splits on the comma into two dead globs (probe 10) — the silent
narrowing the unknown-key error exists to refuse ("a mistyped key would narrow the check
without saying so"). Also two declarations mapping one directory double-count `entries`
(probe 20: 4 for 2 files). Rests on `8d10487`. *Counsel:* refuse a glob containing `{` or
`}` (fnmatch has no braces), and report "0 entries" for a non-empty directory on the
summary line as a visible zero rather than a clean head.

**IX6 — minor.** The landing's own account and the landed state disagree. Re-run: at
`8d10487` the session index reports ten unlisted detail files (the delta's stated result,
"left for the records owner"); at `5600b0e`, seven minutes later, it is clean because the
merge itself carries ten `indexscan:allow` lines absent from both parents (the brief's
stated fact; `docs/SESSIONS.md` 4–13), each stamped "added by session … not a ruling".
Form is compliant (why, who, session, when, narrowest unit); the judgement — permanent
exemption for records-only captures living in the sessions directory, rather than a line
each or a move — was the agent's, taken inside the landing. Rests on `5600b0e`. *Counsel:*
Mike confirms the ten as permanent exceptions, or rules the captures listed or relocated;
the markers already say which session chose and that it was not a ruling.

**IX7 — note.** The designed looseness at work: `instruments/install` is "listed" by a
prose mention at `instruments/README.md` line 130 and has no catalogue row. Not a defect
of the guard — it is what "any mention counts" means — but the index-keeper should know
the guard will never ask for that row.

**IX8 — note (documentation and small edges).** (a) Indented code blocks and HTML
comments count as listed (probes 15–16) while the docstring says only fences are skipped;
one clause would make the looseness explicit. (b) A CommonMark angle-bracket destination
with a space, `[e](<x/e f.md>)`, is unlisted (probe 17). (c) `missing-dir` says "does not
exist" when the path is a file (probe 08). (d) `before=` compares a malformed leading date
as a string (probe 23); harmless. (e) The registry entry is headed "OPT-IN PER INDEX" and
carries `opt_in=False` (the registry's own, licence-shaped meaning), which the test pins —
two meanings of one word in one entry. (f) The README's example shows a sessions
declaration with `before=2026-07-11`; atelier's actual one carries no `before=` — fine as
an example, worth a word so it is not read as the house's. (g) In a non-git tree a
symlink is never an entry (os.walk yields regular files) while in a git tree it is (a
tracked path) — probe 05 vs probe A; immaterial to the floor, which runs in git.

**IX9 — note.** A verbatim copy of the README's example declaration outside a fence in any
Markdown file is a live declaration (probe 30 → `missing-dir`, warn-only). Cheap, by
design (`DECL_START_RX`, the ST1 precedent), and `.indexscanignore` covers a fixture tree.
The undeclared-tree claim itself holds on both planes (probe 29, probe D).

**Overall: PASS-WITH-FINDINGS — 1 MAJOR · 1 MODERATE · 4 minor · 3 note.**

### Re-run ledger

All from the worktree root unless stated; heavy steps under `nice -n 10`, one at a time,
foreground; machine load 25–28 throughout.

| Command | Result |
|---|---|
| `python3 tools/indexscan.py --help` | exit 0; `--selftest` present |
| `python3 tools/indexscan.py --selftest` | `selftest OK`, exit 0 |
| `python3 tools/indexscan.py --root . .` (HEAD) | clean, exit 0: 4 declarations, 272 entries, 254 dated lines; 12 by marker, 44 by `exclude=`, 0 by `before=` |
| same with `--warn` | clean, exit 0 |
| clone at `8d10487`: `indexscan.py --root . .` | 10 `unlisted` in `docs/SESSIONS.md` (names redacted here), 267 entries, 2 by marker, 41 by `exclude=` — decisions and instruments clean: **reproduces** |
| clone at `5600b0e`: same | clean, 267 entries, 12 by marker: **reproduces** |
| `python3 -m unittest tools.test_indexscan tools.test_allowmarker tools.test_mixed_root -v` | 80 tests, OK, exit 0 (12.9 s) |
| `python3 tools/floor.py --list --plane hook` / `--plane ci` | `indexscan warn-only fleet` on both, exit 0 |
| `python3 tools/floor.py --plane hook --root . --tools tools` | exit 0; indexscan clean, 👁️ warn-only; all enforced ✅ |
| `python3 tools/floor.py --plane ci --root . --tools tools` | exit 0; indexscan clean, 👁️ warn-only; secretscan/leakscan 🟡 advisory as expected |
| undeclared scratch tree: `floor.py --plane ci` and `--plane hook` (git-initialised) with `--tools <worktree>/tools` | indexscan "no index declares…", exit 0 on both; the tool alone exit 0 with and without `--warn` |
| `python3 -m unittest discover -s tools -p 'test_*.py'` (once) | 1916 tests, OK, exit 0 in 667 s under load (no `BoundedMemory` timeout) |
| `coldsweep.py` with the brief's four `--also-exclude`, patterns `indexscan:maps` and `indexscan` | declarations only in the four indexes, the README fence, the docstring, the tests and the CHANGELOG; no `--include-barred` |
| probes `IX-probe.py` (40 cases), `IX-probe2.sh` (A–D), `IX-probe3.sh` (the gap, exit codes captured off the command) | tabled above; outputs `IX-probe-out.txt`, `IX-probe2-out.txt`, `IX-probe3-out.txt` in the scratchpad |

### Follow-up checklist

- [ ] IX1 — Mike rules (a) span-aware listed-but-missing in `indexscan`, or (b) narrow the
      deferral claim in docstring, README and the pin test to linked indexes.
- [ ] IX2 — resolve-then-contain in `_entries` (exit 2 on escape) with a symlink test;
      recurrence step: check the sibling scanners that join a committed path to `--root`.
- [ ] IX3 — key the allow map by declaration and name; report duplicates as stale.
- [ ] IX4 — accept only the two kinds; route to `160/750` if that pass holds it.
- [ ] IX5 — refuse brace globs; make "0 entries in a non-empty directory" visible; count
      entries once per directory.
- [ ] IX6 — Mike confirms or re-rules the ten session-index exemptions.
- [ ] IX7–IX9 — one clause each in the docstring/README when IX1's wording is touched.
- [ ] Phase 2: reconcile against the sibling once the orchestrator releases it.
