# Cold pass — the floor's advisory count scoped to its scanner, and three more unsoftenable pins

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-17 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/860-rule-4-cold-pass-queued-advisory-count-per-scanner.md`.
**Why it earns a review:** it changes how the floor reads the one number that carries a
scanner's non-blocking findings onto the board (a misread is either a silent zero or a
false count on every child's floor), and it widens the set of checks pinned as having no
advisory form — the line between what a child may soften and what it may not.

## Spawn provenance

- **Author of the work under review:** the queue run whose intent record is dated
  2026-10-16 15:01 UTC (an Opus orchestrator with dispatched workers; the pointer counts
  the worker's output as the run's authorship; the commit's trailer names a Sonnet
  model). Not opened here.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched on 2026-10-17
  by the Mike-opened Fable review session working in worktree `atelier-review-1017`, on
  Mike's 2026-10-16 answer that a fresh Opus session writes these briefs. It authored
  none of the delta. It is **off-tier for review, disclosed: it forms no finding and
  writes no severity**, and it stops after this brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that passes
  rule 4's criterion. If it runs as reviewer-plus-orchestrator, rule 4's off-tier
  conditions apply and are disclosed in the claim, the pointer and the verdict. The
  reviewer repeats its own provenance in its verdict.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This brief-writer
  read: its instruction file; the four queue pointers it was assigned (160/860–890) in
  full, and 160/500 in full as the shape of an append line (including that item's
  result line); the staging directory's file listing, and the first 50 lines of one
  peer brief of this batch (160/850) and its append, for shape; the landing commit's
  subject, `--stat`, full diff **and message body** (the author's own account); later-
  commit checks on the delta paths (none found); `tools/floor.py` around the `Scanner`
  fields, the registry's `board` entry and the advisory-count contract comment; three
  templates in full; `docs/reviews/` filenames and filename-level greps (no prior
  verdict opened); and grep-hit lines from a `coldsweep` sweep for the unsoftenable
  vocabulary, which included single lines of the commissioning items 115/290 and
  115/320, of other board items, of `CHANGELOG.md`, of ADR 0008 and of tools. It also
  holds its harness-loaded memory index, and, writing the other three briefs of its
  set, read those deltas' diffs, message bodies and parts of their code (instruments
  only). It did not open the intent record,
  `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md` or
  `docs/method/REVIEW.md`. What its orchestrator read is the orchestrator's to disclose;
  it passed on an instruction file, three templates and a list of taken prefixes, and
  no evaluative content. Everything evaluative is in the sibling.

## What the work is

Landing commit (diff it; review the paths at HEAD, `2f9cfe4` or later):

- `dc0ed0e` (authored 2026-10-16 16:02 UTC, committed 16:17 UTC) — floor: scope the
  advisory count to its scanner, pin three more unsoftenable checks. A cherry-pick of
  the worker's `fe4f20d`; it reached `main` directly, ahead of `783bdff` (the board
  commit that queued this pass).

Delta paths:

- `tools/floor.py` — `advisory_count_rx` (replacing `ADVISORY_COUNT_RX`),
  `_read_advisory_count`'s new signature and last-match rule, its one call site in
  `run`, the `Scanner.advisory_count` comment, and `_selftest`'s unsoftenable list
- `tools/test_floor.py` — the module docstring's item 2, `RegistryTest.UNSOFTENABLE`
  and its two tests, and the `AdvisoryCountContract` additions
- `tools/licenscan.py` — one comment naming the reader

No later commit touches these three files (checked with `git log dc0ed0e..HEAD`);
confirm that at your HEAD. The count lines the reader consumes are built by
`advisory_count_line` in `tools/secretscan.py` and `tools/licenscan.py`; those builders
are not the delta, but the contract between them and the reader is.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests and
live behaviour. The lenses organise it; they do not bound it. Non-goals are the only
narrowing and are themselves reviewable.

Probe, at least:

- **The reader against every writer.** For each registered scanner with
  `advisory_count=True`, derive from its source every line it can print to stdout, in
  order, on every exit path (clean, advisory-only, blocking, over-cap, stale marker,
  error). Is the count line always present, always last of its kind, and always in the
  exact wording the new whole-line pattern demands? What does a run that blocks early
  print?
- **What text a scanner does not control.** Paths, finding excerpts and marker
  reasons reach stdout. Which of them can contain a newline, a leading-space run, or
  the scanner's own name followed by the contract wording? Build cases from synthetic
  file names, including ones that place a whole contract-shaped line before *and*
  after the real one.
- **The last-match rule.** Is "the count is printed after every finding line" true of
  every writer at HEAD, and is that ordering pinned by any test or only asserted in a
  comment?
- **The `-1` signal.** A reworded writer now yields `-1` rather than a misread. Trace
  where `-1` lands (the board, the renderers, any exit code) and whether a child sees
  it as loud.
- **The unsoftenable set.** Seven names now appear in two hand-written lists (the
  selftest and the test class). Compare both with the registry at HEAD, with
  `floor.py`'s own docstring on which checks have no advisory form, with
  `tools/README.md`, `docs/method/GUARDS.md`, `docs/method/SECRETS.md` and ADR 0008's
  account of what may re-baseline. Which statement is now authoritative, and do the
  others agree?
- **The config door.** The new test asserts a child asking for an advisory state on any
  of the seven is a `ConfigError`. Is that rejection the registry pin itself, or a
  separate path that could diverge?

**Non-goals:** the decision that boundary and integrity checks have no advisory form at
all (a standing ruling). Whether the new list is complete, and whether its wording
matches that ruling, are in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Among
   them: that a scanner's captured stdout is the only text the reader sees; that a
   printed line is a stable enough contract between self-contained tools; that
   hand-written pin lists catch drift better than a derived one.
2. **Correctness & quality.** Diff `dc0ed0e` on the three paths and read
   `_read_advisory_count`, its call site and the writers whole. Build the writer table
   from *Scope*. Check the regex against `re.MULTILINE` anchoring, trailing `\r`, tabs
   versus spaces, the em dash as a non-ASCII literal, and output decoded with
   `errors="replace"`.
3. **Completeness / harvest.** Every surface that still names `ADVISORY_COUNT_RX`, the
   old unanchored wording, or the old four-name unsoftenable list; the `CHANGELOG.md`;
   whether children reading the floor at `main` need anything to change.
4. **Security & privacy** — mandatory. The count is how advisory secret findings reach
   the board. Can a committed file name make the board under-report a real advisory
   count, or hide a blocking finding behind a plausible count? Synthetic values only;
   never paste a key-shaped literal into the verdict, describe its shape.
   `/security-review` is discharged by grounds (a landed delta; the pending diff is not
   the work) — say so, and do the code-altitude read by hand against the OWASP
   catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest tools.test_floor -v`; `python3 tools/floor.py --selftest`;
  `python3 tools/secretscan.py --selftest` and `python3 tools/licenscan.py --selftest`
- the old-versus-new claim, re-driven in a scratch clone: `dc0ed0e^` against `dc0ed0e`
  on a temporary tree whose file names imitate the count line, recording the count each
  reader returns
- your own crafted outputs from *Scope*, fed to `_read_advisory_count` at HEAD
- mutation: in the scratch clone, give one of the seven an advisory form and confirm
  which tests fail
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`, and
  the hook plane as `.githooks/pre-commit` invokes it); the full Python suite once,
  foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only git is
  fine. Probes, mutated copies and older checkouts go in a private clone under your
  session scratchpad, named by your prefix.
- One heavy process at a time on a shared machine: the full suite at most once, in the
  foreground. Never point a scanner at any other repo on the machine. Never run an
  installed tool by bare name from `PATH`.
- `/security-review` reads the session's pending diff: discharge it by grounds for this
  landed delta, or keep the tree clean whenever you spawn it — never with this brief or
  its sibling dirty.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ English.
  Never quote a secret, placeholder token, email address or personal detail — this repo
  is PUBLIC; describe and locate instead. Counter-example file names that carry a
  key-shaped value are described by shape, not pasted.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer, this
brief's sibling `docs/reviews/2026-10-17-1010-advisory-count-per-scanner-cold.deferred.md`,
the landing commit's message body (the author's account; read subject, stat and diff
only), and the commissioning items:

- `docs/roadmap/115-guardrail-architecture-mike-commissioned/320-three-small-floor-test-and-contract-gaps.md`
- `docs/roadmap/115-guardrail-architecture-mike-commissioned/290-three-guards-describe-a-response-tier-their-code-lacks.md`

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/860-rule-4-cold-pass-queued-advisory-count-per-scanner.md
--also-exclude docs/reviews/2026-10-17-1010-advisory-count-per-scanner-cold.deferred.md
--also-exclude
docs/roadmap/115-guardrail-architecture-mike-commissioned/320-three-small-floor-test-and-contract-gaps.md
--also-exclude
docs/roadmap/115-guardrail-architecture-mike-commissioned/290-three-guards-describe-a-response-tier-their-code-lacks.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is
never barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then append
your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, what you read), per-lens answers, the standing checklist V1–V7 each
answered or discharged with grounds, the writer table, findings with stable IDs (prefix
`AV`: `AV1`, `AV2`, …) and severities (MAJOR / MODERATE / minor / note), an overall
PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger, and a follow-up
checklist. Then STOP and commit phase 1 unrevised before opening the sibling. Edit no
other file.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict: per-finding
notes against the seeded questions and the intent record, any finding formed at
reconcile marked as such, and the overall line restated. Never revise phase-1 text.
Then fold the sibling in below the reconcile and delete it.

Findings on self-authored doctrine are the principal's to decide (rule 3; a guard is
doctrine by function): record all, apply nothing; counsel per finding is welcome,
labelled and kept beneath it.

---

## Verdict — phase 1 (prefix `AV`), written 2026-10-18 00:20 UTC

### Provenance

- **Reviewer:** this session, running as **Fable 5.1** (`claude-fable-5-1`), the tier rule 4
  names (ruling 2026-08-04). Checked at selection; the stop clause did not fire.
- **How spawned:** by a Mike-opened Claude Code **cloud** session (`claude-fable-5-1`,
  orchestrating; it opened on `claude-opus-5` and Mike switched it to Fable before any
  claim or pass). That session authored none of the delta or the brief and was not started
  or instructed by their authors. It forms no finding and writes no severity; it holds the
  `.deferred.md` sibling outside the checkout at a path I was not given, commits this
  phase-1 text before releasing the sibling, and received one operational note from Mike's
  watching session (model, queue scope, container facts, merge instruction — no evaluative
  content about any delta). The queue pointer's claim line discloses the same shape; I have
  not opened the pointer. So the pass runs as reviewer-plus-orchestrator under rule 4's
  two conditions, both disclosed here before the findings.
- **Author of the work:** the 2026-10-16 queue run named in the brief; not opened.
- **What I read:** `docs/method/REVIEW.md`, this brief, `docs/method/00-APEX.md`; the
  landing commit `dc0ed0e` by `--format=%s --stat` and `git diff dc0ed0e^ dc0ed0e` on the
  three paths (never the message body); `tools/floor.py` (docstring, `Scanner`, the
  registry, the reader, `_load_scope`/`_load_flags` docstrings, `Config.validate`, `run`,
  `Result`, `render`, `_selftest`); `tools/secretscan.py` (both render paths, `_main`,
  `_selftest`, `Tally.summary`); `tools/licenscan.py` (§ TWO RESPONSES, both render
  paths, `_main`, `_selftest`); `tools/report.py` lines 145–260; `tools/test_floor.py`
  lines 1–130, 1290–1489, 1840–1879; `CHANGELOG.md` lines 1–90; ADR 0008 lines 175–219;
  `docs/method/SECRETS.md` lines 220–249; `docs/build/templates/CONTRIBUTING.md` lines
  55–94; `tools/README.md` grep hits and lines 478–491; grep hits in `tools/sizescan.py`,
  `.githooks/pre-commit`, `.github/workflows/ci.yml`; `tools/coldsweep.py --help`.
- ⚠️ **Exposures, disclosed.** (1) The branch's `git log` subjects name six other passes'
  verdict commits (HX, DM, BY, RN, EC, SX); I read the subjects, opened none of the files.
  (2) `git status` showed another reviewer's brief modified; not opened. (3) Reading the
  CONTRIBUTING template made the harness attach `docs/build/templates/CLAUDE.md` whole;
  nothing in it bears on this delta. (4) The coldsweep sweeps (run with the brief's exact
  `--also-exclude` list, never `--include-barred`) returned single grep-hit lines from
  board items 010/060, 020/150, 020/410, 115/090, 115/160 and 300/020; I opened none.
  Not opened: the sibling, the queue pointer, `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md`, any other `docs/reviews/` file, items 115/320 and 115/290, and
  the landing commit's body.

### Container facts, and what could not be done here

Cloud container: one full clone, no worktrees, no sibling repos, no estate root, no
`~/.claude/`. The checkout's HEAD advanced during the pass (7bbb5c2 → c9d8a0d) as the
orchestrator committed peers' phase-1 files; the three delta paths were byte-identical to
`dc0ed0e` at every HEAD I checked (`git diff --stat dc0ed0e HEAD -- <paths>` empty). The
local `origin/main` ref read fe020b1, one board commit past the 0aff4d8 the dispatch named;
neither touches the delta. `gh`'s token is invalid; nothing here needed it. Scratch and
private clones under `/home/user/scratch/AV/` (`clone` at the branch tip, `old` at
`dc0ed0e^`). No git command that writes ran in the shared checkout; the one file edited is
this brief. **Not re-driven here (relayed):** "whether children reading the floor at `main`
need anything to change" — no child repo exists in this container; answered from the design
(the hook and CI resolve reader and writers from one atelier checkout, so they move
together) and marked as such. The hook plane's leakscan refuses by design here (no
user-local term list, 115/350); the CI plane is the honest plane and both are reported
below. `/security-review` is discharged by grounds: it reads the session's pending diff,
which is other reviewers' briefs, never this landed delta — it was not run; the
code-altitude read is by hand against the OWASP/CWE output-neutralisation class.

### The writer table — every line a count-carrier can print, in order

Derived from source at HEAD and confirmed by runs (`p1`, `p3`, `p6`, `p8-ci`). Floor never
passes `--json` (it is in `FORBIDDEN_FLAGS`), so the captured stream is always the human
render.

**secretscan**, `render_human` (exit 0 unless a blocking finding, then 1):

1. clean of blocking findings: `✓ secretscan clean — …` · `  suppressed: …` (plus
   `    allow-marker breakdown:` / `    disabled:` lines when non-empty) · **the count
   line** · then, if any advisory finding: the 🟡 block — header, five fixed lines,
   one line per finding `     <PATH>:<line>  [advisory/<kind>] <rule> → <excerpt>  [id]`,
   four fixed lines, an over-cap line.
2. blocking: `✗ secretscan: N finding(s) — commit blocked.` · one line per blocking
   finding `  <PATH>:<line>  [<sev>/<kind>] <rule> → <excerpt>  [id]` · over-cap line ·
   blank · `  suppressed: …` · **the count line** · six fixed remediation lines · then the
   🟡 block as above.
3. **No count line at all** (reader returns −1): `--json`; an unknown `--disable` rule
   (`report.broken`, exit 2); on `--staged`, a git diff failure or an absolute path (exit
   2); on a tree, a missing target (exit 2); a reasonless `.secretscanignore` glob
   (`IgnoreFileError` via `guarded_main`, exit 2); any uncaught exception (traceback,
   exit 1).

**licenscan**, `render_human` (exit 0 unless a blocking finding, then 1):

1. no blocking finding: `✓ licenscan clean — …` · `  suppressed: …` · **the count line**
   · then, if any advisory finding: header, four fixed lines, one line per finding
   `     <PATH>:<line>  [advisory/<kind>] <message>  [id]`, two fixed lines.
2. blocking: `✗ licenscan: N finding(s) — … Publish blocked.` · one line per blocking
   finding · blank · `  suppressed: …` · **the count line** · three fixed lines · the 🟡
   block as above.
3. **No count line**: `--json`; root not a directory (exit 2); `IgnoreFileError` (exit 2);
   uncaught exception.

Three facts the table settles. (i) The count line is printed exactly once on every path
that reaches the report, zero included — "always present" holds only for those paths;
every early exit yields −1. (ii) **The count line is not last of its kind-adjacent text:
in both writers the advisory finding lines, which carry the flagged PATH, print AFTER
it.** The reader's docstring ("the count is printed after every finding line, so a stray
earlier match could never outrank it") is false for the advisory block in both writers.
(iii) The text a scanner does not control is the path (both writers), the excerpt
(secretscan; for the advisory rule it is a fixed `<N chars, entropy X>` form) and the
message (licenscan; fixed wording plus SPDX ids). Rule names, glob counts and marker
breakdowns are the scanner's own vocabulary or integers.

### Lens 1 — approach & assumptions

Load-bearing assumptions, named by me before the sibling:

- **A1. Everything the reader could match is printed before the count line.** False —
  table fact (ii). The last-match rule was chosen on this premise. See AV1.
- **A2. A finding line can never be a whole contract-shaped line because it continues
  past `finding(s)`.** False once the untrusted path contains a newline: `os.walk` (tree)
  and `report.unquote_c` (staged, 115/260) both deliver such a name with a real `\n`, and
  the writers print it raw, so one finding line becomes two physical lines, the first of
  which can be exactly the contract line. The repo's own toolchain made control-character
  names first-class on the read side without neutralising them on the write side. AV1.
- **A3. Captured stdout is the only text the reader sees.** True: one subprocess per
  scanner, `stdout=PIPE`, stderr uncaptured; the CRLF concern is moot because `text=True`
  normalises line endings on capture (re-driven, ledger R12). Holds.
- **A4. A printed line is a stable enough contract between self-contained tools.** Holds
  for drift: every tried misspelling, mojibake, replacement character, ASCII hyphen,
  nbsp and name variant returns −1, never a misread (P4). It does not hold against
  *forgery* from content the writer prints raw — a contract carried in-band on a channel
  that also carries untrusted text cannot be made safe by the reader's pattern alone.
- **A5. Hand-written pin lists catch drift better than a derived one.** Half true. A hand
  list catches a *softening* of a pinned check, which a derived list by construction
  cannot (P5a: selftest plus four tests fail). It does not catch an *omission*: a new
  `advisory=None` scanner, or a name dropped from the tuple, passes everything (P5b). The
  registry already states the two-directional principle for `warn_only` ("declared and
  derived must agree, in both directions"); the unsoftenable pin applies only one. AV2.
- **The brief's non-goal** (boundary and integrity checks have no advisory form at all)
  is a standing ruling and fences off nothing the delta carries; accepted as a narrowing.

### Lens 2 — correctness & quality

- The regex, read against the brief's list: `re.MULTILINE` makes `^`/`$` per line
  (verified); `[ \t]*` admits any indentation, which is what lets a five-space advisory
  line match (AV1) — but pinning two spaces would not help, since a crafted name can put
  the forged text on any physical line with any indentation; the em dash is a UTF-8
  literal matched against text decoded with `errors="replace"`, so a mangled byte
  produces −1, not a misread (P4); `\d` also matches non-ASCII digits and `int()` agrees,
  harmless since the writers print ASCII (P4, recorded, not a finding).
- The old-versus-new claim re-driven (R5): on the brief's tree the old reader returns 77,
  the new returns 1. On the newline-named tree the old reader (first match) returns the
  true 2 and the new reader (last match) returns the forged 0 — the delta moved the hole
  from "a forged line before the count" (needs only a file name) to "a forged line after
  it" (needs a newline in a root-level name), narrower to reach and worse in kind.
- Honest about done versus stubbed: yes; the CHANGELOG entry states the change plainly.
  Overclaim: the reader's docstring and the registry comment assert two invariants the
  writers do not keep (A1, A2). The `-1` docstring reads "if its contract line was not
  there", which conflates an early exit with wording drift; the render then says "the
  count contract has drifted" on a scanner that exited 2 before its report (AV3).
- The ordering claim is pinned by no test: the end-to-end test
  `test_a_path_that_reads_like_the_count_does_not_move_the_board` exercises a blocking
  (before) path only; no test places an advisory finding after the count line or any
  control character in a path.
- Tests: all green at HEAD (R1–R4, R11). The delta's six new or changed tests do what they
  say for the shapes they try.

### Lens 3 — completeness / harvest

- `ADVISORY_COUNT_RX`: zero hits outside barred paths (coldsweep). The two unanchored
  descriptions of the writer's line (`CHANGELOG.md:59`, `tools/README.md:456`,
  `tools/licenscan.py:55`) name the prefix form without the ` — reported, not blocking.`
  tail that the reader now requires; a maintainer who "aligns" a writer to the documented
  form trips −1, which is loud — recorded, not a finding.
- The old four-name list: gone from code; the prose lists (floor docstring, CONTRIBUTING
  template) match the registry and are pinned to it by `SoftenableListsPinnedToRegistry`.
  Mirror sites that still disagree: `tools/README.md:485` ("the fourth check with
  `advisory=None`" — it was the sixth when written on 2026-09-18 and is one of seven now)
  and ADR 0008's AP2 (six names, dated 2026-08-23; conflictscan entered the registry
  2026-09-18). AV5, AV6. `docs/method/GUARDS.md` carries no such list; `SECRETS.md` is
  consistent.
- `CHANGELOG.md` has the entry (lines 33–38). Children: relayed, see container facts.
- What exists and was ignored: the repo already neutralises control characters where it
  knows a line-oriented consumer is downstream — `_wc` for Actions `::` commands (newline
  ends a command) and the `\x1b` strip on a config `why`. The same class was not applied to
  the scanners' own printed paths, which this delta's threat model names as the untrusted
  text. AV1's remedy (b) is that existing pattern, applied one surface over.

### Lens 4 — security & privacy

Design altitude: the count is control data carried in-band on a stream that also carries
attacker-influenced text (committed file names, excerpts). That is the output-neutralisation
class (CWE-117 / CWE-150; OWASP's log-injection guidance) — the vectors are a newline, a
carriage return, or an escape sequence inside a name, each of which lets content pose as
the framing around it. The delta's regex closes the no-control-character case and leaves
the newline case open; `\x1b` sequences cannot forge the count (the pattern needs a line
start) but can still restyle the terminal the hook prints to, a pre-existing hygiene gap
outside this delta. The brief's two questions, answered by probe: **can a committed file
name make the board under-report a real advisory count — yes** (P1, P1b, P1l2, P2: a
root-level file or directory whose name is a forged zero line plus a newline turns
`🟡 … 2 advisory finding(s)` into `✅ … enforced`, JSON `advisory: 0`, on both planes and
for both writers); **can it hide a blocking finding behind a plausible count — no**
(`Result.failed` keys on the exit code, which no printed text can alter; P6 shows ❌ and
`BLOCKED by:` surviving a −1). No secret, personal datum or real key was used or is quoted
here: the probes used the suite's own synthetic digests and a key-shaped literal built
from parts, exactly as the delta's own test does. `/security-review`: discharged by
grounds above.

### Standing checklist

- **V1** — Two claims stronger than their evidence, both in the delta's own comments: the
  count is printed after every finding line (false for the advisory block) and a finding
  line never matches (false with a newline in the path). → AV1.
- **V2** — Every recorded claim in scope re-run; ledger below. All hold except the two
  ordering/matching claims, which are AV1.
- **V3** — The rule changed (the pinned set, the contract wording) and most mirrors agree;
  `tools/README.md:485` and ADR 0008 AP2 lag. → AV5, AV6.
- **V4** — The contract wording lives in three files by deliberate design (self-contained
  scanners) and is pinned from both sides by `AdvisoryCountContract`; the scanner's
  registry name and its `ADVISORY_COUNT_PREFIX` are tied end to end by the same tests.
  Discharged with that note.
- **V5** — The test module's docstring names "a botched harvest" as not re-baselinable
  while sizescan's advisory form drops `--check`, the flag that gates harvest integrity;
  `floor.py`'s parallel sentence says "a broken link". → AV4. The config door and the
  registry pin are one fact read in two places (P7: both spellings hit the same
  `ConfigError`), no divergence.
- **V6** — Lens 4 above; `/security-review` discharged by grounds.
- **V7** — Provenance stated in the brief and again above.

### Findings

**AV1 — MAJOR. The last-match rule rests on an ordering the writers do not keep, and a
newline in a committed root-level name forges the count line after the real one: the
board reads a silent zero, on both planes, for both count-carriers.**
Evidence: table fact (ii); P1 (tree plane, scanner prints `secretscan advisory: 2`, floor
renders `✅ secretscan  enforced`, JSON `advisory: 0`); P1b (the newline in a *directory*
name — every file beneath it forges a line); P1l2 (licenscan, root-level file, JSON 0
against a printed 2); P2 (hook plane in the private clone: `report.unquote_c` restores the
newline git quoted, same result); P4 ("forged AFTER real" → 0). The old reader returned the
true 2 on the same output; the delta's choice of *last* match is what selects the forgery.
Precondition, stated at its true strength: a root-level file or directory name containing
a newline, committed — legal on Linux and macOS and in git, exotic in practice, far more
plausibly adversarial than accidental; the repo's own 115/260 work shows it treats such
names as real input. Consequence: the under-reported count E6b's design calls its
organising defect ("silence and zero must not look alike"), losing the 🟡 and the number
from the board, `--json` and `floorfleet`. It cannot hide a block (lens 4). The suite has
no control-character path case and no advisory-after case, so the false invariant is
asserted in a comment and pinned nowhere. *Counsel, labelled, the principal's to decide:*
(a) reader — treat any count of matches other than exactly one as −1 (one line; a forgery
then renders 🔴 rather than a number; see AV3 for the note's wording); (b) writers —
neutralise control characters in printed paths and excerpts (git's own C-quoting, which
`report.unquote_c` already understands, is the natural spelling), the general fix and the
same pattern `_wc` applies to Actions commands; (c) structural — move the count out of
band (`--json` on a second stream, or the count on stderr), removing in-band framing
altogether. Options (a) and (b) together close this at low cost; (c) is the design-level
answer if the principal wants the contract to stop depending on what paths may contain.
Whichever lands, add the newline-named advisory case to `AdvisoryCountContract` for both
writers and both planes.

**AV2 — minor. The unsoftenable pin is one-directional.** P5a: giving `board` an advisory
form fails the selftest and four tests — the hand lists do their stated job. P5b: dropping
`conflictscan` from both hand lists fails nothing — the prose tests still pass because
prose and registry still agree, and neither tuple is compared to the registry. A new
`advisory=None` scanner joins the registry without the hand lists noticing, which is how
`board`, `conflictscan` and `licenscan` sat unpinned for one to two months until this
delta caught them up. The registry's own `warn_only` pin states "declared and derived must
agree, in both directions". *Counsel:* one equality assertion in `RegistryTest` and one
`check` in `_selftest`: the hand tuple equals `{s.name for s in SCANNERS if s.advisory is
None}`. The hand list stays (it is what catches a softening); the equality catches the
omission.

**AV3 — minor. The −1 note misdiagnoses every early exit as contract drift.** P6: a
reasonless `.secretscanignore` glob makes secretscan exit 2 before its report; the board
renders `❌ secretscan  enforced  (🔴 declares an advisory count and printed none — the
count contract has drifted, not the findings)`. Nothing drifted; the scanner refused to run
and printed its remedy. Every exit-2 and traceback path in the writer table produces this
line. The wording predates the delta; the delta's docstring ("−1 if its contract line was
not there") carries the same conflation into the reader's own account. Also recorded as
fact for the principal, not challenged: a −1 with exit 0 does not fail the floor
(`Result.failed` keys on `rc`), so the 🔴 is log-only on CI and the commit proceeds on the
hook — the 2026-08-04 ruling's expired-advisory shape, applied to drift. *Counsel:* emit
the drift note only when `rc == 0`, or word it "no count line — the scanner exited before
its report (rc N), or the wording has drifted".

**AV4 — minor. The test module's rationale contradicts the registry.** `tools/test_floor.py`
lines 12–16 say "a burned secret, a leaked personal fact, a committed conflict marker and a
botched harvest are not re-baselining problems". The harvest-integrity gate is sizescan's
`--check`, and sizescan's registry advisory form is the same argv without `--check` — a
botched harvest is exactly a thing a child may soften by declaration. `tools/floor.py`
lines 149–150 give the parallel sentence with "a broken link" (linkscan, which is pinned).
The two docstrings disagree with each other and the test one with the registry; the phrase
survived the delta's rewrite of that paragraph.

**AV5 — minor. `tools/README.md:485` calls conflictscan "the fourth check with
`advisory=None`".** When that sentence was written (2026-09-18) six entries already carried
`advisory=None`; at HEAD it is one of seven. A live doc's wrong ordinal on the exact set
this delta re-pins; the delta's harvest of mirror sites did not reach it.

**AV6 — note. ADR 0008's AP2 (2026-08-23) lists six no-advisory names and is one short
since conflictscan entered the registry on 2026-09-18.** The amendment names the registry
as the authority and is a dated record, so this is a reader trap, not a contradiction;
the CHANGELOG entry for this delta does not point at it. *Counsel:* a one-line dated
pointer under AP2, or leave it, as the principal prefers for dated amendments.

**AV7 — note. `test_a_child_cannot_ask_to_soften_any_of_them` tests the spelling the
doctrine is retiring and asserts only the exception type.** P7 shows the legacy list and
the C1 object spelling both hit the same `ConfigError` at `Config.validate`, so today the
test proves what it says and the door is the pin (one fact, two reads). When C1 phase 2
retires bare lists, a blanket rejection of the legacy spelling would keep this test green
while it no longer exercises the door. *Counsel:* pin the reason (`assertIn("no advisory
form", …)`) and use the C1 spelling.

### Overall

**PASS-WITH-FINDINGS — 1 MAJOR · 0 MODERATE · 4 minor · 2 note.**

Why not FAIL, stated so the principal can disagree: the delta does what 115/320 asked —
on the commissioning case the board now reads 1 where it read 77, every re-run holds, and
nothing here argues for unlanding it. The MAJOR is an invariant the delta asserts and the
writers do not keep, with a residual hole that is narrower to reach than the one closed
and worse in kind (a silent zero rather than an inflated number). That is follow-up work on
a guard, not grounds to revert. A genuine fork, surfaced rather than resolved: if the
principal holds that a guard landing with a false stated invariant is disqualifying in
itself, this reads as FAIL on the same evidence; I have given my reading and the grounds.

### Re-run ledger

- R1 `python3 tools/floor.py --selftest` → ok, 16 scanners, 0 failures.
- R2 `python3 tools/secretscan.py --selftest` → selftest OK. R3 `licenscan.py --selftest`
  → selftest OK.
- R4 `python3 -m unittest tools.test_floor -v` → 144 tests, OK, 37 s.
- R5 old-versus-new, private clones at `dc0ed0e^` and HEAD, on the brief's tree (two files
  named like the count line, one carrying a key-shaped literal built from parts): old
  reader 77, new reader 1 — the delta's claim holds. Same two readers on the newline-named
  tree: old 2 (true), new 0 (forged) — AV1.
- R6 crafted outputs to `_read_advisory_count` at HEAD (P4, 21 cases): drift shapes all
  −1; two real lines → last; forged-after → 0; forged-before → true count; name prefix or
  suffix → −1; leading zeros parse; non-ASCII digit parses.
- R7 P1/P1b/P1l2 (tree plane, `floor.py --plane ci`): forged zero on the board and in
  `--json` for secretscan (file and directory names) and licenscan (root-level file).
- R8 P2 (hook plane, `floor.py --plane hook` in the private clone with the newline-named
  file staged): forged zero; clone index and tree restored and verified clean.
- R9 P5a mutation (board given an advisory form): selftest fails on "board cannot be
  softened"; four tests fail (`RegistryTest` ×2, `SoftenableListsPinnedToRegistry` ×2).
  R10 P5b mutation (conflictscan dropped from both hand lists): selftest ok, 13 tests OK —
  AV2. Clone restored after each.
- R11 full Python suite, `ci.yml`'s own command, once, foreground → 1916 tests, OK,
  2 m 57 s. Instruments suite not run: the delta is Python-only.
- R12 `text=True` capture of a child writing `\r\n` → captured `\n`, reader 5; the CRLF
  −1 case is unreachable through the floor.
- R13 P6 (−1 trace): scanner exit 2 → floor `❌`, `BLOCKED by: secretscan`, JSON
  `rc 2, advisory −1`, drift note shown — AV3; synthetic `Result(rc=0, advisory=−1)` →
  `failed` False, mark 🔴.
- R14 P7 (config door): all seven, both spellings → the same `ConfigError` text.
- R15 floor CI plane at HEAD c9d8a0d on the shared checkout → exit 0; secretscan 🟡 23
  advisory, licenscan count 0, all else ✅/👁️. Hook plane as `.githooks/pre-commit` line
  82 invokes it → exit 1, `BLOCKED by: leakscan` (`--require-terms` with no local list —
  the container limitation, 115/350), every other line ✅/👁️.
- R16 coldsweep (brief's exclusions, no `--include-barred`): `ADVISORY_COUNT_RX` 0 hits;
  reader names 18 hits, all in the three delta files; unsoftenable vocabulary 61 hits,
  read for the mirror sites above.
- R17 `git log dc0ed0e..HEAD -- <three paths>` → empty at 7bbb5c2 and at c9d8a0d.

### Follow-up checklist (for the principal's decision; nothing applied)

- [ ] AV1 — choose among (a) exactly-one-match reader, (b) control-character neutralisation
      in printed paths and excerpts, (c) out-of-band count; add the newline-named advisory
      case to `AdvisoryCountContract` for both writers and both planes.
- [ ] AV2 — equality pin of the hand lists against the registry, in the test and the
      selftest.
- [ ] AV3 — condition or reword the −1 render note.
- [ ] AV4 — align the test module's rationale with the registry (and with `floor.py`).
- [ ] AV5 — fix the ordinal at `tools/README.md:485`.
- [ ] AV6 — dated pointer under ADR 0008 AP2, or an explicit decision to leave it.
- [ ] AV7 — pin the rejection reason and the C1 spelling in the door test.

### Reconcile

Written 2026-10-18 00:24 UTC, after the orchestrator committed phase 1 as `51679e6` and
placed the sibling in the tree. Phase-1 text above is unrevised. Opened at this step, and
nothing barred before it: the sibling; the queue pointer (160/860); the intent record
`docs/sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md` (its 115/320 section,
its close, and every line naming this delta, by grep); the commissioning items 115/320 and
115/290 whole; ADR 0008 lines 55–70 (Decision 2 as written); and, of the prior verdicts the
sibling names, only `docs/reviews/2026-08-09-0825-e6b-advisory-e3-fingerprint-cold.md`,
lines 226–247 plus grep hits, to reconcile its AB5 against AV1. No other barred file was
opened.

**Against the pointer and the intent record.** The pointer's claim line states the same
reviewer-plus-orchestrator shape my provenance states; no discrepancy. The intent record
says what the pointer and 115/320 say, and adds one fact that bears on the evidence trail:
`dc0ed0e` reached `main` by cherry-pick, which skips the pre-commit hook (115/340), so the
landing's own proof was the CI floor run, not a local hook — consistent with R15, where the
CI plane is the honest plane here too. 115/320's "Suite: 1,922, OK" was true at its commit;
R11's 1,916 reflects tree movement since (115/270 c removed tests), not this delta.

**Against the seeded questions** (a floor, not a fence; every answer below was reached in
phase 1 unless marked):

1. *Does every `advisory_count=True` scanner run through the capturing branch, on both
   planes?* Yes. Both planes share `run`; the only exits that bypass the capture are the
   guard blocks (scope outside the repo, scope resolving to nothing, not executable), each
   appending a `Result` with `rc 1` and the default `advisory 0`, which renders ❌ — and the
   `disabled`/`skipped` states, where no scanner ran and nothing should be read. No path
   prints straight through and reads nothing. Discharged.
2. *Does anything print after either `advisory_count_line` site, and can it carry a path?*
   Yes and yes — the writer table, fact (ii): the whole 🟡 advisory block, one path per
   finding, prints after the count line in both writers, on both render paths. → AV1.
3. *A newline-named file with a contract-shaped line after the real count — does it win
   under last-match where first-match read the real one?* Yes; this is AV1 exactly, formed
   and probed before this file was opened (P1, P1b, P1l2, P2, P4; R5 records the old
   reader reading the true 2 on the same output). Agreement between a seeded suspicion and
   a cold finding is recorded as a fact about the two, not as extra weight: the evidence
   for AV1 is the probes.
4. *Does anything stop a new boundary scanner entering the registry with an advisory form
   and in neither list?* Nothing mechanical, and the two halves differ. A new scanner with
   `advisory=None` left out of the hand lists is the omission P5b demonstrates and the AV2
   equality pin would catch. A boundary scanner *given* an advisory form at creation is a
   ruling, not a drift — the registry entry's comment is where the house records it
   (publishscan is the worked precedent); no list can know a new name's class in advance.
5. *ADR 0008 still says only the prose-hygiene checks may re-baseline — record or live
   statement?* Decision 2 stands as written at lines 63–66 and is amended beneath (AP2,
   2026-08-23), which is this repo's own convention for ADRs (the 2026-10-16 amendment says
   so in terms). It is a dated record, not a live statement; the live statement is the
   registry, which AP2 itself names as authority. What is now wrong is AP2's own six-name
   snapshot, one short since 2026-09-18 → AV6, unchanged. One thing learned here and added
   to AV4's account: the test module's "a botched harvest" is Decision 2's own phrase (line
   65–66), copied forward; `floor.py`'s docstring departed from it to "a broken link" when
   AP2 corrected that paragraph, and the test docstring did not.
6. *One source for the contract wording, or three copies kept equal by tests?* Three copies
   kept equal by tests, by design (self-contained scanners run as subprocesses) — V4 above.
   The tests are the equality; there is no single source, and the registry name is the
   fourth thing that must agree (`Scanner.name` versus each `ADVISORY_COUNT_PREFIX`),
   pinned end to end by the same tests.

**Against the prior verdict AB5 (2026-08-09, a note).** AB5 named this surface: "a
hostile filename could spoof the parsed count", and judged it of no impact *because* the
old reader took the first match and the only finding lines printed before the count were
blocking ones, so "such a run already exits 1 and ❌ outranks the count". It suggested
matching the full prefix or anchoring to line start when next touched. This delta is that
hardening — and in choosing the *last* match it inverted the premise AB5's "no impact"
rested on: the forgeable position moved from before the count (blocking lines, run ❌
anyway) to after it (advisory lines, run exit 0, board green). AV1 is AB5's residue made
live by the delta's own choice. This sharpens AV1's account; it does not change its
severity, which was set on the probes.

**Finding formed at reconcile:**

**AV8 — note (formed at reconcile). The four-name "can re-baseline" list is the same
one-directional shape as AV2's, and the author said so.** 115/320's close records "left out
of scope: publishscan is in neither 'can re-baseline' list though it has an advisory form";
pointerscan, harvestscan, pathscan and indexscan are likewise absent from
`test_hygiene_checks_can_re_baseline` and the selftest's `can re-baseline` loop. Disclosed
by the author, so not an overclaim; recorded so the AV2 remedy, if taken, is applied to
both lists in one edit rather than to one.

**Overall, restated:** **PASS-WITH-FINDINGS — 1 MAJOR · 0 MODERATE · 4 minor · 3 note**
(AV8 added at reconcile; nothing else moved).

## Deferred material — folded in at the verdict

The sibling `docs/reviews/2026-10-17-1010-advisory-count-per-scanner-cold.deferred.md`,
folded in verbatim at phase 2 and deleted from the tree, per `REVIEW.md` rule 1 ("split
for the duration, merged at rest").

# Sibling to the advisory-count-per-scanner cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-17-1010-advisory-count-per-scanner-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the
brief are committed.** Written 2026-10-17 UTC by the Opus brief-writer named in the
brief's provenance; it forms no finding. Fold this file in below the reconcile and
delete it at phase 2.

## Intent and commissioning records

- Intent record: `docs/sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md` —
  **not opened by the brief-writer**.
- Commissioning board items (single grep lines seen, never read whole):
  `115/320` (three small floor test and contract gaps; one line seen says the old
  pattern matches any `advisory: N finding(s)` text) and `115/290` (three guards
  describe a response tier their code lacks; lines seen name the four-name selftest pin
  and floor.py's "no advisory form by design" wording naming publishscan's exception).
- The landing commit's message body (read by the brief-writer), in summary: three gaps
  "from the 115/290 worker, checked before changing anything" — (1) `test_floor.py`'s
  head comment still said only prose-hygiene checks may re-baseline, rewritten to
  mirror `floor.py`'s docstring with the registry as authority; (2) conflictscan and
  board were pinned nowhere and licenscan only inside the count tests, now all three in
  both pinned sets plus a config-error test, "mutation-checked: giving conflictscan an
  advisory form fails both"; (3) cross-scanner attribution "cannot happen" because each
  scanner's output is captured separately, but a file named like the count line made
  the board read 77 off a blocking finding, "reproduced against the real secretscan".
  Trailer: a Sonnet model.

## Prior verdicts on these surfaces (named by filename grep, not opened, not exhaustive)

- `docs/reviews/2026-08-09-0825-e6b-advisory-e3-fingerprint-cold.md` — the only verdict
  whose text names the count contract (`AdvisoryCountContract` or the old pattern)
- `docs/reviews/2026-07-28-1204-c1-advisory-cold.md`
- `docs/reviews/2026-08-06-0903-licenscan-e1e2-cold.md`
- `docs/reviews/2026-07-26-2215-floor-local-seam-cold.md`
- `docs/reviews/2026-08-09-0823-floor-render-batch-cold.md`

## The pointer's own lens hints

None. The pointer is refs-only.

## Overlap with sibling passes of this batch

- 160/840 (licenscan's advisory tier) and 160/850 (sizescan's size advisory removed)
  have briefs written this batch by another brief-writer; both touch the advisory
  vocabulary and licenscan or sizescan's softenability. Their briefs were seen only as
  filenames (and the first 50 lines of the 160/850 brief). A runner should not charge
  this delta with what those commits changed.
- The publishscan exception named in `floor.py`'s docstring is outside this delta's
  hunks but inside the claim the test docstring now makes.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. The body says cross-scanner attribution "cannot happen" because output is captured
   per scanner. Is every `advisory_count=True` scanner run through the capturing branch
   in `run`, on both planes, or does any path print straight to the child's stdout and
   then read nothing?
2. The last-match rule rests on "the count is printed after every finding line". The
   two writers each call `advisory_count_line` at two sites. Does anything print after
   either site (a stale-marker summary, an over-cap note, a remedy line), and can that
   later text carry a path?
3. A file name containing a newline followed by a full contract-shaped line: printed
   after the real count (for example in a trailing section), would it now win under the
   last-match rule where the old first-match rule would have read the real one?
4. The two unsoftenable lists are hand-written on purpose ("so making one of them
   softenable fails a test instead of quietly redefining the list"). Does anything stop
   a new boundary scanner being added to the registry with an advisory form and to
   neither list?
5. ADR 0008 still says only the prose-hygiene checks may re-baseline, and the new test
   docstring says the registry, not prose, is the authority. Is an ADR a record that
   stays, or a live statement that is now wrong?
6. The whole-line pattern hard-codes the em dash and "reported, not blocking." in a
   third file. The comment calls it the scanners' own wording; is there one source for
   that wording, or three copies kept equal by tests?
