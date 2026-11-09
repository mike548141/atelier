# Record — docs are code, and the session is part of the build

*The doctrine, the design decisions, and the trail of how the work got here are
**artefacts in the repo**, versioned and changed in lockstep with the code — not
lore in someone's head or a chat that scrolls away. A future session (or a peer,
or a more capable reviewer) reconstructs the "why" from the repo alone. If it
can't, the record failed.*

## Docs-as-code — the core discipline

Documentation lives in the repo, in the same commit as the change it describes.
The rule is **lockstep at the integration boundary**: a change to behaviour and
the change to the doc that governs it land **together** on the shared branch, or
the doc is a lie the moment it merges. A commit that alters the CLI surface and
leaves the man page stale is not "done with a doc follow-up owed" — it is a
broken commit. A WIP or spike **branch** may trail its docs while the line is in
flight — that's what branches are for — but what *lands* lands doc-complete
(this is CONCURRENCY's worktree-per-line: a line of work integrates as a unit).
This is EVIDENCE §9 (one fact, one home) plus the apex (no claim stronger than
its evidence — a stale doc *is* an over-strong claim about the code).

Consequences:

- **The doc that governs a thing changes in the thing's commit.** Man pages, the
  architecture note, the doctrine block — all move with the code.
- **Structure-as-documented must exist.** A README that lists a directory or a
  file that isn't there is a defect, not aspiration (an apex violation caught in
  the atelier foundation review itself).
- **Stub honestly.** What isn't built yet is *labelled a stub*, not written up in
  the present tense as though it exists. "Extraction in progress" beats a
  confident paragraph describing a thing that's empty.

## The *why* lives at the site

The smallest unit of the record is the comment and the commit message, and both
carry the same discipline: **say _why_, not _what_.** Code already says what it
does; a comment restating it is noise that rots. What a future reader cannot
recover from the artefact itself is the *reason* — the platform quirk, the
rejected alternative, the non-obvious constraint, the precedent a trade-off
ruling set. Commit messages are the same rule at the change level: a why-dense
body, so the history reads as reasoning, not a diff narration. (This scales up
the same way: an ADR is a why that outgrew a comment; a doctrine doc is a why
that generalised. Which register it belongs in is decided by who must find it —
the reader at the site gets the comment, the re-litigator gets the ADR.)

*(Added 2026-07-10, review B10 — `build/REPO-STANDARD.md` pointed here for this
rule before it was written down; the practice long predates the paragraph.)*

## The session log — an append-only index with detail on demand

Every working session leaves a trace, so the next one starts from where this one
stopped instead of re-deriving it:

- **`SESSIONS.md` is an append-only index** — one entry per session, newest last,
  read at session start (tail it). Append-only is a rule about **content** — an
  entry is never edited or reordered once written — **not a fixed home**: like
  the roadmap, an index that outgrows its budget **rotates**. The recent tail
  stays in `SESSIONS.md`; older entries relocate **verbatim** to a
  `SESSIONS-ARCHIVE.md` growth store (grepped on demand, never loaded whole) —
  the same current-truth/history split as `ROADMAP`→`ROADMAP-DONE`, and the
  answer to the one move a bloated *already-split* index otherwise lacks.
  `tools/sizescan.py` does not measure the index's length — it has no size check
  (Mike's ruling, 2026-10-05: no arbitrary line or size limits) — and nothing
  else reads the index for its shape, so a regression back to a flat log is
  detected by no tool and by no scheduled review: it relies on the writing
  session's discipline and the next session noticing. (Grounded 2026-07-14:
  the cold review found the append-only rule and the budget colliding with no
  sanctioned move for an index that had already done the split.) A cold
  reviewer does not read this tail: it skips the session-log step of the read
  order (`REVIEW.md` rule 2, *the reviewer's start-up reading*), so a closing
  entry carries no duty about deferred material.
- **Detail lives on demand** — when a session is substantial, its full detail
  goes in a `docs/sessions/<date>-<HHMM>-<slug>.md` file and the index carries
  a one-line pointer. (`HHMM` is the session's start time, 24-hour, in UTC —
  `date -u`, ADR 2026-07-15; the identifier is coordination-free per
  CONCURRENCY's record-identifier rule:
  built from facts the session already owns, safe to allocate at open, no
  shared counter. Files named under the retired `NN` scheme keep their names.)
  These identifiers are **long, lowercase and hyphenated by design** (a full
  slug runs 40+ chars); a downstream tool that quotes one — a registry
  validator, a secret/token scanner — must allow that shape rather than flag it
  as a suspicious high-length token, and reference the id in full rather than
  truncating the slug away. *(Bearing: a sibling repo's registry validator
  tripped its token-shape guard on a 46-char id quoted verbatim; the estate's
  own entropy-based scanners pass these ids clean — a hyphenated date-slug
  carries almost no entropy.)* Open the detail file only when a line needs
  unpacking. This keeps the always-loaded index cheap (token discipline)
  without losing depth.
  - **A pointer to an addendum entry names the entry, not the file it extends.**
    When a later session appends a `SESSIONS.md` entry continuing earlier work,
    whatever points at it — a roadmap item, a review brief, a queue line — says
    *the `SESSIONS.md` entry of `<date>`*. Linking the earlier session's detail
    file sends the reader to a file the addendum was never written into: they
    grep it, find nothing, and read the work with no intent record. (Grounded
    2026-07-28: a cold pass followed exactly that pointer, found the named file
    empty of the record, and reached its verdict before the addendum surfaced.)
  - **A detail record ends with an identifiers block, and so does the closing
    message.** These are the handles a later session, a peer or the principal
    uses to find this session's work without reading the narrative. Each is
    read fresh at close, never recalled: `ccclose` prints the block after its
    checks (`ccclose --identifiers` prints it alone), and a field it cannot
    derive says so, to be filled by hand:
    - **Session**: the session id (what `cctranscript` and `ccclose` take),
      the model it ran on, and its window in UTC.
    - **Commits**: every commit the session landed, its workers' included, as
      short SHAs in order, with the range when they run unbroken. The record's
      own commit cannot name itself; the closing message adds it. `ccclose`
      lists a commit as the session's only where its own transcript, or a
      subagent's, shows a commit command that made it; the rest of the window
      prints as *unconfirmed*, to check before it is pasted as fact. A worker
      dispatched as its own session has its own transcript, which the block
      does not read, so an orchestrator's workers' commits print as
      unconfirmed: confirm them by hand from the workers' reports.
    - **Pull requests**: the number of each one the session opened, merged or
      landed, and which it did.
    - **Board**: by number, the items the session completed, the new items
      it created, any it claimed and left open, and the `⏳` review items it
      queued.
    - **Worktrees and branches**: each one the session created, by path and
      branch, and whether it was put away. A removed worktree leaves no trace
      in git, so this list comes from the transcript.
    - **Agents**: how many it launched and how each ended.
    - **Other repos** it wrote to, with their commits. A private repo is named
      generically in a public record (§ *The record is public*); the closing
      message to the principal names it.
    A record extended after its close (an addendum, a resumed session)
    re-reads the block with `ccclose --identifiers` and replaces it, or dates
    the block it leaves as of its first close. Left alone, the window stops
    at the first close while the commits keep growing, and the totals
    disagree (2026-11-08, `160/900` QK14: a record extended five times read
    that way).
    Asked for by Mike, 2026-10-18 (`180/080`): *"the useful identifiers at the
    tail of the session. I am thinking things like commit ID's created by the
    session, the session ID and any others you recommend"*, then *"Other ID's
    to record at the end would be PR ID's worktrees created"* and *"and work
    IDs completed from the board, and new work ID's created"*. The rest of
    the set is the agent's recommendation.
- **Finish the sequence, then *declare* the close.** When the agent judges a
  **sequence of work** done, it does the full tidy-up **unprompted** and *says
  the session is ready to close* — the principal closes on the agent's signal,
  never by having to ask "are we actually done?". Two conditions, both required:
  **(a) the tidy-up is genuinely done**, and **(b) the principal has a clear
  all-done message**. The invariant that tests it: if the principal asks "ready
  to close?", the honest answer is *already* yes — the agent is never caught
  replying "wait, there are things to do first". What "tidied up" means is
  **situation-dependent** — write the session entry, update the roadmap /
  changelog / follow-ups, commit and push, close out worktrees and PRs — take
  the subset the work actually left owing.
  - **The boundary is the balance.** The trigger is *completing* a sequence, not
    a pause *within* one. Stopping mid-sequence to show or ask something — a
    question, a checkpoint, an issue worth understanding first — is always fine
    and carries no close-obligation. Declare the close only when the sequence
    itself is complete. (Grounded 2026-07-12: the signal had run on soft habit
    and drifted after a model change — the artefact was mandated, the signal
    wasn't; Mike sharpened the sequence-vs-within-sequence boundary the same day.)
  - **The all-clear carries its evidence.** The close message does not just
    assert "done" — it *shows* what was captured and put away (session entry,
    roadmap/records updated, commits pushed, worktrees/PRs closed, review queued
    if owed), so the principal closes on verifiable fact, not on trust. The form
    is free — a sentence, a checklist, a small table — but "nothing is owed" is
    itself a claim, and the apex rule that a claim never runs stronger than its
    evidence binds it (`00-APEX.md`). An honest all-clear also *names* anything
    deliberately left open. The test: the principal reads it and closes without
    a nagging "did it really capture everything?" (Grounded 2026-07-20, Mike:
    the declare-the-close signal is only worth the evidence under it.)
    - **A loose end makes the close "not ready until you decide".** A loose
      end is something the close owes and has not put away; open work
      recorded on the board is not one. A close that names its own loose ends
      under "ready" fails the invariant above. The session clears what it can
      before declaring. One it cannot clear, such as a refused delete or a
      pull request held for the principal's ruling, is put to him through the
      decision device (`COMMUNICATION.md` § *Asking for a ruling*), and the
      message says *not ready until you answer*, never "ready". The headline
      claims no more than its evidence: "the scratch folder is clean" over a
      check that found no folders is a claim past it. `ccclose`'s *Scratch
      folder empty* check counts what the session's agents left there.
      (Grounded 2026-10-18, `180/170`: a close opened "✅ Ready to close"
      above an open pull request and 50 files left in the scratch folder after
      both deletes were refused, and asked nothing through the device; on
      reopening it said "the scratch folder is clean" with about 98 files
      still there.)
    - **The evidence names every agent the session launched, and how each
      ended**: reported back, or stopped on purpose and said so. It is read
      from the agent list at that moment, never from memory, and `ccclose`'s
      *Subagents finished* check reads it. A declaration made with an agent
      still running is not a declaration: closing the tab kills that agent
      silently, and the harness's "didn't finish" notice only appears if the
      session is resumed (so the teardown rule in `CONCURRENCY.md`
      § *Orchestrated queue runs* does not rest on that notice alone).
      (Grounded 2026-10-16, `020/420`: a read of 30 sessions found every close made with no agent still running, but eleven
      agents cut by a host crash survived only because their sessions were
      resumed.)
    - **When the close pushes, the evidence is the *floor at head*, not the
      local scan.** "Scanners green locally" is not "floor green at head": CI
      runs checks a local scan does not — reviewscan over what the push itself
      queued, the harvest gate a pushed `[x]` trips — so a tree that scanned
      clean can still red the floor once pushed. An all-clear that closes with a
      push therefore carries the *pushed* floor run's result, or names it as
      pending ("green locally, floor run pending"); "all green" asserted before
      the head run reports is a claim past its evidence. (Grounded 2026-07-23: a
      00:47 close pushed a 🎯-closed item and left the floor red — reviewscan
      since 00:06 plus its own un-harvested `[x]` — and the next session
      inherited the debt to restore green, `165c40f`.)
    - **A push to `main` mid-run is held to the same bar as the close.** The
      floor-at-head rule above is written for the close, but the break it
      guards against also lands from a mid-run merge. Before a merge or push
      of doctrine, a skill or a test to `main`, run the full suite, not only
      the test the change added. (Grounded 2026-10-18: the commit that made
      the queue-run skill load the prompt file landed with six failures in
      `test_templates.py`, the author having run only the new test, and the
      repair came 16 minutes later; `160/900` QK2.)
    - **A *cancelled* run is not a result, and a concurrent session cancels
      yours as a matter of routine.** Where the floor runs under
      `cancel-in-progress: true` — as atelier's `ci.yml` does; a child's
      caller workflow may not — a second session pushing to the same ref
      kills the in-flight run for *your* commit. It ends `cancelled`, which
      is neither pass nor fail, and no run ever reports on the commit you
      pushed. A later commit's green run is **not** a substitute: it
      evidences a different tree, and it is only reassuring at all when your
      commit is an ancestor of it. The all-clear is stated positively: it is
      conclusion `success` on a run for your own SHA, and anything else
      (`cancelled`, `timed_out`, a startup failure, "the run finished") is
      not one. On `cancelled`, re-run it against your own SHA and wait for
      that, **once the group is quiet** (no floor run in flight on the ref):
      a re-run re-enters the same concurrency group, so started while
      another session's run is in flight it cancels that run, inflicting the
      harm this clause guards against. (Grounded 2026-08-09: a doctrine push
      went green locally, its head run was cancelled about 100 seconds later
      by a parallel session's push, and the close cited the superseding
      commit's green — true, but evidence for someone else's tree.)
  - (See also session hygiene in `ECONOMICS.md`: log where you got to, then
    start fresh rather than dragging a bloated context.)

## A session with no repo — what it reads, keeps and hands on

Every onramp and close-out above assumes a tree: a repo's `CLAUDE.md`, a
session log, a board, a commit. A session opened outside any repo (a small job,
an idea being shaped) has only the person-level instructions, and the record
rules have nowhere to land. Three gaps, one answer each. (Approved 2026-11-09,
`410/010`, as Mike's pick from options offered, not a ruling in his words.)

- **Onramp: a thin person-level one.** A short file in the person's own
  configuration, not in any repo, that points at the house doctrine and says
  which parts bind a session with no tree. The rules that need no tree bind
  as written: the apex, the `AUTONOMY.md` floor, `DATA-PROTECTION.md`, the
  calibration and ask rules in `COMMUNICATION.md`, and the defaults in
  `CONVENTIONS.md`. The rules that act on a tree (worktrees, claims, the board,
  the session log) have nothing to act on and do not bind in form. As with the
  calibration in `COMMUNICATION.md`, the pattern is shareable and the instance
  stays person-local.
- **Record and close: move to the repo before recording.** For shaping work the
  default is that the session moves to the repo the work belongs to, or opens
  one, **before it records anything**, so the first record lands where a later
  session will read it. Where no repo exists yet, the thinking stays in the
  reply until one does. A small job that belongs to no repo closes with a
  plain statement in the reply of what was done, what is left, and where any
  output went. Nothing reusable is left only in the person's memory store, which
  no future session of the repo will read.
- **Hand-on: the output reaches the repo it belongs to by a route, not by
  luck.** The routes are the principal carrying it across, or a message to a
  live session in that repo (`CONCURRENCY.md` § *Talk first*). Handing it on as
  a pull request is a further route that is not settled here.

**The privacy line travels with the output.** A session with no repo is where
person-level context is closest to hand, so whatever it carries into a repo,
above all a public one, is checked against that repo's own boundary before it
lands, by what it describes and not by where it came from (§ *The record is
public* below; `DATA-PROTECTION.md`). Abridge on the way in and say that you
abridged.

**Not decided, and not built.** The person-level onramp file itself belongs to
the person, not to this repo, and is the person's to create. A standing scratch repo that
repo-less work defaults into was considered and not adopted: it is the cheapest
to try and the likeliest to become a dumping ground.

## Decisions — ADRs for anything a future session might re-propose

A decision that a later session could reasonably reopen ("why isn't this a
monorepo?", "why sops+age not vault?") is recorded as a short **ADR** in
`docs/decisions/` — context, the decision, the alternatives, the consequences.
The test is *re-litigation risk*: if forgetting the reasoning would cost a future
session a wasted argument, write the ADR.

An ADR moves through the lifecycle standards bodies use (the IETF/IEEE shape:
draft → active → superseded or withdrawn). **Draft** is the one mutable
state — the deliberation written down, binding on nothing yet; accepting it is
the principal's decision, never the author's — and an informed one: the draft
must put what it decides, why, and its consequences in plain language before the
principal accepts (`00-APEX.md`, *The principal's authority is absolute; his
rulings are conditioned on being informed*). Once **accepted**, an ADR is
immutable — the substance of what was decided, and on what reasoning, is never
rewritten (the append-only principle again). Everything after acceptance
happens by *appending*, in one of three verbs:

- **Addendum** — a dated section appended to the ADR when the same decision
  matures: a scope extension, a corrected claim, a sharpening. The accepted
  text above it stands untouched. (Grounded: ADR 0007's addendum 2026-07-12;
  the record-identifiers ADR's same-day addendum 2026-07-13.)
- **Revoked** — the decision stops applying without a replacement: the status
  line gains `revoked <date>` and a dated addendum says why and from when. The
  file stays in the record — a revoked decision still explains the era it
  governed.
- **Superseded** — a new ADR replaces it: the status line gains
  `superseded by <file>`, and the new ADR points back. Never an edit.

## An approval is not the whole ruling — the reservations go in beside it

**When a recommendation is approved *with reservations*, the reservations go
into the record beside the approval, and each one becomes a check the build has
to answer** (the principal's ruling, 2026-08-17; the rule was earned on
2026-08-15 and had reached no doctrine surface until this).

The grounding is a build that shipped and failed. A guard was recommended, the
principal approved it **and raised several reservations**, and the record
captured four words of approval and none of the objections. So the objections
that would have predicted the failure were never written down, never tested
against the build, and the guard was live for six days before the failure they
described arrived. The reservations were not reconstructed afterwards either —
reconstructing them from memory is the same error one level down, and the
record says so instead.

Two things follow, and the second is the one that bites:

- **Capture is the approver's word, not the recorder's summary.** The
  reservation goes down as it was said (the verbatim rule above), because a
  paraphrase of an objection is an objection you have already started to
  answer.
- **A reservation is a *check*, not a caveat.** It is not enough to have
  written it down. Each one names something the build must answer before the
  work is called done, and the answer belongs beside it. An unanswered
  reservation is an open finding wearing a softer word.

This is why an approval alone never closes a recommendation: the approval says
*proceed*, and the reservations say *proceed how*, and only the pair is the
ruling. See `GUARDS.md` § *A rule with no home is not a rule* for the class
this instance belongs to.

## What the principal said arrives three ways — read and honour all of them

The principal speaks to a session through **three channels**, and a record or an
audit of "what did he ask for" that names only one is a confident negative:

1. **The opening prompt** — the message that starts the session.
2. **Mid-turn messages** — typed while the session works. They arrive as
   steering, not as a brief, so they feel lighter than they are.
3. **Question-box picks** — a selection in the structured decision device
   (`COMMUNICATION.md` § *Asking for a ruling*). In a Claude Code transcript
   these are stored as three different record types, and a read that filters
   on the first (`type == "user"`) drops the other two **silently**.

Two rules follow. Mike chose both from options put to him on 2026-11-08 ("Adopt
both rules"; an answer to a question asked, not a ruling in his own words —
`320/070`).

- **A mid-turn instruction counts exactly like an opening one.** The session
  acts on it, and one meant to stand — a rule, a ruling, a scope — is written
  down where later sessions will see it, before the turn ends. This is
  `GUARDS.md` § *A rule with no home is not a rule* applied to an arrival mode
  rather than a rule type: an instruction that arrived as steering and was
  homed nowhere governs nothing after the session closes.
- **An audit of what the principal asked for says which of the three channels
  it read.** Without that, its negatives are artefacts of its filter. "He never
  asked for that" is a claim about the corpus the audit read, and it states
  that corpus.

**Why it earned doctrine.** The loss is scope, not sampling noise. Measured
across the estate's transcripts (2026-08-21, classified identically on both
channels), **24.3%** of what the principal typed arrived mid-turn (3,013
opening against 965 mid-turn), and in one child repo all nineteen of its most
consequential instructions did. Four of the five deliverables that repo exists
to produce were commissioned in messages an opening-prompt read cannot see.
A second repo then rebuilt a requirements list and its extractor dropped his
founding message the same way, returning 3,020 plausible messages that looked
correct. This house's own `cctranscript` read only the first channel and
printed `searched prompts+replies` anyway (`210/100`).

**Both halves, or the rule trades one wrong count for another.** A channel's
*record type* is not its *authorship*. Only **43.3%** of mid-turn records are
typed by the principal; the rest are task notifications, messages from other
sessions and system reminders, which arrive in both records. Widening a read to
the mid-turn channel without also filtering for who wrote each record counts
system text as his words. So an audit, a corpus or a scanner built on this
section names **both**: which channels it read, and how it told his typing from
injected text. Records that predate the field that marks the origin of a
message need their own rule, not a silent drop (one child lost 1,305 that way).

## The roadmap — one file per item, a generated index

The board is a **per-item store** (board-store ADR, 2026-08-15): each item is
its own file under `docs/roadmap/<section>/`, holding its checkbox state line
first and its detail beneath; each section's narrative is that section's
`README.md`; and `ROADMAP.md` is a short **generated index** (`tools/board.py`,
enforced by the `board` floor check) that every session reads at open. Three
defect classes drove the split, each grounded in this repo's own history:

- **Contention at file grain.** Claiming collides on one line by design, but
  every session then edited one shared file — and a wholesale revert of it
  destroyed a sibling session's in-flight work (2026-08-09). Per-item files
  make different-item edits touch different files; only a same-item edit
  collides, which is the collision the mechanism *wants*.
- **Read cost.** A monolithic board reached 4,000+ lines (~67k tokens),
  ordered read at every session open — a finished item kept accreting the
  story of how it got done, history living in a current-truth file. (Grounded:
  a sibling roadmap reached 3000+ lines that way, ~75% completed detail.)
- **State asserted, not derived.** "Done" lived in prose that drifted from the
  tree five recorded times. An item file's own `git log` is provenance — which
  commit flipped the state, and what work it carried.

A completed item simply flips `[x]` **in its own file, in the commit that
finishes the work** — there is no harvest step, and the harvest's red-window
failure mode is retired with it. Pre-split completed detail stays frozen in
`ROADMAP-DONE.md` (append-only, grepped on demand). A repo that has not
adopted the split keeps the monolithic form; the relocation discipline for it
— completed detail out of the hot path, specs grepped on demand — remains as
it was, and `sizescan` still polices it.

**Bulk deletion from a record store is a show-first action, regardless of who
created the mess** (the principal's ruling, 2026-08-04). Before removing a
block from a record store — ROADMAP, SESSIONS, ADRs, reviews — either diff it
and show the principal what goes, or ask. One message, and it removes the
class. Two intuitions make an unshown deletion feel safe, and neither holds:
*"it's my own mess"* — the sections encode the **principal's** rulings, not
the agent's drafts, and deleting the record of another party's decisions is a
different act from deleting your own working notes; *"git remembers"* — git
remembers the *text*, not that the work was supposed to happen, and a roadmap
item that vanishes means the work does not get done, which is closer to
irreversible than the mechanism suggests. Recoverability of bytes is the wrong
test for a record store. (Grounded 2026-07-25: a 185-line "duplicates"
removal, compared by heading names only, was diffed on challenge — thirty
seconds — and one of the five sections was a genuine loss, a completed item
whose only roadmap trace went with it.) The mechanical net beneath this rule
is `tools/harvestscan.py`'s bulk-deletion warn; the rule covers what the net
cannot see, and `AUTONOMY.md` § *Before you destroy or overwrite* carries the
same duty at the general layer.

This is one pattern the whole record shares: **current-truth files stay lean;
history relocates to an on-demand store.** SESSIONS (index + `docs/sessions/`),
the board (generated index + per-item files; pre-split detail in
`ROADMAP-DONE.md`), a README that points into `docs/` — the same
shape. The discipline decays silently, though: the split gets done once by hand,
then nothing fires when a file bloats again. So, for the one form a machine
can name, it carries a **signal** — `tools/sizescan.py`. Cost is size ×
read-frequency (Mike's ruling, 2026-07-20),
so the signal keys on **relocatable cold content on the hot path**, not length:
it **gates** on a completed `[x]` item in a checkbox-worklog file (a done item
belongs in `ROADMAP-DONE.md`; left inline it is pure cost with a lossless fix),
and does not report line count at all (Mike's ruling, 2026-10-05: no arbitrary
size limits; the old length advisory was removed 2026-10-16), because a file
long purely from live current-truth has nothing to relocate. Resolved narrative
under an open item is real cold content a machine cannot name, and no tool or
scheduled review looks for it: nothing fires when a file bloats with it, so
keeping it out is the writing session's discipline and the next session's
noticing. Growth stores are excluded by design; flagging the
*destination* would punish the fix. The
destination has its own contract, though — **harvest integrity** (Mike's ruling,
2026-07-22): the named archive stores (`*-DONE.md`, `*-ARCHIVE.md`) record
finished history only, so a live state marker there (a `[ ]`/`[~]`/`⏳` list
item) also gates — it is either a botched harvest or a box never flipped, and
the remedy is investigate-then-recommend, never a silent fix. And the signal
carries a **trigger**: on a **monolithic** board, harvesting is part of the
session-close tidy-up (above). When a session closes roadmap items, collapsing
them to pointers happens then, not someday. A split board has no harvest step:
a closed item flips `[x]` in its own file (above). That is what stops the
3000-line accretion from ever forming.

## Absolute dating, everywhere in the record

Every dated thing in the record — session entries, ADRs, doctrine changes,
roadmap ticks — states the date **absolutely** (`2026-07-10`), never "today" or
"last week". A record is read out of its writing-context by definition; relative
time is meaningless to the reader who finds it three weeks later, and ambiguous
across models with different cutoffs. (EVIDENCE §7.) And the absolute date is
the **UTC** date (ADR 2026-07-15): an NZ morning is still the previous UTC day,
so the prose date matches the record's own UTC identifier, not the wall clock.

## Describe, don't quote — record prose never carries the shapes the floor hunts

When record prose needs to reference something a floor scanner exists to
catch — an example credential, a licence tag, a stamp or allow-marker's
literal syntax, an address-, phone- or network-shaped string, a probe input —
**describe the shape; never quote it literally.** A scanner that flags such a
line is *correct*: the value's shape is what it scans for, and prose context
is precisely what a fail-safe scanner must not trust. Quoting therefore costs
an allow-marker on a line that was never wrong, and every such marker trains
readers to reach for exemptions — which is how a scanner's findings stop
being believed. Describing is the cheaper move and leaves no exemption debt
behind. (Ruled by the principal 2026-08-04 on **recurrence, not severity** —
four instances in three weeks, each trivial alone: an example credential, a
literal licence tag in a roadmap entry, a stamp marker mentioned in a review
file, and a sweep record that had to describe every probe shape to avoid its
own subject scanners. Three instances of a trivial failure is a defect in the
system producing it.) The carve-out is deliberate content: a test fixture or
canary *inside a tool's own suite* quotes shapes by design; the rule binds
the record stores and doctrine surface, where prose is read, not executed.

## The record is public — keep private repos generic

atelier is public (ADR 0005): its record publishes on every commit — and on a
public repo a scrub of HEAD is not remediation, because the scrubbed prose stays
reachable in pushed history forever. So this rule can only ever bind at
**write-time**. The no-personal-estate-data rule covers **prose that describes**
private-estate security posture, not only literal secret *values* — a
pattern-matching leak scanner catches the value `AKIA…`, never the sentence
"repo X keeps a live key in its history". The regulated class is the **join**:
a private repo's *name* coupled to its *sensitive posture* — which secrets it
holds, where, their exposure history, its publication intent, or the
confidential content it carries. Naming a private sibling is not the harm —
adoption lists and pin bumps name children legitimately, and the record's
resumability depends on it; the test is whether the name is load-bearing for
the lesson. A *worked example* in a doctrine file is the exception: it names no
private child, only "a private child" (Mike's pick from options offered,
2026-11-09, `320/330`; `PROPAGATION.md` § *The route* rule 2). When a record
must describe
security work, either the name or the posture goes generic ("an infra repo",
"a captured runtime snapshot"), and the fine detail lives only in the private
repo's own records. Enforcement, stated honestly (PROPAGATION's enforcement
clause): no scanner can hold this rule — by its own premise the mechanical
floor is unavailable — so it binds through write-time discipline plus periodic
review sweeps of the record, nothing stronger. (Grounded: 2026-07-11 —
session-record posture prose leaked into public atelier, scrubbed at HEAD but
permanent in history; the 2026-07-12 cold review then found the name-to-posture
join had survived that scrub in four more places.)

**A private repo's state is described by its type only.** The join rule above
guards *sensitive* posture. A wider band sits next to it: what condition a
particular private repo was in (its checks passing or failing, its findings, how
far its pin lagged). In a public record that goes by type — "a private child
was failing a check", not the name. Naming a private repo in any other context,
including an act done to it (a pin bumped, a floor installed), stays allowed.
Forward only; no scrub. Decided 2026-11-08 (Mike's pick from offered options, not
his own words); the reasoning and the rejected postures are in
[the ADR](../decisions/2026-08-05-1233-estate-internal-context-in-public-records.md).

**The estate-root repo gets no stricter rule.** It is a private repo like any
other: the name is allowed, and what it holds and its condition go by type only
(Mike's pick from options offered, 2026-11-09, `020/050`: *"Treat like any
private repo"*; an answer, not a ruling in his words). The earlier rule that
named it only in a private child's onramp, never in any public tree, is
withdrawn, forward only; `PROPAGATION.md` § *Doctrine — inherited from atelier*
keeps the account. The name joined to what the repo holds stays barred by the join
rule above.

## Why this is doctrine, not just tidiness

The whole operating model assumes a session can be **resumed cold** — by another
model, on another day, possibly on another device. That assumption is only true
if the record carries the state: what was decided (ADRs), what happened
(sessions), what's true now (architecture + roadmap), and what's owed (roadmap +
review follow-ups). The record is the substrate propagation, review, and
resume-from-anywhere all stand on. A silent gap in it is a defect.
