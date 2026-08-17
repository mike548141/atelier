# Cold pass — the channel as a concurrency primitive

**Pass type:** doctrine cold pass (REVIEW.md rule 4 — a 200-line addition to
`CONCURRENCY.md`, four seam edits to its existing sections, and a floor-block
clause that every child stamps; the wording is the applying session's own,
extracted from a child's practice at the principal's direction).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04). Checked
at selection: a session that cannot honour the bar stops rather than takes.
**Status:** BRIEF WRITTEN, REVIEW NOT RUN. The next cold session that passes
rule 4's criterion and the tier bar takes it — see *Spawn provenance*.

## Spawn provenance

- **Author of the work under review:** the session that wrote the section on
  2026-08-17 (wt: `channel-doctrine-0817`, landing commit `b0f202d`, merged
  to `main` in PR #26, with a pointer re-scope in `bb7c08f`; Opus 5 1M per the
  commit trailer). It extracted the doctrine from a public child's committed
  session records and from a four-round exchange it kept as a transcript.
- **Who wrote this brief:** an atelier session Mike opened 2026-08-17 at 0955
  UTC on the **Fable** tier under his standing cold-session instruction (*do
  any review work, any Fable-dependent work, write briefs for reviews that
  need them; a brief-writer never runs its own brief*). It authored no part of
  this delta, was neither started nor instructed by the authoring session, and
  has edited no file this delta touches. It wrote this brief from the diff of
  the three delta paths at `b0f202d` and from the queue pointer; it did **not**
  open the intent record, the kept transcript, the board section `280-…`
  beyond the pointer itself, or the child's records.
- ⚠️ **Three disclosures, all about the brief-writer.**
  1. **It read the `docs/SESSIONS.md` tail** at session onramp, before this
     brief was commissioned; the index entry for this delta is long and is
     the author's account of the section's structure and grounding. Rule-2
     barred material, read. It is why the intent record and transcript were
     left unopened, and why the seeded questions in the sibling are held to
     what the doctrine text itself says.
  2. **It read the landing commit's message in full.** Generate your own
     reading of the section before you weigh anything this brief says.
  3. **The delta's author contacted the brief-writer after this brief was
     written and committed** (a peer-session message, 2026-08-17 ~1010 UTC,
     on an unrelated board-number collision). It carried one factual note
     about this delta — that the queue pointer had been rescoped to paths, not
     the commit — and no instruction. The brief was already written against
     the rescoped pointer, so nothing in it changed as a result. Stated here
     because rule 4's provenance trail is what makes the pass auditable; the
     author has neither started nor instructed the taker, and the taker should
     confirm the same for itself.
- **Who takes the review:** the next cold session meeting rule 4's single
  criterion — a session the author neither started nor instructed — on the
  Fable tier, checked at selection. The taker repeats its own provenance in the
  verdict: how it was spawned, and its non-involvement with both the authoring
  session and this brief-writing session.
- **Orchestration shape:** the deferred material sits in the sibling
  `2026-08-17-1000-channel-doctrine-cold.deferred.md` (rule 1's split).
  Recommended: run under an orchestrator that holds the sibling's bytes and
  releases them only after the reviewer's findings are durably written. A
  taker working by hand opens the sibling as a deliberate second act after its
  findings are committed, and says so. Fold in and delete when the verdict
  lands.
- **The evidence problem, stated up front.** The section's *Bearing* cites a
  child's committed records and a transcript kept at
  `docs/sessions/2026-08-17-0343-cross-session-channel-transcript.md`. That
  file is the delta's primary source **and** it lives in the barred records
  tree. Phase 1 therefore reviews the doctrine as it stands — internally, and
  against the rest of `CONCURRENCY.md` and the method — and records each
  grounding claim as a claim. The transcript and the child's records are
  released with the sibling for reconcile, where the claims are checked
  against them. Say in the verdict which findings changed on that reading.

## What the work is

One commit, `b0f202d`, three delta paths (the fourth file in the commit's
doctrine set, `docs/build/templates/CLAUDE.md`, is the byte-identical stamp of
the `PROPAGATION.md` block). Reviewed at HEAD.

**`docs/method/CONCURRENCY.md` § *The channel — the coordination git cannot
carry* (new, ~155 lines).** Premise: every mechanism in the doc coordinates by
forcing a collision onto a shared line so git catches it, which cannot reach
the class where both parties are individually correct and neither has written
yet. Then: a one-line formulation (*a file map is a claim about your own
writes; a collision is a fact about somebody else's*); **three laws** (message
is awareness, artefact is authority — a reservation is valid at the instant it
is made and not after; the closing check runs *after* the push; a repair is
itself a claim and its tie-break must be a deterministic function of shared
public evidence — fewest inbound references moves — with a burned identifier
staying burned); **seven message classes** (hello with file set, holdings,
minting, gate-tightening changes, the principal's rulings, findings with
measurement labelled apart from diagnosis, farewell); **three shape rules**
(state what you have *not* done first; hand disposition to the receiver; make
an offer once); a *re-run, don't reason* rule with two evidence failures and a
cost clause (two of four rounds existed only to correct the earlier two); a
publication clause (abridge into the record and say so; a source that exists
only in an agent's context is not a primary source); and a *what it is not*
fence (not the claim, not a lock, not a channel for work).

**Four seam edits in the same file.** § *The trigger* gains an *ask, when a
channel exists* cue, plus two named blind spots of the dirty-tree backstop
(the shared index; a mid-rebase repository state, where `git push` can report
success while pushing nothing) and a *clean seconds ago is not clean now*
paragraph with a reverse-edit rule. § *Integration hygiene* gains
*absorption* — a rebase silently no-ops a shared value that independently
matches instead of conflicting on it. § *Claiming work* gains the file-set
announcement and *file-disjointness, not item-disjointness, as the unit of
parallel safety*, with a note on dispatching several workers. § *Surviving an
interrupted session* gains one sentence on a peer message's volatility.

**`docs/method/PROPAGATION.md` floor block, concurrency bullet (+3
sentences)** and the byte-identical stamp in
`docs/build/templates/CLAUDE.md`: announce a file set on open and answer
peers'; a message reserves nothing, check a shared allocator after the push;
the shared checkout's index and mid-rebase state are shared surfaces — stage
explicit paths and read staged hunk headers before every commit.

The commit deliberately left untouched an open finding against the CF3 yield
branch in the adjacent text (board item `030/140`), stating the fix is the
principal's to choose.

## Scope

Widest the work admits. This delta's subject is **coordination doctrine
extracted from one child's practice and made the method for every repo**, so
the reviewable question is not only whether each law is well stated but
whether it is *doctrine* — grounded, repeatable, and reachable by the sessions
it governs — or a well-written account of one repo's week. In scope: whether
the three laws are independent of each other and of the rules already on the
page (§ *Claiming work*'s claim-before-work, § *Integration hygiene*'s
allocate-then-push); whether the *tie-break by fewest inbound references* is
computable identically by both parties as claimed, and what happens on a tie;
whether the seven message classes are a closed set or an open one, and which
of them the artefact layer already carries; whether the section presupposes a
channel that exists on this platform (what *is* the channel — a harness
message primitive, a file, a commit? — and does the doctrine bind when none is
available); whether the floor sentence is followable by a child session that
has never read § *The channel* (the floor block is what children load, the
section is read on demand); whether the *reverse-edit, never checkout/
restore/stash* rule in § *The trigger* is consistent with the doc's earlier
CF3 yield branch and the open finding against it; and whether the doc's
existing KISS line survives a 155-line section that names three laws and
seven message classes.

**Non-goals, and neither fences the risk:** the ruling to add method plus
floor is the principal's and is not under review — only what was written; the
per-child adoption (`280/020`) is not under review; and no finding is decided
by the reviewer (rule 3), so the findings go to the principal's next ruling
round.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself
   first. Then: the section's premise is that git-collision mechanisms are
   *structurally* blind to a class of cost, and that only messaging catches it.
   Is that a structural claim or an empirical one from a five-session week —
   and does the doc distinguish them? Consider whether the right altitude is
   three laws in the method, or one sentence in the floor plus a pointer to a
   child's practice. Consider whether *message is awareness, artefact is
   authority* is a new law or a restatement of the doc's existing *the claim
   is the durable artefact* — and whether stating it twice strengthens or
   dilutes. Consider whether a doctrine section whose *Bearing* names a live
   child by name binds that child in a way the method's own locality rule
   (work lands in the repo it changes) would question.
2. **Correctness & quality.** Read the whole of `CONCURRENCY.md` at HEAD, not
   the diff — the seam edits sit inside sections that already had rules, and
   a diff hides what it did not touch. Check each cross-reference (`§ The
   channel, law 1/2`; `§ Stay in your lane`; `§ Surviving an interrupted
   session`) resolves to a section that says what the reference claims. Check
   the *hunk headers* instruction (`git diff --cached -U0 | grep '^@@'`) does
   what the text says on this platform. Check the floor sentence and the stamp
   are byte-identical (`tools/stampscan.py` and the templates test). Check
   the tie-break rule for the tie case and for the case where inbound
   references are in a peer's *unpushed* tree. Read the *what it is not* fence
   against the seven classes — do any classes carry work across the boundary
   the fence forbids?
3. **Completeness / harvest.** Every surface that states the pre-channel
   coordination story: `CONCURRENCY.md` (every section, for a sentence that
   now contradicts § The channel), `PROPAGATION.md`, the templates,
   `docs/build/` scaffolds (`create-repo` and any child `CLAUDE.md` it
   stamps), `SKILL`s or memory-facing text that tell a session what to do at
   open and close, `RECORD.md` on what a session record must carry (a
   farewell message's content is now specified twice?), `CHANGELOG.md` (is
   there an entry?), and the board (`280/020` for adoption; `030/140` for
   the CF3 finding left standing). Does any surface tell a session *how* to
   send a peer message on this platform, or is the channel assumed?
4. **Security & privacy** — mandatory. atelier is PUBLIC. The section names a
   child repo, dates, and describes what its sessions did; the publication
   clause says the transcript abridged a repo-name-plus-guard-inventory
   pairing. Check the doctrine text itself carries no private repo name, no
   machine path, no person, and nothing `PROPAGATION.md` bars from a public
   tree — and say whether naming a *public* child's coordination failures in
   the method is within the repo's own privacy rule. The message classes
   include *the principal's rulings* and *findings* crossing repo boundaries:
   test whether the section's publication clause is enough to stop a private
   repo's content crossing into a public one by message, or whether the
   floor sentence needs it too. The house security scanner reads the
   session's pending diff whatever path it is aimed at; this is a landed-delta
   review, so state the reach case that applied rather than assuming one. If
   the lens has no surface beyond these, discharge it in one explicit line
   with grounds.

## Re-run obligation

Re-run, do not read:

- The floor on **both** planes at HEAD, and the full Python and node suites.
  Lift the invocations from [`.githooks/pre-commit`](../../.githooks/pre-commit)
  and `.github/workflows/ci.yml` rather than guessing them.
- The byte-identity claim: `docs/build/templates/CLAUDE.md`'s stamped block
  against `docs/method/PROPAGATION.md`'s floor block via `tools/stampscan.py`
  and the templates test — say what the tool reports.
- The commit's own suite claim (1,324 tests green in the worktree, "exit code
  read directly after three earlier runs reported a green that belonged to
  the primary checkout or to `tail`'s exit code") — reproduce the count at
  HEAD and read the exit code yourself.
- The `git diff --cached -U0 | grep '^@@'` instruction, live, in a scratch
  clone with two staged hunks: say what it prints and whether a reader could
  compare it against "what you believe you wrote".
- The `plainscan` measurement over `CONCURRENCY.md` (advisory): the file is
  now the heaviest method doc on that scanner per the floor's own summary
  line — report the count as a measurement, not a finding.
- The grounding claims inside the section point into barred material (the
  transcript, the child's records); in phase 1 record them as claims and
  verify them at reconcile.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`
(the intent record and the kept transcript included — see *The evidence
problem* above), every prior verdict in `docs/reviews/` (the concurrency
passes especially), and the board section `docs/roadmap/280-…/` beyond the
pointer. Sweep the tree with `python3 tools/coldsweep.py`, whose default
exclusion is exactly that set; if you use `--include-barred`, disclose it. The
sibling `.deferred.md` holds those references and the brief-writer's seeded
questions; open it after your findings are committed. Reconcile after, never
anchor before. A taker whose own onramp has already read the `SESSIONS.md`
tail discloses that in the verdict, as this brief-writer has.

Reading the *doctrine* is not barred — `CONCURRENCY.md` whole, the floor
block, the stamp, and every method doc they cross-reference are the delta and
its context. What is barred is the author's narrative of why, and the
evidence it was drawn from.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `CH`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then open the sibling; append a
reconcile section (naming which findings moved on reading the transcript);
fold the sibling in below it and delete the sibling; finalise. Update the
queue pointer
(`docs/roadmap/280-cross-session-channel-mike-commissioned/030-rule-4-cold-pass-queued-the-channel-section.md`)
and rebuild the index in the same commit. Findings on this delta are the
principal's to decide (rule 3): record them, apply nothing.

---

## Verdict — phase 1 (findings written before any deferred material was opened)

**Written:** 2026-08-17 13:36 UTC · **Reviewed at:** HEAD `574f133` (the three
delta paths are byte-identical at `3b116b2`, the HEAD at write time — checked
by `git diff` between the two, zero lines) · **Landing:** `b0f202d`, pointer
rescoped `bb7c08f`.

### Provenance (repeated, as the brief requires) and disclosures

- **Reviewer:** a Fable-tier subagent (model `claude-fable-5`) spawned by an
  atelier orchestrator session that the principal opened 2026-08-17 at 1321
  UTC on the Fable tier under his standing cold-session instruction. The
  orchestrator wrote none of the delta and none of this brief; it holds the
  context partition and the sibling, forms no finding and writes no severity.
  I was neither started nor instructed by the authoring session
  (wt `channel-doctrine-0817`) nor by the brief-writing session (wt
  `cold-run-0817-0955`), and have edited no file this delta touches. Every
  finding, severity and word below is mine.
- ⚠️ **Disclosures.**
  1. I read the landing commit's message in full (`git show b0f202d`) and the
     head of `bb7c08f`'s, to identify the delta paths and confirm no later
     commit re-touched them. Both carry the author's account. I read
     `CONCURRENCY.md` whole and formed my own reading of the section before
     weighing either message or the brief's *What the work is*.
  2. Sweeps ran only through `tools/coldsweep.py` via a wrapper that always
     passes `--also-exclude` for the `280-…` board section and for
     `docs/reviews/`. No `--include-barred` run. Two title-level exposures
     happened anyway: (a) the generated index `docs/ROADMAP.md` (not barred)
     carries the `280-…` items' *titles* and three sweep hits landed on lines
     314–317 — I saw the titles of `010`, `030` and `040` (the last reads
     "The channel can contaminate review independence…"). That title overlaps
     CH1's subject; CH1 was formed from `REVIEW.md` rules 2 and 4, the
     section's message classes and this brief's own disclosure 3, but I cannot
     rule out that the title primed the direction — stated so the principal
     can weigh CH1's independence. (b) The floor's `plainscan` summary line
     printed two `docs/reviews/` *filenames* (barred directory) as "heaviest";
     filenames only, nothing opened.
  3. Opened by exact path, as permitted: the queue pointer `280/030`. Also
     read (not barred, named by the brief): board item `030/140`,
     `REVIEW.md` rules 2–4, `PROPAGATION.md` §§ around the floor block,
     `00-APEX.md` lines 50–62, `RECORD.md` close lines, `skills/create-repo/`
     stamping steps, `CHANGELOG.md` headings, `tools/test_templates.py`.
  4. Not opened: the `.deferred.md` sibling, the kept transcript, the intent
     record, `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`,
     every other brief or verdict under `docs/reviews/`.
  5. Not run: `/security-review` or any pending-diff scanner — the worktree's
     pending diff at spawn was other passes' work; the reach case is
     discharged under lens 4 on grounds instead.
  6. Ran `gh repo view mike548141/faves --json visibility` (read-only): PUBLIC.
  7. All mutation probes ran in scratch clones/repos under the session
     scratchpad; the worktree took no write from me except this appended text.

### Lens 1 — approach & assumptions (named first, in my own words)

The section rests on five load-bearing assumptions:

- **A1 — a channel exists and a session can enumerate its live peers.** The
  text never says what the channel *is* (a harness message primitive, a file,
  a commit) or where a session learns whether it has one. The floor and § The
  trigger are conditional ("where sessions can message each other"); § Claiming
  work is not (CH10).
- **A2 — an empty enumeration / no reply is a fact.** § The trigger calls the
  ask cue "the only cue that turns the flipped prior into a *fact*", and Hello
  says a session "can enumerate its live peers and ask, rather than inferring
  solitude from a clean tree". Only a *positive* answer is a fact; a null one is
  the same silence the doc says licenses nothing (CH2).
- **A3 — the tie-break is computable identically by both parties.** As written
  it fixes neither the evaluation point nor the tie (CH3).
- **A4 — the message classes are safe to send to every live peer.** They are
  not, for one peer class: a session holding or about to take a rule-4 cold
  review of the sender's delta (CH1).
- **A5 — the class "both correct, neither has written yet" is where cost
  concentrates.** Two claims are braided: a *structural* one (git cannot see
  intent that has not been written — true by construction) and an *empirical*
  one (that class is where the cost concentrates once several sessions run).
  The section keeps them mostly apart — "the only thing *observed* to catch
  it", the dated Bearing — but the sentence "That class is where the cost
  concentrates once several sessions run on one repo" states the empirical
  claim generally on one child's four days. Note N3, not a finding: the doc's
  own bar (repeatable evidence, never testimony) is met by committed child
  records the Bearing cites, which phase 1 cannot open (G10).

**Altitude.** Three laws in the method plus three floor sentences is
proportionate *if* the laws are independent and reachable. Law 2 is already
stated at its seam (§ Integration hygiene, "allocate, push, then check") and
law 1 is restated by the fence's first bullet — so the section carries the same
truth two or three times (N1). The alternative the brief names — one floor
sentence plus a pointer to a child's practice — would fail the doc's own
locality rule less than the current shape fails it: the *Bearing* names a live
public child, but as evidence, not as a binding on it, and every other Bearing
in the doc names `ros`, `tiki` or atelier the same way (N4). Not a finding.

**Does the delta pre-empt the pending `030/140` ruling?** Partly. The commit
says the CF3 yield branch was left untouched, and it was. But the new sentence
"File-disjointness is the unit of parallel safety, not item-disjointness" takes
a position on the axis `030/140`'s options turn on (line vs file as the unit),
and the new hunk-header check in § The trigger is exactly the "compulsory
pre-commit index inspection" `030/140` says must accompany any line-level
branch. The delta has therefore laid the guard half of one option without the
ruling (CH6, minor — the principal should read the two together when ruling).

### Lens 2 — correctness & quality

- **Cross-references.** All resolve and say what is claimed: `§ The channel,
  law 2` (from § Integration hygiene) → "closing check runs after the push";
  `§ The channel, law 1` (from § Surviving) → "message is awareness"; `§ Stay in
  your lane — work lands in the repo it changes` (line 540); `queue-never-
  deliver (§ Stay in your lane)` (line 552); `§ Claiming work — Orphan claims`.
- **The hunk-header incantation, live** (scratch clone, two files staged, then
  a peer hunk in the same file — see re-run ledger). `git diff --cached -U0 |
  grep '^@@'` prints one `@@ -a,b +c,d @@ <context>` line per hunk with **no
  filename**. A reader can compare hunk *count* and line ranges against what
  they wrote; a foreign hunk in a file they also touched stands out by range; a
  foreign hunk in *another* file appears as an unattributed header (CH8).
- **"`git push` can report success while pushing nothing" mid-rebase, live**
  (scratch remote + two clones). Plain `git push` in a stopped rebase fails
  loudly (exit 128, "not currently on a branch"). `git push origin main` with
  `main` already at the remote tip prints "Everything up-to-date", exit 0,
  while a commit made in that checkout during the rebase sits on the detached
  rebase HEAD and is not on `origin/main`; `git status --short` prints nothing.
  Claim reproduced for the explicit-refspec form; the doc could name the form
  (CH8, same finding). `rebase --abort` then dropped the peer's commit from the
  log (reflog only) — the doc's "verify each peer commit is already reachable"
  is the right pre-condition.
- **Byte-identity.** `stampscan`: 1 stamped block verified, `[identical]`
  matches canonical region `floor` (61 lines), exit 0.
  `test_templates.test_stamped_block_matches_canonical` OK (44 tests).
- **Tie-break.** Undefined at 0–0 (the common case for a just-minted
  identifier), unfixed evaluation point (unpushed trees; a reference landing
  between two computations), and the "burned identifier" sub-rule does not say
  whether both parties move on a tie (CH3).
- **The fence vs the classes.** "Findings cross as claims-with-repro; changes
  do not cross at all", yet the third shape rule contemplates "an offer of
  drafted text" — a change crossing as text, once. And a relayed *ruling* is a
  peer's claim under the section's own re-run rule, but the class does not say
  a relayed ruling is checked against the record before it is acted on (CH13).
- **Seam consistency in § The trigger.** "there are two — both cheap … The two
  cues:" is followed by three bullets, and "the other two are discoveries you
  make by accident" misdescribes the say-so cue (CH7). The reverse-edit rule
  ("never `checkout`, `restore` or `stash`") sits three paragraphs from the
  mandated `git pull --rebase --autostash` bookend, and `--autostash` *is* a
  stash of whatever a peer holds in the shared checkout (CH4).

### Lens 3 — completeness / harvest

- `CONCURRENCY.md` every section: no sentence contradicts § The channel; the
  three defects are at seams (CH4, CH7) and in § Surviving's sweep table, which
  has no "repository state" row for the very blind spot the delta named
  (CH11).
- `PROPAGATION.md` floor + template: identical (above). `create-repo` stamps
  the canonical region verbatim (SKILL steps 5, "don't paraphrase it"), so new
  children inherit the sentences without a further edit — the retrofit of
  existing children is `280/020`, out of scope. Followability by a child that
  has never read § The channel: the three sentences are followable with git
  knowledge, but the pointer `(CONCURRENCY.md § The channel)` sends the reader
  to a section that holds neither the hunk-header incantation nor the
  mid-rebase guidance (both in § The trigger) nor the file-set rule's home
  (§ Claiming work) (CH9).
- `RECORD.md`: the farewell class ("what landed, what is released, what is
  left") overlaps the close all-clear; not a contradiction — but under law 1 a
  farewell should *point at* the closing record, and the class does not say so
  (N1).
- `CHANGELOG.md`: no entry for the section or the floor change; every prior
  `CONCURRENCY.md` addition (claiming 2026-07-13, put-away 2026-07-11, the
  trigger flip) has one (CH12).
- **How to send a peer message on this platform:** no surface says. Swept
  (`sendmessage|send_message|peer session|broadcast`, barred paths excluded):
  the only hits are the delta itself. The channel is assumed (CH10).
- Board: `280/020` adoption and `280/030` pointer exist (index titles only);
  `030/140` stands and is discussed under CH6.

### Lens 4 — security & privacy (mandatory)

- **The doctrine text carries** one repo name (`faves`, a public child — verified
  PUBLIC via `gh repo view`), dates, session counts and a description of what
  its sessions did; no machine path, no person other than the principal (named
  throughout the doc already), nothing `PROPAGATION.md` bars from a public
  tree. Naming a *public* child's coordination failures in a Bearing is the
  doc's existing practice (`ros`, `tiki`, atelier sessions 45–46) and inside
  the repo's privacy rule, which bars private repos' names and detail. N4.
- **Is the publication clause enough?** No, not on its own: it lives in the
  on-demand section, while the floor — what children load — instructs the
  file-set announcement and answer, and the section instructs relaying
  rulings and findings across repos, with no abridgement rule at the floor. A
  *public* child session that records a *private* peer's hello (repo name +
  file set) or a relayed finding in its session log reproduces the exact
  repo-name-plus-inventory shape the clause says forced the rule (CH5).
- **Reach case for the house security scanner:** it reads the session's
  pending diff; this is a landed-delta review in a tree whose pending diff is
  other passes' work, so it was not run (disclosure 5). The delta itself was
  scanned by the enforced floor at landing and again here at HEAD: `leakscan`
  and `secretscan` enforced on both planes, exit 0 (secretscan 22 advisory on
  the CI plane, expected).

### Grounding claims recorded for reconcile (phase 1 cannot open the source)

- **G1** a third session noticing two answers to one broadcast found a file two
  sessions each believed they held alone.
- **G2** every version-number reservation in the grounding window was stale by
  merge time.
- **G3** two sessions each yielding off a collided identifier both took "the
  next free one" and collided again five minutes later.
- **G4** two of one day's four repo-wide stops came from correct
  gate-tightening changes.
- **G5** three rulings arrived by relay in a single session.
- **G6** a correct measurement arrived wrapped in a wrong diagnosis that would
  have reverted a shipped decision, more than once.
- **G7** both load-bearing corrections in the transcript came from re-running
  (a compensating-guard probe; a re-read doctrine passage and a withdrawn
  assertion).
- **G8** four rounds, two of which existed only to correct the earlier two.
- **G9** the repo-name-plus-guard-inventory pairing is described, not quoted,
  in the transcript, with the abridgement stated in the file.
- **G10** the Bearing: `faves` 2026-08-13 to 2026-08-17, up to five sessions;
  the child's records name the double-held file, the absorbed version
  constant, the identifier collisions, and two blocking occasions.
- **G11** the three laws are the child's own corrections, not this document's
  advice to it.
- **G12** each of the seven classes was earned by a failure the artefact layer
  could not have caught.
- **G13** "three sessions stalling on one clause" — consistent with `030/140`'s
  own text (three sessions deadlocked the morning after inlining), the one
  claim phase 1 could partly check.

### Findings

**MODERATE**

- **CH1 — The channel is not fenced against the review-independence bar.**
  The seven classes send hello, holdings, findings and rulings to *every* live
  peer, unconditionally. `REVIEW.md` rule 2 calls an earlier verdict "another
  channel for the author's framing"; rule 4's criterion is a session the author
  "neither started nor instructed". A message from a delta's author to a
  session holding or about to take that delta's `⏳` is exactly the framing
  path rule 2 exists to close, and this brief's own disclosure 3 (author
  contacted brief-writer) is an instance. The section says nothing about it.
  *Repro:* read § What the channel carries against `REVIEW.md` rules 2 and 4;
  find no carve-out. *Independence note:* see disclosure 2(a).
- **CH2 — The ask cue overclaims: a null answer is still silence.** § The
  trigger: "the only cue that turns the flipped prior into a *fact* rather than
  a posture"; Hello: "enumerate its live peers and ask, rather than inferring
  solitude from a clean tree". Only a positive answer is a fact; an empty
  enumeration or no reply is the silence the same section says "licenses
  nothing", and enumeration sees only channel-visible peers. As written, a
  reader may reach "solo" from an empty peer list. *Repro:* lines 73–76 and
  423–427 against lines 53–56.
- **CH3 — Law 3's tie-break is not "computable identically" as written.** No
  evaluation point (which tree, at which commit — a reference in a peer's
  unpushed tree or one landing between the two computations gives the parties
  different counts), and no rule for the tie — 0–0 being the *usual* state of a
  just-minted identifier. The "burned identifier" sub-rule does not say whether
  both move on a tie. The doc's other tie-break (§ Claiming work: first push
  wins) is precedence; the section says "cheapest repair rather than
  precedence" without saying when each applies. *Repro:* lines 406–416 vs
  289–293.
- **CH4 — "never `stash`" vs the mandated `--autostash` bookend.** § The
  trigger (new): back out of a peer-held file by reverse edit, "never
  `checkout`, `restore` or `stash`, each of which reaches their work as well as
  yours". § Integration hygiene and the floor mandate `git pull --rebase
  --autostash` at session start — in a shared dirty checkout that stashes the
  peer's edits (re-applied on success; left in a stash if the pop conflicts,
  leaving the peer's tree clean-looking). The new mid-rebase bullet's "back any
  autostash out to a file before aborting" half-names the hazard without
  reconciling the two rules or saying what the bookend does at a dirty shared
  checkout (CF3's first branch says "stage and commit the claim alone" — but
  the sync before it is the autostash). *Repro:* lines 96–98 vs 160–161 and
  floor line 127.
- **CH5 — The publication clause does not reach the floor (privacy).** The
  floor instructs announcing and answering file sets and § The channel
  instructs relaying rulings and findings across repos; the abridge-into-the-
  record rule exists only in the on-demand section. A public child recording a
  private peer's hello or finding reproduces the repo-name-plus-inventory
  shape the clause names. One floor clause ("what a peer says is not what
  this repo's record may hold — abridge and say so") or a floor pointer to the
  clause closes it. *Repro:* floor lines 133–139 vs section lines 485–493.

**minor**

- **CH6 — The delta takes a position on `030/140`'s axis while saying it left
  the finding alone.** "File-disjointness is the unit of parallel safety, not
  item-disjointness" (line 237) plus the now-mandatory hunk-header check are
  the two halves `030/140` says any line-level yield rule needs; the ruling
  reader should meet them together. Not a defect in the sentence; a
  cross-reference the pointer and the item should carry.
- **CH7 — Seam count and characterisation in § The trigger.** "there are two …
  The two cues:" precedes three bullets (lines 53–60 → 62–76); "the other two
  are discoveries you make by accident" (line 76) misdescribes the say-so cue,
  which is the principal's statement.
- **CH8 — The two live-proven incantations are each half-stated.** (a) The
  hunk-header check prints no filenames; `git diff --cached --stat` first, or
  `grep -E '^(\+\+\+|@@)'`, is what lets a reader attribute a foreign hunk.
  (b) It is `git push origin <branch>` (explicit refspec) that reports
  "Everything up-to-date" mid-rebase; plain `git push` fails loudly. Both
  reproduced (re-run ledger).
- **CH9 — The floor pointer mis-targets.** `(CONCURRENCY.md § The channel)`
  ends three sentences whose full rules live in § The trigger (index, mid-
  rebase, hunk headers) and § Claiming work (file set); § The channel holds the
  laws. A child following the pointer finds no incantation.
- **CH10 — Conditionality and the missing primitive.** Floor and § The trigger
  say "where sessions can message each other"; § Claiming work pairs the claim
  with a channel announcement unconditionally (line 240–242). No surface says
  what the channel is or how peers are enumerated. A channel-less adopter gets
  no file-disjointness surface at all, though the claim line — the artefact,
  per law 1 — could carry the file set.
- **CH11 — § Surviving's sweep table lacks the blind spot the delta named.**
  No "repository state — no rebase/merge/cherry-pick in progress" row; and
  "back any autostash out to a file" names no command.
- **CH12 — No `CHANGELOG.md` entry** for a ~155-line doctrine section and a
  floor change every child stamps; prior `CONCURRENCY.md` additions each have
  one.
- **CH13 — Fence vs shape rule; relayed rulings.** "changes do not cross at
  all" vs "an offer of drafted text … once"; and a relayed ruling is a peer's
  claim under the section's own re-run rule, but the class does not say it is
  checked against the record before being acted on.

**notes** (no action implied)

- **N1** Law 1 and the fence's first bullet restate each other; the farewell
  class overlaps `RECORD.md`'s close all-clear and, under law 1, should point at
  the record.
- **N2** KISS/altitude: at ~153 lines the section is within the doc's own scale
  (§ Claiming work ~150, § Orchestrated queue runs ~140). `plainscan` over
  `CONCURRENCY.md` at HEAD: 94 findings (P1 ×10, P2 ×1, P3 ×66, P4 ×17); the
  section (lines 369–521) accounts for 8, the seam edits for 4 — the file was
  the heaviest method doc before this delta. Measurement, not a finding.
- **N3** Structural vs empirical: kept apart except at line 376–378; see lens 1.
- **N4** Naming a public child in the Bearing is within the repo's privacy rule
  and the doc's existing practice.

**Overall: PASS-WITH-FINDINGS — 0 MAJOR · 5 MODERATE (CH1–CH5) · 8 minor
(CH6–CH13) · 4 notes.** Nothing here blocks the doctrine standing; CH1 and CH5
are the two the principal should weigh first, because both are about what
crosses the channel *into* places the method already fences (a cold review; a
public record).

### Re-run ledger (all at HEAD `574f133`, worktree, exit codes read directly)

| Run | Result | Counts |
| --- | --- | --- |
| `floor.py --plane hook` | exit 0 | 11 enforced ✅ · 4 warn-only 👁️; sizescan 2 size-advisory (index, sessions log — not the delta) |
| `floor.py --plane ci` | exit 0 | secretscan 🟡 22 advisory; leakscan cover note (no `--require-terms` on CI plane); rest as hook |
| `unittest discover -s tools` | exit 0 | Ran 1344 tests, OK (commit claimed 1324 at landing; +20 = `coldsweep`'s tests, landed since per `CHANGELOG.md`) |
| `node --test instruments/*.test.js` | exit 0 | 235 pass, 0 fail |
| `stampscan.py --warn` | exit 0 | 1 stamped block, `[identical]` to canonical region `floor` (61 lines) |
| `unittest tools.test_templates -v` | exit 0 | 44 OK, incl. `test_stamped_block_matches_canonical` |
| `plainscan.py --warn` on `CONCURRENCY.md` | exit 0 | 94 (P1 10 · P2 1 · P3 66 · P4 17); section 8, seams 4 |
| Hunk-header probe (scratch clone, 2 files / 3 then 4 hunks) | — | headers print with ranges + context, **no filename**; see CH8 |
| Mid-rebase push probe (scratch remote + 2 clones) | — | plain push exit 128; `push origin main` "Everything up-to-date" exit 0 with an unpushed peer commit on the rebase HEAD; `status --short` empty |
| `gh repo view mike548141/faves` | — | PUBLIC |

No suite result looked like interference; none re-run.

### Follow-up checklist (for the principal's ruling round; nothing applied)

- [ ] CH1 — decide whether § The channel carries a review-independence fence
  (a session on a rule-4 item is off the author's channel for that delta, or
  discloses every message), and whether `REVIEW.md` rule 4 names the channel.
- [ ] CH2 — reword the ask cue and Hello so only a positive answer is a fact.
- [ ] CH3 — fix law 3's evaluation point and tie rule (or drop "computable
  identically").
- [ ] CH4 — reconcile "never `stash`" with `--autostash` at a dirty shared
  checkout; say what the bookend does there.
- [ ] CH5 — put the abridgement rule (or a pointer) in the floor sentence.
- [ ] CH6 — cross-reference the file-disjointness sentence and the hunk-header
  check from `030/140` before ruling on it.
- [ ] CH7–CH13 — wording, pointer target, sweep-table row, CHANGELOG entry.
- [ ] Reconcile — check G1–G13 against the transcript and the child's records;
  say which findings moved.
