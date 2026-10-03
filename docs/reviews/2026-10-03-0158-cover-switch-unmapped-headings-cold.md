# Cold pass — `stampscan --require-stamps` and blockscan's unmapped-heading report

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this pass's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-10-03 0158 UTC; the review runs under the
orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/430-rule-4-cold-pass-queued-the-cover-switch-and-unmapped-headings.md`.
**Why it earns a review:** both tools are guards. One decides whether a floor
block in a child is verbatim; the other decides whether a doctrine edit landed
inside a region a guard watches. A guard that reports clean over nothing, or
over a region it cannot see, is the inversion class this repo keeps finding.

## Spawn provenance

- **Author of the work under review:** the 2026-10-03 queue run (an Opus
  orchestrator with dispatched workers) that landed the merges named under
  *What the work is*. This brief-writer was not that session, was neither
  started nor instructed by it, and has edited none of the delta's paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-10-03 with
  the prompt "Do all cold reviews and any other work dependent on fable", on
  the Fable tier (`claude-fable-5-1`). It wrote this brief from the queue
  pointer, the landing merges' subjects and `--stat` file lists, and the delta
  paths' names; it did not open the intent record.
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
  that the pointer existed and named the two features; nothing else from that
  run was read. Earlier in the same sitting this session commissioned read-only
  inventories of the board's open items and of every verdict in
  `docs/reviews/`, for a ruling round; the summaries it received include prior
  findings on both tools under review (the 2026-09-25 floor-verbatim pass on
  `stampscan`, and the naming-precedence and report-up-duty passes, which name
  `blockscan`'s heading map). Those summaries are the author-side framing this
  pass must meet cold; every line of them that bears on these tools has been
  moved to the sibling and kept out of this brief. The brief-writer also read
  the 2026-09-25 batch's staged-plane brief as a formatting template, the
  session index entries of 2026-09-19 to 2026-10-01, and, as doctrine at
  onramp, `docs/method/REVIEW.md`, `docs/method/00-APEX.md` and
  `docs/method/COMMUNICATION.md` § *Asking for a ruling* at HEAD.

## What the work is

Landing commits (diff these; review the paths at HEAD, `b7520a5` or later):

- `3cb2f64` (2026-10-03) — merge of `4e83dc3`: `stampscan --require-stamps`,
  so a run that checked nothing cannot pass (board `320/130`)
- `33b3c5f` (2026-10-03) — merge of `bd09b1b` and `172d767`: blockscan reports
  the headings its map cannot see, collapsing top-level ones to a count (board
  `320/340`)

Delta paths:

- `tools/stampscan.py` — the `--require-stamps` switch
- `tools/test_stampscan.py` — its tests
- `tools/blockscan.py` — the unmapped-heading report in `--check`
- `tools/test_blockscan.py` — its tests
- `tools/README.md` § *stampscan* and § *blockscan*

Neither commit touched `tools/floor.py`, `.github/workflows/ci.yml` or
`.githooks/pre-commit`; whether the new behaviour is reachable from any wired
invocation is yours to establish from those files at HEAD.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Driven, not read: in a scratch clone, run `stampscan` with and without the new
switch over a tree with zero stamped blocks, over a tree whose only stamps sit
inside fenced code, over a tree where the mixed-root invocation finds the
source but no child, and over a child that resolves the source through a pin.
Run `blockscan --check` over a doctrine file whose edit sits in a `###`
subsection under a mapped `##`, over a file with a heading the map has never
seen at each level, over a renamed heading, and over a heading inside a fenced
block; record what each run prints and what it exits. Compare every wired
invocation of both tools at HEAD (`floor.py` registry, `ci.yml`, the hook,
the child `floor.yml` template) with the invocations the tests exercise.
**Non-goals:** the board items that commissioned the work, and whether either
tool should be in the floor registry at all.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. A
   switch that makes "checked nothing" a failure presumes the tool can tell
   nothing from something: find the shape where the count is non-zero but the
   cover is still empty. A report of unmapped headings presumes the map's
   keying is the right unit: find the edit the new report still cannot see.
2. **Correctness & quality.** Read all of both tools and both test files. Run
   each tool's `--selftest`, its unit tests, and the full Python suite once.
   Drive every state in *Scope*. Check the collapsed top-level count against
   the uncollapsed list for the same tree.
3. **Completeness / harvest.** Every surface that describes either tool's
   contract: `tools/README.md`, the module docstrings, `--help`, the floor
   registry's `why`, `CHANGELOG.md`, and the child template's workflow. Does
   each say what the tool now does, and does any wired caller pass the new
   switch?
4. **Security & privacy** — mandatory. Both tools read files named by argv and
   print paths and heading text; check argument handling against a path with
   a leading `-` or spaces, a heading containing control or bidi characters,
   and a map entry that names a path outside the root. The house scanner is
   discharged by grounds (landed delta; the pending diff is this brief) — say
   so, and deliver the code-altitude read by hand, checked against the OWASP
   catalogue where the work has a code surface.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 tools/stampscan.py --selftest`; `python3 tools/blockscan.py
  --selftest`; `python3 -m unittest tools.test_stampscan tools.test_blockscan`;
  the full Python suite once (`python3 -m unittest discover -s tools`, in the
  foreground)
- the floor on both planes at HEAD
- every state in *Scope*, driven in a scratch clone

## House rules for this run

- You work in the review worktree `/Users/mike/worktrees/atelier-review-430`
  (branch `review-430-1003`), read-only except for THIS brief file. Run **no git
  command that writes** there (no add, commit, stash, checkout, worktree,
  reset, clean). Read-only git (`log`, `show`, `diff`, `blame`) is fine.
  Mutation probes, scratch children and checkouts of older commits go in your
  own clone: `git clone /Users/mike/worktrees/atelier-review-430
  <scratchpad>/CU/probe` under the session scratchpad.
- One heavy process at a time on this machine: run the full Python suite at
  most once, in the foreground with a long timeout; never scan any tree outside
  the worktree or your scratch clone, and never point a scanner at the
  machine's other repos. Other sessions are live on this machine and in this
  repo's primary checkout; touch nothing there.
- `/security-review` is **discharged by grounds**: it reads the session's
  pending diff, which here is this brief, and this is a landed-delta review.
  State that line in your lens-4 answer and deliver the code-altitude read by
  hand.
- Dates in your verdict are absolute ISO-8601 from `date -u` (the hook-plane
  `datescan` reds relative words such as "yesterday" or "next week" and would
  block the orchestrator's commit). Wrap prose at ≤ 100 columns. NZ English.
  Never quote a secret, a placeholder token, an email address or any personal
  detail — this repo is PUBLIC; describe, don't quote.
- Review deep, not fast. A finding needs a probe or a re-driven claim behind it,
  not reasoning alone; a clean lens needs the trail that earned it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held by the orchestrator outside the worktree under the rule-1 split and released only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/430-rule-4-cold-pass-queued-the-cover-switch-and-unmapped-headings.md`
(it carries the author's framing and this pass's claim line), and:

- `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md` (the
  intent record)
- the board items `docs/roadmap/320-*/130-*.md` and `docs/roadmap/320-*/340-*.md`
  (the commissioning items), and `docs/roadmap/160-*/340-*.md`, `160-*/360-*.md`,
  `160-*/300-*.md` (pointers that carry prior verdicts' outcome lines on these
  tools)
- the verdicts `docs/reviews/2026-09-25-0715-floor-verbatim-cold.md`,
  `2026-09-25-0715-naming-precedence-cold.md` and
  `2026-09-25-0715-report-up-duty-cold.md`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-430 --also-exclude
docs/roadmap/160-doctrine-review-owed/430-rule-4-cold-pass-queued-the-cover-switch-and-unmapped-headings.md
--also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up
--also-exclude docs/roadmap/160-doctrine-review-owed <pattern>` — rule 2's
default bar plus the items above; `--include-barred` only with disclosure in
the verdict. Reading the *delta* is never barred: the code, its tests, the
README entries and the registry are the subject. What is barred is the author's
narrative of why, and the verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `CU`: `CU1`, `CU2`, …) and severities (MAJOR / MODERATE
/ minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger with the commands and their results, and a follow-up checklist.
Then STOP and report to the orchestrator that phase 1 is written. Do not open
the sibling (it is not in the tree); do not edit the queue pointer, the board,
or any file but this one.

**Phase 2.** On receipt of the sibling's text, append `### Reconcile` beneath
your verdict: per-finding notes against the seeded questions and the intent
record, any finding formed at reconcile marked as such, and the overall line
restated. Never revise phase-1 text. The orchestrator folds the sibling in below
your reconcile.

Findings are the principal's to decide (rule 3): record all, apply nothing;
your counsel per finding is welcome, labelled as counsel and kept beneath the
finding.

---

# Verdict — phase 1

**Overall: PASS-WITH-FINDINGS — 0 MAJOR · 1 MODERATE · 6 minor · 3 notes.**
Written 2026-10-03 04:45 UTC.

## Provenance

- **Reviewer:** `claude-fable-5-1`, a fresh subagent spawned by the brief-writer
  with this brief as its only framing. Not the author's session (the 2026-10-03
  queue run), not started or instructed by it, and no path of the delta was
  edited by this reviewer. Tier at claim and at verdict: Fable, matching the
  brief's stated tier; the off-tier clause is not invoked.
- **What was read:** this brief; the delta paths (`tools/stampscan.py`,
  `tools/blockscan.py`, `tools/test_stampscan.py`, `tools/test_blockscan.py`,
  `tools/README.md` § *stampscan* and § *blockscan*) in full; `tools/floor.py`
  (registry and `--help`), `.github/workflows/ci.yml`, `.githooks/pre-commit`,
  `.github/workflows/floor.yml`, `docs/build/templates/workflows/floor.yml`,
  `tools/blockscan_map.json`, `.atelier-floor.json`, `.stampscanignore`, and
  `CHANGELOG.md` by grep for the two features. Nothing under the rule-2 bar was
  opened; `coldsweep` was not needed because no tree-wide grep ran outside
  `tools/`, `.github/`, `.githooks/`, `docs/build/templates/` and the six mapped
  method docs. The sibling `.deferred.md` was not opened.
- **Which SHA each read was at.** The worktree was at `4ff8de5` when the delta,
  wiring files and README sections were read. During the pass the orchestrator
  merged `origin/main` into the review branch, moving HEAD to `0a669e7`. The
  diff `4ff8de5..0a669e7` over the delta paths was read in full: `stampscan.py`
  and `blockscan.py` changed only in the allow-marker regex and the ignore-file
  loader (now imported from `tools/allowmarker.py`); the `--require-stamps`
  block, `check_unmapped`, `_headings`, `_render_unmapped` and the `_main`
  wiring are byte-identical across the two SHAs; `tools/README.md` changed only
  outside the two sections under review. Every probe, selftest, unit test, live
  run and floor run in the ledger below was driven at `0a669e7`; the first
  (pre-merge) results at `4ff8de5` were identical state for state and are
  recorded only where they add information.
- **Harness disclosure.** One full-suite run at `4ff8de5` was moved to the
  background by the harness at its 600-second foreground cap (it finished green,
  1576 tests, 765 s). On the orchestrator's instruction the suite was re-run at
  `0a669e7` in the foreground as three alphabetical chunks whose test counts sum
  exactly to the loader's discoverable count (513 + 538 + 571 = 1622).

## Lens 1 — approach and assumptions

**Load-bearing assumptions, named.** (a) `--require-stamps` assumes "at least one
stamped block compared" is the same thing as "the floor block is covered".
(b) `check_unmapped` assumes the map's unit — a `##`-or-deeper ATX heading line
in a doc the map names as a source — is the unit an edit lands in, and that a
`#` heading is only ever the document title. (c) Both assume the advisory
printout is read by someone.

**The shape where the count is non-zero but the cover is empty (probe E):** a
tree whose floor copy is unstamped but which carries one unrelated stamp (a
generic region in another file) passes `--require-stamps` with exit 0 and
"1 stamped block(s) verified". The switch keys on *any* verified stamp, not on
the `(FLOOR_SOURCE, FLOOR_REGION)` pair the same module already defines for the
verbatim rule, while its own `--help` and README frame the intent as "a tree that
is EXPECTED to carry a stamped floor block". Recorded as **CU1**. On atelier's
own tree the gap is latent (exactly one stamped block exists, and it is the
floor), which is why the live run cannot show it.

**The edit the new report still cannot see:** the body under each mapped doc's
`#` title. `_headings` drops level-1 headings as "the document title", but
`extract_section` treats a `#` line as a section terminator, so the text between
the title and the first `##` is neither a mapped section nor a reported unmapped
one. Every one of the six mapped docs has such a body (4–9 non-blank lines each,
measured at `0a669e7`). The fenced presentation of the floor region in
`PROPAGATION.md` is the other invisible span: its own `##` lines sit inside a
fence and are skipped. Recorded as **CU5**. Probe F also confirmed that setext
and indented headings are not detected, consistently with `extract_section`, so
their bodies fold into the enclosing section rather than vanishing; no live doc
uses either (0 setext candidates, 0 four-backtick fences in the six docs).

**Non-goals reviewed:** excluding the commissioning items and the registry
question is a sound narrowing; the reachability question the brief leaves to the
reviewer is answered under lens 3 (CU9).

## Lens 2 — correctness and quality

Both tools and both test files were read whole. Selftests, the two modules'
unit tests (122, green) and the full suite (1622, green) ran at `0a669e7`.
Every state in *Scope* was driven; results are in the ledger. Specific checks:

- **Collapsed count vs uncollapsed list, same tree (live, `0a669e7`):** human
  output says `unmapped: 55`, lists 12 `under mapped` lines, and collapses
  `+ 43 top-level heading(s)`; `--json` carries 55 `unmapped` findings, 12 with
  an `under mapped` detail, 43 with `not in the map`. The arithmetic agrees. The
  *label* does not: 4 of the 43 are `###` headings whose parent `##` is itself
  unmapped, so they are not top-level. Probe F reproduces the mechanism
  (`### Nested under unmapped` lands in the "top-level" count). **CU3**.
- **Parent walk:** a `####` under an unmapped `###` under a mapped `##` is
  correctly labelled `under mapped ## …` (probe F, line 13). Correct.
- **Fence handling in `_headings` (probe H):** a fence is closed by *any* run of
  the same character, so a three-backtick line inside a four-backtick fence
  closes it and the heading after it is reported; a backtick run inside a tilde
  fence is handled correctly. This diverges from the shared sibling rule
  (`stampscan._content_lines`, datescan, linkscan, pathscan, wrapscan: closer
  ≥ opener length, same character, bare). No mapped doc carries a nested fence
  at `0a669e7`, so the live report is unaffected. **CU4**.
- **Stale map suppresses the report (probe G):** exit 2, `stale-heading` only.
  Correct. `--staged`/`--against` never emit `unmapped` (probe E2, live
  `--against HEAD^`). Correct.
- **`--json` under `--require-stamps` (probe F vs F′):** a require failure
  prints only the stderr line and exits 2 with an *empty stdout*, whereas every
  other exit-2 path (a config error) still emits the JSON document. The test
  `test_unstamped_tree_fails_with_switch_under_json_and_warn` pins the exit code
  only, so the gap is tested around rather than caught. **CU2**.
- **Switch semantics otherwise:** allow-skipped blocks do not count (test and
  probe), a glob-netted sole stamp does not count (probe G, message names the 1
  file), drift counts as verified so `--warn --require-stamps` over drift-only
  exits 0 (probe E2 — acceptable: the run did compare something), and a config
  error short-circuits the switch and exits 2 anyway. Off by default; the CI
  invocation is unchanged.
- **Subsection blindness confirmed end to end (probe E1/E2):** `--check` reports
  the `###` under the mapped `##`; a `--staged` run with only that subsection's
  body changed and neither bullet moved exits 0 clean. The report shows the hole;
  the rule still has it. By design per the README; **CU10** records the
  consequence.

## Lens 3 — completeness and harvest

| Surface | Says what the tool now does? |
| --- | --- |
| `tools/README.md` § stampscan | yes — switch, exit code, model, default |
| `tools/README.md` § blockscan | yes — report, collapse, `--json`, planes |
| `stampscan.py --help` | yes |
| `stampscan.py` module docstring, exit-code block | **no** — the new exit-2 reason is absent |
| `blockscan.py --help` for `--check` | **no** — still "integrity-only mode … no co-change check" |
| `blockscan.py` module docstring, THE CHECK `--check` | **no** — "Verifies ONLY the map's own integrity" |
| `CHANGELOG.md` | **no** — no line for either feature (grep for `require-stamps`, `unmapped`, `320/130`, `320/340`, `2026-10`: nothing) |
| `floor.py` registry `why` | n/a — neither tool is registered, by stated design |
| child template `floor.yml` | n/a — names neither tool |

**Does any wired caller pass the new switch?** No. `ci.yml` line 191 still runs
`stampscan.py --warn --root . .`; the registry excludes both tools; the hook
names no scanner (ADR 0008); the child template's workflow names neither. The
switch is reachable only by hand. Further, in the place its `--help` aims it —
a child's hook or CI — it cannot be used at all: a child's `--root .` hits
`missing-source` on `docs/method/PROPAGATION.md` (probe D1), switch or not,
because source resolution is not pin-aware (ST3, still open). The only working
child shape is `--root <atelier checkout> <child file>` (probe D2, exit 0,
identical, 91 lines). **CU8** (stale surfaces) and **CU9** (reachability).

## Lens 4 — security and privacy

`/security-review` is **discharged by grounds**: it reads the session's pending
diff, which in this worktree is this brief, and this is a landed-delta review.
The code-altitude read was delivered by hand against OWASP Top 10 (2021) and
the CWE entries the surfaces map to.

- **Path argument handling (A03 injection surface, CWE-88):** a positional
  beginning with `-` is refused by argparse (`unrecognized arguments`) and
  accepted after `--`; a path containing a space scans normally (stampscan
  probes H1–H3 and the bare `-dash.md` probe). blockscan ignores positionals.
  No defect.
- **Map entry naming a path outside the root (A01 broken access control,
  CWE-22):** `--check`'s `read_disk` resolves `root / relpath` with no
  confinement. A `../` entry (probe I1) and an absolute entry (probe I3) are
  both read silently and exit 0, and the *new* report echoes every `##`-or-deeper
  heading line of the outside file into stdout and `--json`. Before this delta
  the same read existed but only the map's own heading string was echoed; the
  content echo is new. The git plane refuses naturally ("is outside repository",
  probe I4). stampscan closed exactly this class for `source=` in 2026-07-26 ST4.
  Precondition is a committed or PR-carried edit to `blockscan_map.json`; the
  CI step runs on every push and PR of a public repo, so the echo would land in a
  public Actions log. Practical exposure is low (only `## ` lines of runner
  files). **CU6**.
- **Control and bidi characters in heading text and paths (CWE-117 log
  neutralisation, CWE-150):** blockscan prints heading text raw — an ANSI colour
  sequence and a U+202E override pass straight to stdout (probe J1, repr shown
  in the ledger). stampscan `repr`s the offending *line* in its drift hint
  (escaped, probe I) but prints the *path* raw (a filename carrying an escape
  sequence reaches the terminal unescaped). The heading echo is new in this
  delta; the path echo is pre-existing and outside it. **CU7** (note).
- **Privacy:** neither tool reads outside the repo on its own initiative; no
  personal data, secret or token appears in either tool's output paths. Nothing
  in this verdict quotes one.

## Findings

**CU1 — MODERATE.** `--require-stamps` certifies "at least one stamped block
compared", not "the floor is stamped", while its `--help` and the README frame
it as cover for the floor block. Probe E: floor copy unstamped, one unrelated
stamp present → exit 0, "1 stamped block(s) verified". The module already holds
`FLOOR_SOURCE`/`FLOOR_REGION` and `_is_floor_block` for the verbatim rule.
*Counsel:* either key the switch (or a sibling `--require-floor-stamp`) on the
pair, or reword `--help`/README to say exactly what it certifies and name the
gap; add the probe-E shape as a test either way.

**CU2 — minor.** `--json --require-stamps` over nothing prints no JSON (empty
stdout, stderr line, exit 2), unlike every other exit-2 path, which emits the
document with `clean: false`. A machine consumer sees a malformed result rather
than a `clean: false`. Probe F vs F′. *Counsel:* emit the JSON (with a
`require_stamps_unmet` marker) before returning 2; pin stdout in the test.

**CU3 — minor.** The collapsed line `+ N top-level heading(s) no bullet cites`
counts every heading with no *mapped* ancestor, nested ones included: 4 of the
live 43 are `###` headings under unmapped `##`s. README repeats the wording. No
test covers a nested heading under an unmapped parent. *Counsel:* "N other
heading(s)" or count nested-under-unmapped separately; add the probe-F case.

**CU4 — minor.** `_headings` fence pairing closes on any run of the opener's
character, diverging from the shared sibling rule (closer ≥ opener, bare). A
three-backtick line inside a four-backtick fence — the standard way Markdown
shows a fenced example — ends the fence early and the next heading is reported
(probe H1, two false reports). No live effect at `0a669e7`. *Counsel:* reuse the
sibling pairing or `stampscan._content_lines`; add the probe-H shape as a test.

**CU5 — minor (lens 1).** The body under a mapped doc's `#` title is invisible
to the co-change rule and unreported by the new report; all six mapped docs
have one (4–9 non-blank lines each). The fenced floor presentation in
`PROPAGATION.md` is likewise unreported. The docstring states the level-1 choice
but neither it nor the README states the consequence. *Counsel:* either report
the title section as a pseudo-heading when its body is non-trivial, or state
the blind spot where the report's scope is described.

**CU6 — minor (lens 4).** `--check`'s disk reader has no root confinement; a map
`path` with `../` or an absolute path is read and the new report echoes its
`##`-or-deeper heading lines (probes I1, I3). stampscan closed the same class
(ST4) with a `relative_to(root)` check. *Counsel:* apply the same confinement in
`read_disk` and treat escape as `ConfigError`; add a test.

**CU7 — note (lens 4).** Heading text (new) and paths (pre-existing) are echoed
raw to stdout; ANSI and bidi sequences pass through (probe J1, probe I).
*Counsel:* `repr`/escape heading text as the drift hint already does for lines.

**CU8 — minor (harvest).** Contract surfaces left stale: `blockscan.py`'s module
docstring (THE CHECK: `--check` "Verifies ONLY the map's own integrity") and
`--check` help ("integrity-only mode") omit the unmapped report; `stampscan.py`'s
module docstring exit-code block omits the new exit-2 reason; `CHANGELOG.md`
has no line for either feature. *Counsel:* three short edits plus one changelog
bullet.

**CU9 — note.** No wired caller passes `--require-stamps` (`ci.yml` line 191
unchanged; registry, hook and child template name neither tool). In a child —
the place the `--help` text aims it — the switch cannot be used until source
resolution is pin-aware (ST3): probe D1 exits 2 `missing-source` regardless.
The feature is complete as a switch and unreachable as cover. Not a defect of
the delta; recorded so the follow-up is visible.

**CU10 — note.** The report lives only in `--check`, which runs as an advisory
CI step; `--staged` and `--against` stay blind to a subsection-only edit (probe
E2 exits 0 clean with the block unmoved). The 55-line advisory block prints
into a CI log on every push; nothing routes it to a human. By design per the
README ("Mapping or leaving a heading is still a human call").

## Re-run ledger (all at `0a669e7` unless marked)

| Command (in the scratch clone) | Result |
| --- | --- |
| `python3 tools/stampscan.py --selftest` | `selftest OK`, exit 0 (also at `4ff8de5`) |
| `python3 tools/blockscan.py --selftest` | `selftest OK`, exit 0 (also at `4ff8de5`) |
| `python3 -m unittest tools.test_stampscan tools.test_blockscan` | Ran 122, OK (also at `4ff8de5`) |
| `python3 -m unittest discover -s tools -p 'test_[a-h]*.py'` (foreground) | Ran 513, OK |
| `… -p 'test_[i-r]*.py'` (foreground) | Ran 538, OK |
| `… -p 'test_[s-z]*.py'` (foreground) | Ran 571, OK — 513+538+571 = 1622 = loader count |
| `python3 -m unittest discover -s tools` at `4ff8de5` | Ran 1576, OK — harness backgrounded it at the 600 s cap; disclosed above |
| `python3 tools/floor.py --plane hook --root . --tools tools` (lifted from `.githooks/pre-commit`) | exit 0; 12 ✅ enforced, 3 👁️ warn-only |
| `python3 tools/floor.py --plane ci --root . --tools tools` (lifted from `ci.yml`) | exit 0; 10 ✅ enforced, 3 👁️ warn-only; pathscan 1 advisory finding (pre-existing, outside delta) |
| `python3 tools/stampscan.py --warn --root . .` (ci.yml line 191) | exit 0; 1 block verified (template, 91 lines), 147 files by `.stampscanignore` |
| `python3 tools/stampscan.py --require-stamps --root . .` | exit 0; same 1 block |
| `python3 tools/blockscan.py --check --warn --root .` (ci.yml) | exit 0; unmapped 55, 12 listed, +43 collapsed |
| `python3 tools/blockscan.py --check --json --root .` | `clean: true`; 55 unmapped = 12 under + 43 rest; 4 of the 43 are `###` |
| `python3 tools/blockscan.py --against HEAD^ --warn --root .` (ci.yml) | exit 0 clean, no `unmapped` |
| Scope state A — zero stamped blocks, `docs` | without switch exit 0 "no stamped blocks found"; with switch exit 2 |
| Scope state B — only stamps inside a fence | without 0; with 2 |
| Scope state C — mixed root, paths name only the source file | without 0; with 2. Control (paths name `docs/`): 0 / 0, 1 verified |
| Scope state D1 — child tree, `--root <child> .` | exit 2 `missing-source` both ways (ST3) |
| Scope state D2 — `--root <atelier clone> <child>/CLAUDE.md` | exit 0 both ways; identical, 91 lines; path printed absolute |
| Probe E — floor unstamped, one unrelated stamp | exit 0 **with** switch ("1 verified") — CU1 |
| Probe E2 — drift only, `--warn --require-stamps` | exit 0, drift printed as advisory |
| Probe F / F′ — `--json --require-stamps` over nothing / `--json` over missing-source | F: empty stdout, exit 2; F′: JSON emitted, exit 2 — CU2 |
| Probe G — sole stamp under an ignored glob | without 0; with 2, message says "1 file(s) by .stampscanignore" |
| Probes H1–H3 + bare `-dash.md` | `docs/-dash.md` scans; bare `-dash.md` argparse error exit 2; after `--` resolves; space path scans |
| Probe I — ANSI/bidi in a drifting line and a filename | line `repr`-escaped in hint; filename echoed raw |
| blockscan E1/E2/E3 — `###` under mapped `##`; subsection-only staged edit | `--check` lists it `under mapped`; `--staged` exit 0 clean; `--json` 2 findings, `clean: true` |
| blockscan F1/F2 — headings at every level, setext, indented, preamble, 2nd `#` | 4 unmapped: `###` and `####` under mapped, `##` and `###`-under-unmapped as "not in the map"; setext/indented/`#`/preamble not reported |
| blockscan G1/G2 — mapped heading renamed | exit 2 `stale-heading`; no `unmapped` |
| blockscan H1 — headings in fences | plain fence ignored; 4-tick and tilde divergence cases reported (2) — CU4 |
| blockscan I1–I4 — map path `../`, absolute (stale / resolving), git plane | I1 exit 0 read silently; I2 exit 2 echoing the absolute path; I3 exit 0, outside `##` counted; I4 exit 2 "outside repository" — CU6 |
| blockscan J1 — ANSI + bidi heading | echoed raw to stdout — CU7 |
| `grep -c '^# '` over the six mapped docs; 4-tick fences; setext | h1 = 1 each; 0; 0 — title bodies 4/9/4/4/5/4 non-blank lines |
| `grep` of `CHANGELOG.md` for both features | no match — CU8 |

Probe scripts and logs live under the session scratchpad `CU/` (not in the
tree). No git command that writes was run in the worktree; the scratch clone
was fetched and checked out to `0a669e7` after the orchestrator's merge.

## Follow-up checklist

- [ ] CU1 — decide the switch's unit (any stamp vs the floor pair) and align
      `--help`/README; add the probe-E test.
- [ ] CU2 — emit JSON on the require-unmet path; pin stdout in the test.
- [ ] CU3 — reword the collapsed count or split nested-under-unmapped; test.
- [ ] CU4 — align `_headings` fence pairing with the sibling rule; test.
- [ ] CU5 — report or document the title-section blind spot.
- [ ] CU6 — confine `read_disk` to `--root` as stampscan ST4 does; test.
- [ ] CU7 — escape heading text (and paths) in human output.
- [ ] CU8 — blockscan docstring + `--check` help, stampscan docstring exit
      codes, CHANGELOG line.
- [ ] CU9 — nothing to fix in this delta; ST3 (pin-aware source resolution)
      remains the gate on wiring the switch anywhere real.
- [ ] CU10 — a ruling on where the advisory report should land, if anywhere
      beyond a CI log.

### Reconcile

Written 2026-10-03 04:50 UTC, after phase 1 was committed unrevised (`5cb4f2b`).
Read now, for the first time: the sibling's text, the intent record's two
sections on these features, and the commissioning items `320/130` and `320/340`.
The prior verdicts (`FV`, `NP`, `RU`) were met through the sibling's summaries
only; they were not opened. The suite was not re-run. Three light checks ran in
the scratch clone at `0a669e7` to test the records' own claims; they are listed
at the end. Phase-1 text above is untouched.

**The records' claims, re-driven.**

- "With the switch off, the output is byte-identical (stdout, stderr and exit;
  plain, `--warn` and `--json`; atelier's tree)" — **holds.** The pre-delta
  `stampscan.py` (`d4b1a84`) and HEAD's produce identical stdout and stderr and
  exit 0 in all three modes over the tree.
- "Six tests were added, 96 in all" — **holds** (loader count 96).
- "The first output was about 60 lines … it is now 16" — **holds** (16 lines).
- "12 subsections sit under mapped sections: one under APEX, five under
  CONCURRENCY, six under PROPAGATION, including § *The route* and § *Report
  without harming the parent*" — **holds**, line for line with the live run.
- "Another 43 top-level headings are cited by no bullet" — **the count holds,
  the word does not**: 4 of the 43 are `###` headings. The record repeats the
  tool's own mislabel (CU3).
- "**So 020/110's precondition is met.** The wiring bar can now lift without
  shipping green-over-nothing, provided the wiring passes the switch" —
  **overstated; see CU1 below.**

**Per finding.**

- **CU1 (MODERATE) — stands, and the intent record sharpens why it matters.**
  `320/130` asked for the `leakscan --require-terms` shape, and the delta is a
  faithful copy of that shape; as a commission it is met. But the item then
  draws a conclusion from it — the cover precondition on wiring stampscan to
  children is discharged — and that conclusion needs "the floor block was
  compared", which the switch does not certify. A child with its floor
  unstamped and any other stamp in its tree still gets green over an unchecked
  floor with the switch on (probe E). *Formed at reconcile:* the sibling's FV1
  and FV2 bear on the remedy. Keying the switch on the floor pair, as phase-1
  counsel suggested, would inherit FV1 (the pair matches the literal `source=`
  string, so a respelled path would read as "no floor stamp" — failing closed
  here, which is the safe direction, but noisy). FV2's allow-marker hole does
  **not** reach the switch: an allow-skipped block is not counted as cover
  (test and probe). Severity unchanged.
- **CU2 (minor) — stands.** Seeded question 5: the stampscan tests drive
  `_main` with argv in-process, and the blockscan tests drive the CLI by
  subprocess, so both go through argument parsing; the gap is that the `--json`
  case asserts the exit code only.
- **CU3 (minor) — stands**, now with a second surface: the `320/340` landing
  note carries "43 top-level" too. Seeded question 3's last part: the collapse
  does **not** hide the case `320/340` was filed for — both subsections it names
  are listed in full. What it folds away is a `###` under an *unmapped* `##`,
  which is not that item's case.
- **CU4, CU5, CU6, CU7 (minor, minor, minor, note) — stand unchanged.** Nothing
  in the intent record or the items speaks to fence pairing, the title-section
  body, root confinement of map paths, or output escaping. Seeded question 3:
  `###` and `####` under a mapped `##` are both seen and labelled; a heading
  inside a plain fence is ignored; CU4 is the nested-fence exception.
- **CU8 (minor) — stands.** The intent record lists both features as delivered;
  no CHANGELOG line was owed anywhere else that this pass could find.
- **CU9 (note) — stands, and converges with the sibling's FV3**, reached
  independently: nothing automated reaches a child's floor block, and a child
  running the tool gets `missing-source`. Seeded question 2: no wired invocation
  passes the switch, so nothing has changed for the hook, for CI, or for a
  child. The item says as much ("whether to wire it … is still 020/110's
  decision"), which is honest; CU1 is the caveat on its "precondition met".
- **CU10 (note) — stands, and the records already own it.** `320/340` stays
  open for the map-design choice, and the sibling's NP6 and RU1 counsel (map
  subsections) is the unbuilt half. The delta delivers visibility, as
  commissioned, and claims no more. AK4 and DR2's disagreement about the shared
  apex section is untouched by this delta.

**Seeded questions not answered above.**

1. `--require-stamps` fails on zero blocks found, on all blocks allow-skipped,
   and on the sole stamped file netted by an ignore glob (probes A, B, G and the
   allow test); a missing source exits 2 as a config error before the switch is
   consulted. That is what `320/130` asked for. What it does not fail on is CU1.
4. Neither change alters an exit code on either plane for a repo that was green:
   the switch is off by default and byte-identical when off; the unmapped report
   never touches the exit code or `clean`; both floor planes ran green at
   `0a669e7`.

**Reconcile checks (scratch clone, `0a669e7`).** Pre-delta `stampscan.py` from
`d4b1a84` against HEAD's, plain / `--warn` / `--json` over the tree: identical
stdout and stderr, exit 0/0 each. `test_stampscan` loader count: 96. Line count
of the live `blockscan --check --warn` output: 16.

**Overall, restated: PASS-WITH-FINDINGS — 0 MAJOR · 1 MODERATE · 6 minor ·
3 notes.** No finding was added, withdrawn or re-graded at reconcile. One thing
for the principal beyond the findings themselves: `320/130`'s landing note says
the cover precondition on `020/110` is met, and CU1 says it is met for "no
stamps at all" and not for "the floor is unstamped" — worth holding beside
`020/110` before that bar is lifted.

## Folded sibling — released after the phase-1 findings were committed

The `.deferred.md` sibling the orchestrator held outside the worktree, folded in
verbatim at close; the reviewer met it only in phase 2.

# Deferred sibling — cover-switch and unmapped-headings cold pass (CU)

Held by the orchestrator outside the worktree and outside the harness
scratchpad. Released to the reviewer only after its phase-1 findings are
committed. Folded into the verdict file at close.

## 1. The queue pointer's own framing (author's words)

The pointer `160/430` as written by the authoring run, before the claim line:

> Rule-4 cold pass queued: `stampscan --require-stamps` and `blockscan`'s
> unmapped-heading report (`320/130`, `320/340`). The run authored this itself
> (its dispatched workers' output counts as the run's authorship). It was
> queued at landing, and the run neither takes it nor spawns a reviewer for it.
> Tier: Fable, the principal-named review tier, checked at selection. Pass
> type: code cold pass, per `method/REVIEW.md` rule 4. Delta, scoped to paths:
> `tools/stampscan.py`, `tools/test_stampscan.py`, `tools/blockscan.py`,
> `tools/test_blockscan.py`, and those two tools' entries in `tools/README.md`.
> It landed on `main` on 2026-10-03, in merges `3cb2f64` and `33b3c5f`.
> Intent record: `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`.

## 2. Intent record and commissioning items (read these in phase 2)

- `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/130-*.md` — a stamp
  proves wording, not provenance; the commission for `--require-stamps`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/340-*.md` — blockscan
  subsection blindness; the commission for the unmapped-heading report

## 3. What the authoring run said to the orchestrator (channel, verbatim)

> (1) I'm appending one line to the end of docs/SESSIONS.md for my run; I'll
> update it in place later, but only on that line. (2) A new file,
> docs/roadmap/160-doctrine-review-owed/430-rule-4-cold-pass-queued-the-cover-switch-and-unmapped-headings.md:
> a refs-only ⏳ pointer for my run's own code (stampscan --require-stamps,
> blockscan unmapped headings). Under rule 4 my run can't take it; it's yours
> or any Fable session's. I'm not touching any other 160 file.

Nothing else from that run was read by the orchestrator.

## 4. Prior findings on these tools (from inventory summaries the orchestrator
## received; the reviewer meets them only now)

From the 2026-09-25 floor-verbatim pass (`FV`, verdict
`docs/reviews/2026-09-25-0715-floor-verbatim-cold.md`, unruled):

- FV1 (MODERATE): `_is_floor_block` matches the literal `source=` string, not
  the file; four respellings of the path let a narrowed floor pass clean.
- FV2 (MODERATE): a `stampscan:allow:` line inside the floor block skips the
  verbatim check; the tool's footer under a floor-narrow red recommends both
  `narrow=` and the allow marker.
- FV3 (MODERATE): nothing automated reaches a child's floor block; stampscan is
  not in the floor registry, not in the child `floor.yml`, not in create-repo.
  A child running it gets missing-source or scans nothing.
- FV11 (minor): the fleet leg closed on a one-off measurement, not the
  instrument it owed.

From the 2026-09-25 naming-precedence pass (`NP`) and report-up-duty pass
(`RU`), both unruled:

- NP6 (MODERATE), guard half: blockscan missed a floor-region edit because its
  map keys the `##` heading while the edit was in `###` subsections. The guard
  half was boarded as `320/340`, which this delta claims to answer.
- RU1 (MAJOR), blockscan half: blockscan cannot see the `48c181f` edit for the
  same reason; counsel was to map subsections.
- AK4 (note, ask-rule-to-children pass): blockscan double-fires on a shared
  apex section; called a coarse false positive needing an allow marker. DR2
  (da-rulings-applied pass) treats the same red as a genuine defect. The two
  passes disagree.

## 5. Seeded questions (the orchestrator's, labelled as such)

1. Does `--require-stamps` fail only on "zero blocks found", or also on "blocks
   found but none evaluated" (all skipped by ignore glob, allow marker, or
   missing source)? Which did `320/130` ask for?
2. Is `--require-stamps` passed by any wired invocation at HEAD? If not, what
   has changed for the hook, CI or a child?
3. Does the unmapped-heading report see a `###` under a mapped `##`? A `####`?
   A heading added inside a fenced block? Does collapsing top-level headings to
   a count hide the one case `320/340` was filed for?
4. Does either change alter exit codes on the hook or CI plane for a repo that
   was green before the merge?
5. Does the test suite drive the new behaviour through `main()` and argv, or
   only through helpers?
