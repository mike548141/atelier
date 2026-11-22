# Cold pass — the floor's record-store carve-out, `/security-review` in a shared worktree, no credential at rest, solve once at both scopes

**Board:** `docs/roadmap/160-doctrine-review-owed/1280-rule-4-cold-pass-queued-record-store-floor-three-rules.md`
**Status:** ACT 1 WRITTEN 2026-11-22 UTC — PASS-WITH-FINDINGS (1 MAJOR, 2 MODERATE, 2 minor,
2 notes); act 2 (reconcile against the sibling) owed. Reviewer: Fable 5.1 under the principal's
2026-11-23 NZDT drain order, run by orchestrator session `60287c5a` for drain session `eca14b23`.
Brief written 2026-11-14 UTC by a headless Opus 5.5 brief-writer (`cclive` lists it as session
`b059d250`).

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
