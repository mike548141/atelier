# Cold pass — indexscan's date rule

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-17 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/810-rule-4-cold-pass-queued-indexscan-date-rule.md`.
**Why it earns a review:** `indexscan` is on the floor registry for every child (warn-only). The
delta adds a new finding kind that reads dates and times from index lines and file names,
changes the guard's allow-marker grammar to a scoped one, and adds a line-bound exemption form.
A guard is doctrine by function (rule 3).

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
  bodies** (the author's own account, including measurements over the session index); the
  subjects and `--stat` of later commits on the same files; `REVIEW.md` rules 1–4; three
  user-local templates — the ask halves of the 2026-10-16 expected-toolbox and scanner-rule-gates
  briefs and the whole expected-toolbox sibling, seeded questions included (another pass's
  framing); `tools/floor.py`'s indexscan entry and the declaration lines of the declaring indexes
  (grep only); the commissioning item's head line; filename-level greps of `docs/reviews/` (no
  file there opened); and its harness-loaded memory index and instruction files. It did not open
  the intent record, `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md` or any file
  under `docs/reviews/`. Its orchestrator passed it an instruction set and no evaluative content
  about the delta; what the orchestrator read is its own to disclose in its claim. Everything
  evaluative is in the sibling.

## What the work is

Landing commit and merge (diff the commit; review the paths at HEAD, `8acfff1` or later):

- `1c24781` (2026-10-16 08:27 UTC) — tools: indexscan flags an index line dated before the file
  it links (320/430); landed in merge `da3227d` (2026-10-16 08:53 UTC)

Delta paths: `tools/indexscan.py` (the module docstring's MISDATED bullet, THE DATE RULE and its
two following sections, the allow-marker section; `ALLOW_RX` now `scope="one"`, `DATE_KIND`,
`LEAD_LINK_RX`, `TEXT_STAMP_RX`, `NAME_STAMP_RX`, `Tally.dated_lines`, `parse_allow_scoped`,
`discover`'s marker filter, `_clock`, `_real_date`, `_entry_path`, `_misdated`, `check_dates`,
its call in `check_index`, the clean head, `--help` text, `--json` and selftest),
`tools/test_indexscan.py` (the `DateRule` class), `tools/test_allowmarker.py` (indexscan's pinned
`ALLOW_RX`), `tools/test_report.py` (two indexscan line pins) and `tools/README.md` (the date-rule
paragraphs, the exit codes and *What it cannot see*).

**Later commits on the same files — not this delta; do not attribute them to it.**
`tools/indexscan.py`, `tools/test_indexscan.py` and `tools/test_allowmarker.py` are unchanged
since the merge; confirm that. `72a68cc`, `f4afb7a` and `e3e8a4f` (2026-10-16) touch
`tools/README.md` or `tools/test_report.py` outside this delta's hunks (160/850, 830, 840). The
guard itself landed earlier as its own pass (160/700, from `8d10487`); its unlisted-entry rule is
that pass's subject, not this one's.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests and live
behaviour. The lenses organise it; they do not bound it. Non-goals are the only narrowing and are
themselves reviewable.

Derive, from `LEAD_LINK_RX`, `TEXT_STAMP_RX`, `NAME_STAMP_RX` and `_entry_path` at HEAD, exactly
which index lines are compared and which are not, independently of the delta's tests
(`EVIDENCE.md` § 15 is the reason). Pay attention to:

- **What counts as a dated line.** List markers and indentation; link text with leading
  emphasis, an icon or a status glyph before the date; reference-style links; angle-bracket and
  percent-encoded destinations, anchors and query strings; absolute and `../` destinations; a
  link into a subdirectory entry; destinations that land on `exclude=`d or unmatched names; the
  middle dot and its spacing; `UTC` and other zone words; `~` placement.
- **The comparison.** Date against date, time against time: which clock each side is in
  (`docs/method/CONVENTIONS.md`), what `HHMM` means in the file name (start) and in the line, the
  same-day rule, the midnight boundary, impossible dates and times, a file name with a counter
  instead of a time.
- **The direction rule.** The delta checks "not earlier" and states why. Say what that rule
  cannot catch, and whether the docs' list of blind spots is complete.
- **The marker grammar change.** `ALLOW_RX` moved to the shared grammar's `scope="one"`. Re-parse
  every existing `indexscan:allow` marker in the tree at `1c24781^` and at HEAD and say whether
  any changes meaning; check the colon-ending-entry special case in `parse_allow_scoped`; check
  that the line-bound form cannot exempt a line other than its own and that the unscoped form
  never exempts a date finding.
- **Bounded reading.** The index is now read three times; the docstring claims the date rule
  holds nothing beyond its findings. Check against the house's bounded-guard rules and the cap.
- **Reach.** `indexscan` is warn-only on both planes for every child. Say what a child with a
  dated index sees on its next run, and how a later flip to blocking would land. Measure only in
  this repo and in scratch fixtures; never run a scanner over another repo.

**Non-goals:** the unlisted-entry rule and the declaration grammar (160/700). How the date rule
uses the declaration is in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. The central one:
   that an index line can never be legitimately dated earlier than the file it links. Others:
   that a file name's date and time are its start; that the leading link is the entry the line
   describes; that a warn-only tripwire with no current findings earns its cost.
2. **Correctness & quality.** Read `check_dates`, `_misdated`, `_entry_path` and
   `parse_allow_scoped` whole, with the `DateRule` tests; diff `1c24781`. Build a line-shape table:
   shape, compared or not, finding or not, and a counter-example line wherever the behaviour and
   the docs disagree. Check whether each new test fails on `1c24781^` and whether the fixtures
   were derived from the regexes or from the same reading that wrote them.
3. **Completeness / harvest.** `tools/README.md`'s indexscan section; the declaring indexes in the
   tree (`tools/README.md`, `docs/decisions/README.md`, `instruments/README.md` and the session
   index — the last is barred until phase 2, see below); `tools/floor.py`'s indexscan entry and
   its `why=`; `docs/method/RECORD.md` on how the session index is kept; `CHANGELOG.md`.
4. **Security & privacy** — mandatory. Regex cost on adversarial long lines (the link and stamp
   patterns, the chunked reading of over-long lines); what finding text echoes from the index
   into public CI logs; that markers and declarations cannot be used to silence other guards.
   Build counter-examples from synthetic values only. `/security-review` is discharged by grounds
   (a landed delta; the pending diff is not the work) — say so, and deliver the code-altitude read
   by hand against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest tools.test_indexscan tools.test_allowmarker tools.test_report -v`;
  `python3 tools/indexscan.py --selftest`
- `python3 tools/indexscan.py --warn --root . .`, the same without `--warn`, and with `--json`,
  exit codes read explicitly (its output names entries and line numbers, not line text)
- the line-shape table, driven at `1c24781^`, `1c24781` and HEAD in a scratch clone over
  synthetic indexes, comparing stdout, stderr and exit code
- the marker re-parse at `1c24781^` and HEAD over every `indexscan:allow` marker in the tree
- the floor on both planes at HEAD; the full Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only git is fine.
  Probes and older checkouts go in a private clone under your session scratchpad, named by your
  prefix. Never open another `docs/reviews/2026-10-16-*` or `docs/reviews/2026-10-17-*` file — it
  is another pass's framing.
- **The session index is barred, and it is this rule's main real input.** Running the scanner
  over the tree is fine. Re-driving any claim about the index's content (how many of its lines
  are dated later than their file, and why) needs `docs/SESSIONS.md` itself: do that at phase 2,
  or with a script of your own whose output carries counts only and no line text, disclosed in
  the verdict. Never open the file before your phase-1 findings are committed.
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
`docs/reviews/2026-10-17-0930-indexscan-date-rule-cold.deferred.md`, the landing commit's and
merge's message bodies (read subject, stat and diff only), and the commissioning item `430` in
`docs/roadmap/320-child-filed-findings-via-pointing-up/`.

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/810-rule-4-cold-pass-queued-indexscan-date-rule.md
--also-exclude docs/reviews/2026-10-17-0930-indexscan-date-rule-cold.deferred.md
--also-exclude
docs/roadmap/320-child-filed-findings-via-pointing-up/430-no-floor-check-catches-an-orphaned-session-detail-file.md
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then append your
verdict below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier,
what you read), per-lens answers, the standing checklist V1–V7 each answered or discharged with
grounds, the line-shape table, findings with stable IDs (prefix `DM`: `DM1`, `DM2`, …) and
severities (MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line
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

## Verdict — phase 1 (DM), written 2026-10-17T23:58Z

### Provenance, repeated

- **Reviewer:** this session runs as **Fable 5.1** (`claude-fable-5-1`), the tier rule 4 names
  (ruling 2026-08-04); tier checked at selection, so the stop clause did not fire.
- **How spawned:** by a Mike-opened Claude Code **cloud** session (`claude-fable-5-1`,
  orchestrating; it opened on `claude-opus-5` and Mike switched it to Fable before any claim or
  pass). That orchestrator authored none of the delta or the brief and was not started or
  instructed by their authors. It forms no finding and writes no severity; it holds the
  `.deferred.md` sibling outside this checkout at a path I was not given, commits this phase-1 file
  before releasing the sibling, and received one operational note from Mike's watching session
  (model, queue scope, container facts, merge instruction — no evaluative content about any
  delta). The queue pointer's claim line discloses the same shape; I have not opened the pointer.
- **Author of the work:** the 2026-10-16 queue run named in the brief (an Opus orchestrator with
  dispatched workers). Not opened; the landing commit `1c24781` and merge `da3227d` were read as
  subject, `--stat` and diff only — never a message body (`git show --stat --format=%s`,
  `git diff 1b557dd 1c24781`).
- **Container facts that bear:** one checkout at `/home/user/atelier`, branch
  `claude/review-work-briefs-adj6ad`; no worktrees, no sibling repos, no estate root, no
  `~/.claude/`, no `gh`, no GitHub API from the shell. So: the CHANGELOG's "0 findings in … its
  siblings" and the brief's "never run a scanner over another repo" meet here — the sibling half
  is **not re-driven here (relayed)**. The hook plane's leakscan reds by design (no user-local term
  list; board `115/350`), so the **CI plane is the honest floor plane** and I ran both, saying so
  below. The checkout was a **shallow clone (depth 52, graft root `c824287`) when I started**:
  the delta commits were present as objects under remote-tracking refs but not ancestors of HEAD,
  so every "unchanged since" claim was first verified **by content diff**; the orchestrator
  unshallowed the checkout mid-pass and I re-ran the ancestry steps (ledger below). HEAD moved
  from `0aff4d8` to `74a7053f` during the pass (two commits, both under `docs/reviews/`); no delta
  surface changed between the two (`git diff --stat 0aff4d8 74a7053f -- tools/ CHANGELOG.md …`
  empty). Scratch: `/home/user/scratch/DM/` (probe scripts, logs, trees extracted with
  `git archive` at `1b557dd`, `1c24781` and HEAD — the extracted trees contain the barred files;
  none was opened). Private clone: made before the unshallow, so still shallow; I used
  `git archive` from the checkout instead, which needs no history.
- **What I read, in order:** `docs/method/REVIEW.md`, this brief, `docs/method/00-APEX.md`; then
  the five delta paths at HEAD whole (`tools/indexscan.py`, `tools/test_indexscan.py`,
  `tools/test_allowmarker.py`, the indexscan parts of `tools/test_report.py` and
  `tools/README.md`), the landing diff, `tools/allowmarker.py`, `tools/report.py` (the exit and
  render helpers), `tools/floor.py`'s indexscan entry and its Actions-annotation path,
  `docs/method/CONVENTIONS.md`, `EVIDENCE.md` §15, `RECORD.md` § *The session log*,
  `GUARDS.md` whole, `CHANGELOG.md` (the two indexscan entries), `docs/decisions/README.md` and
  `instruments/README.md` whole, `.githooks/pre-commit`, `.github/workflows/ci.yml` and
  `floor.yml` (the floor invocations), `.atelier-floor.json`, `tools/coldsweep.py --help`.
- ⚠️ **Exposure, disclosed.** No barred file was opened. The barred session index was read only
  by (a) the scanner and the shipped tests, as their normal run, and (b) my count-only script
  `/home/user/scratch/DM/count_only.py`, whose output is numbers, line numbers, marker kinds,
  declaration fields and ten-character hashes — no line text, no entry name, no reason (the
  brief's sanctioned shape). I saw commit **subjects** (never bodies) that name other passes: the graft
  root `c824287` ("review(TB): phase-1 verdict … 160/500") and two merges landing `72a68cc`,
  `f4afb7a`, `e3e8a4f`. `git status` showed another reviewer's brief file name as modified; not
  opened. Sweeps ran through `tools/coldsweep.py` with the brief's three `--also-exclude` paths;
  `--include-barred` was never used. `/security-review` was **not run**: the pending diff is this
  brief, not the work (the SL2 hazard), so the lens-4 code read is by hand below. The brief's own
  framing claim that the scanner's output "names entries and line numbers, not line text" is a
  little stronger than true — a `date-mismatch` detail echoes the line's date and time digits, and
  a `stale-allow` detail echoes the marker's entry word via `repr` — but neither is line text, and
  I relied on that only after checking it.

### Lens 1 — approach and assumptions

Load-bearing assumptions, named first and then attacked:

1. **An index line is never legitimately dated earlier than the file it links.** Attacked three
   ways. (a) *The real data:* over the session index at HEAD, 245 leading links are compared;
   0 are earlier by date, 237 equal, 8 later by date; of the 237 equal-date lines, 138 have an
   exactly equal time, 6 a later time, 0 an earlier time, 37 no time on the line, 56 no time in
   the file name (the retired `NN` scheme). The same figures at `1c24781^` (242 compared, 0
   earlier). Holds on the data. (b) *The decisions index:* its 10 dated lines all equal their
   file's date; the convention there is that the line mirrors the file name, not the ADR's
   **Date** field, so a ruling recorded the day after it was given would not fire. Holds by
   convention, not by necessity — the rule depends on index lines carrying the *file's* stamp.
   (c) *The remedy's direction:* when the two stamps disagree the rule blames the **line** ("fix
   the line's date or its link"), yet RECORD.md says a detail file's `HHMM` is the session's
   **start**; a file named by its creation time mid-session, against that rule, makes a true line
   look misdated. The disagreement is real either way, so the *finding* is sound; the *remedy
   text* presumes the file name is the truth (DM6).
2. **A file name's date and time are its start.** RECORD.md says so for session detail files
   (`HHMM` = start, UTC, `date -u`) and the decisions README says so for ADRs. Holds for the
   declared indexes. CONVENTIONS puts both stamps in UTC — file name by the identifier rule, line
   by the required `UTC` word — so the comparison is in one clock. A line written in a *local*
   date (NZ runs ahead of UTC) reads later, never earlier, so that frame break is invisible to
   this rule, which the docs do not say but which is the lenient direction.
3. **The leading link is the entry the line describes.** Holds on the real index (0 list items
   carry a dated link to a session entry anywhere but the leading token; 33 list items lead with a
   link to something outside the declaration, correctly skipped). It is a *shape* assumption,
   though, and the shapes it misses are wider than the docs name (DM4).
4. **A warn-only tripwire with no current findings earns its cost.** Cost measured: the third
   streaming pass over a declaring index of 200,000 undated lines costs ~1.7 s and ~125 MiB in
   total; over the real index it is unmeasurable. Value is prospective — the class occurring in
   the wild rests on `320/430`, which is barred until phase 2; the direction choice rests on the
   14 later-dated lines, which I measured. Earns its cost; the grounding of "the class exists" I
   can only read at phase 2.
5. **Brief framing attacked:** "a guard is doctrine by function" — yes (rule 3; it reaches every
   child through `floor.py@main`). The non-goal (the unlisted rule, 160/700) does not fence off
   this delta's risk; where the two rules share machinery (`_entry_path`, the marker grammar) I
   reviewed the shared piece and point one pre-existing defect at 160/700 (DM10).

### Lens 2 — correctness and quality

`check_dates`, `_misdated`, `_entry_path`, `parse_allow_scoped` and the `DateRule` class read
whole; the landing diff read whole. The code does what the docstring says on every shape the
docstring names; where it and the docs part company the table below has the row (DM1, DM3,
DM4, DM6). Honest about done vs stubbed: yes — the "cannot see" list is explicit, if short. One
overclaim at note strength (DM8). The comparison is correct: ISO dates compare as strings after a
real-date check; `HHMM` compares in minutes after a real-time check; the same-day rule and the
midnight boundary behave (S34–S36); a counter file has no time (S37). `_entry_path` does no
filesystem work — link destinations are pure string paths confined to `--root`. Bounded as
claimed: three streaming reads for a declaring index; `check_dates` holds its findings list (run-
wide cap honoured — 50,000 built, 150,000 counted on a 200k-finding index) and per-line locals.

**Tests.** Run at HEAD: 147 OK (`tools.test_indexscan tools.test_allowmarker tools.test_report`).
Run against `1c24781^` with HEAD's test file: of the 18 `DateRule` tests **13 fail or error and 5
pass** — the five that pass on code with no date rule are the negative-shape tests (counter file,
approximate time, impossible date, excluded/unmatched, leading-link-only), which cannot
discriminate alone; paired with the positive tests they pin behaviour. The `test_allowmarker` pin
and the `test_report` line pin both fail on `1c24781^` as they should. Fixtures were written from
the same reading as the regexes (EVIDENCE §15): the `~` approximate-time shape has **0 instances**
in the real index, so that test encodes a belief about a shape the data does not contain (DM7).

### Lens 3 — completeness and harvest

`tools/README.md`'s indexscan section, the CHANGELOG entry and the docstring agree with each
other and with the code (V5 below for the one exception). Mirror sites swept with coldsweep: the
floor registry's `why=` and comment still describe only the unlisted direction (DM5). Nothing
pre-existing was duplicated: the allow grammar comes from `allowmarker.py` (scope `"one"`, the
same shape five sibling scanners use), the walk from `filewalk`, the exits from `report`.
RECORD.md on the session index: append-only content, detail files named by start — the date
rule's remedies are all edits to an existing entry, which is fine at the commit that writes the
line and conflicts with the frozen-record stance for older lines (DM1). The declaring indexes:
four at HEAD (decisions, tools, instruments, sessions), as the README says; the session index's
live declaration carries **no `before=`**, so DM1 is latent in atelier and live only for a child.

### Lens 4 — security and privacy (mandatory)

`/security-review` discharged by grounds (landed delta; the pending diff is this brief). Code
altitude by hand, against the OWASP Top 10 classes that reach a stdlib file scanner:

- **Injection / log injection (A03):** the new finding text flows to stdout and, in CI, inside
  a `::group::` block. A GitHub workflow command must start a line with `::`; every finding line
  is indented two spaces, the entry comes from the directory walk and the declaration (no
  newline possible), the marker word from a single-space split and printed via `repr`, the dates
  from `\d` captures. `floor.py` annotates only the registry's `name`/`why` through `_wc`
  (percent-escapes `%`, CR, LF). No path for index text to forge an annotation. Verified by
  running the floor on a fixture under `GITHUB_ACTIONS=true`: the only `::` lines are the floor's
  own group markers.
- **Path traversal (A01):** `dir=` is rejected absolute or escaping `--root` (tests);
  `_entry_path` normalises destinations and returns None outside root (S20); link destinations
  never cause a file read.
- **Denial of service by input (A05/A06 class):** adversarial probe
  (`/home/user/scratch/DM/adversarial.py`, synthetic): 1 MiB `- [` with no `]` 0.09 s; 1 MiB
  destination with no `)` 0.14 s; `](` × 300k 0.10 s; `indexscan:allow:` × 60k on one line
  0.09 s; 1 MiB of `%` 0.51 s; 500k `%41` 0.22 s; 100k `<` 0.07 s; 1 MiB of middle dots 0.09 s;
  200k misdated items 2.69 s / 93 MiB with the cap holding; 200k undated items 1.66 s / 125 MiB.
  No super-linear pattern found; all regexes are anchored or guarded by a substring test.
- **Information exposure:** what reaches a public CI log is the index path, a line number, the
  entry's file name, two dates and possibly two times — all already public in a public repo. In a
  private child it reaches that child's own log. `--json` carries the same strings. Nothing is
  over-collected.
- **Markers and declarations silencing other guards:** every marker is word-anchored to its own
  scanner's name; a declaration is an HTML comment no other guard keys on; `exclude=` and
  `before=` narrow only this scanner and are counted. Holds. Within this scanner the unknown-kind
  widening is DM2.
- **Threat enumeration at design altitude:** the delta states bounded reading and fail-closed
  config, and names no threats for the new surface as such. Substance covered by the above;
  recorded as DM9 at note strength, since the house rule says an absent enumeration is a finding.

### Standing checklist V1–V7

- **V1 — no claim stronger than its evidence.** One at note strength: "many lines whose date or
  time is LATER" is 14 of 245 (DM8). The CHANGELOG's "0 findings in atelier" re-run true; "and
  its siblings" not re-drivable here, relayed. The brief's "output names entries and line
  numbers, not line text" is slightly over-tight (provenance above).
- **V2 — re-run every live-proven claim.** Done; ledger below. All reproduce at HEAD.
- **V3 — a changed rule swept to every mirror.** Not fully: `tools/floor.py`'s indexscan `why=`
  and comment (DM5). README, CHANGELOG, docstring, selftest and pins are swept.
- **V4 — one fact, one home.** The rule is stated in the docstring and the README catalogue, the
  house's standing pair for every scanner; the two agree. No new second source.
- **V5 — no internal contradiction.** One: `before=` is documented as making an entry
  "blameless" while the date rule still fires on that entry's lines (DM1). The "never touched"
  wording against the third read is a shade, not a contradiction: no finding, one more pass.
- **V6 — security and privacy.** Lens 4 above; scanner discharged by grounds, hand read done.
- **V7 — rule-4 provenance stated.** In the brief (its *Spawn provenance*) and repeated above.

### Line-shape table

Driven at `1c24781^` (pre), `1c24781` (land) and HEAD over synthetic indexes
(`/home/user/scratch/DM/shapes.py`; raw table `/home/user/scratch/DM/shapes.out`). **pre** is
clean on every row except where noted (its grammar read a scoped marker as an entry named
`date-mismatch:`, so S40/S41/S56/S65/S66 report `stale-allow` of that pseudo-entry at pre, and
S44 reports `stale-allow` plus `unlisted`). **land equals HEAD on every row** (the file is
byte-identical). "cmp" = counted in `dated_lines`; "fires" = `date-mismatch`.

| id | shape (file `log/2026-07-14-1200-x.md` unless said) | HEAD | docs |
|---|---|---|---|
| S01–S06, S08 | `-`/`*`/`+`/`1.`/`1)` markers, 2-space nest, tab | cmp, fires | agree |
| S07 | 4-space nested item under a parent | not compared | silent (DM4) |
| S09 | `-[` no space (not a list item) | not compared | agree |
| S10–S12, S55 | bold-wrapped link; bold, glyph or space before the date | not compared | implied |
| S13 | reference-style link + definition | not compared | silent (DM4) |
| S14–S19 | `<dest>`, `%2E`, `#anchor`, `?query`, `/root-abs`, `../back` | cmp, fires | agree |
| S20 | destination escaping `--root` | not compared; `unlisted` | agree |
| S21 | link into a dated directory entry (`match=*`) | cmp, fires on the dir | agree |
| S22, S23 | destination excluded by `exclude=` / unmatched by `match=` | not compared | agree |
| S24 | `2026-07-14·1100UTC` (no spaces) | cmp, fires | agree |
| S25–S27, S30, S31, S64 | time present but `-` sep, no zone, `NZST`, `1100~`, `~ 1100`, `utc` | cmp, time dropped, passes | silent (DM3) |
| S28 | `1100 UTC+12` (labelled deviation) | read as UTC, fires | silent (DM4) |
| S29 | `~1100 UTC` | cmp, passes | agree |
| S32 | `2500 UTC` | cmp, time None, passes | agree |
| S33 | `2026-02-30` | counted as compared, nothing compared | DM3 |
| S34 | `2026-07-13 · 2359` vs file `2026-07-14-0001` | fires | agree |
| S35 | `2026-07-15 · 0000` vs file `2026-07-14-2359` | passes | agree |
| S36, S61–S63 | equal time; same-day earlier; date-only vs timed file; later day | pass/fire/pass/pass | agree |
| S37 | `NN` counter file, line has a time | passes | agree |
| S38 | four-digit counter `-0001-` read as a time | fires | edge (DM4) |
| S39 | entry before `before=`, line earlier | **fires; `by_before`=1** | contradicts (DM1) |
| S40, S65 | scoped marker trailing, right entry (also `name/`) | exempt, `by_marker`=1 | agree |
| S41 | scoped marker **before** the link | not compared; `stale-allow` | misleading (DM6) |
| S42 | unscoped marker on the misdated line | fires + `stale-allow` | agree |
| S43 | `Date-Mismatch` (wrong case) on the line | fires + `stale-allow` | agree (noisy) |
| S44 | `indexscan:allow:slug: b.md why`, `b.md` unlisted | **exempts `b.md`** (pre: stale + unlisted) | silent (DM2) |
| S45, S46 | two links: lead earlier / lead fine, second earlier | fires once / passes | agree |
| S47–S49 | table row; blockquoted item; heading | not compared | S47 agree; S48/S49 silent |
| S50 | `dir=log match=*` then `dir=log/sub`; link into `log/sub/<dated>` | entry = `sub`, not compared; `unlisted: sub` | DM4 / DM10 |
| S51 | `<dest with a space>` | `unlisted` (dest cut at the space) | pre-existing (DM10) |
| S52 | CRLF line endings | cmp, fires | agree |
| S54 | `2026-7-13` | not compared | implied |
| S56 | scoped marker on a correctly dated line | `stale-allow` | agree |
| S58 | `~~~` fence | hidden; `unlisted` | agree |
| S59 | index inside the mapped dir (`dir=.`) | cmp, fires | agree |
| S60 | `2026-07-14T1100Z` (strict ISO form) | cmp, time dropped, passes | silent (DM4) |
| S66 | two misdated items, one marker | exempts its line only; L4 fires | agree |

### Findings

Severities: MAJOR / MODERATE / minor / note. Each carries its probe. Counsel is labelled and is
the reviewer's, not a decision (rule 3).

**DM1 — MODERATE — `before=` does not scope the date rule, and the docs say the opposite.**
`_entry_path` honours `match=` and `exclude=` only; a frozen-record entry (`before=`) that is
"blameless" for `unlisted` (docstring: "an entry whose name STARTS with an ISO date earlier than
this is blameless … Records written before the index was kept are not made to come clean by
rewriting history") is still date-checked, and the finding's three remedies — change the line's
date, change its link, append a marker to the line — are all edits to an entry that RECORD.md
holds append-only and that `before=` exists to leave alone. `by_before` counts the entry as
excused while a finding fires against its line (S39: `date-mismatch` with `by_before`=1). Latent
in atelier (the live session declaration has no `before=`; 0 compared lines fall before any
cutoff), live for any child that adopts with a `before=` and old dated lines, warn-only.
*Counsel:* either honour `before=` in `check_dates` (skip and count under `by_before`), or state
in the docstring and README that `before=` scopes the unlisted rule only and name the remedy
that is compatible with a frozen entry. The second needs the principal's reading of whether an
appended HTML comment is an "edit" of an append-only entry.

**DM2 — MODERATE — the grammar change widens what an unknown kind exempts, unstated and
untested.** At `1c24781^` the marker took no scope: `indexscan:allow:slug: b.md why` read
`slug:` as the entry and exempted nothing (reported `stale-allow`). At HEAD `discover()` routes
**every** kind other than `date-mismatch` into the unlisted exemptions, so the same marker now
exempts `b.md` (S44), and `Date-Mismatch:` on a misdated line is read as an unlisted exemption
attempt (S43). GUARDS rule (a) wants the narrowest allowance; the rule-matching scanners
(`secretscan`, `datescan`, `linkscan`, `leakscan`, `spellscan`) already make an unknown scope
exempt nothing, and `allowmarker.covers()` keeps the widening only for three scanners "until
115/230 is ruled, because refusing it would void any live marker written that way" — indexscan
has **no live scoped marker** (12 markers in the tree, all unscoped, parse identically under both
grammars), so that reason does not apply here. Neither the docstring, the README nor a test says
which behaviour was chosen. *Counsel:* an unknown kind exempts nothing and is reported
`stale-allow`; pin it with a test; or document the widening and point it at 115/230.

**DM3 — minor — the "dated index line(s) compared" count overstates what was compared.**
`tally.dated_lines` increments when both regexes match, before `_misdated` decides anything. An
impossible date (S33) counts as compared though nothing was; a line whose time is present but not
in the `· HHMM UTC` shape (S25–S27, S30, S31, S60, S64) counts as compared while its time is
silently dropped and only the date is checked. GUARDS rule (b) asks for counts that say what was
checked. On the real index this is 0 lines today (`text_dated_time_word_present_but_unparsed`=0)
— the defect is in the counter, not the data. *Counsel:* count after `_misdated` returns a
decision, and either report "time present, not compared" as its own tally or name it a blind
spot.

**DM4 — minor — the blind-spot list is shorter than the rule's blind spots.** The docstring and
README name four (too-late dates, slug, non-leading link, table rows). The table adds, each
reproduced: reference-style links (S13), list items nested at four or more spaces (S07),
blockquoted items (S48), headings (S49), text opening with emphasis or a glyph (S10–S12), a
strict ISO 8601 `T…Z` stamp (S60), a time labelled `UTC+12` read as plain UTC (S28 — a labelled
deviation under CONVENTIONS rule 2 read as the default), a four-digit counter read as a time
(S38), a marker past the 1 MiB chunk cut (A7/A8 — the docstring names only a *link* straddling
the cut), and an index that maps a directory with `match=*` and also its subdirectory (S50).
None has an instance in the real index (counts: 0, 0, 0, 0, 0 of each). *Counsel:* either list
them or state the rule's grammar positively in one sentence — *the item's first token is
`[YYYY-MM-DD[ · [~]HHMM UTC] …](dest)` at ≤ 3 spaces of indent; anything else is not read*.

**DM5 — minor (V3) — a mirror site was not swept.** `tools/floor.py`'s indexscan entry still
carries `why="a hand-maintained index names every file in the directory it maps"` and the
comment "the UNLISTED direction; listed-but-missing stays linkscan's and pathscan's". That `why`
is what `floor --list` prints on both planes (re-run: both rows read the unlisted sentence) and
what a `::error::` annotation would carry; a child sees `date-mismatch` findings under a reason
that does not mention dates. The registry is doctrine by function. *Counsel:* one clause in the
`why` and one in the comment; the fourth-requirement declaration beside it already fits the new
rule (it names drift, forbids nothing).

**DM6 — minor — the remedy text presumes the file name is the truth and does not say where the
marker goes.** "fix the line's date or its link" omits the third real cause: a detail file named
by its creation time rather than the session's start (RECORD.md), in which case the line is true
and the file is misnamed — the wording steers a reader towards changing a true stamp. "or mark
that line" does not say the marker must follow the link: a marker placed before it (S41) stops
the line being a leading link at all, so the misdated line **leaves the check** and the marker is
reported `stale-allow` with the text "its line is not a misdated link to that entry", which is
untrue of the line as written. *Counsel:* name the three causes; say "append the marker after
the link on that line".

**DM7 — note — test evidence tier.** 5 of 18 `DateRule` tests pass on `1c24781^` (the negative
shapes); the positive 13 discriminate. Fixtures mirror the regex grammar; the `~` approximate
shape has 0 instances in the real index, so its test is wiring evidence only (EVIDENCE §15).
Not a defect; recorded so the tests are weighed at their tier.

**DM8 — note (V1) — "many lines … LATER" is 14 of 245** (8 by date, 6 by time, measured with
the count-only script at HEAD; 14 of 242 at `1c24781^`). The direction argument stands — an equality
rule fires 14 times — "many" is loose.

**DM9 — note (lens 4) — no threat enumeration for the new surface.** The delta states bounded
reading and fail-closed config; it does not name what the new finding text trusts or where it
flows (attacker-influenced index text → stdout → public CI log). Hand read and probes find the
surface safe (lens 4 above); the house rule says the absence is itself the finding, so it is
recorded at note strength.

**DM10 — note, out of this pass's scope → 160/700 (the unlisted rule).** Two pre-existing
behaviours, identical at `1c24781^`, met while probing shared machinery: `_references.mark()`
stops at the first wanted ancestor, so a link into a file that is itself an entry of a second
declaration never lists the directory entry the first declaration wants — `unlisted` fires for a
directory the index links into (S50); and an angle-bracket destination containing a space is cut
at the space, so the file reads as unlisted (S51). Recorded here so the finding is not lost;
not counted against this delta.

**DM11 — note — a filled marker example in a prose code span is live.** `_unfenced` skips
fences, not code spans; the colon heuristic protects only the *placeholder* form. A README that
quotes `<!-- indexscan:allow: b.md why -->` in prose exempts `b.md` (pre-existing, both
versions); quoting the scoped form filled in produces a `stale-allow` at HEAD (noisy, not silent
— the better failure). The shipped README avoids both by using placeholders.
*Counsel:* say so beside the quoted-syntax rule, or skip code spans in `discover`/`check_dates`.

**DM12 — minor — one counter for two hatches.** `by_marker` (and `--json`'s `by_allow_marker`)
sums the unscoped unlisted exemptions and the line-bound `date-mismatch` exemptions. Atelier's
own run prints "12 by allow-marker"; nothing in that line says whether any date finding is being
exempted (none is — I had to write a count-only script to learn it). GUARDS rule (b): the
subtraction is reported *by mechanism*. *Counsel:* a breakdown, as `report.suppressed_line`
already supports for other scanners (`breakdown=`), or a second field.

### Overall

**PASS-WITH-FINDINGS — MAJOR 0 · MODERATE 2 · minor 5 · note 5** (12 findings). The rule does
what it says on every shape its docs name; the live-proven claims reproduce; no live marker
changes meaning. The two MODERATEs are undeclared scope choices with fleet reach — `before=` left
out of the date rule against its own documentation, and an unknown marker kind widened into an
exemption — both warn-only today and both the principal's to decide.

### Re-run ledger

| claim / step | how re-driven | result |
|---|---|---|
| Three core files unchanged since the merge | content diff `da3227d`→HEAD (shallow); `git log da3227d..HEAD -- <3 files>` after unshallow | identical; empty |
| README/`test_report` later commits are `72a68cc`, `f4afb7a`, `e3e8a4f`, outside this delta's hunks | `git log da3227d..HEAD` after unshallow; date-rule, exit-codes and `test_indexscan` pin hunks diffed `1c24781` vs HEAD | the three (plus their two merges); hunks IDENTICAL |
| Delta is `1c24781`, merged by `da3227d` | `show --stat --format=%s`; parents `1b557dd`, `b6df888`; ancestry after unshallow | confirmed |
| Targeted tests | `python3 -m unittest tools.test_indexscan tools.test_allowmarker tools.test_report -v` | 147 OK, 4.7 s |
| `--selftest` | `python3 tools/indexscan.py --selftest` | selftest OK, rc 0 |
| Scanner over the tree, three invocations | `--warn --root . .` / `--root . .` / `--json --root . .` | clean; rc 0/0/0; 4 declarations, 273 entries, 255 dated lines, 12 by marker, 44 by exclude, 0 by before |
| CHANGELOG "0 findings in atelier" | the run above | reproduces; "its siblings" **not re-driven here (relayed)** |
| New tests fail on `1c24781^` | HEAD test files copied beside the pre tree's tools, run there | 13/18 `DateRule` fail or error, 5 pass; both pins fail |
| Marker re-parse at `1c24781^` and HEAD | count-only script, both grammars, every declaring index | 12 live markers, all unscoped, hash-identical results; the README's placeholder line parses as a marker at pre and as none at HEAD |
| Line-shape table at the three versions | `shapes.py`, 60 shapes × 3 versions, json + human | table above; land ≡ HEAD |
| Bounded reading and the cap | `adversarial.py` | ≤ 0.51 s per adversarial line; 200k findings: 50,000 built, 150,000 counted |
| Reach: a child with a misdated index | fixture through `floor.py --plane ci/hook --tools tools`, and with `GITHUB_ACTIONS=true` | `✗ indexscan: 1 finding(s)` with remedy, `(--warn: advisory only …)`, state warn-only, rc 0 on both planes; no annotation (rc 0) |
| Floor, CI plane, HEAD | `python3 tools/floor.py --plane ci --root .` | rc 0; indexscan clean; pathscan 1 warn-only finding unrelated to this delta (a missing path named in an ADR) |
| Floor, hook plane, HEAD | `python3 tools/floor.py --plane hook --root .` | rc 1, BLOCKED by leakscan only (no user-local term list, by design — 115/350); indexscan clean |
| Full Python suite, once, foreground | `python3 -m unittest discover -s tools -p 'test_*.py'` | 1916 tests OK, 179 s |
| Declaring indexes are four | coldsweep `indexscan:maps`; per-index `--json` | decisions, tools, instruments, sessions |
| Session index content claims (barred) | count-only script, HEAD and `1c24781^` | figures in lens 1; **no line text read** |
| Shallow-clone misfires | ancestry re-run after the orchestrator's `--unshallow` | all delta commits and the three later commits are ancestors of HEAD; conclusions unchanged |

### Follow-up checklist

- [ ] DM1 — decide: honour `before=` in the date rule, or document the exclusion and the
      frozen-entry remedy (principal).
- [ ] DM2 — decide: unknown kind exempts nothing (+ test), or document the widening under 115/230
      (principal).
- [ ] DM3, DM12 — tally semantics: count after the decision; split the two hatches.
- [ ] DM4, DM6 — docstring and README: the positive grammar, the fuller blind-spot list, the
      three causes, "append after the link".
- [ ] DM5 — `tools/floor.py` indexscan `why=` and comment.
- [ ] DM9 — a threat line for the new surface, or a ruling that a scanner's bounded/fail-closed
      paragraph discharges it.
- [ ] DM10 — hand to the 160/700 pass or its follow-ups.
- [ ] DM11 — note beside the quoted-syntax rule.
- [ ] Siblings' "0 findings" — re-drive where the sibling repos are reachable.
