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
- ⚠️ **Two disclosures, both about the brief-writer.**
  1. **It read the `docs/SESSIONS.md` tail** at session onramp, before this
     brief was commissioned; the index entry for this delta is long and is
     the author's account of the section's structure and grounding. Rule-2
     barred material, read. It is why the intent record and transcript were
     left unopened, and why the seeded questions in the sibling are held to
     what the doctrine text itself says.
  2. **It read the landing commit's message in full.** Generate your own
     reading of the section before you weigh anything this brief says.
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
