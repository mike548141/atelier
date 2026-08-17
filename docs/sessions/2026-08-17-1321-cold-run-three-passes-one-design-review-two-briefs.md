# 2026-08-17 · 1321 UTC · Three cold passes run, one design review, two briefs written — the whole rule-4 queue in one sitting (wt: cold-run-0817-1321)

**Mike's instruction, verbatim, opening a cold session on the Fable tier:**
*"Please do any reviews and any fable dependent work. Write any briefs required
too"*

The two-session split of 2026-08-15, applied to the whole queue at once: every
pass this session ran came from a brief a *different* cold session wrote and
stopped on (the 0955 Fable session); the two briefs this session wrote, it
stopped on in turn. Nobody reviewed their own brief; nobody reviewed their own
work.

## Tier, stated first

Cold passes run on the tier the principal names — Fable. **This session is
Fable**, and so were the four reviewer subagents it spawned. The orchestrator
held the context partition, released the siblings, and committed the records;
it formed no finding and wrote no severity — the shape `REVIEW.md` rule 4 now
describes, disclosed in the claim (`574f133`), in each pointer and in each
verdict's provenance. One of the four passes reviewed that very clause; its
reviewer recorded that the shape and its disclosure conditions were followable
in its own case, and that the off-tier permission was not exercised because
both hands were Fable.

## What the queue held, and what was done with it

| Pointer | State on arrival | Outcome |
|---|---|---|
| `160-…/230` the 2026-08-17 ruling round applied | brief written 0955, **never run** | **RAN** — PASS-WITH-FINDINGS, 0 MAJOR / 4 MODERATE / 5 minor / 5 note; cycle CLOSED; RR1–RR14 to Mike |
| `160-…/240` `coldsweep.py` | brief written 0955, **never run** | **RAN** — PASS-WITH-FINDINGS, **3 MAJOR** / 5 MODERATE / 2 minor / 1 note; cycle stays **OPEN**; SW1–SW11 to Mike |
| `280-…/030` the channel section + floor clause | brief written 0955, **never run** | **RAN** — PASS-WITH-FINDINGS, 0 MAJOR / 5 MODERATE / 11 minor / 4 note; cycle CLOSED; CH1–CH16 to Mike |
| `290-…/070` CMF1: repurpose `plain-reply.py`, else destroy | Fable design review, brief-less by design | **RAN** — verdict **DESTROY**, 0 MAJOR / 3 MODERATE / 2 minor / 3 note; decision Mike's |
| `160-…/260` the BS1 wording applied | **brief-less** | **BRIEF WRITTEN, NOT RUN** (`BW`) — open for a cold Fable taker |
| `300-…/040` the posture section + fourth guard requirement | **brief-less** | **BRIEF WRITTEN, NOT RUN** (`PT`) — open for a cold Fable taker |

`160-…/080` and `160-…/090` still lead with `⏳` and were left alone: both
cycles ran on 2026-08-09 and wait on the ruling round, not a reviewer — item
`130-…/010`'s stale-`⏳` shape, still worth its ruling. **The pointers this
session closed do not inherit that shape**: each was rewritten to lead with
its closed (or 🛑 open) state, the queue glyph gone, so a future taker's grep
finds no work there.

## How the passes were run

- **Claim on `main` first** (`574f133`), before the worktree and before any
  reviewer was spawned: three pointers TAKEN/RUNNING, the design review TAKEN,
  two claimed for brief-writing only, tier stated in the commit body.
- **Orchestrator-held context partition, four reviewers in parallel**, one
  worktree: the three `.deferred.md` siblings moved out of the tree into the
  session scratchpad before spawning; one common instruction file (paths,
  tools, barred set, deliverable shape, release timing — process, not
  questions) plus a per-pass note naming the brief, the prefix and the
  pass-specific barred board paths; mutation probes in scratch clones under
  the scratchpad; no git from any reviewer; `/security-review` forbidden;
  each reviewer barred from the other three briefs in the same directory.
- **Phase 1 committed before release**, one commit per pass (`b7e0da5`,
  `516be0b`, `08df5ca`, `16da277`), then the sibling's text released by path
  with a scoped, ordered list of what could then be opened; reconcile appended
  beneath, never revising phase-1 text; siblings folded in and deleted in the
  closing commits (`f236153`, `99e72d3`, `419fdac`).
- **`coldsweep.py` was every reviewer's sweep instrument** — and one reviewer's
  subject. Its own pass found the tool correct on the happy path and silently
  non-applying off it, which is the finding class the whole day has been
  about: a string true from one place, asserted from every place.
- **One prefix collision caught late:** the design review was briefed with
  prefix `PR`, which a 2026-08-02 pass already used; the reviewer was
  re-prefixed to `RP` mid-flight, before any ID was written. Prefix
  uniqueness is checked by hand against filenames and by grep; nothing
  guards it.

## What the passes found, in one paragraph each

**RR (the ruling round applied).** The three rulings are rendered, and every
re-run reproduced (both floor planes green, Python 1,344 / node 235,
stampscan identical at 61 lines). What did not hold is the *fit* to what was
ruled: the apex's always-confirm exception re-enumerates the floor list
narrower than `AUTONOMY.md`'s (RR1); rule 4's "forms no finding" condition
is an attestation with no boundary drawn around orchestrator acts (RR2 —
this run's own instruction file is the example); `RECORD.md`'s new section
leans on "the verbatim rule above" and no such rule exists on that surface
(RR3); and at reconcile, the intent record's scope list for ruling two ticked
seven surfaces of which four were touched (RR12). Reconcile against the
ruling record: ruling one adds two conditions the ruling did not state,
ruling two adds an enumeration and drops three named surfaces, ruling three
matches but cites a non-existent neighbour.

**SW (`coldsweep.py`).** Happy path correct: selftest OK, 289 barred files
reproduced at the landing commit, both suites and both planes green. Off it,
**the bar silently does not apply while the provenance line says it did** —
three MAJORs: an absolute, `..` or mistyped `--also-exclude` excludes nothing
and echoes a machine path into the paste-into-verdict line (SW1; this run's
own reviewer instructions say "absolute paths everywhere"); `--root` at a
subdirectory or a child with a relocated `docs` bars zero files at exit 0
(SW2); nested harness worktrees — two live siblings, 596 barred-by-name files
from the main checkout — and all gitignored material are searched (SW3).
MODERATEs: the tuple is the only statement of the barred set and rule 2's
prose names only prior reviews, while onramp step 4 sends every session to
the `SESSIONS.md` tail (SW4 — the collision every brief-writer since 2026-08-15 has
disclosed, live); diagnostics on stdout after the hits (SW5); unreadable
files silently counted as swept (SW6); the tool named on no reviewer-facing
surface but rule 2 (SW8); `--include-barred` silently drops every
`--also-exclude` (SW11, formed at reconcile from a seeded question and
verified in code). Corpus ↔ instances: the released verdicts carry two
`./`-prefix instances and the selftest pins exactly that; the earlier
"instances" were a different class.

**CH (the channel section).** The doctrine says what its sources say, mostly:
of thirteen grounding claims checked against the transcript and the public
child's records, eight verified, five with caveats, none falsified. The
MODERATEs are where the section stops short: the seven message classes are not
fenced against REVIEW.md rules 2/4 — an author's message to a would-be cold
reviewer is exactly the framing path rule 2 closes, and the brief's own
disclosure 3 was an instance (CH1, anticipated by the author's addendum and
already queued at `280/040`); the *ask* cue overclaims, since an empty peer
list is still silence (CH2); law 3's tie-break fixes no evaluation point and
no tie rule (CH3); *never `stash`* is unreconciled with the mandated
`--autostash` bookend at a dirty shared checkout (CH4 — upgraded from reasoned
to observed on the child's record); the abridge-into-the-record clause never
reaches the floor (CH5, privacy).

**RP (repurpose or destroy `plain-reply.py`).** **DESTROY.** The control the
commission asked for was run first and decided it: eight older sessions scored
with `plainscan`'s own engine over `cctranscript --json` — 45 replies, 25
flagged, the preceding prompt reachable for every one, and the transcript
carries `entrypoint`, `effort`, model, branch and context that a Stop payload
does not. A per-reply hook observes strictly less than the transcript already
at rest (RP1); its data would be derived and silently gappy (RP2); a logging
variant keeps the machine-wide fail-open surface and adds a written store for
no gain (RP3). Counsel, labelled: a small transcript-plane report over
`cctranscript --json` — a repurpose of the *engine*, not the hook. And the
item's *If DESTROY* checklist is **incomplete** against what CMF/RG/BG filed —
recorded beside the 🎯, so the ruling is taken informed.

## Two briefs, and what each holds closed

Each written from the diff of the delta paths at the landing commit and the
queue pointer, with the intent records and ruling board items unopened; prior
verdicts and seeded questions in the `.deferred.md` sibling. Two disclosures
stand in both — the `SESSIONS.md` tail was read at onramp before any brief
was commissioned, and each landing commit's message was read in full — and
one more in the BS1 brief: the authoring session's *record* was read in full
at onramp, second-sitting section included, before this session knew it would
write that brief. The posture brief names its own lens-4 question up front: a
verbatim principal quotation about an estate's network posture sits in a
public method doc, and whether that is personal-estate context is for the
reviewer to test.

## The channel, used

A child session that adopted the board store today announced two findings
against atelier's own tools mid-run — a claim fragment on a long title fails
the wrapscan floor on both the state line and the generated index line, and
`index_title`'s fallback swallows the claim into the title. Both were
**reproduced here before recording** (`3b116b2`: `010/130`, `010/140`), the
child's candidate shapes carried as reported with measurement apart from
diagnosis, nothing fixed (this session's lane is review). The child also
believed the fleet-rollout record did not know it had adopted; the record was
re-swept at 1057 and already carries its row — said so in the reply, with
what had *not* been done first.

## Handed to Mike

The ruling backlog grew by four clusters — RR1–RR14, SW1–SW11 (three MAJOR),
CH1–CH16, RP1–RP8 with a DESTROY verdict awaiting his word — on top of the
menu the 0955 session measured. Two briefs wait for a cold Fable taker. This
session presented and stopped, taking no ruling as read.
