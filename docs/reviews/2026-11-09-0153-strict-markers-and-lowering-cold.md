# Cold pass — a malformed allow-marker goes strict after a dated warning (160/480, 160/110), and a check may be lowered only declared, reasoned and expiring (020/170)

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (doctrine by
function: the shared marker reader in every child, and guard doctrine).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** ACT 1 WRITTEN 2026-11-22 UTC: PASS-WITH-FINDINGS (0 MAJOR, 3 MODERATE, 4 minor,
3 notes); act 2 (reconcile) pending the sibling's release. Run on Fable 5.1 under the principal's
drain order of 2026-11-23 NZDT. Brief written 2026-11-09 UTC by session `d16dc612`, a headless
Opus 5.5 brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/1190-rule-4-cold-pass-queued-strict-markers-and-lowering.md`
(barred until phase 2).
**Size:** large: 32 files and 1,158 added lines in the marker commit across every scanner that reads
it, one doctrine commit, and a fleet census to re-derive.
**Why it earns a review:** `tools/allowmarker.py` decides what a scanner exempts in every child, and
it floats at `main`. A wrong read exempts a real secret or leak silently, or reds a child on the
cut-over date. The lowering rule decides how a repo may soften a check at all.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `722ac2e2`,
  2026-11-09, in its ruling round, and the Sonnet worker it dispatched, which wrote the work (per
  the queue pointer). The author queued this pass and does not take it.
- **Who wrote this brief:** session `d16dc612` (`claude-opus-5-5`), a headless brief-writer started
  on 2026-11-09 by coordinating session `74f2b8cd` (Opus 5.5). `74f2b8cd` built none of this delta
  and forms no finding; its launch prompt was the only instruction, and it carried item numbers, the
  owed-or-not test and house rules, no framing of the work. **Off-tier for review, disclosed: the
  brief-writer forms no finding and writes no severity**, ran no review and used no Fable model.
  Neither was started or instructed by the author. Whoever writes a brief does not run it (the
  principal's rule), so both are barred from this pass.
- **Who reviews:** a session on Fable 5.1 that passes rule 4's criterion, started once the principal
  has approved the Fable pass. **Barred from reviewing:** session `722ac2e2` and every worker it
  dispatched; `d16dc612`; `74f2b8cd`.
- **The principal's approval of this brief:** his request, 2026-11-09, verbatim: *"Check all the
  repo's, any work that requires a fable review but does not have a brief written yet I want you to
  write those briefs then finish this session when thats all done"*. That approves the brief only;
  the Fable gate on the pass is unchanged.
- **Contact, disclosed (rule 4):** the brief-writer had no contact with `722ac2e2` or its workers.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  `skills/review-brief/SKILL.md` and `docs/method/REVIEW.md` whole; the house-form brief
  `docs/reviews/2026-11-06-2027-secretscan-exempt-private-keys-cold.md` lines 1–728, verdict
  included (another surface); the queue pointer whole; the intent records' answer and closing notes,
  by extraction; commit subjects and file lists; the delta's `CHANGELOG.md` entries; the results of
  the re-run lines; parts of the delta's own files at HEAD (outlines, constants, comments). It
  opened no commit message body of this delta, and did not open `docs/SESSIONS.md`, `docs/sessions/`
  or the prior verdict on this subject. Its harness loaded user-level and repo instruction files and
  a memory index, which hold private context this brief does not carry. Everything evaluative is in
  the sibling, by count here: a held-back sibling with one pointer block, 3 questions and 2 facts.

## The acceptance test

The principal's answer on `160/480`, 2026-11-09, verbatim: *"Strict, with a warning period"*. The
option read: count broken markers across every repo first; a malformed marker then warns for a set
period (about 30 days) while items are queued in the affected repos, and after that it exempts
nothing. The same answer covers `160/110`'s LK1. The principal's answer on `020/170`, the same day,
verbatim: *"Allow if declared + expiring"*. The option read: a repo may lower a check's response
only with a written reason and an end date, visible in the fleet view; the new model replaces
E6d(i)'s "never lower" wording.

The offered option's words were written by the authoring session and put to the principal; the
quoted pick is his. Recorded as an answer, not a ruling in his words: where the delta's wording goes
past what he picked, say so. These are claims to test, not settled scope.

## What the work is

Two commits on `main`: `6d26b058` (the marker reader and the scanners) and `44f66053` (doctrine).

Commits on `main`: `6d26b058`, `44f66053`. The landing commit is `44f66053`. **Check your tree has
it before reading anything:** `git merge-base --is-ancestor 44f66053 HEAD` exits 0, and an
orchestrator merges `origin/main` into the review branch before it spawns.

Delta paths: `tools/allowmarker.py`, `tools/blockscan.py`, `tools/datescan.py`, `tools/leakscan.py`,
`tools/linkscan.py`, `tools/pathscan.py`, `tools/reviewscan.py`, `tools/secretscan.py`,
`tools/spellscan.py`, `tools/stampscan.py`, `tools/test_allowmarker.py`, `tools/test_leakscan.py`,
`tools/test_pathscan.py`, `tools/test_report.py`, `tools/test_reviewscan.py`, `tools/README.md`,
`tools/leakscan-terms.example.txt`, `docs/method/GUARDS.md`, `docs/method/README.md`,
`.conflictscanignore`, `.leakscanignore`, `.licenscanignore`, `.secretscanignore`,
`.spellscanignore`, `.stampscanignore`, `.wrapscanignore`, `CHANGELOG.md`. Read each at HEAD and
read each commit body-free, scoped to paths so board records stay barred:

```
python3 tools/coldsweep.py --root . --commit 6d26b058 --path tools/allowmarker.py --path tools/blockscan.py --path tools/datescan.py --path tools/leakscan.py --path tools/linkscan.py --path tools/pathscan.py --path tools/reviewscan.py --path tools/secretscan.py --path tools/spellscan.py --path tools/stampscan.py --path tools/test_allowmarker.py --path tools/test_leakscan.py --path tools/test_pathscan.py --path tools/test_report.py --path tools/test_reviewscan.py --path tools/README.md --path tools/leakscan-terms.example.txt --path docs/method/GUARDS.md --path .conflictscanignore --path .leakscanignore --path .licenscanignore --path .secretscanignore --path .spellscanignore --path .stampscanignore --path .wrapscanignore --path CHANGELOG.md
python3 tools/coldsweep.py --root . --commit 44f66053 --path CHANGELOG.md --path docs/method/GUARDS.md --path docs/method/README.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Commits since the delta on these paths:

```
git log --oneline 44f66053..HEAD -- tools/allowmarker.py tools/blockscan.py tools/datescan.py tools/leakscan.py tools/linkscan.py tools/pathscan.py tools/reviewscan.py tools/secretscan.py tools/spellscan.py tools/stampscan.py tools/test_allowmarker.py tools/test_leakscan.py tools/test_pathscan.py tools/test_report.py tools/test_reviewscan.py tools/README.md tools/leakscan-terms.example.txt docs/method/GUARDS.md docs/method/README.md .conflictscanignore .leakscanignore .licenscanignore .secretscanignore .spellscanignore .stampscanignore .wrapscanignore CHANGELOG.md
```

At `457615cc` this printed 4 commit(s). Read anything new the same way.

**Application pass.** `160/480` and `160/110` apply the principal's answer and earlier passes'
counsel. It cannot fully honour rule 2: the delta carries finding ids and the decisions stamped on
them. Sequence (`REVIEW.md` § *Applying decisions to doctrine*): review the work at HEAD and commit
findings first; open the prior verdict after. Name that residual exposure in the verdict.

**Claims the work makes (extracted from its own changelog entry and files, not evaluated):**

- A malformed scoped marker exempts nothing from 2026-12-09. Until `MALFORMED_GRACE_UNTIL` (a dated
  constant, no flag or variable moves it) it still does, and every run warns on stderr.
- `python3 tools/allowmarker.py --census` lists malformed markers read-only. The changelog says a
  census of every repo with a floor found no live malformed marker, only documentation mentions.
- A marker inside an inline code span is a mention; `reviewscan`'s deferral waiver reads the shared
  grammar; a marker naming no rule is counted.
- `leakscan`: terms compared in Unicode NFC; the derived-form separator takes `/` and `+`; the path
  plane no longer honours a marker spelt in a filename.
- `GUARDS.md` § *Provenance, not direction*: a repo may lower a check's response only with a written
  reason and an end date, visible in the fleet view; the tool never lowers one on its own judgement.
  A table sets each lowering mechanism against the rule, with two gaps named as follow-ups.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** the two gaps the delta names in the lowering table, except where a claim depends on
them.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself, first, and damage each
with a probe or confirm it by re-driving. Ask whether this is the right problem, solved at the right
altitude.
2. **Correctness & quality** — does the work do what its claims above say; honest about done versus
stubbed; any overclaim or silent scope cut, each recorded against the text that makes it.
3. **Completeness / harvest** — every surface that states the rule (V3), one home (V4), no
contradiction with sibling doctrine (V5), tests that would stay green on a broken check, what
already exists that this ignored.
4. **Security & privacy** — mandatory. This delta changes what a guard exempts, in every child, on a
date. Treat each marker form as hostile input. Aim `/security-review` at the `tools/` diff from a
clean tree, or discharge it by grounds. Quote no fixture's secret-shaped bytes.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-09 UTC, from the worktree root
at `457615cc`; results are in the sibling. Read exit codes explicitly. Check `uptime` first and run
heavy lines under `nice -n 10`. Python is the `python3` on `PATH` (the tests need 3.10 or later;
`/usr/bin/python3` is 3.9 on this machine and some modules fail at import).

- `cd tools && python3 -m unittest test_allowmarker`
- `cd tools && python3 -m unittest test_leakscan`
- `cd tools && python3 -m unittest test_pathscan`
- `cd tools && python3 -m unittest test_report`
- `cd tools && python3 -m unittest test_reviewscan`
- `python3 tools/allowmarker.py --census --root .`
- `nice -n 10 python3 tools/floor.py --plane ci --root .`
- `nice -n 10 python3 tools/floor.py --plane hook --root .`
- `nice -n 10 python3 -m unittest discover -s tools`
- the adopting child repos, read-only and by count only: `python3 tools/floorfleet.py --root <the
  directory that holds the main atelier checkout and its sibling clones> --json` to a scratch file;
  then, for each child the report marks wired, `python3 tools/allowmarker.py --census --root
  <child>`, totals only

## House rules for this run

- **Live systems:** read-only reads of live systems as needed; **no live writes**. A check that
  would need a write is marked NOT RUN in the verdict, with what it would have shown.
- Probes run on scratch copies and synthetic fixtures under your scratchpad only, deleted when you
  finish. Never mutate the worktree's `tools/` or `instruments/`.
- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live: touch nothing outside your worktree and scratchpad.
- Read-only git only, beyond committing this one file at the end of each phase (or handing it to the
  orchestrator to commit).
- Child repos are read-only and counted, never named: quote no child's name, path or excerpt.
- One heavy process at a time; foreground, long timeout. Never run an installed tool by bare name
  from `PATH`: use the worktree's own copy.
- `/security-review` reads the session's pending diff, not this delta. Aim it at the code by
  reproducing the diff in a scratch clone, or discharge it by grounds, never with this brief or its
  sibling dirty. Over markdown its clean pass is empty; weigh it as nothing.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo is
  PUBLIC: quote no secret, placeholder token, email address, child repo name or path.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the
deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the
reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, this brief's sibling
(`2026-11-09-0153-strict-markers-and-lowering-cold.deferred.md`), every delta commit's message body,
the queue pointer
`docs/roadmap/160-doctrine-review-owed/1190-rule-4-cold-pass-queued-strict-markers-and-lowering.md`,
and the intent records beyond their titles:

- `docs/roadmap/160-doctrine-review-owed/480-rule-4-cold-pass-queued-the-shared-allow-marker-grammar.md`
- `docs/roadmap/160-doctrine-review-owed/110-the-e7-leakscan-cycle-closed-2026-08-09-0-majo.md`
- `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/170-f1-rebuild-the-block-vs-advise-model-from-base.md`

Prior verdicts on this subject, barred until your own findings are committed (rule 2; `coldsweep`
excludes `docs/reviews/` by default):
`docs/reviews/2026-10-03-0357-shared-allow-marker-grammar-cold.md`,
`docs/reviews/2026-08-09-0826-e7-leakscan-build-cold.md`. The delta's docstrings, comments, ADR
text, `tools/README.md` and `CHANGELOG.md` entries carry the author's account of why; they are the
delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1190-rule-4-cold-pass-queued-strict-markers-and-lowering.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/480-rule-4-cold-pass-queued-the-shared-allow-marker-grammar.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/110-the-e7-leakscan-cycle-closed-2026-08-09-0-majo.md \
  --also-exclude docs/roadmap/020-policy-as-code-programme-five-tracks-mik/170-f1-rebuild-the-block-vs-advise-model-from-base.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, any orchestrator, what you read, the UTC day you ran on),
per-lens answers, V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (`6d26b058` and `44f66053`: read body-free
yes/no, findings by id), findings with stable ids (prefix `SML`: `SML1`, `SML2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands and results, children by count only) and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta commits' bodies;
append `### Reconcile` beneath your verdict: per-finding notes against the sibling's questions and
the author's account, any finding formed at reconcile marked as such, and the overall line restated.
Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

Every finding on this delta is the principal's to decide (rule 3): record all, apply nothing.
Counsel per finding is welcome, labelled as counsel and kept beneath it.


---

## Verdict (act 1) — written 2026-11-22 UTC

**Overall: PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE · 4 minor · 3 notes** (SML1–SML10).

### Provenance (rule 4, V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named tier, checked at selection.
  Ran on 2026-11-22 UTC (20:00–21:30 UTC) in the review worktree
  `/Users/mike/worktrees/fable/atelier-160-1190-1958/atelier`, HEAD `3232a7c3`, made from
  `origin/main`; `git merge-base --is-ancestor 44f66053 HEAD` exits 0. Read-only to me except
  this file and my review log.
- **Spawn:** a headless per-pass orchestrator, session `c7e7ec68` (Opus 5.5), itself started by
  drain session `eca14b23` (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold the
  context partition, form no finding and write no severity. `eca14b23` wrote no brief and no
  delta and started no brief-writer for this pass. I was not started or instructed by `722ac2e2`
  or any worker it dispatched, by `d16dc612` or by `74f2b8cd`.
- **Approval:** the principal's weekly drain order of 2026-11-23 NZDT, verbatim: *"Start a fable
  drain or whatever it is called now. Target 100% of weekly budget by 11.30am NZT todat"*.
- **Spawn prompt, as received (process only):** it named the item, this brief, the worktree, the
  finding prefix `SML`, the barred list (the sibling, removed from the worktree on purpose and
  not to be sought in git history, other checkouts or temp; rule 2's records; commit bodies;
  plain `git show`), what I may write (this file below a divider, and a review log at
  `~/.claude/fable-drain/notes/atelier-160-1190-1958.md`), the load rule (`nice -n 10`, one
  suite at a time), the live-systems rule (reads only), the public-repo rule (no session names,
  private repo names or paths, child names, email addresses or placeholder tokens), the
  `/security-review` caution, and the two-act shape ("Act 1: append your full verdict ... then
  STOP. Do not read the sibling."; the orchestrator does the fold). It carried no question about
  the delta, no pointer to where the risk lives and no request about any finding. Its full text
  is in session `c7e7ec68`'s transcript; I hold no other copy to attach.
- **Contact during the pass:** one message from `c7e7ec68`, process only, after my turn ended on
  a monitor wait: *"please continue act 1 ... Wait for yours in the FOREGROUND instead ... then
  carry on with the child census, the dated-clock probe and the verdict. Do not end your turn
  until act 1 is written"*. It changed how I waited for the test run, nothing else. No contact
  from the author, the brief-writer or its coordinator.
- **What I read:** the brief whole; `docs/method/REVIEW.md` rules 1–4, lenses, re-run and the
  checklist; the two delta commits body-free through `coldsweep --commit --path` (26 and 3
  files); the three later commits on the reader (`55c7d409`, `2b8bcd92`, `a78ee8b0`) the same
  way, because the brief says to read anything new on the delta paths and the review is of HEAD;
  `tools/allowmarker.py` whole and `docs/method/GUARDS.md`, `tools/README.md` at the changed
  sections, all at HEAD; sweep hits in `CHANGELOG.md`, `docs/method/README.md` and the
  2026-11-16 census under `docs/method/census/` (two table rows). **Not read:** the sibling,
  `docs/sessions/`, any prior verdict, the queue pointer, the three intent records, any delta
  commit body, any board file. The harness loaded user-level and repo instruction files and a
  memory index that hold private context this verdict does not carry.
- **Residual exposure (application pass):** the delta's docstrings, comments, README and
  changelog carry the prior passes' finding ids (AM1–AM13, LK1–LK6) and the decisions stamped on
  them. I met them as part of the delta, formed my findings at HEAD first, and open the prior
  verdicts only in act 2.

### The acceptance test, re-driven

- *"Strict, with a warning period"* (`160/480`, `160/110` LK1). Built as read: a malformed scoped
  marker is honoured and warned on stderr until `MALFORMED_GRACE_UNTIL` = 2026-12-09 (30 days
  from the answer), then exempts nothing; one dated constant, UTC clock, no override (tests
  pinned at both dates; the suite reads the same with the clock at 2026-12-10, re-run below).
  The warning reaches the CI log through the floor (re-run below). The "count ... across every
  repo first" half was a one-off hand census and nothing carries it through the period (SML2);
  the "items queued in the affected repos" half had nothing to queue (0 live in 22 children).
- *"Allow if declared + expiring"* (`020/170`). The ruled subsection restates the pick faithfully
  for floor `advisory`/`disabled`. It goes past the pick in one place: it carves line markers
  and ignore-file globs out of the end date as "acceptances", a reading the pick does not
  contain and that the same file's Granularity table contradicts for globs (SML3). The older
  invariant block it is "stricter than" was left as written (SML4), and the table it offers as
  "a list and not a feeling" omits the repo level (SML5).

### Lens 1 — approach and assumptions (named first, then probed)

| # | Load-bearing assumption | Probe | Result |
|---|---|---|---|
| A1 | The malformed shape can be told from an honest unscoped marker with a colon in its reason | P1, P5, `FINE` cases re-run | Holds for a spaced reason. **Fails for a glued reason with a later colon** (SML6) |
| A2 | Blanking inline code spans makes a documented mention safe | P1–P3; the one fleet row | Holds per line; **a span that wraps to the next line is not blanked** (SML7) |
| A3 | Registering patterns by compiled object is stable | P6 | Holds: `re.compile` caches; same object, both registered |
| A4 | "Every run warns" reaches a reader | floor ci run | Holds: stderr passes through the floor; 3 warnings printed in atelier's own CI (on fixtures) |
| A5 | The grace is a dated constant no caller can move | source read; `test_the_cut_off_is_a_constant_with_no_override` | Holds (the test would miss `from os import environ`; no such line exists) |
| A6 | The census is the count the acceptance test asked for | census at HEAD and over 22 children | It lists fixtures and live markers alike; no run-time count exists (SML2) |
| A7 | The suite stays green past 2026-12-09 | scratch clone, clock at 2026-12-10, full discover | Holds: 3382 OK; floor ci exit 0 |
| A8 | New print sites neutralise what they echo, as 160/730 RT3 and AM9 require | P2b, P3b, P4b | **Fails**: the grace warning and the census echo ESC, bidi, CR, BEL and a glued token raw (SML1) |
| A9 | Right problem, right altitude | reading | Yes: the shared reader is the one place; one edit reaches every scanner; the doctrine change is one subsection with its mechanism table |

### Lens 2 — correctness and quality (the five claims)

1. Malformed marker exempts nothing from 2026-12-09, warns until then, one constant. **Holds**
   (tests at both dates; probes; clock-advanced run). Honest about the one shape it cannot tell
   apart (`m:allow:ipv4`, later closed by `2b8bcd92`), but the README's "glued word then a space"
   sentence overstates (SML6).
2. `--census` lists malformed markers read-only; the fleet census found no live marker, only
   mentions. **Reproduces**: 11 rows in atelier (fixtures and one docstring), 1 in 22 children (a
   wrapped code-span mention). The tool cannot itself tell a mention from a live marker (SML2).
3. Code-span mention; `reviewscan` deferral waiver through the grammar; a scope naming no rule is
   counted. **Hold**: `scan_brief` uses `parse_allow(line) == "deferral"`; `names_no_rule` is
   wired in five scanners with name sets (`secretscan.ALL_RULES` is a frozenset of names);
   `linkscan`'s kind set has three members where the README table says two (SML8).
4. `leakscan` NFC, `/` and `+` separators, path plane honours no marker. **Hold** (471 tests;
   `honour_markers=False` at `scan_path_name`).
5. GUARDS § *Provenance* rule and table. **Holds as stated; the wording goes past the pick**
   (SML3–SML5). The CHANGELOG's AM11 line reads as a change this commit made; the skill text
   predates it (SML9).

### Lens 3 — completeness and harvest

- V3 sweeps clean for AM6 (one test comment says "gitignore-style"; no scaffold under
  `docs/build/` or `skills/` carries an ignore-file header). E6d(i) wording survives only as
  history in GUARDS and the changelog. The 2026-12-09 date has one code home.
- What already existed and this ignored: `report.safe_text` / `report.broken` for echoed text
  (SML1); the Repo row of the Granularity table (SML5). What arrived later and the delta's
  text now contradicts: 110/060's optional `review-by` on ignore globs (SML3).
- Tests that would stay green on a broken check: none found. The unknown-scope test drives each
  scanner; the clock tests pin both sides; the no-override test is weak (A5) but not green on a
  break that exists.

### Lens 4 — security and privacy (V6)

- `/security-review`: **discharged by grounds**. It reads the session's pending diff; this
  worktree's pending set is the deliberate sibling deletion and this brief, so an aim at the
  delta needed a scratch reproduction of a 1,158-line, 26-file landed diff, and its clean pass
  over the Markdown half would weigh as nothing. The lens was worked directly instead: every
  marker form treated as hostile input on the new read paths (`_read`, `is_malformed`,
  `is_scope_without_reason`, `blank_code_spans`) and the new print paths (`_warn_malformed`,
  `census`/`main`).
- Direction of failure: every new read path fails closed (a malformed, reasonless, code-span or
  wrapped mention exempts nothing, or exempts only until the date with a warning). No crafted
  shape widens an exemption beyond what the pre-delta reader already granted.
- Echo paths: **SML1**. Bounded regexes (`{1,80}?`, `{0,40}`), no catastrophic backtracking
  found in `_malformed_rx` or `_no_reason_rx` (comma-separated alternation, linear).
- Privacy: the census and warning show a marker head, never the line; a token glued into a
  broken head is the one way a value reaches stderr (SML1, P4b).

### V1–V7

- **V1** no claim stronger than its evidence: SML6, SML9; "no live malformed marker" reproduces.
- **V2** re-run every live-proven claim: all re-run lines run (ledger below); the fleet census
  re-derived by count.
- **V3** mirror sites: clean for the grammar; GUARDS/README/changelog/census agree on the date.
- **V4** one fact, one home: SML4 (two statements of the lowering rule), SML8 (kind set vs table).
- **V5** no contradiction: SML3 (glob at the Check level vs glob as acceptance). Cross-references
  checked for the rule reached: GUARDS § Granularity → `tools/README.md` *Allow markers and
  ignore files* holds the grammar and the scope table it promises; the subsection's link to
  `#granularity--the-axis-that-was-doing-silent-work` reaches the table it cites.
- **V6** above. **V7** above.

### Findings

**SML1 — MODERATE (security).** The grace warning (`tools/allowmarker.py` 306–318,
`_warn_malformed`) and the census (`main`, 737–738) print the marker head unneutralised. Probe:
`demoscan:allow:a<ESC>[2J<U+202E>EVIL<CR><BEL>: why` → the warning carries ESC, the bidi
override, CR and BEL raw to stderr; `census_line("x leakscan:allow:a<ESC>[2J<U+202E>EVIL: why")`
returns the head raw and `main` prints it with the file path; a 20-character example access-key
token with a trailing comma glued into the scope is echoed in full. This is the class of 160/730
RT3, and AM9 in this same delta pinned it for the ignore-loader path (`report.broken`); the
post-delta 110/010 note (`_note_unparseable`) maps non-printables to `?` and caps the head at 40,
which shows the house rule was known. The warning path ends 2026-12-09; the census is permanent.
*Recurrence prevention (counsel):* route both through `report.safe_text`, cap the warned head as
the note does, and pin both sites with the shape of `test_the_head_is_bounded_and_printable`.

**SML2 — MODERATE (lens 3; GUARDS § *Fail noisy, then subtract*; the acceptance test).** The
answer's first half, "count broken markers across every repo first", was done once by hand on
2026-11-09 and nothing carries a count through the 30 days: no scanner `Tally` field, no `--json`
key, no `floorfleet` column; `malformed_seen()` has no caller but tests (`grep` over `tools/`);
a line honoured through the grace counts under "N by allow-marker" like a well-formed one. The
only run-time signal is a stderr warning. Contrast AM10 in the same delta, which gave the
unknown-scope case `markers_naming_no_rule` on the suppressed line and in JSON. The census
cannot tell a fixture from a live marker (11 rows at HEAD, all in `tools/` fixtures and one
docstring; 1 row in 22 children, a wrapped documentation mention) so the "0 live" claim rests on
hand inspection. *Counsel:* a `markers_malformed_honoured` count on the suppressed line and in
JSON, mirroring AM10, so the fleet board can show it until 2026-12-09; and have the census skip
paths the scanner's own ignore globs exempt and flag rows inside a quoted string or an unmatched
backtick as probable mentions.

**SML3 — MODERATE (V5; the wording goes past the pick).** GUARDS § *Provenance* 534–539 says the
end date is "always required" at the *check* and *repo* levels, then carves "a *line* marker and
an ignore-file *glob*" out as acceptances with no end date. § *Granularity* 352–356 places the
ignore-file glob at the **Check** level ("A check, or a path, across the repo"). The same file
therefore both requires and waives an end date for a glob. The carve-out is the author's
reading: the principal's pick spoke of "a check's response ... with a written reason and an end
date" and said nothing about globs or line markers. At HEAD the table's last row ("End date:
none, by design") is also behind the machinery: 110/060 (`2522f4fe`) gave ignore globs an
optional `review-by` (`allowmarker.py` 540–671, read by `wrapscan`), which treats a glob as a
thing that can be a deferment. *Counsel:* this is the principal's to decide: either a glob is a
check-level lowering and takes an end date like `advisory`, or it is an acceptance and the
Granularity table moves it to the Line row; either way the last table row should say
"`review-by`, optional (110/060)". The line-marker carve-out matches the rule's own text ("what
they say about one line ... does not decay") and the Granularity table; only the glob is in
tension.

**SML4 — minor (V4).** The invariant block at GUARDS 496–514 (the blockquote and condition 4,
"Expiring, where the claim rots") still states the pre-ruling rule unqualified; the ruled rule
sits beneath it as a subsection that says it "is stricter than condition 4". A reader who stops
at the blockquote, which is the rule's canonical form and the one `docs/method/README.md:86`
summarised before this change, gets the weaker rule. *Counsel:* qualify condition 4 in place
("at the line level; at the check and repo levels the end date is always required, § *Ruled
2026-11-09*") so the rule has one statement.

**SML5 — minor (lens 3).** The lowering table (544–549) claims to set "each lowering ... against
the rule today, so the gap is a list and not a feeling", and the subsection says the rule binds
"at the *check* and *repo* levels", yet the table has no Repo row. § *Granularity* names three
repo-level mechanisms (not wired, adopt mode, bypassed hook); § *Adoption* (752–756) says adopt
mode is a deferment with reason and expiry (C3 built); a bypassed hook or an unwired repo has
neither (§ *Side-stepping*, C4 open). The fleet report at HEAD shows 1 of 23 children absent,
which is the repo-level case the table does not list. *Counsel:* add the three Repo rows with
their honest state.

**SML6 — minor (V1).** `tools/README.md` § *Fails closed* and the reader's comment (277–286) say
a glued word "followed by a space and more words (`datescan:allow:historical record`) is still
read as an unscoped marker whose reason lacks its leading space". Probe P1: the same shape with a
colon later in the reason (`demoscan:allow:historical record: see ADR 0005`) is read as
**malformed**: during the grace it exempts and warns; from 2026-12-09 it exempts nothing. The
census lists the shape, so a repo would find it, but the documented rule is wrong for a reason
that contains a colon within 80 characters, a common shape ("see X: Y"). *Counsel:* state the
limit in the README beside the example, or exclude a head with a space from `_malformed_rx`
except where the space follows a comma (the documented "space inside a composed scope" case).

**SML7 — minor (lens 1, A2).** `blank_code_spans` works a line at a time, by design and
documented (docstring 141–147, test `test_a_multiline_text_is_blanked_line_by_line`). The one
row the fleet census found is exactly this: a syntax mention inside a backtick span that wraps to
the next line in a 100-column Markdown file, read today as a live unscoped marker (`""`, with the
warning) and from 2026-12-09 as nothing. The README's advice "Put the syntax in backticks to
document it" does not say that a wrapped span defeats it, and this estate's wrap discipline
makes wrapping likely. *Counsel:* one README sentence ("keep the span on one line"), or have the
census mark a row whose line holds an unmatched backtick as a probable mention.

**SML8 — note (V4).** `linkscan.FINDING_KINDS` has three kinds (`missing-file`,
`missing-anchor`, `outside-root`; `tools/linkscan.py` 508, used at 777–787); the README table
row (3077) lists two. A marker scoped `outside-root` is counted as naming a rule by the code and
as naming none by the table.

**SML9 — note (V1).** The CHANGELOG entry's cleanup line says "the review-brief skill says to
check the review worktree carries the subject (AM11)" among the changes made. The skill line
(`skills/review-brief/SKILL.md:72`, `merge-base --is-ancestor`) landed in `db2c39f9`, an
ancestor of `6d26b058`; the delta touched no file under `skills/`. True as a fact, not a change
this commit made.

**SML10 — note (non-goal, recorded not scored).** The ruled rule says "a lowering with no end
date is not a lowering this model allows". The fleet report at HEAD shows 3 children with a
floor `disabled` entry, all 3 with no `review-by`, and 6 with `scope`/`flags`; 320/800 made the
missing date a warning. So the rule as written is unmet live in 9 places with no dated path to
compliance, which the brief names a non-goal and the table at HEAD states plainly. Recorded so
the principal rules with the count in front of him.

### Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `6d26b058` (reader, scanners, tests, README, ignore headers, changelog) | yes, `coldsweep --commit` scoped to 26 paths; 6 board files left out | SML1, SML2, SML6, SML7, SML8, SML9 |
| `44f66053` (GUARDS, method README, changelog) | yes, scoped to 3 paths; 1 board file left out | SML3, SML4, SML5, SML10 |
| later on the reader: `55c7d409`, `2b8bcd92`, `a78ee8b0` | yes, same way | none of their own; they inform SML1 (the note sanitises) and SML6 (the no-reason shape) |

### Re-run ledger (all from the worktree root, `python3` 3.14.6, `nice -n 10`, one at a time)

| Line | Result |
|---|---|
| `cd tools && python3 -m unittest test_allowmarker` | exit 0, 84 OK |
| `cd tools && python3 -m unittest test_leakscan` | exit 0, 471 OK |
| `cd tools && python3 -m unittest test_pathscan` | exit 0, 172 OK |
| `cd tools && python3 -m unittest test_report` | exit 0, 110 OK |
| `cd tools && python3 -m unittest test_reviewscan` | exit 0, 70 OK |
| `python3 tools/allowmarker.py --census --root .` | exit 0, 11 rows, all `tools/` fixtures or a docstring |
| `python3 tools/floor.py --plane ci --root .` | exit 0, 20 run of 21; 3 malformed warnings and 7 unparseable notes on stderr, all on atelier's own fixtures and source |
| `python3 tools/floor.py --plane hook --root .` | exit 0, 19 of 19; no marker warning |
| `python3 -m unittest discover -s tools` | first run killed by the harness at my turn's end (no summary); re-run: exit 0, 3382 OK in 1204 s under load 10–17 |
| `floorfleet --root <parent of the main checkout> --json`, then `--census` per wired child | 24 rows: 1 parent, 22 wired children, 1 absent; malformed rows per child `[0×21, 1]`, total 1 (a wrapped documentation mention); 3 children with undated `disabled`, 2 with `advisory`, 6 with `scope`/`flags` |
| dated-clock probe (scratch clone, `_utc_today` → 2026-12-10, full discover, then floor ci) | 3382 OK; floor exit 0 with 0 malformed warnings and 11 notes. A first form that moved the constant instead was a probe artefact and is discarded (log) |
| `/security-review` | NOT RUN, discharged by grounds (lens 4) |

No check needed a live write; none is marked NOT RUN for that reason. Child repos were read
only, by the worktree's own tools, and are counted, never named.

### Follow-up checklist (all the principal's to decide, rule 3; counsel is beneath each finding)

- [ ] SML1 neutralise the two echo paths and pin them (security; recurrence prevention named)
- [ ] SML2 a run-time count of grace-honoured markers, and a census that separates mentions
- [ ] SML3 rule on the glob: check-level lowering with an end date, or acceptance at the Line row
- [ ] SML4 one statement of the lowering rule in GUARDS
- [ ] SML5 the Repo rows in the lowering table
- [ ] SML6 the README's glued-reason sentence
- [ ] SML7 the wrapped-code-span caveat
- [ ] SML8 README `linkscan` row; SML9 CHANGELOG AM11 wording; SML10 recorded for the ruling
- Reviewer's log (commands, evidence, method, the discarded probe):
  `~/.claude/fable-drain/notes/atelier-160-1190-1958.md`, to be folded in at act 2.
