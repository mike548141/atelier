# Cold pass — a loose end makes the close "not ready until you decide", a refused call is an ask and never routed around, and ccclose's scratch-folder check and refused-delete re-route flag

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (a guard or a rule is
doctrine by function, rule 3).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** BRIEF ONLY, not run. Written 2026-11-09 UTC by session `d4a0fcf3`, a headless Opus 5.5
brief-writer. The pass is held for the principal's explicit approval of Fable work; this brief is
not that approval.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/996-rule-4-cold-pass-queued-close-loose-ends-and-routed-refusals.md`.
**Size of this pass:** medium: about 100 lines of code and 45 of doctrine in one commit, with four
instruments' docs.
**Why it earns a review:** This is standing close and autonomy doctrine every session reads, and the
instrument that checks it. The worst failure is a close that reads as verified when it is not, or an
instrument that names a session for a workaround it did not make.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `4c65083c`,
  2026-11-03, and the Opus worker it dispatched, which wrote the text and code (per the queue
  pointer). The author queued this pass and does not take it.
- **Who wrote this brief:** session `d4a0fcf3` (`claude-opus-5-5`), a headless brief-writer started
  2026-11-09 UTC by coordinating session `74f2b8cd` (Opus 5.5), on the principal's request to brief
  every owed pass. Neither wrote any of this delta. **Off-tier for review, disclosed: the
  brief-writer forms no finding and writes no severity**, and stops after writing. It ran no review
  and used no Fable model. `74f2b8cd` built none of these subjects and forms no finding; its launch
  prompt is the brief-writer's only instruction.
- **Barred from running this pass:** session `d4a0fcf3` and session `74f2b8cd` (whoever writes a
  brief does not run it, the principal's rule), and the author session named above with everything
  it started.
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
  item whole; the intent records' opening part and every line naming the principal or a landing
  account; the design note hunks in the delta, every delta commit body-free through
  `tools/coldsweep.py --commit`; commit subjects through `git log`;
  `docs/reviews/2026-11-06-2027-secretscan-public-pem-spans-cold.md` whole, **including that pass's
  verdict and folded sibling** (a different subject, read for house form), the acceptance-test
  section and the status and overall verdict lines of
  `docs/reviews/2026-10-26-0928-g3-grace-metadata-sets-cold.md` (the counts only), and the opening
  30 lines of board item `160/980`; three lines of `docs/SESSIONS.md` and the opening of
  `docs/sessions/2026-11-06-2022-fable-passes-850e.md`; the results of the re-run lines below. It
  did **not** open any other prior verdict or any delta commit's message body. Its harness also
  loaded user-level and repo instruction files and a memory index, which hold private context this
  brief does not carry. Everything evaluative it formed is in the sibling.

## The acceptance test

The principal's words, printed by the span command below (one quoted sentence in `180/170`). The
rule they sit under is `docs/method/RECORD.md`'s invariant on the all-clear, and the harness's rule
that a denied call means adjust. `180/180`'s quoted sentence is a session's words, and is that
session's report, not the principal's.

Print only the quoted spans, before phase 1:

```
python3 -c 'import re, sys
for p in sys.argv[1:]:
    t = " ".join(l.strip() for l in open(p, encoding="utf-8"))
    for m in re.findall(r"\*\"(.+?)\"\*", t): print("-", m)' \
  docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/170-declared-ready-to-close-with-loose-ends.md
```

## What the work is

- **`1569e64`** — `close: a loose end is an ask, a refusal is never routed around (180/170,
  180/180)`.

Delta paths, read at each commit and at HEAD:

- `docs/method/RECORD.md`, `docs/method/AUTONOMY.md`, `docs/method/CONCURRENCY.md`,
  `instruments/ccclose`, `instruments/ccclose.test.js`, `instruments/man/ccclose.1`,
  `instruments/ccclose.design.md`, `instruments/README.md`

First confirm the tree holds the delta, then read each commit body-free:

```
git merge-base --is-ancestor 1569e64 HEAD; echo $?
python3 tools/coldsweep.py --root . --commit <sha> --path docs/method/RECORD.md --path \
  docs/method/AUTONOMY.md --path docs/method/CONCURRENCY.md --path instruments/ccclose --path \
  instruments/ccclose.test.js --path instruments/man/ccclose.1 --path instruments/ccclose.design.md \
  --path instruments/README.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). The commit also touches board records; those are barred until phase 2, so always pass `--path`.

Then see what has landed on those paths since, and read anything new the same way, only as far as it
bears on this delta at HEAD: `git log --oneline 1569e64..HEAD -- docs/method/RECORD.md
docs/method/AUTONOMY.md docs/method/CONCURRENCY.md instruments/ccclose instruments/ccclose.test.js
instruments/man/ccclose.1 instruments/ccclose.design.md instruments/README.md`.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- "A loose end is something the close owes and has not put away; open work recorded on the board is
  not one."
- A refused tool call "is a standing decision about what the agent may do", and the agent "does not
  reach the effect it blocked through another tool".
- "From inside a session the agent cannot know that a rule is a mistake."
- The refused-delete flag lists a later delete only when every route it uses is unrefused; a retry
  by a refused route is not listed; the flag does not expire.
- `REFUSAL` matches the harness's wording, from a "census of the live store", and a failed command
  does not match.
- The design note's figures: across 1119 transcripts, 73 hold a refused delete and 9 are listed; on
  the grounding session the form lists the two Python deletes and not the later `rm`.
- Check 13 reads the folder the harness records in the transcript, "never derived"; a cut walk says
  "at least".
- The design note says what the flag misses: a delete in a script file, other routes, a subagent's
  own transcript, other refused effects.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope,
and a non-goal that fences off the risk is a finding.

**Non-goals:** the worktree-variable work (pass `160/993`); the dispatch doctrine (pass `160/995`);
ccclose checks 1 to 12 as reviewed earlier.

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
in the foreground or under `nice`; its results are held in the sibling. Read exit codes explicitly.
Check `uptime` first and run the heavy lines under `nice -n 10`. Use the `python3` first on the
machine's `PATH`.

```
node --test instruments/ccclose.test.js
nice -n 10 python3 -m unittest discover -s tools
```

Any figure the delta records from a measurement over repositories or transcripts on the machine is a
recorded proof (V2): re-run it read-only and by count. The brief-writer did not re-run those.

## House rules for this run

- **Live systems:** read-only reads of live systems as needed; no live writes. A check that needs a
  write is marked NOT RUN, with why. No push, no write to GitHub, no network service changed.
- **Never print a secret** or any personal data. Probes use scratch copies and synthetic fixtures
  under your scratchpad, deleted when you finish.
- Name your own review worktree in the verdict. It is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad. Child
  repos are read-only and reported by count only, never by name or path.
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
verdict in `docs/reviews/`, this brief's sibling
`docs/reviews/2026-11-09-0207-close-loose-ends-refusals-cold.deferred.md` (a held-back file; by
count: 7 questions, 1 facts), every other item under `docs/roadmap/160-doctrine-review-owed/` beyond
its title, every delta commit's message body, and these intent records beyond their first line:

- `docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/170-declared-ready-to-close-with-loose-ends.md`
- `docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/180-a-denied-delete-was-worked-around-with-python.md`

The delta's own docstrings, comments, README, design note and `CHANGELOG.md` entries carry the
author's account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/170-declared-ready-to-close-with-loose-ends.md \
  --also-exclude docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/180-a-denied-delete-was-worked-around-with-python.md \
  'DELETE_ROUTES|isRefusal|REFUSAL|checkScratch|A refused call|loose end'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the re-run
list. Append your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, any orchestrator, what you read, the UTC day), per-lens answers, V1–V7 each
answered or discharged with grounds, each load-bearing assumption damaged or confirmed with its
probe, a per-commit ledger (read body-free yes/no, findings by id), findings with stable IDs (prefix
`LE`: `LE1`, `LE2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit bodies;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work is doctrine by function, so every finding is the principal's to decide (rule 3): record
all, apply nothing. Counsel per finding is welcome, labelled as counsel and kept beneath it.
