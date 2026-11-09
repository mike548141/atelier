# Cold pass — seven propagation additions the principal approved in one list

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (self-authored doctrine; one
change is to the floor block every child copies).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** BRIEF ONLY. Not run. Held for the principal's explicit approval of the Fable pass.
Written 2026-11-09 UTC by session `d16dc612`, a headless Opus 5.5 brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/1160-rule-4-cold-pass-queued-propagation-doctrine-batch.md`
(barred until phase 2).
**Size:** medium: seven commits, wording only, with a worked-example sweep across nine files and a
change to the stamped floor block; no code.
**Why it earns a review:** Propagation doctrine sets what a child owes the parent and what crosses
between repos, and this repo is public. The worst failure is a route that carries private matter to
a public target, or a floor-block change that strands children.

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
  the sibling, by count here: a held-back sibling with one pointer block, 2 questions and 2 facts.

## The acceptance test

*"Approve all 20"*, on 2026-11-09, after reading a one-line summary of each of twenty items,
approving the recommendation on each. The recommendation approved, item by item:
- `320/380`: accept both: "is ever made public", and one sentence that spelling the actual path in a
  public-candidate repo defeats the rule.
- `320/330`: public doctrine names no private child repo in worked examples.
- `310/020`: convention now (a dated pending-upstream marker in every child), tool later.
- `390/010`: atelier does not model consumer or subject-cluster relationships; one generic line
  points at the estate root's registry.
- `310/120`, `310/140`: a general child-to-any-parent route, drafted as one rule; a PR between repos
  carries the filed idea, not the fix; redaction keyed on the target's visibility; an issue where
  there is no write access; a private parent may receive specifics.
- `320/580`: commission a class-only "Splitting a repo" method section, the children's records
  supplied privately.

The offered option's words were written by the authoring session and put to the principal; the
quoted pick is his. Recorded as an answer, not a ruling in his words: where the delta's wording goes
past what he picked, say so. These are claims to test, not settled scope.

## What the work is

Seven commits on `main`, wording only: six additions and a changelog commit. One (`d57ba4cc`)
changes the canonical floor region and the template's stamped copy.

Commits on `main`: `d57ba4cc`, `9c8cb7e7`, `cb742b46`, `4dcdcecf`, `3f3cf5be`, `9ff7f778`,
`38aab8b1`. The landing commit is `38aab8b1`. **Check your tree has it before reading anything:**
`git merge-base --is-ancestor 38aab8b1 HEAD` exits 0, and an orchestrator merges `origin/main` into
the review branch before it spawns.

Delta paths: `docs/method/PROPAGATION.md`, `docs/build/templates/CLAUDE.md`,
`docs/build/REPO-BOUNDARY.md`, `docs/build/README.md`, `docs/method/00-APEX.md`,
`docs/method/CONCURRENCY.md`, `docs/method/ECONOMICS.md`, `docs/method/EVIDENCE.md`,
`docs/method/RECORD.md`, `docs/method/REVIEW.md`, `docs/method/SIGNING.md`, `CHANGELOG.md`. Read
each at HEAD and read each commit body-free, scoped to paths so board records stay barred:

```
python3 tools/coldsweep.py --root . --commit d57ba4cc --path docs/build/templates/CLAUDE.md --path docs/method/PROPAGATION.md
python3 tools/coldsweep.py --root . --commit 9c8cb7e7 --path docs/build/README.md --path docs/method/00-APEX.md --path docs/method/CONCURRENCY.md --path docs/method/ECONOMICS.md --path docs/method/EVIDENCE.md --path docs/method/PROPAGATION.md --path docs/method/RECORD.md --path docs/method/REVIEW.md --path docs/method/SIGNING.md
python3 tools/coldsweep.py --root . --commit cb742b46 --path docs/method/PROPAGATION.md
python3 tools/coldsweep.py --root . --commit 4dcdcecf --path docs/method/PROPAGATION.md
python3 tools/coldsweep.py --root . --commit 3f3cf5be --path docs/method/PROPAGATION.md
python3 tools/coldsweep.py --root . --commit 9ff7f778 --path docs/build/REPO-BOUNDARY.md
python3 tools/coldsweep.py --root . --commit 38aab8b1 --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Commits since the delta on these paths:

```
git log --oneline 38aab8b1..HEAD -- docs/method/PROPAGATION.md docs/build/templates/CLAUDE.md docs/build/REPO-BOUNDARY.md docs/build/README.md docs/method/00-APEX.md docs/method/CONCURRENCY.md docs/method/ECONOMICS.md docs/method/EVIDENCE.md docs/method/RECORD.md docs/method/REVIEW.md docs/method/SIGNING.md CHANGELOG.md
```

At `457615cc` this printed 10 commit(s). Read anything new the same way.

**Claims the work makes (extracted from its own changelog entry and files, not evaluated):**

- The estate-resources bullet reads "is public, or is ever made public", with one sentence on
  spelling the actual path; the canonical region and the template's stamped copy change together;
  children's copies update at their next pin bump.
- `PROPAGATION.md` § *The route* rule 2 reaches doctrine's own prose; worked examples in eight
  method files and the build README say "a private child"; acts done to a repo and the extraction
  origin's provenance citations are left, pending his word.
- `Pending upstream:` is a greppable marker with an ISO date and the parent item or `unfiled`; the
  enumerator is not built.
- `PROPAGATION.md` models only parent and child, with one generic line pointing other relationships
  at the estate root's registry.
- `PROPAGATION.md` § *The same route between any two repos*: a PR files an idea and never the fix,
  redaction keys on the target's visibility, an issue where there is no write access; how the target
  learns a PR arrived is undecided.
- `REPO-BOUNDARY.md` carries a draft § *Splitting a repo* from one hand-up's testimony, with what
  could not be grounded listed.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** the tool that would enumerate pending-upstream markers and the fleet's pin bumps,
except where a claim depends on them.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself, first, and damage each
with a probe or confirm it by re-driving. Ask whether this is the right problem, solved at the right
altitude.
2. **Correctness & quality** — does the work do what its claims above say; honest about done versus
stubbed; any overclaim or silent scope cut, each recorded against the text that makes it.
3. **Completeness / harvest** — every surface that states the rule (V3), one home (V4), no
contradiction with sibling doctrine (V5), tests that would stay green on a broken check, what
already exists that this ignored.
4. **Security & privacy** — mandatory. This delta sets what may cross into a public repo and how.
Weigh the route for leakage at the altitude of its rules. Quote no private child's name or path,
including any found by sweeping history. No code changed, so `/security-review` has nothing to read:
discharge it in one line.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-09 UTC, from the worktree root
at `457615cc`; results are in the sibling. Read exit codes explicitly. Check `uptime` first and run
heavy lines under `nice -n 10`. Python is the `python3` on `PATH` (the tests need 3.10 or later;
`/usr/bin/python3` is 3.9 on this machine and some modules fail at import).

- `nice -n 10 python3 tools/floor.py --plane ci --root .`

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
(`2026-11-09-0153-propagation-doctrine-batch-cold.deferred.md`), every delta commit's message body,
the queue pointer
`docs/roadmap/160-doctrine-review-owed/1160-rule-4-cold-pass-queued-propagation-doctrine-batch.md`,
and the intent records beyond their titles:

- `docs/roadmap/310-pointing-up-the-child-to-parent-route/020-nothing-enumerates-what-the-estate-owes-the-house.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/380-the-floor-s-public-tense-and-whether-it-should-name-the-root.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/330-does-the-naming-precedence-reach-doctrines-own-prose.md`
- `docs/roadmap/390-repo-relationships-beyond-the-tree-mike-comm/010-consumer-and-subject-cluster-relationships-have-no-model.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/580-missing-house-rule-splitting-a-repo-has-no-method.md`
- `docs/roadmap/310-pointing-up-the-child-to-parent-route/120-the-route-is-atelier-specific-any-parent-repo-needs-one.md`
- `docs/roadmap/310-pointing-up-the-child-to-parent-route/140-a-pr-as-the-carrier-between-any-two-repos.md`

The delta's docstrings, comments, ADR text, `tools/README.md` and `CHANGELOG.md` entries carry the
author's account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1160-rule-4-cold-pass-queued-propagation-doctrine-batch.md \
  --also-exclude docs/roadmap/310-pointing-up-the-child-to-parent-route/020-nothing-enumerates-what-the-estate-owes-the-house.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/380-the-floor-s-public-tense-and-whether-it-should-name-the-root.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/330-does-the-naming-precedence-reach-doctrines-own-prose.md \
  --also-exclude docs/roadmap/390-repo-relationships-beyond-the-tree-mike-comm/010-consumer-and-subject-cluster-relationships-have-no-model.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/580-missing-house-rule-splitting-a-repo-has-no-method.md \
  --also-exclude docs/roadmap/310-pointing-up-the-child-to-parent-route/120-the-route-is-atelier-specific-any-parent-repo-needs-one.md \
  --also-exclude docs/roadmap/310-pointing-up-the-child-to-parent-route/140-a-pr-as-the-carrier-between-any-two-repos.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, any orchestrator, what you read, the UTC day you ran on),
per-lens answers, V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (each of the seven commits: read body-free
yes/no, findings by id), findings with stable ids (prefix `PRB`: `PRB1`, `PRB2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands and results, children by count only) and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta commits' bodies;
append `### Reconcile` beneath your verdict: per-finding notes against the sibling's questions and
the author's account, any finding formed at reconcile marked as such, and the overall line restated.
Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

Every finding on this delta is the principal's to decide (rule 3): record all, apply nothing.
Counsel per finding is welcome, labelled as counsel and kept beneath it.

