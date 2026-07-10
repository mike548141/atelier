# Fable review — the post-method-review batch (extraction close + build/ layer + access/secrets + the scan triad)

**Status:** brief (ask on top). Verdict appended below the divider after the
review runs. This is the sweep session 15 flagged as "the standout — a strong
Fable-sweep candidate": since the `method/` layer review (`957fa08`,
`docs/reviews/2026-07-10-method-layer.md`, verdicted PASS-WITH-FINDINGS), a
coherent batch of doctrine and mechanical controls accrued **review-owed** and
was deliberately *not* built on top of — sessions 14 and 15 each stopped short of
stacking delivery on unreviewed text. This brief clears that debt in one pass.

Range under review: **`957fa08..f72031c`** (atelier HEAD at brief time). Review
**deep, not fast** — generous Fable spend is authorised; this is structural,
load-bearing doctrine plus three pre-publish safety gates whose false-negatives
leak real data. Match effort to stakes: the scans are the highest-stakes items
(a miss is an exfil event), the doctrine docs next, `REPO-BOUNDARY` the lowest.

Nicely recursive again: `REVIEW.md` itself just codified the brief-on-top /
verdict-below lifecycle at `957fa08`; this is the second run of that lifecycle,
so judge whether the lifecycle *worked* as you use it.

## What the work is (context for the reviewer)

Read the repo first: `README.md`, `docs/method/*`, `docs/build/*`,
`docs/ROADMAP.md`, `docs/SESSIONS.md` (tail), and the prior verdict
(`docs/reviews/2026-07-10-method-layer.md`). For the extraction items, read the
ros sources they were lifted from (`../ros/docs/PRINCIPLES.md`, the ros secrets
and access context) to judge the extract-vs-invent line.

**Doctrine text** (a `REVIEW.md` three-lens pass — approach lens is the point):

- **`EVIDENCE.md` §13 + §14** (the A6/A7 extraction close, `3ba6275`) — §13
  source-acquisition ladder (climb to the *cost of being wrong*; blocked ≠
  permission to promote the weak rung); §14 honest-instrument (an instrument the
  agent builds is a source; its "ok"/"applied" is a claim the apex governs —
  verified-not-attempted, silent-success-is-a-defect, "unknown"-is-required,
  known-failure-test enforces). §1–§12 were already reviewed at `957fa08`; **only
  §13/§14 are in scope here.**
- **`build/REPO-STANDARD.md`** (A10, `17ccbde`) — the create-repo standard
  extracted to doctrine: product-in-a-subfolder, size-to-type table, the standard
  file set, honest-CI, the two born/standardise processes, repo-craft
  conventions. Points up to `method/` rather than copying.
- **`build/REPO-BOUNDARY.md`** (`be0dbfd`) — is-this-a-repo by independent-
  lifecycle discriminators → standalone / component / monorepo-folder; advise
  proactively; prefer the reversible direction when ambiguous.
- **`method/SECRETS.md`** (`85d3573`) — reproducible/re-mintable as the enabling
  property; the least/JIT/short-lived triad with standing creds as tracked-debt;
  references-never-values; rotation-on-cadence bounds the undetected window.
  Closes AUTONOMY's forward-reference; completes *detect → rotate → burn-cost-is-
  minutes*.
- **`method/ACCESS.md`** (`b96c6a3`) — the safe-access-onboarding runbook: a
  seven-step ordered sequence (grant-recorded → narrowest credential + plane-split
  → store-first → read-only first ring + reconcile-or-stop → destructive-gate-
  before-power → widen-in-rings → Zero-Trust). Claims to *invent no rule*, only
  sequence AUTONOMY/DATA-PROTECTION/SECRETS/PRINCIPLES.

**Mechanical controls** (validator-run-is-most-of-the-enforcement — so **run
each `--selftest` first and report it** — then an *approach* review of the
pattern set + heuristics, which a validator can't self-check):

- **`tools/licenscan.py`** (A11, `c38e4ce`) — pre-publish licence-consistency
  gate: LICENSE present + SPDX-recognised; every declaration agrees; no
  copyleft-into-permissive header. `--expect <SPDX>`, allow-marker +
  `.licenscanignore`, `--selftest`. 35 tests.
- **`tools/leakscan.py`** — personal-data boundary: shareable structural patterns
  (always) + machine-local literal terms (`~/.claude/leakscan-terms.txt`, never in
  a repo); graceful degradation to structural-only with a loud warning; `--staged`
  hot path; `--disable`/subtree hatches. (Built pre-`957fa08` but never in a
  *doc*-review's scope — the pattern set has not had an approach review.)
- **`tools/secretscan.py`** — zero-dep secret detection: named vendor formats +
  a secret-named-assignment/entropy workhorse; skips safe indirections
  (`!secret`/`${VAR}`/`<ph>`), code refs, public keys, URL paths. Validated 0 FP
  over real tiki source. 47 tests. (Same as leakscan: never approach-reviewed.)

Out of scope (note if you spot something, but don't spend budget): `worktree.py`
and `pins.py` are not tagged review-owed; `PROPAGATION/EVIDENCE §1–12/REVIEW/
RECORD/PRINCIPLES/MODEL-ECONOMICS` were verdicted at `957fa08`.

## Scope — three lenses, run all three

1. **Approach & assumptions** (most important). For doctrine: is this the right
   rule, shaped right, and does the extraction generalise the ros case-law without
   either inventing or de-casing it? For the scans: is the *pattern set / heuristic*
   the right shape — what class of leak does it structurally miss?
2. **Correctness & honesty** — does each doc/tool do what it claims; is it honest
   about what's enforced vs aspirational; any overclaim; a pointer that points at
   a rule that doesn't say what the pointer implies.
3. **Completeness / harvest** — what each should cover and doesn't; what already
   exists in `method/` or the ros sources that it duplicated, contradicted, or
   ignored.

## Load-bearing assumptions to attack — by item

If any is false, that item is mis-built no matter how clean the prose or how
green the tests.

### EVIDENCE §13/§14

1. **§14 is genuinely a new obligation, not §2 re-skinned.** §14 says "an
   instrument you built is a source." Is that a real extension of §1–§4 with
   distinct teeth (the known-failure-test), or does it restate §2 (never a claim
   stronger than its evidence) at length without adding an enforceable rule? If
   it's a restatement, it's doc bloat in the apex's most-read file.
2. **§13's ladder is decidable in the moment.** "Stop at the rung set by the cost
   of being wrong" requires the agent to price *cost-of-being-wrong* before it has
   the fact. Is that operable, or does it collapse to "climb when it feels
   important"? Does §13 give a usable trigger, or only a virtue?
3. **§13 and §11 don't contradict.** §13 says climb; §11 says don't over-verify
   what a capable model reliably knows. The doc asserts they compose. Attack that:
   is there a real gap where an agent can hide under §11 to justify *not* climbing
   on something that mattered?

### build/REPO-STANDARD.md

4. **"Product in a subfolder" is a rule, not a preference dressed as one.** It's
   stated as always-applies, grounded in "learned the hard way" + one exemplar
   (`site/` arriving independently). Is n=1-plus-a-scar enough to make it
   *the* invariant, or should it be a strong default with stated exceptions (a
   single-file tool, a repo that *is* the package)?
5. **The size-to-type table is honest about its own gaps.** Four types with a CI
   column. Does the "Infra / config" row's "lint the config *if* a linter exists"
   quietly license a repo with **no** correctness gate at all — and is that an
   honest-CI position or a hole the honest-CI rule elsewhere would reject?
6. **It points up without drift.** The doc's discipline is "where `method/` owns a
   rule, point up, don't copy." Spot-check the pointers (RECORD for comments-say-
   why, AUTONOMY for private-first, EVIDENCE for grounded-not-invented): does each
   pointed-at rule actually say what REPO-STANDARD implies it says?

### build/REPO-BOUNDARY.md

7. **The discriminators actually decide real cases.** Run them against three live
   estate cases the reviewer can reason about — `tiki` inside `ros`, a hypothetical
   shared library used by two projects, a client engagement. Do the discriminators
   land the same boundary a thoughtful architect would, or do they under-determine
   (two discriminators fire opposite ways with no tiebreak beyond "prefer
   reversible")?
8. **"Prefer reversible → start merged" is the right default and not a rationalise-
   sprawl license.** Splitting-later-is-cheap rests on `git filter-repo` keeping
   history. Is that as cheap as claimed once a folder has a doctrine block, its own
   CI, cross-references? Where's the line past which "start as a folder" becomes
   the accidental-monorepo trap the doc itself warns about?

### method/SECRETS.md

9. **"Every secret is reproducible / re-mintable" is true of the *real* estate,
   not just the ideal.** The whole doctrine — and AUTONOMY's push floor resting on
   it — assumes no hand-kept irreplaceable token exists. Is that actually true, or
   are there estate secrets (a root API key, an account recovery seed, a
   registrar) that *cannot* be re-minted from code behind one approval? If even one
   exists, the "burn cost is minutes" claim is locally false and the doc must say
   where.
10. **The reference/value plane-split is enforced, not just asserted.** The doc
    says the scans catch a bare value mechanically. Cross-check against the actual
    `secretscan` skip-list (assumption 12): is every "safe by construction"
    reference form (`!secret`, `${VAR}`, `<placeholder>`) *actually* on the
    skip-list, and is any *unsafe* form wrongly skipped?

### method/ACCESS.md

11. **The strict ordering ("no step's power precedes its guard") is achievable on
    real platforms.** Step 5 demands the destructive gate exist *as tooling-
    enforced* before the write credential goes live. On a platform that only issues
    one broad credential (no scoped read-only tier — the doc's own "standing creds
    are the common reality"), can you actually hold read-only-first, or does the
    sequence quietly assume a credential granularity many platforms don't offer?
    If so, what's the honest fallback — and does the doc state it, or does it read
    as a runbook that can't be walked on the messy case?
12. **ACCESS invents no rule (its central claim).** Diff its seven steps against
    the docs it cites. Every step must trace to an existing rule in AUTONOMY /
    DATA-PROTECTION / SECRETS / PRINCIPLES. Flag any step that adds a *new*
    obligation smuggled in as a sequence — that would be a silent contradiction of
    its own framing.

### The scan triad — leakscan / secretscan / licenscan

13. **Run each `--selftest` and report the result** before judging — a
    mechanical control's floor is that it runs and its own known-bad fixtures
    fail. A red selftest voids everything below it.
14. **The heuristic's *false-negative* surface is the real risk, not its false
    positives.** FP tuning is documented (secretscan 25→0 over real tiki). But a
    scan's job is catching the leak; a miss is the exfil event the tool exists to
    prevent. For each scan, name a *class* of real leak it structurally cannot see:
    e.g. a secret split across two lines; a personal fact paraphrased rather than
    literal (leakscan's term list is literal); a novel vendor token format
    licenscan/secretscan don't pattern. Is that residual honestly stated in the
    tool's own output/README, or does a clean scan *read* as "safe to publish"
    when it only means "none of the known shapes matched"?
15. **licenscan's copyleft-into-permissive matrix is correct where it blocks.** It
    *blocks* on incompatibility — a false block is friction, a false pass ships a
    licence violation. Attack the SPDX compatibility heuristic: does it correctly
    handle dual-licensed (`A OR B`) declarations, `LicenseRef-` custom strings, and
    a permissive project that legitimately *bundles* copyleft under NOTICE (the
    REPO-STANDARD NOTICE case)? A rigid matrix that can't express "bundled, not
    linked" would false-block the very case REPO-STANDARD sanctions.
16. **leakscan's shareable/local split holds under graceful degradation.** With no
    machine-local term file, it runs structural-only "with a loud warning." Is the
    warning loud enough that a CI run or a hurried session won't read a
    structural-only pass as a full pass — i.e. does the *degraded* mode fail toward
    caution, and is a partial scan visibly partial in its exit code / JSON, not
    just a log line? (This is EVIDENCE §14 turned on the scan itself: does the
    instrument announce what it dropped?)

## The real-world check (per `REVIEW.md` — don't skip it)

For the scans, the review is not complete until each was **run** (`--selftest`
plus a real invocation on this repo) and the result reported. For the doctrine,
the real-world check is the ros cross-read: ACCESS and SECRETS claim the concrete
mechanism "stays instance-local in ros" — confirm ros actually *holds* that
instance content (so the extraction didn't strip a rule that now lives nowhere),
and that nothing sensitive leaked *up* into these shareable docs.

## Disposition & close (reminder)

Findings get stable IDs; each tagged **[fixed]** / **[backlog]** / **[rejected:
grounds]**; fixes consolidate onto one ROADMAP follow-ups item; a finding closes
only when its fix is itself verified (a scan finding closes only when the
re-run is clean). Then tick the ROADMAP pointer and add a SESSIONS entry.
