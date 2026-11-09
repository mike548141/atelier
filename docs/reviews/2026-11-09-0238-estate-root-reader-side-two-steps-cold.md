# Cold pass — the estate root as an ordinary private repo, independence fixed at the reader, the account before the device

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (a rule, a template
and a tool that fixes how reviewers read are doctrine by function, rule 3).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** BRIEF ONLY, not run. Written 2026-11-09 UTC by session `9bb1b984`, a headless Opus 5.5
brief-writer. The pass is held for the principal's explicit approval of Fable work; this brief is
not that approval.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/1210-rule-4-cold-pass-queued-estate-root-reviewer-side-two-steps.md`.
**Size of this pass:** medium: about 670 changed lines, half of them `tools/coldsweep.py` and its
tests, the rest doctrine across eleven files, three stamped or mirrored.
**Why it earns a review:** The delta withdraws a boundary rule, moves a review-independence duty
from every writer to one reader, and changes the rule for every ask put to the principal. Each of
those propagates to every child. The worst failure is a reviewer who believes it is cold and is
not, with the record saying it was.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `722ac2e2`,
  2026-11-09, in its ruling round, and the Sonnet worker it dispatched for each commit (per the
  queue pointer). The author queued this pass and does not take it.
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
  IDs) of `020/050`, `160/910`, `160/930`, `160/270`; the `MAJOR` and answer lines of `020/030`;
  every delta commit body-free through `tools/coldsweep.py --commit`, `e76250cf` whole, the others
  by their prose hunks; commit subjects through `git log`;
  `docs/reviews/2026-11-09-0207-leakscan-off-rules-cold.md` whole (an unrun brief, read for house
  form). It opened **no prior verdict and no delta commit's message body**. Its harness also loaded
  user-level and repo instruction files and a memory index, which hold private context this brief
  does not carry. Everything evaluative it formed is in the sibling.

## The acceptance test

The principal's answers, printed by these lines. They are labels of options he picked; the option
text around them is the author's and is barred until phase 2.

```
grep -o '"Treat like any private repo"' \
  docs/roadmap/020-policy-as-code-programme-five-tracks-mik/050-the-join-c5-guards-was-written-twice-more-on-2.md
grep -o '"Fix the reviewer.s side"' \
  docs/roadmap/160-doctrine-review-owed/910-rule-4-cold-pass-queued-deferral-side-doors.md
grep -o '"Always, as two steps"' \
  docs/roadmap/160-doctrine-review-owed/270-rule-4-cold-pass-queued-decision-asks.md
```

All three are recorded as answers, not rulings in his own words. `docs/method/REVIEW.md` rule 2,
*the reviewer's start-up reading*, `docs/method/RECORD.md` § *The record is public* and
`docs/method/COMMUNICATION.md` § *Asking for a ruling* state what the delta takes them to authorise.
Those are the author's claims to test.

## What the work is

Three commits on `main`, landed 2026-11-09:

- **`e76250cf`** — `method: the estate-root repo is named like any private repo (020/050, 020/030)`.
- **`0ba1ba03`** — `method: an ask's account always arrives as its own message, before the device (160/270)`.
- **`47e8345f`** — `review: independence is fixed at the reader; coldsweep --commit defaults to the safe view (160/910, 160/930)`.

Delta paths, read at each commit and at HEAD:

- `docs/method/PROPAGATION.md`, `RECORD.md`, `REVIEW.md`, `COMMUNICATION.md`, `00-APEX.md`,
  `TOOLBOX.md`, `AUTONOMY.md`, `GUARDS.md` (all under `docs/method/`)
- `docs/build/templates/CLAUDE.md`, `CLAUDE.md`, `skills/review-brief/SKILL.md`
- `tools/coldsweep.py`, `tools/test_coldsweep.py`, `tools/README.md`
- `docs/decisions/2026-08-05-1233-estate-internal-context-in-public-records.md` (a dated correction)
- `CHANGELOG.md`

`tools/README.md` is outside the pointer's path list and inside `47e8345f`, so it is named here.
`e76250cf` also edits two board files the default read leaves out:
`docs/roadmap/020-policy-as-code-programme-five-tracks-mik/250-the-cost-to-weigh-honestly-because-it-is-what.md`
and `docs/roadmap/110-estate-duplication-exception-audit-mike/README.md`. They are outside the
pointer's path list. Name one with `--path` only if your own judgement needs it, and disclose that
you did.

First confirm the tree holds the delta, then read each commit body-free:

```
git merge-base --is-ancestor 47e8345f HEAD; echo $?
python3 tools/coldsweep.py --root . --commit e76250cf
python3 tools/coldsweep.py --root . --commit 0ba1ba03
python3 tools/coldsweep.py --root . --commit 47e8345f
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). `tools/coldsweep.py --commit` is itself part of this delta. With no `--path` it leaves the board
store out, so the three lines above never show the intent records.

Then see what has landed on those paths since, and read anything new the same way, only as far as
it bears on this delta at HEAD:

```
git log --oneline 47e8345f..HEAD -- docs/method/PROPAGATION.md docs/method/RECORD.md \
  docs/method/REVIEW.md docs/method/COMMUNICATION.md docs/method/00-APEX.md docs/method/TOOLBOX.md \
  docs/method/AUTONOMY.md docs/method/GUARDS.md docs/build/templates/CLAUDE.md CLAUDE.md \
  skills/review-brief/SKILL.md tools/coldsweep.py tools/test_coldsweep.py tools/README.md
```

**This is an application review.** Rule 2 cannot be fully honoured: the delta's `CHANGELOG.md`
entries and commit subjects carry finding IDs and decision stamps from the passes it applies (DS,
BF, DR, C5R, RR, CH). Review the edited doctrine at HEAD and commit findings first; open those
verdicts after. The residual exposure is named here, not denied (`REVIEW.md` § *Applying decisions
to doctrine*).

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- The estate root "is a private repo like any other: it may be named, in a private or a public
  tree, and what it holds and the condition it is in go by type only in a public record"
  (`PROPAGATION.md`).
- "The name is in pushed history for good either way, so the harm was never the name; it was the
  name beside what the repo holds, and that join stays barred."
- The withdrawal is "forward only" and "the idea of putting the name on the leak scanner's term
  list is dropped with the rule".
- `TOOLBOX.md` and `AUTONOMY.md` "no longer lean on the old rule"; the floor bullet's template copy
  is "kept identical".
- The account "always goes in a finished message of its own, ahead of the device, in every view;
  that message ends its turn, and the device opens the next and carries the choice alone", at "one
  extra turn on every ask" (`COMMUNICATION.md`); "a session cannot see which display mode the
  principal's harness is in".
- A cold reviewer "skips the session-log step" (`CLAUDE.md` step 4, the child template's step 3),
  "whatever its spawn prompt says, and its spawn prompt and the brief say so too".
- The writer-side duty is withdrawn "because it bound writers by role, and no check could see
  whether it was kept"; the fix "cannot be forgotten by a writer".
- The channels listed as "accepted, not closed" and "also accepted" are the whole of what remains
  (`REVIEW.md` rule 2).
- The three recorded occurrences (2026-08-02, 2026-08-17, 2026-10-18) ground the fix.
- `coldsweep --commit` prints "the message's first line only", leaves the board store out with no
  `--path`, exits 1 when nothing is in scope, refuses a `--root` below the repository top and a
  shallow clone's boundary commit (`tools/README.md`).
- "`coldsweep` is not a floor check: no repo's build changes" (`CHANGELOG.md`).

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope,
and a non-goal that fences off the risk is a finding.

**Non-goals:** the thirteen-fix list (pass `160/1220`), including `db8c44b7`'s later hunks on
`REVIEW.md` and the skill; `DR2`, the floor's confirm bullet, which the delta says is routed to
other work; whether the principal's three picks were the right ones, as distinct from whether the
delta does what they authorised.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Is
   this the right problem, solved at the right altitude and in the right shape, against the
   acceptance test?
2. **Correctness & quality.** Re-drive the claims above. Record each overclaim against the text that
   makes it.
3. **Completeness / harvest.** Every surface that states these behaviours (V3); one home (V4); no
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
python3 tools/coldsweep.py --selftest
cd tools && python3 -m unittest test_coldsweep test_templates; cd ..
python3 tools/floor.py --plane ci --root .
nice -n 10 python3 -m unittest discover -s tools
```

`PROPAGATION.md` keeps a measurement ("63 times across 19 files … 2026-07-28") and the `CHANGELOG.md`
entries record proofs. Any such figure you rely on is a recorded proof (V2): re-run it read-only and
by count. The brief-writer did not re-run those.

## House rules for this run

- **Live systems:** read-only reads of live systems as needed; no live writes. A check that needs a
  write is marked NOT RUN, with why. No push, no write to GitHub, no network service changed.
- **Never print a secret** or any personal data. Probes use scratch copies and synthetic fixtures
  under your scratchpad, deleted when you finish.
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
  PUBLIC: quote no secret, email address, private repo name or path, and do not join the estate
  root's name to what it holds.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, this brief's sibling
`docs/reviews/2026-11-09-0238-estate-root-reader-side-two-steps-cold.deferred.md` (a held-back file;
by count: 16 questions, 3 facts), every other item under `docs/roadmap/160-doctrine-review-owed/`
beyond its title, every delta commit's message body, and these intent records beyond their first
line:

- `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/050-the-join-c5-guards-was-written-twice-more-on-2.md`
- `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/030-c5-re-ruling-owed-the-composed-term-list-execu.md`
- `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/250-the-cost-to-weigh-honestly-because-it-is-what.md`
- `docs/roadmap/280-cross-session-channel-mike-commissioned/030-rule-4-cold-pass-queued-the-channel-section.md`

`160/910`, `160/930`, `160/270` and `160/230` are under the barred folder above. The delta's own
docstrings, comments, README and `CHANGELOG.md` entries carry the author's account of why; they are
the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/020-policy-as-code-programme-five-tracks-mik/050-the-join-c5-guards-was-written-twice-more-on-2.md \
  --also-exclude docs/roadmap/020-policy-as-code-programme-five-tracks-mik/030-c5-re-ruling-owed-the-composed-term-list-execu.md \
  --also-exclude docs/roadmap/020-policy-as-code-programme-five-tracks-mik/250-the-cost-to-weigh-honestly-because-it-is-what.md \
  --also-exclude docs/roadmap/280-cross-session-channel-mike-commissioned/030-rule-4-cold-pass-queued-the-channel-section.md \
  'estate.root|session-log step|side door|finished message of its own'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the re-run
list. Append your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, any orchestrator, what you read, the UTC day), per-lens answers, V1–V7 each
answered or discharged with grounds, each load-bearing assumption damaged or confirmed with its
probe, a per-commit ledger (read body-free yes/no, findings by id), findings with stable IDs (prefix
`RW`: `RW1`, `RW2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit bodies;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work is doctrine by function, so every finding is the principal's to decide (rule 3): record
all, apply nothing. Counsel per finding is welcome, labelled as counsel and kept beneath it.
