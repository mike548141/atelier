# Cold pass — allow-markers that name a kind, and finding IDs

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/750-rule-4-cold-pass-queued-marker-kinds-and-ids.md`.
**Why it earns a review:** an allow-marker is the house's exemption hatch on every
guard, and this delta changed what one exempts in three guards and printed, on
every finding line of nine, the exact token a reader is told to copy into a
marker. A wrong scope rule silences more than intended; a wrong ID teaches every
reader to write the wrong exemption.

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
  `--stat`, the `allowmarker.py` and `report.py` diffs, the leakscan, spellscan
  and sizescan hunks of the ID commit, **and both message bodies** (the author's
  own account); the subjects and `--stat` of later commits on the same files;
  `REVIEW.md` rules 1–4, the four lenses, the checklist and the lifecycle; the ask
  halves of two 2026-10-04 briefs as templates; `docs/reviews/` filenames and
  filename-level greps (no prior verdict opened); the names, not contents, of the
  commissioning board items; and its harness-loaded memory index. Its orchestrator
  read the `docs/SESSIONS.md` index tail through 2026-10-16 (including the
  authoring run's one-paragraph summary) and the 2026-10-16 session record's close
  section, and passed on no evaluative content beyond the pointer list and a
  one-line note naming four later changes to these files. Everything evaluative
  is in the sibling.

## What the work is

Landing commits (diff these; review the paths at HEAD):

- `db1aa4d` (2026-10-05 19:02 UTC) — tools: allow-markers honour a named kind in
  licenscan, sizescan, pointerscan (115/080)
- `ded8d32` (2026-10-05 19:36 UTC) — tools: print a namespaced finding ID on every
  finding line (115/080)
- both landed in merge `2b261e6` (2026-10-05 19:46 UTC)

Delta paths: `tools/allowmarker.py` (`covers`, `is_blanket`); `tools/report.py`
(`finding_id`, `with_id`, `finding_dicts`); the scanners the two commits touch —
`licenscan`, `sizescan`, `pointerscan` (marker kinds), and `datescan`,
`leakscan`, `licenscan`, `linkscan`, `pathscan`, `pointerscan`, `secretscan`,
`sizescan`, `spellscan` (IDs); their tests `test_allowmarker.py`,
`test_licenscan.py`, `test_pointerscan.py`, `test_sizescan.py`,
`test_report.py`; `tools/README.md`; `CHANGELOG.md`.

**Later commits on the same surfaces — not this delta; do not attribute them to
it.** Several change the very kinds this delta made addressable; review the
delta's rule and IDs at HEAD and say which commit a finding rests on:

- `f9ccba8` (2026-10-16) — sizescan: no hatch silences cold content (115/270)
- `72a68cc` (2026-10-16) — sizescan: the size advisory removed, and the hatches
  it leaves inert named (115/270 c) — the `size-advisory` kind goes
- `e3e8a4f` (2026-10-16) — licenscan: the warning made real (an advisory tier)
- `1c24781` (2026-10-16) — indexscan gains a scoped marker kind
  (`date-mismatch`), though `ded8d32` left indexscan without an ID by definition
- `b609b4b` (2026-10-05), `4dfaf8d` (2026-10-05), `39a74b9` and `f4afb7a`
  (2026-10-16) — test runners, quoted paths, the staged-diff reader, staged line
  numbers, on several of the same scanners

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests
and live behaviour. The lenses organise it; they do not bound it. Non-goals are the
only narrowing and are themselves reviewable.

**The scope rule.** For licenscan, sizescan and pointerscan at HEAD, enumerate
every marker form the shared grammar accepts — none, bare, unscoped, a scope
naming one kind, a scope naming a kind in another case, a scope with a typo, a
list scope naming two kinds, a scope naming a kind the scanner later dropped —
and record which kinds each exempts and how the suppression tally counts it.
Whether "any other scope exempts every kind" is the safe default for a guard;
whether `is_blanket` and `covers` agree for every input; whether the three
scanners' `FINDING_KINDS` match what they actually emit. **The IDs.** For each of
the nine scanners: is the printed kind exactly what that scanner's marker accepts
(round-trip it: copy the ID into a marker and confirm that finding, and only it,
goes)? Cases: a spellscan word with an apostrophe, hyphen, capital or non-ASCII
letter; a leakscan or secretscan finding in a path name, where no line can carry
a marker; a sizescan file carrying two kinds; a finding whose rule name contains
characters the marker grammar rejects. Whether appending `  [<scanner>:<kind>]`
breaks any consumer that parses finding lines — `tools/floor.py`, CI workflows,
`floorfleet`, instruments, the child templates. **Non-goals:** the principal's
pick of "both" (fix markers and print IDs), and item 1 of `115/230` that the
"any other scope" branch defers to — though the deferral itself is reviewable.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Among them: that an additive rule keeps every live marker meaning what it
   meant; that "the kind is exactly the marker's scope" holds for every guard;
   that leaving conflictscan, wrapscan, indexscan, reviewscan, publishscan and
   harvestscan without IDs is a definition, not a gap.
2. **Correctness & quality.** Read `covers`, `is_blanket`, the three scanners'
   marker paths and the ID helpers whole; diff both commits. Build the
   marker-form table and the per-scanner round-trip table. Check the `--json`
   shape (`id` last; sizescan's `ids` list) against any reader of it.
3. **Completeness / harvest.** `tools/README.md`'s marker and ID sections,
   `docs/method/GUARDS.md` on exemptions, `CHANGELOG.md`'s entries, the shared
   grammar's own docstring, and every scanner using its own scope logic instead of
   `covers`: do they describe one rule?
4. **Security & privacy** — mandatory. An exemption hatch that widens silently
   is a bypass of the guard it sits on; hunt the marker that exempts more than it
   names. Also: does an ID ever echo matched content into CI logs — spellscan's
   word, a leakscan machine-local term, a secret fragment — beyond what the line
   already printed? Never quote such content. `/security-review` is discharged
   by grounds (a landed delta; the pending diff is not the work) — say so, and
   deliver the code-altitude read by hand against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest tools.test_allowmarker tools.test_report
  tools.test_licenscan tools.test_sizescan tools.test_pointerscan -v` at HEAD and
  at `2b261e6` in a scratch clone
- the back-compat claims at landing, on this repo and your own fixtures only:
  `db1aa4d^` against `db1aa4d` per marker form, and `ded8d32^` against `ded8d32`
  with the trailing ID and the JSON `id`/`ids` fields stripped (the commits'
  sibling-repo runs are not re-run — never point a scanner at other repos; say so)
- `python3 -m unittest tools.test_floor -v` (its advisory-count contract)
- every touched scanner's `--selftest`; the floor on both planes at HEAD; the full
  Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only
  git is fine. Probes, fixtures and older checkouts go in a private clone under
  your session scratchpad, named by your prefix.
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
brief's sibling
`docs/reviews/2026-10-16-1551-marker-kinds-finding-ids-cold.deferred.md`, and the
commissioning items `080`, `230` and `270` in
`docs/roadmap/115-guardrail-architecture-mike-commissioned/` (barred as a section).

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/750-rule-4-cold-pass-queued-marker-kinds-and-ids.md
--also-exclude docs/reviews/2026-10-16-1551-marker-kinds-finding-ids-cold.deferred.md
--also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never
barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, the standing
checklist V1–V7 each answered or discharged with grounds, both tables, findings
with stable IDs (prefix `MK`: `MK1`, `MK2`, …) and severities (MAJOR / MODERATE /
minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger, and a follow-up checklist. Then STOP and commit phase 1 unrevised
before opening the sibling.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict:
per-finding notes against the seeded questions and the intent record, any finding
formed at reconcile marked as such, and the overall line restated. Never revise
phase-1 text. Then fold the sibling in below the reconcile and delete it.

Findings on self-authored doctrine are the principal's to decide (rule 3; a
guard is doctrine by function): record all, apply nothing; counsel per finding is
welcome, labelled and kept beneath it.

---

## Verdict — phase 1 (2026-10-17 UTC)

### Provenance, repeated

- **Reviewer:** a fresh `claude-fable-5-1` subagent (prefix `MK`), spawned on
  2026-10-17 UTC by a Fable orchestrator that authored none of the delta and none
  of this brief. Tier: Fable, on-tier for rule 4. Neither this session nor its
  orchestrator was started or instructed by the delta's author or the
  brief-writer.
- **Worktree:** `/Users/mike/worktrees/atelier-review-1017`, branch `review-1017`,
  HEAD `46fec06` (carries `8acfff1`). Read-only git only. Older checkouts live in
  a private clone under this session's scratchpad (`…/scratchpad/MK/`), with
  detached worktrees at `2b261e6`, `db1aa4d`, `db1aa4d^`, `ded8d32`, `ded8d32^`.
- **What I read:** this brief; `docs/method/REVIEW.md` (rules 1–4, the four
  lenses, the checklist, the re-run rule); the two landing commits' diffs, stats
  and message bodies; `tools/allowmarker.py` and `tools/report.py` whole; the
  marker and ID paths of all nine scanners plus `indexscan`, `conflictscan` and
  `wrapscan` at HEAD; `tools/test_allowmarker.py`, `tools/test_report.py` and
  the tests the marker commit added; `tools/README.md`'s three marker sections
  and its Finding IDs section; `docs/method/GUARDS.md` on granularity and rule
  (b); `CHANGELOG.md`'s unreleased block; `tools/floor.py`'s count reader and
  CLI; `.githooks/pre-commit`, `.github/workflows/ci.yml`, `floor.yml` and the
  child template; `tools/floorfleet.py`'s readers. Not opened: anything barred
  by rule 2, the sibling, the commissioning items, any other 2026-10-16 brief.
- **Sweep:** `tools/coldsweep.py` with the three `--also-exclude` paths the
  brief lists, five patterns, no `--include-barred`. 429 files barred each run.
- ⚠️ **Exposure, disclosed.** The hook-plane floor run (below) scanned the
  staged plane, which at that moment held another reviewer's brief staged by
  the orchestrator. I read only the floor's summary lines and the two pathscan
  finding lines, which name two docs outside this delta; no content of that
  brief reached me.
- `/security-review` is **discharged by grounds**: the delta landed on
  2026-10-05; the only pending diff in this worktree is other reviewers' drafts.
  The security read is by hand (lens 4).

### Lens 1 — approach and assumptions (named first, then attacked)

1. *An additive rule keeps every live marker meaning what it meant.* Holds —
   re-driven (ledger). But the live set was **empty**: the landing commit's own
   survey found no scoped marker for these three scanners anywhere, and this
   tree at HEAD has none in tracked non-record files. The branch kept "so no
   live marker is voided" protected nothing (MK1).
2. *"The kind is exactly the marker's scope" holds for every guard.* Holds for
   the grammar: every emitted kind — 19 secretscan rules, 16 leakscan rules,
   372 spellscan words, 3 datescan, 3 linkscan, 1 pathscan, 6 + 3 + 3 for the
   three — fits `[A-Za-z0-9_-]+`. Fails for four IDs whose marker can exempt
   nothing (MK2).
3. *Leaving six scanners without IDs is a definition, not a gap.* True at
   landing; `indexscan` has since gained a scoped marker (`1c24781`) and still
   prints no ID, so the definition no longer holds at HEAD (MK4).
4. *Fail-open on an unrecognised scope is a safe default for a guard.* It is
   not: on a publish gate a typo exempts a copyleft header, tallied like a
   legitimate marker (MK1, lens 4).
5. *Counting a marker's presence is enough for GUARDS rule (b).* The delta
   created the first partial-exemption case and the three scanners now tally it
   three ways (MK3).
6. *The grammar's same-line separator holds wherever it is called.* pointerscan
   joins an item's lines with spaces before matching, so it does not (MK5).

### Lens 2 — correctness and quality

`covers` and `is_blanket` agree for every input: enumerated over `None`, `""`,
each declared kind, an upper-cased kind, a two-kind list and a nonsense word,
for all three scanners — zero disagreements. `FINDING_KINDS` matches what each
scanner emits (licenscan six, pointerscan three; sizescan emits two and keeps
`size-advisory` as a retired name on purpose, `72a68cc`). `--json`: `id` is the
last key (pinned); sizescan's `ids` is a list. No consumer parses a finding line
or a `findings` array: `floor.py` reads exit codes and the whole-line advisory
count, `ci.yml`, `floor.yml` and the child template call `floor.py`,
`floorfleet` reads config and GitHub, no instrument invokes a scanner. Both
floor planes read the counts correctly with an ID on every finding line.

**Marker-form table** (HEAD; fixture per scanner: licenscan — Apache LICENSE, a
MIT declaration and a GPL header, marker on both lines; sizescan — a roadmap
with a `[x]` item and an archive store with a `[ ]` item, marker in both
headers, `--check`; pointerscan — the module's live specimen, marker on the
item's first line). "A" is the first named kind, "B" the second.

| form | licenscan (A mismatch, B incompatible) | sizescan (A harvest-integrity, B cold-content) | pointerscan (A state, B grammar) |
|---|---|---|---|
| none | both findings, 0 suppressed | both kinds, 0 allowed | grammar + cycle |
| bare, no colon | as none | as none | as none |
| bare colon, no reason | as none | as none (`-->` is no reason) | **whole item exempt**, 1 suppressed (MK5) |
| unscoped | both exempt, 2 suppressed | archive exempt (1 allowed), roadmap inert | whole item exempt, 1 suppressed |
| `:A:` | mismatch exempt, incompatible stands | archive exempt, cold stands | nothing exempt (item trips no state); no tally line (MK3) |
| `:B:` | incompatible exempt, mismatch stands | both stand, 2 inert | grammar exempt, cycle stands |
| `:A:` upper-cased | **both exempt**, 2 suppressed | **archive exempt** | whole item exempt |
| `:A:` with a typo | **both exempt** | **archive exempt** | whole item exempt |
| `:A,B:` list | **both exempt** (reads as unscoped) | **archive exempt** | whole item exempt |
| `:A:` no reason | **both exempt** (reads as unscoped) | archive exempt | whole item exempt |
| retired `size-advisory` | **both exempt** | both stand, 2 inert (retired name honoured) | whole item exempt |
| unknown word | **both exempt** | **archive exempt** | whole item exempt |

Every bold cell is a scope that names less than it exempts, counted on the
`suppressed:` line exactly like a deliberate one.

**Round-trip table** (HEAD; marker scoped to the printed kind on the finding's
own line, header for sizescan; "others" = every other ID unchanged):

| ID | carrier | that finding gone | others |
|---|---|---|---|
| `secretscan:aws-access-key-id`, `:assigned-secret`, `:jwt` | line | yes | unchanged |
| `leakscan:ipv4` | line | yes | unchanged |
| `leakscan:email` on a path-name hit | none (line 0) | n/a | — |
| `linkscan:missing-file` ×2, `:missing-anchor` | line | yes | unchanged |
| `datescan:relative-time-word`, `:invalid-iso-date`, `:non-iso-date` | line | yes | unchanged |
| `spellscan:color` (from a capitalised word), `:organize` | line | yes | unchanged |
| `pathscan:missing-path` | line | yes | unchanged |
| `licenscan:mismatch`, `:incompatible`, `:unknown-declaration` | line | yes | unchanged |
| `licenscan:unknown-license` | LICENSE line | yes | unchanged |
| `licenscan:expect-mismatch` | LICENSE line | **no** — marker inert, uncounted | unchanged |
| `licenscan:no-license` | none | n/a | — |
| `sizescan:harvest-integrity` | header | yes | unchanged |
| `sizescan:cold-content` | header | **no** — by design (`115/270` a), named inert | unchanged |
| `pointerscan:grammar`, `:cycle`, `:state` | item line | yes | unchanged |

The brief's cases: a spellscan word with an apostrophe, hyphen or non-ASCII
letter cannot arise (none of the 372 denylist words carries one; the ID is
lower-cased and the subtraction compares lower-cased); a sizescan file carrying
two kinds cannot arise at HEAD (a finding is cold on a roadmap or live on an
archive store, never both — MK4 b); no rule name contains a character the
grammar rejects.

### Lens 3 — completeness and harvest

`allowmarker.covers`' docstring, the three scanners' `FINDING_KINDS` comments,
`tools/README.md`'s three sections and `CHANGELOG.md` all state the same rule,
including the fail-open branch. `docs/method/GUARDS.md` asks for rule-scoped
allowance and says nothing about an unrecognised scope, so the estate now runs
two rules under one grammar with no doctrinal home for either (MK1). The
Finding IDs paragraph was not swept by three later commits (MK4). The child
templates carry only the generic marker form and need no sweep.

### Lens 4 — security and privacy (by hand, OWASP Top 10 as the catalogue)

Design altitude: the work's class is a text-processing guard whose only trust
boundary is the marker a contributor writes. The threat is A05 (security
misconfiguration, fail-open): a marker that exempts more than it names is a
bypass of the guard it sits on. The hunt found it: every bold cell above, on
`licenscan` — a **blocking publish gate** — silences a GPL header under an
Apache licence, and the tally cannot tell it from a deliberate exemption
(MK1). Code altitude: A03 injection — the ID is built from constants or from a
denylist word, never from free content; a crafted line can carry ID-shaped
text in its excerpt, but no consumer parses the line and the count regex is
whole-line anchored, which the trailing `]` now makes unmatchable. ReDoS: the
scope pattern is a single bounded class with one optional group; linear. A09
logging: no ID echoes anything the line did not already print — spellscan's
word and leakscan's rule name were already there, the term itself stays
redacted. Privacy: nothing new leaves the tree. No other OWASP vector reaches a
stdlib CLI that reads files and prints.

### Standing checklist

- **V1** — the landing message says tallies "keep counting on the marker's
  presence, as they did"; licenscan's new code does not (it leaves the finding
  and counts nothing for a scope that misses), which is better than claimed
  but not what was claimed (MK3). "Copies into the narrowest marker there is"
  is stronger than four IDs support (MK2).
- **V2** — every recorded claim re-run (ledger); the sibling-repo runs not
  re-run, by rule.
- **V3** — the Finding IDs paragraph is a mirror site three later commits
  missed (MK4); no child template states kind semantics, nothing to sweep.
- **V4** — the scope rule has one home (`covers`) for three scanners and five
  per-scanner copies of the opposite rule; GUARDS.md holds neither (MK1).
- **V5** — `covers`' stated grounds contradict the same commit's survey (MK1);
  README says "takes no scope" of a scanner that now does (MK4).
- **V6** — above; scanner discharged by grounds.
- **V7** — stated in the brief and here.

### Findings

**MK1 — MAJOR (doctrine: the principal's to decide; rule 3).** The "any other
scope exempts every kind" branch of `allowmarker.covers` is kept on grounds the
delta's own evidence refutes, and it is a fail-open hatch on a blocking gate.
The docstring keeps it "because refusing it would void any live marker written
that way"; the same commit's message reports no live scoped marker for these
three scanners anywhere in the estate, and this tree at HEAD has none. So
fail-closed cost nothing at landing. What the branch buys instead: on
licenscan, six of the twelve marker forms in the table — a kind in another
case, a typo, a two-kind list, a scope with its reason forgotten, a kind from
another scanner, any word — silence an incompatible copyleft header and are
tallied as one ordinary suppression; on sizescan the same forms exempt an
archive store's harvest-integrity check. The branch has already had its first
concrete cost: `size-advisory` must stay in `FINDING_KINDS` forever (`72a68cc`),
because dropping a retired name silently widens any stale marker to the
unscoped form — every kind ever named becomes a permanent reserved word. And
the estate now runs two rules under one grammar (five scanners fail closed on
an unrecognised scope, three fail open) with `GUARDS.md` silent on both. Rests
on `db1aa4d`; the scope-with-no-reason form is the pre-delta grammar's
backtrack (pinned in `test_allowmarker`, same class). Recurrence-prevention
step, as counsel: an unrecognised scope exempts nothing and is reported as an
unrecognised hatch (the shape sizescan's inert-hatch report already has), the
rule written into `GUARDS.md` once for every scanner; `115/230` item 1 can then
be the same ruling rather than a second one.

**MK2 — MODERATE.** Four printed IDs copy into a marker that cannot exempt the
finding, and two of them fail silently. `licenscan:expect-mismatch`: a marker
scoped to it on the LICENSE line (the only line the finding names) exempts
nothing, is not counted and is not reported. `licenscan:no-license`: no file
exists to carry it; the README's licenscan section lists four markable kinds
while `FINDING_KINDS` and the printed IDs cover six. `sizescan:cold-content` is
inert by ruling (`115/270` a) and the report says so; `leakscan:<rule>` on a
path-name hit says "in the path name". The README's "still gets an ID" discloses
that the ID exists, not that the marker it points at is dead; the paragraph's
headline — the ID "copies into the narrowest marker there is" — is what a
reader acts on. Rests on `ded8d32` (the IDs) and `db1aa4d` (the two kinds in
`FINDING_KINDS` that no marker reaches). Counsel: print those IDs without the
copy-me promise (a `no marker` tag, or no bracket), and have licenscan name an
inert scoped marker the way sizescan does.

**MK3 — minor.** Three scanners, three tallies for a scoped marker that exempts
nothing. licenscan leaves the finding and counts nothing. pointerscan counts
"1 pointer(s) by allow-marker" for a scope naming a detector the item never
tripped, and prints no `suppressed:` line at all when findings remain — so the
partial case the delta created (one detector exempted, another standing) is
the one case the report never shows, against GUARDS rule (b). sizescan at HEAD
counts only a real exemption and names the rest inert. Rests on `db1aa4d`
(the partial case) over a pre-delta render path.

**MK4 — minor.** Three statements on the delta's surfaces are false at HEAD,
each resting on a later commit that did not sweep them: (a) the Finding IDs
paragraph says `indexscan`'s marker "takes no scope, so there is no kind a
marker could name" — since `1c24781` it takes one (`date-mismatch`), and
indexscan is now a scanner with a scoped marker and no ID, the combination the
design says cannot exist; (b) README and CHANGELOG say sizescan reports "up to
two kinds" per file with an `ids` list — since `72a68cc` a finding is cold on
a roadmap or live on an archive store, never both, so `ids` always holds one;
(c) `_kinds` still lists both names, harmless but misleading. V3/V5.

**MK5 — minor (pre-delta, named as such).** pointerscan folds an item's lines
into one space-joined body before the marker grammar runs, so a bare
`pointerscan:allow:` at a line end reads as the unscoped form with the next
line's first word as its reason, and exempts the whole item — identical at
`db1aa4d^` and HEAD (table, row 3). The grammar's same-line separator is
defeated by the caller. Not this delta's, but the printed ID will put more
scoped markers into item bodies, where a dropped reason now widens silently.
Counsel: match the marker per physical line, before the join.

**Overall: PASS-WITH-FINDINGS — 1 MAJOR · 1 MODERATE · 3 minor · 0 note.**

### Re-run ledger

| claim / check | where | result |
|---|---|---|
| five test modules the brief names | HEAD | 318 tests, OK |
| same five | `2b261e6` (scratch clone) | 272 tests, OK |
| `tools.test_floor` (advisory-count contract) | HEAD | 144 tests, OK |
| `--selftest`, nine touched scanners | HEAD | all OK, exit 0 |
| marker-form back-compat, `db1aa4d^` vs `db1aa4d` | 36 fixture runs | byte-identical except the named-kind forms (6) and `size-advisory`, then live (1) |
| ID back-compat, `ded8d32^` vs `ded8d32`, IDs and `id`/`ids` stripped | 18 fixture runs + 18 runs over this tree | byte-identical |
| sibling-repo runs | — | not re-run: no scanner pointed at another repo |
| floor, hook plane | HEAD | exit 0; pathscan 2 warn-only findings in two docs outside the delta |
| floor, ci plane | HEAD | exit 0; secretscan 23 advisory, leakscan structural-only, same pathscan 2 |
| full Python suite, once, foreground | HEAD | 1916 tests, OK |
| `node --test` | — | not run: not on the brief's list; no instrument touched |

### Follow-up checklist

- [ ] MK1 — the principal rules fail-open or fail-closed for the three
      scanners, and the one rule goes into `GUARDS.md` (`115/230` item 1 is the
      same question).
- [ ] MK2 — IDs with no reachable marker print without the copy-me promise;
      licenscan names an inert scoped marker.
- [ ] MK3 — one tally rule for a scoped marker that exempts nothing;
      pointerscan prints its `suppressed:` line when findings remain.
- [ ] MK4 — sweep the Finding IDs paragraph, the sizescan "two kinds" wording
      and `_kinds` for `1c24781` and `72a68cc`.
- [ ] MK5 — pointerscan matches markers per physical line.
