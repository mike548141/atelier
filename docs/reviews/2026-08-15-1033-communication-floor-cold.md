# Cold pass — the communication floor (COMMUNICATION.md's enforcement clause, plainscan, the reply gate, and the repo-plane rescope)

**Pass type:** combined doctrine + code cold pass (REVIEW.md rule 4 — the
enforcement clause was rewritten by the session that built the mechanism it
now points at; the rescope's doctrine and code came from one session too).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04).
**Status:** BRIEF WRITTEN, REVIEW NOT RUN. The next cold session that passes
rule 4's criterion and the tier bar takes it — see *Spawn provenance*.

**Two queue pointers, one brief.** The board carries two rule-4 pointers on
this surface: the COMMUNICATION.md enforcement-clause rewrite (landed
2026-08-09) and the plainscan repo-plane rescope (landed 2026-08-10). Both
name the same doctrine section as their delta and the second builds on the
first's mechanism, so one reviewer reads the surface once. Both pointers are
closed by this pass's verdict.

## Spawn provenance

- **Author of the work under review:** the session that landed the first
  delta on 2026-08-09 and the session that landed the second on 2026-08-10
  (wt: `plainscan-rescope-0810`); see *What the work is*.
- **Who wrote this brief:** a cold session Mike opened on 2026-08-15 with
  the standing instruction, verbatim: *"As a cold session please do any review
  work, any work that is fable dependent, and write briefs for any reviews
  that need them. If you write the brief then do not run the review, that
  will require another cold review session."* That session authored no part
  of either delta, was neither started nor instructed by either authoring
  session, wrote this brief from the deltas and the queue pointers only (it
  did not open the intent records), and **stopped** — it did not run the
  review.
- **Who takes the review:** the next cold session that meets rule 4's single
  criterion — a session the author neither started nor instructed — on the
  Fable tier, checked at selection. The taker repeats its own provenance in
  the verdict: how it was spawned, and its non-involvement with the two
  authoring sessions and the brief-writing session.
- **Orchestration shape:** the deferred material sits in the sibling file
  `2026-08-15-1033-communication-floor-cold.deferred.md` (rule 1's split):
  the intent-record references, the prior-verdict references, and the
  brief-writer's seeded questions. Recommended: the taker runs the review
  under an orchestrator that holds the sibling's bytes and hands them to the
  reviewer only after its findings are durably written. A taker reviewing by
  hand opens the sibling as a deliberate second act after its findings are
  written, and says so in the verdict. Fold in and delete when the verdict
  lands.
- **A note on hashes.** The first pointer names `753adb6` and `e61adc4`;
  those commits were rebased before landing and sit on `main` as `c374959`
  and `beaf240`. The pointer's refs are the pre-rebase objects. Recorded here
  so the taker does not chase a dangling hash.

## What the work is

Landed on `main` as `c374959` (the floor under COMMUNICATION.md, 2026-08-09),
`beaf240` (recitation cap), `b879b02` (P5 built and rejected; the hook's
state-file fix), `171862b` (the reply gate switched on — records and the
tools catalogue), and `e390382` (the repo-plane rescope, 2026-08-10, ruled).
Reviewed at HEAD:

1. [`docs/method/COMMUNICATION.md`](../method/COMMUNICATION.md) § *The
   meta-rules that make it work* — the enforcement clause as rewritten twice:
   the 2026-08-09 correction of the "write-time discipline is the only
   control" claim, and the 2026-08-10 *each plane is scoped to its reader*
   paragraph.
2. [`tools/plainscan.py`](../../tools/plainscan.py) — the engine: rules
   P1–P4 with their stated grounds, the two planes, `RECORDS_GLOBS` and
   `--include-records`, the recitation cap. [`tools/test_plainscan.py`](../../tools/test_plainscan.py)
   — 47 → 51 tests across the deltas.
3. [`tools/hooks/plain-reply.py`](../../tools/hooks/plain-reply.py) — the
   `Stop` hook that lints the agent's own reply and blocks it for rewrite;
   fails open by stated design; the anti-deadlock guard and its state file.
   Its installation is machine-local (`~/.claude/settings.json`) and outside
   the repo — the *shape* of the installation is documented in the tools
   catalogue and is reviewable; the live setting is not in the tree.
4. [`tools/floor.py`](../../tools/floor.py) — the `plainscan` registry entry
   (warn-first via flag, both planes) and the rescope's wiring.
5. [`tools/README.md`](../../tools/README.md) — the plainscan and hook rows.
6. `CHANGELOG.md` — no entry mentions plainscan, the hook, or the
   communication floor at HEAD (grep at brief-writing: zero matches). Stated
   as a fact about the delta's surfaces, for the reviewer to weigh.

The board records that the reply-plane numbers (45 words / 60 characters) were
the principal's ruling and that the repo-plane numbers remain unruled; that
P5 was built, measured and deleted the same day; and that a test in this
module's Stop-hook suite is flaky under the full-suite run. All three are
in-scope facts about the delta, stated here as facts, not as findings.

## Scope

Widest the work admits: the measurement the correction rests on and whether
the doctrine now says what the mechanism does; the four rules and the grounds
each claims; the two-plane design and the fail-open choice; the hook's
behaviour live; the rescope's exclusion list and its ruling; the tests; and
the doctrine as it will bind every repo where the hook is installed. **Non-goals
— one, and it does not fence the risk:** the reviewer does not decide any
finding. Doctrine here is self-authored; findings are the principal's to rule
on (rule 3). Counsel may be recorded, labelled as such. The reply-plane
numbers are ruled and are not re-litigated; whether the mechanism honours the
ruling is in scope.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. Is a Stop hook that blocks the reply the right control for the
   trust failure it answers? Is "records are written for the next agent, not
   the principal" true of the three excluded paths — and only of them? Is
   fail-open the right posture for a gate on the principal's own reading
   surface?
2. **Correctness & quality** — run the suites; run `plainscan` on both
   planes; drive the hook by hand with a clean payload, a rule-breaking one,
   a malformed one, and a repeated session id (the anti-deadlock path); check
   what `RECORDS_GLOBS` actually matches against what the doctrine says it
   excludes. Reproduce the flake if it reproduces.
3. **Completeness / harvest** — the doctrine says four things are checkable
   and names what stays judgement; test the boundary in both directions. Do
   the rules' stated grounds hold (a published standard, dated house
   doctrine, a house call)? What does the correction leave in the person-level
   layer that the doctrine still says is unreachable?
4. **Security & privacy** — mandatory. The hook reads every reply the agent
   writes in every repo and keeps a state file; the engine's output recites
   the offending text. Where does recited text go on each plane, what does
   the state file hold, and does anything cross from a private repo's reply
   into a public tree's record? atelier is PUBLIC — verify nothing in the
   delta or your verdict joins a private repo's name to its posture. The
   house security scanner reads pending diffs; this is a landed-delta
   review, so state the reach case that applied.

## Re-run obligation

Re-run, do not read: the full suites (house invocations live in
[`.githooks/pre-commit`](../../.githooks/pre-commit) — lift them, do not
guess); the test-count claims at the landing commits; the advisory tally the
rescope claims (7,817 → 4,440 on this repo — measure at the landing tree and
at HEAD, and say which you measured); the hook driven live through its stated
paths; and the floor on both planes at HEAD. The 6,704-reply measurement
behind the correction reads a private transcript corpus and cannot be re-run
from the repo — say so, and review the *method* as recorded rather than
treating the number as verified.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`,
every prior verdict in `docs/reviews/`, and the intent records for both
deltas. The sibling `.deferred.md` holds those references and the
brief-writer's seeded questions; open it after your findings are committed.
Reconcile after, never anchor before. A taker whose own session onramp has
already read the `SESSIONS.md` tail discloses that in the verdict.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `CF`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then open the sibling; append a
reconcile section; fold the sibling in below it and delete the sibling;
finalise. Update both queue pointers
(`docs/roadmap/020-policy-as-code-programme-five-tracks-mik/300-generalise-the-finding-don-t-just-fix-this-doc.md`
and the rescope pointer inside
`docs/roadmap/020-policy-as-code-programme-five-tracks-mik/README.md`) and
rebuild the index in the same commit.
