# Cold pass — the EP application (enforcement-is-called-not-copied, applied)

**Pass type:** code cold pass (rule-4 queued — an application of ruled
decisions; the applier's judgement produced the delta).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04).

## Spawn provenance

- **Author of the work under review:** the session that landed the delta on
  2026-08-06, and the session that landed the 2026-08-09 follow-up on the same
  surfaces (see *What the work is*).
- **Who spawned this review:** the principal (Mike), in a session he opened on
  2026-08-09 and pointed at the review queue — rule 4's worked example. His
  words: *"Please do any review work that waiting."*
- **Author's non-involvement:** the taker session authored no part of this
  delta, was neither started nor instructed by the authoring sessions, and
  wrote this brief as the non-author taker. Rule 4's single criterion is met,
  and the tier was checked at selection.
- **Orchestration shape:** the review runs under an orchestrator holding a
  context partition — the intent-record references are withheld from this brief
  and handed to the reviewer only after its own findings are durably written.

## What the work is

Code and templates landed 2026-08-06 plus a 2026-08-09 follow-up on the same
surfaces, reviewed at HEAD:

1. [`tools/floor.py`](../../tools/floor.py) and
   [`tools/floorfleet.py`](../../tools/floorfleet.py).
2. [`tools/pre-commit.sample`](../../tools/pre-commit.sample) and
   [`.githooks/pre-commit`](../../.githooks/pre-commit).
3. [`.github/workflows/floor.yml`](../../.github/workflows/floor.yml) and
   [`.github/workflows/ci.yml`](../../.github/workflows/ci.yml).
4. [`docs/build/templates/workflows/floor.yml`](../build/templates/workflows/floor.yml)
   and
   [`docs/build/templates/CONTRIBUTING.md`](../build/templates/CONTRIBUTING.md).
5. [`docs/decisions/0008-enforcement-is-called-not-copied.md`](../decisions/0008-enforcement-is-called-not-copied.md)
   — Decision 6 and the Consequences control clause.
6. The four test files — the suite grew 1164 → 1178 across the application.
7. The `CHANGELOG.md` entry (2026-08-06), and the 2026-08-09 follow-up:
   `tools/floor.py` validate + `tools/test_floor.py`, the legacy-spelling
   exemption removed for never-softened scanners (delta widened per the
   landing-commit rule).

## Scope

Widest the work admits: whether the application matches the decision it
applies (ADR 0008 is in the delta and is readable now — the *verdict* that
ruled on it is not, until phase 2), the design of the called-not-copied
wiring, the code, the hooks, the workflows, the templates other repos will
copy, the tests, and live behaviour. **Non-goals:** none narrows the delta.
The reviewer does not decide findings' dispositions; residue joins the
principal's ruling round per house practice.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. Does the wiring actually make enforcement *called*, not copied — or
   does any surface still carry a copy that can drift?
2. **Correctness & quality** — run the suites; exercise the hook and the
   floor validate path live; check both workflow files do what the ADR's
   control clause says.
3. **Completeness / harvest** — which surfaces that call or copy enforcement
   were missed; do the two templates and the live workflows agree with each
   other?
4. **Security & privacy** — mandatory, at code altitude: the hook and
   workflows execute on every commit and push — check what they run, what
   they trust, and what a malicious or malformed tree could make them do.
   atelier is PUBLIC — the templates ship to adopters; check what they carry.
   The house security scanner reads pending diffs; this is a landed-delta
   review, so state the reach case that applied.

## Re-run obligation

Re-run, do not read, at least: the full suites (house invocations in
[`.githooks/pre-commit`](../../.githooks/pre-commit)), the suite-count claim
1164 → 1178 at the landing commits, `tools/floor.py` validate on the current
tree, and the pre-commit hook's behaviour on a scratch staged change (in the
scratchpad or read-only — never leave the repo dirty).

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the intent-record refs are orchestrator-held under the rule-1 context partition, handed over only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/sessions/`, and every prior verdict
in `docs/reviews/` — this cycle has prior verdicts, so the bar binds hard. The
intent record (the prior pass and the ruling the application applies) is held
by the orchestrator and will be provided on receipt of your committed
findings. Reconcile after, never anchor before.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `AP` — `EA` and `EP` are taken by prior
passes in this store) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then report; the deferred
references arrive; append a reconcile section and finalise.

---

# Verdict — phase 1 (deferred references not yet read)

**Pass type:** code cold pass (rule-4 queued — application of ruled decisions).
**Tier:** Fable (claude-fable-5) — checked at selection against the 2026-08-04
ruling.

## Provenance, repeated

The author of the delta is the session that landed 38e8bcf…166fa00 on
2026-08-06 (UTC) and the session that landed 4cab670 on 2026-08-09. This
reviewer authored no part of it, was neither started nor instructed by the
authoring sessions, and was spawned by the principal's 2026-08-09 review-queue
session under an orchestrator holding the context partition: the intent-record
references were withheld and remain unread as this verdict is written. Rule 2's
bar was honoured: no prior verdict, no `docs/ROADMAP-DONE.md`, no
`docs/sessions/` file was opened; `docs/ROADMAP.md` was not opened (the
follow-up commit's ROADMAP hunk was excluded from the diff read). One
incidental exposure to disclose: running the floor live printed sizescan's
size-advisory line naming `docs/ROADMAP.md` and its line count — a number, no
content.

## Load-bearing assumptions, named first

1. "Called, not copied" means one registry with call sites carrying no policy —
   and no surface still holds a list that can drift.
2. Adopters can actually reach the canonical enforcement (hook: a local atelier
   clone via `hooks.atelierTools`/`ATELIER_TOOLS`; CI: a checkout of
   `atelier@main`), and the reach mechanism's trust is named, not assumed.
3. The suite growth genuinely exercises the new wiring.
4. The two live workflows, the two templates, and ADR 0008 agree with each
   other and with the code.
5. The hook still fails closed on every missing-input path after the rewiring,
   including the bite-now change to the legacy spelling.

Assumption 1 largely holds and is the delta's real achievement — but it fails
in one place *inside the delta's own files* (AP2): the softenable set exists as
three prose copies, one of which contradicts the registry today. Assumption 2
is where the MAJOR lives (AP1): the reach mechanism's safety rests on a control
the record now names — and a live read shows the control is not in force.

## Re-run obligations — all discharged by re-running, none by reading

Everything ran in a scratch clone of this worktree (`scratchpad/ap-clone`);
this tree was never dirtied and no git mutation ran here.

| Claim / obligation | Result |
|---|---|
| Python suite at HEAD (`unittest discover -s tools`) | ✅ Ran 1210, OK |
| Node suite at HEAD (`node --test instruments/*.test.js`) | ✅ 207 pass, 0 fail |
| floor / floorfleet / signscan `--selftest` | ✅ all ok (13 scanners) |
| Registry-driven selftest loop (ci.yml's awk form) | ✅ all 13 exit 0 |
| Suite count at e3b94c1 (parent of 38e8bcf) | ✅ Ran 1164, OK |
| Suite count at 0f45771 (application's completing commit) | ✅ Ran 1178, OK |
| Suite count at 8642a07 (follow-up's parent) | ✅ Ran 1200, OK |
| Suite count at 4cab670 (follow-up) | ✅ Ran 1202, OK |
| `floor.py --plane ci --root .` at HEAD | ✅ exit 0; three render states live; secretscan's advisory count (21) carried on the board |
| `floor.py --plane hook --root .` at HEAD | ✅ exit 0; leakscan full cover (`structural + local`) on this machine |
| `--json` mode | ✅ stdout pure JSON, 13 results, states as designed |
| Hook, live in a scratch child repo (tracked shim + `core.hooksPath` + `hooks.atelierTools`) | ✅ clean commit passes |
| Hook: staged AWS-shaped secret | ✅ blocks, exit 1, remedy printed |
| Hook: `ATELIER_TOOLS` at an empty dir | ✅ blocks fail-closed with the three-line remedy |
| Hook: legacy bare-list `scope.leakscan` (the bite-now ruling) | ✅ blocks as a config error naming the reasoned spelling |
| Hook/sample identity | ✅ byte-identical (and test-pinned) |

The suite-count claim is therefore **true as stated at the landing commits**:
1164 → 1178 binds to e3b94c1 → 0f45771. The same-day continuation on the same
surfaces (be0667e, 166fa00) took the suite to 1200 and the follow-up to 1202 —
the brief's figure under-describes the delta's own test growth (AP8).

**House security scanner reach case:** this is a landed-delta review from a
read-only tree; `/security-review` reads pending changes and there are none,
so it could not be genuinely aimed at the work. Discharged on those grounds;
in its place the security lens below was run by hand at both altitudes, with
live adversarial probes (planted secret, escaping scope, missing tools,
missing terms, legacy spellings) and the CI/CD threat catalogue consulted for
the work's class.

## Lens 1 — approach & assumptions

The design is right, and the application is faithful to it. Every enforcement
surface now carries a call, not a copy: the tracked hook names no scanner, the
child caller names no scanner, atelier's own CI runs the floor in one
registry-driven step, and the two deliberate out-of-registry steps (signscan,
stampscan) each state their grounds where they run. The warn-only render state
is derived from the entry (argv flag or `warn_only`, pinned to each other both
ways by the selftest), never listed beside it — the right shape.

Two approach-level defects survive, both findings below: the registry's own
*prose* still carries vendored policy that has drifted (AP2), and the safety
of the floating `@main` — the assumption the whole propagation design leans on
— is asserted by the new Consequences clause against controls that a live read
shows are not in force (AP1).

## Lens 2 — correctness & quality

Everything the delta claims to do, it does — verified live, not read: the
bite-now rule blocks exactly the legacy-on-boundary case and spares atelier's
own softenable legacy lists (its config parses at HEAD); EP9's interpreter
guard sits ahead of the run line; EP4's two-edit pin doctrine appears at both
points of use and floorfleet's `pinned` detail says the true thing; EP5's
`--root repo` is in the reusable selftest loop and the local-check skip is in
both workflows with matching grounds; EP10's prove-it command leads with
`core.hooksPath`; exit codes are untouched by the render change
(`Result.failed` includes warn-only, and the selftest pins an erroring
warn-only check as blocking). The ADR's control clause is *stated* correctly
in both workflow files' terms (SHA-pinned third-party actions, least-privilege
`contents: read`, pinning documented as two edits) — but the clause's central
claim fails a live check (AP1). One honesty defect stands inside the delta's
files: the docstring/ADR/registry disagreement over sizescan (AP2).

## Lens 3 — completeness / harvest

The two templates and the two live workflows agree (test_templates pins the
thin caller, the reusable workflow's shape, the parent loop's local-check
skip, and CONTRIBUTING's EP10/EP1(b) content — all green). Surfaces checked
for missed copies: sibling CI templates (ci-python, ci-static — no floor
copies), the template tree (no `run_scan` lines anywhere), the decisions
README (prose only). Residue: CONTRIBUTING's parenthetical never-softened list
is a prose copy of registry policy that no test pins to `advisory is None`
(folded into AP2); the ci-static template's `check_links.py` step runs outside
the local seam Decision 6 built, so that child class's own gate stays
invisible to floorfleet (AP6).

## Lens 4 — security & privacy

Code altitude, driven live where possible: no shell anywhere in the run path
(argv exec, fixed interpreter); local `run` membership enforced lexically and
resolved (symlink escape blocked — suite-pinned); scope escape blocked on both
halves; workflow-command injection encoded at the point of interpolation
(`_wc`, grouping routed off stdout under `--json`); child-authored config text
control-stripped at one seam shared by floor and board; third-party actions
SHA-pinned in all four workflow files; both workflows least-privilege.
Fail-closed held on every path probed: missing floor.py, missing scanner,
missing interpreter (code + suite), unparseable config, unknown scanner,
unsoftenable advisory, escaping scope, missing term list (suite-pinned; a
resolver-fallback caveat in AP4).

Design altitude: the delta's own threat statement (EP7) names the right threat
— and the live read against it is the MAJOR below. Privacy: the term list
stays machine-local on every surface, CI is structural-only and says so on the
board rather than claiming full cover; templates ship no personal data;
nothing in the delta widens collection.

## Findings

**AP1 — MAJOR (security, design altitude): the named control for the floating
`@main` is not in force.** The Consequences clause this delta added (EP7)
states the design "rests entirely on the boundary claim, and the boundary is
who can write atelier's `main`: branch protection, signed commits, and review
on the registry are the control." Live reads, 2026-08-09:
`gh api repos/mike548141/atelier/branches/main/protection` → 404 "Branch not
protected"; `rules/branches/main` → `[]`. There is **no branch protection and
no ruleset on `main`**. Of the clause's three legs, one is absent, one is
warn-first everywhere it is checked (signature verification reports and never
blocks, on both the parent and child planes), and one is post-hoc (registry
changes land directly on `main` under the standing autonomy grant; review
follows landing). So the record asserts a control the estate does not
currently have, on the surface whose compromise the same clause names as
"arbitrary code running in every child's CI" — and no instrument checks it:
floorfleet enumerates whether children *call* the floor, and nothing
enumerates the boundary that makes calling safe. The clause's own standard
("named, checkable control") is the standard it fails. Severity MAJOR;
recurrence-prevention step owed with the fix (the security-finding shape
REVIEW.md requires): either put the control in force and make its state
machine-checked (a parent-row check reading branch-protection/ruleset state,
red when absent — the same absences-raise-their-hands doctrine floorfleet
already applies to children), or re-word the clause to the truth: current
state, aspirational control, dated plan. Which — and whether solo-operator
economics change the answer — is the principal's call.

**AP2 — MODERATE: the softenable set is vendored prose, and one copy has
drifted.** The registry says sizescan and publishscan carry advisory forms
(`advisory=` non-None; the selftest asserts "sizescan can re-baseline"), and
`Config.validate` will honour a child's `advisory.sizescan` declaration. But
floor.py's own module docstring says the integrity scanners "(linkscan,
reviewscan, sizescan) have no advisory form here… a botched harvest [is] not
[a] re-baselining problem" and that "only the prose-hygiene checks (datescan,
wrapscan, spellscan) carry one" — wrong twice at HEAD (sizescan, publishscan).
ADR 0008 Decision 2 makes the same claim ("the boundary and integrity
scanners have no advisory form at all"), and Decision 6's closing clause
re-affirms Decision 2 unchanged. CONTRIBUTING's never-softened list
(secretscan, leakscan, linkscan, reviewscan, licenscan) agrees with the code
and contradicts the ADR. Net: a child *can* soften the harvest-integrity gate
while the decision record says it cannot — either the registry wrongly offers
the form or the doctrine overstates, and none of the three prose lists is
test-pinned to `Scanner.advisory is None`. This is the "list beside the
registry" shape the module's own warn-only work refused, in the same file.
Both the code and the ADR are in this delta; the ADR text is doctrine, so
disposition is the principal's.

**AP3 — minor (security hardening): `${{ inputs.sign-boundary }}` is
interpolated inline into two `run:` scripts** in the reusable floor.yml
(machine-key and GitHub-server signature steps). The hardening corpus the EP7
clause leans on treats inline expression interpolation in `run:` as the
script-injection entry point and prescribes routing through `env:`. The input
comes from the calling repo's own workflow file, so the trust domain is the
caller's — but this file is the estate's shipped pattern, and atelier's own
ci.yml already does it right (`SIGN_BOUNDARY` via `env`). One-line fix per
step.

**AP4 — minor: a set-but-missing `ATELIER_LEAKSCAN_TERMS` silently falls back
to the default list.** Driven live: with the env var pointing at a nonexistent
file, the hook-plane commit passed with "structural + local" cover from the
default `~/.claude/leakscan-terms.txt`. `resolve_terms_path` skips any
candidate that does not exist, so a mistyped dedicated-list path yields
silently narrower cover than intended on exactly the plane EP3 hardened
against silent degradation. `leakscan.py` is adjacent to, not named in, this
delta — but the hook's full-cover claim rests on it. Suggested shape: an
explicitly set path that does not resolve is an error, not a fall-through.

**AP5 — note: ADR Decision 1's "~30-line caller" is stale** — the shipped
caller is 97 lines (the caller itself is ~10; the rest is deliberate doctrine
comment). Nothing load-bearing; a reader using the figure as a conformance
sniff test measures wrong.

**AP6 — note: the ci-static template's `check_links.py` gate runs outside the
local seam**, as a bespoke CI step — so a static-site child's own gate is
exactly the estate-invisible check Decision 6 built a home for. A future
template revision could declare it via `local` and let it show on the board.

**AP7 — note: the selftest loop's awk parse of `--list` is
column-positional.** A local-check name containing whitespace shifts fields;
the failure direction is closed (a missing `atelier/tools/<word>.py` reds the
step, argv has a fixed prefix, no shell evaluation of the name), so this is
robustness, not a hole. `_load_local` accepts any control-stripped string as a
name; a character-class restriction would close the cosmetic gap.

**AP8 — note (brief framing, attackable per rule 1): the suite-count claim
under-describes the delta.** 1164 → 1178 is true and was verified at
e3b94c1 → 0f45771, but the delta as the brief itself defines it (all
2026-08-06 surfaces plus the follow-up) grew the suite 1164 → 1200 → 1202.
Claim verified; framing narrow.

## Overall

**PASS-WITH-FINDINGS — 1 MAJOR, 1 MODERATE, 2 minor, 4 notes.**

The application is faithful, tested, and honest about what it does; every
re-run reproduced, and every fail-closed path probed held. The MAJOR is not in
the code: it is the gap between the delta's own security record and the live
state of the control that record names. Per REVIEW.md, no disposition is
decided here; all findings join the principal's ruling round, and the MAJOR
means this pass does not close the cycle.

## Follow-up checklist

- [ ] AP1 — principal's ruling: put the `main`-protection control in force
      and machine-check it, or re-state the EP7 clause to current truth with a
      dated plan. Carries a severity and a recurrence-prevention step
      (security finding).
- [ ] AP2 — principal's ruling: sizescan (and publishscan) softenability —
      align registry, docstring, ADR Decision 2 and CONTRIBUTING; pin the
      never-softened list to `Scanner.advisory is None` with a test wherever
      prose names it.
- [ ] AP3 — route `sign-boundary` through `env:` in the reusable workflow's
      two signature steps.
- [ ] AP4 — make an explicitly set, non-resolving `ATELIER_LEAKSCAN_TERMS` an
      error rather than a silent fall-through.
- [ ] AP5 — refresh Decision 1's caller line-count figure (or drop the
      number).
- [ ] AP6 — consider declaring the ci-static link gate through the local seam
      in a future template revision.
- [ ] AP7 — consider a name character-class check in `_load_local`.
- [ ] AP8 — none (recorded for the reconcile round).

## Reconcile — after reading the deferred references (2026-08-09)

Read only after the verdict above was durably written: (1) the prior cycle's
verdict, `docs/reviews/2026-07-26-2215-adr0008-enforcement-propagation-cold.md`
(EP1–EP10, 3 MAJOR · 5 minor · 1 LOW · 1 nit after its own reconciliation);
(2) `docs/ROADMAP-DONE.md` § "The EP application". Nothing else was opened —
one exposure to own: the read window for that section overran a few paragraphs
into the opening of the next section ("The floor-render batch"), which
describes work inside my reviewed delta; its content agreed with what I had
already established from the tree and changed nothing above. The
withdrawn-directory ban was honoured throughout; the withdrawn Opus pass is
known to me only as the quarantine notice both deferred surfaces carry.

Nothing above is revised. All additions below are marked post-reconcile.

### The prior cycle's decisions and [fixed] claims, verified at HEAD

Every EP ruling the application claims to have landed verifies live or in the
suite — none was taken on the record's word:

- **EP1(b)** (flags reason on unsoftenable checks): verified in phase 1 —
  code, suite, and the bite-now follow-up driven live in a scratch repo.
- **EP1(a)/EP2** (scope/flags/docs read out estate-wide): the 🔎/🔧/📁 board
  lines exist in `floorfleet.render` and are suite-pinned; the sentence EP2
  called false is now true. The ruling chose visibility over refusal for a
  reasoned declaration's residual cover-shrink; that is the remedy in force,
  and the declared-but-unreadable state EP1 attacked is closed on the routes I
  probed (non-resolving scope on an unsoftenable check blocks; outside-repo
  and symlink scopes block; a reasoned flags positional is visible on the
  board).
- **EP3** (hook-plane full cover asserted): `--require-terms` is in the hook
  template; full cover confirmed live on this machine, and the no-list block
  is suite-pinned (`test_a_clone_with_no_term_list_blocks_rather_than_half_
  scanning`). The counsel's fallback ("a terms column on floorfleet") was
  also built — the board's term-list footer.
- **EP4, EP5, EP6, EP8, EP9, EP10**: all verified in phase 1 (two-edit pin
  doctrine at both points of use and the corrected `pinned` wording; `--root
  repo` plus the decided local-skip in both workflows; Decision 6; the
  trigger-shape concession in floorfleet's docstring; the interpreter guard;
  `core.hooksPath` first in the prove-it block).
- **Post-reconcile addition:** the ROADMAP-DONE entry left one asymmetry "for
  the application's own cold pass" — `scope`'s older error message did not
  name the working form while the new `flags` one did. Verified resolved at
  HEAD: the 2026-08-09 follow-up (4cab670) added the working-form remedy to
  the `scope` error too. The item left for this pass was already closed by
  the delta under review; recorded so the ruling round need not chase it.
- The record's own verification figures reconcile exactly with my
  measurements: "suite 1164 → 1178 exit 0" was taken at the five-commit
  application worktree, matching my 1164 at e3b94c1 and 1178 at 0f45771.

### AP1 against the EP cycle's standing MAJORs

The queue pointer records the cycle as open on the prior pass's three MAJORs
(EP1, EP2, EP3). **AP1 is none of those restated.** All three were about
declared cover being smaller than it read; their substance verifies as closed
at HEAD (above). **AP1 is a descendant of EP7** — a minor in the prior cycle.
EP7's counsel was: name the control that makes floating `@main` safe
("branch protection, signed commits, review on the registry"), converting an
accepted risk "into a named, checkable one". The application added exactly
that clause. AP1 is the first check of the named control, and it fails: no
branch protection, no rulesets, signing warn-first, registry review post-hoc.
The escalation from minor to MAJOR is not severity drift on the same finding —
EP7's defect was an *unnamed* control (a record gap); AP1's is a security
record now *asserting* a control that is not in force, which is the honesty
class EP2 defined ("a claim about a sibling tool's behaviour is either
verified or not made"), applied to the estate's widest-blast-radius surface.
In that sense AP1 is EP2's standard and EP7's subject, meeting for the first
time — genuinely new as a finding, with clear lineage.

### Agreements, divergences, and shared blind spots

- **Agreement in method and in verdict shape.** The prior pass's "what held
  under attack" list re-verified here almost line for line: fail-closed on
  every driven route, the staged-path class shut, the seam only adding,
  enumeration fail-safe. My phase 1 found the same strengths independently.
- **Agreement on the seeded trade.** The prior pass answered ADR 0008's
  floating-`@main` question "right for a floor, provided the control is
  named". AP1 does not reopen that answer; it tests the proviso.
- **Divergence / shared blind spot (post-reconcile marking on AP2).** The
  prior pass cited the docstring's "boundary and integrity checks have no
  advisory form" as a design fact and cited the selftest beside it — but the
  selftest asserts sizescan *can* re-baseline, and the registry gives both
  sizescan and publishscan advisory forms. The contradiction predates both
  passes (born with the module at 40c7a22) and survived the prior cycle
  unnoticed; AP2 stands unchanged, now with the note that it is a two-pass
  blind spot, which strengthens the counsel to pin the prose lists to
  `Scanner.advisory is None` rather than trust any reviewer to keep noticing.
- **AP4's lineage (post-reconcile marking).** The prior pass's EP3 probe
  drove the no-list-at-all case; the fix closed it. AP4 is the surviving
  sibling — a *set but non-resolving* `ATELIER_LEAKSCAN_TERMS` silently
  falling back to the default list. New, minor, unchanged.
- **A prior invocation note, since fixed.** The 2026-07-26 pass warned that
  floorfleet discovers nothing when run from a `.claude/worktrees/` checkout;
  HEAD's `main_checkout`-based discovery (TA7) resolves it. Outside my
  delta's core but verified in the code read; no finding.
- **Delta boundary, for the record.** The 2026-08-06 work comprised two work
  items with separate rule-4 pointers — the EP application (five commits) and
  the floor-render batch (be0667e, 166fa00). My brief folded both surfaces
  into one delta and my phase 1 reviewed both; the suite-count claim binds to
  the first, which is AP8's resolution. If the render batch carries its own
  queued pass, that reviewer's scope overlaps mine on those two commits —
  a coverage overlap, not a gap.

### Post-reconcile status

No finding's severity or substance changes. Counts stand: **1 MAJOR ·
1 MODERATE · 2 minor · 4 notes — PASS-WITH-FINDINGS.** AP1 classified as a
descendant of EP7 (and none of the standing MAJORs); AP2 marked a two-pass
blind spot; AP4 marked EP3's residual sibling; AP8 resolved by the record's
own figures. With a MAJOR standing, this pass does not close the cycle
(REVIEW.md's no-MAJOR close rule): the EP cycle remains open, its residue —
EP1–EP10's decided backlog plus AP1–AP8 — joins the principal's ruling round,
and the application of whatever is ruled here earns its own queued pointer.

*Verdict finalised 2026-08-09 (UTC). Reviewer: cold rule-4 pass, Fable
(claude-fable-5), spawned by the principal's review-queue session; the
deferred references were received from the orchestrator only after the
phase-1 verdict above was durably written.*

## Rulings — 2026-08-23 (structured asks, the live ruling round)

Ruled by Mike through `AskUserQuestion` (AP1 solo; AP2–AP8 batched with
the presenting session's recommendations, per his pacing ruling of the
same sitting):

- **AP1** — ruled: re-word to the truth and queue the check. An appended
  ADR 0008 amendment states the controls actually in force and names the
  aspiration, with a queued item for a machine-checked boundary; branch
  protection is not enabled (it would break the direct-to-main workflow
  the estate's sessions run on — the trade-off was put to him plainly).
- **AP2** — ruled: align the prose to the code (floor.py docstring fixed,
  ADR amendment appended) and queue the test that pins the three lists
  to `Scanner.advisory`.
- **AP3, AP4** — ruled: fix as recommended (env: routing for the
  workflow input; an explicitly-set terms path that does not resolve is
  an error, not a fall-through).
- **AP5, AP6, AP7, AP8** — ruled: no change; recorded here only.

Application follows; tags gain [fixed] as each lands verified.

**Applied 2026-08-23** (wt: ruling-round-0823): AP1 [fixed — truth
amendment appended to ADR 0008, boundary check funded at 115/180], AP2
[fixed — docstring + amendment, test-pin at 020/340], AP3/AP4 [fixed];
AP5–AP8 [no change, as ruled]. Application review queued at 160/090.
