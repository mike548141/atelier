# Cold pass — the empty term list, the credential carve-out, publishscan's visible hatch, the hand-up route's parent duties

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (a guard every child
runs and a route every child files through are doctrine by function, rule 3).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** act 1 written 2026-11-15 UTC by a Fable 5.1 reviewer in worktree
`atelier-160-1220-2002`, under a headless Opus 5.5 orchestrator started by drain session
`21a271a5` (the principal's `/fable-drain` order of 2026-11-16 NZDT); PASS-WITH-FINDINGS, 0 MAJOR,
2 MODERATE, 6 minor, 3 notes; act 2 (reconcile) follows the sibling's release. Brief written
2026-11-09 UTC by session `9bb1b984`, a headless Opus 5.5 brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/1220-rule-4-cold-pass-queued-thirteen-technical-fixes.md`.
**Size of this pass:** medium: about 785 changed lines across four fixes, three of them scanners
that block on every child's plane, plus a live-corpus comparison if you re-run the blast-radius
claim.
**Why it earns a review:** Three of these scanners decide what may be committed or published in
every child, and a change of their blocking set reaches each child at its next CI run. The worst
failure is a guard that goes quiet on a secret while the record says it blocks again.

**Scope of this brief, against the pointer.** The pointer lists thirteen items. This brief covers
four: `160/090`, `160/470` and `160/300`, whose prior passes each stood with a MAJOR, and `160/100`,
whose fix the pointer names as a question worth the pass's time. The other nine are named under
*Non-goals*. The principal's rule for this brief-writing run is that a small fix after a pass with
no MAJOR is not owed a review. The nine stay on the pointer as a dated note and were reported to him
as candidates; he can widen this pass.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `722ac2e2`,
  2026-11-09, in its ruling round, and the Sonnet workers it dispatched, which wrote the commits
  (per the queue pointer). The author queued this pass and does not take it.
- **Who wrote this brief:** session `9bb1b984` (`claude-opus-5-5`), a headless brief-writer started
  2026-11-09 UTC by coordinating session `74f2b8cd` (Opus 5.5), on the principal's request to brief
  every owed pass. Neither wrote any of this delta. **Off-tier for review, disclosed: the
  brief-writer forms no finding and writes no severity**, and stops after writing. It ran no review
  and used no Fable model. `74f2b8cd` built none of these subjects and forms no finding; its launch
  prompt is the brief-writer's only instruction.
- **Barred from running this pass:** session `9bb1b984` and session `74f2b8cd` (whoever writes a
  brief does not run it, the principal's rule), and session `722ac2e2` with everything it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `74f2b8cd`: the
  item numbers, the rules of the run, and the statement that it built none of these subjects. It
  carried no framing of the work. The brief-writer had no contact with the author session or its
  workers.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md` and `docs/method/REVIEW.md` whole; the board
  item whole; the first line, last nine lines and every `MAJOR` line (verdict counts and finding
  IDs) of all thirteen items; the delta commits body-free through `tools/coldsweep.py --commit`, by
  their `CHANGELOG.md` hunks; commit subjects through `git log`;
  `docs/reviews/2026-11-09-0207-leakscan-off-rules-cold.md` whole (an unrun brief, read for house
  form). It opened **no prior verdict and no delta commit's message body**. Its harness also loaded
  user-level and repo instruction files and a memory index, which hold private context this brief
  does not carry. Everything evaluative it formed is in the sibling.

## The acceptance test

The principal's answer, printed by this line (a label of the option he picked; the text around it
is the author's and is barred until phase 2):

```
tr -s ' \n' ' ' < docs/roadmap/160-doctrine-review-owed/090-rule-4-review-queued-tier-fable-pass-type-code.md | grep -o '"Approve all 13"'
```

Recorded as an answer, after a one-line summary of each fix, not a ruling in his own words. What
each summary said is on the item and is barred until phase 2. `CHANGELOG.md` states what the delta
takes the answer to authorise: the author's claim to test.

## What the work is

- **`db8c44b7`** — `scanners: leakscan refuses an empty or unreadable term list; AR5-AR8 fixes (160/090)`.
- **`29edf58d`** — `scanners: a fingerprint under a credential key blocks again (160/100)`.
- **`3b002d51`** — `scanners: publishscan prints what its ignore file hid; edge patterns (160/470)`.
- **`a81ebe5a`** — `docs: changelog and tools README for 160/090, 160/100, 160/470` (its `160/050`
  paragraph is out of scope).
- **`3312cdbd`** — `method: the hand-up route gains parent-side duties, a narrower duty, a private-first rule (160/300)`.

Delta paths, read at each commit and at HEAD:

- `tools/leakscan.py`, `tools/test_leakscan.py`, `tools/floorfleet.py` (the term-list board hunk
  only), `tools/test_floorfleet.py`, `tools/signscan.py`, `tools/test_signscan.py`,
  `tools/test_floor.py`, `.github/workflows/floor.yml`
- `tools/secretscan.py`, `tools/test_secretscan.py`
- `tools/publishscan.py`, `tools/test_publishscan.py`, `tools/floor.py`
- `docs/method/REVIEW.md` (rule 3's added sentence), `skills/review-brief/SKILL.md`,
  `docs/decisions/README.md`
- `docs/method/PROPAGATION.md` § *Pointing up*, `CLAUDE.md` (the read-order step)
- `tools/README.md`, `CHANGELOG.md`

First confirm the tree holds the delta, then read each commit body-free. With no `--path` the board
store is left out of the diff:

```
git merge-base --is-ancestor 3312cdbd HEAD; echo $?
python3 tools/coldsweep.py --root . --commit db8c44b7
python3 tools/coldsweep.py --root . --commit 29edf58d
python3 tools/coldsweep.py --root . --commit 3b002d51
python3 tools/coldsweep.py --root . --commit a81ebe5a
python3 tools/coldsweep.py --root . --commit 3312cdbd
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1).

Then see what has landed on those paths since, and read anything new the same way, only as far as
it bears on this delta at HEAD: `git log --oneline 3312cdbd..HEAD -- tools/leakscan.py
tools/secretscan.py tools/publishscan.py tools/signscan.py tools/floor.py tools/floorfleet.py
.github/workflows/floor.yml docs/method/PROPAGATION.md CLAUDE.md`.

**This is an application review.** Rule 2 cannot be fully honoured: the delta's `CHANGELOG.md`
entries and commit subjects carry finding IDs and decision stamps from the passes it applies (AR,
AB, PL, RU). Review the code and doctrine at HEAD and commit findings first; open those verdicts
after. The residual exposure is named here, not denied (`REVIEW.md` § *Applying decisions to
doctrine*).

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- Under `--require-terms` (the hook plane) a term list holding no terms is "exit 2"; without the
  flag it "degrades like an absent list, with a warning naming the file", and the pass line says
  "structural only". "CI passes no `--require-terms`, so no child's CI changes."
- An unreadable list "is exit 2 with a remedy, not a traceback"; a set-but-empty `--terms ""` or
  environment value "is refused under `--require-terms` and means 'not set' without it".
- `api_key: SHA256:<body>` "passed fully clean after E3"; the carve-out "is now off on any line
  that names a credential key, which restores the pre-E3 block. Fingerprints in prose context stay
  suppressed, as ruled."
- Suppressions are "located (`path:line`, human and `--json`, first 50) as well as counted".
- `publishscan` prints what `.publishscanignore` hid on every run, "zero included", "on the default
  and history planes"; paths match with case folded; `.*_history` and `._*` match the basename
  only; "the selftest asserts every entry is reachable".
- "Each was probed against every floor-carrying repo on this machine, old scanner against new, and
  no repo's blocking result changed" (`CHANGELOG.md`, the four-application entry).
- An atelier session "reads the open hand-up PRs at open and lands any it finds first"; the
  merge-time check is `gh pr view <n> --json headRefName,title,body,files` and "the harm is one-way,
  so it is read before the merge".
- A hand-up's number "is provisional"; an index conflict is resolved "by merging in the parent's
  worktree", "never a rewrite of the reporter's branch".
- "The duty is the principal's repos", "the narrower of the two options"; "a doctrine defect that
  is a vulnerability goes private first, with its public item landing with the fix".
- "AR4 was already fixed"; "AR2 is largely moot, the bypass having been removed".

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope,
and a non-goal that fences off the risk is a finding.

**Non-goals:** the other nine items of the pointer (`160/050` `e2a8c16f`, `160/220` `f816cebc` and
`dfd4a324`, `160/490` `c7fe93b0`, `160/520` `ddbe669c`, `160/560` `d7747285`, `160/590` `7a516d0a`,
`160/570` `436273ba`, `160/430` `1adda4fa`, `160/680` `c11c5371`), small applications after passes
with no MAJOR, not briefed under the principal's rule for this run; earlier fixes on those same
items from before this list; `160/300`'s privacy clause (pass `160/1050`, its own brief);
`47e8345f`'s hunks on `REVIEW.md` and the skill (pass `160/1210`). `tools/floorfleet.py`'s `gh`
handling is `160/050`'s. A finding you make in passing on any of these is still a finding; just do
not go looking.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Is
   this the right problem, solved at the right altitude and in the right shape, against the
   acceptance test?
2. **Correctness & quality.** Re-drive the claims above. Record each overclaim against the text that
   makes it.
3. **Completeness / harvest.** Every surface that states this behaviour (V3); one home (V4); no
   contradiction (V5). Find tests that would stay green on a broken delta by mutating a scratch
   copy.
4. **Security & privacy**, mandatory: at design altitude what this exposes, over-collects or leaks
   by weakness of design; at code altitude the likely vectors for its class, checked against an open
   catalogue (OWASP ASVS or the domain's equivalent). Aim `/security-review` at code only from a
   clean tree, as *House rules* says; weigh a clean pass over markdown as nothing.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-09 UTC, from the worktree root,
except the `cd tools` line, and its results are held in the sibling. Read exit codes explicitly.
Check `uptime` first and run the heavy lines under `nice -n 10`. Use the `python3` first on the
machine's `PATH` (3.14.6 when written); CI pins 3.12.

```
python3 tools/leakscan.py --selftest
python3 tools/secretscan.py --selftest
python3 tools/publishscan.py --selftest
python3 tools/signscan.py --selftest
cd tools && python3 -m unittest test_leakscan test_secretscan test_publishscan test_signscan test_floor test_floorfleet test_templates; cd ..
python3 tools/floor.py --plane ci --root .
nice -n 10 python3 -m unittest discover -s tools
```

The "old scanner against new" comparison over every floor-carrying repo is a recorded proof (V2):
re-run it read-only, by count, reporting no repo by name. The brief-writer did not re-run it.

## House rules for this run

- **Live systems:** read-only reads of live systems as needed; no live writes. A check that needs a
  write is marked NOT RUN, with why. No push, no write to GitHub, no network service changed. `gh pr
  list` and `gh pr view` are reads.
- **Never print a secret** or any personal data. Probes use scratch copies and synthetic fixtures
  under your scratchpad, deleted when you finish. A fixture shaped like a credential stays synthetic
  and is not quoted in the verdict.
- Name your own review worktree in the verdict. It is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad. Child
  repos are read-only and reported by count only, never by name or path.
- **Skip the session-log step of the read order** (`CLAUDE.md` step 4; `REVIEW.md` rule 2). If you
  read it anyway, disclose what you met.
- One heavy process at a time, foreground, with a long timeout. Never run an installed tool by bare
  name from `PATH`: use `python3 tools/<x>.py` or `instruments/<x>` from your worktree.
- `/security-review` reads the session's pending diff, not this delta. Aim it at the code by
  reproducing the diff in a scratch clone, or discharge it by grounds and do the code-altitude read
  by hand, never with this brief or its sibling dirty.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo is
  PUBLIC: quote no secret, email address, private repo name or path.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/` (for this delta chiefly
`docs/reviews/2026-09-25-0715-ap-rulings-applied-cold.md`,
`docs/reviews/2026-08-09-0825-e6b-advisory-e3-fingerprint-cold.md`,
`docs/reviews/2026-10-03-0357-publishscan-round-2-cold.md` and
`docs/reviews/2026-09-25-0715-report-up-duty-cold.md`), this brief's sibling
`docs/reviews/2026-11-09-0238-empty-terms-credential-carveout-publishscan-handup-cold.deferred.md`
(a held-back file; by count: 13 questions, 3 facts), every item under
`docs/roadmap/160-doctrine-review-owed/` beyond its title, which includes this delta's four intent
records (`090`, `100`, `470`, `300`), and every delta commit's message body.

The delta's own docstrings, comments, README and `CHANGELOG.md` entries carry the author's account
of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  'require.terms|structural only|credential key|never-publish path|hand-up'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the re-run
list. Append your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, any orchestrator, what you read, the UTC day), per-lens answers, V1–V7 each
answered or discharged with grounds, each load-bearing assumption damaged or confirmed with its
probe, a per-commit ledger (read body-free yes/no, findings by id), findings with stable IDs (prefix
`TL`: `TL1`, `TL2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit bodies;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work is doctrine by function, so every finding is the principal's to decide (rule 3): record
all, apply nothing. Counsel per finding is welcome, labelled as counsel and kept beneath it.

---

## Verdict — act 1 (cold, Fable 5.1), 2026-11-15 UTC

### Provenance (V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named tier, checked at selection. The
  one reviewer: it read the delta, answered the lenses, assigned every severity below.
- **Spawn:** a headless Opus 5.5 orchestrator, itself started by drain session `21a271a5` (Opus
  5.5), under the principal's `/fable-drain` order of 2026-11-16 06:53 NZDT (the weekly drain
  approval; a pass running at the reset may finish). Both are rule-4 off-tier orchestrators: they
  hold the context partition, form no finding and write no severity. Neither wrote the brief or the
  delta. The orchestrator read the brief, the board item (to claim it) and the drain instructions.
  Not started or instructed by the barred sessions `9bb1b984`, `74f2b8cd`, `722ac2e2` or anything
  `722ac2e2` started.
- **The orchestrator's direction, summarised (not verbatim; it was process only):** the item id and
  the brief's path; this worktree's path and the rule to use absolute paths; the review-log path;
  what may be written (this file and the log); no commit, push, add, stash or branch change; no
  live writes, reads allowed; load discipline (`nice`, one suite at a time); the barred set as the
  brief states it; the partition (the `.deferred.md` sibling removed from the worktree, not to be
  sought anywhere); how act 1 ends and how act 2 is released. It carried **no question about the
  delta, no pointer to where the risk lives, and no request about any finding**.
- **Worktree:** `atelier-160-1220-2002` (a linked worktree of this repo), HEAD `e9ecf7d4`, the
  claim commit; `git merge-base --is-ancestor 3312cdbd HEAD` exit 0. `git status` shows only the
  sibling's planned deletion.
- **Read before writing (disclosed):** this brief whole; `docs/method/REVIEW.md` whole; the five
  delta commits body-free through `tools/coldsweep.py --commit` (each reported "message body not
  printed", 0 barred and 0 board-store files); the delta paths at HEAD; `PROPAGATION.md`
  § *Pointing up* whole; `SECURITY.md`; `GUARDS.md` headings and § *Fail noisy, then subtract*;
  the child template's doctrine bullet; `CHANGELOG.md` only through the delta's own hunks and the
  brief's coldsweep sweep (184 hits, the `160/` section excluded); the titles only of board items
  `310/020` and `140/020`. The repo's own `CLAUDE.md` and the user-level instruction file were
  loaded by the harness; they hold private context this verdict does not carry. **Not read:**
  `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, any prior verdict, any `160/` item
  body, any delta commit body, the sibling. Residual exposure, as the brief names it: the delta's
  `CHANGELOG.md` entries and commit subjects carry the prior passes' finding ids (AR, AB, PL, RU)
  and one-line summaries of what each fix answered. Everything evaluative below was formed before
  any of those verdicts was opened.
- **Live reads taken (no writes):** `gh repo view` (visibility, issues flag), `gh pr list` (open
  and all states), `gh pr view` on the two open hand-ups (header fields and file list; body length
  only), `gh api …/private-vulnerability-reporting`. Read-only scans of the 23 floor-carrying repos
  on this machine, reported by count only.
- **Review log (open by design):** `~/.claude/fable-drain/notes/atelier-160-1220-2002.md`, every
  check and its result, act-1 entries written before the sibling's release.

### Load-bearing assumptions, named first (lens 1)

- **A1 — a term list that loads no terms is never legitimate cover.** Confirmed for the hook plane
  (the doctrine wants full cover or no commit). Damaged at the edge: the refusal's remedy says
  "Restore the list", which assumes loss; an adopter whose list is empty by inexperience is told to
  restore what never existed (TL10).
- **A2 — the board and the hook agree on whether this machine has cover.** Damaged: they disagree
  on the set-but-empty environment value the delta itself made a refusal (TL1).
- **A3 — a credential-named key on a line makes any fingerprint on it a credential.** Confirmed as
  the ruled direction's natural edge (prose lines name no key; probes on eight shapes behave as
  the tests say). Damaged in degree: "blocks" holds only where the entropy net can see the body
  (TL7).
- **A4 — the hatch is safe once visible.** Confirmed: the suppressed line prints zero, lists the
  first ten, `--json` carries all, both planes; `floor.py --plane ci` shows it live.
- **A5 — case folding the denylist and keeping the hatch case-sensitive changes no child's result
  today.** Confirmed by re-run over 23 repos (below). The asymmetry can red a child later (a
  `*.log` exemption and an `APP.LOG`), and the README states it.
- **A6 — a read-order step is enough to make landing hand-ups happen.** Damaged by the forge: two
  hand-ups have stood open since 2026-11-13, through several atelier sessions, four days after the
  step landed; the enforcement rung the pass asked for was declined and is unowned (TL2).
- **A7 — the parent-side duties bind only atelier, so "Children: nothing to do".** Damaged: two
  of the added rules bind reporters (children), and the stamped bullet does not carry them (TL6).
- **A8 — the brief's account of the work.** Held: the five commits, their subjects and paths match
  the tree; the two branches (3312cdbd is not an ancestor of the other four) merged later and all
  sit under HEAD. Twenty-two later commits touch the delta paths; none reverses a delta hunk
  (verified by reading the functions at HEAD and by behaviour probes, not by reading those
  commits' bodies).

### Per-lens answers

1. **Approach.** Right problems, right altitude: each fix sits in the scanner or the doctrine
   section that owns the behaviour, reuses the sibling grammar (`report.suppressed_line`, the
   rule-(b) tally shape, `shlex`), and takes the narrower option where one was offered. The one
   altitude miss is `160/300`: a duty that had "no trigger" was given a prose trigger and no
   check, and its first week shows the shape of the original defect again (TL2).
2. **Correctness.** Every behavioural claim in the brief's list re-drove true (re-run ledger).
   Three statements are stronger than their evidence: "blocks" (TL7), "eleven stood open for
   three weeks" (TL4), and `terms_state`'s "cannot drift" (TL1).
3. **Completeness / harvest.** Mirrors swept: the old publishscan `why` is gone from every surface
   (0 hits tree-wide); README, CHANGELOG, floor.py, REVIEW.md rule 3, decisions README, the skill,
   floor.yml and the pin test all carry their sentence. Missed: the floorfleet board for the
   empty-value case (TL1); the stamped child bullet for the reporter-side rules (TL6); a
   cross-reference that reaches no rule (TL5). One test is platform-blind (TL8).
4. **Security & privacy.** `/security-review` **NOT RUN, discharged with grounds:** it reads the
   session's pending diff, and this worktree's pending diff is the deletion of the `.deferred.md`
   sibling, that is, the barred bytes themselves (the SL2 class REVIEW.md names); a scratch clone
   cannot redirect it. Code altitude by hand against ASVS input-handling and injection classes:
   `--end-of-options` closes option injection through a workflow-supplied boundary (probe: an
   option-shaped boundary raises, not silently lists nothing); the remedy quotes paths with
   `shlex` (test PL13 re-run); the ignore file is control-stripped at ingest; the new regexes are
   linear; the new lists are bounded (50 locations, 10 printed). Design altitude: the hand-up
   check runs at merge, after the branch name and title are already published; the delta says so
   and names the push-time lint as the next rung (unbuilt, see TL2). Printing exempted paths on a
   public CI log adds nothing: they are tracked, so already public. No personal data enters any
   output the delta adds. The leakscan refusals fail closed in every probed shape.

### V1–V7

- **V1** — three overclaims: TL1, TL4, TL7.
- **V2** — re-run ledger below; the fleet comparison re-run and held.
- **V3** — swept, with two misses: TL1 (board), TL6 (stamped bullet).
- **V4** — the left-out list has one home (code comment; README and docstring point at it); the
  empty-list semantics live in README with code comments beside the code, acceptable.
- **V5** — TL3 (read order vs reviewer rules), TL5 (GUARDS cross-reference), TL6 ("every repo"
  vs the narrowed duty; "the shapes below" naming shapes that are not below). Cross-references
  checked by rule reached: `SECURITY.md` l.21 holds the quoted sentence; `board.py --check` exists
  and is the default mode; `gh pr view … --json headRefName,title,body,files` works as written.
- **V6** — above; discharged scanner, hand read done.
- **V7** — stated above; the brief's provenance block agrees with it.

### Per-commit ledger

| commit | read body-free | findings |
|---|---|---|
| `db8c44b7` leakscan empty/unreadable list, AR5–AR8 | yes (coldsweep) | TL1, TL9, TL10 |
| `29edf58d` fingerprint under a credential key | yes (coldsweep) | TL7, TL11 |
| `3b002d51` publishscan visible hatch, edge patterns | yes (coldsweep) | TL8 |
| `a81ebe5a` changelog and README | yes (coldsweep) | TL4, TL7 (wording) |
| `3312cdbd` hand-up route duties | yes (coldsweep) | TL2, TL3, TL4, TL5, TL6 |

### Findings

Every finding here is on doctrine by function (rule 3): recorded, nothing applied. Counsel is
labelled and kept beneath each.

- **TL1 — MODERATE.** `floorfleet.terms_state()` says "present, full cover" where the hook
  refuses. With `ATELIER_LEAKSCAN_TERMS` set but empty, `leakscan --require-terms` exits 2 ("set
  but empty", the refusal `db8c44b7` added) while `terms_state()` returns `(True, "present at
  <default list>")`, because it calls `resolve_terms_path(None)` with `require=False`
  (`tools/floorfleet.py` l.848). Its docstring says it asks "through leakscan's own resolver so
  the answer cannot drift from the scanner's". The delta swept the board for the empty-list case
  and not for the empty-value case it introduced in the same commit. Probed both ways in this
  worktree (bool and the "present"/"refused" words only; the path is a home path and is not
  quoted). *Counsel:* call `resolve_terms_path(None, require=True)` in `terms_state`, map
  `TermsPathError` to `(False, str(e))`, and add the mirror of
  `test_an_empty_explicit_value_is_refused_under_require_terms_only` to `test_floorfleet.py`.
- **TL2 — MODERATE.** The hand-up landing duty is prose at rung 1, already not complied with, and
  its enforcement is unowned. The forge shows #135 and #136 (`report-` heads) open since
  2026-11-13, through the sessions that committed on 2026-11-12 to 2026-11-16, four days after
  `CLAUDE.md` step 6 made landing "the first act of a session that finds one". The pass asked for
  the push-time lint as its own item; the CHANGELOG records that the applying commit "does not
  file" it, and a tree sweep finds no item holding it (`handupscan`, "title lint": 0 hits outside
  `PROPAGATION.md` and `CHANGELOG.md`). `PROPAGATION.md`'s own sentence applies to the lint: a
  finding with no owner. #136 also shows the new reporter rules not reaching reporters: its title
  carries the item's provisional number and does not say hand-up. (`namescan`, landed later, lints
  private names in branch names and titles, not the hand-up grammar.) *Counsel:* file the lint
  item now, naming `report-` prefix, "hand-up" in the title, no `NNN/NNN` in the title, files =
  item + index; until it exists, add the `gh pr list` read to the one place every atelier session
  already runs at open (`cclive`, or `board.py --check`), so the trigger is a tool and not a
  sentence.
- **TL3 — minor.** `CLAUDE.md` step 6 binds a cold reviewer too. A reviewer that obeys it takes a
  live write mid-pass (a merge) and reads a child's account, which can be of the very doctrine it
  is reviewing; REVIEW.md rule 2's reviewer carve-out skips step 4 only. The brief's house rules
  overrode it for this pass, but the two texts disagree. *Counsel:* one clause in step 6 and in
  rule 2's "start-up reading" paragraph: a cold reviewer skips step 6 as it skips step 4.
- **TL4 — minor (V1).** "Eleven stood open for three weeks" (`PROPAGATION.md` § *Report without
  harming the parent*, and `CHANGELOG.md`). Forge data over all 71 hand-up-like PRs: eleven were
  open at once twice (2026-09-10, oldest 14 days; 2026-10-02, oldest 11 days); one hand-up ever
  reached 22 days, in a batch of seven. The count holds; the duration does not. *Counsel:*
  "eleven stood open at once, the oldest two weeks; one had earlier waited three weeks".
- **TL5 — minor (V5).** "A `handupscan` run at merge, is the next rung (`GUARDS.md`)": GUARDS.md
  holds no rung, ladder or hand-up rule (headings and a text sweep). The rung vocabulary is
  `PROPAGATION.md` § *When a rule keeps breaking* ("Three rungs, cheapest first"). The pointer
  passes a file-exists test and reaches no rule. *Counsel:* cite that section, or GUARDS.md
  § *Fail noisy, then subtract* if the intended rule is the warn-then-block pattern.
- **TL6 — minor (V3/V5).** The duty is narrowed to the principal's repos, but the stamped child
  bullet (`docs/build/templates/CLAUDE.md` l.90, mirrored at `PROPAGATION.md` l.188) still reads
  "every repo, atelier included", and the correction ("read it as the principal's") lives in the
  parent file an outside adopter does not read. The same bullet does not carry the two new
  reporter-side rules (expect the index conflict; the number is provisional, no self-reference),
  though they bind reporters, and the CHANGELOG says "Children: nothing to do". § *The duty* also
  says "the shapes below" are hold-and-flag, a fork and PR, or an issue; the route below lists
  direct write, channel and hold-and-flag, so two of the three named are not below. *Counsel:* one
  clause in the stamped bullet at the next floor bump ("of the principal's; outside it, a PR or an
  issue"), and list the adopter's two shapes in § *The route*.
- **TL7 — minor (V1).** README and CHANGELOG say the body under a credential key "is scored as an
  ordinary entropy hit and blocks". It blocks where `HIGH_ENTROPY_RX` (`[A-Za-z0-9+_-]{32,}`, no
  `/`) can see a 32+ run: a synthetic estimate over uniform 43-character base64 bodies puts that at
  about 71 %; the rest pass clean under a credential key before and after E3, and the test fixture
  `FP256` has no `/`. Pre-existing and not widened by the delta; the delta's own words "restores
  the pre-E3 block" are exact. *Counsel:* in README, "blocks where the entropy net can see the
  body" plus the charset limit under the documented limits; widening the net is its own item.
- **TL8 — minor (lens 3).** `test_pl7_an_ignore_glob_stays_case_sensitive` stays green when
  `_ignored` uses `fnmatch.fnmatch` (mutation probe on a scratch copy, macOS): on POSIX
  `normcase` is the identity, so the test pins the Windows behaviour it never runs on. *Counsel:*
  patch `os.path.normcase` to `str.lower` inside the test, or assert on `fnmatchcase` by identity.
- **TL9 — note.** The set-but-empty value "means not set" without `--require-terms` is justified by
  "a CI step that routes an unset secret into the env var"; the shipped `floor.yml` and workflow
  templates set no `ATELIER_LEAKSCAN_TERMS`. The behaviour is harmless; the comment describes a
  shape the floor does not ship.
- **TL10 — note.** The empty-list refusal's remedy, "Restore the list", assumes loss. A new
  adopter with nothing yet listed reads it as a broken tool. *Counsel:* "Add your terms, or unset
  the list: a list with no terms is the same as no list."
- **TL11 — note.** `_fingerprint_locations_line` counts spans and lists deduplicated
  `(path, line)` pairs; below the cap, two fingerprints on one line make the count exceed the list
  with no suffix saying why (the suffix prints only at the cap). The JSON carries both, so the
  reader can see it; the human line cannot.

**Overall: PASS-WITH-FINDINGS — 0 MAJOR, 2 MODERATE, 6 minor, 3 notes.** The scanner changes do
what they claim and change no child's blocking result on this machine; the doctrine change is
sound in direction and already shows, in its first week, that a prose trigger did not fire.

### Re-run ledger (V2)

Load at start 9.4, during 5 to 11 (several passes running); every suite under `nice -n 10`, one
process at a time, `python3` = 3.14.6 from `PATH`.

- `leakscan --selftest` · `secretscan --selftest` · `publishscan --selftest` · `signscan
  --selftest`: all OK, exit 0.
- `cd tools && python3 -m unittest <the seven modules>` (run as a subshell): Ran 1202 tests in
  369 s, OK, exit 0.
- `python3 tools/floor.py --plane ci --root .`: exit 0; publishscan prints `suppressed: 0
  never-publish path(s) by .publishscanignore`; secretscan prints the new location line.
- `nice -n 10 python3 -m unittest discover -s tools`: Ran 3134 tests in 1094 s, OK, exit 0
  (a first run was cut off with the reviewer's turn after about 850 tests and re-run whole; load
  5 to 16 while it ran).
- Old-vs-new publishscan (`3b002d51^` against HEAD), 23 floor-carrying repos, default and history
  planes, `--json`: 23/23 same exit code and finding set on both planes; 13 exempted paths now
  surfaced fleet-wide; 1 repo with default-plane findings, unchanged.
- Old-vs-new secretscan (`29edf58d^` against HEAD), the 6 repos with fingerprint-shaped tracked
  lines (the other 17 cannot reach the changed branch: no fingerprint span, no carve-out): 6/6
  same exit (0), blocking count (0), totals and fingerprint-suppression counts.
- Old-vs-new leakscan: discharged by reading. The diff is confined to term-list resolution; the
  machine's list is populated, so both versions take the same path over every repo.
- AB1 synthetic, `api_key: SHA256:<FP256>` and three more credential-key shapes: old exit 0 with
  one suppression; new exit 1, `high-entropy`, `response: block`. Four prose shapes stay
  suppressed in both.
- leakscan synthetic: empty, comments-only, directory, `--terms ""`, env set-but-empty, populated:
  each prints the sentence the CHANGELOG states; refusals exit 2 with a remedy, no traceback.
- `gh pr view 135` and `136 --json headRefName,title,body,files`: works; both carry the item and
  `docs/ROADMAP.md` only.
- `gh api …/private-vulnerability-reporting`: enabled. `gh repo view`: issues enabled, PUBLIC.

### Follow-up checklist

- [ ] TL1 · TL2 (the principal decides; both have one-line fixes and a filing)
- [ ] TL3 · TL4 · TL5 · TL6 · TL7 · TL8 (wording and test fixes, one session)
- [ ] TL9 · TL10 · TL11 (notes; take or decline when the above lands)
- [ ] act 2: reconcile against the sibling (13 questions, 3 facts) and the barred records, then
      the orchestrator folds the sibling
