# atelier ROADMAP

Lean by design: **what's open**, prioritised, read every session. Completed
detail lives in [`ROADMAP-DONE.md`](ROADMAP-DONE.md) — the current-truth/history
split (`method/RECORD.md`); `tools/sizescan.py` is the signal that keeps this
file honest. Sequencing rule from the 2026-07-10 review: **mechanism before more
content** — a repo that inherits docs but not the propagation + review cadence
has inherited the costume, not the doctrine.

Checkbox states — a **work-owed tri-state**, never a disposition (Mike,
2026-07-22): `[ ]` work still owed · `[x]` **no more work owed** — delivered,
superseded, or declined, with the disposition said in the item's own text (a
dated note), never a fourth bracket · `[~]` **claimed** by a live parallel
session — `(claimed <date>-<HHMM>, wt: <branch>)`, optionally extended in place
with a resume breadcrumb (`· at: <step>` — CONCURRENCY § Surviving an
interrupted session) — don't start a `[~]` item;
take the next open one (`method/CONCURRENCY.md` § Claiming work) ·
`⏳` **review queued** for a non-author to take — any spawner passing rule 4's
criterion may take it; the taker writes the brief (`method/REVIEW.md` rule 4).
**The pointer is refs only** — name the delta and the intent record, no
evaluative account; the account lives in the session record, so a taker meets
the work cold (REVIEW.md rule 4's ceiling, stated here at the point of use).
And the delta list stays *complete*: a later commit that touches a queued
delta's doctrine surfaces — even for hygiene — widens the pointer's delta
list in the same commit (AW6 ruling, 2026-07-23). The pointer itself is
queued **in the commit that lands the work** — landing = queuing, so no
window exists where landed doctrine sits unpointed and untracked (AWA2
ruling, 2026-07-23; its enacting batch exercised exactly that window).

## Doctrine — review-owed

Completed review cycles (Claiming-work, REACH ×3, the independence batch,
COMMUNICATION, RECORD keep-generic, signing doctrine, PRINCIPLES §8, the plugin
bundle, CONCURRENCY put-away, CLI-docs standard, ADR 0006/ccarchive addendum,
CONVENTIONS + UTC-at-rest, lean-files/sizescan, the review-trigger/sizescan
combined cycle — 0407 → F1–F9 applied → 0544 → G1–G3 applied → 0629 terminal
no-MAJOR pass, closed 2026-07-19; the 2026-07-20 triple cycle — DOCUMENTATION
doctrine + CONCURRENCY posture flip + session-onramp operating-rhythm, three
rule-4 cold passes all PASS no-MAJOR, applied `87af9f9`; the review-line
artefact cycle — rule-4 cold pass PASS 0M/1M/5L, Mike's accept-all applied
terminal, closed 2026-07-21; the REVIEW.md scope/lens-4 cycle — 2158 cold
pass 2M/3M/2L → SL1–SL7 accept-all applied `d553045` → 0244 terminal
no-MAJOR application pass, closed 2026-07-22; the harvest-integrity cycle —
0819 pass 1M/3M/2n → HI-F1–F6 accept-all applied `30d350c` → 0943 terminal
no-MAJOR application pass, closed 2026-07-22; the secrets/access cycle —
1021 rule-4 cold pass taken by the 1018 queue run, PASS-WITH-FINDINGS
0M/4m/4L/1n terminal; SA1–SA9 ruled accept-all and applied `f8350ee`
2026-07-23, cycle closed; the economics cycle — 0222 rule-4 cold pass
0M/4m/3L/1n, EB1–EB8 ruled accept-all, terminal application `86f8530`
2026-07-23; the queue-run cycle — 1149 pass → QR1–QR9 applied `b65209c` →
0222 rule-4 application pass 0M/1m/3L/2n, QA1–QA6 applied `5891184`
terminal 2026-07-23; the v2-plugin cycle — 1215 pass → VP1–VP8 applied
`ff8a07f` → 0222 rule-4 application pass 0M/2m/1L/1n, VA1–VA4 applied
`bbaec81` terminal 2026-07-23; the apex-widening cycle — 0222 pass 1M/4m/3L/1n
→ AW1–AW9 applied `e8d707c` → 0330 rule-4 application pass 0M/2m/1L/1n,
AWA1–AWA4 accept-all applied terminal 2026-07-23; the security-canon cycle —
0222 pass 1M/1m/3L/1n → SC1–SC6 applied `c27189e` → 0330 rule-4 application
pass 0M/1m/1L/1n, SCA1–SCA3 accept-all applied terminal 2026-07-23) →
[`ROADMAP-DONE.md`](ROADMAP-DONE.md).

- [ ] 🎯 **Glossary ratify pass (Mike)** — end-to-end read of
  `method/GLOSSARY.md`: tighten wording, rule on the full-definition entries
  (principal / agent / session / doctrine — new canonical homes), confirm the
  admission rule. Until then the SEED banner holds entries as PROPOSED.
- ⏳ **Capture → doctrine: the close all-clear carries the pushed floor run's
  result** — APPLIED 2026-07-23 (queue run 0959, inline Opus). RECORD.md's
  all-clear evidence rule gained a sub-point: when a close pushes, the evidence
  is the *floor at head*, not the local scan ("green locally, floor run pending"
  is honest; "all green" before the head run reports is a claim past its
  evidence). **⏳ review queued for a non-author** (self-authored doctrine, REVIEW
  rule 4). *Delta:* the RECORD.md all-clear "floor at head" sub-point (landed this
  commit). *Intent record:* this capture line + its grounding (`165c40f`: a 00:47
  close pushed a 🎯-closed item and left the floor red — reviewscan since 00:06 +
  an un-harvested `[x]` — and the next session inherited the debt to restore
  green). Rides the normal review cycle when a qualifying session takes it.
- [ ] **Propagate the widened apex floor to the fleet children** — the remaining
  half (the in-repo restatement sweep is DONE, `a4740c4`, →
  [`ROADMAP-DONE.md`](ROADMAP-DONE.md)). Each child copies the floor block
  statically, so they adopt the
  three-element floor + honesty-precondition clause at their next pin bump /
  harvest, per-child commits. **Ungated 2026-07-23** (apex cycle closed on Mike's
  AWA accept-all). The canonical child floor block now lives at
  `docs/build/templates/CLAUDE.md` (byte-identical to PROPAGATION's inlined
  block) — children align to it. Pairs naturally with the `floor.yml`
  cold-content gate + `pull_request`-trigger adoption already queued below (same
  pin-bump lane).

## build/ layer — open strands

- [ ] **Code-signing standard across the fleet** (Mike, 2026-07-11) — "how do we
      sign all the code in the various repos". Two distinct layers, deliberately
      split by cost:
      - [ ] **Flip CI from warn to block.** signscan runs `--warn` fleet-wide;
            flipping to blocking (drop `--warn`, make the gh-plane warning an
            error) is Mike's call once the pre-existing scanner debt is cleared
            and every active machine signs. Vigilant mode stays off until then.
            **Gate assessed 2026-07-12 (session 47), corrected same day by the
            post-session self-review — not met, and the blockers are the
            owners', not the main line's.** None of the three red children fails
            on *signing* (~~so the flip wouldn't newly-red them~~ — **corrected
            2026-07-19, see below**; but the fleet isn't clean enough to declare
            enforce-mode honestly): two fail
            secretscan on owner-tracked secret debt (the principal's rotations,
            session 39's owed list); the third is red on **both** its bespoke CI
            (lint + a test error, agent-actionable, separate cleanup) **and**
            its floor (leakscan findings). Which child is which lives in their
            own private records, not here (RECORD's name × debt join).
            **Retraction:** this session first published a claim that session 41
            had "mis-filed" the third child's redness as scanner debt — that
            claim was built on a `--limit 1` run query that happened to catch
            the bespoke CI workflow; the floor workflow is red too, session 41's
            filing was accurate, and the accusation is withdrawn. On the two
            secret-debt children signscan never runs (secretscan fails first).
            The **"every active machine signs"** half is also unverified. Flip
            held — Mike's call + Mike's action (the rotations). **Hold
            re-confirmed by Mike 2026-07-23** (offered a scheduled rotation
            sitting; chose hold-as-is).
            **Correction 2026-07-19 — "wouldn't newly-red them" was wrong; the
            greens proved nothing** (under `--warn` no floor can *fail* on
            signing, and on scanner-red children the signing steps never run).
            **Before flipping, run `tools/signfleet.py`** — built this session
            for exactly this question. First run: **10 pass, 2 fail, both
            currently green**. Seven unsigned commits from two causes, neither a
            second machine: a boundary set too early, and five replayed by a
            **rebase-merge** (`gh pr merge --rebase`; merges here are agent-run)
            which re-commits server-side, stripping signatures — a recurring
            hazard, since squash/merge-commit are web-flow-signed and it is not.
            Evidence chain in the session record. **Applied (principal's call):
            both boundaries corrected (signfleet 12/12) and
            `allow_rebase_merge` disabled on all 13 repos — shut server-side
            rather than left to each session to remember; merge-commit + squash
            remain, local rebase unaffected, reversible.** Remaining blocker:
            the scanner debt. "Every active machine signs" stays unverified, but
            the drift behind that doubt is explained and is **not** a machine.
      - [ ] **Release-artifact signing + SBOM (deferred, was A5).** Signing *built
            artifacts* + a deterministic SBOM needs external tooling (syft/cosign),
            which hits the tool-install floor and breaks the zero-dep house-tool
            pattern — a deliberate design call, not a build. Revisit when a real
            *release* (a published package/binary) needs provenance; GitHub's
            native artifact attestations are the lightest route if so. Now also
            recorded as SIGNING.md's layer 2 with the same stated trigger.
  - [ ] **C5 backlog strand**: `tools/scaffold.py` (mechanise the
        seed/rename/stamp core; skill becomes its wrapper) — only if a stamp
        defect recurs despite step 5's new mechanical prove-the-stamp.

Completed build/inheritance work (REPO-STANDARD, licenscan, signing doctrine +
activation, faves/ros floor adoption, create-repo rewire + real-scaffold,
REPO-BOUNDARY, worktree tooling) → [`ROADMAP-DONE.md`](ROADMAP-DONE.md).

## Orchestrated queue runs — from hand-carried prompt to doctrine (Mike, 2026-07-22)

Built 2026-07-22 as ratified (CONCURRENCY § Orchestrated queue runs +
ECONOMICS § tier split + plugin-bundled `queue-run` skill) →
[`ROADMAP-DONE.md`](ROADMAP-DONE.md). What remains open is its review:

- [ ] **Third-seat executor trial (Mike, 2026-07-23, per `dadde1d`)** — on the
  next queue run, dispatch one or two *routine, well-floored* items to the
  mid tier (Sonnet) instead of the workhorse; orchestrator reviews as normal.
  Keep the step-down only on the floor's evidence (scanners/tests/review all
  green, no hand-up); record the outcome either way — tier claims are
  extracted from practice, not assumed. Fan-out sub-agents on the cheapest
  genuinely-capable tier is already standing practice (no trial needed).
  - **Run 1 outcome — 2026-07-23 (Opus-orchestrated queue run):** two items
    dispatched to Sonnet — the **cc-tools vocab audit** (`85b17dd`: clean
    single-file delivery, zero-drift finding correct on my review, 160/160 node
    tests, recommendation correctly *held as a recommendation* not baked) and
    the **S3 datescan build** (`6077972`: `tools/datescan.py` + 41 tests, suite
    372 green, advisory wiring correct, honest baseline reported, exemption
    limits documented honestly). **Both PASSED the orchestrator review with no
    hand-up and no rework** — first positive data point that Sonnet genuinely
    does the routine-docs and first-of-kind-scanner classes under the floor.
    **One run ≠ a standing tier claim** (extracted-from-practice wants
    corroboration): leave the trial open for a second run's data before
    promoting Sonnet to the standing executor seat for these classes. Note for
    contrast: the doctrine-text apex sweep + the correctness-sensitive ccrepo
    ledger were kept on **Opus** this run (doctrine-text + silent-failure class
    → capable tier, per ECONOMICS QR5) — the split behaved exactly as the tier
    rule predicts.
  - **Run 2 outcome — 2026-07-23 (0618 Opus-orchestrated queue run):** two more
    Sonnet items — the **S1 wrapscan** and **S5 spellscan** first-of-kind scanner
    builds (`72e8ecb`/`760260473`, advisory-only, 40+60 tests, suite 472). **Both
    PASSED** the orchestrator review no-rework, each surfacing an honest judgement
    call left to its ⏳ review. (Recorded in the 0618 session entry as "run 2" but
    not folded into this trial record until the 0707 run — reconciled here.)
  - **Run 3 outcome — 2026-07-23 (0707 Opus-orchestrated queue run):** one item
    to Sonnet — **applying the datescan DSR1–DSR8 review findings + re-baseline**
    (`b7b292c`). This is a *step up* from run 1's classes: not a fresh build or a
    docs audit but **modifying scanner detection logic** (a silent-failure class,
    the kind ECONOMICS QR5 nominally routes to the capable tier). It was
    dispatched to Sonnet because it was **exceptionally well-floored** — 41
    existing tests + selftest + a cold review naming exactly what to change — and
    the orchestrator (Opus) re-verified the suite and read the risk-bearing DSR3
    logic + header before merge. **PASSED with no rework**: all eight findings
    applied, baseline 60→0, and Sonnet independently **caught three further real
    bugs** the review hadn't named, declared the DSR3 silent-miss trade honestly
    in-header, and correctly *declined to guess* an un-derivable date (left an
    honest `allow`). **Reading:** the discriminator that worked was the *floor
    density*, not the nominal class — a well-floored silent-failure task with a
    prescriptive review is safely Sonnet-with-Opus-verify; a *thinly*-floored one
    still isn't. **Three runs now agree** (five Sonnet items, zero rework): the
    docs-audit, fresh-scanner-build, and prescriptively-reviewed-fix classes all
    clear the floor. This is now enough corroboration to **write Sonnet into
    ECONOMICS as the standing executor** for those classes — a small doctrine edit
    (self-authored ⇒ rule-4 ⏳ at landing) that a future session should take; the
    one guardrail the data supports is *floor density, not nominal class*, so the
    doctrine line must say "well-floored + prescriptively-reviewed", not "any
    routine work". The two first-of-kind *reviews* this run stayed on **Opus**
    (gate-flip judgement → capable tier) — split held as predicted.

## Security doctrine vs public good practice — gap analysis (Mike, 2026-07-22)

Mike's directive during the SECRETS.md access-management session: *"take into
account any publicly available good practice for security that we should build
into the doctrine"* — OWASP named, the NCSC developers collection linked, and a
secure-SDLC checklist pasted (threat modelling/STRIDE, secure defaults, least
privilege, secure coding, secrets management, supply-chain checks, automated
scanning, peer review, continuous learning). The *credentials* slice landed
same-session (SECRETS.md "Grounding in public practice", `caa85fe` — NIST SP
800-63B rev 4 + OWASP secrets cheat sheet, corroboration named, the one
divergence owned). The rest is a doctrine-wide sweep, deliberately not crammed
into that delta:

Mapping done 2026-07-22 (record:
[`sessions/2026-07-22-1025-security-canon-gap-map.md`](sessions/2026-07-22-1025-security-canon-gap-map.md)
— A/B/E confirmed narrow, C reframed to mutable-tag CI actions, D dismissed
instance-layer) → [`ROADMAP-DONE.md`](ROADMAP-DONE.md).

- **Already held — name, don't rebuild** (verified by the mapping,
  2026-07-22): automated scanning in the pipeline (the floor scanners), peer
  review before ship (REVIEW.md), least privilege (SECRETS triad), secrets
  never in source (right plane), repo protection (ADR 0007 signing + the
  floor — active since 2026-07-12 per SIGNING.md), incident learning (the
  harvest loop; the anti-slop *promotion rule* is a capture below, not yet
  doctrine — the original list overclaimed it, corrected 2026-07-22), clean
  maintainable code (PRINCIPLES).

*review: WARRANTED when the mapping moves to doctrine edits; the capture
itself is records-only.*

## Anti-slop invariant registry — promote recurring review findings to always-on checks (Mike, 2026-07-21)

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
[`sessions/2026-07-22-1036-invariant-candidates.md`](sessions/2026-07-22-1036-invariant-candidates.md))
→ [`ROADMAP-DONE.md`](ROADMAP-DONE.md).

- **S1–S5 / V1–V7 ALL APPROVED 2026-07-23** (Mike, plain-language
  walk-through of the mining record's candidates; the PROPOSED-then-ratify
  pattern; S5 approved explicitly on ROI over its borderline finding
  count). Approved seams/homes are the record's proposals unamended: all
  twelve shared-floor. The promotion rule itself (>2 occurrences ⇒
  candidate) is thereby exercised end-to-end and stands as practice.
**All five approved scanners S1–S5 are BUILT + wired advisory** (S1/S3/S5
earlier; S2 `pathscan` `b738f21` + S4 `stampscan` `2fe97f3` this run — detail →
[`ROADMAP-DONE.md`](ROADMAP-DONE.md)). **S1/S3/S5 first-of-kind reviews are DONE**
(S3 at 0618; S1 + S5 at 0707 — verdicts + follow-ons below). **S2 + S4 reviews
are the open first-of-kind work (⏳ below).**
- ⏳ **pathscan (S2) first-of-kind review** — advisory `b738f21` (queue run
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
- ⏳ **stampscan (S4) first-of-kind review** — built + merged `2fe97f3` (queue
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
*datescan (S3) review is DONE (2026-07-23) — verdict PASS-WITH-FINDINGS
(0 MAJOR / 4 minor / 3 Low / 1 nit), NOT gate-ready (~75% baseline noise); brief
[`docs/reviews/2026-07-23-0618-datescan-s3-cold.md`](reviews/2026-07-23-0618-datescan-s3-cold.md),
detail → [`ROADMAP-DONE.md`](ROADMAP-DONE.md). Its follow-ons: the DSR-apply is
now DONE (above); the flip precondition is met (above). S1/S5 follow-ons below:*

*datescan DSR1–DSR8 apply + re-baseline DONE 2026-07-23 (queue run 0707, Sonnet
`b7b292c`) — baseline 60→0, detail → [`ROADMAP-DONE.md`](ROADMAP-DONE.md). The
flip follow-on stays open:*

*datescan advisory→blocking flip — **RULED + DONE 2026-07-23 (Mike: "agree flip
it")**. atelier `ci.yml` datescan dropped `--warn` (blocks clean, 0 breaches);
child `floor.yml` template gained a docs-scoped datescan blocking step + its
selftest, so children adopt at their next pin bump (re-baseline first — see the
fleet-floor item below). Honest limit recorded in-gate: DSR3 narrowed `today`, so
a bare "today = this date" claim with no cue passes silently — tighter but not
exhaustive. → [`ROADMAP-DONE.md`](ROADMAP-DONE.md) at next harvest.*
*wrapscan (S1) first-of-kind review DONE 2026-07-23 (queue run 0707, cold Opus) —
**PASS-WITH-FINDINGS 1M/3m/2L**, NOT gate-ready; MAJOR is gate-scope not
detection (154/287 baseline is deliberate SESSIONS index rows). Brief
[`docs/reviews/2026-07-23-0707-wrapscan-s1-cold.md`](reviews/2026-07-23-0707-wrapscan-s1-cold.md),
detail → [`ROADMAP-DONE.md`](ROADMAP-DONE.md). Two follow-ons stay open:*

*wrapscan (S1) review APPLIED 2026-07-23 (queue run 0959, `ceb3fda`) —
option-A scope + WS1–WS6, gated scope 0 findings, stays advisory →
[`ROADMAP-DONE.md`](ROADMAP-DONE.md). The flip precondition is now met:*
- [ ] 🎯 **wrapscan flip (Mike's call, once clean)** — **scope RULED 2026-07-23
      (Mike: "agreed option A")**: doctrine-surface scope + `.wrapscanignore` the
      record stores. **Apply landed `ceb3fda` (above) — the flip precondition is
      now MET: a clean `--warn` run over the gated doctrine surface (0 findings).**
      Drop `--warn` + add to `floor.yml` is a Mike go/no-go. Not pre-authorised;
      surfaced here now clean.
*spellscan (S5) first-of-kind review DONE 2026-07-23 (queue run 0707, cold Opus) —
**PASS-WITH-FINDINGS 0M/2m/1L/1n**, NOT gate-ready; core safety proven (no wrong
corrections), real latent bug SS1 found, license/practice exclusion ruled
permanent. Brief
[`docs/reviews/2026-07-23-0707-spellscan-s5-cold.md`](reviews/2026-07-23-0707-spellscan-s5-cold.md),
detail → [`ROADMAP-DONE.md`](ROADMAP-DONE.md). Follow-ons stay open:*

*spellscan (S5) review APPLIED 2026-07-23 (queue run 0959, `b910962`/`4872f07`)
— SS1–SS4 + `catalogue` rename, baseline 71→40 (remainder all genuine/quotes),
stays advisory → [`ROADMAP-DONE.md`](ROADMAP-DONE.md). It surfaced a live
follow-on that also blocks the flip's near-zero re-baseline:*
- [ ] 🎯 **Rule the ~36 general-sense `artifact`→`artefact` breaches in frozen
      records** (surfaced by the 0959 spellscan apply). The apply proved the
      *general* "a produced thing" sense (a session record, a web page) is a
      genuine NZ breach distinct from the CI/SBOM term-of-art — and ~36 of the
      40 remaining spellscan findings are that sense sitting in **frozen
      historical records** (`SESSIONS.md`, `ROADMAP-DONE.md`, `docs/reviews/*`,
      other `docs/sessions/*`), which the apply's bounds deliberately did not
      touch. **The decision is Mike's** because it collides with the
      immutable-history ethos (current-truth/history split): either (a)
      spelling-normalise the frozen records too, or (b) rule them permanently
      out of scope as *untouched history* — a `.spellscanignore`/allow on the
      record stores. This is also the **spellscan flip's blocker**: near-zero
      re-baseline can't be reached until (a) or (b) lands. (Adjacent, noted not
      acted: two `artifact→artefact` rename-notation *mentions* at
      `SESSIONS.md:157` + a review file — a MENTION not a USE, a possible future
      heuristic extension.)
      **license/practice exclusion ruled PERMANENT by the review** (empirically
      vindicated — `practice` ×178 is correct NZ noun usage).
*spellscan `catalog` rename DONE (both frozen records; article quote verbatim).
The advisory→blocking **flip stays a Mike go/no-go**, now with its precondition
named: it is blocked on the 🎯 above (near-zero re-baseline needs the frozen-
record `artifact` decision first) — datescan's pattern.*
- [ ] **Codify V1–V7 as the always-loaded reviewer checklist** — the
      registry mechanism's doctrine half; lands in REVIEW.md/the review
      skill with each item's cited grounding. Self-authored doctrine ⇒
      rule-4 ⏳ at landing.
- [ ] **Two-layer acceptance criteria, one verification pass.** (Build item —
      waits on the 🎯 rulings above; the mining record's "how the registry
      would be checked" section holds the proposal.) Per-change
      criteria (task-specific) + the invariant catalogue (loaded automatically)
      assemble into ONE checklist a verifier runs. The author need not remember
      the org rule — the catalogue enforces it unasked. Invariants are
      declarative rules with conditions (path globs, exemptions), e.g. "writes
      to `users` must go through the repository; exempt migrations; glob
      `src/**/*.go`".
- [ ] **Enforcement seam — how does an invariant get checked?** (Per-candidate
      seams proposed in the mining record — scanner vs checklist vs verifier,
      one line of why each; decisions ride the 🎯 rulings above.) Three
      candidates to place on our existing spectrum: a CI scanner (like
      leakscan/secretscan — the machine-checkable ones), a review-time
      checklist item, or an agent-verifier criterion. Decide which invariants
      are code-checkable (→ scanner) vs judgement (→ verifier/human).
- [ ] **Where does the registry live?** (Proposed per candidate in the mining
      record — all five scanner candidates shared-floor, one checklist
      repo-specific; decision rides the 🎯 rulings above.) atelier-shared floor invariants (fleet-
      wide, like the current scanners) vs repo-specific catalogues (a child's own
      conventions). Likely both, same layering as doctrine: shared floor +
      local append. Ties REPO-STANDARD.

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

## instruments/ — open features

### cc-tools parameter vocabulary (Mike, 2026-07-23)

Strand closed 2026-07-23 (queue run): the flag-vocabulary audit found zero
drift (`85b17dd`, vocabulary table in `instruments/README.md`) and Mike
ratified **flags-follow-operation** as the adopted principle → detail in
[`ROADMAP-DONE.md`](ROADMAP-DONE.md).

### ccarchive (Mike, 2026-07-17)

Restore (full + delta), dataless awareness, and manifest signing all built
2026-07-22; the two open questions answered by measurement (tool-result
sidecar capture hole; keep-separate counselled) → detail in
[`ROADMAP-DONE.md`](ROADMAP-DONE.md), record
[`sessions/2026-07-22-1050-cc-instruments-questions.md`](sessions/2026-07-22-1050-cc-instruments-questions.md).
What remains is Mike's:

- **Metadata classes RULED 2026-07-23** (plain-language walk-through, the
  cc-instruments record's context relayed): tool-result sidecars **capture**;
  per-project `memory/*.md` **capture**; top-level `history.jsonl`
  **capture — Mike overturned the lean-exclude counsel** (wants the
  typed-prompt stream as a first-class artefact; grounds: his call, small
  cost). Signing defaults + keep-separate counsel **accepted as-is** —
  binary exits, new-machine red-until-key, two instruments; that 🎯 closes
  with no work owed.
- **ccarchive capture widened — BUILT 2026-07-23** (`3c6394d`, merged
  `2df595e`): all four ruled classes first-class end-to-end, exclusions
  now documented in a man-page CAPTURE section, 150 tests green. One
  operator note: the shrink guard covers memory files uniformly, so a
  legitimately condensed memory file needs `--force` — safe-over-silent.
  Detail → [`ROADMAP-DONE.md`](ROADMAP-DONE.md).

### ccrepo (Mike, 2026-07-17)

Reconciliation drift closed 2026-07-22 (richest-record dedup; exact ccusage
match on frozen data); spend-config fill closed 2026-07-23 (populated from
real receipts, machine-local); archive sourcing (`--from-archive`, closing the
observe-side seam alongside cctranscript) closed 2026-07-23; the **rollup
precompute ledger** (`8a31b95`, 3.1× warm speedup, `rollup==recompute` proven
live, per-file keying, transparent-by-default confirmed by Mike) closed
2026-07-23 → [`ROADMAP-DONE.md`](ROADMAP-DONE.md). ccrepo strand closed.

Completed instruments work (ccrepo actuals/breakdown, ccarchive integrity/audit,
the **man-page convention rollout — ccarchive worked example + cctranscript +
ccrepo, all installed CLIs now carry a `man/<tool>.1` + trimmed `--help`, closed
2026-07-21**) → [`ROADMAP-DONE.md`](ROADMAP-DONE.md).

## File-size hygiene (new 2026-07-14)

The generalised anti-bloat work. `sizescan` flags relocatable **cold content** on
the hot path across the fleet (and reports size as advisory); these are the
outstanding strands.

Completed file-size work (the 2026-07-14 sizescan build/review + wiring; the
2026-07-18 fleet harvests — ros 7123→982 in two ruled stages, faves, shed; the
grounded-budgets correction; the 2026-07-19 tripwire-split application, superseded
by the cold-content rebalance; the **2026-07-20 size-signal rebalance to a
cold-content gate + its rule-4 review (PASS 0M/2M/3L) + Mike's accept-all ruling
applied 2026-07-21**; the fleet-wide `hooks.atelierTools` fix) →
[`ROADMAP-DONE.md`](ROADMAP-DONE.md).
- [ ] **Existing fleet children pick up the reworked `floor.yml` gate** — children
      copy `floor.yml` statically, so they adopt the cold-content gate at their
      next pin bump / harvest. **At the same bump, apply the 2026-07-23 trigger
      ruling (Mike): private children that take no fork PRs drop the
      `pull_request` trigger** — halves metered-minute burn; the merge-preview
      scan is consciously traded away where the owner is the only contributor;
      public children keep both (free). They also inherit the SHA-pinned
      actions + the SECURITY.md template from the security-canon close, **and the
      new docs-scoped `datescan` blocking step (added to the template 2026-07-23
      on Mike's flip ruling) — a child RE-BASELINES its records first (ISO-fix or
      `datescan:allow` the genuine breaches; that first red is the signal) and
      adjusts the path if it keeps records outside `docs/`.** **The rebalance dissolves the all-open-roadmap
      red**: a wholly-open ROADMAP (ros's ~125 open items) no longer reds on
      length — with no cold content to relocate it is advisory now, not a standing
      red — so the class-grounded-budget workaround is no longer needed for that
      case. A child that still reds does so on un-harvested `[x]` items, its own
      harvest lane. faves and ros run bespoke CI without `sizescan --check` — a
      separate floor-adoption step.

## North star — context follows the person, work follows anywhere

- [ ] **Two-tier person-context portability.** **Design pass DELIVERED
      2026-07-22** →
      [`sessions/2026-07-22-1233-person-context-portability-design.md`](sessions/2026-07-22-1233-person-context-portability-design.md)
      — constraints C1–C8 from cited doctrine, an 8-threat pass, candidate
      architectures per leg, argued recommendations (tier-1 filesystem:
      age/sops capsule, decrypt-on-need; tier-2: estate-root private repo +
      wrong-tier gate; tier-1 phone: out of scope app-native, phone-as-
      terminal when needed; tier-2 phone: app memory as a declared, dated
      second system; seam: filesystem canonical, phone derived). Records-
      only; review WARRANTED when it moves to build/doctrine.
  - **D1–D5 RULED 2026-07-23** (plain-language walk-throughs; stamps and
    grounds in the design record §Decision stamps): D1 the capsule rides
    the private estate repo (plaintext-binding reading confirmed); D2+D4
    **full app-plane parity, superseding the design's counsel** — both
    tiers reach phone/web/desktop-app memory as a generated, date-stamped
    profile (grounds recorded: no phone-unique risk; tier-1 already
    transits the provider in filesystem-leg conversations; standing
    memory deletable); D3 ADP enabled and may be load-bearing; D5 the key
    backup lives in the person-level credential home.
  - [ ] **Build the capsule** — encrypt tier-1 into an age capsule with
        per-machine keys, estate-repo carrier (D1), decrypt-on-need
        unlock, key backed up per D5. Gated on writing the
        **tier-classification rule** (what makes a fact tier 1 — a
        doctrine act) and the wrong-tier pre-commit gate (design §5).
  - [ ] **App-plane profile generator** — render the date-stamped
        both-tier profile from the canonical store for the app's
        memory/Projects (D2/D4 parity ruling); define the reconcile
        cadence; the one-directional seam holds (filesystem canonical).
      Original item, for context: both excluded from atelier, both
      must reach every device Mike works from, handled by sensitivity:
      - *Crown-jewels* (health/family/finance/estate map): E2E-encrypted only
        (iCloud ADP or sops/age); **never a plain remote, not even private
        GitHub**; encrypted at rest even locally; device floor (FileVault/
        passcode).
      - *Instance/identity/toolbox* (accounts, venv paths, domains, client-entity
        facts): private but lighter; may tolerate a private store/repo.
      Honest gap: the **iPhone leg has no filesystem mechanism** — the Claude app
      doesn't read `~/.claude`; phone-side is app memory/Projects, a different
      system. This needs a focused design pass, not "a sync problem".
- [ ] **Resume any project from any device, anywhere** — depends on propagation
      + person-context above.

## Session archive — decided 2026-07-23

Superseded by ccarchive (Mike's ruling, plain-language walk-through): the
nightly iCloud archive under ADP-class E2E answers the original item's
encryption concern; one archive, tamper-checked, capture widened same day
(sidecars + memory + prompt history). Consciously not taken: the NAS
second leg and a rolling-retention clock — history is kept indefinitely
unless Mike asks for a retention rule. Detail →
[`ROADMAP-DONE.md`](ROADMAP-DONE.md).

## Sharing — public since 2026-07-10 (ADR 0005)

The private-first sequence (peer-adoption → restructure → *then* public) was
consciously collapsed: the peer-of-two never became a peer-of-three, so **public
is the friction mechanism**, not a reward withheld until after it. atelier is
public as a **named worked example** (README "If you're adopting this"). What was
"before public release" is now **post-public hardening**:

- [ ] **One real peer adoption** (CEL, then a client-org) — still the highest-value
      hardening; now happens *with* strangers able to read it too. Treat their
      confusion as the harvest.
- [ ] **Practice/instance restructure** of AUTONOMY + STORAGE — the person-local
      specifics (grant ledger, Apple/iCloud) → marked worked-examples. No longer
      a publication gate; do it as the named-worked-example framing gets tested by
      a real adopter.
- [ ] **Exercise the interactive fill + bundled-mode scaffold end-to-end**
      — owed post-ship; both flagged unexercised (model-prose, proven at
      use) in the CHANGELOG's own honesty note. Per VA2 (2026-07-23) the
      exercise now includes the **plugin-update case**: install 0.2.0,
      scaffold bundled-mode, update the plugin, observe whether the stamped
      `<plugin-path>` tracks, dangles, or goes stale — then reconcile
      `commands/install-hook.md`'s dangling-path wording and make the
      variant's drift bullet state what a missing path means. No text change
      before the observation (the honest fix is the exercise, not a guessed
      sentence).

Completed sharing work (public release, the plugin bundle widening, atelier's own
CI, child-CI scanner floor, linkscan build + wiring) → [`ROADMAP-DONE.md`](ROADMAP-DONE.md).

## Open questions

- **Checkbox grammar RULED 2026-07-23 (Mike): keep the tri-state** — the
  bracket answers the one machine-checked question (is work owed?);
  dispositions live in dated notes. Promote to five states only if we find
  ourselves repeatedly grepping dispositions apart (the promotion rule).

- Does ros keep canonical copies of any doctrine, or hold only bearings + point
  up for everything (as §0 now does)? Default: point up; resolve per doc at
  extraction.
- **Floor template's duplicate trigger — RULED 2026-07-23 (Mike): trim
  `pull_request` on no-fork private children**, applied per child at its
  next pin bump (standing guidance now in the fleet-adoption item above);
  public children keep both triggers (free). The template itself stays
  two-trigger — it serves public repos too, and the N4 publish-safety
  rationale holds there. Full two-sided analysis preserved →
  [`ROADMAP-DONE.md`](ROADMAP-DONE.md).

- [ ] **Map and understand the difference between honesty (that claude does
      well), the truth, and transparency** — MIKE'S raw note, to be fleshed out
      BY MIKE before anyone interprets it: it is fundamental to atelier (apex-
      level, touches 00-APEX.md) and he wants to define it himself. Do NOT
      elaborate, reframe, or seed a design around this line until Mike has
      expanded it. Prompt him with exactly this line. (Mike, 2026-07-22.)
- [ ] **Grab the AI chat (Teams, 15/7/26) with a colleague** <!-- datescan:allow: verbatim; wrapscan:allow: marker-inflated line --> —
      MIKE'S raw to-do, to be fleshed out and positioned BY MIKE before anyone
      interprets it. The export is held locally/privately; the full verbatim pointer
      (name + path) is kept in Mike's private note, deliberately NOT published
      here (atelier is public). Do NOT interpret until Mike expands it.
      (Mike, 2026-07-22.)
The `MODEL-ECONOMICS.md` → `ECONOMICS.md` rename was executed 2026-07-22
(nothing dangles; children re-point at their next pin bump) →
[`ROADMAP-DONE.md`](ROADMAP-DONE.md).

Resolved questions (docker-heap standardisation, estate credential governance) → [`ROADMAP-DONE.md`](ROADMAP-DONE.md).
