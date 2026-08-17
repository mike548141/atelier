# Cold pass — the reply gate unwired, and the three premise corrections

**Pass type:** doctrine cold pass (REVIEW.md rule 4 — the correction to
`COMMUNICATION.md` was written by the session that diagnosed the failure and
executed the unwiring; the two "rules earned" it states are new doctrine by
function, in the author's own wording).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04).
**Status:** BRIEF WRITTEN, REVIEW NOT RUN. The next cold session that passes
rule 4's criterion and the tier bar takes it — see *Spawn provenance*.

## Spawn provenance

- **Author of the work under review:** the session that landed the delta on
  2026-08-15 (wt: `plain-reply-unwired-0816`; Opus tier per the commit
  trailer; see *What the work is*).
- **Who wrote this brief:** a cold session Mike opened on 2026-08-15 at about
  1120 UTC with the standing instruction, verbatim: *"As a cold session please
  do any review work, any work that is fable dependent, and write briefs for
  any reviews that need them. If you write the brief then do not run the
  review, that will require another cold review session."* That session
  authored no part of this delta and was neither started nor instructed by the
  authoring session. It wrote this brief from the delta (`git show cd6232b`
  for the four doctrine/tool surfaces below) and the queue pointer only; it
  did **not** open the session record or the board item the pointer names as
  intent records. **One disclosure:** its own session onramp read the tail of
  `docs/SESSIONS.md`, whose last index entry summarises this delta — that
  entry was read before this brief was written and is the reason the intent
  record itself was left unopened. The same session is orchestrating four
  *other* cold passes (the 2026-08-15-103x briefs, written by a different cold
  session) and **stopped** on this one — it did not run this review.
- **Who takes the review:** the next cold session that meets rule 4's single
  criterion — a session the author neither started nor instructed — on the
  Fable tier, checked at selection. The taker repeats its own provenance in
  the verdict: how it was spawned, and its non-involvement with the authoring
  session and with the brief-writing session.
- **Orchestration shape:** the deferred material sits in the sibling file
  `2026-08-15-1126-reply-gate-unwired-cold.deferred.md` (rule 1's split): the
  intent-record references, the prior-verdict references, and the
  brief-writer's seeded questions. Recommended: the taker runs the review
  under an orchestrator that holds the sibling's bytes and hands them to the
  reviewer only after its findings are durably written. A taker reviewing by
  hand opens the sibling as a deliberate second act after its findings are
  written, and says so in the verdict. Fold in and delete when the verdict
  lands.
- **Adjacent pass, not this one.** The 2026-08-15-1033 brief
  (`communication-floor-cold`) reviews the *earlier* deltas on the same
  surfaces — the enforcement clause as first written (2026-08-09) and the
  repo-plane rescope (2026-08-10). Its verdict, once landed, is a prior
  verdict for this pass and is barred until reconcile like any other. This
  pass reviews what came *after*: the unwiring and the corrections.

## What the work is

Landed 2026-08-15 on `main` as `cd6232b`, merged as `433dc1f`. Reviewed at
HEAD:

1. [`docs/method/COMMUNICATION.md`](../method/COMMUNICATION.md) § *Some of it
   is enforceable* — the enforcement clause now says the reply plane is
   unwired, states how it failed, and states a rule (*a machine-decidable rule
   can still have no machine-deliverable remedy*); the plane-scoping paragraph
   beneath it was retensed and given a survival clause for any future
   collector.
2. [`tools/README.md`](../../tools/README.md) § *`plainscan.py`* — the
   two-planes description and the install stanza's preamble, rewritten to
   describe the reply plane in the past tense with a stop notice and to keep
   the install form "for the record and not to be reinstated without a
   ruling".
3. [`tools/hooks/plain-reply.py`](../../tools/hooks/plain-reply.py) —
   docstring only: an *UNWIRED — DO NOT REINSTALL WITHOUT A RULING* banner and
   a *THE PREMISE THIS FILE WAS BUILT ON, AND WHY IT WAS FALSE* section; the
   *WHAT THIS IS* paragraph re-tensed. **No behaviour changed** — the code is
   as it was, wired to nothing.
4. `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/README.md`
   § *COMMUNICATION.md enforced* — the section preamble retensed and pointed
   at the new ruling item.
5. **The unwiring itself is machine-local** — a hook stanza removed from
   `~/.claude/settings.json` on the principal's machine. It is not in the
   tree. Its *shape* is documented in the tools catalogue and reviewable; the
   live state is verifiable only by reading that file on this machine, and the
   verdict should say whether it was.

The commit message states measurements — a 12-hour transcript window,
24 sessions active, 16 hit, 29 turns blocked, 6 twice, ~123,500 characters
reprinted, a give-up path that fired on 4 of 6 turns — and a mechanism claim:
that a `Stop` hook fires after Claude Code has already streamed the reply, so
a block appends rather than replaces. Both are the author's claims and are
in scope as such.

## Scope

Widest the work admits: the mechanism claim and whether it is established
rather than asserted (the commit says the *previous* premise was asserted in
three places and checked in none — the same test applies to its replacement);
the measurement's method as recorded, since the corpus is private and cannot
be re-run from the repo; whether the corrections say what the mechanism does
and nothing more; the two rules stated as earned and whether the evidence
earns them; what the doctrine now leaves standing (the repo plane, the
"scoped to its reader" ruling, the fail-open trade) and whether each survives
the failure on its own grounds or only by assertion; and what a future session
reading these three surfaces cold will believe and do. **Non-goals — one, and
it does not fence the risk:** the reviewer does not decide any finding.
Doctrine here is self-authored; findings are the principal's to rule on (rule
3), and the destroy-or-repurpose ruling is his and is *not* under review — the
account he will rule on is. Counsel may be recorded, labelled as such.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. Is "a `Stop` hook cannot un-print" true of Claude Code as shipped
   today, in every surface the hook ran on (terminal CLI, IDE extension,
   web/desktop app) — and did anyone check more than one? What does the
   claim rest on: documentation, a transcript, an experiment? Does the
   correction over-reach — is *any* rewrite-before-read control impossible,
   or only this one at this hook point? Was unwiring the only remedy the
   evidence supported, or the one the author reached first?
2. **Correctness & quality** — read all four surfaces at HEAD side by side
   with the diff: do they now agree with each other and with the hook's
   actual behaviour? Does anything in `COMMUNICATION.md`, `tools/README.md`,
   the hook, `tools/floor.py`, `tools/plainscan.py` or the tests still assume
   a live reply plane? Run the suites and the floor on both planes at HEAD;
   drive the hook by hand once to confirm the docstring's account of what it
   returns matches what it returns.
3. **Completeness / harvest** — every surface that named the reply plane as
   live: doctrine, catalogue, tests, CHANGELOG (does one exist for the
   wiring, the unwiring, either?), skills, templates, child-facing floor
   blocks, session-onramp text. What did the correction sweep miss? The
   commit says two rules were earned — do they belong where they were put,
   are they stated once, and does anything already in the doctrine say the
   same thing under another name?
4. **Security & privacy** — mandatory. The delta quotes measurements over
   the principal's private transcript corpus and names counts of sessions;
   atelier is PUBLIC — check that nothing in the four surfaces or the record
   surfaces joins a private repo's name to its posture or carries transcript
   content. The unwiring removed a hook that read every reply in every repo
   and kept a state file — say what, if anything, that state file still holds
   on this machine and whether the docstring tells a reader. If the lens has
   no surface beyond that, discharge it in one explicit line with grounds.
   The house security scanner reads pending diffs; this is a landed-delta
   review, so state the reach case that applied.

## Re-run obligation

Re-run, do not read: the mechanism claim itself — establish by experiment or
by cited documentation whether a `Stop` hook block replaces or appends, and
on which surface(s) you tested; the suites and the floor on both planes at
HEAD (house invocations live in [`.githooks/pre-commit`](../../.githooks/pre-commit)
and `.github/workflows/ci.yml` — lift them, do not guess); the hook driven
live with a clean and a rule-breaking payload; the live-install state
(`~/.claude/settings.json` — report presence or absence of the stanza, quote
nothing else); and the tree-wide search for surfaces still asserting a live
reply plane. The transcript measurement cannot be re-run from the repo — say
so, and review the *method* as recorded rather than treating the numbers as
verified.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`,
every prior verdict in `docs/reviews/` (including the 2026-08-15-1033
communication-floor verdict once it lands), the intent record for this delta,
and the board item `020-…/310-…` (the ruling item, which carries the author's
full account). The sibling `.deferred.md` holds those references and the
brief-writer's seeded questions; open it after your findings are committed.
Reconcile after, never anchor before. A taker whose own session onramp has
already read the `SESSIONS.md` tail discloses that in the verdict.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `RG`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then open the sibling; append a
reconcile section; fold the sibling in below it and delete the sibling;
finalise. Update the queue pointer
(`docs/roadmap/160-doctrine-review-owed/180-rule-4-review-queued-tier-fable-pass-type-doc.md`)
and rebuild the index in the same commit.

---

## Phase-1 verdict — 2026-08-17, finding prefix `RG`

### Provenance, repeated

- **Reviewer:** a **Fable** reviewer subagent (tier checked at selection),
  spawned 2026-08-17 by an atelier session Mike opened at 0710 UTC under his
  standing cold-session instruction, verbatim: *"do any review work and any
  work that is fable dependent … write briefs too if they are required."* The
  reviewer authored no part of `cd6232b` and was neither started nor
  instructed by the authoring session (wt: `plain-reply-unwired-0816`) or by
  the brief-writing session of 2026-08-15 ~1120 UTC.
- **Orchestration shape — a departure, stated plainly so it can be rejected on
  sight:** the orchestrator is **Opus, not Fable**, unlike the 2026-08-15
  precedent where both roles ran Fable. It holds the deferred sibling,
  releases it only after these findings are durably committed, commits the
  records, and forms no finding and writes no severity. Reviewer's one-line
  view: rule 4's tier bar governs who forms the findings, and every finding
  and severity here is Fable's alone, so the shape honours the bar in
  substance — accepting the departure is Mike's call, not ours.

### Barred-material exposure — disclosed

Three exposures, in increasing order of this reviewer's own fault:

1. **Auto-memory.** The machine's project memory (in this session's system
   context before the pass began) carries one-line summaries of this delta
   and of the 2026-08-15 cold-run results — the same class as the
   brief-writer's SESSIONS.md-tail disclosure.
2. **Surface 4 at HEAD.** The in-scope board section `020-…/README.md`
   § *COMMUNICATION.md enforced* carries, landed after `cd6232b`, a summary
   of the 2026-08-15-1033 verdict including CMF1–CMF6 headlines. Reading the
   surface the brief names exposes that much; unavoidable under the brief's
   own instruction to read the surfaces at HEAD.
3. **A defective grep — the house rule's exact failure mode.** The first
   tree-wide sweep excluded barred paths with a regex anchored on a `./`
   prefix grep does not emit, so its hits included barred lines: four
   `docs/SESSIONS.md` index entries (the wiring, the rescope, the unwiring,
   the 1123 cold-run), one matched line each from four `docs/sessions/`
   records, two `docs/ROADMAP-DONE.md` lines, and — worst — substantial
   excerpts of the 1033 communication-floor verdict: its FAIL line, CMF1–CMF7
   finding texts, parts of its re-run table and reconcile. The board item
   `310-…` stayed excluded throughout. The second sweep used git-pathspec
   excludes and leaked nothing.

**Contamination direction, honestly:** RG3, RG6 and RG7 below overlap
territory the 1033 verdict also covers. Each was established after exposure
from primary evidence this reviewer generated itself — code reads, live hook
drives, its own documentation query, its own CHANGELOG grep — but anchoring
cannot be ruled out; the reconcile should treat those three as corroborated
rather than independent. RG1, RG2, RG4, RG5, RG8 and RG9 have no counterpart
in anything seen.

### Re-runs executed

| Obligation | How | Result |
|---|---|---|
| Mechanism claim | official hooks documentation queried via a fresh claude-code-guide subagent (code.claude.com/docs/en/hooks.md); a live block-and-observe experiment is not possible from inside a reviewer subagent, said plainly | **Established by cited documentation.** A blocking Stop "prevents Claude from stopping, continues the conversation" — output is appended, nothing retracted; `last_assistant_message` is a documented Stop input ("the complete final assistant message text for the turn"). Per-surface display behaviour is undocumented; the doctrine scopes its claim to the terminal, matching the evidence — no over-reach |
| Suites at HEAD | `python3 -m unittest discover -s tools -p 'test_*.py'` ×3 · `node --test instruments/*.test.js` | exit 0 on all three runs (item 120's flake did not reproduce) · 235/235 pass |
| Floor, both planes | `python3 tools/floor.py --plane hook --root . --tools tools` · `--plane ci --root .` | both exit 0; hook plane green with 4 warn-only; ci plane 🟡 secretscan 22 advisory + degraded leakscan cover — the documented expected state |
| Hook driven live | 8 payloads piped to `/usr/bin/python3 tools/hooks/plain-reply.py`, `PLAIN_REPLY_STATE` isolated in the reviewer scratchpad | clean/short → silent exit 0 · rule-breaking → `decision: block` naming P1/P3 at the 45/60 chat limits · 3rd consecutive block → `additionalContext` give-up, counter popped · 4th → blocks again at count 1 · malformed stdin → exit 0 silent. Shapes match the docstring; semantics drift at RG6 |
| Live install state | `~/.claude/settings.json` read for shape only | `"hooks": {}` — **no Stop stanza; `plain-reply` appears nowhere in the file**. The unwiring is real on this machine. Nothing else read or reported |
| Tree sweep | two greps (`plain-reply`/`reply plane`, then `stop.hook`), barred paths excluded — correctly on the second attempt | one surviving live-plane assertion: `tools/plainscan.py` docstring → RG2 |
| Transcript measurement | cannot be re-run from the repo — the corpus is private; the method reviewed as recorded | counts copied consistently across all three corrected surfaces; one internal figure not derivable from the recorded counts → RG5 |

### The four lenses

1. **Approach & assumptions.** Load-bearing assumptions, named first: (a) a
   Stop-hook block appends rather than replaces — now established by cited
   documentation (re-runs table); (b) the give-up note is visible to the
   principal — still unestablished anywhere and surviving at HEAD (RG3);
   (c) the measurement's counters mean what the prose says — unverifiable,
   one internal tension (RG5). The correction does not over-reach: it says a
   `Stop` hook cannot un-print, not that every rewrite-before-read control is
   impossible, and it scopes the failure to this hook point. Only one surface
   class (terminal transcripts) was measured, and the doctrine's claim is
   phrased to the terminal — the generalisation matches the evidence. Remedy
   choice: the ruling itself keeps repurpose open, so the remedy space was
   not collapsed to the author's first reach.
2. **Correctness & quality.** The four surfaces agree with each other and
   with the hook's behaviour on the mechanism, the dates and the numbers —
   29 / 6 / ~123,500 / 45 / 60 / 30.6% are consistent everywhere they appear.
   Two residues: doctrine's "Detection was sound throughout" contradicts the
   delta's own trigger evidence (RG1), and the anti-deadlock docstring claims
   memory and turn-scoping the code does not implement (RG6). "No behaviour
   changed" verified: the `cd6232b` hunk on the hook is docstring-only.
   Suites, floor, drives: green, above.
3. **Completeness / harvest.** The commit says the premise "was asserted in
   three places"; there is a fourth. `tools/plainscan.py`'s module docstring
   still presents the reply plane live and load-bearing ("gating the replies
   the principal actually reads … The second plane is the point") — RG2.
   CHANGELOG carries neither the 2026-08-09 wiring nor the 2026-08-15
   unwiring (RG7). Of the two rules earned, the first lands once in
   `COMMUNICATION.md` with no duplicate under another name (GUARDS.md and
   PRINCIPLES.md checked); the second lands on **no live doctrine surface at
   all** (RG4). Tests, templates, skills and child-facing floor blocks:
   swept, clean. Board item `120-…` is stale against HEAD (RG9).
4. **Security & privacy** — discharged with grounds, not by silence. No
   surface in the delta names a private repo or joins one to a posture; the
   transcript figures are counts and no transcript content travels; the one
   verbatim Mike quote is his ruling on his own tool, captured per doctrine.
   The state file `~/.claude/.plain-reply-state.json` **remains on this
   machine**: 233 bytes, mtime 2026-08-15 11:30 UTC, three entries of
   session-key → {16-hex text-hash prefix, count, timestamp} — no reply text,
   coordination data only; the docstring names the path but the unwiring
   banner never tells a reader the residue exists (RG8). Reach case for the
   house security scanner: it reads the session's pending diff, and this is a
   landed-delta review with no pending diff, so it had no reach here — the
   surfaces were read directly instead.

### Findings

**RG1 · MODERATE** — the carried lesson keeps half its own evidence.
`COMMUNICATION.md` (HEAD ~L109–110) asserts "Detection was sound throughout;
the remedy was the part nobody checked", while the same delta's commit account
says the triggers "were near-misses and board item identifiers, not the
'genuinely unreadable output' the hook claims to catch" and that the rewrite
"introduces findings the first scan never saw, so the gate fires on its own
output". By the author's own evidence, detection failed too — on calibration,
not on rule evaluation — and the doctrine sentence erases that half. Why it
matters: this sentence is the direct input to the open destroy-or-repurpose
ruling; a silent collector built on "detection was sound" inherits a detector
the measurement says fired mostly on near-misses. Counsel, labelled: keep the
machine-deliverable-remedy rule; let the clause state both failures.

**RG2 · MODERATE** — a fourth surface still asserts a live reply plane.
`tools/plainscan.py` docstring, § *ONE ENGINE, TWO PLANES* (~L77–89): "reply —
a Stop hook reading `last_assistant_message`, **gating** the replies the
principal actually reads", and "The second plane **is** the point." The
commit's "asserted in three places and checked in none" is itself an unswept
count. A cold reader of the engine — the file the 2026-08-10 ruling made
load-bearing — is told the gate is live and central. Counsel: retense the
section and point it at the hook's stop notice.

**RG3 · MODERATE** — the give-up path's visibility claim survives at HEAD on
exactly the unchecked-mechanism class this delta indicts. Hook docstring
L64–67 ("findings appended as a **visible note** … The principal **sees** the
mess AND sees that the wall fired") and `tools/README.md` L859–862 ("saying so
**visibly** in the transcript … the one part of the design the evidence
vindicated"). The note is emitted as `hookSpecificOutput.additionalContext`,
whose effect for a Stop hook is undocumented (this pass's own documentation
re-run: the documented Stop output fields are hookEventName / decision /
blockReason; `additionalContext`'s function is unspecified), and no check of
its visibility is recorded anywhere in the delta. "Fired on 4 of the 6" is
measurable from transcripts; "the principal saw it" is not established.
Overlaps barred territory — re-derived; see the disclosure. Counsel: correct
both passages now; if the file is ever repurposed, verify the visible channel
before claiming one.

**RG4 · MODERATE** — the second earned rule has no live home. "An approval is
not the whole ruling" exists in the commit message (and, per the brief, in the
barred records), but a tree-wide grep outside barred paths returns nothing:
no method doc states it, and none states an approval-capture rule under
another name. A rule the delta headlines as *earned* is invisible to every
future session that reads doctrine rather than history — the exact gap the
rule itself describes. Counsel: state it once where ruling-capture doctrine
lives.

**RG5 · minor** — one figure in the measurement's method does not cohere as
recorded: "the second attempt succeeded roughly a third of the time" cannot
be derived from "29 turns blocked, 6 of them twice" under either reading of
those counts (both give roughly 74–79% second-attempt success). The corpus is
private, so the numbers cannot be checked — only the method can be, and the
method as recorded leaves this figure unaccounted. Commit account only; it
does not appear on the corrected surfaces. Counsel: record what "succeeded"
counted, or drop the fraction from any future account.

**RG6 · minor** — the anti-deadlock section describes a mechanism the code
does not implement. "The hook remembers, per session, the last text it
blocked": `sig` is computed and stored (L199, L220) and never read back.
"After MAX_BLOCKS attempts on one turn": the state has no turn identity, so
the counter spans consecutive blocked replies across turns until a clean
reply resets it — verified by drive (an identical fourth payload after
give-up blocks again at count 1). Docstring-only in unwired code, but the
banner directs distrust at the premise section specifically, not at this one.

**RG7 · minor** — CHANGELOG records neither event. The 2026-08-09 wiring of a
machine-wide blocking gate and its 2026-08-15 unwiring are both absent; the
file is otherwise current (2026-08-17 entries) and its last COMMUNICATION
entry is 2026-07-12. A changelog reader cannot learn the reply gate ever
existed, let alone that it failed.

**RG8 · note** — machine residue the docs do not mention.
`~/.claude/.plain-reply-state.json` survives the unwiring: 233 bytes, three
entries of session-key → hash-prefix/count/timestamp, no reply text. The
docstring names the path; the unwiring banner does not mention the residue.
Counsel: delete it with a destroy ruling, or note it beside the install form.

**RG9 · note** — board item `120-…/010` (StopHook suite flake, 🔥, "verify
against HEAD before acting") did not reproduce: three full-suite runs at
HEAD, all exit 0, and the per-test `PLAIN_REPLY_STATE` isolation the item's
hypothesis pointed toward is present at HEAD with the flake history recorded
in the fixture docstring. A candidate for closure by a session that owns it;
not this pass's to close.

### Overall

**PASS-WITH-FINDINGS — 0 MAJOR / 4 MODERATE / 3 minor / 2 note.** The
unwiring is verified real on this machine, the mechanism claim the correction
rests on is established by cited documentation, the three corrected surfaces
are mutually consistent, and the suites and both floor planes are green at
HEAD. What remains is doctrine keeping half its own evidence (RG1), a fourth
uncorrected assertion of the old premise's frame (RG2), one surviving
unchecked mechanism claim of the same class the delta indicts (RG3), and an
earned rule with no home (RG4). All findings are Mike's to rule (rule 3);
counsel above is labelled as such.

### Follow-up checklist

- [ ] RG1 — restate the COMMUNICATION.md lesson to carry both failures
- [ ] RG2 — retense `tools/plainscan.py` § *ONE ENGINE, TWO PLANES*
- [ ] RG3 — correct the give-up visibility wording in the hook docstring and
      `tools/README.md`
- [ ] RG4 — give "an approval is not the whole ruling" a live doctrine home
- [ ] RG5 — ground or drop the "roughly a third" figure in future accounts
- [ ] RG6 — fix or delete the anti-deadlock description with the
      destroy-or-repurpose ruling
- [ ] RG7 — CHANGELOG entries for the wiring and the unwiring
- [ ] RG8 — remove the state file with the ruling, or note the residue
- [ ] RG9 — verify and close board item `120-…` (its owner's call)
- [ ] Pending at verdict time: a documentation follow-up (`stop_hook_active`;
      `systemMessage` vs `additionalContext` visibility) had not returned.
      RG3 and RG6 stand without it and could only be strengthened by it.
