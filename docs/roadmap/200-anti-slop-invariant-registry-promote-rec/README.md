# Anti-slop invariant registry — promote recurring review findings to always-on checks (Mike, 2026-07-21)

### 🎯 Index-integrity mechanism, estate-wide (Mike ruled 2026-08-09)


### 🎯 Queued from ros (Mike ruled 2026-08-03): mint "a test cannot falsify its own code's assumption" as method/ doctrine


### Mine the estate's own history for repeat offences (Mike, 2026-07-25)

**The ask, in Mike's words:** *"exactly this is what we need to be scanning all
the repo's and transcripts to find."*

**What prompted it.** A rule broke three times — private repo name joined to its
security posture in a public record (2026-07-11, 2026-07-12, 2026-07-25), every
time at the identical moment: summarising fleet-wide scan state into an atelier
record. Each time it was caught by luck: Mike's unease, a post-session
self-review, an unrelated question. Nobody was looking for the *pattern*, only
for the instance in front of them. Three occurrences of one failure is not bad
discipline — it is a missing check with a very loud signal nobody was reading.

**The principle this rests on.** A rule that keeps breaking needs *mechanising,
not restating*. Recurrence — not severity — is the trigger for promotion to an
always-on check: a severe-but-once failure is a judgement call, while a
trivial-but-thrice failure is a defect in the system that keeps producing it.
Pairs with the existing rule that a rule breaking repeatedly should first be
checked for bad *framing* before being restated louder.

**The work.** A retrospective evidence pass over what the estate already
records, to surface every rule that has broken more than once:

- **Sources**, richest first: session records and their honest-notes sections ·
  review briefs and their findings (already graded, already deduped by cycle) ·
  git commit messages, especially corrective vocabulary — "fix", "correct",
  "missed", "should have", "caught only because", "again", "third time" ·
  `ROADMAP-DONE` entries describing what went wrong · the transcripts themselves
  via `ccarchive`/`cctranscript`, which reach across every repo and are the only
  source carrying what an agent *thought* rather than what it committed.
- **Signal to extract**: the same corrective appearing N times, especially
  across different repos or different sessions — cross-repo recurrence is much
  stronger evidence of a systemic hole than one repo's habit.
- **Output**: ranked candidates for this registry, each with its occurrence
  count, the dates, and the moment-of-failure that produced it. The
  moment-of-failure matters more than the rule text: all three occurrences of
  the join defect shared one trigger, and a check aimed at that trigger would
  have caught all three.
- **Honest limits to state up front**: commit messages describe what an author
  *noticed*, so this finds self-caught failures and misses silent ones entirely;
  transcript volume makes exhaustive reading impractical, so sampling strategy
  is part of the design, not an afterthought; and a failure that was never
  written down anywhere is invisible to every source listed above.

**Why it is worth real budget.** Every candidate it surfaces is a defect class
already proven to recur in *this* estate, with its evidence attached — which is
exactly the grounding this repo's doctrine demands and the thing that is
normally hardest to get. It is the up-flow (child → parent) of cross-repo
learning applied to failures rather than techniques.

**First known candidate**, carried from 2026-07-25: the private-repo × posture
join (see the enforcement-propagation section for the sketch and its
false-positive caveat).

### The ladder landed; two pieces of work fall out of it (Mike, 2026-07-29)

**The ask, in Mike's words:** *"As sessions are still running into the issue
when it is written down 3 times. How do we make it structural, mechanical, or
policy as code to stop the same issue recurring that the doctrine already warns
the sessions about"* — and, separately, *"I don't think we should be repeating
the same point in 3 different places i.e. our DRY principle."*

Both are answered in doctrine now — `method/PROPAGATION.md` gained *When a rule
keeps breaking — climb, never restate* (three rungs: framing → mechanise at the
moment of failure → **remove the situation**) and *One statement, stamped copies
— never three originals*. The third rung is the new one, and it is what this
session actually did to the review deferral: not a better label, but moving the
bytes so the failure has nowhere to happen. What the doctrine cannot do by
itself is the two things below.



Source: <https://thenewstack.io/engineering-ai-slop-registry/> (Aviator). A
mechanism for AI+human engineering that fits atelier's "mechanism before more
content" ethos. The idea: an **invariant catalogue** — codified, always-checked
rules capturing the conventions/constraints that live in senior engineers'
heads (convention blindness, deprecated APIs, module boundaries, security
baselines) and that a model has no per-codebase training for. They call it the
"anti-AI-slop registry".

**What's genuinely NEW for atelier** (much is already ours — see below): the
systematic REGISTRY and its promotion rule.
Mining done 2026-07-22 (330 findings / 47 reviews → 5 scanner + 7 verifier
candidates; record:
[`sessions/2026-07-22-1036-invariant-candidates.md`](../../sessions/2026-07-22-1036-invariant-candidates.md))
→ [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md).

- **S1–S5 / V1–V7 ALL APPROVED 2026-07-23** (Mike, plain-language
  walk-through of the mining record's candidates; the PROPOSED-then-ratify
  pattern; S5 approved explicitly on ROI over its borderline finding
  count). Approved seams/homes are the record's proposals unamended: all
  twelve shared-floor. The promotion rule itself (>2 occurrences ⇒
  candidate) is thereby exercised end-to-end and stands as practice.
**All five approved scanners S1–S5 are BUILT + wired advisory** (S1/S3/S5
earlier; S2 `pathscan` `b738f21` + S4 `stampscan` `2fe97f3` this run — detail →
[`ROADMAP-DONE.md`](../../ROADMAP-DONE.md)). **S1/S3/S5 first-of-kind reviews are DONE**
(S3 at 0618; S1 + S5 at 0707 — verdicts + follow-ons below). **S2 + S4 reviews
are the open first-of-kind work (⏳ below).**
- 🎯 REVIEWED 2026-07-26 (rule-4 Fable cold pass): PASS-WITH-FINDINGS 3M/5m
  — [verdict](../../reviews/2026-07-26-2215-pathscan-s2-cold.md); PS1–PS8 await
  Mike's ruling (rule 3). Recommendation: keep advisory, five preconditions
  to flip (gate doctrine surface only; fourth anchor + root `*.md`; burn down
  the gated residual incl. the one live TP at `docs/build/README.md:28`; flip
  via the floor registry, not ci.yml; fix the docstring overclaim).
  **pathscan (S2) first-of-kind review** — advisory `b738f21` (queue run
  0959), rule-4 non-author reviewer needed (this run built it). *Delta:*
  `tools/pathscan.py` + `test_pathscan.py`, wired `--warn` in `ci.yml`.
  *Intent record:* `sessions/2026-07-22-1036-invariant-candidates.md` § S2.
  The build's own open questions for the reviewer (from its report): is the
  triple-anchor resolution (root / own-dir / outermost-`docs`-ancestor)
  defensible or too atelier-specific; should README-without-`.md` (38 of 174
  findings, the largest class) get an `.md`-append retry or stay a residual;
  the extension-suffix-only heuristic leg is the noisiest half — tighten before
  gating? Baseline 174 on `docs/` is heuristic noise by design; gate-readiness +
  scope (à la WS1) are the review's call.
  **⚠️ An Opus pass ran on 2026-07-26 0647 UTC and was NOT ACCEPTED** — reviews
  run on the wrong tier (Mike, 2026-07-26): cold review passes are Fable's.
  The item is re-queued unchanged and still awaits its first accepted review.
  The withdrawn pass is preserved as history under `docs/reviews/withdrawn/`
  and is **not reading for the redo** — open it only after your own verdict
  is written and committed.
- 🎯 REVIEWED 2026-07-26 (rule-4 Fable cold pass): PASS-WITH-FINDINGS 3M/3m/1n
  — [verdict](../../reviews/2026-07-26-2215-stampscan-s4-cold.md); ST1–ST7 await
  Mike's ruling (rule 3). Recommendation: do NOT wire yet, not even advisory —
  a config error survives `--warn` and the live tree exits 2 today (the
  quarantined withdrawn file + the new brief trip the parser); staged
  preconditions in the verdict.
  **stampscan (S4) first-of-kind review** — built + merged `2fe97f3` (queue
  run 0959), **BUILT BUT NOT WIRED** (see the wiring blocker below), rule-4
  non-author reviewer needed (this run built it). *Delta:* `tools/stampscan.py`
  + `test_stampscan.py`, marker convention added to `PROPAGATION.md` +
  `templates/CLAUDE.md` (invisible HTML comments); 46 tests, live pair CLEAN
  (byte-identical). *Intent record:*
  `sessions/2026-07-22-1036-invariant-candidates.md` § S4. Reviewer must
  scrutinise: **(0) THE WIRING BLOCKER (load-bearing, found in-run):** the
  marker parser recognises stamp markers anywhere it scans — including prose and
  code spans that only *document* the syntax — and treats a stray/unpaired
  marker as a hard config error (exit 2) that `--warn` does NOT suppress. So
  even advisory wiring lets ordinary docs about stampscan block the floor (a
  ROADMAP pointer describing the markers reddened the floor mid-run; the
  stampscan CI step was reverted, so it is unwired). **Precondition to wire:
  strip fenced/inline code before marker-hunting, as every sibling scanner
  does.** (1) the **marker convention borders on a doctrine act** —
  `narrow=<reason>` declares a legitimate narrowing vs a silent drop (mechanically
  identical subsequences), needs explicit ratification; (2) the stamp-end marker
  appended inline to the `---` divider (rather than its own line) — a placement
  compromise forced by a collision with the pre-existing `test_templates.py`
  slice logic (a cleaner fix teaches `template_block()` to strip markers);
  (3) fence-stripping + duplicate-line subsequence matching are first-of-kind
  residuals unexercised beyond fixtures. Other inlined-floor candidates
  (`method-layer P1`, `foundation Q2`, `CF4`/`IR2`/`SL1`/`HI-F4`) are NOT wired —
  their canonical source+region weren't confidently identifiable without guessing.
  **⚠️ An Opus pass ran on 2026-07-26 0647 UTC and was NOT ACCEPTED** — reviews
  run on the wrong tier (Mike, 2026-07-26): cold review passes are Fable's.
  The item is re-queued unchanged and still awaits its first accepted review.
  The withdrawn pass is preserved as history under `docs/reviews/withdrawn/`
  and is **not reading for the redo** — open it only after your own verdict
  is written and committed.
*datescan (S3) review is DONE (2026-07-23) — verdict PASS-WITH-FINDINGS
(0 MAJOR / 4 minor / 3 Low / 1 nit), NOT gate-ready (~75% baseline noise); brief
[`docs/reviews/2026-07-23-0618-datescan-s3-cold.md`](../../reviews/2026-07-23-0618-datescan-s3-cold.md),
detail → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md). Its follow-ons: the DSR-apply is
now DONE (above); the flip precondition is met (above). S1/S5 follow-ons below:*

*datescan DSR1–DSR8 apply + re-baseline DONE 2026-07-23 (queue run 0707, Sonnet
`b7b292c`) — baseline 60→0, detail → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md). The
flip follow-on stays open:*

*datescan advisory→blocking flip — **RULED + DONE 2026-07-23 (Mike: "agree flip
it")**. atelier `ci.yml` datescan dropped `--warn` (blocks clean, 0 breaches);
child `floor.yml` template gained a docs-scoped datescan blocking step + its
selftest, so children adopt at their next pin bump (re-baseline first — see the
fleet-floor item below). Honest limit recorded in-gate: DSR3 narrowed `today`, so
a bare "today = this date" claim with no cue passes silently — tighter but not
exhaustive. → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) at next harvest.*
*wrapscan (S1) first-of-kind review DONE 2026-07-23 (queue run 0707, cold Opus) —
**PASS-WITH-FINDINGS 1M/3m/2L**, NOT gate-ready; MAJOR is gate-scope not
detection (154/287 baseline is deliberate SESSIONS index rows). Brief
[`docs/reviews/2026-07-23-0707-wrapscan-s1-cold.md`](../../reviews/2026-07-23-0707-wrapscan-s1-cold.md),
detail → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md). Two follow-ons stay open:*

*wrapscan (S1) review APPLIED + **FLIPPED TO BLOCKING** 2026-07-23 (queue run
0959, apply `ceb3fda`, flip on Mike's ruling) — option-A doctrine-surface scope,
WS1–WS6, gated scope 0 findings; atelier `ci.yml` dropped `--warn`, child
`floor.yml` gained a blocking wrapscan step (child re-baselines its record stores
first). An over-wide doctrine-prose line now fails the build. →
[`ROADMAP-DONE.md`](../../ROADMAP-DONE.md).*
*spellscan (S5) first-of-kind review DONE 2026-07-23 (queue run 0707, cold Opus) —
**PASS-WITH-FINDINGS 0M/2m/1L/1n**, NOT gate-ready; core safety proven (no wrong
corrections), real latent bug SS1 found, license/practice exclusion ruled
permanent. Brief
[`docs/reviews/2026-07-23-0707-spellscan-s5-cold.md`](../../reviews/2026-07-23-0707-spellscan-s5-cold.md),
detail → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md). Follow-ons stay open:*

*spellscan (S5) review APPLIED + **FLIPPED TO BLOCKING** 2026-07-23 (queue run
0959, apply `b910962`/`4872f07`, flip on Mike's ruling) — SS1–SS4 + `catalogue`
rename. **Frozen-record `artifact` question RULED 2026-07-23 (Mike: keep history
verbatim)**: the ~36 general-sense `artifact` breaches in the frozen record
stores (`SESSIONS.md`, `ROADMAP-DONE.md`, `docs/reviews/*`, `docs/sessions/*`)
are NOT retro-spelled — history stays as-written — so the gate is scoped to the
LIVE doctrine surface (`method/`/`build/`/`decisions/`) and a `.spellscanignore`
nets the record stores. Re-baseline resolved the 2 genuine doctrine-surface
findings (ADR 0007 "Artifact signing" = supply-chain term-of-art, allow-marked;
one general-sense `artifact`→`artefact` fixed in a decision record). atelier
`ci.yml` dropped `--warn`; child `floor.yml` gained a blocking spellscan step
(child re-baselines first). license/practice exclusion PERMANENT (`practice`
×178 correct NZ noun). → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md). (Adjacent, noted
not acted: two `artifact→artefact` rename-notation *mentions* — a MENTION not a
USE — a possible future heuristic extension.)*
- **The floor-local-seam cycle — CLOSED, no ruling owed.** Its verdict pointer
  was harvested 2026-08-09 → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) § *The
  floor-local-seam cycle's verdict pointer, retired*. LS1–LS5 were ruled and
  applied 2026-07-27 as Track A's A4 and re-verified against live code at HEAD
  before the close; the `🎯` it carried until that harvest was residue, and it
  had been inflating the count of rulings Mike was said to owe.

**What atelier ALREADY has (this EXTENDS, doesn't invent):**
- The **floor scanners** (leakscan/secretscan/signscan/sizescan) ARE always-on
  invariants — machine-checked, fleet-wide, never re-argued. This idea
  generalises them to project-specific, review-derived rules.
- **Writer ≠ verifier independence** — REVIEW.md rule 4 (different context,
  different blind spots, structured findings on the durable record) is exactly
  the article's "the writing agent and verifying agent are different… a
  structured report per criterion, not a gut-check from the same model".
  Corroboration of standing doctrine, not a new claim.
- **Move human judgment UPSTREAM / review before build** — "humans review
  specs, plans, constraints, acceptance criteria, not 500-line diffs" is our
  review-is-an-input-not-a-gate line (ros CLAUDE.md + REVIEW.md). Corroborated
  by their intent-driven experiment (spec reviewed first → agent builds 6k LOC
  → second agent verifies 65 criteria in 6 min: 60 pass / 4 fail / 1 partial).

Framing worth keeping: *"You're not building software anymore. You're building
the machine that builds software, and quality control is part of that machine."*
*review: WARRANTED when this moves from capture to doctrine/mechanism (it
touches REVIEW.md + EVIDENCE.md + the scanner floor); brief owed at pickup.*
