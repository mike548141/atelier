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

---

## Verdict (2026-07-10, Fable 5, fresh session) — PASS-WITH-FINDINGS

Reviewed deep-not-fast at `f72031c`: every in-scope doc read whole, all three
scan sources read line-by-line, every `--selftest` + the full 133-test suite +
real whole-repo invocations run, and the ros cross-read done against the live
ros tree. **The batch stands: the doctrine is grounded, the extraction held its
instance content (with one exception), and the scans' mechanical floors are
green.** Sixteen findings; the two that bite hardest are both *honesty* defects
of exactly the class this batch itself codified — a recorded proof that was
stale at the commit that recorded it (B1), and a pointer to an instance artifact
that doesn't exist (B14). The doctrine works; the batch's own record fell short
of it twice. That is also evidence the doctrine is the right one.

### The mechanical floor (assumption 13) — run and reported first

| Check | Result |
|---|---|
| `leakscan --selftest` / `secretscan --selftest` / `licenscan --selftest` | **all OK**, exit 0 |
| full suite (`unittest discover`, all five tools) | **133 tests, OK** |
| `leakscan` whole-repo, live | clean, **structural + local** (term list present), exit 0 |
| `secretscan` whole-repo, live | clean, exit 0 |
| `licenscan --expect Apache-2.0`, live | **exit 1 — 4 findings**, all in `tools/test_licenscan.py` fixtures (see B1) |

No selftest was red, so the reviews below stand on a proven floor. The licenscan
red is a true positive against its own unexempted fixtures, not an engine fault.

### Answers to the load-bearing assumptions

**1. §14 vs §2 re-skinned** — a real extension, not bloat. §2 governs the
agent's prose; §14 extends the apex to artifacts the agent *builds* and adds an
enforceable rule §2 lacks: the known-failure test (drive the instrument through
a known failure, assert it reports it). "Unknown is a required output" and
read-back-before-"applied" are likewise checkable, not exhortative. The closing
mapping paragraph is the only near-redundant text; it earns its place as the
pointer-web. **Holds.**

**2. §13 decidable in the moment** — operable, because the rung anchors tie to
*action classes*, not felt importance: "a number going into advice, a config
about to hit a live system, the precondition of an irreversible act" is
AUTONOMY's own recoverable-vs-floor line reused as the trigger. An agent always
knows which class its claim feeds. **Holds** (sharpened one line, B15).

**3. §13 vs §11** — they compose, with one residual: both leave "the model
reliably knows this" to self-assessment, and §2 itself warns fluency
masquerades as knowledge. The escape hatch is real but bounded: §11 can only
trim verification *below* the stakes line, because §13 sets the rung by cost of
being wrong, not by confidence. Made explicit in one sentence (B15 [fixed]).

**4. Product-in-subfolder as invariant** — **the assumption fails as stated**,
and the doc's own sizing table is the counter-evidence: two rows down, infra
repos keep "the config tree as-is" and docs repos put "content at root". It is
a strong default for repos with a deployable artifact, not "the rule that
always applies". B8 [fixed].

**5. Infra CI row** — yes, "lint *if* a linter exists" quietly licenses a repo
with no correctness gate at all, silently — which the honest-CI rule two
sections later would reject (it demands uncovered ground be *stated*). B9
[fixed]: no-gate must be a documented statement, never a silent absence.

**6. Pointers point true** — private-first → AUTONOMY floor + `decisions/0003`
✓; grounded-not-invented → EVIDENCE ✓; when-to-ADR → RECORD ✓. **One fails:
comments-say-why → RECORD.md, which contains no such rule** (it covers
docs-as-code, sessions, ADRs, roadmap, dating — grep confirms no comments rule).
Two REPO-STANDARD bullets point at it. B10 [fixed] by adding the rule to RECORD
(grounded: it is existing house practice — "why-dense body" in commit
conventions, ros code-review bar).

**7. Discriminators vs real cases** — they decide all three correctly.
*tiki-in-ros*: the visibility seam is real but **hypothetical until publication
actually approaches**, and the don't-pre-split rule lands exactly the boundary
the estate chose (stay merged; leakscan's `--staged tiki/` subtree mode is the
bridge; split when publish fires). *Shared library*: reuse fires → own repo,
unambiguous. *Client engagement*: the named monorepo case. Opposing
discriminators (reuse says split, shared-lifecycle says stay) resolve through
prefer-reversible; "the strongest usually decides" is soft but the default
makes it safe. **Holds.**

**8. Split-later-is-cheap** — true of *history* (`git filter-repo`), and the
doc's own accidental-monorepo warning is the counterweight; but cheapness decays
as a folder accretes cross-references, CI wiring, and its own doctrine block.
The line past which the trap closes is the discriminator firing — so the rule
must be split *promptly* when one fires, not eventually. B16 [fixed], one word
plus a clause.

**9. Every secret re-mintable** — **true of the managed estate, verified in
ros** (internal secrets rotate mechanically; the tiki standing user is a
tracked debt with its reason stated; external mint procedures written). The
honest edge the doc doesn't state: the **store's own age key**. For *exposure*
the doctrine holds perfectly (regenerate + re-encrypt, minutes). For *loss* it
is guarded by redundancy (Keychain copy, an out-of-band backup the ros README
itself marks ⚠), not by re-minting — and person-level credentials (Apple-ID
recovery class, in the personal vault) sit outside the doctrine entirely, by
design but unstated. B12 [fixed]: scope + master-key paragraph.

**10. Reference forms vs the actual skip-list** — verified against
`INDIRECTION_RX`: `!secret` ✓, `${VAR}` ✓, `<placeholder>` ✓, plus `$(cmd)`,
`$VAR`, `{{ }}`, `env:`/`vault:`/`sops:`. No unsafe form is wrongly skipped in
the doc-named set. One accepted trade found: `$` + letter skips a *literal*
secret that merely starts `$uper…` — overwhelmingly a shell var, right call,
but it belongs in the stated residual (B7). **Holds.**

**11. Strict ordering on one-credential platforms** — **the assumption fails on
the messy case, and the doc doesn't state the fallback.** Where the platform
issues one broad credential (the doc's own "common reality"), write *power*
arrives with the credential — before the destructive gate exists — so "no
step's power precedes its guard" cannot be walked literally. The honest
fallback (hold the ring behaviourally, encode the gate before any write is
*performed*, track the scope gap as debt) was implicit in step 2's
tracked-debt clause but never said for the ordering itself. B13 [fixed].

**12. ACCESS invents no rule** — six of seven steps trace cleanly (grant
recording → AUTONOMY self-widening; scoped credential + plane split →
SECRETS/DATA-PROTECTION verbatim; store-first → SECRETS right-plane;
read-first + reconcile-or-stop → DATA-PROTECTION; rings + capable-model-first →
PRINCIPLES/AUTONOMY, with the rollout→access transposition honestly flagged;
ZT → PRINCIPLES §5). **Step 5 smuggles a strengthening**: DATA-PROTECTION
requires the gate before the *op*; ACCESS demands it before the *power* goes
live. Right idea — but it is the sequence's own contribution and must say so
(it is also the clause assumption 11 breaks on). B13 [fixed] covers both.

**13.** Reported above — floor green, licenscan's red is B1.

**14. False-negative surfaces** — named per scan, none previously stated
anywhere: *leakscan* — paraphrased personal facts (the term list is literal),
secrets/PII split across lines, binary containers (docx/PDF/sqlite are
`\x00`-skipped silently), non-NZ address/phone shapes, and renamed-file staged
additions (B4). *secretscan* — concatenated/multi-line secrets, single-case hex
tokens outside a secret-named assignment (the deliberate FP trade), novel
vendor formats not assignment-anchored, `$`-prefixed literals (B6), same rename
gap (B4). *licenscan* — **vendored copyleft carrying the traditional prose
licence header but no `SPDX-License-Identifier` tag — the most common real-world
shape — is invisible to check 3**; only metadata and SPDX-tagged files are
seen. A clean scan today *reads* as "safe to publish" while meaning "no known
shape matched": B7 [fixed] adds a "what these scans cannot see" section to
`tools/README.md`, which is EVIDENCE §14's announce-what-you-dropped applied to
the triad's own documentation.

**15. The copyleft matrix where it blocks** — correct on canonical short ids,
and `A OR B` / `LicenseRef-` degrade *conservatively* (unknown-declaration
friction, never a false pass — exit still 1). Bundled-copyleft-under-NOTICE
does block, and the allow-marker/ignore hatch is the sanctioned expression of
"bundled, not linked" — now named in the README residual (B7) rather than left
for the user to infer. **One real hole: the modern canonical `-only` suffixes**
(`GPL-2.0-only`, `AGPL-3.0-only`, `LGPL-3.0-only`, `LGPL-2.1-only`) and `+`
forms fall through `normalise_spdx` → a strong-copyleft header downgrades from
high/incompatible **block** to medium/unknown-declaration. The gate still fires
(any finding → exit 1) so it is a mis-tier, not an exfil-class miss — but it
mis-tiers the exact case the matrix exists for. B2 [fixed] + regression tests.

**16. Degraded mode fails toward…pass.** The warning is loud in human output
and the JSON carries `scanned_local_terms: false` — but the **exit code is 0**,
so a hook or CI run without the term file is indistinguishable from full cover
at the only interface automation reads. B5 [fixed]: `--require-terms` exits 2
when the list is absent, for hook/CI lines that expect full cover; default
behaviour unchanged (a peer adopter legitimately has no list).

### The real-world check (ros cross-read)

- **SECRETS**: ros holds the instance content the extraction claims it holds —
  `secrets/README.md` (sops+age chain, Keychain redundancy, mint procedure for
  a new org), PRINCIPLES §5 bearing (credential-triad honest gap, tiki-user
  standing debt with stated reason), §7 (store-not-exempt). Nothing stripped;
  the general/instance split is real. ✓
- **ACCESS**: **fails.** ACCESS.md and method/README both state the concrete
  estate access map "stays instance-local in ros" — ros holds **no such
  artifact** (no consolidated domains-onboarded / credential-per-domain /
  plane-split / rings-walked record; only scattered posture notes, e.g. nas02
  READ-ONLY in SPECS). The pointer names a document that doesn't exist — the
  RECORD structure-as-documented defect. B14.
- **Nothing leaked up**: the shareable docs name mechanisms (`sops+age`,
  `!secret`) and generic domains ("a NAS") only — no estate topology, no
  personal data. leakscan (structural + local terms) confirms mechanically. ✓

### Findings — dispositions

| ID | Sev | What | Disposition |
|---|---|---|---|
| B1 | high | "Live-proven clean on atelier" (ROADMAP + session 15) was **false at the commit that recorded it** — licenscan exits 1 at `c38e4ce`..HEAD on its own unexempted test fixtures. The proof ran mid-build at best; the durable claim outlived it. PRINCIPLES §6's cautionary case verbatim, in the batch that codified §14. | **[fixed]** `.licenscanignore` (same reasoned exemption as both siblings); ROADMAP claim corrected; re-run clean is the close condition. Session-15 entry left verbatim (append-only); this verdict is the correction record. |
| B2 | high | `normalise_spdx` misses `-only`/`+` SPDX forms → strong-copyleft header mis-tiers block→warn. | **[fixed]** generic suffix normalisation + selftest/unit regression. |
| B3 | med | licenscan check 3 is blind to prose licence headers (no SPDX tag) — the commonest vendored-copyleft shape. | **[fixed]** residual stated in README (B7) + docstring; pattern-matching prose preambles stays out of scope deliberately (conservative tool, human pre-publish scrub owns it). |
| B4 | med | `--staged` uses `--diff-filter=ACM`: renamed-and-edited files' added lines are never scanned (git rename detection is on by default) — silent hole in both scanners' hot path. | **[fixed]** `ACMR` in both; proven live with a staged rename+secret. |
| B5 | med | leakscan degraded (no term list) exits 0 — partial cover invisible to automation. | **[fixed]** `--require-terms` (exit 2 if absent) for hooks/CI. |
| B6 | low | `$`+letter indirection skip also skips a literal `$uper…`-style secret. | **[fixed]** accepted trade, now stated in README residual (B7). |
| B7 | med | No scanner states its false-negative surface; clean reads as safe-to-publish. | **[fixed]** "What these scans cannot see" section in `tools/README.md`. |
| B8 | med | REPO-STANDARD's "rule that always applies" contradicted by its own sizing table (infra/docs rows). | **[fixed]** scoped to repos with a deployable artifact; table rows are the stated exceptions. |
| B9 | low | Infra CI row silently licenses zero correctness gate. | **[fixed]** no-gate must be documented, not silent. |
| B10 | med | comments-say-why pointed at RECORD.md twice; RECORD.md doesn't contain it. | **[fixed]** rule added to RECORD.md (the why lives at the site), grounded in existing practice. |
| B11 | low | "Seed from `templates/`" — no `templates/` exists here yet (owed but present-tense); build/README item 3 still lists the licence gate as unbuilt (landed `c38e4ce`). | **[fixed]** both lines corrected. |
| B12 | med | SECRETS' "no hand-kept irreplaceable artifact" unscoped — age-key *loss* is redundancy-guarded not re-mintable; person-level vault out of scope by design but unstated. | **[fixed]** honest-boundary paragraph. |
| B13 | med | ACCESS step 5 strengthens DATA-PROTECTION (gate-before-*power* vs gate-before-*op*) while claiming to invent nothing; ordering unwalkable on one-credential platforms, fallback unstated. | **[fixed]** strengthening owned + honest fallback stated. |
| B14 | high | ACCESS/method-README point at an estate access map ros doesn't hold. | **[fixed]** wording corrected to created-at-first-onboarding + owed; **[backlog]** ros owes its first consolidated access map (sensitive content — a ros session's job, seeded from the nas02/tiki facts it already scatters). |
| B15 | low | §13/§11 tiebreak implicit. | **[fixed]** one sentence: when they pull opposite ways, stakes win. |
| B16 | low | Split-later-is-cheap decays with accretion; "promptly" unstated. | **[fixed]** one clause in REPO-BOUNDARY. |

### The lifecycle, judged in use (second run)

It worked, and better than the first run in one specific way: the pre-named
assumptions aimed straight at real defects (assumption 4 → B8, 6 → B10, 9 →
B12, 11 → B13, 13 → B1, 15 → B2, 16 → B5 — seven of sixteen assumptions
surfaced a finding). A cold Fable session ran the whole brief with zero
clarifying questions — the ask-on-top format carries enough context. One
improvement worth carrying into REVIEW.md at its next touch (**[backlog]**, on
the follow-ups item — not edited now, since REVIEW.md is outside this batch's
scope and stacking unreviewed doctrine edits is what the gate exists to stop):
**a review re-runs every "live-proven" claim inside its scope** — B1 shows a
recorded proof can be stale by the time it's durable, and this batch's own §14
says an instrument's old "ok" is not today's evidence.

### Close conditions

All [fixed] items land this session; the scan findings close only on a clean
re-run (`licenscan --expect Apache-2.0` exit 0; B4 proven with a live staged
rename). Gate outcome: **cleared on landing of the fixes** — the create-repo
rewire and further extraction may stack on this batch once the re-runs are
green.
