# Cold pass — the shared allow-marker grammar and ignore loader

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this pass's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-10-03 0357 UTC; the review runs under the
orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:** `docs/roadmap/160-doctrine-review-owed/480-rule-4-cold-pass-queued-the-shared-allow-marker-grammar.md`.
**Why it earns a review:** fourteen floor scanners now parse their allow markers and ignore files through one module; a defect there is a defect in every guard on every plane in every repo, and a behaviour change there moves every child's floor at once.

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

- `5d087ec` (2026-10-03) — merge of `643cf80`: one allow-marker grammar and ignore loader, per-guard parameters (board `115/080` part 2)

Delta paths:

- `tools/allowmarker.py` (new) — the shared grammar and loader
- `tools/test_allowmarker.py` (new) — its tests
- the marker and ignore-file code in `tools/blockscan.py`, `conflictscan.py`, `datescan.py`, `leakscan.py`, `licenscan.py`, `linkscan.py`, `pathscan.py`, `pointerscan.py`, `reviewscan.py`, `secretscan.py`, `sizescan.py`, `spellscan.py`, `stampscan.py`, `wrapscan.py`

`tools/floor.py`, `tools/filewalk.py`, the hook and the workflows did not change. The fourteen scanners float at `main` for every child.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Driven, not read: build one fixture tree carrying every marker shape — bare, scoped with reason, scoped without reason, malformed scope (space, missing colon, empty reason), a marker inside a fenced block, inside inline code, in prose that merely mentions the syntax, in a header line, past the header, two markers on one line, a marker whose rule name belongs to a different scanner — and every ignore-file shape (`*`, `**`, a leading `/`, a trailing `/`, a `!` negation, a blank and a comment line, a glob crossing `/`, a path with spaces). In a scratch clone run every one of the fourteen scanners with `--json` over that tree at the landing commit's parent and at HEAD, and diff the outputs. Every difference is either a documented behaviour change or a finding. Do the same for each scanner's `--selftest`. **Non-goal:** the board item that funded the single-sourcing, and part 3 of it.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. Single-sourcing presumes the fourteen grammars were the same grammar: find where they differed before and which behaviour won. Per-guard parameters presume the differences are parametric: find the one that was structural.
2. **Correctness & quality.** Read all of `tools/allowmarker.py`, its tests, and the marker and ignore code in every one of the fourteen scanners at HEAD. Run every `--selftest`, `tools.test_allowmarker`, and the full Python suite once in the foreground with a long timeout. Drive the fixture tree in *Scope* through all fourteen, both commits.
3. **Completeness / harvest.** Every surface that documents marker and ignore-file grammar: `tools/README.md` (the shared section and each scanner's), each module docstring, `GUARDS.md` § *Allowances*, the floor registry, `CHANGELOG.md`, the child template. Do they now agree with one grammar?
4. **Security & privacy** — mandatory. The allow marker is the hatch through every guard. Check fail direction on every malformed shape (does a bad scope exempt more or less?), whether a reason can carry a control or bidi character into a rendered board row, whether the ignore loader can be pointed outside the root, and whether a marker in a file the scanner never reads can still exempt. The house scanner is discharged by grounds (landed delta; the pending diff is this brief) — say so, and deliver the code-altitude read by hand, against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- every scanner's `--selftest`; `python3 -m unittest tools.test_allowmarker`; the full Python suite once (foreground, long timeout)
- the floor on both planes at HEAD
- the fixture-tree `--json` diff across all fourteen scanners, parent vs HEAD

## House rules for this run

- You work in the shared review worktree `/Users/mike/worktrees/atelier-review-430`
  (branch `review-430-1003`), read-only except for THIS brief file. Other
  reviewers are working there at the same time on their own briefs; never open
  another `docs/reviews/2026-10-03-*` file — it is another pass's framing. Run
  **no git command that writes** there (no add, commit, stash, checkout,
  worktree, reset, clean). Read-only git (`log`, `show`, `diff`, `blame`) is
  fine. Mutation probes, scratch children and checkouts of older commits go in
  your own clone: `git clone /Users/mike/worktrees/atelier-review-430
  <scratchpad>/AM/probe` under the session scratchpad, named by your
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
`docs/roadmap/160-doctrine-review-owed/480-rule-4-cold-pass-queued-the-shared-allow-marker-grammar.md`
(it carries the author's framing and this pass's claim line), and:

- `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md` (the
  intent record)
- the board item `docs/roadmap/115-*/080-*.md` (the fund and its routing notes)
- the verdicts `docs/reviews/2026-08-09-0826-e7-leakscan-build-cold.md`, `2026-08-06-0903-licenscan-e1e2-cold.md`, `2026-08-05-1320-f1-guards-allowances-cold.md`, and every `2026-09-25-0715-*.md` on a scanner
- `docs/roadmap/160-doctrine-review-owed/060-*.md`, `110-*.md`, `350-*.md`, `370-*.md`, `410-*.md`, `420-*.md` (pointers carrying scanner verdicts)

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-430 --also-exclude
docs/roadmap/160-doctrine-review-owed/480-rule-4-cold-pass-queued-the-shared-allow-marker-grammar.md
--also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned --also-exclude docs/roadmap/160-doctrine-review-owed <pattern>` — rule 2's
default bar plus the items above; `--include-barred` only with disclosure in
the verdict. Reading the *delta* is never barred: the code, its tests, the
README entries and the registry are the subject. What is barred is the author's
narrative of why, and the verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `AM`: `AM1`, `AM2`, …) and severities
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

## Verdict — phase 1 (cold reviewer, 2026-10-03 04:39 UTC)

### Provenance

- **Reviewer:** `claude-fable-5-1`, Fable tier, spawned by the brief-writer
  (the orchestrating session) with this brief as its only framing. Not the
  author's session; not instructed by the author. Phase 1 only; the sibling
  `.deferred.md` was not opened and is not in the tree.
- **Where the delta was read.** The review worktree (`review-430-1003`, HEAD
  `4ff8de5` at pass start) did **not** contain the landing merge `5d087ec` —
  `git merge-base --is-ancestor` said so, and `tools/allowmarker.py` was absent
  from it. Every read and run below was made in a scratch clone checked out at
  `main` = `ca61feb` (which carries `5d087ec` and is "17c75a9 or later" as the
  brief asks). The parent for the parity drive is `cadcf4e`, the merge's first
  parent; `tools/` differs between `cadcf4e` and `ca61feb` only by the sixteen
  files of the landing commit, so the drive is pure. Mid-pass the orchestrator
  merged `main` into the worktree (now `4ff5f81`); `tools/` there differs from
  `ca61feb` only in `pathscan.py`/`test_pathscan.py` hunks outside the marker
  and ignore code (checked by diff). This is recorded as AM11, not as a defect
  in the delta.
- **What I read.** This brief; `tools/allowmarker.py` and
  `tools/test_allowmarker.py` in full; the marker and ignore code of all
  fourteen scanners at `ca61feb` and their removed code via the landing diff;
  `tools/floor.py`'s registry and plumbing, `.githooks/pre-commit`,
  `.github/workflows/ci.yml`; `tools/README.md` (headings, every allow/ignore
  line, § *Exempting a false positive*, § *Tests*); `docs/method/GUARDS.md`
  §§ *Granularity*, *Acceptance and deferment*; the template `floor.yml`'s
  hatch comment; `CHANGELOG.md`'s head and its `git log`; the repo's own
  `.*scanignore` files and `.atelier-floor.json`.
- **Exposure, disclosed.** (1) `git log --oneline` listings of `main` showed
  the *subjects* of records commits, among them `bb13b4e` ("…four marker
  divergences filed rather than unified"); I did not open them or any board
  item. (2) A tree-wide token census (`grep -rho` for scoped markers) ran over
  `docs/reviews/` and the record stores — output was marker tokens and, in one
  case, a file count; no record or verdict content was read. (3) The hook-plane
  floor run loaded the machine-local leakscan term list, as that plane does by
  design; nothing from it is quoted here. (4) The orchestrator's mid-pass note
  about the worktree merge; it carried no finding.
- **Scanner discharge.** `/security-review` is discharged by grounds: it reads
  the session's pending diff, which here is other passes' drafts and this
  brief, and this is a landed-delta review. The lens-4 read below is by hand.

### Lens 1 — approach and assumptions

The load-bearing assumptions, named: (a) the fourteen grammars were one
grammar with parametric differences; (b) the eleven ignore loaders were one
loader; (c) children consume the fourteen scanners from a whole `tools/`
directory, so a new sibling import resolves (`sys.path.insert` of the
scanner's own directory, now also added to blockscan, pointerscan and
reviewscan); (d) the extraction changes no behaviour.

(a) and (d): **confirmed at the regex and loader level.** At `cadcf4e` the
sixteen compiled patterns divide into exactly four parameters — scope (none /
one / comma-list), group name (`kind`/`rule`), separator (`[ \t]*`/`\s*`),
named reason or not — plus blockscan's apostrophe spelling, which is the same
character class. Nothing "won": every difference became an argument, and
`test_allowmarker` pins each scanner's `.pattern` to its pre-extraction
literal. The eleven loaders were textually identical apart from docstrings
(checked by AST extraction at the parent). The parity drive (lens 2) found no
output difference.

The structural difference the brief asks for is leakscan's comma-joined list
(`scope="list"`), correctly made a mode rather than a default. But the deeper
structural divergence sits **outside** the module and the extraction did not
reach it: the scanners disagree about what to *do* with a parsed scope — match
it against the finding's rule name (datescan, leakscan, secretscan, linkscan),
match it against the offending word (spellscan), or discard it and treat any
scoped spelling as the whole line (licenscan, pathscan, sizescan, pointerscan,
reviewscan check 1) — and reviewscan's check 2 reads its `deferral` scope
through a raw substring that bypasses the grammar entirely (AM1, AM4). The
module's thesis "every difference is a parameter here" is true of the regex
and false of the hatch as a whole.

(c) holds for every wiring the repo documents (`hooks.atelierTools` names a
directory; `floor.yml` checks atelier out). A child that had copied a single
scanner file would now fail with `ImportError` on `allowmarker`; the hook's
comment says children never vendor, so this is an assumption to carry, not a
finding.

### Lens 2 — correctness and quality

Re-run, not read (ledger below): all 28 `--selftest`s pass at both commits;
`tools.test_allowmarker` passes (25 tests); the full suite exits 0. The fixture
tree (every marker shape S01–S19, plus previous-line / next-line / cross-line
placements, plus six ignore-file variants) produced **byte-identical `--json`
output and exit codes at `cadcf4e` and `ca61feb`** for all thirteen tree
scanners and for blockscan `--check` in-tree. The single textual difference in
the whole diff was a temp-directory name inside stampscan's selftest banner.
No behaviour change landed.

The shared behaviour, as driven: a bare marker, a missing colon, an empty
reason, an upper-cased marker and a marker glued to a word exempt nothing
(S02, S08, S09, S17, S18 — all flagged by every scanner). A reasoned unscoped
marker exempts the line; a reasoned scope matching the rule exempts that rule
and keeps the others (leakscan S04, S14; linkscan S04). A marker on the
previous or next line exempts nothing. The same-line separator holds: a reason
on the line after the colon leaves the finding standing (datescan L03).
A scope naming no rule leaves the finding standing in the rule-matching
scanners (S13). Scoped markers of one scanner never touch another's findings
(leakscan over the secretscan fixture flagged every line). Unreasoned ignore
globs exit 2 in all eleven loaders; absent files load nothing.

Defects and weaknesses are AM1–AM4 and AM7–AM8. Quality notes: the pin test
`test_pins_cover_every_scanner_that_imports_the_module` globs `*scan.py`, so a
future non-scanner importer (floor.py, board.py) escapes the pin; the IndexError
in `test_single_scope_group_name_is_parameter` pins a trap as behaviour (AM8).

### Lens 3 — completeness and harvest

**No doc surface changed with the delta.** `git log cadcf4e..ca61feb` over
`tools/README.md`, `docs/method/GUARDS.md`, `CHANGELOG.md` and `docs/build/` is
empty. Consequences, each checked at `ca61feb`:

- `tools/README.md` has no entry for `allowmarker.py`; its § *Tests* line is
  still true. Every scanner section documents the **unscoped** form only —
  the file contains zero scoped spellings — while the tree carries about ninety
  live scoped markers (49 `reviewscan:allow:deferral:`, 18 leakscan, 6
  linkscan, 3 pathscan, 3 secretscan, 2 spellscan, 1 datescan). The scope
  vocabulary (rule name / word / ignored / `deferral`) is readable only from
  docstrings and code (AM5).
- Module docstrings: the eleven loader wrappers now carry a uniform
  "Single-sourced (115/080 part 2)" docstring; each scanner's grammar comment
  still describes its own pattern, consistently with the module. licenscan's
  `parse_allow` docstring promises a kind narrows; the code never compares it
  (AM4).
- `GUARDS.md` has no section titled *Allowances*; the grammar lives in
  § *Granularity* as `<guard>:allow: <reason>` plus the principle "a guard with
  more than one rule therefore supports rule-scoped allowance". It agrees with
  the module in principle and gives no grammar for the scoped form.
- The floor registry (`tools/floor.py`) mentions markers only in its remedy
  text (`<name>:allow: <reason>` / `.<name>ignore`); consistent, unscoped.
- `CHANGELOG.md` has no entry for the single-sourcing; its newest entry is
  2026-09-20, so the 2026-09-26, 2026-10-01 and 2026-10-03 runs are all
  unharvested — a class, not this delta alone (AM5, counsel).
- The child template (`docs/build/templates/workflows/floor.yml`) shows the
  unscoped hatch and "a root-relative path glob". Consistent with the code.
- The repo's own `.leakscanignore`, `.secretscanignore` and `.licenscanignore`
  headers say "gitignore-style globs"; the loader is `fnmatch` (AM6).

So the surfaces agree with one another and with the code **on the unscoped
grammar**, and are silent or wrong on the scoped grammar and the glob
semantics — exactly the two places the drive found divergent behaviour.

### Lens 4 — security and privacy (by hand, OWASP-aligned)

The allow marker is the hatch through every guard, so the read is: input
validation and fail direction of each malformed shape (A03 injection class,
A04 insecure design), output encoding of attacker-influenced text (A03), and
path handling of the loader (A01 broken access control).

- **Fail direction of malformed scopes — OPEN, whole line.** A scope with no
  reason (S05), an empty reason after the scope (S06), a space inside the scope
  (S07) and a list with a trailing comma (S15) each back off to the unscoped
  form, whose "reason" is the scope word, and **exempt every rule on the line**
  in every scoped scanner — datescan, leakscan, secretscan, spellscan,
  linkscan, pathscan and licenscan were all driven to it. For the two boundary
  guards this means a credential or leak-shaped value beside a mistyped scoped
  marker ships. The author pinned this in `test_allowmarker` as "existing
  behaviour, pinned not endorsed (reported to the principal)"; the drive
  confirms the live effect across all consumers (AM2).
- **Mentions exempt — OPEN.** An inline-code mention and a prose mention of the
  syntax on a finding-bearing line exempt it in thirteen scanners (S10, S11);
  only stampscan strips code spans before hunting markers (AM3).
- **Scope ignored — OPEN for licenscan.** Any scope text exempts the line in
  licenscan, a multi-kind guard (S13). Single-kind guards doing the same are
  within GUARDS' rule but silently diverge from the rule-matching scanners
  (AM4).
- **A reason-less hatch — OPEN.** reviewscan's check 2 accepts
  `reviewscan:allow:deferral:` as a bare substring: a marker with no reason,
  and one inside a code span, both passed a brief carrying a deferred section
  (AM1). No live marker in the tree is reason-less; one live brief carries the
  token inside a code span and so passes by mention alone.
- **Unknown scopes — CLOSED but silent** in the rule-matching scanners (AM10).
- **Reason text as output.** The reason's content is never captured or
  rendered — only its first character is tested — so a control or bidi
  character in a reason reaches no board row (S16 exempted exactly as a plain
  reason does; nothing echoed). The ignore-file loader does echo the offending
  **glob** verbatim in `IgnoreFileError`, and floor.py relays child output
  unfiltered; a U+202E in a glob reached stderr raw (AM9, note).
- **Ignore loader and the root.** `load_ignore_globs(root, filename)` takes
  the filename from a scanner constant, never from input, and reads
  `<root>/<filename>` only; globs filter the walk and can only remove files.
  It cannot be pointed outside the root by an ignore file. `--root` itself is
  the caller's, as before.
- **Markers in files the scanner never reads.** Every consumer tests the
  marker on the text it scans: the line (most), the first fifteen lines
  (sizescan), the item body or first line (pointerscan), the stamped block's
  lines (stampscan), the changed region (blockscan — the one place `\s*` is
  live, so a reason may sit on the next line of the same region). A marker in
  another file, or in an ignored file, exempts nothing. Confirmed by the
  previous-line / next-line placements.

### Findings

**AM1 — MODERATE.** reviewscan's `deferral` scope is matched as a raw
substring (`DEFERRAL_ALLOW in line`, `tools/reviewscan.py:255`), outside the
shared grammar and with **no reason required**. Probe: four briefs with a
deferred section and no verdict — reason-less marker, marker inside a code
span, control, properly reasoned — reviewscan failed only the control. This is
a fifteenth marker site the "fourteen sites" extraction missed, it contradicts
GUARDS rule (c) and reviewscan's own remedy text (`deferral: <reason>`), and
it is the most-used scoped marker in the tree (49 live, none reason-less
today; one live brief passes by a code-span mention).
*Counsel:* read it as `allowmarker.scope_of(ALLOW_RX, line, "kind") ==
"deferral"`, add a pin in `test_allowmarker`, and re-run reviewscan over
`docs/reviews/` before landing to see what the tightened read reds.

**AM2 — MODERATE.** A malformed scoped marker exempts the whole line in every
scoped scanner (S05, S06, S07, S15 — fixture-proven in seven scanners,
including both boundary guards). The grammar's optional scope group backs off
and the scope word becomes the reason. Pre-existing and author-disclosed in the
tests; recorded here because the single-sourcing is the first moment one fix
reaches all fourteen. The live-marker census found no marker currently in these
shapes in this repo.
*Counsel:* make a marker whose text after `:allow` contains a second colon but
no reasoned scope a **mention** (exempt nothing) — the fail-closed direction
GUARDS' "a marker with no reason exempts nothing" already states — and pin the
four shapes. It is a grammar change for every child; sweep the fleet's live
markers first.

**AM3 — MODERATE.** An inline-code or prose mention of the marker syntax on a
finding-bearing line exempts that line in thirteen scanners (S10, S11);
stampscan alone strips code spans first and its docs say a code span is the
safe way to document the syntax — untrue everywhere else. The scanners that
strip inline code (datescan, spellscan, linkscan) do so *after* `parse_allow`
has read the raw line.
*Counsel:* one shared helper that blanks code spans before `present` /
`scope_of`, called by every consumer; stampscan's `_strip_inline_code` is the
grounded precedent. Prose mentions stay inherent to the grammar and are the
documented residual.

**AM4 — MODERATE (licenscan) / minor (pathscan, sizescan, pointerscan,
reviewscan check 1).** The scope is parsed and discarded: `parse_allow(...) is
not None`. licenscan has several kinds and its docstring says a kind narrows,
yet `licenscan:allow:<anything>: reason` exempted a copyleft SPDX header
(S13). For the single-kind guards the whole line is the narrowest unit, which
GUARDS permits, but a typo'd or foreign scope then exempts silently where the
rule-matching scanners keep the finding — three behaviours for one spelling.
*Counsel:* licenscan compares the kind; the single-kind guards either refuse a
scope that is not their one kind or declare `scope=None` so the module's
parameter table says what the guard actually honours.

**AM5 — MODERATE (harvest).** The scoped grammar and the per-scanner scope
vocabulary are documented nowhere a user reads: `tools/README.md` carries only
unscoped spellings, `GUARDS.md` states the principle without the grammar, and
the delta added no README entry for `allowmarker.py` and no CHANGELOG line
(CHANGELOG is unharvested since 2026-09-20 across three runs — a class).
*Counsel:* one README section, *Allow markers and ignore files*, holding the
grammar, a scanner × scope-vocabulary table (rule name / word / none /
`deferral` / comma-list) and the glob semantics; link it from GUARDS
§ *Granularity*; a CHANGELOG entry for the single-sourcing.

**AM6 — minor.** Ignore files call themselves "gitignore-style"; the loader is
`fnmatch`: `*` crosses `/` (`docs/*.md` also exempts `docs/sub/a.md` — wider
than gitignore), a leading `/` never matches (silently exempts nothing), `!` is
a literal (silently no effect), `**` equals `*` and `**/x` misses a top-level
`x`. Fixture-proven on the `ignore` variant and by direct `ignored()` probes.
The repo's live globs are shapes where both readings agree.
*Counsel:* state the real semantics in the loader docstring and the ignore-file
headers, or refuse `/`-anchored and `!` lines at load time as the config error
they are (a glob that can never match is the unreasoned glob's sibling).

**AM7 — minor.** `datescan.ALLOW_MARKER_RX` and `pathscan.ALLOW_MARKER_RX` are
defined and never referenced; the docstring counts them among the fourteen
sites and the test pins them as load-bearing. `SEP_ANY_SPACE` is behaviourally
live for blockscan alone (multi-line region search); stampscan applies it per
line. *Counsel:* delete the two constants and their pins, and say in the module
docstring that `\s*` exists for blockscan's region search.

**AM8 — minor.** The group name is stated twice and the readers' defaults
disagree (`marker_rx` → `kind`, `scopes_of` → `rule`): `scopes_of(marker_rx(M,
scope="list"), text)` raises `IndexError` only when a marker is present, i.e.
mid-scan on the first marked file, with exit 1 and a traceback the floor would
read as a red with no rows. All ten live callers pass the group explicitly.
*Counsel:* fix the group name inside `marker_rx` or derive it from
`rx.groupindex`, and drop the IndexError pin.

**AM9 — note.** `IgnoreFileError` echoes the glob verbatim; a U+202E in a glob
reached stderr raw through floor.py. Low impact (committed file, run already
exits 2). *Counsel:* reuse publishscan's control-character stripping.

**AM10 — note.** A scope naming no rule is silently inert in the rule-matching
scanners; `--disable` validates rule names, the marker path does not.
*Counsel:* add "N marker(s) naming no rule" to the suppression tally.

**AM11 — note (process).** The review worktree did not carry the delta at
pass start; the brief's "review the paths at HEAD" presumed it did. Recovered
by a scratch clone at `main`; the orchestrator later merged. No delta defect.

### Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 5 MODERATE (AM1–AM5) · 3 minor (AM6–AM8) ·
3 notes (AM9–AM11).** The extraction itself is sound: byte-identical patterns,
identical loaders, no behaviour change across every shape driven, every test
and selftest green, both floor planes green. The findings are about what the
single-sourcing now makes fixable in one place and did not yet fix: a hatch
site it missed (AM1), the open fail direction of malformed and mentioned
markers (AM2, AM3), scopes that are parsed but not honoured (AM4), and a
grammar nobody documented (AM5). None blocks the landing.

### Re-run ledger

All at `ca61feb` (scratch clone `…/scratchpad/AM/probe`) unless stated;
parent `cadcf4e` at `…/scratchpad/AM/parent`. Dates `date -u`.

| Re-run | Command | Result |
|---|---|---|
| Selftests ×14, both commits | `python3 <tools>/<s>.py --selftest` | 28 × exit 0 |
| New tests | `python3 -m unittest tools.test_allowmarker` | 25 tests, OK |
| Full suite (once) | `python3 -m unittest discover -s tools -p 'test_*.py'` | exit 0, 15 m 16 s wall, started 04:20:03 UTC. My `tail -25` cut the `Ran N tests` line, so the count is not recorded; a second run is barred by the brief, so it stays unrecorded. A peer session's suite (`test_[a-h]*.py`, another prefix's clone) ran concurrently — environmental, noted. An accidental second invocation of mine was killed about ten seconds in (SIGTERM, before any test completed) |
| Floor, hook plane | `python3 tools/floor.py --plane hook --root <clone> --tools <clone>/tools` | exit 0; 12 ✅ enforced, 3 👁️ warn-only; nothing staged, so staged scanners scanned nothing |
| Floor, CI plane | `python3 tools/floor.py --plane ci --root .` | exit 0; secretscan 22 advisory (entropy class, known), leakscan structural-only by design; pathscan 1 and pointerscan 1 warn-only findings, neither in marker or ignore code |
| Fixture drive, parent vs HEAD | `run_fixture.py`: 6 variants × 13 scanners `--json`, blockscan `--check` in-tree | `diff -r` identical except a temp-dir name in stampscan's selftest banner |
| Fixture, markers variant | per-shape table (summarise.py) | S02/S08/S09/S17/S18 flagged everywhere; S05/S06/S07/S15 exempt whole line in 7 scoped scanners; S10/S11 exempt in 13, flagged by stampscan; S13 flagged in rule-matching scanners, exempt in licenscan/pathscan |
| Fixture, ignore variants | `ignore`, `star`, `dstar`, `bare`, `bidi` | `bare`/`bidi` exit 2 in all 11 loaders; `star`/`dstar` exit 0 except licenscan's repo-level `no-license`; `ignore`: trailing-slash dir, slash-crossing glob and spaced path exempted; leading `/` and `!` lines matched nothing |
| reviewscan deferral probe | four briefs, `--root <abs> <abs>` | reason-less and code-span markers pass; control fails; reasoned passes |
| sizescan | `--check --root <fix> --json`, both commits | identical, clean; a non-existent path exits 2 |
| Loader identity at parent | AST extraction of the 3 symbols × 11 scanners | identical bodies; conflictscan differs by docstring only |
| Live scoped-marker census | token grep over the tree | ~90 live; none in the AM2 shapes; 0 reason-less `deferral`; 1 code-span `deferral` mention in a brief |

### Follow-up checklist

- [ ] AM1 — route reviewscan check 2 through the shared grammar; pin; re-scan `docs/reviews/`
- [ ] AM2 — decide the malformed-scope direction (ruling: grammar change reaches every child)
- [ ] AM3 — shared code-span blanking before marker reads; stampscan precedent
- [ ] AM4 — licenscan compares its kind; single-kind guards declare `scope=None`
      or refuse foreign scopes
- [ ] AM5 — README *Allow markers and ignore files* section + GUARDS link + CHANGELOG entry
- [ ] AM6 — fnmatch semantics stated, or `/`/`!` lines refused at load
- [ ] AM7 — remove the two dead `ALLOW_MARKER_RX` constants and their pins
- [ ] AM8 — single-source the group name inside `marker_rx`
- [ ] AM9, AM10 — tally and sanitise, when a hand is in the module
- [ ] AM11 — brief template: verify the worktree carries the landing commit before spawning

### Reconcile

Phase 2, 2026-10-03, same reviewer (`claude-fable-5-1`). Written on receipt of
the sibling's text from the orchestrator, after phase 1 was committed
unrevised (`5e0cd68`). Phase-1 text above is untouched. Opened for this
section, at the worktree's merged HEAD: the intent record's § *`115/080`
part 2*, the board item `115/080` with its routing notes, the filed item
`115/230`, `tools/floor.py:680` and `tools/datescan.py:160–178`. The suite was
not re-run.

**Against the intent record and `115/080`.** The author's claims and this
pass's re-drive agree on the central one: no behaviour change. The author
records string-identical patterns (blockscan's one redundant backslash aside),
byte-identical output on the real tree and on 170 fixture comparisons; this
pass independently found identical output over six variants × thirteen
scanners plus blockscan in-tree. The author records the suite at 1,601 tests on
the worker and 1,604 OK on merged `main`; that supplies the count my ledger
could not, as the **author's** figure — my own run gives exit 0 only. The
binding constraint "share the mechanism, never the behaviour" explains why
AM2 was preserved rather than fixed, and I accept that as the right call for
this part; AM2 stands as a finding about the grammar, not about the
extraction.

**Against `115/230` (the four divergences the author filed).**

- *Item 1, scope with no reason widens* — is **AM2**. The author's precondition
  (count such markers across the estate before closing it) is the same as my
  counsel. This pass adds: the live effect is driven in seven scanners
  including both boundary guards; the class also covers an empty reason after
  the scope (S06) and a space in the scope (S07), which the item's wording
  does not name; and this repo's live tree holds none. The fleet count is not
  something this pass could make — it was barred from other repos.
- *Item 2, unscoped scanners accept scoped spellings* — I saw it (conflictscan
  and wrapscan S04) and left it as pinned behaviour in lens 2 without an ID.
  It belongs with **AM4** as the fourth of the "one spelling, several
  behaviours" cases; no new ID.
- *Item 3, two separator rules, two unused regexes* — is **AM7**. One
  correction to the item in the author's favour and one against: it is right
  that datescan's and pathscan's `\s*` regexes are unused; it lists stampscan
  beside blockscan as using `\s*`, but stampscan applies it to single lines,
  so blockscan is the only place the separator changes an outcome.
- *Item 4, docstring drift* — **my lens 3 missed this and was wrong on it.**
  I wrote that each scanner's grammar comment describes its pattern
  consistently with the module. `datescan.py:165–167` still says the sibling
  scanners treat the marker as a bare substring and accept an empty reason;
  that has been false since the 2026-08-05 tightening, and it now sits above a
  dead constant. Recorded as **AM12** below, formed at reconcile on the
  author's evidence.

**Not in the author's filing, and standing after reconcile:** AM1 (the
reviewscan substring — the record's "left on their own copies, deliberately"
list names publishscan's loader, wrapscan's sibling-marker strip and
`board.py`, not this site, so it reads as missed rather than chosen), AM3
(mentions exempt), AM4 (scope parsed and discarded), AM5 (no user-facing
grammar), AM6 (`fnmatch` against "gitignore-style"), AM8–AM10.

**Against the prior findings.**

- **LK1** (2026-08-09, MODERATE, reviewer argued MAJOR, unruled) is AM2's
  ancestor. Seeded question 1 answered: **yes, inherited** — the backtrack is
  in the shared builder for both scope modes. It is in the seven scoped
  consumers, not fourteen: the unscoped builders have no scope group to back
  off from. I held AM2 at MODERATE in phase 1 without knowing LK1's reviewer
  had argued MAJOR. On reconcile I keep MODERATE on my own evidence (no live
  marker in the shape here; the marker must be mistyped by the person placing
  it) and flag for the ruling that the blast radius is now every child's
  boundary guards through one function — the argument for MAJOR is stronger
  after single-sourcing than it was when LK1 was written, and the fix is now
  one edit.
- **LC1** (ruled fixed: licenscan's raw substring test replaced by
  `parse_allow`) — **AM1 is the same class, recurring** in reviewscan's check
  2. The LC1 fix did not sweep for sibling substring tests.
- **sizescan F2** (header-only, ruled fixed) — preserved. Seeded question 3:
  the header-only rule lives in sizescan's caller (`parse_allow(header)`), not
  in the grammar, and the delta did not touch it; its selftest passes at both
  commits. My fixture did not raise a sizescan finding, so this is the code
  path plus the selftest, not a drive — said plainly.
- **GA3** (the suppressed set is reachable only by grep) — AM10's counsel
  (tally markers naming no rule) is adjacent; no change to either.
- **LK5 / LK6 / the ignore-before-terms note** — the loader's ordering is in
  the callers and unchanged; `star`/`dstar` variants confirmed a blanket glob
  empties every path-based scan (licenscan's repo-level finding excepted).
  LK6 (a path self-exempting through marker text in a filename) was not
  driven; no claim either way.
- **FW1 / FW3 / FW8** — `filewalk.py` is untouched by this delta. FW3's point
  ("no test imports the shared module") does **not** recur: `allowmarker` has
  a 25-test file that pins every consumer.
- **RC1** — seeded question 5: the landing diff contains no line of the
  `+++ b/` staged parser (grep of `cadcf4e..5d087ec` over `tools/`); left for
  part 3 as the verdict anticipated.
- **BL1, SP1/BL3, HP8** — outside this delta's paths; nothing to add.

**Seeded questions 2 and 4.** (2) No scanner's grammar won; each difference is
a declared parameter — true of the regex. The differences that are *not*
parameters are consumer-side (AM1, AM4), which is this pass's lens-1 answer.
(4) `test_allowmarker.py` drives the module and each scanner's `parse_allow` /
`load_ignore_globs` by import; it never runs a scanner's `main()`. The CLI path
was proved twice — the author's 170 comparisons and this pass's fixture drive —
and neither proof is in the standing suite. *Counsel (not a new finding):* a
small standing fixture test through two or three scanners' CLIs would make the
"output unchanged" claim re-runnable rather than recorded.

**Findings formed at reconcile.**

**AM12 — minor (formed at reconcile, on `115/230` item 4).** Scanner comments
still describe the retired bare-substring acceptance: `datescan.py:165–167`
says five siblings exempt on any mention and accept an empty reason. False at
HEAD, and misleading to anyone reading the one scanner to learn the grammar.
My phase-1 lens 3 stated the opposite and is corrected by this entry.
*Counsel:* fold into AM7's edit — the comment goes with the dead constant.

**AM13 — note (formed at reconcile, on the item's own "coupling, stated").**
`tools/floor.py:680` says the scanners are "self-contained by deliberate design
… a peer can copy one alone". With `filewalk` and now `allowmarker` imported,
that is false twice, and the author recorded it without fixing it. A surface
my lens 3 did not list. *Counsel:* correct the comment with AM5's README
section, and state the real unit of reuse (the `tools/` directory).

**Overall, restated: PASS-WITH-FINDINGS — 0 MAJOR · 5 MODERATE (AM1–AM5) ·
4 minor (AM6–AM8, AM12) · 4 notes (AM9–AM11, AM13).** No phase-1 finding is
withdrawn. AM2 and AM7 coincide with the author's own `115/230` items 1 and 3;
AM12 and AM13 come from the author's record; AM1, AM3–AM6 and AM8–AM10 are new
to this pass. The one severity question I hand up rather than settle is AM2
against LK1's argued MAJOR.

## Folded sibling — released after the phase-1 findings were committed

The `.deferred.md` sibling the orchestrator held outside the worktree, folded in
verbatim at close; the reviewer met it only in phase 2.

# Deferred sibling — the shared allow-marker grammar and ignore loader (AM)

Held by the orchestrator outside the worktree and outside the harness
scratchpad. Released to the reviewer only after its phase-1 findings are
committed. Folded into the verdict file at close.

## 1. The queue pointer's own framing (author's words)

> - ⏳ **Rule-4 cold pass queued: the shared allow-marker grammar and ignore
> loader (`115/080` part 2).** The run authored this itself (its
> dispatched workers' output counts as the run's authorship). It was
> queued at landing, and the run neither takes it nor spawns a reviewer
> for it. *Tier:* Fable, the principal-named review tier, checked at
> selection. *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
> *Delta, scoped to paths:* `tools/allowmarker.py` and
> `tools/test_allowmarker.py` (both new), and the marker and ignore-file
> code in `tools/{blockscan,conflictscan,datescan,leakscan,licenscan,`
> `linkscan,pathscan,pointerscan,reviewscan,secretscan,sizescan,`
> `spellscan,stampscan,wrapscan}.py`. It landed on `main` on 2026-10-03,
> in merge `5d087ec`.
> *Intent record:*
> `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`.

## 2. Intent record and commissioning item (read in phase 2)

- `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`
- the board item named in the pointer

## 3. What the authoring run said to the orchestrator (channel, verbatim)

> a sixth refs-only pointer of mine is on main, docs/roadmap/160-doctrine-review-owed/480-rule-4-cold-pass-queued-the-shared-allow-marker-grammar.md, a code pass. No other detail.

Nothing else from that run was read by the orchestrator.

## 4. Prior findings and seeded questions (the orchestrator's, labelled)

Prior findings bearing on the marker and ignore code (unruled unless stated):

- LK1 (2026-08-09, MODERATE, reviewer argued MAJOR, unruled): a scoped leakscan
  allow-marker whose scope segment is malformed (no reason, or a space in a composed
  scope) silently re-parses as the unscoped form, exempting every structural rule on
  the line; the backtrack was commented as intended. If the shared grammar inherited
  it, it is now fleet-wide across fourteen guards.
- LC1 (2026-08-06, MODERATE, ruled fixed): licenscan accepted a bare or prose-mention
  marker by raw substring test; fixed to `parse_allow` per line. SD4 (ruled fixed):
  stampscan accepted a whitespace-only `narrow=`. Same class.
- GA1 (2026-08-05, minor; in effect decided by funding 115/080): ten copies of the
  reason-required loader. GA3 (note): the suppressed set is reachable only by grep.
- sizescan F2 (2026-07-14, ruled fixed): a prose mention of `sizescan:allow` anywhere
  exempted the whole file; fixed to header-only (first 15 lines). Whether the shared
  grammar keeps the per-scanner header-only rule is a parameter question.
- LK5 (note): an ignore glob disables term cover. LK6 (note): a path can self-exempt
  via marker text in the filename; C5R10 contradicts it.
- .leakscanignore memory (user-local, 2026-08-09): path globs filter before the term
  list on both planes, so a repo-wide `*` makes any term unreachable.
- FW1/FW3/FW8 (2026-09-25, unruled): the single-sourced file walk (`filewalk.py`,
  115/080 part 1) raises on an unenterable directory pre-3.14, has no test file, and
  seven of eleven readers skip an unreadable file silently. The routing note on
  115/080 (2026-09-27) tells part 2's taker to read FW1 and FW3 first.
- RC1 (2026-09-25, MAJOR, unruled): `conflictscan --staged` and `leakscan --staged`
  parse only a literal `+++ b/` header; the verdict names 115/080 parts 2–3 as the
  recurrence vehicle. HP8 (note): an inlined formula duplicates `similarity()`.
- BL1 (MODERATE): four scanners truncate lines at 8 KiB and only the prose tally
  says so. SP1/BL3: duplicate suppression across window seams is wrong both ways.

Seeded questions (the orchestrator's): (1) Did the shared grammar inherit LK1's
fail-open backtrack, and is it now in fourteen guards? (2) Which scanner's prior
grammar won where they differed, and is each difference a declared parameter? (3)
Is the sizescan header-only rule preserved? (4) Does `tools/test_allowmarker.py`
drive the grammar through each scanner's `main()`, or only the module? (5) Did the
delta touch the `+++ b/` staged parser (RC1) or leave it for part 3?
