# Review brief — SC1–SC6 application to the security canon (cold, rule-4)

- **Stamped**: 2026-07-23 03:22 UTC (brief written before any applied file was
  opened)
- **Subject**: commit `c27189e` — the application of the SC1–SC6 rulings onto
  the security-canon doctrine. Files in the delta: `SECURITY.md`,
  `tools/README.md`, `tools/pre-commit.sample`, `docs/build/REPO-STANDARD.md`,
  `docs/build/templates/SECURITY.md`. Reviewed as applied text at HEAD
  (`9df3510`).
- **HEAD attribution, established mechanically before this brief**: one later
  commit from another, closed cycle (`bbaec81`, v2-plugin application) touched
  `docs/build/REPO-STANDARD.md` after the subject — its sole hunk is confined
  to Process step 1 (signing bake, profile-gated), disjoint from every SC hunk.
  All SC-applied text at HEAD is therefore `c27189e`'s wording, and `bbaec81`'s
  step-1 wording is out of scope for this verdict.
- **Rule-4 status**: the prior pass (0222 security-canon cold) carried 1 MAJOR,
  so this application inherits rule-4 status. Findings are the principal's to
  decide (rule 3); this reviewer recommends and applies nothing. If this pass
  returns no MAJOR, the cycle is terminal per REVIEW.md's close rule.

## Spawn provenance (stated verbatim, repeated in the verdict)

This review was spawned by a non-author taker session that the principal (Mike)
opened and pointed at the review queue on 2026-07-23; neither the doctrine's
author, any prior verdict's author, nor the applier session (or its subagents)
started or instructed this review or this reviewer; the taker authored none of
the chain and gave the reviewer refs only.

## Sequencing note — the application-review residual (rule 2), named not denied

An application review cannot fully honour rule 2: the delta's own commit
message carries a per-ruling digest (SC1–SC6, one line each), read via
`git show` before this brief because HEAD attribution required it — that is
the applier's framing of what each ruling meant, and it cannot be un-read.
The ROADMAP pointer likewise names the chain. Beyond that exposure the
deferral holds: the prior verdict
(`docs/reviews/2026-07-23-0222-security-canon-abce-cold.md`), all other
`docs/reviews/` files, `docs/sessions/`, `docs/SESSIONS.md`, and
`docs/ROADMAP-DONE.md` stay unopened until my findings are durably written
below. The reconcile section (ruling-by-ruling faithfulness) is written only
after that point.

## Attack surface — named by this reviewer as its first act

The subject is a security-surface delta: it edits the repo's disclosure
channel, its supply-chain pinning doctrine, and the trust story for the
scanners every child repo's gate depends on. My load-bearing assumptions to
attack, before reading any applied text:

1. **The PVR claim is live, not stale.** The commit claims private
   vulnerability reporting is enabled and API-verified. A recorded proof can
   be false at HEAD — re-run it, don't take it.
2. **"Swept to the fetch-at-CI reality" actually matches the shipped
   reality.** The stale "deferred" notes are claimed gone; the replacement
   prose is claimed to describe what `floor.yml` actually does. Both halves
   are checkable: grep the stale phrasing repo-wide, and read `floor.yml`
   against the new prose. A sweep that swapped one wrong description for
   another is worse than the stale note it replaced.
3. **The pin-bump recipe works as written.** SC3 adds an annotated-tag
   dereference (`.object.type` check). A recipe an adopter will paste must
   parse and behave — for annotated *and* lightweight tags, and for the
   failure path (tag missing, API error). Check the actual commands.
4. **The trust-root asymmetry is *named*, not *resolved* — and naming it is
   enough only if the residual list is honest about what an adopter
   inherits.** SC5 puts "detection floats, trust roots pin" in a residual
   list. Attack: does the applied text leave a child repo trusting
   `atelier@main` scanner code fetched at CI time — an unpinned execution
   path inside the very gate the doctrine calls load-bearing? Is that risk
   stated at true strength where an adopter will read it, or buried?
5. **Cross-file coherence after a five-file edit.** SECURITY.md (root),
   the SECURITY.md template, REPO-STANDARD, tools/README, and
   pre-commit.sample all describe overlapping machinery. After the sweep, do
   they tell one story (uptake split, PVR-at-seeding, pin discipline), or
   did the application fix each file locally and leave a contradiction
   between them?
6. **The uptake split (SC4) is operationally true.** "Scanner fixes float to
   child CI at main; doctrine/template fixes ride the pin bump" — verify
   that is what the shipped mechanics actually do, not just what the
   sentence now says.
7. **CI action SHA-pins still hold where the doctrine states them.** Re-check
   the referenced pins against the shipped workflow(s).

The brief's own framing — including the taker's handed description of the
subject — is attackable per rule 1; nothing above narrows the widest scope
the work admits.

## The four lenses, aimed

1. **Approach & assumptions** — was accept-all-as-counselled applied with
   judgement, i.e. does each ruling's *intent* survive translation into this
   wording, and do the assumptions above hold?
2. **Correctness & quality** — does the applied text do what the commit
   claims; any overclaim ("verified", "swept", "live") stronger than its
   evidence; any silent scope-cut in the sweep.
3. **Completeness / harvest** — instances of the same stale classes the sweep
   should have caught elsewhere; sibling text that duplicates or now
   contradicts the applied story.
4. **Security & privacy** — mandatory, and here it is the subject itself:
   disclosure channel, supply-chain pins, scanner trust roots. Attack the
   design an adopter inherits. `/security-review` reach is assessed in the
   verdict: this is a landed markdown delta, so if the scanner cannot be
   aimed at it, the mechanical floor is discharged in one explicit line with
   grounds — the substantive lens still runs in full.

## Proofs to re-run (widest scope; re-run, never take)

- `python3 -m unittest discover -s tools` (expect ~330; report count)
- `node --test instruments/*.test.js` (report count)
- The five scanners, exit codes checked explicitly, invocations lifted from
  `tools/pre-commit.sample` / `tools/README.md`: secretscan, leakscan,
  linkscan, reviewscan, sizescan `--check`
- `gh api repos/mike548141/atelier/private-vulnerability-reporting`
  (read-only) — the SC1 live claim
- Pin-bump recipe: annotated-tag dereference parsed/exercised where checkable
- Repo-wide grep for the swept "deferred" phrasing; `floor.yml` read against
  the new fetch-at-CI prose
- CI action SHA-pins re-checked where the doctrine references them

---

# Verdict — PASS-WITH-FINDINGS (0 MAJOR · 1 minor · 1 LOW · 1 nit)

- **Stamped**: 2026-07-23 03:27 UTC (findings written before any deferred
  material was opened; reconcile section appended after, separately stamped)
- **Cycle status**: this pass returns **no MAJOR finding**, so per
  `REVIEW.md`'s close rule the security-canon cycle is **terminal** — what
  remains below is decided into the backlog by the principal (rule 3; this
  application carries rule-4 status, so every finding is counsel, and this
  reviewer applies nothing).

## Spawn provenance (repeated verbatim from the brief)

This review was spawned by a non-author taker session that the principal (Mike)
opened and pointed at the review queue on 2026-07-23; neither the doctrine's
author, any prior verdict's author, nor the applier session (or its subagents)
started or instructed this review or this reviewer; the taker authored none of
the chain and gave the reviewer refs only.

## `/security-review` reach — discharged with grounds

The harness scanner reviews *pending* changes and excludes markdown
documentation by file class; this subject is a landed, clean-tree delta of
four markdown files and one shell-comment hunk, so there is nothing the
scanner can genuinely be aimed at — its absence here weighs as nothing either
way. Lens 4 ran substantively instead (below and SCA1/SCA2): the subject *is*
a security surface — disclosure channel, supply-chain pins, scanner trust
roots — and was attacked as design, not scanned as code.

## What I re-ran, with results

| Proof | Invocation | Result |
|---|---|---|
| Python tool suite | `python3 -m unittest discover -s tools` | ✅ **Ran 331 tests — OK** |
| Node instrument suite | `node --test instruments/*.test.js` | ✅ **150 pass, 0 fail** |
| secretscan | `python3 tools/secretscan.py --root . .` | ✅ clean, exit 0 (checked explicitly) |
| leakscan | `python3 tools/leakscan.py --root . .` | ✅ clean (structural + local), exit 0 |
| linkscan | `python3 tools/linkscan.py --root . .` | ✅ clean, exit 0 |
| reviewscan | `python3 tools/reviewscan.py --root . .` | ✅ clean (3 post-boundary records carry a review line), exit 0 |
| sizescan | `python3 tools/sizescan.py --check --root . .` | ✅ exit 0 — one size-*advisory* (ROADMAP.md 463 lines), 0 cold-content, 0 harvest-integrity; advisory never fails `--check`, per its own doctrine |
| SC1 live claim | `gh api repos/mike548141/atelier/private-vulnerability-reporting` | ✅ `{"enabled":true}`, exit 0 — the commit's "API-verified" claim reproduces at HEAD |
| SC3 recipe, lightweight branch | `gh api repos/actions/checkout/git/ref/tags/v5` | ✅ `.object.type` = `commit`, SHA = `fbc6f399…` — matches the floor pin exactly; same for setup-python v6 (`ece7cb06…`) |
| SC3 recipe, annotated branch | `git/git` tag `v2.45.0`: ref call → type `tag`; then both dereference commands as written | ✅ `gh api …/git/tags/<sha> --jq .object.sha` and `git ls-remote --tags <url> 'v2.45.0^{}'` return the **same** commit `786a3e4b…` — the recipe works verbatim on both tag kinds |
| All doctrine-referenced action pins | tag↔SHA re-resolved for all five distinct pins across `ci.yml`, `floor.yml`, `ci-python.yml`, `ci-static.yml` | ✅ every pin's trailing tag comment still resolves to its pinned SHA (checkout v4/v5, setup-python v5/v6, setup-node v4) |
| SC2 sweep, stale phrasing gone | repo-wide grep: `deferred supply-chain`, `scanner distribution`, `cannot do this yet`, `only scan gate`, `no atelier path`, `vendor / fetch / publish` | ✅ zero hits in live doctrine/tooling; remaining hits are dated records only (CHANGELOG entry under a 2026-07-10 heading, sessions/reviews/ROADMAP-DONE) — records narrate history and are correctly unswept |
| SC2 replacement matches reality | `floor.yml` read in full against the new prose in SECURITY.md / tools/README / pre-commit.sample; `bafeaa3` confirmed as the commit that shipped floor.yml | ✅ the fetch-at-CI description matches the shipped template (checkout-beside, run from atelier's tree, scoped to `repo/`); one hedging gap → SCA2 |
| HEAD attribution | `git diff --stat c27189e 9df3510` over the five delta files; `git show bbaec81` | ✅ only REPO-STANDARD.md moved after the subject, in a disjoint step-1 signing hunk — all SC text at HEAD is `c27189e`'s |

## Findings

### SCA1 — minor — the named trust asymmetry understates its cost to an adopter

- **Claim**: SC5's applied text names the atelier@main scanner-trust asymmetry
  but states only the benefit ("newest detection is safest"), never the
  inherited grant: **anyone with write to atelier's `main` gets arbitrary
  code execution in every child's floor job** — including reading a *private*
  child's checked-out tree, and writing `$GITHUB_ENV` to influence later
  steps. That is the very consequence the sibling trust-list rationale states
  explicitly for its own surface.
- **Evidence**: `tools/README.md` (the new SC5 bullet, ~lines 112–117):
  "Child CI trusts `atelier@main` for scanner code — by design… newest
  detection is safest… Detection floats, trust roots pin — the asymmetry is
  deliberate, named here where the residuals live." Contrast
  `docs/build/templates/workflows/floor.yml` (~line 183): "a floated trust
  root would let **anyone with write to atelier's main mint trust for every
  child**" — followed by "(Contrast the scanners above, which deliberately
  float main…)". The doctrine thus states the attacker capability for the
  pinned surface and goes silent on the identical actor for the floated one;
  a residual list exists precisely to state what an adopter inherits, at true
  strength (00-APEX: never a claim weaker than the risk). The bound is real —
  `permissions: contents: read`, no secrets in the scanner steps, the `ref:`
  pin escape hatch is offered — but the bound is what should be *written*,
  not inferred.
- **Counsel**: one clause in the tools/README residual bullet (mirrored or
  pointed-to in floor.yml's WHY header): the float is also a standing
  code-execution grant — a write to atelier's `main` runs in every child's
  floor job, bounded by `contents: read` and no step secrets; a child wanting
  the opposite call pins `ref:` exactly as the trust list pins. Not MAJOR:
  the trust itself is named plainly, the design is deliberate and ruled, the
  blast radius is bounded, and an alert reader of floor.yml can assemble the
  consequence — the defect is strength-of-statement, not concealment.

### SCA2 — LOW — "scanner fixes reach a child's CI automatically" is true only of the default configuration

- **Claim**: SECURITY.md's SC4 uptake split states the scanner-fix path
  categorically, but the floor template itself sanctions two configurations
  that break it: the commented `ref:` pin ("Want reproducible CI instead?…")
  and the adopter-fork instruction ("Adopters: point `repository:` at your
  own atelier fork") — a fork's `main` does not advance when atelier's does,
  so for a fork-pointing adopter scanner fixes also arrive only on a
  deliberate sync.
- **Evidence**: `SECURITY.md` lines 56–60 vs
  `docs/build/templates/workflows/floor.yml` lines 13 and 19–21.
- **Counsel**: hedge the sentence to the default — e.g. "scanner fixes reach
  a child's CI automatically **in the floor template's default
  configuration** (floating `main`; a pinned `ref:` or a fork takes them on
  deliberate sync instead)". LOW: the claim is accurate for the shipped
  default and for every child of mike548141/atelier.

### SCA3 — nit — REPO-STANDARD's PVR verification names the command but not the observation

- **Claim**: the REPO-STANDARD bullet says "verified with `gh api
  repos/<owner>/<repo>/private-vulnerability-reporting`" without the expected
  output; the template's seed comment gives it (`→ enabled: true`).
  Verification means observing the value — the doctrine text a scaffolder
  follows should say what "took" looks like.
- **Evidence**: `docs/build/REPO-STANDARD.md` lines 85–89 vs
  `docs/build/templates/SECURITY.md` lines 8–11.
- **Counsel**: append `→ enabled: true` to the REPO-STANDARD command mention.

## Lens summaries

1. **Approach & assumptions** — the accept-all application translated each
   ruling's intent with judgement, not transcription: SC1 lands as a
   seeding-act obligation in both the standard and the template (the class
   fix, not just the instance); SC2 replaces the stale notes with prose that
   matches the shipped floor.yml mechanics; SC3's recipe is correct on both
   tag kinds (proven live); SC4's two-speed split is the right model of the
   shipped machinery (hedge owed, SCA2); SC5 names the asymmetry where the
   residuals live (strength owed, SCA1). No assumption from my attack surface
   broke.
2. **Correctness & quality** — every live claim in the commit message
   reproduced under re-run: PVR `enabled:true`, floor.yml shipped at
   `bafeaa3`, all pins resolve, the recipe executes verbatim. No overclaim
   found beyond SCA2's categorical sentence.
3. **Completeness / harvest** — the sweep caught every live instance of the
   stale class (grep-proven zero residue outside dated records); ROADMAP
   carries no stale scanner-distribution item; the five files now tell one
   story (uptake split, PVR-at-seeding, pin discipline, fetch-at-CI).
   Observation, no finding: the child CI templates pin older action
   generations (checkout v4 / setup-python v5) than ci.yml and floor.yml
   (v5 / v6) — all pins valid and tag-true, skew predates this delta.
4. **Security & privacy** — run substantively as the subject itself; the two
   real findings (SCA1, SCA2) both live here. The disclosure channel is now
   verified end-to-end (policy → enabled switch → API proof, and the template
   makes the switch part of seeding). The mechanical-floor discharge is
   stated above.

---

## Reconcile — deferred material opened after the findings above were durably written

*Stamped 2026-07-23 03:28 UTC. Opened only now:
`docs/reviews/2026-07-23-0222-security-canon-abce-cold.md` (the prior verdict
and its Decisions stamp). Nothing else from the deferred list was needed or
read.*

### Ruling-by-ruling faithfulness

| Ruling | Decision stamp | Did it reproduce at HEAD? | Faithful to counsel? |
|---|---|---|---|
| SC1 (MAJOR) | [fixed] — instance: PVR enabled + API-verified; class: enable-and-verify part of the seeding act | ✅ PVR re-verified `enabled:true` by this reviewer; REPO-STANDARD bullet + template seed comment both carry the obligation with the verify command | ✅ Verbatim to counsel; the template goes one better by stating the expected observation (`→ enabled: true`) — SCA3 asks REPO-STANDARD to match it |
| SC2 (minor) | [fixed] — three stale notes swept to fetch-at-CI | ✅ All three swept; repo-wide grep finds zero live residue (dated records correctly untouched); `bafeaa3` confirmed as floor.yml's shipping commit | ✅ The reviewer's "decided" reading was confirmed and applied as counselled |
| SC3 (LOW) | [fixed] — recipe dereferences annotated tags | ✅ Both dereference commands exercised live on a real annotated tag (git/git v2.45.0): identical commit SHA from `gh api …/git/tags/<sha>` and `ls-remote '<tag>^{}'`; lightweight branch re-proven on all five action pins | ✅ The `.object.type` clause and both alternatives landed exactly as counselled |
| SC4 (LOW) | [fixed] — uptake sentence split two-speed | ✅ The split is in SECURITY.md as stamped | ✅ Faithful to the counselled split. **Overlap**: my SCA2 sharpens the *counsel itself* — the counselled sentence inherits a categorical "automatically" that the floor's own `ref:`-pin and fork options qualify. Not applier drift; the applier applied the ruling as given |
| SC5 (LOW) | [fixed] — asymmetry named in the residual list | ✅ The bullet is in tools/README's residual section, rationale pointer to floor.yml, trust-list contrast included | ✅ Faithful — the counsel asked to *name* the asymmetry and it is named. **Overlap**: my SCA1 is the next increment beyond the ruling (state the inherited code-execution grant and its bound, not only the asymmetry), not a drift from it |
| SC6 (nit) | [no change needed] — SA9 already swept | ✅ Re-proven: grep for "artifact" in tools/README.md + REPO-STANDARD.md returns zero hits at HEAD | ✅ No action was the ruling; none was taken |

### Anything the application drifted?

No. Every [fixed] stamp reproduces mechanically at HEAD; no ruling was
narrowed, extended, or reworded beyond its counsel; SC5's applied bullet and
SC2's replacement prose match the prior verdict's counselled shape closely
enough to be near-verbatim. The prior verdict's re-run table and mine agree
everywhere they overlap (five pins, both suites, five scanners, PVR — with
the PVR value flipped from `false` to `true` exactly as the decision stamp
claims happened pre-application). My three findings divide cleanly: SCA1 and
SCA2 are refinements *on top of* rulings faithfully applied (both on the
counselled wording, neither on the applier's execution of it); SCA3 is a new
harmonisation nit between the two files SC1 touched.

### Cycle status, restated after reconcile

No MAJOR in this pass; the MAJOR count fell 1 → 0. Per REVIEW.md's close
rule the security-canon review cycle **closes as terminal** — the findings
above go to the principal as backlog counsel, and this application does not
spawn another full ceremony.

---

*Reviewed 2026-07-23, brief 03:22 UTC → findings 03:27 UTC → reconcile
03:28 UTC · cold rule-4 application pass, read-only, one file written (this
one). Findings SCA1–SCA3 are the principal's to decide (REVIEW.md rules 3–4);
the reviewer applied nothing.*

---

## Decisions (stamped 2026-07-23, the applying session)

Mike ruled all three **accept as counselled**, walked through one-by-one in
plain language with impacts. Applied by a session that authored neither the
doctrine, the prior verdicts, nor the applications under review. No MAJOR in
the pass ⇒ **the security-canon cycle is terminal and closes on this
landing** (REVIEW.md termination rule; no further pointer).

- **SCA1 [fixed]** — the residual bullet now states the float's standing
  grant at strength (write to atelier `main` = code in every child's floor
  job) with its bound (`contents: read`, no step secrets) and the `ref:` pin
  escape named.
- **SCA2 [fixed]** — the uptake sentence hedged to the floor template's
  default configuration; pinned/forked children take fixes on deliberate
  sync.
- **SCA3 [fixed]** — `→ enabled: true` appended to REPO-STANDARD's PVR
  verify command, matching the template.
