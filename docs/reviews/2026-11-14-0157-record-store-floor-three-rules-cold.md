# Cold pass — the floor's record-store carve-out, `/security-review` in a shared worktree, no credential at rest, solve once at both scopes

**Board:** `docs/roadmap/160-doctrine-review-owed/1280-rule-4-cold-pass-queued-record-store-floor-three-rules.md`
**Status:** BRIEF ONLY, not run. Written 2026-11-14 UTC by a headless Opus 5.5 brief-writer
(`cclive` lists it as session `b059d250`). Queued, waiting on the principal's explicit approval of
Fable work; this brief is not that approval.

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (the floor region every child
inlines, a review lens, the credential ladder and a design principle are doctrine by text and by
function, rule 3).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Size of this pass:** small to medium: one commit, 124 added and 19 removed lines, all markdown,
across six non-board files; no code. Four separate changes, each short.
**Why it earns a review:** The first change edits the always-confirm floor, the one region every
child repo inlines so it binds without reading atelier. Two failures are worst. First, a floor that
now contradicts itself, or lets a session proceed on a bulk record deletion because the wording
still files it under "recoverable": the class the change exists to close, propagating to every
child at its next pin. Second, doctrine that claims more than its grounding: a one-case credential
rung read as settled practice, a principle quoted as the principal's words when it is a paraphrase,
or a scanner caution that names a mechanism the evidence does not establish. Doctrine text is
public and binds the fleet once trusted.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `d0ca5d24`,
  2026-11-09 UTC, and the worker it dispatched (per the queue pointer). The author queued this pass
  and does not take it.
- **Who wrote this brief:** a headless brief-writer (`claude-opus-5-5`; `cclive` lists it as session
  `b059d250`), started 2026-11-14 UTC by an estate health sweep, orchestrator session `58027096`
  (Opus), on the principal's instruction that a brief is written for every review known to be
  owed (Mike, 2026-11-14, verbatim: *"include all briefs are written where we know a fable
  review is required"*). Neither wrote any of this delta. **Off-tier for review, disclosed: the
  brief-writer forms no finding and writes no severity**, and stops after writing. It ran no review
  and used no Fable model.
- **Barred from running this pass:** session `b059d250` and session `58027096` (whoever writes a
  brief does not run it), and session `d0ca5d24` with everything it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `58027096`: the
  item number, the pointer's opening sentence, and the rules of the sweep. It carried no framing of
  the work. The brief-writer had no contact with the author session or its worker.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md`; the queue pointer whole; **the four intent
  records whole**, including the author's landing notes under each (`030/130`, `160/195`,
  `060/010`, `160/170`); **the delta commit's message body**, read through plain `git show`; the
  2026-08-03 commit that queued `060/010`, whose diff printed four `docs/SESSIONS.md` index lines;
  the head of an unrelated unrun brief and the whole of the most recent brief and its sibling (read
  for house form); `CHANGELOG.md`'s entry; parts of `RECORD.md`, `AUTONOMY.md`, `REVIEW.md`,
  `PROPAGATION.md`, `PRINCIPLES.md`, `tools/blockscan_map.json` and `tools/test_templates.py` at
  HEAD. It opened **no prior verdict file**. Its harness also loaded user-level and repo
  instruction files and a memory index, which hold private context this brief does not carry.
  Everything evaluative it formed is in the sibling.

## What the work is

One commit on `main`, landed 2026-11-09 UTC (stamped 2026-11-10 NZDT):

- **`920d63f3`** — `doctrine: carve record stores out of the floor; add three grounded rules`.

Read it body-free: `python3 tools/coldsweep.py --root . --commit 920d63f3` (subject, stat and diff,
never the body; board files left out). Plain `git show` prints the body before the diff, and
reading is atomic (`REVIEW.md` rule 1), so it is barred. Check first that your tree has the delta:
`git merge-base --is-ancestor 920d63f3 HEAD` exits 0.

The four changes, read at the commit and at HEAD:

1. **The floor's record-store carve-out (`030/130`).** `docs/method/PROPAGATION.md`, the
   *Always stop and confirm (the floor)* bullet inside the `floor:begin` / `floor:end` region, and
   the same bullet in `docs/build/templates/CLAUDE.md`, the stamped copy every child holds. The
   confirm list gains bulk deletion from a record store; the closing clause becomes "Everything
   else recoverable".
2. **`/security-review` in a shared worktree (`160/195`).** `docs/method/REVIEW.md`, lens 4's reach
   paragraph (*The four lenses*, item 4): the new sentences from "One shape defeats the first
   caution" to "disclose any exposure in the verdict".
3. **No credential at rest (`060/010`).** `docs/method/SECRETS.md` § *The credential triad*, the two
   new paragraphs; `docs/method/PRINCIPLES.md` §5 (the case sentence) and the checklist line
   "Used only rarely?".
4. **Solve once at both scopes (`160/170`).** `docs/method/PRINCIPLES.md` §8, the new bullet.

Plus the `CHANGELOG.md` entry for all four.

**The files have moved since, not the regions.** Three later commits touch these files:
`2a6d7a41` changes the *Asking* bullet in the same floor region and template (pass `160/1440`'s
subject), and `55c7d409` and `dd3d60d4` change other parts of `REVIEW.md`. None of the three
touches the four regions above. Judge this delta's text as it stands at HEAD.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- The floor: bulk deletion from a record store is always-confirm, "meaning the roadmap, session
  logs, ADRs or reviews, whoever wrote it, shown first because recoverable bytes are the wrong
  test there"; and "Everything else recoverable — commit/push/PR included — just proceed".
- The canonical region and the stamped template carry the same text, and "No child is changed by
  this: each takes it at its next pin" (`CHANGELOG.md`).
- Lens 4: "`/security-review` reads the session's pending diff, not a path it is aimed at"; in a
  shared worktree "pending" means every session's uncommitted work; three reviewers in one batch
  (2026-08-15) each scanned the shared tree; so "run the scanner only where the worktree is
  verifiably clean at the moment of aiming, else discharge it in one line with grounds".
- Secrets: the next rung is "no credential at rest", "in Mike's words, captured 2026-08-03", quoted;
  it "sits below the triad … and above a standing credential"; "*tested* is a condition of the
  rung"; the minting credential "stays a tracked debt" and the rotation cadence "then bounds that
  credential, since a deleted one has no exposure window left to bound"; rehearsal cadence and the
  frequency boundary "are open until a second instance"; "This is a one-case claim."
- Principles §8: "Mike's principle (2026-07-25, captured in paraphrase)"; the three flows are "all
  in `PROPAGATION.md`" under the named sections; "the up and down flows are practised … the lateral
  route is the youngest, written 2026-11-09".
- `CHANGELOG.md`: "Doctrine wording only; no scanner or tool changes", and its summary of each part.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs and real-world behaviour.
There is no code, but the floor region is checked by code (`tools/test_templates.py`,
`tools/stampscan.py`, `tools/blockscan.py` with `tools/blockscan_map.json`), and whether those
checks hold the new clause is in scope. The lenses organise the scope; they do not bound it.
Anything not named a non-goal is in scope, and a non-goal that fences off the risk is a finding.

**Non-goals:** the *Asking* bullet and anything `2a6d7a41` changed (pass `160/1440`); whether the
principal's 2026-08-04 record-store ruling, his 2026-08-03 capture or his 2026-07-25 principle were
the right calls, as distinct from whether the delta states and applies them faithfully; rolling
the new floor into any child (each takes it at its next pin; no child is changed here);
`160/150` and `160/160`, which the `160/170` work leaves open.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else.
   Is a clause in the confirm list the right fix for the floor contradiction, against the
   alternatives the intent record names? Does the floor now say what `RECORD.md` and `AUTONOMY.md`
   rule (show-first, "or ask") or something stricter or looser? Is a wording rule the right answer
   to a scanner that cannot be aimed, rather than a mechanical guard? Is the credential rung
   grounded enough to be a rung, and is the solve-once bullet a principle or a restatement?
2. **Correctness & quality.** Re-drive each claim above against its grounding: every quote against
   its source, character for character; every date against the commit or record it cites; every
   section pointer resolves to what it says. Read the floor bullet as one sentence: does each
   clause still parse, and does anything in it contradict the new entry? Record each overclaim
   against the text that makes it.
3. **Completeness / harvest.** Every surface that states the floor, the record-store rule, the
   scanner caution, the credential ladder or one-source (V3): the floor region and template;
   `RECORD.md`, `AUTONOMY.md`, `00-APEX.md`; `skills/review-brief/SKILL.md` and
   `skills/session-onramp/SKILL.md`; `CONCURRENCY.md`; `PRINCIPLES.md` §5 and §2, `EVIDENCE.md` §9;
   `GLOSSARY.md`; the blockscan map's sources for the floor bullet. One home (V4); no contradiction
   (V5).
4. **Security & privacy**, mandatory: at design altitude, whether the new credential rung, as
   written, could lead a session to delete a credential it cannot rebuild, or to leave the minting
   credential less watched; whether the floor change could let a destructive act through under the
   new "else"; whether any line lets a reader infer which child, platform or tool grounds the
   one-case claim or the solve-once example; and whether anything falls outside
   `docs/PERSONAL-DATA.md`'s closed list. Code altitude: there is no code in the delta; discharge
   `/security-review` in one line with grounds (it excludes markdown, so a clean pass is empty, and
   this pass is itself the shape lens 4 now warns about if your worktree is shared).

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-14 UTC, from the worktree root
(the two `unittest` lines from `tools/`), and its results are held in the sibling. Read exit codes
explicitly. Check `uptime` first and run the floor line under `nice -n 10`, alone. Use the `python3`
first on the machine's `PATH` (3.14.6 when written); CI pins 3.12.

```
git merge-base --is-ancestor 920d63f3 HEAD; echo $?
python3 tools/coldsweep.py --selftest; echo $?
python3 tools/coldsweep.py --root . --commit 920d63f3 > /dev/null; echo $?
cd tools && python3 -m unittest test_templates; echo $?; cd ..
cd tools && python3 -m unittest test_blockscan; echo $?; cd ..
python3 tools/blockscan.py --root . .; echo $?
nice -n 10 python3 tools/floor.py --plane ci --root .; echo $?
```

The delta's recorded facts are recorded proofs (V2): the 2026-08-03 capture date and the quoted
words (against `git log -S` on the quote), the 2026-07-25 principle date, the 2026-08-04 ruling
date `RECORD.md` cites, the three 2026-08-15 reproductions (against the verdict files the intent
record names: read them in phase 2 only, see *Deferred reading*), the lateral route's 2026-11-09
date (against `git log -S` on its heading), and "no scanner or tool changes" (against the commit's
stat). Re-check each by the cheapest read-only route and say which you could not re-run and why.

## House rules for this run

- **Live systems:** none is needed. No live writes, no push, no write to GitHub, no network service
  changed, no credential touched. A check that would need one is marked NOT RUN, with why.
- Never read a child repo, and never read a session transcript's content. Never print personal
  data or a secret value.
- Name your own review worktree in the verdict. It is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad.
- **Skip the session-log step of the read order** (`CLAUDE.md` step 4; `REVIEW.md` rule 2). If you
  read it anyway, disclose what you met.
- One heavy process at a time, foreground, with a long timeout. Never run an installed tool by bare
  name from `PATH`: use `python3 tools/<x>.py` from your worktree.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo is
  PUBLIC: quote no secret, email address, private repo name or path, and name no child repo.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/` (including the three 2026-08-15 verdicts lens 4 cites), this brief's
sibling `docs/reviews/2026-11-14-0157-record-store-floor-three-rules-cold.deferred.md` (a held-back
file; by count: 15 questions, 8 facts), every commit's message body, and these records beyond their
first bold title sentence:

- `docs/roadmap/030-enforcement-propagation-the-estate-rollo/130-the-floor-says-everything-recoverable-just-pro.md`
- `docs/roadmap/160-doctrine-review-owed/195-security-review-reads-the-worktree-not-the-target.md`
- `docs/roadmap/060-a-fourth-rung-for-the-credential-ladder/010-extend-the-credential-preference-ladder-so-the.md`
- `docs/roadmap/160-doctrine-review-owed/170-principle-solve-once-reuse-the-building-block.md`
- every other item under `docs/roadmap/160-doctrine-review-owed/`

The intent records' bodies hold the evidence base and the open questions, but also the author's
landing notes; they are read whole in phase 2. The principal's quoted words in `060/010` and the
date in `160/170` are re-checked in phase 1 by `git log -S` and `git show <sha> --format=`, which
print the diff without the body. The delta's own `CHANGELOG.md` entry and doctrine text carry the
author's account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/030-enforcement-propagation-the-estate-rollo/130-the-floor-says-everything-recoverable-just-pro.md \
  --also-exclude docs/roadmap/060-a-fourth-rung-for-the-credential-ladder/010-extend-the-credential-preference-ladder-so-the.md \
  'record store|recoverable|pending diff|credential at rest|solve once'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the re-run
list. Append your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, any orchestrator, what you read, the UTC day), per-lens answers, V1–V7 each
answered or discharged with grounds, each load-bearing assumption damaged or confirmed with its
probe, a per-claim ledger, findings with stable IDs (prefix `RC`: `RC1`, `RC2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger and a follow-up checklist. Then STOP: act 1 is committed, unrevised, **before** the
sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit body;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work is doctrine by function, so every finding is the principal's to decide (rule 3): record
all, apply nothing. Counsel per finding is welcome, labelled as counsel and kept beneath it.
