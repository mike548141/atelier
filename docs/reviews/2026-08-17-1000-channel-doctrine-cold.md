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

### Reconcile (2026-08-17, after release)

**Written:** 2026-08-17 13:45 UTC, at HEAD `b7e0da5` (phase-1 committed
unrevised; the three delta paths still byte-identical to `574f133`). Nothing
above this heading was edited.

**Provenance of this step.** The orchestrator released the sibling's text by
message after the phase-1 commit; the orchestrator formed no finding. I then
opened, in this order and nothing else: (1) the intent record
`docs/sessions/2026-08-17-0734-channel-doctrine.md` including its post-landing
addendum; (2) the transcript
`docs/sessions/2026-08-17-0343-cross-session-channel-transcript.md`; (3) the
public child's committed records — `docs/SESSIONS.md` (grep-located excerpts in
the 2026-08-15…17 window) and `docs/decisions/README.md` lines 25–52 — read-only,
in the sibling checkout under the home directory; (4) board `280-…` README, `010`
and `020` (`040` stays unopened — I know only its index title, disclosure 2(a));
(5) the single `docs/SESSIONS.md` index line for the `0734` record (line 268, by
slug grep); (6) the five prior verdicts the sibling names, and `030/140` re-read.
Still no git state change, no other file edited.

#### Grounding claims G1–G13 against the sources

| # | Claim | Result | Where |
| --- | --- | --- | --- |
| G1 | third session, two answers, double-held file | ✅ verified | child record "What parallel work actually cost" (two files double-held; a third session noticed) |
| G2 | every version reservation stale by merge time | ✅ verified | child record "Every reserved version number was stale by merge time" (three reservations, all resolved higher); repeated later for a `.99`→`.106` |
| G3 | polite double yield, collided again in five minutes | ✅ verified | child ADR index: two records stamped the same number, both renumbered to the next, red again five minutes later; the number left a permanent hole; **the tie-break and "fewer inbound references" are the child's own words** — stated there for the state *both records pushed and `main` red* |
| G4 | two of one day's four repo-wide stops from gate-tightening | ⚠️ verified with a mislabel | the child's table lists **four collisions between correct decisions**, of which **two** stopped every session's commits; the other two stopped "both, silently" / would have been absorbed. "Four repo-wide stops" over-counts the stops (CH14) |
| G5 | three rulings arrived by relay in one session | ✅ verified | child record: "brought back three owner rulings this session would otherwise never have seen … Rulings do not cross between sessions by themselves" |
| G6 | measurement wrapped in wrong diagnosis, "more than once" | ⚠️ one named instance | in the child's records (recorded from both sides); a second is arguable in transcript § 2 (right measurement, wrong compensating-guard diagnosis) — defensible across the evidence base, not from the child's records alone (CH14) |
| G7 | both load-bearing corrections came from re-running | ✅ verified, one nuance | transcript §§ 2–3. The second re-read was done by a **peer** of the withdrawing session ("a peer went and re-read your source"), not by the counterparty — the doctrine's "the other re-read … and withdrew" compresses that (CH14) |
| G8 | four rounds, two only to correct the earlier two | ⚠️ count survives, target loose | four numbered exchanges; §§ 2 and 3 are the corrections; **both correct claims made in § 1** (and one atelier item), so "the earlier two" should read "the first"; § 2 also carried the finding's acceptance, so "only" is slightly strong |
| G9 | abridged repo-name + guard-inventory pairing, stated in file | ✅ verified | transcript "Scope and what is deliberately omitted" and § 4 |
| G10 | Bearing: five sessions, double-held file, absorbed constant, identifier collisions, two blocking occasions | ✅ verified | child records: "Five faves sessions ran concurrently"; the `.88` absorbed bump; the ADR and version collisions; table rows 3–4. Window start 2026-08-13 not confirmed from headings (earliest concurrency notes seen are 08-15/16); immaterial |
| G11 | the three laws are the child's own corrections | ✅ verified | "a broadcast is not a reservation either … only a pushed commit reserves"; ADR index: check **after** the push; fewer inbound references moves; the burned number stays burned |
| G12 | each of seven classes earned by a failure | ⚠️ six of seven | hello/file-set, holdings, minting, gate-tightening, rulings, findings each have a named failure in the child's records. **Farewell** has none I could find; it comes from the principal's commission ("Saying Hi when a new session starts or resumes or closes") — CH15 |
| G13 | "three sessions stalling on one clause" | ✅ verified | transcript § 3, the child's own self-report; consistent with `030/140` |

**Which findings moved on that reading.**

- **CH4 (MODERATE → MODERATE, evidence upgraded).** Phase 1 reasoned the
  `--autostash` hazard from the commands; the child's own record for the day the
  floor came home says it: *"a peer's `pull --rebase --autostash` in the shared
  primary checkout absorbed our uncommitted work and collided on `sw.js`"*. The
  finding is now observed, not inferred. Severity unchanged — it was already
  weighed as a real seam contradiction.
- **CH3 (MODERATE → MODERATE, grounds sharpened).** The child's source rule is
  stated for the state *both records pushed, `main` red* — the evaluation point
  is implicit there and was dropped in extraction; the tie case is undefined in
  both. Same severity, sharper counsel: restore the precondition and add the tie.
- **CH1 (MODERATE, unchanged; anticipated).** The intent record's addendum
  reaches the same gap after landing and queues it at `280/040`, deliberately not
  fixing it because the fix sits in `REVIEW.md` rule 4 while this delta is queued
  under it. My phase-1 CH1 was formed before that reading (disclosure 2(a)
  stands: the `040` index title may have primed the direction). Anticipated by
  the author, unaddressed in the text; severity stands.
- **CH2 (MODERATE, unchanged; strengthened by a prior verdict).** The flip
  pass's CF2 [fixed] wrote "their silence licenses nothing" into § The trigger
  precisely so cue-silence could never license relaxing; the new "ask" cue's
  wording sits beside that fixed line and re-opens the door for a null
  enumeration. Not anticipated as such; the principle it violates was ruled
  2026-07-20.
- **CH8 (minor, unchanged; grounded).** The child's record names the exact
  shape — "`git rev-parse HEAD` equal to `origin/main` … reads exactly like
  success; `git status | head -1` saying 'interactive rebase in progress' is the
  signal" — and, separately, "`git push` printed success while pushing nothing".
  Supports CH11's sweep-table row as well.
- **CH6 (minor, unchanged).** The intent record and `010` restate "nothing here
  is written over `030/140`"; neither notices that the file-disjointness sentence
  and the mandatory hunk-header check sit on the same axis. Not anticipated.
- **CH5, CH7, CH9, CH10, CH11, CH12, CH13** — unchanged; none anticipated by
  the intent record or the prior verdicts. CH12: the intent record and `010`
  list every surface that landed and neither names a `CHANGELOG.md` entry, so
  the omission is confirmed, not explained.
- **N1–N4** — unchanged. N4 confirmed: `010` and the intent record treat the
  child's records as public evidence, and `gh` reports the child PUBLIC.

**New findings from the reconcile reading** (numbered on from phase 1; recorded
here, phase-1 counts left as written):

- **CH14 (minor) — three grounding restatements are looser than their
  sources.** (a) "Two of one day's four repo-wide stops" — the source has four
  *collisions*, two of them repo-wide stops. (b) "the other re-read a doctrine
  passage and withdrew" — a *peer* re-read; the counterparty withdrew. (c) "more
  than once arrived wrapped in a wrong diagnosis" — one named instance in the
  child's records; the second rests on reading the transcript's § 2 as the same
  shape. Each is small; together they sit inside the one class the section's
  own findings rule polices (measurement labelled apart from diagnosis), and
  `030/140` records the same house habit — a quotation acquires the quoter's
  emphasis unless diffed against the source.
- **CH15 (minor) — "each earned by a failure" is true of six classes.** The
  farewell class is grounded in the principal's commission, not in a failure the
  child's records name; the sentence should say so, or the class should carry
  its own bearing (the orphan-claim judgement it spares is a cost, not a failure
  observed).
- **CH16 (minor, completeness) — the child's post-commit check was not
  extracted.** The same window's records carry the mirror of the pre-commit
  hunk-header check: *"After a commit, verify it exists and says what you wrote —
  `git log -1` naming your subject, not merely a clean status. A clean status is
  equally consistent with 'committed' and 'someone else committed it for
  you'"*, learned when a session's staged files landed inside two peer commits.
  § The trigger's index blind spot names only the pre-commit half.

#### The brief-writer's eight seeded questions — answered after the fact

1. *What is the channel?* Not stated anywhere; the doctrine is conditional in
   the floor and § The trigger, unconditional in § Claiming work — CH10. The
   child's records show it as a harness message primitive between live sessions
   plus a broadcast on open; the method abstracts it away and points nowhere.
2. *Tie-break on different trees; what breaks a tie?* Not stated; the child's
   source presupposes both artefacts pushed and `main` red; nothing breaks a tie
   in either — CH3.
3. *Claim content described two ways?* Not a contradiction: the claim line still
   carries *what*; the file set rides on the channel, not in the claim. Which is
   the rule is clear; whether the file set *should* also live in the artefact is
   CH10's note.
4. *Does the reverse-edit rule decide `030/140`?* No — it governs backing out
   your own edits, and CF3's yield says touch nothing. What does touch the axis
   is the file-disjointness sentence plus the hunk-header check (CH6); the intent
   record's "nothing written over it" was meant and is true of the yield branch.
5. *Is "a symptom count locates a fault's existence, never its site" measurement
   or generalisation?* The child's own words, verbatim in transcript § 3 —
   source, not the author's generalisation.
6. *Count the rounds.* Four exchanges; two are corrections; both correct
   claims made in the *first* (G8). Characterisation survives; "the earlier two"
   is loose. Left out that a reader would want: the peer-not-counterparty nuance
   (CH14b), the child's post-commit check (CH16), and the tie-break's pushed-and-
   red precondition (CH3).
7. *Is "read the staged hunk headers before every commit" proportionate for a
   solo session, and does the floor say when it applies?* The sentence's subject
   ("the shared checkout's index …") scopes it; its adverb ("before every
   commit") does not, and the pointer sends the reader to the wrong section
   (CH9). A solo worktree session can read it as not applying, but the floor
   does not say so.
8. *Did the addendum's correction reach the doctrine text or only the record?*
   The record: `bb7c08f` rescoped the queue pointer and dated the first child's
   pin position; the doctrine text was not touched, and the gap the same use
   exposed (CH1's) was queued at `280/040` rather than fixed — a home, so not
   the rule-with-no-home class.

#### Prior verdicts' [fixed] claims verified at HEAD

- Flip pass (2026-07-20) CF1–CF7: all present in `CONCURRENCY.md` at HEAD —
  the evidenced-alone/unevidenced trade (CF1), "silence licenses nothing" (CF2),
  the dirty-primary rule (CF3), the floor bullet's flipped prior (CF4),
  "affirmative statement or record, never an absence" (CF5), no "(primary)"
  residue (CF6), "when unsure which rung, take the worktree" (CF7).
- Claiming-work pass (2026-07-13) 1–7 and the applied pass 1–2: all present —
  claim keys on selection, lands on `main` from the primary checkout, per-leaf
  fan-out, the `[~]`→`[ ]` revert step, the tracker precondition, adjacent-item
  conflict with "no unchanged line between them", timestamp demoted to tiebreak.
- Cancelled-run pass CR1–CR3: on `RECORD.md`, not this delta's surfaces — not
  verified here.
- Put-away pass: no findings on the KISS line; the claiming pass judged the
  claim mechanism inside the no-locking line, which is the same reading N2 gives
  the channel.

**Overall after reconcile: PASS-WITH-FINDINGS stands — 0 MAJOR · 5 MODERATE
(CH1–CH5, none moved in severity; CH3 and CH4 sharpened/grounded) · 11 minor
(CH6–CH13 + CH14–CH16 new) · 4 notes.** Findings remain the principal's to
decide (REVIEW.md rule 3); nothing applied.

## Deferred material — folded in at reconcile

# Deferred material — the channel as a concurrency primitive (open only after your findings are durably written)

Sibling of `2026-08-17-1000-channel-doctrine-cold.md` under REVIEW.md rule 1's
split. Fold into the brief below the verdict and delete this file when the
verdict lands.

## Intent record and primary source

- `docs/sessions/2026-08-17-0734-channel-doctrine.md` — the authoring
  session's account, including an addendum (`516a4c0`) in which the channel
  corrected the doctrine's own artefact after landing. **Not opened by the
  brief-writer.**
- `docs/sessions/2026-08-17-0343-cross-session-channel-transcript.md` — the
  four-round exchange the section cites as primary source, kept verbatim with
  a stated abridgement. **Not opened by the brief-writer.** This is where the
  grounding claims are checked: the two corrections that "came from a party
  re-running a claim", the two rounds that "existed only to correct", the
  offer-made-once, and the abridged repo-name pairing.
- The public child `faves` (`~/.pets/faves`, its `docs/sessions/`) — the
  committed records the *Bearing* cites for the double-held file, the absorbed
  version constant, the identifier collisions and the two gate-tightening
  stops. Readable, and quotable only to the extent the child's own records are
  public. **Not opened by the brief-writer.**
- The board section `docs/roadmap/280-cross-session-channel-mike-commissioned/`
  — `010` (the commission, with the principal's prose) and `020` (per-child
  adoption). **Not opened by the brief-writer** beyond the `030` pointer.
- The `docs/SESSIONS.md` index entry for this delta. ⚠️ **Read by the
  brief-writer**, at onramp — see the disclosure in the brief.

## Prior verdicts on the same surfaces

- `docs/reviews/2026-07-20-1355-concurrency-flip-cold.md` — the pass that
  flipped § *The trigger*'s prior; the *ask, when a channel exists* cue edits
  the text that pass reviewed.
- `docs/reviews/2026-07-13-concurrency-claiming-work.md` and
  `2026-07-13-2256-claiming-work-applied.md` — the passes on § *Claiming
  work*, which the file-set announcement now extends.
- `docs/reviews/2026-07-11-concurrency-put-away.md` — the earliest concurrency
  pass, for the doc's original KISS line.
- `docs/reviews/2026-08-09-0822-record-cancelled-run-clause-cold.md` — the
  nearest prior treatment of "a parallel session's push changes what your run
  reports", which the mid-rebase blind spot touches.
- The open finding against the CF3 yield branch, board item
  `docs/roadmap/030-enforcement-propagation-the-estate-rollo/140-cf3-s-claiming-rule-collapses-on-a-monolithic.md`
  — left standing by the delta on purpose; check whether the new
  *reverse-edit, never checkout/restore/stash* text in § *The trigger* answers
  it, contradicts it, or leaves it exactly as open.

## Brief-writer's seeded questions (a floor, never a fence)

Generate your own before reading these. Treat a question you did not think of
as a prompt to re-read the surface, not as an agenda — and note that the
brief-writer read the commit message and the session index entry, so these
questions inherit some of the author's framing.

1. What *is* the channel, concretely, on this platform? The section says
   "where sessions can message each other" and never names a mechanism. A
   session reading the floor sentence in a child has to decide whether it
   *can*. Does anything tell it how to find out — and is the doctrine
   therefore conditional in a way the floor sentence's imperative mood hides?
2. Law 3's tie-break — *whichever artefact carries fewer inbound references
   moves* — is claimed computable identically by both parties. Both parties
   see different trees (each has unpushed work). Is the count taken on the
   integration branch only, and does the text say so? What breaks a tie?
3. The *hello* class says give the file set. § *Claiming work* says a claim
   says *what*, never *which files*, and now says the claim is *paired* with
   a file-set announcement. Two sentences on one page now describe the claim's
   content differently. Which is the rule?
4. § *The trigger*'s new paragraph says never `checkout`, `restore` or `stash`
   to back out of a file a peer also holds. The doc's CF3 yield branch (a few
   lines below) and the finding against it in `030/140` concern the same
   move. Does the new text decide what the delta said it deliberately left
   for the principal — and if so, was that intended?
5. The *findings* class says label measurement apart from diagnosis. The
   section's own *re-run* subsection contains a diagnosis ("a symptom count
   locates a fault's existence, never its site") stated as a rule. Is it a
   measurement from the transcript, or the author's generalisation? Check at
   reconcile.
6. The *cost clause* — two of four rounds were corrections. Read the
   transcript and count. Say whether the doctrine's characterisation of the
   exchange survives your reading, and whether anything the transcript shows
   was left out of the doctrine that a reader would want.
7. The floor sentence adds *read the staged hunk headers before every commit*
   to every child's onramp. Is that a proportionate ask for a solo session in
   a repo with no peers, and does the floor bullet say when it applies?
8. The addendum commit `516a4c0` says the channel "corrected its own
   doctrine's artefact" after landing. That is a live instance of the section
   in use, one hour old. Read it at reconcile and say whether the correction
   reached the doctrine text or only the record — the *rule with no home*
   class the same day's ruling round minted.
