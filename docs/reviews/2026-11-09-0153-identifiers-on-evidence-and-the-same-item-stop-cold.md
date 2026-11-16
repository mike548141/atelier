# Cold pass — ccclose --identifiers credits on evidence (160/960), and a peer's edits stop only a claim of the same item (010/160, 160/260)

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (doctrine by
function: a close-out instrument and a concurrency rule every session reads).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** ACT 1 WRITTEN 2026-11-16 UTC on Fable 5.1: verdict below the divider; act 2
(reconcile against the sibling and the barred records) owed next.
Written 2026-11-09 UTC by session `d16dc612`, a headless Opus 5.5 brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/1170-rule-4-cold-pass-queued-identifiers-on-evidence-and-the-same-item-stop.md`
(barred until phase 2).
**Size:** large: two unrelated subjects in one pass. One is 757 added lines of instrument code,
tests, design note and man page; the other is 169 added lines of doctrine, an ADR amendment and the
board tool's docstring.
**Why it earns a review:** `ccclose --identifiers` credits commits to a session in close-out
records, so a false credit is a false record. The claim rule decides when a session may start beside
a live peer, so a wrong narrowing lets two sessions take one item.

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
  the sibling, by count here: a held-back sibling with one pointer block, 2 questions and 1 fact.

## The acceptance test

The principal's answer on `160/960`, 2026-11-09, verbatim: *"Credit only on evidence"*. The option
read: `ccclose --identifiers` lists a commit only where the session's own transcript shows it made
it, and shows anything uncertain as uncertain. The principal's answer on `010/160`, the same day,
verbatim: *"Stop only for the same item"*. The option read: a session still works in its own
worktree and stops only where a peer's unsaved changes touch the item it wants; claiming a different
item beside a live peer is allowed. That answer also covers `160/260`'s BA1.

The offered option's words were written by the authoring session and put to the principal; the
quoted pick is his. Recorded as an answer, not a ruling in his words: where the delta's wording goes
past what he picked, say so. These are claims to test, not settled scope.

## What the work is

Two commits on `main`, on two subjects: `4e3b3984` (`ccclose`) and `2744f6aa` (the claim rule, with
the board tool's docstring and an ADR amendment). The second also touched one session record, which
stays barred, so scope to the paths below.

Commits on `main`: `4e3b3984`, `2744f6aa`. The landing commit is `2744f6aa`. **Check your tree has
it before reading anything:** `git merge-base --is-ancestor 2744f6aa HEAD` exits 0, and an
orchestrator merges `origin/main` into the review branch before it spawns.

Delta paths: `instruments/ccclose`, `instruments/ccclose.test.js`, `instruments/ccclose.design.md`,
`instruments/man/ccclose.1`, `instruments/README.md`, `docs/method/RECORD.md`,
`docs/method/CONCURRENCY.md`, `tools/board.py`, `tools/README.md`, `docs/roadmap/README.md`,
`docs/decisions/2026-08-15-0610-board-store-per-item-files.md`, `CHANGELOG.md`. Read each at HEAD
and read each commit body-free, scoped to paths so board records stay barred:

```
python3 tools/coldsweep.py --root . --commit 4e3b3984 --path CHANGELOG.md --path docs/method/RECORD.md --path instruments/README.md --path instruments/ccclose --path instruments/ccclose.design.md --path instruments/ccclose.test.js --path instruments/man/ccclose.1
python3 tools/coldsweep.py --root . --commit 2744f6aa --path CHANGELOG.md --path docs/decisions/2026-08-15-0610-board-store-per-item-files.md --path docs/method/CONCURRENCY.md --path docs/roadmap/README.md --path tools/README.md --path tools/board.py
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Commits since the delta on these paths:

```
git log --oneline 2744f6aa..HEAD -- instruments/ccclose instruments/ccclose.test.js instruments/ccclose.design.md instruments/man/ccclose.1 instruments/README.md docs/method/RECORD.md docs/method/CONCURRENCY.md tools/board.py tools/README.md docs/roadmap/README.md docs/decisions/2026-08-15-0610-board-store-per-item-files.md CHANGELOG.md
```

At `457615cc` this printed 10 commit(s). Read anything new the same way.

**Application pass.** Both subjects apply the principal's answers and earlier passes' counsel. It
cannot fully honour rule 2: the delta carries finding ids and the decisions stamped on them.
Sequence (`REVIEW.md` § *Applying decisions to doctrine*): review the work at HEAD and commit
findings first; open the prior verdict after. Name that residual exposure in the verdict.

**Claims the work makes (extracted from its own changelog entry and files, not evaluated):**

- `ccclose`'s Commits line lists a commit only where one command of the session or its subagents
  made it: subject, repo, a non-error result and the time must all fit, one command to one commit; a
  commit command quoted in a heredoc, grep or echo is no evidence.
- What does not fit prints as unconfirmed, with why. The JSON gains fields and changes no existing
  meaning.
- The limits are written into `ccclose.design.md` §15.1, the man page, the README and `RECORD.md`.
- `CONCURRENCY.md` § *Claiming at a dirty primary checkout* (CF3): a peer's uncommitted edits stop a
  claim only where they touch the item wanted; a different item beside a live peer is claimed with
  `--rebuild --from-index`, by pathspec.
- A peer's staged entries and a monolithic board are named as the cases this does not cover.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** `ccclose` behaviour outside `--identifiers`, except where the delta changed it.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself, first, and damage each
with a probe or confirm it by re-driving. Ask whether this is the right problem, solved at the right
altitude.
2. **Correctness & quality** — does the work do what its claims above say; honest about done versus
stubbed; any overclaim or silent scope cut, each recorded against the text that makes it.
3. **Completeness / harvest** — every surface that states the rule (V3), one home (V4), no
contradiction with sibling doctrine (V5), tests that would stay green on a broken check, what
already exists that this ignored.
4. **Security & privacy** — mandatory. `ccclose` parses session transcripts, which are untrusted
text with a path to a record; weigh that parse. Aim `/security-review` at the `instruments/ccclose`
diff from a clean tree, or discharge it by grounds.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-09 UTC, from the worktree root
at `457615cc`; results are in the sibling. Read exit codes explicitly. Check `uptime` first and run
heavy lines under `nice -n 10`. Python is the `python3` on `PATH` (the tests need 3.10 or later;
`/usr/bin/python3` is 3.9 on this machine and some modules fail at import).

- `node --test instruments/ccclose.test.js`
- `cd tools && python3 -m unittest test_board`
- `nice -n 10 python3 tools/floor.py --plane ci --root .`
- `nice -n 10 python3 tools/floor.py --plane hook --root .`

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
- `ccclose` reads session transcripts: quote none, and report only counts of credited or unconfirmed
  commits from any real session you point it at.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the
deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the
reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, this brief's sibling
(`2026-11-09-0153-identifiers-on-evidence-and-the-same-item-stop-cold.deferred.md`), every delta
commit's message body, the queue pointer
`docs/roadmap/160-doctrine-review-owed/1170-rule-4-cold-pass-queued-identifiers-on-evidence-and-the-same-item-stop.md`,
and the intent records beyond their titles:

- `docs/roadmap/160-doctrine-review-owed/960-rule-4-cold-pass-queued-identifiers-credit-on-evidence.md`
- `docs/roadmap/010-board-store-migration-per-item-files-mik/160-cf3-s-sibling-stop-is-now-stricter-than-its-cause.md`
- `docs/roadmap/160-doctrine-review-owed/260-rule-4-cold-pass-queued-bs1-wording.md`

Prior verdicts on this subject, barred until your own findings are committed (rule 2; `coldsweep`
excludes `docs/reviews/` by default):
`docs/reviews/2026-10-26-0917-identifiers-credit-on-evidence-cold.md`,
`docs/reviews/2026-09-25-0715-bw-rulings-applied-cold.md`. The delta's docstrings, comments, ADR
text, `tools/README.md` and `CHANGELOG.md` entries carry the author's account of why; they are the
delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1170-rule-4-cold-pass-queued-identifiers-on-evidence-and-the-same-item-stop.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/960-rule-4-cold-pass-queued-identifiers-credit-on-evidence.md \
  --also-exclude docs/roadmap/010-board-store-migration-per-item-files-mik/160-cf3-s-sibling-stop-is-now-stricter-than-its-cause.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/260-rule-4-cold-pass-queued-bs1-wording.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, any orchestrator, what you read, the UTC day you ran on),
per-lens answers, V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (`4e3b3984` and `2744f6aa`: read body-free
yes/no, findings by id), findings with stable ids (prefix `IDS`: `IDS1`, `IDS2`, …) and severities
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

## Verdict — act 1, 2026-11-16 UTC

### Provenance (rule 4, V7)

- **Tier:** Fable 5.1, the principal-named review tier, checked at selection by the spawner and
  stated here. The reviewer that read the delta, answered the lenses, assigned every severity and
  wrote this text is this Fable session; nothing below was formed by any other hand.
- **Spawn:** a headless orchestrator session (Opus 5.5) spawned this reviewer; that orchestrator was
  started by drain session `1e053526` (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold
  the context partition, form no finding and write no severity. Neither wrote the brief or the
  delta. The reviewer was not started or instructed by any barred session (`722ac2e2` and its
  workers, `d16dc612`, `74f2b8cd`). No contact with the author or the brief-writer occurred.
- **The spawn prompt, in substance (process direction only):** the worktree path; the brief path and
  "read it in full first and follow it exactly"; the finding prefix `IDS`; that the sibling
  `.deferred.md` was removed from the worktree on purpose and is not to be sought in git history or
  any other location until released by message after act 1 is committed; the rule-2 barred list;
  a user-local review log to keep; what may be written (this file and the log only; no commit, no
  push); live reads allowed, no live writes, counts only from any real transcript; load limits;
  the scanners to run over this file; the act-1 ending words. It carried the principal's drain
  order of 2026-11-16, verbatim: *"I want to use things other than my weekly budget to clear as
  many fable reviews as possible like using fable drain. I thought we could start by using up all
  the API credits I have."* and *"As always you must ensure that nothing harms the integrity or
  quality of the review process and verdicts, for example if the review is done by API it must be
  as good as running it locally"*. It contained no question about the delta, no pointer to where
  the risk lives and no request about any finding. The release message has not yet arrived.
- **Lane:** the Agent SDK on the Platform API, under that order. No claude.ai connector was
  available, and none was needed.
- **Worktree:** `/Users/mike/worktrees/fable/atelier-160-1170-0709/atelier`, HEAD `4956e3e2`;
  `git merge-base --is-ancestor 2744f6aa HEAD` exits 0 (re-checked). The only dirty path at open
  was the sibling's deletion (the partition). Read-only to this session except this file.
- **Exposure, disclosed:** this brief whole; `docs/method/REVIEW.md` whole; the repo and user
  instruction files and a memory index the harness loads at start (private context this verdict
  does not carry; none of it concerns this delta); coldsweep banners naming barred files it left
  out; index titles of board items in sweep output (titles are not barred); `CHANGELOG.md` entries
  back to the 2026-08 board work, met while reading the delta's own entries and sweeping. Two
  board files the landing commit touched but the brief's path list omitted were read body-free with
  `--path` and are disclosed under IDS4. The session log was not opened (reviewer's start-up
  reading skips it). No prior verdict, intent record body, session record, commit body or the
  sibling was opened. Real transcripts of this repo were touched three ways, counts only: a field
  census over the six newest main and six newest subagent transcripts (two of the six are the
  author's and the brief-writer's sessions; no content read), `ccclose --identifiers --json` on
  three sessions including the author's (`722ac2e2`), and a count of commit-command idioms and
  heredoc sizes. No line of any transcript was read as text.
- **Residual exposure named by the brief:** the delta carries the prior pass's finding ids (IE1 to
  IE14) and decision stamps in its changelog, comments and design note; they were read as the delta.
  The prior verdicts stay unopened until act 2.
- **UTC day run:** 2026-11-16, 07:11 to 07:45 UTC.

### Method (the 2026-11-15 ruling)

Order: brief whole → `REVIEW.md` whole → load, tree, tier → both commits body-free via
`coldsweep --commit --path` (the brief's two lines, exit 0 each) → since-delta commits per path (62
in all; the three on `ccclose` read body-free, scoped; `git diff 4e3b3984..HEAD --
instruments/ccclose` has no hunk inside the identifiers block, so the delta's code is
HEAD's) → the doctrine at HEAD
(`CONCURRENCY.md` § The trigger, § Integration hygiene, § Claiming work, § Selecting the next item;
`board.py` docstring 1 to 129; `RECORD.md` 92 to 121) → the four re-run lines → V3 sweeps with
`coldsweep` (the brief's exclusions, by script) → probes on scratch copies and synthetic fixtures
(none in the worktree): a CF3 probe with the worktree's `board.py` by path, regex timing, subject
extraction, variable-path resolution, a transcript field census, live `ccclose` runs, an idiom
count. Left out, and why: the 29 since-delta commits on `tools/README.md` and the five on
`RECORD.md` were not read one by one; the surfaces were read at HEAD and swept for the delta's
rule, which is what the pass judges. `ccclose` behaviour outside `--identifiers` is the brief's
non-goal. The full step-by-step record with every command and result is the review log at
`~/.claude/fable-drain/notes/atelier-160-1170-0709.md` (user-local; counts only, no transcript
text).

### The acceptance test, answered

- *"Credit only on evidence"*: met in direction. On three real sessions no commit is credited
  without a fitting command, and the two delta commits print as unconfirmed for the author's
  session (a worker made them: the stated IE8 limit). What the pick did not foresee is how often
  the session's own commits now print as uncertain: 36 of 44 and 63 of 105 unconfirmed commits on
  two real sessions carry the "matches a command that does not fit" note, and one measured cause is
  the house's own `W=…; git -C "$W"` idiom, which the binding never resolves (IDS2). Honest, but the
  label loses force when it covers most of a session's work.
- *"Stop only for the same item"*: met for the worktree and the item file. The delta adds one
  stop on a different item the pick did not cover: a peer's staged line (branch 3) makes the
  claimer wait. It is forced by the shared index and the hook, not chosen, and the delta discloses
  it as a case not covered; it still goes past the answer's words, so it is put to him (IDS6).

### Lens 1 — approach and assumptions (named first, then damaged or confirmed)

- **A1. Every tool-use record carries `cwd` and a `timestamp`, and every tool-result record a
  `timestamp`.** Confirmed on real data: 6 main + 6 subagent transcripts, 100% on each field (e.g.
  672/672 assistant records with both; 357/357 results with a timestamp).
- **A2. A commit's committer second falls inside the span from the tool-use record to its result.**
  Confirmed by construction (the command runs between the two records) and by the fixture tests
  (`ran()` places the records 500 ms either side); the one-second slack covers clock granularity.
- **A3. The run directory can be resolved from the record's `cwd`, a preceding `cd` and each `-C`.**
  Damaged: `runDir` calls `resolvePath(w, d, new Map(), null)`, an empty variable map, so any
  variable in a `cd` or `-C` word yields `null` and the command is read as another repo's. Probe:
  `W=/r/wt\ngit -C "$W" commit -q -m "a: b"` → dir `null`; same for `cd "$W" &&` and `${W}`;
  literal paths resolve. The sibling `-F` path logic in the same file expands literal assignments
  (`assignmentsIn`, `expandVars`). → IDS2.
- **A4. Only a `git` word in command position counts, so quoted commit commands are no evidence.**
  Half-confirmed: the forms the tests cover (quote opens directly before `git`) are excluded; a
  `;`, `&&`, `|` or `(` inside the quoted text re-opens command position and the subject comes out
  garbled. → IDS3.
- **A5. The parse is cheap on any command a session emits.** Damaged: blanking heredoc bodies to
  spaces and then anchoring with `[\n;&|(]\s*` is quadratic in the blanked region. → IDS1.
- **A6. `--rebuild --from-index` cannot absorb a sibling's unstaged line; a peer's staged line is
  refused at the hook on a pathspec commit.** Confirmed by scratch probe with the worktree's
  `board.py`: unstaged peer line left out (D, exit 0, peer's file still ` M`); staged peer line,
  pathspec commit refused (A, exit 1); whole-index commit absorbs it (B, exit 0, three files).
- **A7. A dirty sibling is no reason to refuse a different item.** Confirmed as reasoning: the
  mechanical base is closed by A6, and the evidentiary base is the flipped prior restated; the text
  says so and admits the old stop's firing rate was never measured.
- **Right problem, right altitude?** Binding the credit to the command is the right read-side fix.
  The write-side alternative, a session-id trailer on every commit, is named in the design note's
  §11 as the thing the read "can do without" and is never weighed in §15.1's options; it would reach
  the two largest under-credit causes measured here (worker sessions, removed worktrees). → IDS9.

### Lens 2 — correctness and quality

Claims re-driven: the four-way binding (tests IE1 to IE3, re-run green; live runs consistent);
one command, one commit (test green); failed command counts for nothing (IE2 green); heredoc, grep,
echo quoting (IE4 green for the covered forms; IDS3 for the rest); JSON gains fields and changes no
meaning (field list test green; `via` is not in the JSON, by prior design); CF3's three branches
(probe A, B, D). Overclaims found: the run-directory claim (IDS2), the quoted-command claim (IDS3),
the changelog's account of the 010/030 edit (IDS4), BA4's "one spelling" (IDS8). Honest about done
versus stubbed: the design's under-credit list is long and candid; two forms are missing from it
(the variable path, IDS2; the quoted-text `;`, IDS3).

### Lens 3 — completeness and harvest

- V3 sweeps found no skill, template or child-facing surface stating the old sibling stop; the rule
  lives in CF3 with pointers from § On a split board, `tools/README.md`, `docs/roadmap/README.md`,
  the ADR and the docstring. The `ccclose` rule is mirrored in `RECORD.md`, `instruments/README.md`,
  the man page and the design note, and they agree, with one trivial gap: the man page says the
  command's directory must resolve "into this repo or one of its worktrees" while the code also
  accepts any directory sharing the git common dir.
- Tests that would stay green on a broken check: none found for the four-way binding. Two gaps:
  no test drives a large heredoc (IDS1 is invisible to the suite), and the `git -C "$D"` → `null`
  unit assertion pins IDS2's behaviour as intended rather than catching it.
- What already exists that this ignored: `assignmentsIn`/`expandVars` for the run directory
  (IDS2); the trailer the harness already stamps on every commit (IDS9).

### Lens 4 — security and privacy

- `ccclose` parses untrusted command text with regexes. Threats weighed: resource exhaustion
  (IDS1, measured: 47 s on one 1 MB command, 156 s on 2 MB; the old regex took 2 ms); false credit
  by crafted text (needs a same-subject commit in the same repo in the same second as the crafted
  command's span: negligible); code execution (none: the parse runs no command; `repoScope` runs
  `git rev-parse` read-only, with `--no-optional-locks`, in a directory only if it exists); leakage
  (the block prints subjects, short SHAs, PR numbers and fixed-text notes; directories and command
  text are never printed; the JSON adds no new personal data).
- `/security-review`: discharged by grounds. It reads the session's pending diff, and this
  worktree's pending diff is the deleted sibling, whose content a diff would print into the
  reviewer pre-draft (the SL2 trap). A scratch clone (`git clone`, then `git archive`) was refused
  by the permission layer, so the diff could not be reproduced where the scanner could be aimed.
  The lens above is the hand pass that stands in for it.

### The standing checklist

- **V1** — four claims stronger than their evidence: IDS2, IDS3, IDS4, IDS8.
- **V2** — all four re-run lines green (ledger below); CF3's mechanical claims re-driven (probe);
  the design's quoting and directory claims re-driven (IDS2, IDS3).
- **V3** — swept; mirrors agree (lens 3). No stale "subject appears in" text remains anywhere.
- **V4** — one home: CF3 for the stop, `board.py`'s docstring for the mechanism, `ccclose.design.md`
  §15.1 for the binding; the other surfaces carry clauses and pointers. Held, with IDS8's spelling
  wobble inside the canonical docstring.
- **V5** — cross-references checked for the rule reached: § The trigger holds the `git diff
  --cached` and pathspec rules CF3 cites; § Integration hygiene's *After the stop* holds the
  `fetch`/`ff-only` sync CF3's push-rejected bullet cites; `030/140` is open as named. One
  contradiction in letter: IDS5. One record disagreement: IDS4.
- **V6** — lens 4 above; the scanner discharged with grounds.
- **V7** — provenance in the brief and repeated above.

### Findings (prefix IDS; all the principal's to decide, rule 3; counsel labelled beneath)

**IDS1 — MODERATE — the command-position parse is quadratic over blanked heredoc bodies, a
regression.** `codeOf` blanks a heredoc body to spaces, keeping offsets, and `GIT_CMD` anchors with
`(?:^|[\n;&|(]\s*…)`: from every newline `\s*` runs across every blanked line before failing, so
cost grows as lines × bytes. Measured on the worktree's copy, one command holding a terminated
heredoc then a commit: 1,000 lines 141 ms; 5,000 lines 3.1 s; 10,000 lines 11.9 s; 20,000 lines
(1.08 MB) 46.6 s; 40,000 lines 156 s. The pre-delta `GIT_MSG` regex reads the same 20,000-line
text in 1.9 ms; the same new regex with `[ \t]*` in place of `\s*` reads it in 6.4 ms. `cdBefore`'s
regex has the same shape and runs once per git command. Real exposure today is nil: the largest
heredoc in three real sessions is 141 lines and the live runs took 3 to 4 s. Latent: one large
file written by heredoc, a thing sessions do, makes the close-out checker hang for a minute.
*Counsel:* `[ \t]*` after the separator in `GIT_CMD` and in `cdBefore`'s regex; add a test with a
5,000-line heredoc under a time bound.

**IDS2 — MODERATE — the run directory never resolves a shell variable, so the house's own
`W=…; git -C "$W" commit` idiom prints its commits as unconfirmed, and the four surfaces do not say
so.** `runDir` passes an empty variable map to `resolvePath`; a `cd "$W"` or `-C "$W"` yields
`null` even when the same command assigned `W` a literal, and the command is read as another
repo's. The `-F` path logic beside it does resolve literal assignments. On real sessions, 17 of 49
and 12 of 69 commit commands use the variable form, and 36 of 44 and 63 of 105 unconfirmed commits
carry the "does not fit" note (the other cause is the stated one: worktrees an orchestrator made
and since removed). The man page, README, design note and `RECORD.md` say the record's cwd, a
preceding `cd` and each `-C` "resolve into the repo" and list no variable limit; the unit test pins
`git -C "$D"` → `null` as intended. Direction is honest (under-credit), so not a false record; but
a block that marks most of a session's own commits uncertain will be pasted over.
*Counsel:* resolve `cd`/`-C` words through `assignmentsIn`/`expandVars` as `-F` paths are (a
literal in the same command, or an earlier `export`); until then, name the limit on all four
surfaces and in the "does not fit" note's wording.

**IDS3 — minor — "a commit command quoted in a heredoc body, a grep pattern, an echo or an `sh -c`
string runs nothing and is no evidence" is true only where the quote opens directly before `git`.**
No quote tracking exists: `sh -c "cd x; git commit -m …"`, `grep "x; git commit -m …"` and
`echo $(git commit …)` all put `git` in command position, and the subjects come out garbled
(`"a:`, `a: g)`). False credit needs that garbled subject to equal a real commit's in the same repo
and second, which is negligible; the real effect is under-credit of a genuine `$(git commit …)`.
The design note, man page and README state the stronger claim. *Counsel:* state the limit as the
tests cover it, or stop at an unbalanced quote before the `git` word.

**IDS4 — minor — the changelog and the ADR disagree about which records the landing commit
corrected, and the changelog misdescribes one edit.** The changelog says "the ADR, `010/020` and
`010/030` are corrected to say the stop had lived in an interim sentence"; the ADR says "this ADR,
`010/020` and `010/160`" were wrong about where the stop lived. The commit's board edits (read
body-free with `--path`, disclosed): `010/020` gained exactly that correction; `010/030` gained a
"Superseded 2026-09-20" note about the two slips now caught at the hook, nothing about where the
stop lived; `010/160` was not touched by this commit. *Act-2 check owed:* whether `010/160` was
corrected in its close. *Counsel:* make the changelog name the edits made, and the ADR name the
records corrected.

**IDS5 — minor — CF3's branch 2 now sanctions rewriting a stranger's dirty generated index, and the
general prohibition it sits under carries no carve-out.** § The trigger's dirty-tree backstop says
"never work around a stranger's in-flight edits and never absorb them into a commit", and the child
template stamps "never work around or absorb them" into every child, while CF3 says "if the
stranger had rebuilt it on disk their copy is rewritten … they rebuild again". The old rule's
sanctioned touch staged only the claimer's hunks and rewrote no dirty file; the new one overwrites
one. It is safe (the index is derived, the hook catches a stale re-stage, probe D) and the carve-out
is argued in CF3, but a reader of the backstop or the template meets a flat prohibition. The
trigger's first bullet already points claim-first at § Claiming work; the backstop bullet does not.
*Counsel:* one clause at the backstop bullet and the template ("the claim's one touch excepted,
§ Claiming work").

**IDS6 — note — branch 3 is a stop on a different item, past the answer's words.** "Stop only for
the same item" read as "claiming a different item beside a live peer is allowed"; a peer's staged
line on another item now makes the claimer wait, because the shared index bakes that line and the
hook refuses the pathspec commit (probe A). The delta discloses it as a case not covered. It is a
mechanical consequence, not a choice, and the alternative (commit the whole index) absorbs the
peer's work (probe B). *Counsel:* put it to the principal as the one residual stop, with the two
probe outcomes, so his answer covers it.

**IDS7 — note — branch 2's order of operations is implicit.** Rebuilding `--from-index` before
staging one's own item regenerates an index without the claim, and the hook then refuses (probe C,
self-correcting on the next rebuild). The text says "stage your item's file and the index,
regenerated with …" and leaves the order to inference. *Counsel:* "stage the item, then rebuild
`--from-index`, then stage the index".

**IDS8 — note — BA4's "`--rebuild` is the one spelling" is true of the prose surfaces outside
`board.py` only.** The docstring the delta names canonical keeps `rebuild --from-index` at three
places (lines 46, 106, 114) beside its own `--rebuild` at line 36, and the hook's printed remedy is
`board.py rebuild --from-index`, kept bare on purpose (lines 718 to 726: the committed preamble
must not drift). Both spellings run (probed, exit 0 each). *Counsel:* either sweep the docstring's
prose or narrow the claim.

**IDS9 — note — the write-side alternative was not weighed.** A session-id trailer on every commit
(the harness already stamps a trailer) would make attribution exact, reach worker sessions'
commits (the IE8 limit) and commits from removed worktrees, the two largest under-credit sources
measured on real sessions, at the cost of one line per commit. The design note names it only as
what the read "can do without" (§11). *Counsel:* weigh it in §15.1 as an option, taken or declined
with grounds.

### Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `4e3b3984` (`ccclose`) | yes: `coldsweep --commit`, 7 paths | IDS1, IDS2, IDS3, IDS9 |
| `2744f6aa` (claim rule) | yes: `coldsweep --commit`, 6 paths + 2 board files | IDS4 to IDS8 |

### Overall

**PASS-WITH-FINDINGS: 0 MAJOR, 2 MODERATE, 3 minor, 4 note.** No false credit was found and the
claim rule holds mechanically; the two MODERATE findings are a latent cost regression and an
undocumented under-credit that together make the block less useful than its surfaces say.

### Re-run ledger

| Line (worktree root; `python3` 3.14.6; node 24.18.0) | Result |
|---|---|
| `nice -n 10 node --test instruments/ccclose.test.js` | exit 0; 111 pass, 0 fail; 119.7 s |
| `cd tools && nice -n 10 python3 -m unittest test_board` | exit 0; Ran 108 tests, OK |
| `nice -n 10 python3 tools/floor.py --plane ci --root .` | exit 0; no ✗; one unrelated advisory |
| `nice -n 10 python3 tools/floor.py --plane hook --root .` | exit 0; no ✗ |

Children: none touched (0 read, 0 named). Load at open: 2.84; one suite at a time, foreground.
Scratch probes (all under the review log's scratch folder, deleted at the end): `cf3probe.sh`,
`redos.js`, `heredoc.js`, `fields.py`, `idiom.py`, `live.sh`; the worktree's `tools/` and
`instruments/` were run by path and never changed.

### Follow-up checklist

- [ ] IDS1: narrow `\s*` to `[ \t]*` in `GIT_CMD` and `cdBefore`; add a timed large-heredoc test.
- [ ] IDS2: resolve variables in `cd`/`-C` words, or name the limit on the four surfaces and in
      the note text.
- [ ] IDS3: state the quoting limit as tested, or track an open quote before `git`.
- [ ] IDS4: align the changelog and ADR on which records were corrected; check `010/160` (act 2).
- [ ] IDS5: a carve-out clause at the backstop bullet and the child template.
- [ ] IDS6: put branch 3 to the principal as the residual stop on a different item.
- [ ] IDS7: state the order in branch 2.
- [ ] IDS8: sweep the docstring prose or narrow BA4's claim.
- [ ] IDS9: weigh the session-id trailer in §15.1.
- [ ] Act 2: open the sibling, the prior verdicts, the intent records and the commit bodies;
      append `### Reconcile`.
