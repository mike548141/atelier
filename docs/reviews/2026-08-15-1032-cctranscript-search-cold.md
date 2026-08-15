# Cold pass — the `cctranscript --search` build

**Pass type:** code cold pass (rule-4 queued — the build applies a reviewed
design, and the builder's judgement produced both the code and the places it
departed from the design).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04).
**Status:** BRIEF WRITTEN, REVIEW NOT RUN. The next cold session that passes
rule 4's criterion and the tier bar takes it — see *Spawn provenance*.

## Spawn provenance

- **Author of the work under review:** the session that landed the delta on
  2026-08-09 (see *What the work is*).
- **Who wrote this brief:** a cold session Mike opened on 2026-08-15 with
  the standing instruction, verbatim: *"As a cold session please do any review
  work, any work that is fable dependent, and write briefs for any reviews
  that need them. If you write the brief then do not run the review, that
  will require another cold review session."* That session authored no part
  of this delta, was neither started nor instructed by the authoring session,
  wrote this brief from the delta and the queue pointer only, and **stopped**
  — it did not run the review.
- **Who takes the review:** the next cold session that meets rule 4's single
  criterion — a session the author neither started nor instructed — on the
  Fable tier, checked at selection. The taker repeats its own provenance in
  the verdict: how it was spawned, and its non-involvement with both the
  authoring session and the brief-writing session.
- **Orchestration shape:** the deferred material sits in the sibling file
  `2026-08-15-1032-cctranscript-search-cold.deferred.md` (rule 1's split): the
  intent-record references, the prior-verdict references, and the
  brief-writer's seeded questions. Recommended: the taker runs the review
  under an orchestrator that holds the sibling's bytes and hands them to the
  reviewer only after its findings are durably written. A taker reviewing by
  hand opens the sibling as a deliberate second act after its findings are
  written, and says so in the verdict. Fold in and delete when the verdict
  lands.

## What the work is

Landed 2026-08-09 on `main` as `0eb03ed`. Reviewed at HEAD:

1. [`instruments/cctranscript`](../../instruments/cctranscript) — the
   `--search <term>` / `--regex` mode and its flags (`--since`/`--until`,
   `--top`, `--materialise`, `--from-archive`, and any others the file
   declares).
2. [`instruments/cctranscript.test.js`](../../instruments/cctranscript.test.js)
   — the suite grew 38 → 62 tests in the landing commit.
3. [`instruments/man/cctranscript.1`](../../instruments/man/cctranscript.1) —
   the manual page's `--search` sections.
4. [`instruments/README.md`](../../instruments/README.md) — the catalogue row,
   the `--materialise` / flag-vocabulary note, and the shared-flags table rows.
5. [`instruments/cctranscript.search.design.md`](../../instruments/cctranscript.search.design.md)
   — the design of record, with a status banner listing where the build
   departed from it. **This document is in-delta and reviewable as such** —
   it is the builder's account of its own departures, not settled ground.
6. The `CHANGELOG.md` entry that landed with them.

The tool reads Claude Code session transcripts on the local machine (live
logs, or the archive mirror). It is an instrument, not doctrine, but it is
shipped in a PUBLIC repo and reads a private corpus.

## Scope

Widest the work admits: the design the build claims to apply and every
departure it declares, the code, the tests, the manual page and README as the
contract users read, and real behaviour exercised live against a transcript
store. **Non-goals:** none narrows the delta. The reviewer does not decide
findings' dispositions; residue joins the principal's ruling round per house
practice.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. Read the design of record cold and decide, before reading the
   banner, what a faithful build would look like — then compare. Is each
   declared departure a departure the design should have made, and are there
   undeclared ones?
2. **Correctness & quality** — run the suite; run the tool live against a
   store (a scratch store you construct is acceptable, and safer for
   disclosure — see lens 4); probe the term gate (escaping, non-ASCII, regex
   mode), the date bounds, `--top`'s truncation accounting, and what happens
   on an evicted or unreadable file. Do the tests pin the properties the
   design's DONE conditions name, or weaker proxies of them?
3. **Completeness / harvest** — the design's DONE conditions versus what the
   banner concedes; the flag vocabulary versus the sibling instruments (does
   `--search` reuse their conventions or coin new ones); the manual page and
   README versus the actual flags at HEAD.
4. **Security & privacy** — mandatory, at code altitude, and this instrument
   has a real surface: it searches a private transcript corpus and prints
   excerpts. What does an excerpt carry, where does it go, and could its
   output be pasted into a public record by a session following the house's
   own evidence rules? Regex input handling (catastrophic patterns, injection
   into anything shell-adjacent). Path handling under `--from-archive`.
   atelier is PUBLIC — verify nothing in the delta, and nothing you put in
   your verdict, carries transcript content or private-repo detail. The
   house security scanner reads pending diffs; this is a landed-delta
   review, so state the reach case that applied.

## Re-run obligation

Re-run, do not read: the instrument suite (house invocation lives in
[`.githooks/pre-commit`](../../.githooks/pre-commit) — lift it, do not guess);
the 38 → 62 test-count claim at the landing commit; the manual page through
the house renderer and linter (they differ — the repo's records name both);
and every timing or ratio claim the design banner or the CHANGELOG entry
makes, where a store to measure against exists — and where it does not, state
that plainly rather than reading the numbers as verified.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`,
every prior verdict in `docs/reviews/`, and the intent record for this delta.
The sibling `.deferred.md` holds those references and the brief-writer's seeded
questions; open it after your findings are committed. Reconcile after, never
anchor before. A taker whose own session onramp has already read the
`SESSIONS.md` tail discloses that in the verdict.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `CS`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then open the sibling; append a
reconcile section; fold the sibling in below it and delete the sibling;
finalise. Update the queue pointer
(`docs/roadmap/160-doctrine-review-owed/010-rule-4-review-queued-tier-fable-pass-type-code.md`)
and rebuild the index in the same commit.

---

# Verdict — cold pass on the `cctranscript --search` build

**Provenance, repeated.** Reviewer: a cold rule-4 reviewer on the Fable tier,
spawned by this pass's orchestrator — a Fable session Mike opened on 2026-08-15
at about 1120 UTC under his standing cold-session instruction (do any review
work, any Fable-dependent work, write briefs for reviews that need them; a
brief-writer never runs its own brief) and pointed at the review queue. The
orchestrator authored no part of this delta and was neither started nor
instructed by the authoring session or by the brief-writing session (a separate
cold session earlier on 2026-08-15); the reviewer likewise. The `.deferred.md`
sibling was withheld under the orchestrator's context partition — moved out of
the worktree before this reviewer was spawned — so nothing below this line was
written with it, the intent record, or any prior verdict in hand. Orchestrator's
disclosure: its own session onramp read the tail of `docs/SESSIONS.md`, whose
index entries summarise these deltas; the reviewer did not, and received only
the brief and this preamble.

What this reviewer read and did not read: the brief; the delta at `0eb03ed`
(all six surfaces plus the commit message, taken as the author's claims); the
sibling instruments `ccrepo` and `ccarchive` for flag vocabulary; the design
body (§1–§14, lines 58–415) **before** the status banner (lines 1–57), in that
order — the file's layout allows it and the reviewer formed its own picture of a
faithful build first. It read the queue pointer file and did not edit it. Of the
board it read only file names under `docs/roadmap/210-instruments-open-features/`
(to check that items the commit message says were queued exist); it did **not**
open the "§ instruments/ — open features" item's body, which the pointer names
as an intent record — that is reconcile-stage reading. No `SESSIONS.md`,
`sessions/`, `ROADMAP-DONE.md`, prior verdict or `.deferred.md` was opened; no
tree-wide grep was run over records. Two exposure disclosures are in Lens 4.

**The delta reviewed.** Landing commit `0eb03ed` (2026-08-09) on top of
`81a6604`; the six surfaces named by the pointer. Worktree HEAD `3d0df11`.
`git diff 0eb03ed HEAD -- instruments/{cctranscript,cctranscript.test.js,
man/cctranscript.1,README.md,cctranscript.search.design.md}` is empty — the
delta's instrument surfaces are byte-identical at HEAD. `CHANGELOG.md` gained
unrelated entries under three later commits (`ab74014`, `15d3de2`, `71b3e8f`);
those are out of scope. The design commit `d96f2b8` (2026-07-27) is the design
of record and was read as such, not reviewed.

## Load-bearing assumptions, named first

1. **Search is I/O-bound; a whole-file regex gate on the raw JSON is the cost
   control** (design §2, §10; code comment at `cctranscript:746-762`).
2. **The raw-JSON gate is a safe prefilter for the decoded-text probe** — a
   file that fails the gate cannot hold a hit the decoded text would show
   (banner bullet 2; `rawForms`, `buildMatchers` at `cctranscript:776-799`).
3. **`N.M` refs must be gate-invariant, so a gated file is parsed whole**
   (banner bullet 1; `runSearch` at `cctranscript:903-912`).
4. **A log's mtime is never earlier than its last message**, so an mtime day
   before `--since` is a safe skip (design §9; `cctranscript:889-891`).
5. **`--search` is a mode of the existing `--list` sweep**, sharing
   `pickSessions()` and the scoping vocabulary, parsed by the same
   `takeValue` convention as every other value flag (design §1, §3).
6. **The tool's output goes to a human at a terminal**, so what an excerpt
   carries needs no threat step (implicit — the design has none).
7. **The evicted-mirror behaviour is settled by flags-follow-operation** and
   reuses `isDataless()` (design §8).

Under attack: 1 held (a miss runs at the floor: 2.2–2.3 s against a 1.5–2.3 s
bare read of 582 files / 796 MB — counts only, see Lens 2). 2 held for literal
terms with one gap (astral characters, CS6) and **failed for `--regex`**: gate
and probe run against different texts, so a class of patterns can never match
and the man page's workaround does not rescue them (CS1). 3 held; the tests pin
it. 4 held on the fixture invariant and by construction of a live log; not
provable for copied logs, and stated as an assumption. 5 held in shape and
**failed at one edge**: `--search` with no following token falls through to the
render mode (CS2). 6 is the assumption the design never named — the primary
callers of these instruments are agent sessions, whose evidence rules push
command + output into records (CS3). 7 held; the simulated-eviction seam
exercises it both ways.

## Lens 1 — approach & assumptions

**Right problem, right shape.** One flag plus a mode over the existing pool is
the smallest build that answers "which session said X"; a subcommand or a
second code path would have duplicated `pickSessions()`. `readTurns(file, opts)`
defaulting to the render's behaviour is the right seam — one extraction path,
callers unchanged (verified: 38 pre-existing tests still pass at HEAD).

**A faithful build, read cold from the design body:** `--search`, `--regex`,
`--case`, `--materialise`, `--since/--until`; whole-file gate; parse only
survivors; gate-invariant refs; one row per turn with a hit count; bounded
single-line excerpt; unsearched-layer count on every run; `--think` documented
as void; evicted skip + count + `--materialise`; `--json` meta; ≤1.5× floor;
README note; man page NOTES. Against that picture the banner's six departures
are the right departures, and the first is the important one — the reviewer
reached the same contradiction (refs need every preceding turn; §10 step 4
parses only survivors) before reading the banner. Choosing correctness and
replacing a wall-clock guard with `sessionsParsed` is the honest resolution.

**Undeclared departures found:** (a) the `--regex` gate is a false-negative
class the banner names for literal terms and says is "documented" for regex —
the documentation is wrong in a way that makes the class silent (CS1); (b) the
design's `--since/--until` "exact ccrepo meaning" does not survive `--utc`
(CS5); (c) the design's DONE list stays entirely `[ ]` under a "BUILT" banner
(CS4); (d) `--search` with no term is a fall-through, not an error (CS2).

**Brief framing attacked.** The brief calls this a "code cold pass" and says no
non-goal narrows the delta — both hold. It says the design's banner is "the
builder's account of its own departures, not settled ground" — correct, and
the banner is largely honest; the reviewer's disagreements are with what it
left out, not with what it says.

## Lens 2 — correctness & quality (everything re-run, nothing read)

Every claim below was re-run; the command and observed result are given.
Where the store is the live one, only counts and times are reported.

- **Suite at HEAD:** `node --test instruments/cctranscript.test.js` → tests 62,
  pass 62, fail 0 (10.6 s). Sibling suites `ccrepo.test.js` + `ccarchive.test.js`
  → 173 pass. `python3 -m unittest discover -s tools -p 'test_*.py'` → Ran 1321,
  OK. `python3 tools/floor.py --selftest` → ok (15 scanners).
- **38 → 62 claim:** scratch clone at `0eb03ed` → tests 62 / pass 62; at its
  parent `81a6604` → tests 38 / pass 38. **Holds.**
- **Manual page:** `mandoc -T lint instruments/man/cctranscript.1` → exit 0
  (mandoc present at `/usr/bin/mandoc`); `man -P cat …` → exit 0, 427 lines,
  renders every `--search` section. `--help` → 24 lines. **Holds.**
- **Floor at HEAD (read-only, worktree):** hook plane exit 0; CI plane exit 0;
  the usual 👁️ warn-only lines and 🟡 advisories, none new.
- **Live probes on a synthetic store** (seven fixture logs under a throwaway
  HOME, one hand-written with JSON-escaped `ā` and a surrogate-pair
  emoji, one 8 MB tool result, one `chmod 000`): literal terms containing `"`,
  `\` and a newline all hit (`P2a–d`); `Māori` finds both the raw and the
  escaped spelling and `māori`/`--case` behave (`P3a–c`); one row per turn
  with `(N hits)`; a 4 MB tool result excerpts to one bounded line under
  `--tools` (`P9`) and counts as tool-only without it (`P9b`); `--top 1` hides
  and reports; a reply before any prompt cites `0.1`; `--list --search` is
  silent; a positional path narrows to one file; `-n` is inert; bad `--since`,
  `--top -5`, `--search ''` and an invalid pattern all exit 2 with the reason.
- **Where probes failed the claims:** `--regex` across `"`, `\`, newline and
  anchors (`P4a–e`, `P5a–c`: all zero hits, in both spellings — CS1);
  `--search` as the last token renders a transcript, exit 0 (`P1` — CS2);
  `--utc` moves the `--since` day boundary (CS5); the escaped emoji fixture is
  missed while the raw one hits (`P7a` — CS6); the tool-only tally ignores
  the date window (`P25` — CS7).
- **Timing / ratio claims (live store, counts and seconds only, three bare
  reads then paired runs):** bare read of every live log 582 files / 796 MB →
  2.32, 1.49, 1.48 s. Miss (`--all`, nonsense term) → `elapsedMs` 2.26 / 2.18 s,
  swept 582, parsed 0 — **at the floor, holds.** Broad term (in 580 of 582
  sessions) → 9.90 / 10.27 s, parsed 582 — the banner's 9.6 s / "3.7×" holds in
  seconds; the ratio is 4.4–6.8× against this bare read. Selective term
  (parsed 72 of 582, 13 matched) → 4.44 / 4.21 s = 1.9–2.0× the tool's own
  miss run and 1.8–3.0× the bare read — the banner's **"1.22–1.32× … condition
  13 met" did not reproduce** (CS4). Macron term → 5.34 s, parsed 168.
- **Tests vs DONE conditions:** the suite pins the properties, not proxies —
  literal/regex disagreement, case, macron round trip, ref resolution on
  reopen with default flags, one-row-three-hits, 800 KB excerpt, tool-only
  tally both ways, `--think` inert, since/until on turn timestamps plus the
  mtime skip counted, `--json` field set with zeros, gate = parsed count,
  `--top` accounting, ordering, exit codes, evicted/materialise through the
  simulate seam, gzip parity. Gaps: no test for `--regex` with `"`/`\`/anchor
  (CS1), for trailing `--search` (CS2), for `--utc` × `--since` (CS5), for the
  escaped-astral form (CS6), for the tally under a date window (CS7), or for
  the `unreadable` counter (it works — `P6d`: "6 of 7 swept … 1 log(s) could not
  be read"). Fixtures are synthetic and written in the test — good hygiene.

## Lens 3 — completeness / harvest

- **DONE conditions vs banner:** 14 of 15 met as built; 13 partially and
  honestly conceded (though the selective-term ratio overstates it, CS4).
  The checklist itself is untouched under a "BUILT" banner (CS4).
- **Flag vocabulary vs siblings:** `--since/--until/--top/--materialise/
  --from-archive/--dest/--json/--repo` reuse `ccrepo`/`ccarchive` words and
  meanings (checked against `ccrepo:1138-1200,1246,1567-1572`); the exceptions
  are cctranscript's stricter date validation (dashes tolerated, exit 2 on
  junk — `ccrepo` compares strings unvalidated) and the `--utc` interaction
  (CS5). `--search`, `--regex`, `--case` are new words for operations no
  sibling has; the design's naming argument for `--search` over `--matching`
  holds. README table rows and the rewritten `--materialise` note match the
  code at HEAD.
- **Man page vs flags at HEAD:** every `--help` flag is in the page (the drift
  guard test); the page's `--search` OPTIONS, EXAMPLES, EXIT STATUS and NOTES
  are present. Defects: the NOTES `--regex` advice (CS1) and the EXIT STATUS
  "2 … `--search` with no term" claim (CS2); `--tools` "each summarised to a
  single line" is the render's truth, contradicted for search two paragraphs
  up — minor wording.
- **What the commit says was queued:** files exist under
  `docs/roadmap/210-instruments-open-features/` whose names match the
  archive-mode pool cost (`050-…`), `--think` doing nothing (`080-…`) and
  subagent logs out of scope (`090-…`) — the design §12 items reached the
  board. File names only were read.
- **Harvest beyond the delta:** `--list` (and `--list --all`) crashes with a
  raw `EACCES` stack on an unreadable log where `--search` counts it (CS11,
  pre-existing since 2026-07-23, `firstUserPromptText`); an unreadable or
  cwd-less log silently drops out of `--repo <name>` scope because its label
  falls back to the folder-name tail and only *evicted* records get the
  encoded-suffix fallback (`cctranscript:727-728`).
- **The record:** the "6 escaped vs 6,698 raw" figure lost its escape in three
  records and reads as the same character twice (CS9).

## Lens 4 — security & privacy

**Design altitude.** The design enumerates cost, eviction and correctness
threats and none for exposure: what an excerpt carries (private prompt/reply
text, tool inputs and results in full under `--tools`), what `--json` carries
(session ids, `cwd` — absolute paths of the operator's repos), and where the
output goes. The tool's stated readers are humans, but the instruments layer
exists for Claude-teammate use, and this house's own review doctrine requires
"the command and the observed result" in verdicts — the paste channel is built
in. Nothing in `--help`, the man page or the README says the output is
transcript content that must not be reproduced in shared records; this brief
had to say it to the reviewer. Absent enumeration is the finding (CS3).

**Code altitude** (OWASP-shaped, checked not recalled): no shell — the one
subprocess is `execFileSync('stat', [...])` with an argument array
(`cctranscript:172`); no network; no `eval`/deserialisation beyond `JSON.parse`
in try/catch; paths come from CLI flags and `CCARCHIVE_DEST` (trusted by the
house scanner's own precedent) and are read-only; the tool writes nothing.
User regex is compiled as given — a catastrophic pattern hangs the operator's
own process (CS12, note; not a vulnerability by the house scanner's rules).
`--json` prints `cwd` per session by design of the existing `--list`.

**Delta and verdict hygiene:** the delta carries no transcript content — the
commit message, banner and CHANGELOG report counts and times; the man page's
example rows are invented. This verdict reports shapes, counts and seconds
only; the synthetic store's text is the reviewer's own.

**House scanner reach case.** Landed-delta review; the reviewer re-applied the
delta as a pending diff in a scratch clone (`81a6604` + the six files from
`0eb03ed`) to aim `/security-review` at it. The skill ignored the path argument
and read the **shared worktree's** dirty state instead — the pending-diff
scanner cannot be aimed at a clone from a session whose cwd is the worktree.
Its scan is therefore **discharged**: the manual pass above stands in for it,
and no HIGH/MEDIUM finding was surfaced from the code by either. **Exposure
disclosure #1:** that scan showed the reviewer another pass's brief and its
`.deferred.md` sibling (the reply-gate pass, prefix `RG`) and a pointer edit —
material for a different subject, none of it about `cctranscript`; this
reviewer's own sibling appeared only as a deleted path with no content, and
nothing above was formed from it. **Exposure disclosure #2:** the hook-plane
floor printed `docs/SESSIONS.md` as a size-advisory file name — a name only.

## Findings

**CS1 (MODERATE)** — `--regex` gate and probe run against different texts, so a
class of patterns can never hit, and the documented workaround does not work.
*What:* `buildMatchers` (`cctranscript:789-799`) uses the same user pattern as
the whole-file gate over raw JSON and as the probe over decoded turn text. A
pattern that involves a `"`, a `\`, a newline class (`\n`, `\s+` across a line
break) or an anchor (`^`, `$`, which bind to the whole file in the gate) fails
one of the two whatever spelling it is written in. *Evidence:* synthetic-store
probes `P4a` `alpha\s+beta` → parsed 0, hits 0; `P4b` `alpha\\nbeta` (the NOTES
advice) → parsed 1, hits 0; `P4d` `"alpha"` → parsed 0; `P4e` escaped-quote
form → parsed 1, hits 0; `P5a` `^second` and `P5c` `lines$` → parsed 0. The
literal search for the same strings hits (`P2a–d`). Man page NOTES
(`cctranscript.1:583-590`) tells the user to "write against the escaped form"
— that yields gate-pass, probe-miss. *Why it matters:* the failure is silent —
"0 hits" reads as absence, the exact quiet wrongness design §5 names — and
quotes are common in what people grep for. *Counsel (reviewer decides
nothing):* for `--regex`, bypass the gate when the pattern contains any of
`" \ ^ $` or a whitespace/newline class and parse those files whole (the cost
shows in `sessionsParsed`, which is honest); or run the probe over each raw
line JSON-decoded; and correct NOTES to say what does and does not match. Add
a test with a quoted regex and an anchored one.

**CS2 (MODERATE)** — `--search` with no following token silently renders a
transcript instead of exiting 2. *What:* `takeValue('--search')` returns
`undefined` when the flag is last (`cctranscript:87-90,114-115`), so `doSearch`
is false and the CLI falls into the render path. *Evidence:* `P1` → the latest
session's transcript, exit 0; `P18` (`--search ''`) → exit 2 as tested. Man
page EXIT STATUS (`cctranscript.1:526`) promises 2 for "`--search` with no
term"; the test at `cctranscript.test.js:751-767` covers only the empty
string. *Why it matters:* an agent that drops the term prints a whole private
transcript into its context, and the exit code says success. *Counsel:* set
`doSearch = argv.includes('--search')` and let `runSearch`'s own guard fire;
add the trailing case to the exit-2 test.

**CS3 (MODERATE)** — no threat step for a tool that prints a private corpus,
and no caution on any user-facing surface. *What:* design §14 covers review
posture only; the man page, `--help` and README say nothing about the output
being transcript content or about where it may be reproduced. *Evidence:*
grep of `instruments/README.md` and the man page for a caution → none; the
`--json` shape prints session id, `cwd`, timestamps and excerpts. *Why it
matters:* the primary callers are agent sessions whose evidence rules require
command + output in verdicts, and atelier is public — the paste path is a
design property, not a user error. *Counsel:* one NOTES paragraph plus a
README sentence: output is transcript content — report shapes and counts in
shared records, never excerpts, ids or paths; consider a `meta.privacy` line
in `--json`. A doc-drift test could pin the NOTES line.

**CS4 (minor)** — the selective-term ratio did not reproduce, and the design's
DONE checklist is untouched under a "BUILT" banner. *Evidence:* live-store
re-run (counts only): miss 2.2 s, selective (72 of 582 parsed) 4.2–4.4 s =
1.9–2.0× the tool's own floor; broad 9.9–10.3 s. The banner's "1.22–1.32×"
depends on a bare-read floor stated as a 2× range (2.5–4.9 s). All 15 DONE
boxes at `cctranscript.search.design.md:351-377` remain `[ ]`. *Counsel:*
state condition 13 as not met at wall-clock and met structurally; tick or
annotate the DONE list so the design of record reads true without the banner.

**CS5 (minor)** — `--utc` silently changes the day boundary of
`--since/--until`. *What:* `dayNum` → `dateOf` (`cctranscript:340-345,856`)
folds to a UTC day under `--utc`; `ccrepo` is always local
(`ccrepo:206-217`). *Evidence:* a fixture turn at 23:30 UTC on 2026-01-02:
`--since 20260103` → 1 hit; the same with `--utc` → 0 hits (host zone NZST).
Man page (`cctranscript.1:342,349,379`) says "local date" unconditionally and
describes `--utc` as presentation only. *Counsel:* pin the bounds to local
regardless of `--utc` (ccrepo parity, the design's stated intent), or document
the interaction; one test either way.

**CS6 (minor)** — the literal gate's "every form the term can take" misses
astral characters escaped as surrogate pairs, and mixed raw/escaped spellings.
*What:* `rawForms` (`cctranscript:776-781`) emits `\u` + the full code point
(five hex digits for an emoji), a spelling JSON never writes; JSON writes two
`\uXXXX` units. *Evidence:* `P7a` — the raw-emoji fixture hits, the
hand-escaped `🚀` fixture does not (hits 1, matched 1 of the 2
sessions holding it). *Counsel:* build the escaped form per UTF-16 code unit,
or narrow the claim in the code comment and NOTES; add the fixture.

**CS7 (minor)** — the tool-only tally ignores the date window. *What:*
`toolLayerHolds` (`cctranscript:920-923`) is set before the `since`/`until`
test at `:925-926`. *Evidence:* `P25` — a tool call dated 2026-01-01 with
`--since 20260102 --utc` still prints "the term is in 1 session's tool calls
or results (add --tools)"; adding `--tools` in that window finds nothing.
*Counsel:* apply the same date filter to the tally; test it.

**CS8 (minor)** — the reported sweep time excludes pool construction, which the
commit message calls the dominant cost in archive mode. *What:* `t0` is taken
after `pickSessions()` (`cctranscript:869-870`), so "swept in X s" and
`meta.elapsedMs` omit the per-mirror `stat` and full-gunzip sniff, and the
sweep then gunzips each mirror again. *Evidence:* code path
`archiveSessions → sessionRecord → cwdFromLog` (`:200-206,234-241`) then
`readLogText` (`:893`). The pool item is queued (`210-…/050-…`, name only read).
*Counsel:* start the clock before the pool or print both figures.

**CS9 (note)** — record defect: the "6 escaped sequences against 6,698 raw"
figure appears in the design banner (`cctranscript.search.design.md:22`), the
CHANGELOG (`CHANGELOG.md:88` at HEAD) and the commit message with the escaped
spelling collapsed to the same character as the raw one, so the sentence reads
as X against X. The code comment (`cctranscript:774`) has it right.

**CS10 (note)** — a value flag takes whatever token follows it, flag or not:
`--search --json` searches for the literal `--json` under `--json` output
(`P20`), `--search --regex` searches for `--regex` in regex mode (`P19`), and
`--since --search x` exits 2 with the date error (`P27`). Same shape as the
sibling parsers; one NOTES line, or a "next token is a flag" guard in
`takeValue`, would close it.

**CS11 (note, outside the delta — harvest)** — `--list` crashes with a raw
`EACCES` stack on an unreadable log (`P6c`; `firstUserPromptText`,
`cctranscript:311`, pre-existing 2026-07-23) where `--search` counts it
(`P6d`); and an unreadable or cwd-less log falls out of `--repo <name>` scope
silently (`P6e`: 6 of 6 vs `P6d`: 6 of 7) because only evicted records get the
folder-suffix fallback (`cctranscript:727-728`). Counsel: route both through the
same fallback and catch the read in `--list`.

**CS12 (note)** — a zero-length pattern (`a*`) counts a hit per position (399
"hits" over 6 fixture sessions, `P16`) — harmless, the guard prevents a hang;
a catastrophic pattern has no guard and hangs the operator's own process.
Worth one NOTES sentence, nothing more.

## Overall

**PASS-WITH-FINDINGS — 0 MAJOR / 3 MODERATE / 5 minor / 4 note.** The build is
the design, honestly departed from where it had to be, with a hermetic suite
that pins the real properties. An author must fix the `--regex` gate/probe
mismatch and its wrong NOTES advice (CS1), the trailing-`--search`
fall-through (CS2), and add the output-privacy caution (CS3); the minors are
each a line or a test. Dispositions are the principal's per house practice;
none of the counsel above is a decision.

## Follow-up checklist

- [ ] CS1 — regex gate bypass or per-line decoded probe + corrected NOTES;
      tested against a quoted regex and an anchored regex hitting a fixture
      turn, and `sessionsParsed` reflecting the bypass.
- [ ] CS2 — `--search` as last token exits 2; tested by adding the trailing
      case to the exit-2 table.
- [ ] CS3 — NOTES + README caution that output is transcript content; tested
      by the man-page drift guard or a `assert.match(page, /shapes and counts/)`
      style pin.
- [ ] CS4 — banner and CHANGELOG restate condition 13 as structural-only; DONE
      list ticked/annotated; tested by reading the design at HEAD.
- [ ] CS5 — since/until pinned to local or documented; tested with a turn at
      23:30 UTC under both flag sets.
- [ ] CS6 — `rawForms` per code unit; tested with a surrogate-pair fixture.
- [ ] CS7 — tally date-filtered; tested with an out-of-window tool hit.
- [ ] CS8 — elapsed includes the pool or prints both; tested via `meta`.
- [ ] CS9 — restore the escaped spelling in banner + CHANGELOG; tested by
      eye.
- [ ] CS11 — `--list` catches unreadable logs; `--repo` fallback for
      cwd-less records; tested with a `chmod 000` fixture.
- [ ] CS12 — one NOTES sentence on pathological patterns.

## Reconcile — post-verdict, against the intent record and the deferred questions

Opened after phase 1 was committed (`1b93f34`), on the orchestrator's release,
and only the surfaces the sibling names: the board section
`docs/roadmap/210-instruments-open-features/README.md` (the *cctranscript
learns to search* narrative) and items `050-…`, `080-…`, `090-…`;
`docs/ROADMAP-DONE.md` § *cctranscript learns to search*; the queue pointer
`160-…/010-…`; and the two prior verdicts
`docs/reviews/2026-07-11-instruments-test-floor-code-review.md` and
`docs/reviews/2026-07-17-1000-adr0006-ccarchive-preserve-cold.md`. Nothing in
phase 1 above is revised; additions are marked as such.

### Applied as ruled?

There is no prior ruling on this delta to apply — this is the first pass. The
design (2026-07-27) closed its six questions on measurement and recorded "no
decision left open" for the principal; the build applied that design, and the
record (board narrative, `ROADMAP-DONE`) restates the six departures the banner
declares, word for word with the commit message. The record and the delta agree
with each other; the reviewer's disagreements (below) are with both.

### What the record resolves from the checklist

- **CS8** — the archive-plane pool cost is *known* to the record: item `050-…`
  states that "11.5 s of a 13.9 s archive search happens before a single hit
  is scored" and names both causes. CS8 therefore stands as a *reporting* gap
  (the tool's own summary hides a cost the record documents), not a discovery;
  severity unchanged (minor).
- **CS9** — narrows: `ROADMAP-DONE.md` § *cctranscript learns to search* carries
  the figure legibly ("6 escaped … against 6,698 raw ones"); the collapse is
  in the design banner, the CHANGELOG and the commit message only. Severity
  unchanged (note).
- **CS11** (harvest, outside the delta) — the 2026-07-11 verdict's item 9
  ("one `sessionRecord()` constructor … divergent label fallback") was ruled
  `[fixed]` and is the constructor now in place; the label fallback it
  unified is the one that drops an unreadable log out of `--repo` scope. Not
  a regression of that fix — a case it never covered.
- Nothing in the record resolves CS1–CS7, CS10 or CS12.

### Divergences between the record and this verdict

- `ROADMAP-DONE.md` (and the board narrative) state that a selective search
  "runs at 1.22–1.32× a bare read, **which meets the condition**". This
  reviewer's re-run (Lens 2) put a selective term at 1.9–2.0× the tool's own
  miss run; the "meets" claim rests on a floor the banner itself gives as a
  2× range. CS4 stands.
- `ROADMAP-DONE.md` says the `--regex` limitation "lives in NOTES rather than
  being papered over". NOTES tells the user to write such patterns "against
  the escaped form", which the reviewer showed yields gate-pass, probe-miss
  (CS1). The record believes the limitation is documented; it is documented
  wrongly.
- Board item `080-…` (`--think` does nothing) still carries the census figure
  the banner corrected (24,856 blocks; the banner and man page say 31,800).
  A stale number in a follow-up item — record hygiene, folded into CS9's
  class; no new ID.
- `ROADMAP-DONE.md`'s harvested checkbox line reads "DESIGN DONE 2026-07-27,
  BUILD not started" under a section headed "done 2026-08-09" — a verbatim
  harvest of the pre-build item text; the section prose is current. Note
  only.
- The two prior verdicts do not touch `--search`. The 2026-07-11 pass's
  item 3 (parsing at module load must not exit) is honoured by the delta:
  `normDate`, `--top` validation and `buildMatchers` all run inside
  `runSearch`, not at load. The 2026-07-17 pass's guard 1 (no personal data
  in code) holds for the delta — the archive default is derived from the home
  directory at run time and no operator path is committed; its guard 2
  (dest inside a repo refused) is a write-side guard with no read-side
  analogue owed here.

### Answers to the six seeded questions

1. **A seventh departure.** Yes, several, none of them a flag: the DONE list
   the banner does not mention is met except as declared, but the banner is
   silent on (a) the `--regex` class being *silently* unmatchable rather than
   documented (CS1), (b) `--utc` moving the `--since/--until` boundary
   (CS5), (c) the astral-escape gap in "every form the term can take" (CS6),
   and (d) the DONE checklist left `[ ]` under "BUILT" (CS4). Every flag in
   `--help` is named in the design or the banner (`--top` in the banner);
   the design named `--case`, which the build kept.
2. **Is a documented false negative acceptable in a recall tool?** No, and the
   pass found it is worse than the banner says: the class is real for `"`,
   `\`, newline classes *and anchors*, and the documented workaround does not
   work (CS1). Visibility: NOTES only — not at the `--regex` OPTIONS entry,
   not in the run's own summary. Counsel as in CS1: bypass the gate for that
   pattern class (cost visible in `sessionsParsed`) or decode per line;
   whichever, the OPTIONS entry and the summary line should say when a
   pattern falls in the class.
3. **Structural guard vs the property.** The test pins the *mechanism* (a
   swept file that misses is never parsed — 1 of 13) exactly; that is what
   guards against the "simplify into parse-everything" regression the design
   feared, and it is the right structural guard. It does not pin the *cost*
   outcome, and the cost outcome is what the record overstates: the 3.7× /
   9.6 s figure reproduced in seconds (9.9–10.3 s); the 1.22–1.32× did not
   (CS4). Recommendation stands: state condition 13 as structurally met and
   not met at wall-clock, and let `elapsedMs` beside `sessionsParsed` carry
   the truth per run.
4. **Excerpts as an exfiltration path.** No redaction, no warning; the only
   bound is width (table: the resolved column budget; `--json`: 160
   characters), which is wide enough to carry a whole token or an address in
   a tool input under `--tools`. Under the house's own recorded leak class
   (scanner output pasted into a public record) this is exactly the design
   step CS3 says is missing; the seeded question sharpens *what* an excerpt
   can carry — a Bash command line with a credential in it, whole. CS3's
   severity (MODERATE) stands; its counsel gains one item — the caution
   should name tool-input excerpts specifically, and `--tools` in the man
   page should say the input is excerpted whole.
5. **Shared-vocabulary claims, flag by flag.** `--materialise`: same name,
   same skip-and-count default, same opt-in read in `ccarchive` (`--verify`/
   `--audit`), `ccrepo` and `cctranscript --search` — holds. `--top`: same
   per-level truncation after ordering, hidden rows counted and printed —
   holds. `--since/--until`: same name, same on-or-after / on-or-before
   local-day meaning on the message's own timestamp — holds by default;
   diverges under `--utc` (CS5), and at the edges cctranscript validates and
   tolerates dashes where `ccrepo` compares strings unvalidated (a stricter
   sibling, not a conflict). `--from-archive`/`--dest`: identical resolution
   order — holds.
6. **The subagent gap.** Item `090-…` records 417 live subagent logs outside
   every view. Neither the search output nor the man page says so: NOTES
   names `--think` as void and `-n` as inert but not that subagent logs are
   outside the sweep; FILES describes `subagents/` only as the source of the
   *finished* count. For a search, that is a recall gap the user cannot see —
   the same silent-absence class the design's own no-silent-caps rule guards
   against. Recorded as a post-reconcile addition (CS14).

### Post-reconcile additions (clearly marked; phase-1 text unrevised)

**CS13 (note, post-reconcile)** — the design was not reviewed before it was
built to. `docs/reviews/` holds no verdict on the 2026-07-27 design; its §14
deferred review to the design-to-build move, and this pass is that review.
The banner's most important departure (§4 vs §10, a contradiction visible in
the design text alone) and CS1 (gate text ≠ probe text) are both
design-altitude defects a design-time pass would have cost a paragraph to
catch. Not a fault of the build; a data point for `REVIEW.md` § *Review the
design, not only the build*.

**CS14 (minor, post-reconcile)** — `--search` does not tell the user that
subagent logs are outside the sweep. *Evidence:* board item `090-…` (417
live logs); man page NOTES and the summary line carry no such statement;
`allSessions()` walks one level (`cctranscript:256-290`). *Counsel:* one NOTES
sentence and, cheaply, a `meta.subagentLogsSearched: false` field beside
`thinkingSearched` so the machine format states the boundary too.

**Severity amendments:** none. Overall unchanged —
**PASS-WITH-FINDINGS — 0 MAJOR / 3 MODERATE / 6 minor / 5 note** (CS14 minor
and CS13 note added post-reconcile).

- [ ] CS13 — no fix owed on the delta; a data point for the doctrine.
- [ ] CS14 — NOTES sentence + `meta` field; tested by a `--json` field
      assertion and the man-page pin.

## Deferred material (folded in at verdict landing)

# Deferred — the `cctranscript --search` cold pass

*Sibling of `2026-08-15-1032-cctranscript-search-cold.md`. Open only after the
reviewer's own findings are durably written (REVIEW.md rule 1). Fold in below
the verdict and delete this file when the verdict lands.*

## References withheld from the brief

- **Intent record:** `docs/roadmap/210-instruments-open-features/README.md`
  (the *cctranscript learns to search* narrative and the follow-up items
  `050-…`, `080-…`, `090-…` it spawned), and `docs/ROADMAP-DONE.md`
  § *cctranscript learns to search*. The design document itself is in-delta
  and was not withheld.
- **The queue pointer:**
  `docs/roadmap/160-doctrine-review-owed/010-rule-4-review-queued-tier-fable-pass-type-code.md`.
- **Prior verdicts on the instruments** — reconcile only, never anchor:
  `docs/reviews/2026-07-11-instruments-test-floor-code-review.md` and
  `docs/reviews/2026-07-17-1000-adr0006-ccarchive-preserve-cold.md`. The
  design pass of 2026-07-27 has no verdict file of its own — check whether it
  was reviewed at all before being built to.

## The brief-writer's seeded questions

Written by a non-author cold session from the delta alone. A floor, never a
fence — the reviewer's own findings come first.

1. **The banner is the builder marking its own homework.** Six departures are
   declared in the design's status banner. A cold read of the design followed
   by a cold read of the code is the only way to find a seventh. Two places to
   look first: the design's DONE conditions that the banner does *not*
   mention, and any flag in `--help` that the design never named.
2. **The false-negative class in `--regex`.** The banner says the raw-line
   prefilter's escaping gap is "real and documented in NOTES rather than
   papered over" for regex mode. Is a documented false negative acceptable in
   a *search* tool whose whole value is recall, and does the manual page make
   it visible where a user would look, or only in a notes section?
3. **The wall-clock guard replaced by a structural one.** DONE condition 13
   became a `meta.sessionsParsed` assertion. Does the new test pin the
   property the 1.5× condition protected, or a property that is easier to
   pass? Reproduce the 1.22–1.32× and 3.7× figures if a store admits it.
4. **Excerpts as an exfiltration path.** The tool prints tool-input excerpts
   whole (the banner says searching one field is "the quiet wrongness §5
   warns against"). Whole tool inputs can carry secrets and personal data. Is
   there any redaction, truncation, or warning — and should there be, given
   the house's own rule that a scanner output pasted into a public record is
   a leak class it has recorded before?
5. **Shared-vocabulary claims.** The README table says `--since`/`--until`,
   `--top` and `--materialise` are shared vocabulary across the instruments.
   Check each flag's semantics in each instrument that claims it — same name,
   same meaning, same edge behaviour?
6. **The subagent gap.** A follow-up item records that subagent logs sit
   outside every `cctranscript` view. For a search tool that is a recall gap
   the user cannot see. Does `--search` say so in its output or manual page?
