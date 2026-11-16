# Cold pass — ccclose --identifiers credits on evidence (160/960), and a peer's edits stop only a claim of the same item (010/160, 160/260)

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (doctrine by
function: a close-out instrument and a concurrency rule every session reads).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** PASS RAN 2026-11-16 UTC on Fable 5.1: act 1 verdict (committed `004a9bec`) and
act 2 reconcile below the divider; the held-back sibling is folded below the reconcile.
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

### Reconcile — act 2, 2026-11-16 UTC, after act 1 was committed (`004a9bec`)

Opened after the orchestrator's release message, which named the held file's path and the
records to read, and nothing about the delta: the sibling (27 lines: the pointer's two questions,
the brief-writer's two, one held-back fact, the re-run results at `457615cc`); the queue pointer
`160/1170`; the intent records `160/960`, `010/160`, `160/260` whole; the prior verdicts
`2026-10-26-0917` (IE1 to IE14, their reconcile) and `2026-09-25-0715` (BA1 to BA8, their
reconcile); the bodies of `4e3b3984` and `2744f6aa`; the 2026-09-20 session record's late closing
note (`2744f6aa`'s one record edit); `010/020` at HEAD; the 2026-10-18 session-log entry that
landed the first identifiers block. No act-1 text above is revised.

**The pointer's questions.** *Can a commit be credited on evidence the session did not produce?*
Not in any case probed or found: every credit needs a non-error command of the session or a
subagent, in this repo, in the commit's second. The residuals are IDS3 (a garbled subject from
quoted text) and the rewrite tier (a copy made inside a rebase span), each needing a peer's
same-subject commit in the same repo and second. *Can two sessions still both claim one item?*
No: the item's own dirty file stops the claim (branch 1), and a same-item claim that has already
landed collides on the state line at push (the unchanged push-rejected bullet). The brief-writer's
second question (a peer's claim landed by another worktree between the read and the claim) is
that bullet's case; the delta did not change it and this pass did not re-drive it, since the
mechanism is git's rebase conflict and the doctrine's own bearing. The first (a peer's same-subject
commits inside the window) is answered by IE1/IE11's tests and A2 to A4: credited only on the same
second, same repo and a non-error command; otherwise unconfirmed with the "does not fit" note. The
held-back fact (the two subjects share only the session that made them) matches what act 1 found.
Re-run drift since `457615cc`: 105 → 111 node tests, 87 → 108 board tests, and the CI plane's 28
`secretscan` advisories are gone, replaced by one unrelated declarations advisory.

**Per finding, against the prior verdicts and the author's account.**

- **IDS1** — not anticipated. The prior verdict's one cost line concerns `fileSubjects`; the
  author's body reports seventeen tests that fail on the old code and pass now, none timed. The
  regression is the delta's own. Stands, MODERATE.
- **IDS2** — IE3's counsel was "its `-C` or cwd resolving under `repo.root`" and IE10 named
  `git -C "/path with space"`; neither named a shell variable, and the author's body says "repo
  (cwd, cd, -C into this repo or its worktrees)" without the limit. The unit assertion `git -C
  "$D"` → `null` shows a choice, recorded nowhere a reader meets. Stands, MODERATE.
- **IDS3** — IE4's counsel was to skip "heredoc bodies and quoted strings that are not the `-m`
  argument"; the author implemented command position only and the surfaces claim the counsel's
  full scope. Stands, minor.
- **IDS4** — settled from the records. The author's body puts the `010/030` edit under BA5 ("the
  2026-09-20 closure logged and 010/030's gate note superseded"), so the changelog folded a BA5
  edit under BA1's sentence. `010/160`'s body still says CF3 stopped a sibling claim (its "What
  changed underneath the rule" section) and was not corrected; its close note settles the rule,
  not the misdescription. The ADR's sentence is accurate as a statement about a record left
  uncorrected; the changelog's is not. Stands, minor.
- **IDS5** — the author's body says "the stamped child block never carried the claiming rule, so
  no stamped copy changes", which is true of the claim rule and silent on the backstop sentence
  the child template does carry. BA1's counsel (one operative sentence in CF3) was followed.
  Stands, minor.
- **IDS6** — the author recorded the exception in `010/160`'s close note ("a peer's staged entries
  and a monolithic board stay named exceptions"), after the answer was given on an option that
  read "claiming a different item beside a live peer is allowed". The principal answered without
  the exception in front of him. Stands, note; the ask is unchanged.
- **IDS7** — not anticipated by either prior pass. Stands, note.
- **IDS8** — BA4 was a spelling-drift finding on `tools/README.md` and § On a split board; the
  author's "one spelling, `--rebuild` (BA4)" applied it to those and left the docstring's own
  prose. Stands, note.
- **IDS9** — IE8 offered two routes (read the worker transcripts the parent launched, or document
  the limit); the author took the documented route, as `160/960`'s close records. A trailer was in
  neither the counsel nor the options. Stands, note.

No finding is formed at reconcile. Nothing is applied: every finding is the principal's (rule 3).

**Overall, restated: PASS-WITH-FINDINGS: 0 MAJOR, 2 MODERATE, 3 minor, 4 note.**

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-16)

The text below is the brief's held-back sibling,
`2026-11-09-0153-identifiers-on-evidence-and-the-same-item-stop-cold.deferred.md`, copied
verbatim. It was removed from the review worktree before the reviewer started, held outside the
tree until act 1 was committed (`004a9bec`), then released to the reviewer for act 2. The
orchestrator forms no finding and has not edited it; the sibling file itself is deleted in the
fold commit, so the brief's mentions of it by name now point here.

# Deferred reading for `2026-11-09-0153-identifiers-on-evidence-and-the-same-item-stop-cold.md`

Open only after your act-1 findings are committed (`docs/method/REVIEW.md` rule 1). Fold into the
brief below the reconcile, then delete this file. A floor, never a fence.

## The queue pointer's questions (the author's framing, verbatim)

> whether a commit can be credited on evidence the session did not produce; whether two sessions can
still both claim one item under the narrower stop.

## The brief-writer's questions

1. Under a concurrent peer making same-subject commits within the time window, what does the matcher
credit?
2. A peer's claim commit landed by another worktree between this session's read and its claim: what
stops the double claim now?

## What the brief-writer held back

- The two subjects were queued together by the author and share only the session that made them.

## Re-run results (2026-11-09 UTC, at `457615cc`)

`ccclose.test.js`: 105 tests, 105 pass, exit 0. `test_board`: 87 tests, OK, exit 0. `floor.py
--plane ci`: exit 0, with 28 `secretscan` advisories reported and not blocking. `--plane hook`: exit
0.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

Orchestrator's form fix at the fold: two probe-script lines that set a synthetic git identity
carry a trailing `leakscan:allow:email` marker so the public-repo gate passes; no text was
changed.

# Review log — atelier 160/1170 (prefix IDS), cold pass on Fable 5.1

Worktree: /Users/mike/worktrees/fable/atelier-160-1170-0709/atelier
Brief: docs/reviews/2026-11-09-0153-identifiers-on-evidence-and-the-same-item-stop-cold.md
Reviewer tier: Fable 5.1. Orchestrators: headless Opus 5.5 (spawner) under drain session 1e053526.
Lane: Agent SDK on the Platform API (principal's API-credit drain order, 2026-11-16).

## Act 1

### Step 1 — brief read in full
- Read the brief, lines 1-226 (Read tool). Scope: two commits 4e3b3984 (ccclose --identifiers) and
  2744f6aa (CONCURRENCY.md claim rule, board.py docstring, ADR amendment). Lenses 1-4, V1-V7,
  re-run list of 4 lines, finding prefix IDS. Sibling .deferred.md barred until act 1 committed.

### Step 2 — floor of the pass: tree, tier, load, provenance
- `uptime` 07:11 UTC: load 2.84 / 3.02 / 4.68. Fine to run suites under nice.
- `git merge-base --is-ancestor 2744f6aa HEAD` → exit 0. HEAD = 4956e3e2. Tree: only the sibling
  .deferred.md shows as deleted (the partition); nothing else dirty.
- `date -u` → 2026-11-16 07:11 UTC. PATH python3 = 3.14.6; /usr/bin/python3 = 3.9.6; node v24.18.0.
- Read docs/method/REVIEW.md whole (lines 1-709) for verdict shape, rules 1-4, V1-V7, the
  2026-11-15 method-record ruling.

### Step 3 — body-free delta reads (coldsweep --commit, per the brief's two lines)
- coldsweep --commit 4e3b3984 --path ×7 → exit 0; 7 files, 757+/163-. Output 87.5 KB, persisted
  by the harness; read from that file. No board-store file in the path list.
- coldsweep --commit 2744f6aa --path ×6 → exit 0; 6 files, 133+/76-. coldsweep reported: 2 board
  files left out by default (010/020, 010/030 items), 1 board file SHOWN because --path covered it
  (docs/roadmap/README.md — the delta, disclosed), 1 rule-2 barred file left out
  (docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md). Neither message body printed.
- `git log --oneline 2744f6aa..HEAD -- <12 paths>` → 62 commits (brief said 10 at 457615cc).
  Next: per-file breakdown so I read only what touched in-scope files.

### Step 4 — delta read in full (both commits, body-free)
- 4e3b3984 diff read whole from the persisted coldsweep output (1430 lines): CHANGELOG entry,
  RECORD.md Commits bullet, instruments/README.md identifiers paragraph, instruments/ccclose
  (+403/-: gitCommands/GIT_CMD command-position regex, codeOf heredoc blanking, commitCommandsIn,
  runDir/cdBefore/cDirs, CmdLog/noteCommand/noteCommandResult, fileSubjects keyed by cmd:offset,
  repoScope, attributeCommits with fitsSpan/SPAN_SLACK, rewrites tier, squash-titled-like-own
  note, boardChanges claimedMoved/viaSquash, render lines, ID_HEURISTIC), ccclose.design.md
  (§ Commits/Board bullets, §15.1 options, IE8/IE13/IE10 paragraphs, JSON field note),
  ccclose.test.js (+331: CT map, ran/ranFor/commitCmd timed fixtures, IE1-IE10 tests, rewrite
  test, cut-record test, commitCommandsIn unit test), man/ccclose.1 (Commits/Board paragraphs).
- 2744f6aa diff read whole: CHANGELOG entry; ADR 2026-08-15-0610 "Amended 2026-11-09" section;
  CONCURRENCY.md § On a split board rewrite and § Claiming at a dirty primary checkout rewrite
  (three-branch list + parenthetical history); docs/roadmap/README.md (--rebuild spelling,
  pointer to board.py docstring); tools/README.md board paragraph; tools/board.py docstring
  (--rebuild spelling, STAGED vs UNSTAGED, LIVE RESIDUALS (1) (2)).
- Per-file commits since delta: ccclose 3 (1bc89816, 6890e9db, 50547442); test.js 2; design.md
  2; man 2; instruments/README.md 6; RECORD.md 5; CONCURRENCY.md 7; board.py 2; tools/README.md
  29; roadmap/README.md 0; ADR 0; CHANGELOG many. Decision: read the 3 ccclose commits
  body-free scoped to the ccclose paths; read CONCURRENCY.md, RECORD.md, board.py, README
  sections AT HEAD rather than every intermediate commit (the subject is the rule as it stands).

### Step 5 — post-delta ccclose commits, section map, re-run line 1
- Post-delta ccclose commits read body-free (coldsweep --commit, scoped): 1bc89816 (check 12 agent
  states; hunks at 1287-1368, renderIdentifiers agents line 1909, exports), 50547442 (judgeAgent
  failed state; hunks 1341-1397, 1938), 6890e9db (exports only). `git diff 4e3b3984..HEAD --
  instruments/ccclose` hunks: 1287, 1306, 1315, 1324, 1335, 1342, 1368, 1909, 2069: none in the
  identifiers commit block (lines 1593-1765 at HEAD). So the delta's identifiers code IS HEAD's.
- CONCURRENCY.md section map grepped; read § The trigger (29-150), § Claiming work (374-563),
  § Integration hygiene 252-301 (After the stop, 160/520 SY1), § Selecting the next item
  (1153-1202).
- RE-RUN 1: `nice -n 10 node --test instruments/ccclose.test.js` → exit 0, 111 tests, 111 pass,
  0 fail, 119.7 s. Output in scratch rerun-node.txt.
- RE-RUN 2: `cd tools && nice -n 10 python3 -m unittest test_board` → exit 0, Ran 108 tests, OK.
- RE-RUN 3: `nice -n 10 python3 tools/floor.py --plane ci --root W` → exit 0, 162 lines, no ✗;
  advisory "declarations: 21 checks, 0 meet all five" (unrelated to the delta).
- Real transcript field counts (fields.py, counts only, no content read): 6 newest main
  transcripts of this repo's project folder and 6 newest subagent transcripts: every assistant
  record has cwd and timestamp (e.g. 672/672, 457/457); every tool_result user record has a
  timestamp (357/357). The binding's reliance on o.cwd and record timestamps holds on real data.
  (Two of the six main transcripts are the author's and the brief-writer's sessions; counted
  fields only, read no content.)

### Step 6 — V3 sweeps (coldsweep via sweep.sh, excludes the 4 intent records + rule-2 set)
- 'queue-active': 3 hits (ADR:177, CONCURRENCY 450, 477). 'dirty sibling': CHANGELOG 2467 (old
  entry, record), ADR 176/192, CONCURRENCY 476. 'sibling.{0,40}dirty': ADR 129/158, board.py
  99/147/819, floor.py 846, test_board 968, ROADMAP index line. 'from-index': 30 hits, all the
  delta's surfaces + board.py/test_board. 'next open item': CONCURRENCY 290 (After the stop, SY1),
  451, 509; session-open prompt 60 and template-history 59 (the live-claim rule, not CF3).
  'stricter than its cause': CHANGELOG 887 + index line only (old paragraph gone). 'CF3': 28 hits;
  no skill, template or child-facing surface states the old stop.
- 'unconfirmed'/'identifiers block'/'credits a commit'/'ccclose': mirrors are RECORD.md 102-113,
  instruments/README.md 411-421, CONCURRENCY 1252 (pointer). No stale "subject appears in" text
  anywhere (1 hit = this brief).

### Step 7 — probes
- cf3probe.sh (scratch repos, worktree's board.py by path, hook = `--check --staged`):
  A: peer STAGED X; I stage Y, `--rebuild --from-index`, stage index, pathspec commit → hook
     refused, exit 1 (CF3 branch 3's claim re-driven: TRUE).
  B: same state, whole-index commit → hook passed, exit 0, commit carried X (the hazard the
     pathspec rule exists for: TRUE).
  C: peer UNSTAGED X; rebuild --from-index BEFORE staging own Y → "already current" (0 claims),
     then pathspec commit refused (stale index) → self-corrects on rerun; order is implicit in
     CF3's branch 2 wording.
  D: correct order (stage Y, rebuild --from-index, stage index, pathspec) → exit 0; peer's X stays
     ` M` unstaged; index does not carry X (branch 2's claim re-driven: TRUE).
  Observed: the hook's printed remedy spells `board.py rebuild --from-index` (bare `rebuild`),
  while the delta swept docs to `--rebuild` (BA4). Checking whether bare `rebuild` is accepted.
- Bare `rebuild` probe: `board.py rebuild --root S2` exit 0; `rebuild --from-index` exit 0; --help
  line 5-6: "the bare `check`/`rebuild` words still work (roadmap 010/090)". board.py 718-726:
  the bare word in `rebuild_cmd()` output STAYS deliberately (committed preamble + remedy). So the
  remedy is not wrong; the docstring prose (lines 46, 106, 114) still spells `rebuild --from-index`
  after the delta's BA4 "one spelling" claim. → note-level.
- redos.js: shipped regexes linear on env/-C/nice chains (<3 ms at 100-300 KB); an unterminated
  heredoc of 20k lines (320 KB) → 7,416 ms. heredoc.js (realistic TERMINATED heredoc then a
  commit): 1,000 lines 141 ms; 5,000 lines 3,082 ms; 10,000 lines 11,866 ms; 20,000 lines
  (1.08 MB) 46,605 ms. Isolated: the shipped GIT_CMD over the blanked 20k text 26,574 ms; the same
  regex with `[ \t]*` after the separator instead of `\s*`: 6.4 ms; 40k lines: 156,205 ms.
  Cause: codeOf blanks heredoc bodies to spaces, then `(?:^|[\n;&|(]\s*…)` lets `\s*` run across
  every blanked line from each `\n` → O(lines × bytes). cdBefore's regex has the same shape.
- Subject extraction probe (commitSubjectsIn): -qm/-am/-q -m/two -m/--amend -m/--message= all read
  correctly. `sh -c "cd x; git commit -m \"a: e\""` → subject `"a:` (counted as a command: the `;`
  inside the quoted string is read as command position); `grep -n "x; git commit -m …"` → `"a:`;
  `echo $(git commit -q -m "a: g")` → subject `a: g)`; backtick form → none. So the design's "a
  commit command quoted in … a grep pattern, an echo or an sh -c string runs nothing and is no
  evidence" holds only where the quote opens directly before `git`.
- Live runs by explicit transcript path (counts only; `--root` = this worktree; locateTranscript
  by bare id found nothing because the files carry the full UUID name, while the brief's ids are
  8-char prefixes — not a defect): b27a9a78: confirmed 4, unconfirmed 42 (1 noted), leftOut 0,
  unreadable 0. d0ca5d24: confirmed 24, unconfirmed 44 (36 noted), claimedMoved 33. 722ac2e2:
  confirmed 64, unconfirmed 105 (63 noted); the delta's 4e3b3984 and 2744f6aa print as
  UNCONFIRMED (a worker session made them: the IE8 limit, as designed). The high "noted" share
  (the session's own command gave the subject but did not fit) prompted the idiom probe below.
- coldsweep --commit 2744f6aa --path 010/020 --path 010/030 (board files the commit touched,
  omitted from the brief's path list; DISCLOSED): 010/020 gained a 📝 correction note (the stop
  lived in an interim sentence of § On a split board); 010/030 gained a "Superseded 2026-09-20"
  note about the two slips being caught at the hook — NOT about where the stop lived. So the
  CHANGELOG's "the ADR, 010/020 and 010/030 are corrected to say the stop had lived in an interim
  sentence" misdescribes 010/030; the ADR names "this ADR, 010/020 and 010/160" as the wrong
  records; 010/160 was not touched by this commit (act-2 check owed).
- design.md §11 (316-324): "the best a fresh read can do without a session id in every commit" —
  a commit trailer is named as the thing the read does without; §15.1's options list does not
  weigh it. templates/CLAUDE.md 62-70: "never work around or absorb them".
- gather(): locateTranscript by id searches ~/.claude/projects/*/<id>.jsonl; a path is accepted.

### Step 8 — variable-path probe, idiom census, timings, re-run 4, verdict
- commitCommandsIn probes: `W=/r/wt\ngit -C "$W" commit …` → dir null; `cd "$W" &&` → null;
  `${W}` → null; literal `-C /r/wt` and `cd /r/wt &&` → /r/wt. runDir passes `new Map()` to
  resolvePath: no variable expansion. Old GIT_MSG regex over the blanked 20k heredoc: 1.9 ms
  (so IDS1 is a regression of the delta).
- idiom.py (counts only): b27a9a78 8 commit commands (0 via $VAR, 4 literal, 4 cwd), max heredoc
  75 lines; d0ca5d24 49 (17 $VAR, 19 literal, 13 cwd), max 141; 722ac2e2 69 (12 $VAR, 33 literal,
  24 cwd), max 74. No heredoc ≥ 1000 lines in any.
- Live identifiers wall-clock: 722ac2e2 4 s; d0ca5d24 3 s.
- RE-RUN 4: `nice -n 10 python3 tools/floor.py --plane hook --root W` → exit 0, 96 lines, no ✗.
- /security-review: DISCHARGED by grounds (pending diff = the deleted sibling → SL2 trap; git
  clone and git archive into scratch both refused by the permission layer). Lens 4 by hand.
- Verdict appended to the brief below `---` (file now 527 lines). Status line updated to ACT 1
  WRITTEN. Findings: IDS1 MODERATE, IDS2 MODERATE, IDS3-5 minor, IDS6-9 note. Overall
  PASS-WITH-FINDINGS 0/2/3/4.
- Scanners on the brief: datescan exit 0 clean; spellscan exit 0 (docs/reviews ignored by
  .spellscanignore: covered nothing); wrapscan exit 0 (same, .wrapscanignore); reviewscan exit 0.
  Width: no appended line over 100 columns (awk check); the >100 lines reported are the
  brief-writer's own (title, command lines).
- Scratch folder removed after copying the probe scripts below.

### Probe scripts (verbatim, for re-running)

#### cf3probe.sh
```
#!/bin/zsh
# CF3 branch 3 probe: a peer's STAGED item line, my claim by pathspec with the index
# regenerated --from-index: does `board.py --check --staged` at the pre-commit hook refuse?
set -u
W="/Users/mike/worktrees/fable/atelier-160-1170-0709/atelier"
S="/Users/mike/.claude/fable-drain/notes/scratch-1170/cf3"
rm -rf "$S"; mkdir -p "$S"; cd "$S" || exit 2
git init -q -b main . ; git config user.email x@example.invalid; git config user.name probe  # leakscan:allow:email: synthetic probe identity, reserved .invalid domain
mkdir -p docs/roadmap/010-sec
printf '# Board\n' > docs/roadmap/README.md
printf '# Section\n' > docs/roadmap/010-sec/README.md
printf -- '- [ ] **X** peer item\n' > docs/roadmap/010-sec/010-x.md
printf -- '- [ ] **Y** my item\n' > docs/roadmap/010-sec/020-y.md
python3 "$W/tools/board.py" --rebuild --root "$S" >/dev/null
git add -A && git commit -q -m "seed" && echo "seed ok"
# the hook: the staged-plane check
mkdir -p .git/hooks
cat > .git/hooks/pre-commit <<HOOK
#!/bin/sh
python3 "$W/tools/board.py" --check --staged --root "$S"
HOOK
chmod +x .git/hooks/pre-commit
# the peer stages a claim of X (item only, index not yet rebuilt)
printf -- '- [~] (claimed) **X** peer item\n' > docs/roadmap/010-sec/010-x.md
git add docs/roadmap/010-sec/010-x.md
echo "--- peer staged X. git diff --cached --stat:"; git diff --cached --stat
# I claim Y: edit, stage, rebuild from index, stage index
printf -- '- [~] (claimed) **Y** my item\n' > docs/roadmap/010-sec/020-y.md
git add docs/roadmap/010-sec/020-y.md
python3 "$W/tools/board.py" --rebuild --from-index --root "$S"
git add docs/ROADMAP.md
echo "--- index now carries X?"; grep -c 'claimed' docs/ROADMAP.md
echo "--- A: pathspec commit (Y + index) — expect REFUSED:"
git commit -q -m "claim Y" -- docs/roadmap/010-sec/020-y.md docs/ROADMAP.md; echo "exit=$?"
git log --oneline | head -3
echo "--- B: whole-index commit — expect hook PASS (absorbs X):"
git commit -q -m "claim Y whole"; echo "exit=$?"
git show --stat --format=%s HEAD | head -8
# ordering probe: rebuild from index BEFORE staging own item
echo "--- C: order probe: fresh repo, rebuild --from-index before git add of own item"
S2="/Users/mike/.claude/fable-drain/notes/scratch-1170/cf3b"; rm -rf "$S2"; mkdir -p "$S2"; cd "$S2" || exit 2
git init -q -b main . ; git config user.email x@example.invalid; git config user.name probe  # leakscan:allow:email: synthetic probe identity, reserved .invalid domain
mkdir -p docs/roadmap/010-sec; printf '# Board\n' > docs/roadmap/README.md; printf '# Section\n' > docs/roadmap/010-sec/README.md
printf -- '- [ ] **X** peer item\n' > docs/roadmap/010-sec/010-x.md
printf -- '- [ ] **Y** my item\n' > docs/roadmap/010-sec/020-y.md
python3 "$W/tools/board.py" --rebuild --root "$S2" >/dev/null; git add -A; git commit -q -m seed
mkdir -p .git/hooks; cat > .git/hooks/pre-commit <<HOOK
#!/bin/sh
python3 "$W/tools/board.py" --check --staged --root "$S2"
HOOK
chmod +x .git/hooks/pre-commit
printf -- '- [~] (claimed) **X** peer item\n' > docs/roadmap/010-sec/010-x.md   # peer: UNSTAGED
printf -- '- [~] (claimed) **Y** my item\n' > docs/roadmap/010-sec/020-y.md
python3 "$W/tools/board.py" --rebuild --from-index --root "$S2"; echo "index claimed-count after rebuild-before-add: $(grep -c claimed docs/ROADMAP.md)"
git add docs/roadmap/010-sec/020-y.md docs/ROADMAP.md
git commit -q -m "claim Y" -- docs/roadmap/010-sec/020-y.md docs/ROADMAP.md; echo "C exit=$? (1 = hook refused, the stale index)"
echo "--- D: correct order: add own item, then rebuild --from-index, then add index, pathspec commit"
python3 "$W/tools/board.py" --rebuild --from-index --root "$S2"; git add docs/ROADMAP.md
git commit -q -m "claim Y" -- docs/roadmap/010-sec/020-y.md docs/ROADMAP.md; echo "D exit=$?"
echo "peer's X still dirty and unstaged? $(git status --short | tr '\n' ' ')"
echo "index carries X as claimed? $(grep -c 'claimed) \*\*X' docs/ROADMAP.md)"
```

#### heredoc.js
```
const cc = require('/Users/mike/worktrees/fable/atelier-160-1170-0709/atelier/instruments/ccclose');
const time = (label, fn) => { const a = process.hrtime.bigint(); const r = fn(); console.log(label, 'ms', (Number(process.hrtime.bigint() - a) / 1e6).toFixed(1), 'items', Array.isArray(r) ? r.length : r); };
const hd = (n) => "cat > /tmp/f.md <<'EOF'\n" + 'a line of prose in a file a session writes by heredoc\n'.repeat(n) + "EOF\ngit add -- f.md && git commit -q -m \"docs: add f\"";
for (const n of [1000, 5000, 10000, 20000]) time(`terminated heredoc ${n} lines (${hd(n).length} bytes), commitCommandsIn`, () => cc.commitCommandsIn(hd(n), '/r'));
// The same regex with [ \t]* after the separator instead of \s*, on the blanked text.
const GIT_OPTS = '(?:(?:-[Cc]|-c)\\s+(?:"[^"]*"|\'[^\']*\'|\\S+)\\s+|--no-pager\\s+)*';
const mk = (ws) => new RegExp('(?:^|[\\n;&|(]' + ws + '|\\b(?:then|do|else)\\s+)(?:[A-Za-z_]\\w*=\\S*\\s+)*(?:(?:command|time|exec|env|nice(?:\\s+-n\\s*-?\\d+)?)\\s+)*git\\s+(' + GIT_OPTS + ')(commit|merge|rebase|pull)\\b', 'g');
const blank = (s) => s.split('\n').map((l, i) => (i > 0 && i < s.split('\n').length - 2 ? ' '.repeat(l.length) : l)).join('\n');
const big = blank(hd(20000));
time('regex as shipped (\\s*) over blanked 20k', () => [...big.matchAll(mk('\\s*'))]);
time('regex with [ \\t]* over blanked 20k', () => [...big.matchAll(mk('[ \\t]*'))]);
time('regex as shipped over blanked 40k', () => [...blank(hd(40000)).matchAll(mk('\\s*'))]);
```

#### redos.js
```
const cc = require('/Users/mike/worktrees/fable/atelier-160-1170-0709/atelier/instruments/ccclose');
function t(label, s) { const a = process.hrtime.bigint(); const r = cc.commitCommandsIn(s, '/r'); const b = process.hrtime.bigint(); console.log(label, 'len', s.length, 'ms', Number(b - a) / 1e6, 'items', r.length); }
t('env-assign chain 20k', '; A=b '.repeat(20000) + 'x');
t('env-assign chain 50k', '; A=b '.repeat(50000) + 'x');
t('-C chain 5k', 'git ' + '-C "a b" '.repeat(5000) + 'status');
t('-C chain 20k', 'git ' + '-C "a b" '.repeat(20000) + 'status');
t('nice chain 20k', '; ' + 'nice -n 10 '.repeat(20000) + 'x');
t('heredoc unterminated 20k lines', 'cat <<EOF\n' + 'git commit -m x\n'.repeat(20000));
t('many heredocs 5k', 'cat <<A\nx\nA\n'.repeat(5000) + 'git commit -q -m "y: z"');
t('quotes -C odd', 'git -C "unterminated ' + 'a '.repeat(20000) + ' commit -m x');
```

#### fields.py
```
import json, os, sys, glob
# Counts only: which records carry cwd and timestamp, in real transcripts. Prints no content.
base = os.path.expanduser('~/.claude/projects/-Users-mike--pets-atelier')
files = sorted(glob.glob(os.path.join(base, '*.jsonl')), key=os.path.getmtime)[-6:]
agents = sorted(glob.glob(os.path.join(base, '*', 'subagents', 'agent-*.jsonl')), key=os.path.getmtime)[-6:]
def scan(f):
    c = dict(a=0, a_cwd=0, a_ts=0, bash=0, bash_cwd=0, res=0, res_ts=0, res_err=0)
    with open(f, encoding='utf-8', errors='replace') as fh:
        for ln in fh:
            try: o = json.loads(ln)
            except Exception: continue
            m = o.get('message') or {}
            cont = m.get('content') if isinstance(m, dict) else None
            if o.get('type') == 'assistant' and isinstance(cont, list):
                c['a'] += 1; c['a_cwd'] += 'cwd' in o; c['a_ts'] += 'timestamp' in o
                for b in cont:
                    if isinstance(b, dict) and b.get('type') == 'tool_use' and b.get('name') == 'Bash':
                        c['bash'] += 1; c['bash_cwd'] += 'cwd' in o
            if o.get('type') == 'user' and isinstance(cont, list):
                for b in cont:
                    if isinstance(b, dict) and b.get('type') == 'tool_result':
                        c['res'] += 1; c['res_ts'] += 'timestamp' in o; c['res_err'] += bool(b.get('is_error'))
    return c
print('main transcripts:', len(files))
for f in files: print(' ', os.path.basename(f)[:8], scan(f))
print('subagent transcripts:', len(agents))
for f in agents: print(' ', os.path.basename(f)[:14], scan(f))
```

#### idiom.py
```
import json, os, re, glob
# Counts only. Among each real transcript's Bash commands that run `git commit`, how many address the
# repo through a shell variable (-C "$X", cd "$X") vs a literal, and the largest heredoc body (lines).
base = os.path.expanduser('~/.claude/projects/-Users-mike--pets-atelier')
ids = ['b27a9a78', 'd0ca5d24', '722ac2e2']
HD = re.compile(r"<<-?\s*(['\"]?)([A-Za-z_]\w*)\1")
def cmds(f):
    with open(f, encoding='utf-8', errors='replace') as fh:
        for ln in fh:
            try: o = json.loads(ln)
            except Exception: continue
            if o.get('type') != 'assistant': continue
            m = o.get('message') or {}
            for b in (m.get('content') or []):
                if isinstance(b, dict) and b.get('type') == 'tool_use' and b.get('name') == 'Bash':
                    c = (b.get('input') or {}).get('command')
                    if isinstance(c, str): yield c
def hd_max(c):
    ls = c.split('\n'); best = 0
    for i, l in enumerate(ls):
        for mm in HD.finditer(l):
            tag = mm.group(2); j = i + 1
            while j < len(ls) and ls[j].strip() != tag: j += 1
            best = max(best, j - i - 1)
    return best
for sid in ids:
    f = sorted(glob.glob(os.path.join(base, sid + '*.jsonl')))[0]
    n = var = lit = plain = 0; hmax = 0; big = 0
    for c in cmds(f):
        hmax = max(hmax, hd_max(c)); big += hd_max(c) >= 1000
        if not re.search(r'\bgit\b.*\bcommit\b', c, re.S): continue
        n += 1
        if re.search(r'(-C\s+"?\$|\bcd\s+"?\$)', c): var += 1
        elif re.search(r'(-C\s+"?/|\bcd\s+"?/)', c): lit += 1
        else: plain += 1
    print(sid, 'git-commit commands', n, '| via $VAR', var, '| via literal abs path', lit, '| neither (cwd)', plain, '| max heredoc lines', hmax, '| heredocs >=1000 lines', big)
```

#### live.sh
```
#!/bin/zsh
# Counts only. Runs the worktree's ccclose --identifiers --json on real sessions of this repo.
W="/Users/mike/worktrees/fable/atelier-160-1170-0709/atelier"
for sid in "$@"; do
  node "$W/instruments/ccclose" --identifiers --json --root "$W" --session "$sid" > "/Users/mike/.claude/fable-drain/notes/scratch-1170/live-$sid.json" 2>"/Users/mike/.claude/fable-drain/notes/scratch-1170/live-$sid.err"; echo "$sid exit=$?"
  /usr/bin/python3 -I - "$sid" <<'PY'
import json, sys
sid = sys.argv[1]
j = json.load(open(f"/Users/mike/.claude/fable-drain/notes/scratch-1170/live-{sid}.json"))
c = j['commits']; b = j['board']
print('  commits known', c['known'], 'confirmed', c['total'], 'unconfirmed', c['unconfirmed']['total'], 'noted', sum(1 for x in c['unconfirmed']['items'] if 'note' in x), 'leftOut', c['leftOut']['total'], 'unreadable', c['evidenceUnreadable'], 'unbroken', c['unbroken'])
print('  window', j['session'].get('window'))
want = {'4e3b3984', '2744f6aa'}
print('  delta shas in confirmed:', [x['short'][:8] for x in c['items'] if x['short'][:8] in want], 'in unconfirmed:', [x['short'][:8] for x in c['unconfirmed']['items'] if x['short'][:8] in want])
print('  board keys', sorted(b.keys()) if isinstance(b, dict) else b)
print('  agents', j['agents'].get('total') if isinstance(j.get('agents'), dict) else j.get('agents'))
PY
done
```

#### sweep.sh
```
#!/bin/zsh
W="/Users/mike/worktrees/fable/atelier-160-1170-0709/atelier"
for p in "$@"; do
  echo "===== $p"
  python3 "$W/tools/coldsweep.py" --root "$W" \
    --also-exclude docs/roadmap/160-doctrine-review-owed/1170-rule-4-cold-pass-queued-identifiers-on-evidence-and-the-same-item-stop.md \
    --also-exclude docs/roadmap/160-doctrine-review-owed/960-rule-4-cold-pass-queued-identifiers-credit-on-evidence.md \
    --also-exclude docs/roadmap/010-board-store-migration-per-item-files-mik/160-cf3-s-sibling-stop-is-now-stricter-than-its-cause.md \
    --also-exclude docs/roadmap/160-doctrine-review-owed/260-rule-4-cold-pass-queued-bs1-wording.md \
    "$p" 2>&1 | grep -v '^docs/roadmap/[0-9]' | head -40
done
```
- Final width pass: no appended line over 100 characters (python len, lines 229-529); datescan
  exit 0 again after the rewrap. Tree: ` D` sibling (partition), ` M` brief. ACT 1 SAVED at
  2026-11-16 ~07:50 UTC; waiting for the release message before act 2.

## Act 2 — 2026-11-16 UTC, after the release message (act 1 committed as 004a9bec)

- Release message (orchestrator): named the held file path, the records to read, the shape of
  the reconcile, "no commit or push"; nothing about the delta or any finding.
- Read: the held sibling (27 lines; 2 pointer questions, 2 brief-writer questions, 1 held-back
  fact, re-run results at 457615cc: node 105 pass, board 87 OK, ci 28 secretscan advisories,
  hook exit 0). `git log -1 --format=%B` for 4e3b3984, 2744f6aa, 004a9bec. Queue pointer
  160/1170 whole (34 lines); intent records 160/960 (63), 010/160 (58), 160/260 (97) whole.
  Prior verdict 2026-10-26-0917 (901 lines): section map, IE1-IE14 headings + context, IE1-IE4
  full (487-519), IE8-IE10 full (549-575), grep for cost/variable mentions (line 459 fileSubjects
  only). Prior verdict 2026-09-25-0715 (551 lines): section map, BA1-BA8 headings + 3 lines,
  reconcile notes 444-491. SESSIONS.md: grep for the delta's ids (one 2026-10-18 entry, line 325)
  and the 2026-11-09 entries (lines 335-340; the 1233 UTC queue run is the author's); the
  2026-09-20 session record's late closing note via `git show 2744f6aa -- docs/sessions/...`;
  010/020 at HEAD lines 50-62.
- Findings vs records: IDS1 not anticipated (regression of the delta); IDS2 not anticipated by
  IE3/IE10 (no variable named) and the author's body claims the resolution without the limit;
  IDS3: IE4 counsel wider than what was built; IDS4 settled: the 010/030 edit was BA5 per the
  commit body, the changelog filed it under BA1; 010/160's body uncorrected; IDS5: body says no
  stamped copy changes (true of the claim rule, silent on the backstop line); IDS6: exception
  recorded in 010/160's close note after the answer; IDS7 new; IDS8: BA4 applied to README and
  CONCURRENCY, docstring prose left; IDS9: IE8's two routes, trailer in neither. No finding
  formed at reconcile; severities unchanged.
- `### Reconcile` appended (brief now 594 lines). Scanners: datescan 0, spellscan 0, wrapscan 0,
  reviewscan 0. No appended line over 100 characters. Sibling NOT folded or deleted (orchestrator
  folds). No commit, no push. ACT 2 SAVED.
