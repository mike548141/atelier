# Cold pass — sizescan's size advisory removed, and the hatches it leaves inert

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-17 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/850-rule-4-cold-pass-queued-size-advisory-removed.md`.
**Why it earns a review:** it removes a signal from a floor guard every child runs,
rewrites which of that guard's hatches still exempt anything (one of them on the
harvest-integrity gate), reports a new class of "inert" hatch, and edits
`docs/method/RECORD.md`'s account of what keeps the session index lean.

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
  160/790, 160/800 and 160/860; the landing commit's subject, `--stat`, diff on the
  doctrine, comment and pin paths and the first 220 lines of the `tools/sizescan.py`
  diff, **and message body** (the author's own account, with principal quotes); the
  merge's re-merge diff stat (board and record files only); two 2026-10-16 briefs in
  full as templates; `docs/reviews/` filenames and filename-level greps (no prior
  verdict opened); the title lines of the commissioning board items; grep-hit lines
  naming the retired advisory in `CHANGELOG.md`, `tools/README.md` and two tests,
  and naming sizescan in `docs/method/RECORD.md` and `tools/floor.py`; and its
  harness-loaded memory index. It did not open the intent record,
  `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md` or
  `docs/method/REVIEW.md`. What its orchestrator read is the orchestrator's to
  disclose; it passed on an instruction file, three templates and a list of taken
  prefixes, and no evaluative content. Everything evaluative is in the sibling.

## What the work is

Landing commit (diff it; review the paths at HEAD, `b50db0c` or later):

- `72a68cc` (2026-10-16 15:28 UTC) — sizescan: remove the size advisory, and name
  the hatches it leaves inert (115/270 c); landed in merge `da85210` (2026-10-16
  15:45 UTC), whose own changes beyond the commit are board and record files only

Delta paths: `tools/sizescan.py` (read whole at HEAD; about 680 lines changed),
`tools/test_sizescan.py`, `tools/test_report.py`'s sizescan pins and round-trip,
`tools/README.md`'s sizescan section, two passages of `docs/method/RECORD.md` (the
session-index bullet and the cold-content signal paragraph), and comments in
`tools/pins.py` (`MAX_CLAUDE_MD_BYTES`) and `tools/blockscan.py`
(`MAX_MAPPED_FILE_BYTES` and the BOUNDED MEMORY docstring).

The commit builds on `f9ccba8` (2026-10-16, no hatch silences the cold-content gate;
its own pass, 160/790). Its parent is `2e2da81`, the base of two sibling commits
(`f4afb7a`, `e3e8a4f`) merged before it; `e3e8a4f` also edits `tools/test_report.py`
and `tools/README.md`. No later commit touches the delta paths at the time of
writing; confirm at your HEAD.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests
and live behaviour. The lenses organise it; they do not bound it. Non-goals are the
only narrowing and are themselves reviewable.

Build the full hatch table from the code at HEAD: every marker spelling the shared
allow grammar accepts (unscoped, each scope in `FINDING_KINDS` including the
retired `size-advisory`, an unknown scope, no reason, a body-only mention, a
leftover `budget=N`), every `.sizescanignore` glob shape, on every file class the
tool walks (the roadmap, the other current-truth names, each archive store, a store
outside the default directories). For each: does it exempt anything, is it reported
as inert, how is it counted on the `suppressed:` line and in `--json`, and what did
`72a68cc^` do with it. Then the scope change: which files the tool reads, and how
far into each, before and after; is any file now unread that a gate used to see?
Check `--check` and bare exit codes on each class, the `--json` shape against every
consumer (the floor's registry entry and its advisory form, tests, anything that
read `reference` or `over`), and the per-finding line pins. On the doctrine side:
what each edited `RECORD.md` passage now says detects the defect it describes, and
whether the rest of `RECORD.md` agrees; whether the reworded `pins.py` and
`blockscan.py` comments still ground their ceilings without the number they used to
cite. **Non-goals:** the principal's decision to remove the advisory (quoted in the
delta) — but what the removal leaves undetected, and how the delta says so, is in
scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Among them: that reporting an inert hatch is safer than accepting or rejecting
   it; that keeping a retired scope name is needed to stop a stale marker widening;
   that "caught at review" is a real detector for prose-shaped cold content.
2. **Correctness & quality.** Read `tools/sizescan.py` and its tests whole at HEAD;
   diff `72a68cc`. Record the hatch table from *Scope* with a counter-example line
   wherever the code and the docstring disagree. Check that the new tests would
   fail on `72a68cc^` for the reason each test names.
3. **Completeness / harvest.** Every surface that still names the size advisory,
   the reference points, the budget marker or "line count is advisory": the README,
   `docs/method/` (RECORD, GUARDS, PROPAGATION), the templates and create-repo skill,
   `CHANGELOG.md` (is an entry owed, and do older entries now read as current?),
   `test_allowmarker.py`, and children that may carry a now-inert marker.
4. **Security & privacy** — mandatory. The privacy angle is small; the integrity
   angle is not. Hunt for any marker or glob that now exempts an archive store's
   harvest-integrity check where it did not before, or stops exempting one where it
   did, and for any file a gate no longer reads. Fixtures from synthetic content
   only. `/security-review` is discharged by grounds (a landed delta; the pending
   diff is not the work) — say so, and deliver the code-altitude read by hand
   against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest discover -s tools -p 'test_sizescan.py' -v`, the same for
  `test_report.py`, `test_allowmarker.py`, `test_pins.py` and `test_blockscan.py`;
  `python3 tools/sizescan.py --selftest`
- sizescan at `72a68cc^`, `72a68cc` and HEAD in a scratch clone, bare and with
  `--check`, over a synthetic fixture tree carrying every row of your hatch table:
  compare stdout, exit code and `--json`
- `python3 tools/sizescan.py --check --root . .` on this repo at HEAD, exit code
  read explicitly
- the floor on both planes at HEAD; the full Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only
  git is fine. Fixture trees, older checkouts and probes go in a private clone
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
brief's sibling `docs/reviews/2026-10-17-0955-size-advisory-removed-cold.deferred.md`,
the landing commit's message body (read subject, stat and diff only), and items
`270` and `330` in `docs/roadmap/115-guardrail-architecture-mike-commissioned/`
(the commissioning item, and a finding filed at the same merge on a passage this
delta edits).

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/850-rule-4-cold-pass-queued-size-advisory-removed.md
--also-exclude docs/reviews/2026-10-17-0955-size-advisory-removed-cold.deferred.md
--also-exclude
docs/roadmap/115-guardrail-architecture-mike-commissioned/270-three-defects-found-adding-finding-ids.md
--also-exclude
docs/roadmap/115-guardrail-architecture-mike-commissioned/330-record-md-rotation-trigger-has-no-signal.md
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never
barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, the standing
checklist V1–V7 each answered or discharged with grounds, the hatch table, findings
with stable IDs (prefix `SZ`: `SZ1`, `SZ2`, …) and severities (MAJOR / MODERATE /
minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger, and a follow-up checklist. Then STOP and commit phase 1 unrevised
before opening the sibling.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict:
per-finding notes against the seeded questions and the intent record, any finding
formed at reconcile marked as such, and the overall line restated. Never revise
phase-1 text. Then fold the sibling in below the reconcile and delete it.

Findings on self-authored doctrine are the principal's to decide (rule 3; a
guard is doctrine by function, and `RECORD.md` is doctrine): record all, apply
nothing; counsel per finding is welcome, labelled and kept beneath it.

---

## Verdict — phase 1 (written 2026-10-18 UTC, before the sibling was opened)

### Provenance, repeated

- **Reviewer:** Claude Fable 5.1 (`claude-fable-5-1`), the principal-named tier (ruling
  2026-08-04), checked at selection; the rule-4 stop clause did not fire.
- **Spawn:** dispatched by a Mike-opened Claude Code **cloud** session (`claude-fable-5-1`,
  orchestrating; it opened on `claude-opus-5` and Mike switched it to Fable before any claim
  or pass). That session authored none of the delta or this brief and was not started or
  instructed by their authors. It forms no finding and writes no severity; it holds the
  `.deferred.md` sibling outside the checkout at a path this reviewer was not given, commits
  this phase-1 text before releasing the sibling, and received one operational note from
  Mike's watching session (model, queue scope, container facts, merge instruction — no
  evaluative content about any delta). The claim line in the queue pointer discloses the same
  shape; the pointer was not opened. The brief-writer's own exposure is disclosed above.
- **Container:** a cloud container — one checkout (a full clone, unshallowed), **no
  worktrees, no sibling repos, no estate root, no user-level Claude directory**. `gh` is on
  PATH with an invalid token; nothing here needed it. python3 3.13, node v22, git. 4 CPUs
  shared with up to five other reviewers; every heavy process below ran alone and in the
  foreground. Scratch: `/home/user/scratch/SZ/` (fixtures, driver, logs, private clone).
- **Checkout worked in:** `/home/user/atelier`, branch `claude/review-work-briefs-adj6ad`,
  HEAD `fe72b22` when this pass began (another pass's phase-1 commit `0dd1bfda` landed on
  the branch during the run — expected). The clone's `origin/main` ref resolves to
  `fe020b16`; the orchestrator named `0aff4d8`; both are ancestors of HEAD and the branch
  adds only review commits. The seven delta paths are byte-identical at `da85210`, `0aff4d8`
  and HEAD (`git diff --stat` empty). **No worktree was used and no git command that writes
  was run in the checkout.** Older code was taken from a private clone
  (`/home/user/scratch/SZ/clone`) with `git archive` of `tools/` at `2e2da81` (= `72a68cc^`),
  `72a68cc` and HEAD; the HEAD extraction was `cmp`-identical to the checkout's `sizescan.py`.
- **What was read:** `docs/method/REVIEW.md`, this brief, `docs/method/00-APEX.md`, the
  repo `CLAUDE.md`; `tools/sizescan.py`, `tools/test_sizescan.py` and `tools/allowmarker.py`
  whole at HEAD; `docs/method/RECORD.md` whole; `tools/README.md` lines 655–780 at HEAD plus
  its `72a68cc` hunks; the `72a68cc` diff on all seven paths (`git diff 72a68cc^ 72a68cc`,
  never a bare `show`); subjects and stats only for `72a68cc`, `da85210`, `f9ccba8`,
  `e3e8a4f`, `f4afb7a`; the merge's stat against both parents and its CHANGELOG-only hunk;
  `tools/floor.py`'s sizescan registry entry and selftest lines; `tools/test_floor.py`
  150–165; `.githooks/pre-commit` 1–90; `ci.yml` (grep); `docs/method/GUARDS.md` 225–295;
  board item `115/230` whole and the `115/` directory listing (titles; `270` and `330` not
  opened); `110/100` lines 110–130; `tools/test_report.py`'s round-trip helper and sizescan
  pins; `tools/indexscan.py` lines 1–45; `.sizescanignore`, `.wrapscanignore`, `.gitignore`;
  grep hits only in `CHANGELOG.md`, `tools/test_allowmarker.py`, `tools/floorfleet.py`.
  Templates (`docs/build/templates/`), `skills/` and `docs/method/` other than `RECORD.md`
  were grepped for sizescan: no hits.
- ⚠️ **Exposure, disclosed.** (1) `docs/SESSIONS.md` is rule-2 barred; a grep for the
  indexscan declaration printed its first three lines (an `indexscan:maps` declaration and
  two `indexscan:allow` lines naming two 2026-07-22 record files). No session entry was
  read; nothing in those lines bears on this delta. A slip, by this reviewer, while checking
  whether indexscan covers the session index. (2) `git log` on the branch showed five other
  passes' verdict-commit subjects; none opened. (3) One coldsweep hit was `docs/ROADMAP.md`'s
  index line for this pass's pointer — the title line only. (4) `tools/__pycache__/` exists
  in the checkout, written 2026-10-17 23:09–23:11 UTC, before this pass began (2026-10-18
  00:03 UTC); it is gitignored and not this reviewer's — every Python run here set
  `PYTHONDONTWRITEBYTECODE=1`. Not opened before this point: any other `2026-10-16-*` or
  `2026-10-17-*` review file, `drafts/`, `withdrawn/`, `ROADMAP-DONE.md`, `docs/sessions/`,
  the queue pointer, `115/270`, `115/330`, the sibling, or any delta commit's message body.
- **Sweep:** `tools/coldsweep.py` with the brief's four `--also-exclude` paths exactly as
  given, seven patterns (every name the retired advisory carried); never `--include-barred`.

### Load-bearing assumptions, named first (lens 1)

The delta's own framing, tested rather than taken:

- **A1 — "Nothing a gate relied on is now unread."** Holds. Before and after, the
  cold-content gate reads only `ROADMAP.md` and the integrity gate only `*-DONE.md` /
  `*-ARCHIVE.md`; both are still streamed whole (table rows R24–R25, A15, A17). What moved
  to header-only (15 lines) are the four other hot-path names, which never gated.
- **A2 — "Keeping `size-advisory` in `FINDING_KINDS` is needed to stop a stale marker
  widening."** Holds, and it is the shared grammar that makes it so: `allowmarker.covers`
  treats a scope naming *none* of the kinds as the unscoped form (its docstring calls this
  "not endorsed", the class of board `115/230` item 1). Probe A05 (retired scope, live
  store: still gates) against A06 (a typo'd scope, live store: exempt, counted as an
  allow) is the difference the retained name buys. But the protection covers one spelling
  only — every other unrecognised scope still widens, and the delta's documentation says
  the opposite (**SZ1**).
- **A3 — "Reporting an inert hatch is safer than accepting or rejecting it."** Defensible:
  silent acceptance is the defect the delta names; rejecting (exit 2) would red children's
  floors on a non-defect. The cost is that an inert hatch has no expiry or escalation, so
  the "remove it" in the report is advice nobody is made to act on (**SZ10**, note).
- **A4 — "Caught at review" is a real detector for prose-shaped cold content and for a
  session index regressing to a flat log.** Does not hold as written. No review, scan or
  session rule reads `SESSIONS.md` or an all-open `ROADMAP.md` for shape: cold passes are
  barred from the index until phase 2 (rule 2, `coldsweep`'s default exclusion), `indexscan`
  checks that the index names every mapped file and that dates are plausible (its docstring,
  lines 1–45) — not entry shape — and the one routine reader, the next session's start,
  tails the index with no rule telling it to act. The tool docs say so honestly ("nothing in
  this tool points at it"); `RECORD.md` does not (**SZ2**).
- **A5 — "The removal changes no exit code anywhere."** Holds on 75 fixture rows × 3 modes
  at `72a68cc^` vs `72a68cc` (zero changes), and by construction: exit 1 keys on `gated`,
  which was already cold-content-or-live-marker only. The estate-wide count in the CHANGELOG
  entry (29 repos) is **not re-driven here (relayed)** — no sibling repo exists in this
  container, and the brief forbids pointing a scanner at one anyway.

### Per-lens answers

**1. Approach & assumptions.** The removal implements a recorded ruling and the brief
names that decision a non-goal; it is honoured as one. What the removal leaves undetected
is stated plainly in `tools/sizescan.py` and `tools/README.md` ("the only pointer to
prose-shaped cold content… gone"), which is the honest shape. `RECORD.md` substitutes the
word "review" for the lost detector in two places and leaves "nothing fires when a file
bloats again — so it carries a signal" standing a paragraph later, now untrue for bloat
(SZ2). The retained-name design (A2) is a local patch over a shared fail-open grammar
with an open item (`115/230`); patching locally is reasonable while that item waits, but
the docs then overclaim what is inert (SZ1).

**2. Correctness & quality.** Code and docstring agree everywhere the hatch table was
driven except the two overclaims (SZ1, SZ4) and one wrong explanatory sentence in the
report (SZ5). New ≡ HEAD on every row. The 90 tests at HEAD pass; 26 of them fail against
the `72a68cc^` module — 15 for exactly the reason each test names (the advisory line
present, `reference`/`over` in the finding, `SIZE_REFERENCE` present, the inert tally
absent, `files_allowed` 2 not 1), 11 by `TypeError`/`KeyError` on the new `inert`
parameter and JSON key, which proves presence of the feature rather than the behaviour
named. `test_check_exits_1_through_every_hatch_and_says_so` and
`test_sizescanignore_glob_does_not_exempt_the_gate_and_is_named` pass on both — they are
`f9ccba8`'s pins, insensitive to the "and inert" wording. The `test_report.py` pins and
round-trip match the rendered lines byte-for-byte (run, not read). No overclaim of
done-vs-stubbed found in the delta itself.

**3. Completeness / harvest.** Surfaces that still named the advisory: `tools/README.md`
and the module docstring now carry it as history only (correct); `CHANGELOG.md` carries a
`Removed` entry — landed in the merge commit, not in `72a68cc` (SZ6); the same-day
2026-10-16 "no hatch silences" entry beneath it still says the three hatches "quiet the size
advisory", acceptable in an append-only log but worth knowing; `test_allowmarker.py` pins
`FINDING_KINDS` with the retired name (intended); templates and the create-repo skill
carry no sizescan hatch at all (clean); `docs/method/GUARDS.md` and `PROPAGATION.md` do not
name sizescan (clean by absence). Left behind: `RECORD.md` line 57 still says an index
"outgrows its budget" (SZ3); board item `110/100` still lists `sizescan:budget` as a live
reasonless exemption (SZ7); atelier's own `.sizescanignore` glob exempts nothing a walk can
reach and its comment states a purpose `f9ccba8` already retired (SZ11). Children that may
carry a now-inert marker: **not checkable here (relayed)**; the CHANGELOG says two across
the estate; this repo has zero (`--check --root . .` at HEAD: `0 inert hatch(es)`).

**4. Security & privacy.** Design altitude: the delta *narrows* what is read (four hot
names header-only), adds no new input class, and keeps the two gates' read set unchanged.
Integrity hunt, from the table: no marker or glob exempts an archive store now that did
not before, none stops exempting one that did (A01–A22, G01–G08 old ≡ new on exempt
status); no file a gate used to read is unread (A1). The one live-and-silent hatch on the
integrity gate — an unrecognised scope — is pre-existing (A06 identical at `72a68cc^`) and
is the subject of SZ1 because the delta now documents it as inert. Code altitude, by
hand against the OWASP Top 10 classes that fit a stdlib file scanner: no shell, no eval, no
network (injection: none); targets resolve against `--root` via the shared
`report.resolve_targets` (path handling: unchanged); reads are streamed with fixed caps
and `_read_header` stops at 15 lines (resource exhaustion: improved); the new regex
`sizescan:budget\s*[=:]?\s*(\d+)` runs over a 15-line header bounded at 8 KiB per line
(no catastrophic backtracking surface); `--json` adds repo-relative paths and hatch
labels only (disclosure: nothing new). Fixtures: every probe here was synthetic; the
delta's tests likewise. `/security-review` **discharged by grounds**: it reads the
session's pending diff, and in this shared checkout the pending diff is other reviewers'
briefs, not the landed delta; nothing here was aimed at it.

### The standing checklist

- **V1 — No claim stronger than its evidence.** Two bites: SZ1 ("everything else is
  inert and named" — an unrecognised scope is live and unnamed) and SZ2 ("caught at review"
  — no detector exists). Minor: SZ4 (a budget marker on a glob-skipped store is never
  named), SZ5.
- **V2 — Re-run every recorded "live-proven" claim.** Re-run: every test file the brief
  lists, `--selftest`, the full suite, both floor planes, the repo-wide `--check`, and the
  table. Not re-drivable here: the CHANGELOG's 29-repo count (relayed; see A5).
- **V3 — Changed rule swept to every mirror site.** Swept: README, docstring, CHANGELOG,
  tests, `pins.py`, `blockscan.py`, templates, skills, `docs/method/`. Missed by the delta:
  `RECORD.md` line 57 (SZ3, same bullet it edited), board `110/100` (SZ7), the repo's own
  `.sizescanignore` comment (SZ11).
- **V4 — One fact, one home.** The retired reference numbers (~300/~250/~200) survive as
  history in three places and as the live grounding of `MAX_CLAUDE_MD_BYTES` in `pins.py`,
  honestly labelled "nothing here reads that number" (SZ9, note). Acceptable.
- **V5 — No internal contradiction.** Three doc layers disagree on what still exempts:
  `_inert_hatches`' docstring and the tests say "or a scope naming no kind"; the module
  docstring and README say "only two hatches… unscoped or `harvest-integrity`" (SZ1).
  `RECORD.md`'s edited paragraph: "nothing fires when a file bloats… so it carries a
  signal" against "does not report line count at all" (SZ2). `RECORD.md` line 57 against
  the delta's own sentence five lines later (SZ3).
- **V6 — Security & privacy on every review.** Lens 4 above; `/security-review` discharged
  with grounds.
- **V7 — Rule-4 pass states its spawn provenance.** Brief: yes (its *Spawn provenance*
  section). Verdict: above.

### The hatch table (HEAD code; `72a68cc^` → `72a68cc`; HEAD ≡ `72a68cc` on every row)

Fixture: 75 rows under `/home/user/scratch/SZ/rows/`, each run bare, `--check` and `--json`
at the three SHAs (675 invocations; log `hatchtable.out`, raw `hatchtable.json`). Codes:
`gate` finding that fails `--check` · `adv` size-advisory finding, exit 0 (old only) · `0`
silent · `X` exempt and counted "by sizescan:allow header" · `K` skipped wholesale and
counted "by .sizescanignore" · `+h` named on the cold finding · `+I` named inert and
tallied · `+a` counted as an allow though it exempted nothing (old) · `+k` counted as a
glob skip though the file still gated (old) · `–` not read.

| Header hatch (lines 1–15) | `ROADMAP.md` with `[x]` | `ROADMAP.md` all-open, 400 lines | other hot file, 400 lines | archive store, live item | archive store, clean |
|---|---|---|---|---|---|
| none | gate → gate | adv → 0 | adv → 0 | gate → gate | 0 → 0 |
| `sizescan:allow: <reason>` (unscoped) | gate+h+a → gate+h+I | 0+a → 0+I | 0+a → 0+I | X → X | X → X |
| `…:allow:cold-content:` | gate+h+a → gate+h+I | adv+a → 0+I | adv+a → 0+I | gate+a → gate+I | 0+a → 0+I |
| `…:allow:harvest-integrity:` | gate+a → gate+h+I | adv+a → 0+I | adv+a → 0+I | X → X | X → X |
| `…:allow:size-advisory:` (retired) | gate+a → gate+h+I | 0+a → 0+I | 0+a → 0+I | gate+a → gate+I | 0+a → 0+I |
| unrecognised scope (`…:allow:living-doc:`, a typo of `harvest-integrity`) | gate+h+a → gate+h+I | 0+a → 0+I | 0+a → 0+I | **X → X, unnamed (SZ1)** | X → X |
| marker with no reason (`sizescan:allow`, `sizescan:allow:`) | gate → gate | adv → 0 | adv → 0 | gate → gate | 0 → 0 |
| body-only mention (line 16 or later) | gate → gate | adv → 0 | adv → 0 | gate → gate | 0 → 0 |
| `sizescan:budget=N` (`=`, `: ` and space forms) | gate(ref=N) → gate+h+I | 0 → 0+I | 0 → 0+I | gate → gate+I | 0 → 0+I |
| `sizescan:budget=` (no digits) | gate → gate (not a marker) | — | — | — | — |
| `.sizescanignore` glob matching the file | gate+h+k → gate+h+I | 0+k → 0+I | 0+k → 0+I | K → K | K → K |
| glob **and** a budget or scoped marker on the same store | n/a | n/a | n/a | K, markers unseen → K, markers unseen (SZ4) | same |
| unscoped allow **and** budget on one file | gate+h+a → gate+2h+2I | 0+a → 0+2I | 0+a → 0+2I | X → X (+I for the budget) | — |
| glob with no reason anywhere in `.sizescanignore` | exit 2 → exit 2, every class (`IgnoreFileError`) | | | | |

| Location / file class | What is read, old → new | Gate behaviour |
|---|---|---|
| `ROADMAP.md` at root, under `docs/`, under `sub/docs/` | whole → whole | gates on `[x]` (both) |
| a ROADMAP.md under an archive directory (a growth-store dir) | – → – | never gated (both) |
| the four other hot-path names: SESSIONS.md and ARCHITECTURE.md under docs/, README.md and CLAUDE.md at the root | whole (for length) → first 15 lines | never gated; stale hatches now named |
| a README.md or CLAUDE.md anywhere but the root (one under docs/, the nested one under tools/) | – → – | a hatch there is never named |
| a hot-path basename inside a store directory (a README.md under reviews/, a SESSIONS.md under sessions/) | – → – | a hatch there is never named |
| `*-DONE.md` / `*-ARCHIVE.md` anywhere, incl. `docs/sessions/` and `other/` | whole → whole | gates on `[ ]`/`[~]`/`⏳` (both) |
| `node_modules/<pkg>/ROADMAP-DONE.md` | – → – | never scanned (HA1, both) |
| `SESSIONS.md` carrying `[x]` items | counted as nothing (both) | `cold_item_count` is roadmap-only |

Boundary checks: a marker on line 15 is a hatch, on line 16 a mention, at both SHAs; the
`suppressed:` line gains one field ("N inert hatch(es) (exempt nothing)") and nothing in
`tools/floor.py`, `tools/floorfleet.py` or `instruments/` parses sizescan's `--json` or its
tally (grep), so the shape change has no consumer beyond `test_report.py`, which pins it.

### Findings

**SZ1 — MODERATE — An unrecognised scope on an archive store is a live, silent hatch; the
delta documents it as inert.** `tools/sizescan.py` lines 125–145 ("only two hatches can
still exempt anything… Everything else is present and inert, and is named") and
`tools/README.md` lines 734–751 ("Two hatches still do something… Every other hatch is
present and inert, and the report names it") are stronger than the code. A header marker
whose scope names none of `FINDING_KINDS` — a typo of `harvest-integrity`, any invented
word — exempts an archive store's integrity check (probe A06: live `[ ]` item, no finding,
exit 0 under `--check`), is counted only as "1 file(s) by sizescan:allow header",
indistinguishable from a deliberate unscoped marker, and is never named. `_inert_hatches`'
own docstring (lines 665–674, "or a scope naming no kind") and the test
`test_the_unscoped_form_and_an_unknown_scope_exempt_only_the_archive_store` know this; the
two reader-facing documents and the CHANGELOG entry do not. The behaviour is pre-existing
(`72a68cc^` identical) and comes from `allowmarker.covers`' additive rule, which its own
docstring marks "not endorsed… kept until `115/230` is ruled"; the delta leans on that very
rule to justify retaining `size-advisory`, so it knew the mechanism. Lens 4: on the
integrity gate, a child's misspelt scope parks live work in an archive with no trace in the
report, which is the "hatch read as if it did something" class the delta exists to end,
inverted.
*Counsel (the reviewer's, for the principal; applies nothing):* (a) say it in the docstring
and README — "an unscoped marker, a `harvest-integrity` scope, **or any scope the tool does
not recognise**, exempts the store"; (b) with no behaviour change, print a note under the
store ("unrecognised scope `X` — read as unscoped; exempting") and tally it separately on
the `suppressed:` line, so the shape is visible per rule (b); (c) leave the behavioural fix
(unknown scope → inert) to `115/230`, which already says it needs an estate count first.
Recommend (a)+(b) now.

**SZ2 — MODERATE — `RECORD.md` names "review" as the detector that replaces the advisory,
and no such detector exists; the same paragraph still says the discipline "carries a
signal" for bloat.** Lines 62–66: "a regression back to a flat log is caught at review, not
by a number"; lines 269–271: resolved narrative "stays caught at review". No review reads
the session index or an all-open roadmap for shape (A4 above: rule 2 bars cold passes from
`SESSIONS.md`; `indexscan` checks mapping and dates, not entry shape; the next session's
start tails the index with no rule to act). Lines 261–263, unedited by the delta and now
false for length: "nothing fires when a file bloats again. So it carries a **signal** —
`tools/sizescan.py`" — after this delta nothing fires on bloat, by ruling. For a repo on the
split board (atelier itself) the cold-content gate is structurally silent too (a done item
flips in its own file, lines 230–236), so for this repo the advisory was the last signal on
the hot path and the doctrine now claims one where there is none. The tool docs are honest
about the loss; the doctrine is not — and the doctrine is what children read. The ruling
(remove the advisory) is a non-goal and stands; the *wording* that replaced it is the
author's, and it is the author's wording this finding is on.
*Counsel:* options for the principal — (i) write it as it is: "not detected by any tool or
scheduled review; relies on the writing session's discipline and the next session
noticing" (the stub-honestly rule, one sentence, lines 62–66 and 269–271; and reword
261–263 so "signal" is claimed for `[x]` items and live markers only); (ii) a **shape**
check, not a size check, consistent with the ruling — `SESSIONS.md`'s own contract is one
dated line per session, so an entry that is not a single dated line is a flat-log
regression a machine can name without any number; (iii) add "the index stayed one line per
session" to the session-close tidy-up list in `RECORD.md`. Recommend (i) now, (ii) as a
board item for the principal's decision; they are compatible.

**SZ3 — minor — `RECORD.md` line 57 still says an index "outgrows its budget" and
rotates; there is no budget, and no rotation trigger is now named anywhere.** The delta
edited lines 62–66 of the same bullet and left this sentence. The 2026-07-14 grounding note
("the budget colliding") is history and fine; "outgrows its budget" is present-tense
doctrine pointing at a removed mechanism. (Mirror sweep, V3/V5.)

**SZ4 — minor — A stale `sizescan:budget` or scoped marker on an archive store that a
`.sizescanignore` glob skips is never named (probe A11).** The glob skips the store before
its header is read, so "Everything else is present and inert, and is named, never silently
accepted" (docstring line 135) overclaims by one class; `_inert_hatches`' docstring half
says so ("skips the store before it is read"). Fix is one header read for a glob-skipped
store, or a qualified claim.

**SZ5 — minor — The report's "Inert hatches" explanation gives the wrong reason for some of
them.** `_inert_block` (lines 785–788): "each exempts nothing, because sizescan no longer
has a size advisory for it to quiet". A `cold-content` scope on an archive store (A03), or
a `harvest-integrity`/`cold-content` scope on a non-roadmap hot file (H05, H07), never
quieted the advisory — at `72a68cc^` the advisory still fired beside them (`over=151`).
They exempt nothing because they never did. Wording.

**SZ6 — note — Brief framing, tested (rule 1).** The merge `da85210`'s own changes beyond
`72a68cc` are not "board and record files only": it carries the `CHANGELOG.md` `Removed`
entry (+13 lines). The entry is owed under `RECORD.md`'s lockstep rule and is present at the
landing on the shared branch; its content is accurate except as SZ1 notes ("a stale scoped
marker is not read as the unscoped one" is true of `size-advisory` only). Its estate-wide
claim — 29 repos, exit codes unchanged, 28 advisory lines gone, 2 inert hatches named — is
**not re-driven here (relayed)**; the exit-code half is supported by the table and by
construction.

**SZ7 — note — Board item `110/100` line 124 still lists `sizescan:budget` among three live
exemptions that "need no reason and are not counted".** A dated audit observation inside an
open item; a reader acting on the item would look for a hatch that no longer exists.

**SZ8 — note — Two tally habits worth knowing, both pre-existing and unchanged.** An
exempting marker on a *clean* archive store counts as "1 file(s) by sizescan:allow header"
though it suppressed nothing (A12); and the inert count sits on the `suppressed:` line
while the docstring says it "is not a suppression". GUARDS rule (b) counts mechanisms, so
both are defensible; the second is a category mix the delta acknowledges.

**SZ9 — note — `tools/pins.py` line 79 was widened to 90 columns** (the file already carries
nine other lines over 85; `wrapscan` scans Markdown only, so no floor effect). The "about
200 lines" figure is now the live ground of `MAX_CLAUDE_MD_BYTES` with its only home in that
comment, honestly labelled; `blockscan.py`'s "a few hundred lines" likewise. Acceptable.

**SZ10 — note — Inert hatches have no expiry and no escalation.** The report says "remove
them"; nothing makes anyone. GUARDS says deferment expires; this is closer to acceptance,
and report-only is the house pattern for a non-defect, so the choice is defensible. Recorded
so the trade-off is visible, not as a defect.

**SZ11 — note — atelier's own `.sizescanignore` glob (`.claude/worktrees/**`) exempts
nothing a walk can reach, and its comment states a purpose already retired.** `filewalk`
prunes a linked worktree at its `.git` file, so the glob never fires (the tree reports
`0 file(s) by .sizescanignore · 0 inert`); and since `f9ccba8` a glob does not stop a
hot-path file gating, so the comment's "lets another session's mid-flight tree gate this
one's commit" is no longer what the glob prevents for `ROADMAP.md` (table R12/R14, old).
Belongs to `160/790`'s scope more than this delta's; recorded here because this delta is
the one that would now name such a glob inert if it ever matched.

### Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 2 MODERATE · 3 minor · 6 note.** The ruling is implemented
faithfully and the gates' behaviour is unchanged on every row driven; the two MODERATEs are
claims stronger than their evidence — the hatch docs say an unrecognised scope is inert when
it exempts, and `RECORD.md` says review catches what nothing now detects.

### Re-run ledger

| Claim or check | How | Result |
|---|---|---|
| `test_sizescan.py` | `python3 -m unittest discover -s tools -p test_sizescan.py` | 90 tests OK (10.7 s) |
| `test_report.py` / `test_allowmarker.py` / `test_pins.py` / `test_blockscan.py` | same, each file alone, sequentially | 70 / 30 / 19 / 26 OK |
| `sizescan --selftest` | `python3 tools/sizescan.py --selftest` | `selftest OK`, rc 0 |
| repo at HEAD | `python3 tools/sizescan.py --check --root . .` | clean, rc 0; `0 inert hatch(es)`; `.sizescanignore` present, matches nothing |
| full Python suite, once, foreground | `python3 -m unittest discover -s tools -p 'test_*.py'` | 1916 tests OK (176.9 s) |
| floor, CI plane | `python3 tools/floor.py --plane ci --root .` | rc 0; sizescan ✅; pathscan warn-only finding on an unrelated ADR; secretscan 23 advisory, unrelated |
| floor, hook plane | `python3 tools/floor.py --plane hook --root .` | rc 1, BLOCKED by leakscan — no user-local term list in this container (`115/350`), expected; sizescan ✅ |
| hatch table | `/home/user/scratch/SZ/hatchtable.py`, 75 rows × {bare, `--check`, `--json`} × {`72a68cc^`, `72a68cc`, HEAD} | 0 exit-code changes old → new; 0 differences new vs HEAD |
| new tests fail on `72a68cc^` for the reason named | HEAD's `test_sizescan.py` against the `2e2da81` module in scratch | 26 of 90 fail: 15 for the named reason, 11 by `TypeError`/`KeyError` on the new parameter/key |
| "exit codes unchanged across 29 repos" (CHANGELOG) | — | **not re-driven here (relayed)**: no sibling repo in this container; supported by construction and by the table |
| "2 inert hatches named" across the estate (CHANGELOG) | — | **not re-driven here (relayed)**; this repo has 0 |
| `/security-review` | — | discharged by grounds (landed delta; pending diff is other reviewers' briefs) |
| mirror sweep | `coldsweep.py` with the brief's exclusions, 7 patterns | hits listed under lens 3; no barred file searched |

### Follow-up checklist (for the principal; nothing applied)

- [ ] SZ1 — name the unrecognised-scope form as live in docstring and README; consider the
      report note and separate tally; route the behavioural fix through `115/230`.
- [ ] SZ2 — reword `RECORD.md` 62–66, 261–263, 269–271 to state honestly what detects a
      flat-log regression and prose-shaped cold content (nothing, today); decide whether a
      shape check on the index's one-line contract is wanted.
- [ ] SZ3 — `RECORD.md` line 57: drop "outgrows its budget" or name the rotation trigger.
- [ ] SZ4 — read a glob-skipped store's header, or qualify the "never silently accepted" claim.
- [ ] SZ5 — reword `_inert_block`'s reason.
- [ ] SZ7 — annotate `110/100` line 124.
- [ ] SZ11 — refresh the `.sizescanignore` comment (or drop the dead glob) under `160/790`.
- [ ] Relayed, for a session with the estate: confirm the two inert hatches the CHANGELOG
      counts are named on their repos' next floor run.
