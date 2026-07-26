# Cold review (rule 4) — PRINCIPLES §1: "Design the way out before the way in"

**Subject (refs only):** the bullet added to `docs/method/PRINCIPLES.md` §1 in
commit `e29c49a` (2026-07-24). Establish the exact hunk with
`git show e29c49a` and review it at HEAD, in the context of the whole
principles set.

**Spawn provenance:** this review was spawned by a non-author taker session the
principal (Mike) opened and pointed at the review queue on 2026-07-26 ("Please
do any review work"); the work's author neither started nor instructed this
review or this reviewer; the taker authored none of the delta and gives the
reviewer refs only, no evaluative account. Session and reviewer tier: Fable
(cold review passes run on Fable — the principal's ruling, 2026-07-26).

**Taker exposure, owned:** the taker read the ROADMAP queue pointer and
SESSIONS index one-liners before writing this stub. Nothing evaluative from
either appears above the divider.

**The reviewer's first acts:** establish what the bullet claims and why from
the delta and HEAD yourself; name the load-bearing assumptions and attack
surface as your own; run all four lenses at the widest scope
(`docs/method/REVIEW.md`). The heavy lenses: 1 — is adopt-only-once-the-exit-
exists the right rule stated at the right strength (absolute vs default), and
does it hold against the repo's own practice (the dependencies atelier and its
tooling actually carry — check them against the rule rather than trusting the
bullet's own grounding claims); 3 — coherence with its named twin ("Build the
way back before the way forward") and with REACH's escalate-cheapest-first /
never-mint-what-you-can't-withdraw language — genuine pairing or duplicated
rule with drift potential; 2 — any overclaim in the bullet's grounding.

**Re-run obligations:** `python3 tools/floor.py --plane ci` ·
`python3 -m unittest discover -s tools` · `node --test instruments/*.test.js`.
Lens 4: a landed one-bullet markdown delta — discharge `/security-review` in
one explicit line with grounds; note that the bullet itself is *about*
dependency risk, so lens 4's design-altitude reading of it (does following it
reduce or create exposure) is in scope.

**Reading discipline (hard):** do not open `docs/ROADMAP.md`,
`docs/SESSIONS.md`, `docs/sessions/**`, any other file in `docs/reviews/`, or
anything under `docs/reviews/withdrawn/`. Do not grep git history for review
commits; confine git archaeology to the delta commit named above. Open the
deferred section below only after your findings are durably written to this
file; then append the reconcile, named as such.

Findings carry stable IDs (**WO1…**) with claim / evidence / counsel; close
with **PASS**, **PASS-WITH-FINDINGS**, or **FAIL** and severity counts.
Self-authored doctrine at the principal's instruction: REVIEW.md rules 3–4
govern — findings are the principal's to decide; nothing is applied in this
pass.

---

## Deferred — open only after your findings are durably written above

*Intent record:* no separate record — the queue pointer states the intent: a
new resilience principle paired with "Build the way back before the way
forward" — before adopting an external dependency, first establish how you
keep working without it (fallback / export path / swappable seam / degraded
mode); adopt only once the exit exists. Grounded, per the pointer, in
atelier's zero-dependency tooling as the limit case and browser-fetch as the
documented dependency exception, and cross-linked to REACH.

---

## Reviewer's attack surface (named before any deferred content read)

*Reviewer: cold rule-4 session, Fable, worktree at HEAD `9aef298`. Established
the subject from `git show e29c49a` and `docs/method/PRINCIPLES.md` at HEAD.
Read so far: the delta commit, PRINCIPLES.md, REACH.md, REVIEW.md. Nothing
below the brief's divider, no other reviews, no ROADMAP/SESSIONS at HEAD.*

The bullet's load-bearing assumptions, as I name them:

1. **The absolute is right-strength.** "Adopt only once that exit exists" is
   stated as an absolute (within PRINCIPLES' standing stated-exception
   grammar). Assumption: every external dependency adoption can afford an exit
   at adoption time. Attack: find a dependency class where the rule is either
   vacuous (an exit trivially "exists" — git's distributed nature as the exit
   from GitHub) or unmeetable (the harness the whole operating model runs on).
2. **The repo's own practice complies.** The bullet claims grounding in
   atelier's practice (zero-dep tooling, browser-fetch as the documented
   exception). Attack: enumerate the dependencies atelier and its tooling
   *actually* carry — runtimes, CI platform, hosting, the agent harness itself,
   the browser-fetch engine — and test each against "the exit existed at
   adoption". If a load-bearing dependency has no established exit, the
   grounding claim is an overclaim and the rule indicts the practice it claims
   to be grounded in.
3. **The cross-links say what the bullet says they say.** The bullet cites
   REACH "escalate-cheapest-first and never mint access you can't withdraw".
   Attack: verify REACH actually carries the second phrase as stated; a
   citation to paraphrased language that doesn't exist is a §6 provenance
   defect in doctrine.
4. **The twin is a genuine pair, not duplication.** "Build the way back"
   (restore path per destructive action) vs "Design the way out" (exit per
   adopted dependency) — and, the sharper risk I add myself: §2's "commodity
   sub-feature sits behind a swappable seam" bullet already governs swappable
   seams for adopted capability. Attack: is the new bullet a third home for
   seam doctrine, with drift potential across §1/§2?
5. **Compliance is visible.** §6 says a principle whose violation is invisible
   isn't a principle; the twin bullet demands a *stated* way back. Attack: does
   this bullet require the exit be recorded anywhere? An "established" exit
   nobody wrote down is unverifiable at review time.
6. **Following the rule reduces exposure (lens 4, design altitude).** An exit
   path is a second code path: fallbacks and degraded modes are classic
   security-bypass surfaces. Attack: does the bullet say the exit must hold
   the security posture, or does it silently license a weaker back door?
7. **Placement in §1 is right.** It's a design-time adoption rule; §1 is
   runtime resilience, §2 owns coupling/seams. The bullet pre-empts this with
   its "runtime faces / design-time commitment" sentence — test whether that
   holds or is a patch over a mis-filing.

Re-run obligations accepted: `python3 tools/floor.py --plane ci`,
`python3 -m unittest discover -s tools`, `node --test instruments/*.test.js`,
and an explicit one-line `/security-review` discharge with grounds.

---

## Verdict — cold rule-4 pass (Fable, 2026-07-26, worktree at `9aef298`)

**Provenance repeated:** spawned by a non-author taker session the principal
opened and pointed at the queue; the author neither started nor instructed this
review; reviewer received refs only. Reviewer read nothing below the brief's
divider before this section was written; no other review files, no
ROADMAP/SESSIONS at HEAD, no withdrawn/ content, git archaeology confined to
`e29c49a`.

### Re-runs

- `python3 tools/floor.py --plane ci` — **exit 0**, all nine scanners enforced
  and clean (one pre-existing size-advisory on `docs/ROADMAP.md`, advisory
  only, never fails `--check`).
- `python3 -m unittest discover -s tools` — **exit 0**, selftest OK.
- `node --test instruments/*.test.js` — **207 pass / 0 fail**.
- **`/security-review` discharged in one line with grounds:** the work is a
  landed one-bullet markdown delta — nothing dirty for a pending-changes
  scanner to read, and markdown documentation is outside the scanner's file
  classes, so any pass would be definitionally empty (REVIEW.md's own caution);
  lens 4 is instead run at design altitude below (WO5).

### Findings

**WO1 (minor) — the REACH cf. attributes a maxim REACH does not carry.**
*Claim:* `PRINCIPLES.md:61-62` cites "cf. REACH.md escalate-cheapest-first and
never mint access you can't withdraw"; the second phrase exists nowhere in the
doctrine — `grep -rn withdraw docs/method/` hits only this bullet and an
unrelated RECORD.md line. *Evidence:* REACH's actual boundary is "never mint
access from the principal's saved credentials" without an explicit grant
(`docs/method/REACH.md:6-7`) and ride-not-mint (`REACH.md:107-119`) — an
ownership/provenance rule (whose store), not a revocability rule (what can be
withdrawn). The paraphrase changes the cited rule's content; the same invented
phrase rides the queue record (the `e29c49a` ROADMAP hunk).
Escalate-cheapest-first is cited accurately. *Counsel:* cite REACH's real
language, or own the withdrawability gloss as this bullet's reading;
revocability content honestly lives nearer §5 (short-lived credentials,
"losing it costs a rotation", `PRINCIPLES.md:193-206`) if a cf. for it is
wanted.

**WO2 (minor) — no stated-exit tooth; the twin has one, this doesn't.**
*Claim:* "first establish how you keep working without it" never requires the
exit be *recorded*; the twin closes with "A destructive verb with no stated
way back is not finished" (`PRINCIPLES.md:50-51`), and §6 holds that a
principle whose violation is invisible isn't a principle. With "the ability to
run degraded" on the accepted-exit list, an unrecorded exit is claimable by
hand-wave ("we'd manage"), unverifiable at review time. *Evidence:* the repo's
own compliant practice records its exits — the toolchain residual named in
`tools/README.md:103-109`, browser-fetch's exception status in
`instruments/README.md:11-13` — so the bullet under-specifies relative to its
own grounding. *Counsel:* add the symmetric closing tooth, e.g. "an adoption
with no stated exit is not finished".

**WO3 (minor) — §2's adopt-outright clause now silently collides.**
*Claim:* §2's seam bullet licenses "adopt that product outright rather than
build (KISS, precedence 5–6)" with no exit mention (`PRINCIPLES.md:135-137`);
the new bullet preconditions *every* adoption on an exit. Neither
cross-references the other, though both carry the "swappable seam" concept
from opposite directions (in-house default swappable *for* a product; adopted
product swappable *away*). This — not the way-back twin — is where the brief's
duplication/drift question lands: a reader inside §2's grammar adopts outright
and never meets §1's precondition. *Evidence:* `PRINCIPLES.md:53-62` vs
`128-143`. *Counsel:* one cross-link closes it — e.g. §2's "adopt that product
outright" gains "(with its way out designed first — §1)".

**WO4 (note) — the retrofit-cost claim is asserted, not case-grounded.**
*Claim:* "the exit is cheapest to build at adoption time — near-impossible to
retrofit mid-outage" (`PRINCIPLES.md:57-58`) carries no atelier case. The
practice grounds the *destination* — zero-dep tooling (`tools/README.md:78-87`,
verified: no third-party deps outside `instruments/browser-fetch/requirements.txt`),
browser-fetch surviving its own loss via ladder rungs 1–2 — but no decided
instance exercises the *before-adoption timing* the bullet's title rule turns
on. Not invented-to-fill-a-heading; it is general engineering wisdom stated as
if decided. §6: a claim carries its test. *Counsel:* accept as the general
claim it is, or wait for the first real adoption under the rule to become its
case and say so.

**WO5 (note) — lens 4 at design altitude: the exit is itself a surface.**
*Claim:* following the bullet reduces lock-in and supply-chain exposure
(consistent with §8's zero-dep control, `PRINCIPLES.md:286-292`), but an exit
is a second path: an export/migration path is a data-egress mechanism, and a
degraded mode is where fail-safe defaults are most tempted to relax. §2's seam
bullet names its §5 interaction for security-critical commodities ("held to
§5..., not waved through", `PRINCIPLES.md:138-140`); this bullet is silent on
whether the exit must hold the posture. *Evidence:* `PRINCIPLES.md:53-62`
lists exit forms with no §5 hook. *Counsel:* either a short clause (the exit
is designed to §5 and §1 fail-safe standard, never a weaker back door) or an
explicit acceptance that §5's global binding suffices — the principal's call.

### What held (attacks run and failed)

- **Strength (absolute vs default):** "adopt only once that exit exists" is
  right-strength inside the preamble's stated-exception grammar
  (`PRINCIPLES.md:4-5`); the unpinned-toolchain residual shows the exception
  path already working in practice (`tools/README.md:103-109`). The vacuity
  risk is WO2's recording gap, not a strength defect.
- **Practice compliance:** the grounding claim survives the check the brief
  ordered. Dependencies actually carried: tools/ — genuinely zero-dep;
  browser-fetch — pinned `mcp`/`playwright`, documented as the exception, its
  loss leaves rungs 1–2 working; CI — three SHA-pinned actions
  (`.github/workflows/ci.yml:74-82`, `floor.yml:81-94`) with the local hook as
  the degraded plane; toolchain — stated residual; GitHub hosting — git's
  distributed model is the inherent export path. No un-exited, un-stated
  load-bearing dependency found.
- **Twin pairing:** genuine pair, not duplication — distinct objects (a
  destructive *action*'s restore path vs an *adoption*'s exit path), and the
  bullet's differentiation from the circuit breaker / graceful degradation is
  accurate. The real drift risk sits with §2 (WO3).
- **Placement:** §1 is coherent — beside its twin, with the "runtime faces /
  design-time commitment" sentence doing real work, not patching a mis-filing.

### Verdict

**PASS-WITH-FINDINGS** — 0 MAJOR · 3 minor (WO1–WO3) · 2 notes (WO4–WO5).
The bullet is sound doctrine, correctly placed, honestly grounded in the
practice it names; its defects are a mis-attributed citation, a missing
stated-exit tooth, and an un-cross-referenced collision with §2. Per rule 3,
all findings are the principal's to decide; nothing applied in this pass.

## Reconciliation (deferred section opened after verdict committed)

The deferred section carries no seeded questions — only the intent record,
which restates the queue pointer's claims (pairing, exit-before-adoption,
grounding in zero-dep tooling + browser-fetch, "cross-linked to REACH").

- **Findings added:** none. The intent record raises nothing the attack
  surface and verdict had not already tested.
- **Findings withdrawn:** none.
- **Findings sharpened:** none in substance. One observation for the record on
  **WO1**: the deferred intent says only "cross-linked to REACH" — the
  invented maxim ("never mint access you can't withdraw") appears in the
  bullet itself and in the `e29c49a` ROADMAP hunk, both already cited in WO1;
  the deferred text neither strengthens nor weakens that finding.

Verdict unchanged: **PASS-WITH-FINDINGS** — 0 MAJOR · 3 minor · 2 notes.
