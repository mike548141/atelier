# Cold pass — disclosed contact with a review chain, the non-scalar field under an allowlist, and closing a house question locally

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (a guard or a rule is doctrine
by function, rule 3).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** RUN 2026-11-22 UTC, both acts written (act 1 committed before the sibling opened,
locally as `90d55919`, landed as `30daf253`; reconcile beneath it; sibling and review log folded in
below by the orchestrator). PASS-WITH-FINDINGS, restated at reconcile: 0 MAJOR / 4 MODERATE /
7 minor / 4 note. Findings await the principal's ruling (rule 3); nothing applied. Brief written
2026-11-09 UTC by session `d4a0fcf3`, a headless Opus 5.5 brief-writer. Run under the principal's
drain order of 2026-11-23 NZDT (drain session `eca14b23`).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/999-rule-4-cold-pass-queued-disclosed-contact-scalar-allowlist-closed-questions.md`.
**Size of this pass:** small: three doctrine paragraphs, about 35 lines, in four files.
**Why it earns a review:** This is standing review, secrets and propagation doctrine every repo
reads. The worst failure is a rule that reads as a defence and is not, or one that cannot be checked
by anyone but its subject.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `4c65083c`,
  2026-11-03, and the Opus worker it dispatched, which wrote the text (per the queue pointer). The
  author queued this pass and does not take it.
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
  account; every delta commit body-free through `tools/coldsweep.py --commit`; commit subjects
  through `git log`; `docs/reviews/2026-11-06-2027-secretscan-public-pem-spans-cold.md` whole,
  **including that pass's verdict and folded sibling** (a different subject, read for house form),
  the acceptance-test section and the status and overall verdict lines of
  `docs/reviews/2026-10-26-0928-g3-grace-metadata-sets-cold.md` (the counts only), and the opening
  30 lines of board item `160/980`; three lines of `docs/SESSIONS.md` and the opening of
  `docs/sessions/2026-11-06-2022-fable-passes-850e.md`; the results of the re-run lines below. It
  did **not** open any other prior verdict or any delta commit's message body. Its harness also
  loaded user-level and repo instruction files and a memory index, which hold private context this
  brief does not carry. Everything evaluative it formed is in the sibling.

## The acceptance test

No record the brief-writer read carries a ruling of the principal's on these three texts. Judge each
against its host doctrine: `docs/method/REVIEW.md` rule 4 (the criterion, the context partition),
`docs/method/SECRETS.md` on exposure, and `docs/method/PROPAGATION.md` on pointing up.

## What the work is

- **`ef9e975`** — `review: contact with a delta's review chain is disclosed by the receiver
  (280/040)`.
- **`ba4e95b`** — `secrets: a non-scalar value under a kept field is un-allowlisted (320/090)`.
- **`3b1cb23`** — `propagation: the opening check covers closing a house question too (310/090)`.

Delta paths, read at each commit and at HEAD:

- `docs/method/REVIEW.md`, `docs/method/CONCURRENCY.md`, `docs/method/SECRETS.md`,
  `docs/method/PROPAGATION.md`

First confirm the tree holds the delta, then read each commit body-free:

```
git merge-base --is-ancestor 3b1cb23 HEAD; echo $?
python3 tools/coldsweep.py --root . --commit <sha> --path docs/method/REVIEW.md --path \
  docs/method/CONCURRENCY.md --path docs/method/SECRETS.md --path docs/method/PROPAGATION.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). The commit also touches board records; those are barred until phase 2, so always pass `--path`.

Then see what has landed on those paths since, and read anything new the same way, only as far as it
bears on this delta at HEAD: `git log --oneline 3b1cb23..HEAD -- docs/method/REVIEW.md
docs/method/CONCURRENCY.md docs/method/SECRETS.md docs/method/PROPAGATION.md`.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- Contact with a delta's review chain "is permitted only as disclosed contact", recorded by the
  receiver; the rule says the receiver records it because "a self-report is the weaker artefact".
- "Disclosure is the rule because a factual correction and a framing … cannot be told apart from
  outside without it."
- A channel message from an author to a session in the chain is "disclosed contact"
  (`CONCURRENCY.md`).
- A non-scalar value under a kept field is un-allowlisted: "drop it, or recurse the allowlist into
  it, and never print it whole".
- The opening check "covers both shapes" of deciding a house question locally; a ruling that looks
  adjacent "is not a ruling on your question".
- "The second shape is the worse one", with three groundings cited.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope,
and a non-goal that fences off the risk is a finding.

**Non-goals:** the channel doctrine's other limits (`280/`), as reviewed under
`2026-08-17-1000-channel-doctrine-cold.md`; the rest of those files.

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
python3 tools/pathscan.py --root . docs/method/REVIEW.md docs/method/SECRETS.md docs/method/PROPAGATION.md docs/method/CONCURRENCY.md
nice -n 10 python3 -m unittest discover -s tools
```

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
`docs/reviews/2026-11-09-0207-contact-scalar-allowlist-closed-questions-cold.deferred.md` (a
held-back file; by count: 7 questions, 1 facts; now folded below the verdict and the file
removed), every other item under
`docs/roadmap/160-doctrine-review-owed/` beyond its title, every delta commit's message body, and
these intent records beyond their first line:

- `docs/roadmap/280-cross-session-channel-mike-commissioned/040-the-channel-can-contaminate-review-independence.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/090-proposal-a-field-allowlist-leaks-through-non-scalar-fields.md`
- `docs/roadmap/310-pointing-up-the-child-to-parent-route/090-pointing-up-names-one-shape-of-local-overreach-and-there-are-two.md`

The delta's own docstrings, comments, README, design note and `CHANGELOG.md` entries carry the
author's account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/280-cross-session-channel-mike-commissioned/040-the-channel-can-contaminate-review-independence.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/090-proposal-a-field-allowlist-leaks-through-non-scalar-fields.md \
  --also-exclude docs/roadmap/310-pointing-up-the-child-to-parent-route/090-pointing-up-names-one-shape-of-local-overreach-and-there-are-two.md \
  'disclosed contact|un-allowlisted|non-scalar|closing an open house question'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the re-run
list. Append your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, any orchestrator, what you read, the UTC day), per-lens answers, V1–V7 each
answered or discharged with grounds, each load-bearing assumption damaged or confirmed with its
probe, a per-commit ledger (read body-free yes/no, findings by id), findings with stable IDs (prefix
`DC`: `DC1`, `DC2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit bodies;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work is doctrine by function, so every finding is the principal's to decide (rule 3): record
all, apply nothing. Counsel per finding is welcome, labelled as counsel and kept beneath it.

---

## Verdict — act 1, 2026-11-22 UTC

### Provenance

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named review tier, checked at
  selection. Review worktree: `/Users/mike/worktrees/fable/atelier-160-999-2000/atelier`, HEAD
  `74b2f65d` (the claim commit), read-only to me except this file.
- **Spawn:** started by headless per-pass orchestrator session `a9a9eba8` (Opus 5.5), itself started
  by drain session `eca14b23` (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold the
  context partition, form no finding and write no severity. Neither wrote the brief or any of the
  delta; `eca14b23` started no brief-writer. I was not started or instructed by the brief's barred
  sessions (`d4a0fcf3`, `74f2b8cd`, author `4c65083c` or anything it started).
- **Approval:** the principal's drain order of 2026-11-23 NZDT, verbatim: *"Start a fable drain or
  whatever it is called now. Target 100% of weekly budget by 11.30am NZT todat"*.
  <!-- datescan:allow: the principal's words, quoted verbatim; the relative word is his -->
- **Orchestrator direction received (process only, as rule 4 requires):** the spawn prompt named
  the item, the worktree, the brief and `REVIEW.md`; the provenance above; the partition (the
  `.deferred.md` sibling removed from the worktree, released by message after act 1 is committed;
  every other rule-2 barred record barred until then); live systems read-only, no writes; load
  rules (`uptime` first, `nice -n 10`, one suite at a time, no bare tools from `PATH`); what I may
  write (this file below a divider, the Status line, and one running log outside the repo); no git
  operations; public-repo naming rules; rule 3 (record all, apply nothing); the act-1 and act-2
  finish words. It contained no question about the delta, no pointer to where the risk lives and
  no request about any finding. The orchestrator's release message is not yet received and is
  recorded in the reconcile. The log named in the prompt is a user-local file outside this repo; it
  is appended to this file at the fold, per § *The lifecycle*.
- **Contact:** none from any author session or anyone else during the pass (rule 4's disclosed
  contact: nothing to disclose).
- **What I read:** the brief whole; `docs/method/REVIEW.md` whole; the three delta commits
  body-free through `tools/coldsweep.py --commit … --path` (each printed a board-store file left out
  by default; I read none); the four delta paths at HEAD around each paragraph and their heading
  lists; commit subjects on the delta paths since the landing and for 2026-08-16 to 2026-08-19;
  `docs/roadmap/310-…/060-…` and `…/080-…` (first 30 lines each; not barred); the first line only of
  the three barred intent records; `docs/method/census/2026-11-16-1142-…` rows REV16–REV22 and
  `…-1204-…` rows PRO21–PRO24; `docs/method/GLOSSARY.md` by grep; `skills/review-brief/SKILL.md`
  55–135; `skills/review-drain/orchestrator-prompt.md:23`; `docs/build/templates/CLAUDE.md:95–100`;
  `tools/attribscan.py` 1–30; `instruments/ccapple` and `instruments/ccmail` by grep and the
  field-keeping functions. I skipped the session-log step of the read order, opened no prior
  verdict, no session file, no `ROADMAP-DONE.md`, no commit body, and did not look for the sibling.
  My harness loaded user-level and repo instruction files and a memory index; they hold private
  context this verdict does not carry, and none of it is an account of this delta.
- **Load:** `uptime` load 4.43 at start, 6.03 before the suite, 8.98 at its end (several passes
  running); the suite ran under `nice -n 10`, single process, foreground, once.

### Lens 1 — approach and assumptions (named first, then tested)

Load-bearing assumptions I named before reading the delta's claims:

- **A1. The channel is the only post-spawn route that matters.** Confirmed as the rule's scope,
  damaged as a premise: the rule says "contact … is permitted only as disclosed contact" without
  saying what counts as contact beyond the channel example. Records the author writes after the
  spawn (its intent record, its commit bodies) are not contact, because rule 2 governs when they
  are read. The gap I found is not the route but the direction and the recorder (DC1).
- **A2. The receiver can always write to the review's provenance.** False in one of the two
  directions the wording covers (DC1).
- **A3. A "field allowlist before printing" is a stated house duty the SECRETS paragraph refines.**
  False: no doctrine states it (DC3). The paragraph is sound as a refinement; it has nothing under
  it.
- **A4. The audience for the PROPAGATION paragraph is child sessions.** Confirmed by its own
  grounding ("a child that tried both"), which is what makes the floor block the mirror that matters
  (DC5).
- **A5. The three paragraphs sit at the right altitude and in the right home.** Confirmed for
  REVIEW.md rule 4 (the criterion's silence is exactly where the clause is placed) and PROPAGATION
  § *Check the parent's file first* (the check is the thing extended). For SECRETS.md the home is
  defensible (§ *Exposure* opens with "watch the surfaces where a credential could surface") but a
  reader looking for output-side rules would look in § *Right plane* first; note only (N3).

Right problem? Yes for all three: each closes a real silence (post-spawn contact; a typed hole in
an allowlist; the second shape of local overreach), and each is grounded in a recorded instance.
Right shape? REVIEW's is a rule with a recorder; the recorder is mis-assigned for one direction.
SECRETS's is a refinement without a base. PROPAGATION's is a principle ("binds it identically")
without the matching procedure.

### Lens 2 — correctness and quality (the claims re-driven)

| Claim (brief § *The claims*) | Result |
|---|---|
| Contact is permitted only as disclosed contact, recorded by the receiver | Overclaim in one direction: when the chain side initiates, the receiver is the author (DC1) |
| A correction and a framing cannot be told apart from outside without disclosure | Holds; but a *paraphrased* disclosure still cannot be told apart from outside (DC2) |
| A channel message from author to chain is disclosed contact (CONCURRENCY) | Holds; both copies point at REVIEW.md rule 4 and reach it (lines 280–295) |
| A non-scalar value under a kept field is un-allowlisted; drop or recurse, never print whole | Holds as written; "recurse the allowlist into it" is under-specified (N2) and the base duty is unstated (DC3) |
| The opening check covers both shapes | Asserted, not instrumented: the check's bullets name a procedure for shape one only (DC6) |
| The second shape is the worse one, three groundings | Groundings exist; 310/060 and 310/080 match their one-line descriptions; 310/090's date is corroborated by its creation commit (`ef7f9878`, 2026-08-19) |
| Grounding: "within the hour … disclosed on its own initiative" | Corroborated in kind by subjects `b0f202de` (19:53 +1200) and `3832c32e` (22:27 +1200, "disclose the delta author's post-write contact with the brief-writer"); "within the hour" not checkable from un-barred records (DC8, held) |

No silent scope-cut found: each commit is the paragraph its subject names, nothing more. Text at
HEAD is identical to the landing text for all four paragraphs (paragraph compare of `git show
3b1cb23:<path>` against HEAD).

### Lens 3 — completeness and harvest

- Mirror sites (V3): the contact rule has no slot in `skills/review-brief/SKILL.md` (items 1–6 carry
  no provenance or contact line) nor in any `skills/review-drain/*` prompt; the census of
  2026-11-16 classes it "directive-only, invisible" (REV20). The allowlist rule's one operational
  copy lacks the non-scalar clause (DC4). The two-shapes rule is absent from the floor block and its
  stamped template copy (DC5). `GLOSSARY.md` has no entry for "disclosed contact" or "review chain"
  (N1).
- One home (V4): the contact rule's home is REVIEW.md rule 4, and CONCURRENCY's two lines point at
  it: sound. The allowlist refinement's *base* has no home (DC3). The two-shapes rule's home is
  PROPAGATION § *Check the parent's file first*: sound.
- Harvest: `tools/attribscan.py` already guards the FORM of an attribution to the principal (a
  partial mechanical half of shape two at atelier, warn-only until 2027-02-08); the paragraph does
  not point at it. Counsel under DC6.
- Tests that stay green on a broken delta: none of the three paragraphs has a test (all three
  census rows say directive-only), so mutation has nothing to bite on; discharged with that ground.

### Lens 4 — security and privacy

- Design altitude: the SECRETS paragraph is itself a privacy-by-design rule and its mechanism is
  right (a typed hole in an allowlist is an unfiltered surface). Its weakness is that it binds only
  a session that already allowlists (DC3). The REVIEW paragraph's exposure surface is the review
  record itself: a paraphrased disclosure lets the receiver's judgement stand in for the evidence
(DC2). - Code altitude: the delta is prose; `/security-review` cannot reach markdown and the tree
  carries my own pending edit to this brief, so it was not run (REVIEW.md § lens 4, both cautions).
  Checked by hand against the rule's class instead (ASVS V8 data protection, "do not log or expose
  sensitive data"): the repo's one provider-read allowlist, `instruments/ccmail` `publicShape`
  (filename, mimeType, size) and the message rows (id, From, Date, Subject, sizeEstimate), keeps
  scalars only; `instruments/ccapple` projects named SQLite columns (no `SELECT *`). No instrument
  in this repo keeps a non-scalar field from a provider read. Nothing in the delta over-collects.
- Nothing private is quoted in this verdict; child repos are not named.

### Standing checklist V1–V7

- **V1** No claim stronger than its evidence: DC6 ("binds it identically"), DC8 (held), N2.
- **V2** Re-run every recorded proof: see the re-run ledger; both lines re-run, both clean.
- **V3** Swept to every mirror: DC4, DC5; the contact rule reaches no skill or template (lens 3).
- **V4** One fact, one home: DC3 (a refinement whose base fact has no home); otherwise sound.
- **V5** No internal contradiction: DC1, DC2, DC7 (REVIEW.md rule 4 against its own clauses);
  cross-references checked for the rule reached, not only the file: CONCURRENCY.md:762 →
  REVIEW.md rule 4 reaches lines 280–295; CONCURRENCY.md:642 → § *What the channel is not* reaches
  line 760; PROPAGATION.md:612–617 → `310/090`, `310/080`, `310/060` all exist and the two I may
  read match. N4 (CONCURRENCY.md:641) read twice, no contradiction.
- **V6** Security and privacy: lens 4 above; `/security-review` discharged with grounds.
- **V7** Spawn provenance: the brief states it (§ *Spawn provenance*) and this verdict repeats it.

### Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `ef9e975` review/concurrency: disclosed contact | yes (`coldsweep --commit`, two `--path` hits, two board files left out unread) | DC1, DC2, DC7, DC8, N1, N4 |
| `ba4e95b` secrets: non-scalar under a kept field | yes (one `--path` hit, two board files left out unread) | DC3, DC4, N2, N3 |
| `3b1cb23` propagation: both shapes | yes (one `--path` hit, three board files left out unread, the queue pointer among them) | DC5, DC6 |

### Findings

**DC1 — MODERATE — the recorder is wrong for one of the two directions the rule covers.**
`REVIEW.md:284–291`. "Contact between a delta's author and any session in that delta's review
chain … is permitted only as disclosed contact: the **receiving** session records it." "Between"
covers both directions; the grounding and the reasoning assume author-initiated contact. When a
reviewer or brief-writer messages the author (a question, a request for a repro), the receiver is
the author, whom the same sentence names the interested party whose self-report is the weaker
artefact, and who has no legitimate write to the review record (rule 4 bars it from the chain). As
worded the rule either assigns the record to the one party it says should not keep it, or leaves
chain-initiated contact unrecorded. *Counsel:* "recorded by the chain-side session, whichever
party sent the message", and say plainly whether chain-initiated contact is permitted at all (the
criterion's spirit says a reviewer that asks the author a question has been instructed by the
answer).

**DC2 — MODERATE — a paraphrase is allowed where the sibling clause demands verbatim.**
`REVIEW.md:286–287` requires "what was said and what changed as a result". Two sentences earlier
(`REVIEW.md:265–268`, RR2) the same rule requires the orchestrator's spawn prompt and release
message "verbatim or as an attached file", and `CONCURRENCY.md:743–748` holds that a source that
exists only in a context window is not a primary source. The rule's own justification is that a
correction and a framing cannot be told apart from outside; a paraphrase of the message is the
receiver's judgement that it was not framing, which is the judgement disclosure exists to let an
outsider make. The receiver's record is also a self-report; what makes it the stronger artefact is
the recorder's interest, and only a verbatim record removes the recorder's reading from the
evidence. *Counsel:* "verbatim or as an attached file", the same words as RR2, and the channel
transcript kept where one exists (`CONCURRENCY.md` § *The channel crosses publication
boundaries*, abridged on the way into a public record with the abridgement stated).

**DC3 — MODERATE — the refinement hangs off a duty no doctrine states.** `SECRETS.md:367–370`
binds "a session reading a provider API that allowlists the fields it keeps before printing". No
doctrine requires a session to allowlist at all: `grep -rn -i allowlist docs/method` finds only this
paragraph, the command allowlist (`TOOLBOX.md`) and the permission allowlist (`AUTONOMY.md`). A
session that prints a provider read raw into its transcript breaks nothing in `SECRETS.md`, and
the only statement of the base duty in the repo is one skill prompt
(`skills/review-drain/orchestrator-prompt.md:23`). The brief names the worst failure as a rule that
reads as a defence and is not; this one defends only sessions that already defend themselves.
*Counsel:* one sentence before this paragraph stating the base duty (a session that prints a
provider read keeps an allowlist of fields, because the transcript is a durable, archived surface:
`instruments/ccarchive` captures it), and the drain prompt pointed at it.

**DC4 — MODERATE — the rule's one operational copy omits the clause the rule exists for.**
`skills/review-drain/orchestrator-prompt.md:23`: "allowlist fields before printing because provider
reads can carry credentials", nothing on a non-scalar value under a kept field. That prompt is what
every drain reviewer is handed for live reads; a reviewer following it to the letter reproduces the
`320/090` failure exactly (a kept field that turns out to hold an object). V3 names skills as mirror
sites. *Counsel:* add "a non-scalar value under a kept field is un-allowlisted: drop it or never
print it whole (`SECRETS.md` § *Exposure*)" to that line; the drain session's own fuller wording
(which my spawn prompt carried) shows the gap is already being patched by hand outside the repo.

**DC5 — minor — the floor block carries shape one and not shape two.** `PROPAGATION.md:605–617`
grounds the rule in a child; the text a child session reads is the floor block
(`PROPAGATION.md:203–222`, stamped at `docs/build/templates/CLAUDE.md:95–100`), which says "Check
the parent's actual file first — this block is a lossy summary" and nothing about closing a house
question. A child that believes a house question is settled does not think it is reporting a
doctrine problem, so the bullet's trigger never fires and it never reaches the canonical section.
Minor rather than MODERATE because the floor block is single-sourced and stamped, so the fix is
one clause in one place. *Counsel:* "and a house question is closed by the house: never record an
open one as settled locally" in the same bullet.

**DC6 — minor — "binds it identically" is a principle without its procedure.**
`PROPAGATION.md:605–608`. The check's three bullets (`PROPAGATION.md:594–603`) tell shape one what
to open (the canonical file, at the owning section) and what to file (a findability defect). For
shape two the paragraph gives the principle (a house question is closed by the house; an adjacent
ruling is not a ruling on your question) and no step: which record to open (the board item that
holds the question, read for its state), and what to do if it is open (file evidence to it, never a
closure). *Counsel:* a fourth bullet, and a pointer to `tools/attribscan.py`, which already guards
the form of an attribution to the principal and is the mechanical half of this shape at atelier.

**DC7 — minor — the chain list omits the orchestrator rule 4 itself defines.** `REVIEW.md:284–285`
lists "brief-writer, reviewer, reconciler". `REVIEW.md:255–268` gives the off-tier orchestrator a
role in the same chain: it chooses the barred set and times the release. An author's message to the
orchestrator ("release the sibling", "bar this file too") is contact with the chain that the list
does not name; the reviewer's verbatim record of the orchestrator's messages would show the effect
but not the contact. *Counsel:* add "orchestrator" to the list.

**DC8 — note — "within the hour" is held, not decided.** `REVIEW.md:291–292`. The un-barred record
corroborates the event (subjects `b0f202de`, `3832c32e`, same day) but the disclosure commit is
2 h 34 min after the section merged, and the message time lives in the barred brief. Checked at
reconcile; becomes a V1 finding only if the record does not bear "within the hour".

**N1 — note.** `GLOSSARY.md` has no entry for "disclosed contact" or "review chain"; both are terms
of art the rule introduces.

**N2 — note.** `SECRETS.md:370` "recurse the allowlist into it": a field allowlist written for the
parent object does not describe the child object's fields, so recursing it is under-specified; the
safe default the sentence already offers first is "drop it". Counsel: "recurse an allowlist written
for that object's type".

**N3 — note.** Home of the SECRETS paragraph: § *Exposure* is defensible; a reader looking for an
output-side rule would look in § *Right plane, never the wrong one* first. Counsel: a one-line
pointer there.

**N4 — note.** `CONCURRENCY.md:641–642` (a later landing, `280/050`): "Talk-first never reaches a
cold reviewer. A message from a delta's author into its review chain is disclosed contact" reads at
first as a ban beside a permission; on a second read the first sentence is about the talk-first
protocol not applying, not about messages. No contradiction; the first sentence could say "the
talk-first protocol".

### Overall

**PASS-WITH-FINDINGS — 0 MAJOR / 4 MODERATE / 3 minor / 5 note** (DC1–DC4 MODERATE; DC5–DC7 minor;
DC8 and N1–N4 notes). The three
paragraphs are grounded, placed at the right altitude, and unchanged since landing; none is wrong in
what it says. The defects are in what each leaves out: a recorder for the other direction and a
verbatim standard (REVIEW), the base duty and its one operational copy (SECRETS), the procedure and
the floor-block mirror (PROPAGATION). All are the principal's to decide (rule 3); nothing applied.

### Re-run ledger

| Line | Result |
|---|---|
| `git merge-base --is-ancestor 3b1cb23 HEAD` | exit 0 |
| `python3 tools/pathscan.py --root . docs/method/REVIEW.md docs/method/SECRETS.md docs/method/PROPAGATION.md docs/method/CONCURRENCY.md` | ✓ clean, exit 0, 45 path references checked |
| `nice -n 10 python3 -m unittest discover -s tools` (python3 = 3.14.6, first on `PATH`) | python exit 0 (`pipestatus[1]`), about 19 minutes under load 6–9. My `\| tail -6` kept a selftest's late-flushed stdout rather than unittest's "Ran N tests / OK" line, so the test count is not in my record; the exit code is. Not re-run (the brief allows the full line once; a second run on a 16 GB laptop with other passes live is a load cost I did not take) |
| `python3 tools/coldsweep.py … 'disclosed contact\|un-allowlisted\|non-scalar\|closing an open house question'` | exit 0, 10 hits over 747 files, 1018 excluded as barred; no `--include-barred` |
| `/security-review` | NOT RUN: prose delta the scanner excludes, and the tree carried my own pending edit to this brief |

### Follow-up checklist

- [ ] The principal rules on DC1–DC8 and N1–N4 (rule 3); counsel is beneath each.
- [ ] Reconcile (act 2): the sibling's 7 questions and 1 fact; the three commit bodies; the barred
      intent records; DC8 checked against the 2026-08-17 brief's provenance.
- [ ] The review log (user-local during the pass) is appended to this file at the fold.

### Reconcile — act 2, 2026-11-22 UTC

Opened after act 1 was committed (`90d55919`), on the orchestrator's release message (process
only: the sibling's path, what is now open, the shape of this section, no git writes, no fold; its
text is in the review log appended at the fold). Read in this act: the held sibling (7 questions,
1 fact, the brief-writer's re-run results); the three commit bodies (`git log -1 --format=%B`); the
three intent records in full; the queue pointer `160/999`; and, for DC8, the 2026-08-17 channel
brief's provenance (lines 33–47, 255–260) and its verdict at lines 484–492, plus
`docs/reviews/2026-08-21-0820-pointing-up-cold.md` by grep for the closure shape. No act-1 text is
revised; where the record changes a finding's weight, it is said here.

**The brief-writer's re-run results against mine.** Pathscan: both clean. Suite: the sibling
records 2,643 tests OK in 1,167 s on Python 3.14.6; mine exited 0 on the same interpreter in about
the same time, count uncaptured (act 1, re-run ledger). Consistent. The sibling's note that the
system Python 3.9.6 cannot import four test modules is outside this delta.

**The author's account (commit bodies, intent records) against each finding.**

- **DC1 stands.** The body of `ef9e975` says "(author to brief-writer, reviewer or reconciler)":
  the author's own account is one-directional, which is the framing the wording inherited.
- **DC2 stands, strengthened.** The instance the rule generalises from is itself a paraphrase: the
  channel brief's disclosure 3 (lines 37–45) gives the gist of the author's note, not its text. The
  rule encodes the instance's form, including its weakness.
- **DC3 stands, sharpened.** `320/090` says the allowlist-before-printing discipline is "the
  discipline the child's own doctrine prescribes" and that "the child already carries the full rule
  locally in its own wording"; it proposed one sentence and the worker landed exactly one. So the
  base duty exists in a child's doctrine, is stack-independent by § *The test*, and the house never
  adopted it. Counsel: the child's wording is one message away for the applier.
- **DC4 stands.** No account touches the drain prompt.
- **DC5 and DC6 stand.** `310/090` offered a symmetric check ("is this the house's to decide?",
  with two consequences); the worker added a paragraph beneath the asymmetric bullets instead, and
  neither route reached the floor block. The item's candidate wording is a ready counsel for DC6.
  The body's claim that `310/050`'s pass covers no part of this shape is borne out: that verdict's
  only "clos-" hits are "closing-the-loop" (lines 27, 236, 272, 400).
- **DC7 stands.** `280/040` names the same three roles; the orchestrator is absent there too.
- **DC8 is decided: minor (V1), formed at reconcile from the record.** The channel section merged
  at 07:58 UTC (`46dd5a0b`, `b0f202de` at 07:53) and the author's message is dated "~1010 UTC" in
  the channel brief's disclosure 3: about 2 h 12 min, not "within the hour". The phrase is in
  `REVIEW.md:291` and in `280/040`'s first lines; the event is real, its timing is overstated.
  Counsel: "the same morning". (Aside, not this delta's: the channel brief says the contact came
  "after this brief was written and committed" while its commit `89963d2e` is 10:27 UTC and its
  verdict's *Written* line reads 13:36 UTC; the brief's own clock is loose.)
- **N1–N4 stand.** The 2026-08-18 channel pass's verdict (lines 484–492) found this gap in its own
  words ("the section says nothing about it"); the delta answers it without citing it, which is a
  traceability note (R1 below).

**The sibling's seven questions, each against my findings.**

1. *The receiver may not know the sender is the author.* Not raised in act 1. It is answerable: the
   hello message and claims carry session ids, and the intent record and pointer name the author's
   (`160/999` names `4c65083c`). But the rule does not tell the receiver to check, and a receiver
   that records only contact it knows to be the author's records less than it should. **DC9 —
   minor, formed at reconcile, prompted by the sibling:** the rule binds on an identification it
   never asks for. Counsel: the receiver records every message it gets during the pass, by sender
   id, and marks any that match the delta's author; this also resolves DC1's recorder question.
2. *Does disclosed contact that changed the brief still meet the criterion?* Not raised in act 1
   as its own point (DC1's counsel brushed it). The rule makes disclosure the remedy and says
   nothing about what the record decides: a disclosed framing that changed a brief has instructed
   the chain, which the criterion forbids, yet the pass is not said to be withdrawn, degraded or
   referred. **DC10 — minor, formed at reconcile, prompted by the sibling:** who judges a disclosed
   contact, and against what, is unstated. Counsel: the principal judges at acceptance, with
   § *A pass that is not accepted is withdrawn* as the consequence; the receiver's record is what
   he judges on, which is DC2's reason for verbatim.
3. *Who else counts; is "review chain" defined?* DC7 (the orchestrator) and N1 (no glossary
   entry). A mid-turn relay by the principal is his own word and not contact under this rule; a
   batch scheduler is a spawner and rule 4's criterion already governs it.
4. *Is "scalar" the wrong line?* Partly raised as N2; the sibling's point is sharper and I take it.
   A kept scalar can be the secret: a PEM string, a token pasted into a description field, a
   serialised object in a string. The delta's sentence is true (a kept object is unfiltered) and
   partial (a kept scalar is filtered by name only). **DC11 — minor, formed at reconcile, prompted
   by the sibling:** the type line is necessary and not sufficient; the paragraph presents it as the
   defence. Counsel: one clause pairing it with a pattern check on kept scalars, which the house
   already has as `tools/secretscan.py`.
5. *An empty allowlist at depth passes the value whole.* Covered by N2: "recurse the allowlist into
   it" is under-specified. Read literally, an empty allowlist keeps nothing; the hazard is a missing
   one falling back to print-whole. N2's counsel stands.
6. *Is "the worse one" carried by the grounding?* Not raised, and I do not raise it: `310/090`
   argues the mechanism (an absence is unnoticed; a wrong artefact is actively defended) and
   `310/080`'s four-week survival is the measured instance. DC6 is about the missing procedure, not
   the comparative.
7. *How does a child tell a house question from its own?* The paragraph does not say; § *The test*
   is written for rules. This is DC6's gap seen from the child's side; counsel there gains one
   clause: the same test applies to a question as to a rule.

**The sibling's fact** (three commits in one run, no pass since) matches my since-landing check
(63 later commits on the paths, none touching the four paragraphs).

**R1 — note, formed at reconcile.** The 2026-08-18 channel pass found this gap (its verdict, lines
484–492) and the landed rule answers it without citing that finding; `280/040` cites only the
instance. Traceability only.

**Overall, restated.** PASS-WITH-FINDINGS — 0 MAJOR / 4 MODERATE / 7 minor / 4 note. Act 1's
tally was 0 / 4 / 3 / 5; at reconcile DC8 moved from note to minor on the record, and DC9, DC10,
DC11 (minor) and R1 (note) were formed here, each marked as such. Nothing applied; every finding
is the principal's to decide (rule 3). The orchestrator folds the sibling in below this section.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-22)

*Released to the reviewer only after its act-1 findings were committed (locally `90d55919`, the
hash the reviewer's text cites; landed as `30daf253` when rebased with this fold); folded here
verbatim (headings demoted two levels, one line over 100 columns wrapped) and the sibling file
removed, per the brief. The orchestrator, headless Opus 5.5 session `a9a9eba8` started
by drain session `eca14b23`, held the partition, formed no finding and wrote no severity; drain
session `eca14b23` wrote no brief and no delta and started no brief-writer for this pass.*

### Sibling to the contact-scalar-allowlist-closed-questions cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-09-0207-contact-scalar-allowlist-closed-questions-cold.md`, held
under `docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief
are committed.** Written 2026-11-09 UTC by the brief-writer, session `d4a0fcf3` (Opus 5.5), named in
the brief's provenance; it forms no finding and assigns no severity. Fold this file in below the
reconcile and delete it at phase 2.

#### Re-run results held back from the brief

Run once by the brief-writer, 2026-11-09 UTC, from the worktree root at `b1f9499`, machine load
averages 10 to 22 throughout:

- `python3 tools/pathscan.py --root . docs/method/REVIEW.md docs/method/SECRETS.md
  docs/method/PROPAGATION.md docs/method/CONCURRENCY.md`: exit 0 (suppressed: 0 by allow-marker · 0
  file(s) by .pathscanignore · 0 rec).
- Full suite, `nice -n 10 python3 -m unittest discover -s tools`, Python 3.14.6: 2,643 tests, OK,
  exit 0, 1,167 s. An earlier run on the system Python 3.9.6: 2,307 tests, 4 import errors
  (`test_floor`, `test_floorfleet`, `test_personal_data`, `test_precommit`: a module-level `str |
  None` annotation) and 1 timeout under load (`test_spellscan.BoundedMemory`, which passed alone on
  3.14).

#### Prior records on nearby surfaces (named by filename, not opened unless the brief says so, not
exhaustive)

- `docs/reviews/2026-08-17-1000-channel-doctrine-cold.md`

#### Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. Disclosed contact: nothing obliges the sender to say it was the author. A receiver who does not
   know the message came from the author cannot record it. Is the rule enforceable from the
   receiving end, as it claims?
2. "Permitted only as disclosed contact" against rule 4's "a session the author neither started nor
   instructed". Does disclosed contact that changes the brief still meet the criterion? The
   grounding is a message that changed nothing.
3. Who else counts: the orchestrator, a batch scheduler, a mid-turn relayed by the principal? Is
   "review chain" defined?
4. "Non-scalar": a JSON string holding a serialised object is a scalar. A base64 string? A very long
   string? Is "scalar" the wrong line?
5. "Recurse the allowlist into it": for a child that does, an empty allowlist at the depth where the
   secret sits passes it whole.
6. "The second shape is the worse one": does a three-item grounding carry the comparative, or is it
   asserted?
7. `310/090`'s check says a house question is closed by the house. How does a child tell a house
   question from its own before it closes one? Is that the same test as *whose rule is it*?

#### Facts held back from the brief

- The three commits landed in one queue run, and no pass has read them since.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

*Form fixes only: headings demoted two levels; 47 lines over 100 columns wrapped at word
boundaries, no word changed. No public-repo gate blocked a token, so no placeholder was needed.*

### Review log — atelier 160/999 cold pass (worktree atelier-160-999-2000)

Reviewer: Fable 5.1. Orchestrator session a9a9eba8; drain session eca14b23. Act 1 begun 2026-11-22
20:01 UTC.
Commands run from the worktree root "/Users/mike/worktrees/fable/atelier-160-999-2000/atelier" via
`git -C` / absolute paths.

#### Steps

- 20:01 UTC `uptime` → load 4.43 7.00 6.84 (16 GB laptop, several passes). `git status --short` →
  only the expected deletion of the `.deferred.md` sibling. HEAD 74b2f65d (claim commit).
- Read brief `docs/reviews/2026-11-09-0207-contact-scalar-allowlist-closed-questions-cold.md` whole
  (209 lines). Read `docs/method/REVIEW.md` whole (836 lines) for verdict shape and rule 4 text.
- `git merge-base --is-ancestor 3b1cb23 HEAD` → exit 0 (tree holds the delta).
- `python3 tools/coldsweep.py --root <wt> --commit ef9e975 --path docs/method/REVIEW.md --path
  docs/method/CONCURRENCY.md --path docs/method/SECRETS.md --path docs/method/PROPAGATION.md` →
  subject, stat, diff; body not printed; 2 board files left out. Diff: +16 lines REVIEW.md (rule 4,
  "Contact after the spawn is disclosed contact"), +3 lines CONCURRENCY.md (§ What the channel is
  not, "not a side door into a review").
- Same for `ba4e95b` → +11 lines SECRETS.md (§ Exposure, "On the output side, a field allowlist…");
  2 board files left out.
- Same for `3b1cb23` → +13 lines PROPAGATION.md (§ Check the parent's file first, "The check covers
  both shapes…"); 3 board files left out (incl. the queue pointer 160/999).
- `git log --oneline 3b1cb23..HEAD -- <4 paths>` → 63 later commits on the delta paths.
  Paragraph-level compare (python, landing text via `git show 3b1cb23:<path>` vs HEAD): CONCURRENCY,
  SECRETS, PROPAGATION paragraphs IDENTICAL; REVIEW.md delta paragraph (HEAD lines 280–295)
  identical by eye (the list block around it changed: rule 2's start-up-reading paragraph, rule 4's
  RR2 orchestrator clause, pointerscan clause, 320/420 pin clause). Scratch copies deleted.
- Located at HEAD: REVIEW.md:280, CONCURRENCY.md:760 (and a second mirror at 642 from a later
  landing, 280/050), SECRETS.md:367, PROPAGATION.md:605.
- Brief's sweep: `python3 tools/coldsweep.py --root <wt> --also-exclude ×4 'disclosed
  contact|un-allowlisted|non-scalar|closing an open house question'` → exit 0, 10 hits over 747
  files, 1018 excluded as barred. Hits: CHANGELOG.md:916, docs/ROADMAP.md:234, CONCURRENCY 642/761,
  PROPAGATION 606, REVIEW 172/280/286, SECRETS 369/370. No `--include-barred` used.
- Re-run: `python3 tools/pathscan.py --root <wt> <4 paths>` → ✓ clean, exit 0, 45 path refs checked.
- `ls tools | grep -i scan` → datescan.py and wrapscan.py exist (to run on the brief after writing).
- Intent records, first line only (per the brief): 280/040, 320/090, 310/090 all `[x] DONE
  2026-11-03 (wt: atelier-qr-4c65-doctrine2)`; titles match the delta's subjects.
- Commit subjects 2026-08-16..19 (`git log --format='%h %ad %s' --date=short`): `b0f202de 2026-08-17
  19:53 +1200 method: the channel becomes a concurrency primitive`; `46dd5a0b 19:58 merge PR #26`;
  `3832c32e 2026-08-17 22:27:50 +1200 reviews: channel brief — disclose the delta author's
  post-write contact with the brief-writer`; `89963d2e 22:27:50 reviews: three cold-pass briefs
  written…`. Corroborates the REVIEW.md grounding (an author contacted the brief-writer; the
  brief-writer disclosed it). "Within the hour" cannot be checked from subjects alone: the
  disclosure commit is 2h34m after the merge; the message time is in barred records. → reconcile
  item.
- Read CONCURRENCY.md 630–650 and 735–775 (the channel sections); headings list. Read SECRETS.md
  headings, 207–240, 330–380. Read PROPAGATION.md headings, 575–640, floor block 203–222.
- 310/060 and 310/080 (not barred; first 30 lines each): 310/080 = a capture recorded the
  assistant's `[-]`/`[^]` proposal as the principal's and it was quoted forward; 310/060 = the
  2026-07-23 "keep three" answer was to "should the bracket carry the disposition", read as refusing
  the indexing question never put. Both match the PROPAGATION paragraph's one-line descriptions.
- `git log --diff-filter=A -- <310/090 path>` → created `ef7f9878 2026-08-19 12:01 +1200`. The
  paragraph's "2026-08-19" is corroborated.
- Mirror-site grep (`grep -rn -i -E 'disclosed contact|review chain|non-scalar|un-allowlisted|house
  question|adjacent is not|before printing|allowlist'` over skills/, docs/build/, tools/README.md,
  instruments/, docs/method/, README.md): the only operational copy of the allowlist rule is
  `skills/review-drain/orchestrator-prompt.md:23` ("allowlist fields before printing because
  provider reads can carry credentials"), with no non-scalar clause. No copy of "disclosed contact"
  in any skill or template. `docs/method/census/2026-11-16-1142-record-review-concurrency.md:140`
  row REV20 classes the contact rule "directive-only | invisible"; census 1204 row PRO23 classes the
  closed-question rule "directive-only | diff, judgement; attribscan sees only an attribution word".
- GLOSSARY.md: no entry for "disclosed contact" or "review chain"; "Provenance" at line 45.
- `grep -rn -i 'allowlist' docs/method` → besides SECRETS 367–375 only TOOLBOX (command allowlist)
  and AUTONOMY (permission allowlist). No doctrine states the base duty to allowlist fields of a
  provider read before printing; the SECRETS paragraph is conditional on a session that already
  does.
- Floor block (PROPAGATION 203–222) and its stamped copy `docs/build/templates/CLAUDE.md:97`: "Check
  the parent's actual file first — this block is a lossy summary". Shape one only; nothing on
  closing a house question.
- `skills/review-brief/SKILL.md` 55–135: items 1–6 carry no provenance or contact slot; provenance
  appears only as V7 in the standing checklist line (133). `skills/review-drain/` has no "contact"
  text.
- `tools/attribscan.py` 1–30: checks the FORM of an attribution to the principal (quote, citation or
  demotion nearby), not its truth; partial guard for shape two at atelier only.
- Code altitude for the SECRETS rule: `instruments/ccapple` reads local SQLite with named columns
  (no `SELECT *`), scalars by construction, not a provider API. `instruments/ccmail:1144
  publicShape(a)` keeps `{filename, mimeType, size}` of a Gmail attachment part — all scalar in the
  API schema; 1100–1112 message rows keep id/thread/date/from/subject strings. Conforms to the new
  rule; no non-scalar kept field found.
- Suite: `(cd <wt> && nice -n 10 python3 -m unittest discover -s tools)` with `python3` =
  /Library/Frameworks/Python.framework/Versions/3.14/bin/python3 (3.14.6), uptime load 4.93 before.
  Still running past 600 s; moved to background, result recorded below when it ends.

#### Candidate findings (act 1)

- DC1 (REVIEW.md:285–291) "the receiving session records it": when the chain side initiates
  (reviewer asks the author a question), the receiver is the author, whom the same sentence calls
  the interested party whose self-report is the weaker artefact, and who has no legitimate write to
  the review record. Rule as worded yields the wrong recorder in one of the two directions "contact
  between" covers. Criterion: V5 (agrees with itself), V1.
- DC2 (REVIEW.md:287) "what was said and what changed" permits a paraphrase; rule 4's orchestrator
  clause (REVIEW.md:265–268) demands the spawn prompt and release message "verbatim or as an
  attached file", and CONCURRENCY.md:743–748 says a source that exists only in a context window is
  not a primary source. A paraphrase of a framing message is the receiver's judgement of whether it
  was framing, the judgement disclosure exists to let an outsider make. Criterion: V5, CONCURRENCY §
  channel crosses publication boundaries.
- DC3 (SECRETS.md:367–370) the paragraph is conditional ("a session … that allowlists the fields it
  keeps") and no doctrine states the base duty; a session that prints a provider read raw breaks
  nothing in SECRETS.md. The only operational statement of the base duty is one skill prompt.
  Criterion: lens 3, V4 (the fact has no home), brief's "a rule that reads as a defence and is not".
- DC4 (skills/review-drain/orchestrator-prompt.md:23) the one mirror of the allowlist rule carries
  "allowlist fields before printing" without the non-scalar clause, so a reviewer following it
  reproduces the 320/090 failure exactly. Criterion: V3.
- DC5 (PROPAGATION.md:605–609 vs 203–222 and templates/CLAUDE.md:97) the floor block, the one text a
  child session reads, carries shape one ("Check the parent's actual file first") and not shape two;
  the paragraph's own grounding is a child. Criterion: V3 (child templates are named mirror sites).
- DC6 (PROPAGATION.md:605–608) "the check binds it identically" is asserted; the three bullets of
  the check name the procedure for shape one (open the canonical doctrine file at the owning
  section) and none for shape two (open the board item that holds the question and read its state).
  Criterion: V1.
- DC7 (REVIEW.md:284–285) the chain list "brief-writer, reviewer, reconciler" omits the orchestrator
  rule 4 itself defines (it chooses the barred set and times the release). Criterion: V5 with
  REVIEW.md:255–268.
- DC8 (REVIEW.md:291–295, grounding) "within the hour" is unverifiable from the un-barred record;
  the disclosure commit is 2h34m after the section merged. Check at reconcile against the barred
  brief. Criterion: V1 (held, not decided, in act 1).
- Note: CONCURRENCY.md:641–642 "Talk-first never reaches a cold reviewer. A message … is disclosed
  contact" (a later landing, 280/050) reads at first as "never" against the rule's "permitted";
  resolved on a second read (talk-first's protocol does not apply; the contact rule does). Note
  only.
- Note: REVIEW.md:290–291 "a self-report is the weaker artefact" — the receiver's record is also a
  self-report; what makes it stronger is the recorder's interest, not its form. Folded into DC2's
  counsel.
- Sound, checked: SECRETS 320/090 title matches ("a response-field allowlist leaks through
  non-scalar fields"); PROPAGATION's three groundings exist and 310/060, 310/080 match their
  one-line descriptions; cross-refs CONCURRENCY:762 → REVIEW rule 4 (reaches the rule at 280),
  CONCURRENCY:642 → § What the channel is not (reaches 760), PROPAGATION → 310/090, 310/080, 310/060
  (all exist); pathscan clean; delta text unchanged since landing; the one atelier instrument with a
  provider-read allowlist (ccmail publicShape) keeps scalars only.
- Suite ended 20:27 UTC: python exit 0 (`pipestatus[1]`); my `| tail -6` kept a selftest's
  late-flushed stdout, so unittest's "Ran N" line is not in the capture; count unrecorded, exit code
  is. Not re-run (load 9, brief allows the line once).
- `grep -rn -i -E 'object raw|certificate object|dump a user' skills docs/method tools/README.md` →
  no hits: the object-level ban in my spawn prompt came from outside the repo; DC4 stands.
- Act 1 written to the brief below `---` (Status line updated; verdict with provenance, lenses,
  V1–V7, per-commit ledger, DC1–DC8 + N1–N4, overall, re-run ledger, follow-ups). Severities:
  DC1–DC4 MODERATE, DC5–DC7 minor, DC8/N1–N4 note. Overall PASS-WITH-FINDINGS 0/4/3/5.
- Scans on the brief: `tools/datescan.py` ✓ clean (478 lines); `tools/wrapscan.py --limit 100` ✓
  (file is in .wrapscanignore so it scanned nothing; checked by awk instead: no prose line of mine
  over 100 columns; over-width lines are the brief-writer's commands, title and paths, and my table
  rows); `tools/reviewscan.py` ✓ (1 brief keeps deferred material out).
- Act 1 ends 2026-11-22 ~20:30 UTC. Waiting for the orchestrator's release message. Nothing barred
  opened.

#### Act 2

- Release message from orchestrator session a9a9eba8 (verbatim, process only): "Act 1 is committed
  (90d55919, brief file only, every commit gate green); act 2 may now begin. The held sibling is
  this one file, and act 2 may now read it:
"/Users/mike/.claude/fable-held/atelier--2026-11-09-0207-contact-scalar-allowlist-closed-questions-cold.deferred.md".
  The brief's other rule-2 barred records (its Deferred reading section) and the delta commits'
  message bodies are now open to you as phase 2 says. Append `### Reconcile` beneath your verdict in
  the brief, never revising act-1 text; add your act-2 steps to the same review log. Do NOT fold the
  sibling in or delete anything: the orchestrator folds. Same rules as before (no git writes, no
  live writes, niced single-process tests, public-repo wording, dates from `date -u`, run the date
  scanner on the brief before finishing). End with "ACT 2 SAVED"."
- 20:32 UTC `git log -1` → HEAD 90d55919 "review 160/999: act 1 of the cold pass"; `git status
  --short` → only the sibling's deletion.
- Read the held sibling at the path the release named (whole): 7 seeded questions, 1 fact,
  brief-writer's re-run results (pathscan exit 0; suite 2,643 tests OK, 1,167 s, Python 3.14.6; four
  import errors on the system 3.9.6), one prior record named by filename.
- Read commit bodies `git log -1 --format=%B` for ef9e975, ba4e95b, 3b1cb23. Read intent records
  280/040, 320/090, 310/090 whole, and the queue pointer 160/999 whole.
- `docs/reviews/2026-08-17-1000-channel-doctrine-cold.md` lines 33–47 (disclosure 3: author's
  message "2026-08-17 ~1010 UTC", one factual note, nothing changed), 255–260 (Written 13:36 UTC),
  484–492 (the pass's finding that the section says nothing about author→chain messages).
- `TZ=UTC git log -1 --date=iso-local` → b0f202de 07:53:02 UTC, merge 46dd5a0b 07:58:07 UTC. Message
  ~10:10 UTC ⇒ ~2 h 12 min after landing: "within the hour" (REVIEW.md:291, 280/040) not borne out.
  DC8 decided minor (V1) at reconcile.
- `ls docs/reviews | grep -i pointing` → 2026-08-21-0820-pointing-up-cold.md; grep
  'clos(e|ing|ure)|settled|second shape|adjacent' → only "closing-the-loop" (lines 27, 236, 272,
  400); PU-1 MAJOR at 155. The body's claim that the pass covers no part of the closure shape holds.
  (Its Status line still reads BRIEF ONLY while line 421 says the pass returned 1 MAJOR: stale line
  in an old record, not this delta.)
- Reconcile appended beneath the verdict; Status line updated (RUN 2026-11-22 UTC, both acts
  written; restated tally). Formed at reconcile, marked: DC8 → minor; DC9 (receiver not told to
  identify the sender; from sibling Q1), DC10 (what a disclosed contact decides, who judges; Q2),
  DC11 (kept scalar can be the secret; Q4), R1 note (channel pass's finding not cited). Q3 → DC7/N1;
  Q5 → N2; Q6 not raised, grounds given; Q7 → DC6 counsel. Restated overall: PASS-WITH-FINDINGS 0
  MAJOR / 4 MODERATE / 7 minor / 4 note.
- Scans on the brief: datescan ✓ clean (575 lines); no prose line after the divider over 100
  characters (python check); reviewscan ✓. `git status --short` unchanged shape (M brief, D
  sibling). No sibling fold, no deletion, no git write by me.
- Act 2 ends 2026-11-22 20:35 UTC.
