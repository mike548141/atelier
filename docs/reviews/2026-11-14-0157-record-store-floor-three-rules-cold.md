# Cold pass — the floor's record-store carve-out, `/security-review` in a shared worktree, no credential at rest, solve once at both scopes

**Board:** `docs/roadmap/160-doctrine-review-owed/1280-rule-4-cold-pass-queued-record-store-floor-three-rules.md`
**Status:** PASS RAN 2026-11-22 UTC — PASS-WITH-FINDINGS (1 MAJOR, 2 MODERATE, 3 minor,
2 notes); act 1 committed as `dc9a0a78` before the sibling opened, act 2 reconciled below, and
the sibling folded below the verdict. Reviewer: Fable 5.1 under the principal's 2026-11-23 NZDT
drain order, run by orchestrator session `60287c5a` for drain session `eca14b23`. Brief written
2026-11-14 UTC by a headless Opus 5.5 brief-writer (`cclive` lists it as session `b059d250`).

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
sibling (a held-back file, now folded below the verdict; by count: 15 questions, 8 facts), every
commit's message body, and these records beyond their first bold title sentence:

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

---

# Verdict — act 1 (2026-11-22 UTC)

**Overall: PASS-WITH-FINDINGS — 1 MAJOR (RC1), 2 MODERATE (RC2, RC3), 2 minor (RC4, RC5),
2 notes (RC6, RC7).** The delta does what its four parts set out to do, and its quotes and
pointers hold; the MAJOR is that the floor's new confirm-list entry has no home in the list
`00-APEX.md` names as the one home, so the parent and its children now read the same act two ways.
Per `REVIEW.md` § *Applying decisions to doctrine*, a MAJOR keeps the cycle open. Every finding is
the principal's to decide (rule 3); counsel is labelled and sits beneath each.

## Provenance (rule 4, V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named tier, checked at selection.
  Spawned by headless per-pass orchestrator session `60287c5a` (Opus 5.5), itself started by drain
  session `eca14b23` (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold the context
  partition, form no finding and write no severity. Neither wrote the brief or the delta, and
  drain session `eca14b23` started no brief-writer. I was not started or instructed by any barred
  session (`b059d250`, `58027096`, `d0ca5d24` or anything it started). No contact from the author
  or the brief-writer reached me.
- **Authority:** the principal's weekly Fable drain order of 2026-11-23 NZDT, verbatim: *"Start a
  fable drain or whatever it is called now. Target 100% of weekly budget by 11.30am NZT todat"*
  (his spelling, verbatim). It lapses at the reset (2026-11-22T23:00Z); a pass running then may
  finish.
- **Spawn prompt, as received (process only):** worktree path, brief path, the partition (the
  sibling removed from my tree, its deletion left unstaged; no history, other checkouts or
  scratch reads), what I may write (this file below the divider and the Status line; a running
  review log outside the repo, appended verbatim at the fold), no commit/push/live write, load
  rules (one suite at a time under `nice -n 10`), public-repo naming rules, and the finish shape.
  It carried no question about the delta, no pointer to where risk lives and no request about any
  finding. The release message for act 2 will be recorded in § *Reconcile*.
- **Review worktree:** `/Users/mike/worktrees/fable/atelier-160-1280-2009/atelier`, detached at
  `c4bc074b`. `git status` showed only the expected unstaged deletion of the sibling.
- **What I read, in order:** this brief whole; `docs/method/REVIEW.md` whole; the delta body-free
  (`coldsweep --commit 920d63f3`); the floor region and template at HEAD; `RECORD.md` 440-465;
  `AUTONOMY.md` 8-20, 40-168, 274-290; `00-APEX.md` 83-90; `SECRETS.md` 30-105, 310-323;
  `PRINCIPLES.md` 190-237, 265-289, 296-369, 612-630, 748; `PROPAGATION.md` headings and
  1178; `EVIDENCE.md` headings; `CONVENTIONS.md` 57-59; `GLOSSARY.md` 60-68; `CONCURRENCY.md`
  930 and 1015-1030; `skills/review-brief/SKILL.md` 94-112; `docs/build/templates/docs/reviews/
  README.md` 24-40; `tools/blockscan_map.json` 1-40; `tools/test_templates.py` grep; tool
  `--help` texts; `docs/PERSONAL-DATA.md` whole; `CHANGELOG.md` 598-616; two census records
  under `docs/method/census/` (2026-11-16, not on the barred list, read after RC1 and RC2 were
  formed); board rows `020/README` 262-270 and `300/020` 136-141 (not barred). Session-log step
  skipped (rule 2). No prior verdict opened; the five 2026-08-15 and two 2026-07-21 verdict files
  were listed by **name only**.
- **Exposure, disclosed:** the brief's authorised `git show --format= b3101c3b` grep for the
  quoted words also printed one `docs/SESSIONS.md` index line (a one-sentence account of the
  2026-08-03 queueing). It steered no finding. The coldsweep sweep printed one-line hits from
  non-barred board items; none carried an account of this delta.

## Lens 1 — approach and assumptions (named first)

- **A1 — the floor region is a copy and `AUTONOMY.md` § *Always confirm* is the list's home.**
  Confirmed: `00-APEX.md` 85-87, *"the list is `AUTONOMY.md` § Always confirm, which holds it
  once; `PROPAGATION.md`'s floor block carries the copy"*; `AUTONOMY.md` 40-42 and 154, *"this
  file is where that list lives"*. The delta edits the copy and the template only → **RC1**.
- **A2 — the 2026-08-04 ruling is show-first-or-ask, not stop-and-confirm.** Confirmed:
  `RECORD.md` 446-449 (*"either diff it and show the principal what goes, or ask. One message"*),
  `AUTONOMY.md` 280-285 (*"show what goes, or ask, before it is removed"*), and the house's own
  guard re-rank (`300/020` line 139: *"Show first, then act. The bytes are recoverable."*). The
  floor files the act under *Always stop and confirm* → **RC2**. The brief's lens-1 question is
  answered: the floor says something **stricter** than `RECORD.md` and `AUTONOMY.md`, or is
  ambiguous between the two, depending on how a reader weighs the rider against the heading.
- **A3 — a wording rule is the right answer to a scanner that cannot be aimed.** Accepted. The
  scanner is a harness command the repo cannot wrap, so no in-repo guard can refuse it; the
  verifiable precondition the delta names (a clean worktree at the moment of aiming) is the one
  control available. Where it belongs as well is the skill that writes briefs and the skill that
  spawns batches → **RC3** (counsel).
- **A4 — the credential rung is grounded enough to be a rung.** Confirmed as a labelled one-case
  claim: the quote is verbatim (ledger below), the position in the ladder is reasoned in the text,
  *tested* is made a condition, the minting credential is kept as debt, and the open questions
  are named. One design gap at the seam with the secrets floor → **RC7** (note).
- **A5 — the solve-once bullet is a principle, not a restatement.** It is mostly a restatement
  and says so (*"the bullet above and one-source … already hold it"*); its new content is the
  cross-repo reading through the three flows, each of which resolves. Honest; no finding beyond
  the date stamp → **RC5**.
- **A6 — the regions are unchanged at HEAD.** Confirmed: `git diff 920d63f3 HEAD -U0` hunk
  headers on the six files all fall outside the four regions (old lines 127-143 and 29-47 for the
  floor; 363-377 `REVIEW.md`; 79-100 `SECRETS.md`; 210-213, 313-328, 622 `PRINCIPLES.md`).
- **A7 — the floor's own checks hold the new clause.** Confirmed for the copy-equals-canonical
  test: `test_templates` 55 OK; `stampscan --require-floor-stamp` *"[identical] matches canonical
  region 'floor' (109 lines)"*. Not held for co-change with the rule's source → **RC4**.

## Lens 2 — correctness: per-claim ledger

| Claim (brief § *The claims*) | Re-driven against | Result |
|---|---|---|
| Floor: bulk record deletion is always-confirm; "Everything else recoverable" | `PROPAGATION.md` 146-162 read as one sentence | Parses; "else" excludes the listed acts, so the old contradiction is closed in the floor. Semantics vs the ruling: RC2 |
| Canonical region and template carry the same text | `stampscan`, `test_templates` | Holds (identical, 109 lines) |
| "No child is changed by this" | commit stat (`--format=`): 11 files, all in atelier | Holds |
| `/security-review` reads the pending diff, not a path | harness behaviour; cited 2026-08-15 verdicts | **Not re-run** in act 1 (read-only, no harness probe; verdicts barred). Act 2 |
| Three reviewers in one batch (2026-08-15) | `ls docs/reviews` names only: five 2026-08-15 files | Count unverified: RC6 (note), act 2 |
| Quote *"delete the credential entirely and make its rebuild cheap, automated and tested"*, captured 2026-08-03 | `git log --all -S` on two fragments → `b3101c3b` (2026-08-03T05:58Z); narrow grep of its added lines | **Holds character for character**; the source wraps across two lines, which is why a one-line `-S` on the whole sentence hits only the delta. Date holds (0557 UTC) |
| Rung "sits below the triad … above a standing credential" | `SECRETS.md` 61-100 | Reasoned in the text; consistent with § 17 (enabling property) and § 310 (rotation cadence), both of which resolve |
| "This is a one-case claim" and the open questions | `SECRETS.md` 90-100; `PRINCIPLES.md` 234 | Labelled at both sites; no second site drops the label |
| §8: "Mike's principle (2026-07-25, captured in paraphrase)" | `git log -S'2026-07-25' -- PRINCIPLES.md`: only the delta and `de1049b3` | Date **not re-checkable** from non-barred sources (`RECORD.md` 457's 2026-07-25 is a different event). Act 2 against `160/170` |
| §8: three flows "all in `PROPAGATION.md`" | headings 506, 24, 845 | Holds |
| §8: "the lateral route is the youngest, written 2026-11-09" | `git log -S` on the heading → `3f3cf5be`, 2026-11-08T14:24Z | Off by one day: NZDT date at rest: RC5 |
| `CHANGELOG.md`: "Doctrine wording only; no scanner or tool changes" | commit stat | Holds (markdown only) |
| `RECORD.md`'s 2026-08-04 ruling date | `git log -S'show-first action'` → `53785b95` "the 2026-08-04 sitting's five small edits" | Consistent |

## Lens 3 — completeness / harvest (V3, V4, V5)

Surfaces that state the floor, the record-store rule, the scanner caution, the ladder or
one-source, each checked at HEAD:

- Floor region and template: identical (above). `GLOSSARY.md` 60-62 defines *Floor*; no entry
  for *record store* (the floor and `RECORD.md` both define it by enumeration; not a finding).
- `AUTONOMY.md` § *Always confirm*: **no record-store entry** (RC1). § *The one rule* (10-13)
  and `docs/method/README.md` 14-15 still say *"proceed on anything recoverable"* with no
  carve-out: the contradiction the delta closed in the floor stands at the home (RC1 evidence).
- `00-APEX.md` 85-87: names the home the delta did not change (RC1).
- `skills/review-brief/SKILL.md` 99-106 and `docs/build/templates/docs/reviews/README.md` 30-34:
  restate lens 4's scanner guidance with the first caution only (RC3). `skills/review-drain/
  SKILL.md` and `skills/queue-run/SKILL.md`: no mention of the scanner at all (RC3 counsel).
- `PRINCIPLES.md` §5 and §2, `EVIDENCE.md` §9: consistent; the §8 bullet cites both correctly.
- `tools/blockscan_map.json` *stop-and-confirm*: sources `00-APEX.md` only (RC4).
- Cross-reference line (V5): every pointer the delta writes reaches the rule it names:
  `SECRETS.md` § *The credential triad* (61); "the enabling property above" (17); "the rotation
  cadence below" (310); `PROPAGATION.md` § *Pointing up* (506), § *The mechanism* (24), § *The
  same route between any two repos* (845); `EVIDENCE.md` §9 (121); `PRINCIPLES.md` §2 DRY (89).

## Lens 4 — security and privacy (V6)

- **Design altitude, the rung:** as written it cannot lead a session to delete a credential it
  cannot rebuild without first breaking its own condition (*"tested is a condition of the rung"*,
  `SECRETS.md` 93-94), and it keeps the minting credential watched (*"stays a tracked debt"*,
  bounded by the rotation cadence). One seam is unstated → RC7 (note).
- **Design altitude, the floor:** the new "else" lets through only acts not in the list; bulk
  record deletion is in the list, so nothing destructive newly passes. The residual risk is RC2's
  ambiguity (a reader who takes "shown first" as the whole duty acts after showing, which is what
  the ruling allows, so the risk is to consistency, not to data).
- **Inference about the one-case child or tool:** `SECRETS.md` 90-92 names no child, platform or
  tool; *"backup tool"* and *"delegation grant is standing-only"* describe a class. The §8
  example (*"a network tool handles its wire protocol in one module"*) names no repo. Discharged.
- **Personal data:** the delta adds *"Mike's words"* and *"Mike's principle"*: the first name in
  the house's standing form; `pdlistscan` clean in the floor run. Nothing outside
  `docs/PERSONAL-DATA.md`'s closed list.
- **Code altitude:** no code in the delta. `/security-review` **NOT RUN**: it excludes markdown,
  so a clean pass would be empty, and my worktree carries a pending diff (this verdict, the
  sibling's deletion), the exact shape the delta's caution names. Discharged on those grounds.

## Findings

Severities: MAJOR / MODERATE / minor / note. All are the principal's to decide.

### RC1 — MAJOR · the floor's new entry is absent from the list APEX names as its home (V3–V5)

`00-APEX.md` 85-87 says the always-confirm list *"is `AUTONOMY.md` § Always confirm, which holds
it once; `PROPAGATION.md`'s floor block carries the copy"*. The delta adds *bulk deletion from a
record store* to the copy (`PROPAGATION.md` 147-150, template 33-36) and not to the home:
`AUTONOMY.md` § *Always confirm* (44-146) has no such entry; the rule sits under § *Before you
destroy or overwrite* (280-285) as a show-first act, and § *The one rule* (10-13) still reads
*"Proceed on anything recoverable"* with no carve-out, as does `docs/method/README.md` 14-15. The
floor is the region every child inlines, so a child reads the act as a floor stop while an atelier
session consulting the named home reads it as show-then-act. The 2026-11-16 census record
(`docs/method/census/2026-11-16-1204-apex-autonomy-guards-propagation.md` 347-351) states the same
gap independently: *"The 'one list' of always-confirm stops is two lists."* The delta's own
`CHANGELOG.md` line says *"`PROPAGATION.md` and the template change together"*; the home was not
in the sweep. MAJOR because the surface is the floor, the two statements now disagree on the
strength of the duty, and V4's rule (`EVIDENCE.md` §9; `PROPAGATION.md` § *One statement, stamped
copies*) is the one the delta's own §8 bullet invokes.

*Counsel:* decide RC2 first, then write the entry once at the home in the words that decision
gives, re-derive the floor copy from it, and sweep § *The one rule* and `docs/method/README.md`
14-15 for the carve-out. Map the home as a blockscan source (RC4) so the next drift is caught.

### RC2 — MODERATE · confirm vs show-first: the floor says more than the ruling, or two things

The floor lists the act under *"Always stop and confirm (the floor)"* with the rider *"shown first
because recoverable bytes are the wrong test there"*. The ruling as recorded is show-first **or**
ask, one message, then act (`RECORD.md` 446-449; `AUTONOMY.md` 280-285; the house's own reading
in `300/020` line 139, *"Show first, then act."*). Position in the list makes the act a floor
stop, to which `00-APEX.md` 112-118 attaches re-briefing before the act and the principal's
confirmation; the rider says showing is the duty. A reader can take either. If the floor means
confirm, it is stricter than the ruling and the two homes contradict; if it means show-first, the
list heading mis-describes its own member. Neither is said.

*Counsel:* one ruling settles it. If show-first stands, the clause belongs in its own sentence
after the list (*"One act is show-first rather than confirm: …"*) so the heading stays true. If
the principal upgrades it to confirm, `RECORD.md`, `AUTONOMY.md` and `300/020` record the upgrade
in his words.

### RC3 — MODERATE · the shared-worktree scanner caution has no mirror where briefs are written

`REVIEW.md` lens 4 now carries two cautions. `skills/review-brief/SKILL.md` 99-106 and
`docs/build/templates/docs/reviews/README.md` 30-34 restate the lens with the first caution only
(*"never run it over a brief carrying deferred material"*); neither says the scanner reads the
session's pending diff or that a shared worktree must be verifiably clean. `PRINCIPLES.md` §6
277-287 names `skills/` and the templates as sweep surfaces. The brief-writer works from the
skill, so the next brief tells a reviewer to *"aim it at the in-scope diff"* in a batch where
aiming does nothing. `skills/review-drain/SKILL.md`, which spawns the very shape the caution
names, does not mention the scanner.

*Counsel:* one sentence in the skill and the template beside the first caution; and the
review-drain skill's spawn prompt says whether the worktree is per-reviewer, so the reviewer knows
which case it is in before it aims anything.

### RC4 — minor · the co-change guard cannot see the new clause's source (lens 3, in scope)

`tools/blockscan_map.json` 21-27 sources the *stop-and-confirm* bullet to `00-APEX.md` § *The
principal's authority is absolute* only. Neither `AUTONOMY.md` § *Always confirm* (the named home)
nor `RECORD.md` § *The roadmap — one file per item, a generated index* (the heading above the
record-store rule, line 408) is mapped, so a change to the rule at either source raises no
co-change warning for the floor. The delta added the clause without adding its source; the shape
pre-dates it. `blockscan` and `test_blockscan` pass (exit 0) because the map resolves; the gap is
coverage, not breakage.

*Counsel:* add both headings as sources of the *stop-and-confirm* entry.

### RC5 — minor · a local date at rest (V1, `CONVENTIONS.md`)

`PRINCIPLES.md` 369: *"the lateral route is the youngest, written 2026-11-09"*. The commit that
wrote § *The same route between any two repos* is `3f3cf5be`, authored 2026-11-09T03:24+13:00,
which is **2026-11-08** UTC. `CONVENTIONS.md` 57 rules *"UTC at rest; local on presentation"*.
One day, one stamp; doctrine is at rest.

*Counsel:* `2026-11-08`.

### RC6 — note · the three-reviewer reproduction is unverified in act 1

`REVIEW.md` 372-374: *"Three reviewers in one batch (2026-08-15, the SL2 channel class) … each
scanned the shared tree"*. Five verdict files carry that date (names only; all barred until act
2). Whether exactly three ran the scanner and what each disclosed is checked at reconcile; this
note exists so the check has an id.

### RC7 — note · the rung's seam with the secrets floor is unstated

`AUTONOMY.md` 127-137 puts *"regenerating credentials"* on the secrets floor and carves out only
*use* of a provisioned credential through the resolving machinery. The rung has a run mint a
credential and delete it on every use. `PRINCIPLES.md` §5 already frames external regeneration as
*"behind a one-off human approval"* (216-218), and the rung sits under that bullet, but
`SECRETS.md` 79-100 does not say that mint-per-run runs under that one-off grant rather than as a
fresh floor stop each time. A reader of `SECRETS.md` alone cannot tell. One clause closes it.

## Standing checklist V1–V7

- **V1** — RC2 (the floor's heading claims confirm where the ruling grants show-first), RC5
  (date). Every other claim re-driven holds or is carried to act 2 (ledger).
- **V2** — all seven re-run lines pass (ledger below); recorded proofs: the quote and its date
  hold; the 2026-08-04 date is consistent with its landing commit; the 2026-07-25 date and the
  three reproductions are not re-checkable from non-barred sources in act 1 (said so; act 2).
- **V3** — RC1 (the home, § *The one rule*, `method/README.md`), RC3 (skill, template README).
- **V4** — RC1.
- **V5** — RC2; the cross-reference line in lens 3 names the rule each pointer reaches.
- **V6** — lens 4 above; `/security-review` NOT RUN with grounds.
- **V7** — provenance stated above, repeating the brief's.

## Re-run ledger

All from the worktree, `python3` = 3.14.6 (first on `PATH`, as the brief says), one suite at a
time under `nice -n 10`, foreground; `uptime` load 6.3 at start, 9.7 at the floor.

| Line | Result |
|---|---|
| `git merge-base --is-ancestor 920d63f3 HEAD` | exit 0 |
| `coldsweep.py --selftest` | selftest OK, exit 0 |
| `coldsweep.py --root . --commit 920d63f3` | exit 0 (output read, body not printed) |
| `unittest test_templates` (run as `python3 -m unittest discover -s tools -p test_templates.py`, the no-`cd` equivalent) | Ran 55 tests, OK, exit 0 |
| `unittest test_blockscan` (same form) | Ran 58 tests in 41.1 s, OK, exit 0 |
| `blockscan.py --root . .` | exit 0; advisory list of unmapped headings |
| `nice -n 10 floor.py --plane ci --root .` | exit 0; 20 checks run, every enforced check green; secretscan 29 and leakscan 3 advisories, non-blocking. `stampscan` and `blockscan` are not on the ci plane |
| extra: `stampscan.py --require-floor-stamp docs/build/templates/CLAUDE.md` | 1 block verified, identical, exit 0 |
| brief's `coldsweep` sweep (three `--also-exclude`) | 95 hits over 748 files, 1017 barred files excluded, clean exit |

Not run: `/security-review` (grounds in lens 4). Not re-checkable in act 1: the 2026-07-25 date,
the three 2026-08-15 reproductions, the harness's pending-diff behaviour.

## Follow-up checklist

- [ ] Principal rules RC1 and RC2 together (one ask: confirm or show-first; one home).
- [ ] Principal rules RC3 (sweep to the skill, the template README and the drain skill's prompt).
- [ ] Principal rules RC4 (map the two source headings) and RC5 (`2026-11-08`).
- [ ] Act 2: open the sibling and the barred records; RC6 count; the 2026-07-25 date against
      `160/170`; screen the author's account; `### Reconcile` beneath this verdict.
- [ ] After rulings: application by a hand that wrote neither the doctrine nor this verdict, with
      its own `⏳` pointer (RC1 is MAJOR, so the cycle stays open).

The full method record (every command and file range, in order) is the review log, appended
verbatim at the fold.

### Reconcile (act 2, 2026-11-22 UTC)

Act 1 was committed unrevised as `dc9a0a78` before this was written. Released by orchestrator
session `60287c5a` in a process-only message (the held file's path, the barred records now open,
the deliverable's shape; no question about the delta, no request about any finding). Read for this
act: the sibling whole (15 questions, 8 facts); the four intent records whole; the delta's commit
body; the five 2026-08-15 verdicts' scanner passages; `git log -S` on *solve once*. Nothing in
act 1 is revised.

**The sibling's facts against mine.** All eight agree with act 1 where they overlap. Counts that
moved between 2026-11-14 and 2026-11-22 (48 → 55 `test_templates` tests; 86 → 95 sweep hits;
`RECORD.md` line 418 → 446) are tree growth, not disagreement. Fact 8 adds that *solve once* first
entered the board in `58776c4a`; re-run: 2026-07-25T02:53Z, so the §8 date holds in UTC too
(closes the act-1 gap on that date).

**The author's account.** The commit body restates the `CHANGELOG.md` entry and adds nothing.
`030/130` says *"`AUTONOMY.md` restates it as floor-class"*: it does not. `AUTONOMY.md` places the
rule under § *Before you destroy or overwrite* as *"One class is stricter … show-first"*, not in
§ *Always confirm*. That misreading is the likeliest root of RC1 and RC2: the author took the rule
to be a floor stop already and so put it in the confirm list, where the home never had it.
`160/195` chose option (b) (wording in `REVIEW.md`) over option (a) (a batch-preamble line), which
is the choice RC3 and Q10 bear on. `060/010`'s landing note matches the doctrine text. `160/170`
names the child whose tool grounds the in-repo example; the §8 bullet describes it by class only.

**Per finding, against the sibling's questions.**

- **RC1 (MAJOR) — stands.** No question addresses the home list directly; Q5 and Q8 circle it.
  The author's account above explains the gap and does not close it.
- **RC2 (MODERATE) — stands; Q5 asks the same question.** Q3 adds a second tension: the bullet's
  rationale clause (*"because what the floor guards cannot be taken back"*) now has one member
  whose bytes can be taken back; the rider says why it is there, so a child learns the reason, but
  the heading and the rationale both describe the other members. Q4 (*"whoever wrote it"*: "it"
  reads as the record, loosely as the store) and Q6/Q7 (*"meaning"* reads as a closed list;
  *"bulk"* is undefined in the floor as in `RECORD.md`) are wording the same ruling would settle;
  the floor is faithful to `RECORD.md` 448's four-item list and to its undefined *bulk*, so neither
  is a new overclaim. *Counsel, added:* if the clause moves to its own sentence (RC2 counsel),
  *"such as"* and *"whoever created it"* can be chosen in the same breath; *bulk* already has a
  machine reading in `harvestscan` (HV1, 50 net lines) that the prose could cite as the net, not
  the rule.
- **RC3 (MODERATE) — stands; Q11 asks it.** Q11 also asks whether `CONCURRENCY.md`
  § *Orchestrated queue runs* owes the line: it tells orchestrators where held material lives and
  says nothing
  about what a reviewer's scanner reads; one pointer there to lens 4 would do. Q10 (followability):
  *"verifiably clean at the moment of aiming"* is checkable (`git status --porcelain` empty) but
  is a precondition, not a guarantee against a concurrent write between the check and the scan;
  option (a) of `160/195`, which the author declined, is the only shape that makes it hold. So the
  rule is followable as a precondition and honest if read that way; the batch skill is where the
  guarantee would live. Folded into RC3's counsel, no new finding.
- **RC4 (minor) — stands; Q8 asks it.**
- **RC5 (minor) — stands.** Fact 6 records the same commit with its NZDT date.
- **RC6 — closed as a note; a finding is formed at reconcile in its place (RC8 below).** The
  three verdicts `160/195` names: `1032` (lines 347-358) and `1033` (line 234) each aimed the
  scanner at a scratch clone, saw it read the shared worktree's pending diff and were shown another
  pass's brief and sibling; `1030` (line 186) says *"the shared worktree's pending diff held none of
  this delta — it held another pass's material (disclosed above), over which I ran nothing"* and
  discharged the scanner. Two scans, one discharge.
- **RC7 (note) — stands.** No question addresses the seam with the secrets floor.

**Findings formed at reconcile** (marked as such; both from the sibling's questions, each
re-driven against the record before being written):

- **RC8 — minor · "Three reviewers … each scanned the shared tree" is two (V1).** `REVIEW.md`
  372-375 and `160/195`'s title (*"three reproductions"*). The record shows two reviewers ran the
  scanner and one ran nothing; the third's exposure came by another route. The mechanism claim
  itself (*"reads the session's pending diff, not a path it is aimed at"*) is established by the two
  that ran it, each independently, each disclosing the same behaviour; Q9's worry that the
  mechanism is inferred from one shape is answered by the two verdicts' own words, and the claim
  was not re-driven at landing (the landing note says *"wording only"*). *Counsel:* *"two"*, with
  the third named as a disclosure, keeps the sentence true without weakening the rule.
- **RC9 — note · two precision points in the rung's paragraph (Q13, Q14).** (i) *"a deleted one
  has no exposure window left to bound"*: a credential minted for the run exists for the run, so
  the window is one run long, not zero; the paragraph's *"between uses it does not exist"* is
  exact and the later clause overshoots it by a run. (ii) *"sits below the triad"*: least privilege
  still applies to a credential minted per run; the rung sits below the triad's second and third
  members. The duty's transfer to the minting credential (Q13's second half) is labelled as reasoned
  by the paragraph's own *"the limits that follow are reasoned from it"*; no finding there.

**Questions discharged without a finding.** Q1: the new *"else"* excludes the listed act, so no
bulk record deletion sits on the proceed side (act 1 lens 2). Q2: the checklist line is a question
pointing at §5, where the one-case label sits; a reader of the checklist alone meets a prompt, not
a settled rung. Q12: the queueing record says *"in Mike's words"* and *"Captured from Mike"*; the
doctrine repeats that attribution and adds nothing stronger; whether the words were his or a
sibling ADR's phrasing relayed cannot be checked from this repo, and that residual is the record's,
not the delta's. Q15: a paraphrase labelled as one is the house's *his call* shape
(`docs/PERSONAL-DATA.md` § *Granted by*); the bullet points at §2 and `EVIDENCE.md` §9 with one
sentence of gloss, which is pointing, not a second home; *practised* for up and down and *written*
for lateral is the honest split and the bullet says the grounding is uneven; the two examples
describe a tool class and a platform class and name no child (the board record that names the
child is already public, so the doctrine adds no inference).

**Overall, restated: PASS-WITH-FINDINGS — 1 MAJOR (RC1), 2 MODERATE (RC2, RC3), 3 minor (RC4,
RC5, RC8), 2 notes (RC7, RC9); RC6 closed into RC8.** The cycle stays open on RC1. Every finding
is the principal's to decide; counsel is labelled and sits beneath each.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-22)

Held out of the review tree, user-local, by orchestrator session `60287c5a` from the claim until act
1 was committed as `dc9a0a78`; then released to the reviewer for act 2 and folded here by that
orchestrator, which forms no finding. The reviewer read it only in act 2 (see *Reconcile* above).
The text below is the sibling's, verbatim and whole, with no change; the separate
`.deferred.md` file is removed from the tree in the same commit.

# Held back — the floor's record-store carve-out and three doctrine additions

Opened only once the reviewer's own findings are durably written (`REVIEW.md` rule 1). A floor,
never a fence. Written by the brief-writer (`cclive` lists it as session `b059d250`), which did not
author the delta. Nothing here is a finding: these are questions, and facts read off the machine.

## The pointer's own questions

1. Does the carve-out leave a recoverable-but-bulk record deletion on the wrong side of the floor's
   own closing sentence ("Everything else recoverable … just proceed")?
2. Is a one-case rule stated as more than one case? `SECRETS.md` says so in its own paragraph;
   `PRINCIPLES.md` §5 says so in a parenthesis; the checklist line "Used only rarely? Ask whether it
   need exist between uses at all" carries no marker. Does a reader of the checklist alone meet a
   settled rung?

## The brief-writer's questions

3. The floor bullet still ends "because what the floor guards cannot be taken back", and the new
   entry is on the list precisely because its bytes can be taken back. Does the bullet now
   contradict one of its own entries (V5), and does a child reading only the region learn why the
   entry is there?
4. "whoever wrote it": what is "it"? The store, the block, the record? `RECORD.md` says "regardless
   of who created the mess". Does the clause parse as the ruling means?
5. `RECORD.md` and `AUTONOMY.md` make a record-store bulk deletion show-first: "diff it and show the
   principal what goes, or ask". The floor's heading is "Always stop and confirm". Is showing then
   proceeding still allowed, or has the floor made the rule stricter than the ruling it carries,
   without saying so?
6. "meaning the roadmap, session logs, ADRs or reviews" reads as a closed list. `RECORD.md`'s same
   four look illustrative. Does the floor now exclude other one-file record stores a child keeps
   (a changelog, a decisions log, a ledger), and should "meaning" be "such as"?
7. "Bulk" is undefined in both texts. The grounding case was a 185-line removal in which one
   section was a genuine loss. Does deleting one item, or one section, escape the floor?
8. `tools/blockscan_map.json` maps the floor bullet's sources to one `00-APEX.md` heading only
   (fact 4). The new clause summarises `RECORD.md`'s record-store rule. Was a second source owed,
   so a later change to that rule is caught as moving the floor?
9. Lens 4 states as fact that `/security-review` "reads the session's pending diff, not a path it
   is aimed at". The evidence is three reviewers in one batch, one shape, one day. Is that the
   mechanism established, or the mechanism inferred from one shape (V1)? Was it re-driven at
   landing?
10. "verifiably clean at the moment of aiming": how does a reviewer verify it, and does the clean
    state survive a concurrent session writing between the check and the scan? Is the rule
    followable as written, or is option (a) of the intent record (the orchestrator commits before
    every spawn and writes nothing while reviewers run) the only way to meet it?
11. `skills/review-brief/SKILL.md`'s lens-4 compression carries the markdown exclusion and the
    deferred-material caution, and not the shared-worktree shape (fact 8). The skill says it may
    compress, never contradict. Was it a mirror site this delta owed (V3), and does
    `CONCURRENCY.md` need the same line?
12. "In Mike's words, captured 2026-08-03", then a quote. The record that queued it says "Captured
    from Mike", and its session-log line says a sibling session's ADR argued the idea and he routed
    the doctrine half to atelier (fact 5). Are the quoted words his, verbatim, or the ADR's
    phrasing as relayed? If the latter, is the attribution an overclaim?
13. "a deleted one has no exposure window left to bound": a credential minted for the run exists
    during the run. Is the exposure window zero, or one run long, and does the run-time window need
    stating? The intent record left open whether the rotation duty lapses or transfers; the
    doctrine settles it: the duty moves to the minting credential. Is that settled on reasoning
    alone, and is it labelled as reasoned?
14. "The rung sits below the triad": the triad is least-privilege, just-in-time, short-lived, and
    least privilege still applies to a credential minted per run. Is "below the triad" coherent,
    or is the rung below the last two only?
15. Solve once: the bullet says "Mike's principle (2026-07-25, captured in paraphrase)". Is a
    paraphrase attributed to him consistent with the house's verbatim-capture practice
    (`RECORD.md`, `COMMUNICATION.md`)? Does the bullet restate §2 DRY and `EVIDENCE.md` §9 while
    claiming to point at them (V4)? "the lateral route is the youngest, written 2026-11-09": the
    same day as this delta (fact 6). Is "practised" for up and down, and only "written" for
    lateral, the honest split, and does the bullet lean on the lateral route anyway? Privacy: do "a
    network tool handles its wire protocol in one module" and "One child repo's backup tool, on a
    platform whose delegation grant is standing-only" let a reader with the public estate in view
    name the child or the platform?

## Facts read off the machine (2026-11-14 UTC, from the worktree root)

1. Re-run lines: `git merge-base --is-ancestor 920d63f3 HEAD` exit 0; `coldsweep --selftest` exit
   0; `coldsweep --commit 920d63f3` exit 0, 206 lines; `python3 -m unittest test_templates` from
   `tools/`, 48 tests OK; `python3 -m unittest test_blockscan` from `tools/`, 58 tests OK in 46.7 s;
   `blockscan.py --root . .` exit 0; `floor.py --plane ci --root .` exit 0, 49 s wall clock under
   `nice -n 10`, Python 3.14.6, load average 9 to 13 on 12 cores. The *Deferred reading* sweep
   command ran exit 0, 86 hits over 679 files; its only hits on barred paths were board titles in
   `docs/ROADMAP.md`.
2. `920d63f3`'s stat: `CHANGELOG.md`, `docs/ROADMAP.md`, `docs/build/templates/CLAUDE.md`,
   `docs/method/PRINCIPLES.md`, `docs/method/PROPAGATION.md`, `docs/method/REVIEW.md`,
   `docs/method/SECRETS.md` and four board item files; 124 insertions, 19 deletions. Markdown only.
3. Later commits on the delta's files: `2a6d7a41` (`PROPAGATION.md` and the template, hunks at the
   *Asking* bullet, lines 63 and 161 before it), `55c7d409` and `dd3d60d4` (`REVIEW.md`, other
   sections). None touches the four regions under review.
4. `tools/blockscan_map.json`, entry `stop-and-confirm`: anchor "**Always stop and confirm (the
   floor):**"; one source, `docs/method/00-APEX.md` § *The principal's authority is absolute; his
   rulings are conditioned on being informed*.
5. `git log -S "delete the credential entirely"`: first `b3101c3b`, 2026-08-03, "roadmap: queue a
   fourth rung for the credential ladder — no credential at rest". Its item heading reads "(Mike,
   2026-08-03)"; its body says "an alternative in Mike's words: … Captured from Mike; not yet
   designed or decided". The same commit's `docs/SESSIONS.md` index line says a sibling session's
   ADR argued the idea and Mike routed the doctrine half to atelier.
6. `### The same route between any two repos` (`PROPAGATION.md` line 814 at 2026-11-14) first
   appears in `3f3cf5be`, 2026-11-09, "method: one route carries an idea between any two repos
   (310/120, 310/140)". Its authoring session was not checked.
7. The closing clause's words appear only at `PROPAGATION.md` line 145, the template line 47 and
   `CHANGELOG.md`. The show-first rule is at `RECORD.md` line 418 (listing "ROADMAP, SESSIONS, ADRs,
   reviews"; the principal's ruling, 2026-08-04) and `AUTONOMY.md` line 242.
8. `skills/review-brief/SKILL.md`, lens 4 (lines 89 to 96 at 2026-11-14), names `/security-review`,
   the markdown exclusion and the deferred-material caution; it carries no shared-worktree line.
   "solve once" first enters `docs/ROADMAP.md` in `58776c4a`, 2026-07-25.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

The reviewer's running work log, appended whole by orchestrator session `60287c5a` at the fold.
No orchestrator or other session read or steered it while the pass ran.

# REVIEW LOG — atelier 160/1280, Fable 5.1 cold pass (act 1)

Worktree: /Users/mike/worktrees/fable/atelier-160-1280-2009/atelier (HEAD c4bc074b)
Brief: docs/reviews/2026-11-14-0157-record-store-floor-three-rules-cold.md
Reviewer: Fable 5.1 (claude-fable-5-1), spawned by orchestrator session 60287c5a, started by
drain session eca14b23. Log started 2026-11-22T20:11Z.

## Steps

- 2026-11-22T20:11Z `uptime`: load 6.33 6.68 6.54 (16 GB laptop, several passes sharing).
  `/usr/bin/python3` = 3.9.6; first `python3` on PATH = 3.14.6 (matches brief).
  `git status --short`: only ` D docs/reviews/...deferred.md` (expected partition deletion).
- Read brief in full (lines 1-251).
- Read docs/method/REVIEW.md whole at HEAD (lines 1-836) for verdict shape, rules 1-4, lens 4,
  V1-V7, the method-record rule (2026-11-15 ruling).
- `git merge-base --is-ancestor 920d63f3 HEAD` -> exit 0 (tree holds the delta).
- `python3 tools/coldsweep.py --selftest` -> "selftest OK", exit 0 (python3 = 3.14.6). NOTE: I
  ran this one line after a `cd` into the worktree in the same shell; every later command uses
  absolute paths only.
- `python3 tools/coldsweep.py --root <worktree> --commit 920d63f3` -> exit 0; subject, stat,
  diff printed; body not printed; 5 board files left out by default (ROADMAP.md + the four intent
  records). Stat of the six non-board files: 87 insertions, 11 deletions (brief says 124/19 across
  "six non-board files": checking the whole-commit stat next).
  Delta content observed (six files): CHANGELOG entry; floor bullet in PROPAGATION.md and
  templates/CLAUDE.md (identical hunks: "bulk deletion from a record store ... wrong test there;"
  and "Everything else recoverable"); REVIEW.md lens 4 new sentences; SECRETS.md two paragraphs
  after the triad; PRINCIPLES.md §5 case sentence, §8 bullet, checklist line.
- `git show --stat=200 --format= 920d63f3` (no body): 11 files, 124 insertions, 19 deletions.
  So the brief's "124 added and 19 removed lines ... across six non-board files" counts the five
  board files too; the six non-board files are 87/11. Brief-framing slip, not a delta defect.
- `git show -s --format='%H%n%ad%n%cd%n%s' --date=iso-strict 920d63f3`: author
  2026-11-10T02:26:08+13:00 (= 2026-11-09T13:26Z), committer 2026-11-10T02:29:43+13:00. Brief's
  "landed 2026-11-09 UTC (stamped 2026-11-10 NZDT)" and CHANGELOG's "2026-11-09" both hold.
- `git log --all -S'delete the credential entirely and make its rebuild cheap' --format='%h %ad %s'`
  -> ONE hit: 920d63f3 (the delta). The quoted sentence exists nowhere in git history before the
  delta. CANDIDATE: the quote "In Mike's words, captured 2026-08-03" has no earlier home in the
  tree the reviewer can reach by the brief's named route. Follow-up: narrower -S fragments.
- `git log -S'The same route between any two repos' --format=... -- docs/method/PROPAGATION.md`
  -> 3f3cf5be 2026-11-09T03:24:49+13:00 = 2026-11-08T14:24:49Z, subject "method: one route
  carries an idea between any two repos (310/120, 310/140)". The delta's "written 2026-11-09" is
  the NZDT date; CONVENTIONS.md requires UTC at rest. CANDIDATE (minor): local-date stamp.
- `git log -S'recoverable bytes' -- RECORD.md AUTONOMY.md` -> no hit (the phrase is the delta's
  paraphrase, not RECORD.md's text). Reading RECORD.md directly next.
- `git log -S'2026-07-25' -- PRINCIPLES.md` -> de1049b3 (2026-11-17, §11) and 920d63f3 only.
- Floor region at HEAD: PROPAGATION.md lines 132-244 (awk between floor:begin/end). Bullet at
  146-162 parses as one sentence; "Everything else recoverable" closes it. Template
  docs/build/templates/CLAUDE.md lines 19-128 (stamp:begin source=docs/method/PROPAGATION.md
  region=floor): diff of the two regions showed no difference in the floor text (my sed ranges
  overran at the tail; stampscan/floor will confirm mechanically).
- RECORD.md 446-463: "Bulk deletion from a record store is a show-first action, regardless of
  who created the mess (the principal's ruling, 2026-08-04). ... either diff it and show the
  principal what goes, or ask. ... Recoverability of bytes is the wrong test for a record
  store." Grounded 2026-07-25 (185-line duplicates removal). Net: harvestscan bulk-deletion warn.
- AUTONOMY.md 8-20 (The one rule: "Proceed on anything recoverable"), 40-168 (Always confirm:
  "The floor. These hold everywhere ... this file is where that list lives"), 274-285 (Before
  you destroy or overwrite: "One class is stricter ... bulk deletion from a record store is a
  show-first action — diff the block and show what goes, or ask, before it is removed").
  `grep -n -i 'record store' AUTONOMY.md` -> only line 281. The Always-confirm list (lines
  44-146) has NO record-store entry.
- 00-APEX.md 85-87: "an always-confirm floor stop (the list is AUTONOMY.md § Always confirm,
  which holds it once; PROPAGATION.md's floor block carries the copy children inline)".
  CANDIDATE RC1 (V4 one home / V3 sweep): the delta adds a confirm-list entry to the COPY
  (floor region + template) and not to the list APEX names as the one home.
  CANDIDATE RC2 (V5 / lens 1): the floor lists the act under "Always stop and confirm" with a
  "shown first" rider; RECORD/AUTONOMY rule it show-first OR ask (show, then remove). Position
  in the list makes it a floor stop (APEX: re-brief before, informed confirmation); the rider
  says show-first. Two readings; the two homes disagree on whether the agent may proceed after
  showing.
- SECRETS.md headings (17 Reproducible/enabling property; 61 triad; 102 non-reuse; 310 Rotation
  cadence; 324 Exposure). Lines 61-100 read: the two new paragraphs sit under § The credential
  triad; "the enabling property above" resolves to § 17; "the rotation cadence below" resolves
  to § 310. Both pointers reach the rule they name.
- PRINCIPLES.md: §5 at 192; case sentence 229-234 ("the next rung is no credential at rest ...
  a one-case claim"); §8 at 321, the new bullet at 354-369, "the bullet above" = "Build the
  reliable tool once; reuse it forever" (345-353); checklist line 748 "Used only rarely? Ask
  whether it need exist between uses at all (§5)"; §2 DRY at 85-91; §6 sweep surface list
  277-287 names docs/, skills/, commands/, templates/, children's floor blocks.
- PROPAGATION.md headings: § Pointing up (506), § The mechanism (24), § The same route between
  any two repos (845), § One statement, stamped copies (1178). All three §8 pointers resolve.
  EVIDENCE.md §9 at 121 ("One fact, one home"), §14 at 248, §19 at 489.
- CONVENTIONS.md 57: "UTC at rest; local on presentation"; 59: prose stamps YYYY-MM-DD + HHMM
  UTC. The §8 "written 2026-11-09" is the NZDT day of 3f3cf5be (2026-11-08T14:24Z).
- GLOSSARY.md 60-62 defines Floor; no entry for "record store" (grep). Noted, not a finding:
  RECORD.md 446-448 defines it by enumeration and the floor repeats the enumeration.
- skills/review-brief/SKILL.md 99-106 and docs/build/templates/docs/reviews/README.md 30-34
  restate lens 4's scanner guidance with the FIRST caution ("never run it over a brief carrying
  deferred material") and NOT the shared-worktree caution the delta adds. grep of
  skills/review-drain/SKILL.md and skills/queue-run/SKILL.md for security-review|scanner|shared
  worktree: 0 hits. coldsweep for 'pending diff': REVIEW.md:370 and CHANGELOG:608 only.
  CANDIDATE RC3 (V3): the new caution has no mirror in the skill brief-writers work from.
- tools/blockscan_map.json 21-27: "stop-and-confirm" bullet sources = 00-APEX.md § The
  principal's authority... ONLY. Not AUTONOMY.md § Always confirm (APEX's named home), not
  RECORD.md § record store. CANDIDATE RC4: the co-change guard cannot see the RC1 class; the
  delta did not add the new clause's source.
- tools/test_templates.py 36-90: the template test compares the stamped block to the canonical
  region verbatim (test_stamped_block_matches_canonical). stampscan --help: compares stamped
  copies to canonical source; blockscan --help: co-change check from the hand-maintained map.
- docs/PERSONAL-DATA.md read whole (PD1 account name, PD2 author's full name, ...). The delta
  adds "Mike's words"/"Mike's principle": first name only, the house's standing form. Not a
  finding.
- `ls docs/reviews | grep '^2026-08-15\|^2026-07-21'` (NAMES ONLY, files not opened): five
  2026-08-15 verdicts (1030, 1031, 1032, 1033, 1126) and two 2026-07-21. The delta says "Three
  reviewers in one batch (2026-08-15)". Count check is phase 2.
- Later commits: 2a6d7a41 (2026-11-12, Asking bullet + others), 55c7d409 and dd3d60d4
  (2026-11-10, REVIEW.md 4 lines each). `git diff 920d63f3 HEAD -U0` hunk headers on the six
  files: no hunk falls inside the four regions (floor bullet old 127-143 / template 29-47;
  REVIEW.md old 363-377; SECRETS.md old 79-100; PRINCIPLES.md old 210-213, 313-328, 622).
  The brief's "the files have moved since, not the regions" holds.
- Quote trace: `git log --all -S'rebuild cheap'` and -S'automated and tested' -> b3101c3b
  (2026-08-03T17:58:10+12:00 = 2026-08-03T05:58Z, "roadmap: queue a fourth rung ..."),
  a9abc266 (store migration), 920d63f3. `git show --format= b3101c3b | grep -n -i -E
  'delete the credential|rebuild cheap|automated and tested|credential at rest'` (narrow): added
  lines 14-15 read `in Mike's words: "delete the credential entirely and make` / `its rebuild
  cheap, automated and tested".** Captured from Mike`. Character-for-character match with the
  delta's quote; the one-line -S missed it because the source wraps. Date 2026-08-03 holds
  (0557 UTC per the index line). EXPOSURE: the grep also printed one docs/SESSIONS.md index
  line (+79) carrying a short account ("a sibling session's ADR argued that where a platform
  grants delegation standing-only, the credential can be del..."). Disclosed; it steered no
  finding.
- `git log -S'show-first action' -- RECORD.md AUTONOMY.md` -> 53785b95 2026-08-06T00:51+12:00
  "doctrine: the 2026-08-04 sitting's five small edits, one landing". The 2026-08-04 ruling
  date RECORD.md cites is consistent with its landing commit's subject.
- Brief's coldsweep sweep (pattern 'record store|recoverable|pending diff|credential at
  rest|solve once', three --also-exclude): 95 hits over 748 files, 1017 excluded as barred;
  ✓ line printed. Hits read: census 2026-11-16-1204 line 347-351 ("The 'one list' of
  always-confirm stops is two lists ... The block adds bulk deletion from a record store (in
  AUTONOMY.md it sits under § Before you destroy or overwrite, not § Always confirm) and leaves
  out deploy-on-push of a new content class and the merging of other people's work");
  census 2026-11-16-1142 REC24 ("shown to the principal first ... enforced, partial (warns):
  harvestscan ... The showing itself: invisible"); roadmap 020 README 265 ("show-first action
  — Mike's call, it narrows agent autonomy"); roadmap 300/020 line 139 ("030/130 |
  record-store deletion confirm | forbids · recovery: restore from history | Show first, then
  act. The bytes are recoverable."). Census records are not on the barred list; they post-date
  the delta (2026-11-16) and were read after RC1/RC2 were formed from APEX/AUTONOMY.
- 'one-case' in docs/method (excl. census): SECRETS.md:90 and PRINCIPLES.md:234 only.
- CHANGELOG.md 600-614 at HEAD: entry unchanged from the delta.
- CONCURRENCY.md 1017-1030: held-back review notes live in a user-local directory outside the
  repo, every worktree and any scratchpad (Mike's answer 2026-11-09, 160/380).
- harvestscan --help: `--only-bulk-deletes` reports only when >= 50 net lines leave the watched
  records (HV1). floor.py --help, datescan.py --help read for argv.

## Re-run ledger (all from the worktree, python3 = 3.14.6, one suite at a time)

1. `git merge-base --is-ancestor 920d63f3 HEAD` -> 0.
2. `python3 tools/coldsweep.py --selftest` -> "selftest OK", 0.
3. `python3 tools/coldsweep.py --root <wt> --commit 920d63f3 > /dev/null` -> 0 (run with output
   shown instead, same exit).
4. `nice -n 10 python3 -m unittest discover -s <wt>/tools -p test_templates.py` (the no-cd
   equivalent of `cd tools && python3 -m unittest test_templates`) -> Ran 55 tests, OK, 0.
   uptime at start: load 9.68.
5. same for test_blockscan.py -> Ran 58 tests in 41.1 s, OK, 0.
6. `nice -n 10 python3 tools/blockscan.py --root <wt> <wt>` -> 0; advisory list of unmapped
   headings (incl. PROPAGATION.md:845 § The same route between any two repos, under mapped
   § Pointing up); "coverage: 7 file(s) opened".
7. `nice -n 10 python3 tools/floor.py --plane ci --root <wt>` -> 0; 20 checks run, every
   enforced check ✅ (secretscan 29 advisory, leakscan 3 advisory, both non-blocking); stampscan
   and blockscan are NOT on the ci plane list.
8. (extra) `nice -n 10 python3 tools/stampscan.py --root <wt> --require-floor-stamp
   docs/build/templates/CLAUDE.md` -> "1 stamped block(s) verified ... [identical] matches
   canonical region 'floor' (109 lines)", 0. Mechanical proof the two floor copies match.
- RECORD.md 446 sits under "## The roadmap — one file per item, a generated index" (line 408):
  the heading blockscan would need if the record-store clause were mapped.
- docs/method/README.md:14-15: "AUTONOMY.md — proceed on anything recoverable (commit/push/PR
  granted for all work); confirm on the hard-to-undo floor (private→public, destructive, ...":
  another restatement site without the record-store carve-out (RC1 evidence).

## Not run / not re-checkable in act 1
- `/security-review`: NOT RUN. Grounds: the delta is markdown only (the scanner excludes it, so
  a clean pass is empty); my worktree carries a pending diff (this brief's verdict and the
  sibling's deletion), so a run would scan my own draft, the shape lens 4 warns about.
- The three 2026-08-15 reproductions: the verdict files are barred until act 2; five same-day
  verdict files exist by name.
- The 2026-07-25 principle date (§8): no non-barred source carries it (`git log -S'2026-07-25'
  -- PRINCIPLES.md` hits only the delta and de1049b3). RECORD.md:457's 2026-07-25 is a
  different event (the 185-line removal). Re-check in act 2 against 160/170.
- The harness claim "`/security-review` reads the session's pending diff, not a path": a
  harness behaviour I cannot probe read-only here; grounded in the delta's cited verdicts (act 2).

## Findings formed (act 1)
RC1 MAJOR, RC2 MODERATE, RC3 MODERATE, RC4 minor, RC5 minor, RC6 note, RC7 note. Verdict text in
the brief. Overall: PASS-WITH-FINDINGS (1 MAJOR, 2 MODERATE, 2 minor, 2 notes).

## Act 1 written (2026-11-22 UTC)
- Status line updated; verdict appended below `---` (brief now 533 lines). Four finding headings
  shortened to <= 100 columns; a stray spellscan marker on the principal's verbatim quote removed
  (docs/reviews is spellscan- and wrapscan-ignored, so the marker was noise).
- Gates over the brief: `datescan.py --root <wt> <brief>` -> clean, exit 0 (re-run after edits:
  clean). `wrapscan.py` and `spellscan.py` -> clean, exit 0, but both report "scanned nothing"
  (docs/reviews ignored by .wrapscanignore/.spellscanignore). `reviewscan.py` -> exit 0, "1 review
  brief(s) keep deferred material out of the brief". awk column check on lines > 254 (my text):
  no non-table line over 100 characters after the heading edits.
- `git status --short`: ` D ...deferred.md` (expected) and ` M ...cold.md` (the brief). Nothing
  else written in the repo. No commit, no push, no git add.
- Act 2 waits on the orchestrator's release message naming the sibling's path.
- Final: RC1/RC2 headings shortened again; awk check clean; datescan clean exit 0; tree unchanged otherwise.

## Act 2 (reconcile) — released by orchestrator session 60287c5a
- Release message (process only): act 1 committed and pushed to main as dc9a0a78, unrevised;
  may now read the held sibling (one file, user-local held directory), the four intent records
  whole, prior verdicts incl. the 2026-08-15 ones, the delta's commit body; append ### Reconcile
  beneath the verdict, never revise act-1 text; do not fold or delete; same rules.
- Read the sibling whole (101 lines): 15 questions, 8 facts. Facts 1-8 agree with mine except
  counts that moved since 2026-11-14 (48 -> 55 tests; 86 -> 95 sweep hits; RECORD.md line 418 ->
  446; PROPAGATION 814 -> 845). Fact 8 adds: "solve once" first enters ROADMAP in 58776c4a,
  2026-07-25.
- Read the four intent records whole: 030/130 (author's account says "AUTONOMY.md restates it
  as floor-class"; the fix "name the record-store case in the region's confirm list"), 160/195
  (three reproductions named: verdicts 1030, 1032, 1033; option (a) batch-preamble not taken,
  option (b) wording chosen), 060/010 (quote + "Captured from Mike; not yet designed or
  decided"; open questions; landing note), 160/170 (the paraphrase; names a child repo by name,
  which the §8 bullet anonymised as "a network tool"). Commit body 920d63f3 read: four
  paragraphs restating the four parts; nothing beyond the CHANGELOG entry.
- `git log --all -S'solve once'` -> 58776c4a 2026-07-25T14:53:04+12:00 (= 2026-07-25T02:53Z)
  "roadmap: capture 'solve once, reuse the building block' principle (Mike, note-for-later)".
  The 2026-07-25 date holds in UTC too.
- 2026-08-15 verdicts grep (security-review|scratch clone|pending|shared worktree): 1032 lines
  347-358 ("The skill ignored the path argument and read the shared worktree's dirty state ...
  Exposure disclosure #1: that scan showed the reviewer another pass's brief and its .deferred.md
  sibling (the reply-gate pass)"); 1033 line 234 ("The skill's harness ignored the aim and read
  this worktree's pending diff instead ... the SL2 exposure disclosed above"); 1031 line 96 and
  1126 lines 288-289 are discharge lines (not run). 1030: checking its reach-case passage.
- 1030 line 186 (lens 4): "the shared worktree's pending diff held none of this delta — it held
  another pass's material (disclosed above), over which I ran nothing ... discharged". So of the
  three named verdicts, two (1032, 1033) ran the scanner; 1030 did not. RC6 -> closed; RC8 formed
  at reconcile (minor, V1: "three ... each scanned" is two).
- RC9 formed at reconcile (note) from Q13/Q14: run-time exposure window unstated; "below the
  triad" vs least privilege still applying.
- Author's account checked: 030/130 "AUTONOMY.md restates it as floor-class" is contradicted by
  AUTONOMY.md 274-285 (Before you destroy or overwrite; "stricter ... show-first"). Likely root
  of RC1/RC2. Recorded in the Reconcile.
- `### Reconcile` appended beneath the verdict; act-1 text untouched. Overall restated:
  PASS-WITH-FINDINGS, 1 MAJOR, 2 MODERATE, 3 minor, 2 notes.
- Act 2 checks: awk column check from `### Reconcile` on; `git diff dc9a0a78 -- <brief>` removed-line
  count (0 expected: append-only); datescan over the brief; `git status --short` (brief modified,
  sibling deletion). Results recorded by the orchestrator at the fold. ACT 2 SAVED.
