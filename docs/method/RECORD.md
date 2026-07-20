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
  read at session start (tail it). Append-only is a rule about **content** — an
  entry is never edited or reordered once written — **not a fixed home**: like
  the roadmap, an index that outgrows its budget **rotates**. The recent tail
  stays in `SESSIONS.md`; older entries relocate **verbatim** to a
  `SESSIONS-ARCHIVE.md` growth store (grepped on demand, never loaded whole) —
  the same current-truth/history split as `ROADMAP`→`ROADMAP-DONE`, and the
  answer to the one move a bloated *already-split* index otherwise lacks.
  `tools/sizescan.py` flags the index when it crosses budget. (Grounded
  2026-07-14: the cold review found the append-only rule and the budget colliding
  with no sanctioned move for an index that had already done the split.)
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
  - (See also session hygiene in `MODEL-ECONOMICS.md`: log where you got to, then
    start fresh rather than dragging a bloated context.)

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
principal accepts (`00-APEX.md`, *The principal's authority is conditioned on
being informed*). Once **accepted**, an ADR is
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

## The roadmap — current-truth, with completed detail moved aside

`ROADMAP.md` is **current-truth**: what's open, prioritised, read every session.
Its failure mode is subtler than "finished items pile up" (they do): a *finished
item keeps accreting the story of how it got done* — a correction, a review
verdict, a live-proof note, a suite count. The item quietly becomes a mini
session-log. That narration is valuable **case-law**, but it is *history* (what
happened) living in a *current-truth* file (what's open), and every session pays
to load it. (Grounded: a sibling roadmap reached 3000+ lines this way, ~75%
completed detail; atelier's own reached 1091 before the same harvest.)

The fix is relocation, never deletion (a de-cased roadmap is as much theatre as a
de-cased principle):

- **A completed item collapses to a one-line pointer** — the outcome plus a link
  to where the detail already lives (the session detail file that captured it, or
  `ROADMAP-DONE.md`). The case-law is preserved on demand, not loaded every time.
- **Completed detail moves to `ROADMAP-DONE.md`** — the append-only store that is
  *meant* to grow, the same index/detail split as the session log.
- **Full specs of pending features live in a `SPECS.md`** grepped on demand,
  never loaded whole.

This is one pattern the whole record shares: **current-truth files stay lean;
history relocates to an on-demand store.** SESSIONS (index + `docs/sessions/`),
ROADMAP (open + `ROADMAP-DONE.md`), a README that points into `docs/` — the same
shape. The discipline decays silently, though: the split gets done once by hand,
then nothing fires when a file bloats again. So it carries a **budget and a
signal** — `tools/sizescan.py` reports any current-truth file over its line
budget (advisory; the growth stores are excluded by design, since flagging the
*destination* would punish the fix). And it carries a **trigger**: harvesting is
part of the session-close tidy-up (above) — when a session closes roadmap items,
collapsing them to pointers happens then, not someday. That is what stops the
3000-line accretion from ever forming.

## Absolute dating, everywhere in the record

Every dated thing in the record — session entries, ADRs, doctrine changes,
roadmap ticks — states the date **absolutely** (`2026-07-10`), never "today" or
"last week". A record is read out of its writing-context by definition; relative
time is meaningless to the reader who finds it three weeks later, and ambiguous
across models with different cutoffs. (EVIDENCE §7.) And the absolute date is
the **UTC** date (ADR 2026-07-15): an NZ morning is still the previous UTC day,
so the prose date matches the record's own UTC identifier, not the wall clock.

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
