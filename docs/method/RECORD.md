# Record — docs are code, and the session is part of the build

*The doctrine, the design decisions, and the trail of how the work got here are
**artifacts in the repo**, versioned and changed in lockstep with the code — not
lore in someone's head or a chat that scrolls away. A future session (or a peer,
or an independent reviewer) reconstructs the "why" from the repo alone. If it
can't, the record failed.*

## Docs-as-code — the core discipline

Documentation lives in the repo, in the same commit as the change it describes.
The rule is **lockstep**: a change to behaviour and the change to the doc that
governs it land **together**, or the doc is a lie the moment it merges. A commit
that alters the CLI surface and leaves the man page stale is not "done with a
doc follow-up owed" — it is a broken commit. (Scope: what binds is what lands on
the **shared branch**. A spike or WIP commit may trail its doc while it stays on
its own branch; the *merge* is where lockstep holds — "the doc follows next
week" landing on trunk is exactly the lie the rule exists to kill.) This is EVIDENCE §9 (one fact, one
home) plus the apex (no claim stronger than its evidence — a stale doc *is* an
over-strong claim about the code).

Consequences:

- **The doc that governs a thing changes in the thing's commit.** Man pages, the
  architecture note, the doctrine block — all move with the code.
- **Structure-as-documented must exist.** A README that lists a directory or a
  file that isn't there is a defect, not aspiration (an apex violation caught in
  the atelier foundation review itself).
- **Stub honestly.** What isn't built yet is *labelled a stub*, not written up in
  the present tense as though it exists. "Extraction in progress" beats a
  confident paragraph describing a thing that's empty.

## The session log — an append-only index with detail on demand

Every working session leaves a trace, so the next one starts from where this one
stopped instead of re-deriving it:

- **`SESSIONS.md` is an append-only index** — one entry per session, newest last,
  read at session start (tail it). Never rewritten; history is not edited.
- **Detail lives on demand** — when a session is substantial, its full detail
  goes in a `docs/sessions/<date>-NN-slug.md` file and the index carries a
  one-line pointer. Open the detail file only when a line needs unpacking. This
  keeps the always-loaded index cheap (token discipline) without losing depth.
- **Write it before finishing.** The session entry is part of the work, not an
  afterthought — the handoff is a deliverable. (See also session hygiene in
  `MODEL-ECONOMICS.md`: log where you got to, then start fresh rather than
  dragging a bloated context.)

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

## Why this is doctrine, not just tidiness

The whole operating model assumes a session can be **resumed cold** — by another
model, on another day, possibly on another device. That assumption is only true
if the record carries the state: what was decided (ADRs), what happened
(sessions), what's true now (architecture + roadmap), and what's owed (roadmap +
review follow-ups). The record is the substrate propagation, review, and
resume-from-anywhere all stand on. A silent gap in it is a defect.
