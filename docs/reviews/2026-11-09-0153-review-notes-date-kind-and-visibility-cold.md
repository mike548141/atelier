# Cold pass — held-back review notes leave the shared scratch (160/380), a dated rule carries a readable kind (160/450), and a repo declares its visibility (260/050)

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (doctrine by
function: review doctrine, the floor and the fleet view).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** BRIEF ONLY. Not run. Held for the principal's explicit approval of the Fable pass.
Written 2026-11-09 UTC by session `d16dc612`, a headless Opus 5.5 brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/1180-rule-4-cold-pass-queued-review-notes-date-kind-and-visibility.md`
(barred until phase 2).
**Size:** large: three subjects in four commits across doctrine, `floor.py`, `floorfleet.py` and
`coldsweep.py`, with a live check against GitHub in CI to reason about.
**Why it earns a review:** The first subject is about the independence of every cold pass. The
second decides how checkers read a dated rule across children. The third is meant to notice a
private repo turned public.

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

The principal's answers, 2026-11-09, verbatim, each a pick from offered options: on `160/380`,
*"Keep it out of that folder"* (held-back review notes never live in the orchestrator's scratch
folder; the rule says where they go); on `160/450`, *"Add a readable label"* (each dated rule
carries a `mandate` or `default` kind the checkers read; existing dates get labelled); on `260/050`,
*"Yes, with the loud alert"* (each repo declares its visibility in its floor config, cross-checked
against GitHub, public repos get the stricter checks, and a says-private-is-public mismatch is red).
He added the same day that this builds on the daily visibility check filed under `390/020`, never a
second one.

The offered option's words were written by the authoring session and put to the principal; the
quoted pick is his. Recorded as an answer, not a ruling in his words: where the delta's wording goes
past what he picked, say so. These are claims to test, not settled scope.

## What the work is

Four commits on `main`: `d7abac17` and `595db812` (`160/380`), `db2c39f9` (`160/450`), `c4424324`
(`260/050`). `CHANGELOG.md` is in the last.

Commits on `main`: `d7abac17`, `db2c39f9`, `c4424324`, `595db812`. The landing commit is `595db812`.
**Check your tree has it before reading anything:** `git merge-base --is-ancestor 595db812 HEAD`
exits 0, and an orchestrator merges `origin/main` into the review branch before it spawns.

Delta paths: `docs/method/CONCURRENCY.md`, `docs/method/REVIEW.md`, `docs/method/GUARDS.md`,
`docs/method/PROPAGATION.md`, `docs/build/REPO-STANDARD.md`, `docs/build/templates/CONTRIBUTING.md`,
`skills/review-brief/SKILL.md`, `tools/README.md`, `tools/floor.py`, `tools/floorfleet.py`,
`tools/coldsweep.py`, `tools/test_floor.py`, `tools/test_floorfleet.py`, `tools/test_coldsweep.py`,
`.atelier-floor.json`, `CHANGELOG.md`. Read each at HEAD and read each commit body-free, scoped to
paths so board records stay barred:

```
python3 tools/coldsweep.py --root . --commit d7abac17 --path docs/method/CONCURRENCY.md --path docs/method/REVIEW.md --path skills/review-brief/SKILL.md --path tools/README.md
python3 tools/coldsweep.py --root . --commit db2c39f9 --path docs/build/REPO-STANDARD.md --path docs/build/templates/CONTRIBUTING.md --path docs/method/GUARDS.md --path docs/method/PROPAGATION.md --path skills/review-brief/SKILL.md --path tools/README.md --path tools/coldsweep.py --path tools/floor.py --path tools/floorfleet.py --path tools/test_coldsweep.py --path tools/test_floor.py --path tools/test_floorfleet.py
python3 tools/coldsweep.py --root . --commit c4424324 --path .atelier-floor.json --path CHANGELOG.md --path docs/build/REPO-STANDARD.md --path tools/floor.py --path tools/test_floor.py
python3 tools/coldsweep.py --root . --commit 595db812 --path docs/method/CONCURRENCY.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Commits since the delta on these paths:

```
git log --oneline 595db812..HEAD -- docs/method/CONCURRENCY.md docs/method/REVIEW.md docs/method/GUARDS.md docs/method/PROPAGATION.md docs/build/REPO-STANDARD.md docs/build/templates/CONTRIBUTING.md skills/review-brief/SKILL.md tools/README.md tools/floor.py tools/floorfleet.py tools/coldsweep.py tools/test_floor.py tools/test_floorfleet.py tools/test_coldsweep.py .atelier-floor.json CHANGELOG.md
```

At `457615cc` this printed 7 commit(s). Read anything new the same way.

**Application pass.** `160/380` and `160/450` apply the principal's answers and earlier passes'
counsel. It cannot fully honour rule 2: the delta carries finding ids and the decisions stamped on
them. Sequence (`REVIEW.md` § *Applying decisions to doctrine*): review the work at HEAD and commit
findings first; open the prior verdict after. Name that residual exposure in the verdict.

**Claims the work makes (extracted from its own changelog entry and files, not evaluated):**

- `CONCURRENCY.md` § *Orchestrated queue runs* says held-back material goes in a user-local
  directory outside the repo, every worktree and any harness scratchpad, never a reviewer's working
  directory, with a close-time listing of the scratchpad root.
- `REVIEW.md` rule 1 no longer calls an orchestrator-held store structural unless the bytes never
  sit on a path the reviewer is given.
- `.atelier-floor.json` advisories take an optional `kind`; `floor.py` validates and shows it;
  `floorfleet.py` shows it and says aloud when it is missing; on the hook plane a mandate's or
  unlabelled `review-by` moving later than HEAD's is a warn-only line. No existing date is labelled
  by this change.
- `"visibility": "public" | "private"` in `.atelier-floor.json`. Inside Actions only, `floor.py`
  reads GitHub's live answer (the event payload if the API is unreachable): declared private but
  public is a red build; the reverse, an unreadable answer and no declaration all warn and never
  block. It detects and alerts and cannot stop a flip.
- `coldsweep.py` warns when an `--also-exclude` matches nothing.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** what a public declaration tightens and the daily external check, which the delta
names as `390/020`'s, except where a claim depends on them.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself, first, and damage each
with a probe or confirm it by re-driving. Ask whether this is the right problem, solved at the right
altitude.
2. **Correctness & quality** — does the work do what its claims above say; honest about done versus
stubbed; any overclaim or silent scope cut, each recorded against the text that makes it.
3. **Completeness / harvest** — every surface that states the rule (V3), one home (V4), no
contradiction with sibling doctrine (V5), tests that would stay green on a broken check, what
already exists that this ignored.
4. **Security & privacy** — mandatory. `260/050` calls GitHub from CI and turns the answer into a
red build; weigh token use and the unreachable path. `160/380` is itself a confidentiality rule for
cold passes. Aim `/security-review` at the `tools/` diff from a clean tree, or discharge it by
grounds.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-09 UTC, from the worktree root
at `457615cc`; results are in the sibling. Read exit codes explicitly. Check `uptime` first and run
heavy lines under `nice -n 10`. Python is the `python3` on `PATH` (the tests need 3.10 or later;
`/usr/bin/python3` is 3.9 on this machine and some modules fail at import).

- `cd tools && python3 -m unittest test_floor`
- `cd tools && python3 -m unittest test_floorfleet`
- `cd tools && python3 -m unittest test_coldsweep`
- `nice -n 10 python3 tools/floor.py --plane ci --root .`
- `nice -n 10 python3 tools/floor.py --plane hook --root .`
- `nice -n 10 python3 -m unittest discover -s tools`
- `gh repo view --json visibility  # read-only; run inside your worktree`
- the adopting child repos, read-only and by count only: `python3 tools/floorfleet.py --root <the
  directory that holds the main atelier checkout and its sibling clones> --json` to a scratch file,
  then the kinds and visibility the fleet view reports, by count

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
(`2026-11-09-0153-review-notes-date-kind-and-visibility-cold.deferred.md`), every delta commit's
message body, the queue pointer
`docs/roadmap/160-doctrine-review-owed/1180-rule-4-cold-pass-queued-review-notes-date-kind-and-visibility.md`,
and the intent records beyond their titles:

- `docs/roadmap/160-doctrine-review-owed/380-rule-4-cold-pass-queued-the-scratchpad-clause.md`
- `docs/roadmap/160-doctrine-review-owed/450-rule-4-cold-pass-queued-the-date-kind-rule.md`
- `docs/roadmap/260-sharing-public-since-2026-07-10-adr-0005/050-p3-the-floor-does-not-know-whether-a-repo-is-p.md`

Prior verdicts on this subject, barred until your own findings are committed (rule 2; `coldsweep`
excludes `docs/reviews/` by default): `docs/reviews/2026-09-25-0715-scratchpad-clause-cold.md`,
`docs/reviews/2026-10-03-0357-date-kind-rule-cold.md`. The delta's docstrings, comments, ADR text,
`tools/README.md` and `CHANGELOG.md` entries carry the author's account of why; they are the delta,
and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1180-rule-4-cold-pass-queued-review-notes-date-kind-and-visibility.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/380-rule-4-cold-pass-queued-the-scratchpad-clause.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/450-rule-4-cold-pass-queued-the-date-kind-rule.md \
  --also-exclude docs/roadmap/260-sharing-public-since-2026-07-10-adr-0005/050-p3-the-floor-does-not-know-whether-a-repo-is-p.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, any orchestrator, what you read, the UTC day you ran on),
per-lens answers, V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (each of the four commits: read body-free
yes/no, findings by id), findings with stable ids (prefix `RNV`: `RNV1`, `RNV2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands and results, children by count only) and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta commits' bodies;
append `### Reconcile` beneath your verdict: per-finding notes against the sibling's questions and
the author's account, any finding formed at reconcile marked as such, and the overall line restated.
Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

Every finding on this delta is the principal's to decide (rule 3): record all, apply nothing.
Counsel per finding is welcome, labelled as counsel and kept beneath it.

