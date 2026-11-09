# Cold pass — the empty term list, the credential carve-out, publishscan's visible hatch, the hand-up route's parent duties

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (a guard every child
runs and a route every child files through are doctrine by function, rule 3).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** BRIEF ONLY, not run. Written 2026-11-09 UTC by session `9bb1b984`, a headless Opus 5.5
brief-writer. The pass is held for the principal's explicit approval of Fable work; this brief is
not that approval.
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
