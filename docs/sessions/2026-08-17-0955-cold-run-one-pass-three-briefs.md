# 2026-08-17 · 0955 UTC · One cold pass run, three briefs written — both hands on Fable this time (wt: cold-run-0817-0955)

**Mike's instruction, verbatim, opening a cold session on the Fable tier:**
*"Do any reviews or fable dependent work and ask questions if the repo has
any."*

The two-session split of 2026-08-15, another turn along: the pass this
session ran came from a brief a different cold session wrote and stopped on
(the 0710 Opus session), and the three briefs this session wrote it stopped on
in turn. Nobody reviewed their own brief; nobody reviewed their own work.

## Tier, stated first because last time it was the thing to reject

Cold passes run on the tier the principal names — Fable. **This session is
Fable**, and so was the reviewer subagent it spawned: the 2026-08-15 shape,
not the 2026-08-17 0710 departure. The orchestrator held the context
partition, released the sibling, and committed the records; it formed no
finding and wrote no severity — which is now what `REVIEW.md` rule 4 says the
arrangement requires, since the ruling round earlier the same day wrote the
clause. Nothing to ratify here; the shape is on-tier in both hands and the
disclosure is made in the claim (`880a2d3`), the pointer and the verdict all
the same, because a reader should meet it rather than discover it.

## What the queue held, and what was done with it

| Pointer | State on arrival | Outcome |
|---|---|---|
| `160-…/220` board generator's child-facing strings | brief written 2026-08-17 0730, **never run** | **RAN** — PASS-WITH-FINDINGS, 0 MAJOR / 4 MODERATE / 4 minor / 4 note; cycle CLOSED; BG1–BG12 to Mike |
| `160-…/230` the 2026-08-17 ruling round applied | **brief-less** | **BRIEF WRITTEN, NOT RUN** (`RR`) — open for a cold Fable taker |
| `160-…/240` `coldsweep.py` | **brief-less** | **BRIEF WRITTEN, NOT RUN** (`SW`) — open for a cold Fable taker |
| `280-…/030` the channel section + floor clause | **brief-less** | **BRIEF WRITTEN, NOT RUN** (`CH`) — open for a cold Fable taker |

`160-…/080` and `160-…/090` still lead with `⏳` and were left alone: both
cycles ran on 2026-08-09 and wait on the ruling round, not a reviewer — the
stale-`⏳` shape item `130-…/010` describes, still worth its ruling.

## How the pass was run

- **Claim on `main` first** (`880a2d3`), before the worktree and before the
  reviewer was spawned: one pointer TAKEN/RUNNING, three claimed for
  brief-writing only, tier stated in the commit body.
- **Orchestrator-held context partition** (rule 1's structural shape): the
  `.deferred.md` sibling moved out of the worktree into the session
  scratchpad before spawning, so no reviewer sweep could reach it; one Fable
  reviewer subagent; mutation probes in scratch clones under the scratchpad;
  no git from the reviewer; `/security-review` forbidden (it reads the
  session's pending diff, which in a shared worktree is the other briefs).
- **Phase 1 committed before release** (`3ec982a`), then the sibling text
  carried verbatim in the release message with a scoped list of what could
  then be opened; reconcile appended beneath, never revising phase-1 text;
  sibling folded in and deleted in the closing commit.
- **`coldsweep.py` was the reviewer's sweep instrument** — its first use in
  a live pass, one day after it landed — and it did what it was built for
  with one exception the reviewer disclosed itself: a sweep run without the
  pass-specific `--also-exclude` flags printed three lines of a barred board
  item. The default bar (records + verdicts) held; the *per-pass* bar (the
  board items under review) is not the tool's default and depends on the
  reviewer passing it. That is a data point for the `SW` pass, and it is
  recorded here rather than relayed to that pass's brief-writer — which is
  this session — because the brief was already committed when it happened.

## What the pass found, in one paragraph

The three code commits do what they say for the geometry they name; every
claim that could be re-run reproduced in kind (selftest OK; Python suite
1,344; node 235; both floor planes green; pathscan 29 → 1 before/after;
the public child's index 49 pathscan / 16 wrapscan → 0 / 0, byte-identical
to its committed index). What did not hold is the generalisation around
them, and all four MODERATEs are the class the delta itself named — *a
string true from one place, asserted true from every place*: the index text
and so the enforced check's verdict now depend on where the generator ran
from (BG1, flip-flop across geometries); the child spelling names two of the
hook's three resolution branches, so a symlinked-tools child or a fresh
unconfigured clone gets `python3 /board.py` (BG2); "passes wrapscan in any
repo" is a property of the current data, not the renderer — a long state
line with an allow-marker renders to a flagged 187-column line (BG3), so the
withdrawn `070` policy question is not closed by the code; and the
corrections did not reach `tools/README.md`, `CHANGELOG.md` or the module
docstring, which still carry the superseded spelling and the withdrawn
residual (BG4). Minor: stale child guidance in `030`; `plainscan` ×13 on the
index (same class, next gate); a home-directory assertion that is
tautological where it matters and fails with `HOME=/`; a subdirectory
silent no-op. Notes: the pathscan survivor is a false positive, not "a real
stale path"; the 28-per-commit figure was a hand run; private-child naming
in the public tree (pre-existing); the brief's own barred paths were wrong
(`010-…`, not `115-…`/`160-…` — the reviewer barred the right ones).

## Three briefs, and what each holds closed

Each written from the diff of the delta paths and the pointer, with the
intent record, the ruling board items and (for the channel) the kept
transcript unopened; prior verdicts and seeded questions in the
`.deferred.md` sibling. Two disclosures stand in all three — the
`SESSIONS.md` tail was read at onramp before any brief was commissioned, and
each landing commit's message was read in full — and one more each where it
applied: the coldsweep brief-writer was *using* the tool under review at the
time; the channel brief-writer was contacted by the delta's author after the
brief was committed (one factual note over the peer channel, no instruction,
nothing changed — recorded in the brief's provenance because that trail is
the audit). The channel brief also names its evidence problem up front: the
section's primary source is a session transcript in the barred records tree,
so phase 1 reviews the doctrine as it stands and the transcript is released
for reconcile.

## The channel, used

A peer atelier session announced mid-run that two sessions had minted board
section `290` within the hour with no git conflict and a well-formed index
that the enforced gate passed; it moved its own to `300` by the fewest-inbound-
references tie-break the section prescribes and said so. This session
answered with its holdings, led with what it had not done, and offered one
corroborating count that the peer correctly rejected under law 1 — the refs
were committed and unpushed at the moment of writing, so they were not
evidence the other party could see. Then the peer disclosed that it was the
*author* of the channel delta whose brief this session had just written, and
this session appended the contact to that brief's provenance. Two rulings the
peer asked to have relayed are in the backlog below, tagged as already seen
by Mike in-session today.

## Handed to Mike

The ruling backlog was measured rather than estimated: **39 open `[ ]` items
carry `🎯`**, of which the closed review cycles awaiting a ruling round now
number eleven — BG1–BG12 (this session), AA6–AA13, RG1–RG9, LR1–LR9,
BS1–BS14 (one MAJOR), CMF1–CMF10 (one MAJOR), CS1–CS14, CM1–CM13, TD1–TD3,
CR1–CR6, AB1–AB6, LK1–LK6, FR1–FR6, AP2–AP8, plus the 2026-08-05 batch's
residue — walked one by one in plain language when he chooses to sit. Item
`150-…` says that sitting runs in a fresh session; this session presented the
menu and stopped, taking no ruling as read.

## The second sitting — Mike took the two open MAJORs (1045 UTC)

Asked where to start, he chose *"the two open MAJORs first"*, and ruled all
three asks put to him, each briefed in plain language with per-option
impacts before the popup:

- **BS1 → "Wording now + fund the staged-plane build."** Applied in this
  session on the four surfaces (docstring, catalogue, CONCURRENCY with the
  dirty-sibling-is-a-stop sentence, ADR by appended amendment); `010/020`
  funded with the rebuild-from-index flag folded in; BS cycle CLOSED on the
  wording; rule-4 `⏳` queued at `160-…/260`. Ruling recorded at
  `290-ruling-round-…/050`.
- **BG1/BG2 → "Apply as counselled."** Funded and left for a working session
  (`290-ruling-round-…/060`): decide the spelling from the repo, emit the
  hook's whole expression, test that both resolve identically. Not applied
  here — the session that orchestrated the pass is the wrong author for its
  fix.
- **CMF1 → verbatim:** *"Do a fable review to see if it can be usefully
  repurposed e.g. to gather data/stats on plain speak to find the root cause
  when its not plain. Otherwise we will destroy the hook per your
  recommendation."* Recorded with the context he was given and a `⏳` Fable
  design review queued (`290-ruling-round-…/070`) — REPURPOSE with a design,
  or DESTROY; the CMF cycle closes on the outcome either way. The review must
  check the `cctranscript` instruments before proposing a hook.

Not touched: BS2–BS14, BG3–BG14, CMF2–CMF10 and every other cluster in the
menu — the round runs one ask at a time and stopped where Mike stopped.
