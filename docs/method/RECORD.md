# Record — docs are code, and the session is part of the build

*The doctrine, the design decisions, and the trail of how the work got here are
**artifacts in the repo**, versioned and changed in lockstep with the code — not
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
recover from the artifact itself is the *reason* — the platform quirk, the
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
  read at session start (tail it). Never rewritten; history is not edited.
- **Detail lives on demand** — when a session is substantial, its full detail
  goes in a `docs/sessions/<date>-NN-slug.md` file and the index carries a
  one-line pointer. Open the detail file only when a line needs unpacking. This
  keeps the always-loaded index cheap (token discipline) without losing depth.
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
    and drifted after a model change — the artifact was mandated, the signal
    wasn't; Mike sharpened the sequence-vs-within-sequence boundary the same day.)
  - (See also session hygiene in `MODEL-ECONOMICS.md`: log where you got to, then
    start fresh rather than dragging a bloated context.)

## Decisions — ADRs for anything a future session might re-propose

A decision that a later session could reasonably reopen ("why isn't this a
monorepo?", "why sops+age not vault?") is recorded as a short **ADR** in
`docs/decisions/` — context, the decision, the alternatives, the consequences.
The test is *re-litigation risk*: if forgetting the reasoning would cost a future
session a wasted argument, write the ADR. An ADR is immutable once decided;
superseding it is a new ADR that points back, never an edit (the append-only
principle again).

## The roadmap — current-truth, with completed detail moved aside

- **`ROADMAP.md` stays lean** — what's open, prioritised, read every session.
- When it grows, **completed detail moves to `ROADMAP-DONE.md`** rather than
  bloating the live file — the same index/detail split as the session log.
- Full specs of pending features live in a `SPECS.md` grepped on demand, never
  loaded whole.

## Absolute dating, everywhere in the record

Every dated thing in the record — session entries, ADRs, doctrine changes,
roadmap ticks — states the date **absolutely** (`2026-07-10`), never "today" or
"last week". A record is read out of its writing-context by definition; relative
time is meaningless to the reader who finds it three weeks later, and ambiguous
across models with different cutoffs. (EVIDENCE §7.)

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
adoption lists, pin bumps, and worked examples (e.g. ros, faves, numen) name
children legitimately, and the record's resumability depends on it; the test is
whether the name is load-bearing for the lesson. When a record must describe
security work, either the name or the posture goes generic ("an infra repo",
"a captured runtime snapshot"), and the fine detail lives only in the private
repo's own records. Enforcement, stated honestly (PROPAGATION's enforcement
clause): no scanner can hold this rule — by its own premise the mechanical
floor is unavailable — so it binds through write-time discipline plus periodic
review sweeps of the record, nothing stronger. (Grounded: 2026-07-11 —
session-record posture prose leaked into public atelier, scrubbed at HEAD but
permanent in history; the 2026-07-12 cold review then found the name-to-posture
join had survived that scrub in four more places.)

## Why this is doctrine, not just tidiness

The whole operating model assumes a session can be **resumed cold** — by another
model, on another day, possibly on another device. That assumption is only true
if the record carries the state: what was decided (ADRs), what happened
(sessions), what's true now (architecture + roadmap), and what's owed (roadmap +
review follow-ups). The record is the substrate propagation, review, and
resume-from-anywhere all stand on. A silent gap in it is a defect.
