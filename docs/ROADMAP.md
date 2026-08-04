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
ruling, 2026-07-23; its enacting batch exercised exactly that window). The same
landing-equals-bookkeeping rule binds the other two state changes (enacted
2026-08-03; grounding harvested to `ROADMAP-DONE.md`): an `[x]` and its harvest
to `ROADMAP-DONE.md` are **one commit**, never two — the cold-content gate fires
the moment an `[x]` lands on the hot path, so a later harvest leaves the pushed
floor red for the window between them (2026-07-26: `d847866` red, `0485540`
green). And an **inline claim** (`wt: none`) **closes in the commit that lands
its work** — a worktree merge forces a return to this file, an inline claim has
no such forcing step, and the one item that skipped the worktree skipped its
close with it (2026-07-26, cleared hours after `b89a306` had shipped).

## Policy-as-code programme — five tracks (Mike approved 2026-07-27)

**What this is.** ADR 0008 made enforcement propagate *by call, not by copy*,
and the rollout landed. This section is the follow-on programme: the holes the
rollout left, the nine cold review verdicts of 2026-07-26 consolidated into
buildable work, and the doctrine gaps that let each hole open. Grounded in a
sweep of every session transcript 2026-07-23 → 2026-07-27 (60 sessions; the
25th is a gap day), with every claim re-verified against the live repos rather
than inherited from a record.

**The finding that organises it.** The defect ADR 0008 exists to end kept
reappearing *inside the fix*: **a check that runs, exits 0, and covers
nothing.** It appeared in the registry wiring (absolute paths matched no staged
path), in the boundary scanners (a `--staged` absolute path scanned nothing), in
the nested-worktree exemptions, and — per the cold passes — in `scope`, in the
hook plane's `leakscan`, and in `floorfleet`'s own conformance claim. It is one
class, and the tracks below are ordered by how much of it each closes.

**Sequencing: A → B → C, then D and E.** A is the only track with live
exposure; B stops it recurring; C stops the slow decay. D and E are real and
neither is bleeding. **Ruling cadence** (Mike, 2026-07-27): the 56 cold-pass
findings are ruled *at the point of work*, batched per item, in plain language
with impacts — not in one cold sitting, which would be an under-contextualised
ask. Three exceptions are ruled up front because they are live fail-opens whose
fix shape genuinely branches: EP1, EP3, and the `advisory` schema change (C1).

This section is **refs only** where the work is already queued elsewhere — it
points, it does not restate (thin anchor, fat pointer). New work is written out
in the track that owns it.

### Track A — close the fail-opens 🔥

*The floor can report green while checking nothing. The only track with real
exposure.* Findings are counsel from the 2026-07-26 rule-4 Fable passes; the
rulings are Mike's (REVIEW rule 3), and each application earns a further cold
pass while a MAJOR stands.

> 📦 **All 6 items complete, both cold passes, and the review cycle CLOSED**
>   → [`ROADMAP-DONE.md`](ROADMAP-DONE.md) (A5a fixed 2026-07-27; A1–A4 + A5b
>   landed 2026-07-27, worktree `track-a-fail-opens`; the application's own
>   pass ruled and applied 2026-07-28, TA1–TA9, worktree
>   `ta-findings-application`; the TA application's terminal cold pass ran
>   2026-07-28 — 0 MAJOR, so the cycle closes per REVIEW.md's no-MAJOR rule).
>   Track closed — the fail-opens are shut, each fix driven live against the
>   probe that proved the defect. What remains below is Mike's ruling on the
>   terminal pass's residue, not work.


### Track B — make the enumerator real

*`floorfleet` is what turns "I hope the policy propagated" into "I know it did",
and nothing runs it.* Three of the four items below already have costed entries
further down this file; they are pointed at, not restated.

- **B1 — schedule the conformance check.** **BUILT 2026-07-28** (Mike ruled
  option B). The daily workflow is committed and pushed in the estate-root repo;
  it is blocked on the token only, which is Mike's to mint. Its enabling work —
  `--from-github`, without which a runner discovers nothing — landed in atelier.
  Options, ruling, the token spec and the corrected costing → § *🎯 Schedule the
  conformance check* below. The host repo stays unnamed here and that is not an
  oversight: `PROPAGATION.md` binds *any* public tree including atelier's own,
  so writing it into this file would be committing the breach the rule exists to
  avoid. A public tree references it by local-path convention.
- **B2 — `--status` mode** (wired *and* passing) and **B3 — the
  Actions-disabled blind spot**: **BOTH DONE 2026-07-28**, landed together
  because they are one defect — a board answering *is it wired* while reading
  as though it answered *is it working*. ⏳ **review queued**, see the entry in
  § *Doctrine — review-owed*. The first live run is the finding: **5 of 14
  repos read `wired ✅` and had been RED on their default branches since the
  2026-07-25 rollout**, unnoticed for three days. Detail →
  [`ROADMAP-DONE.md`](ROADMAP-DONE.md).
- [ ] **The scheduled consumer's workflow still owes its token-spec comment**
      — FS1's all-repos grant statement is applied on every surface atelier
      carries (module docstring, `--from-github` help + docstring, the
      empty-estate failure message, 2026-08-03); the one remaining surface
      is the consuming workflow's permissions comment in the private
      estate-root repo, a one-line edit that repo owes itself.
- [ ] 🎯 **The five red floors themselves are now open work.** `--status` found
      them; it does not fix them. Each is a real finding in a child repo and
      each is that repo's own call to clear (the same reasoning as the
      bootstrap reds already recorded below). Deliberately not named here with
      their posture — that join is the breach this file already records three
      times.
- [ ] 🎯 **B4 — the roadmap-deletion guard: BUILT, MEASURED, and deliberately
      NOT WIRED (2026-07-28).** `tools/harvestscan.py` exists, is tested (16
      tests) and runs clean on the live tree. It fingerprints *content* as the
      item required — never titles — and the measurement is why it stops short
      of the registry.
      **Replayed over all 390 commits touching `ROADMAP.md`**, each against its
      parent exactly as a hook would see it:

      | design | fires on | items |
      |---|---|---|
      | raw body, Jaccard ≥ 0.6 | 165 commits (42.3%) | 257 |
      | + bookkeeping stripped, containment | 120 (30.8%) | 179 |
      | + review pointers excluded | 105 (26.9%) | 158 |

      Every step fixed a **cause** — matching on claim stamps and cycle
      vocabulary that churn while the work does not; punishing an item for
      being absorbed into a larger one; counting refs-only `⏳` pointers whose
      disappearance *is* the mechanism working — and each bought less than the
      last. **One roadmap commit in four would still warn**, which is the rate
      the 2026-07-26 audit already showed gets a guard `allow`-markered into
      silence. Reviewer's counsel to itself is `stampscan`'s: **do not wire,
      not even advisory.**
      **The signal is real, which is why this is shelved and not binned.**
      Replayed against `dd7fcb74` — the commit that removed 185 lines on a
      heading-only comparison and lost a completed item — it reports 2 items,
      including work that genuinely vanished. The detector works; the
      discriminator does not.
      **What would make it wireable, none of it a threshold change:** scope to
      delete-only commits (a commit rewriting a section is both the noisy case
      and the one a human is already reading); compare against a branch's
      merge-base rather than the previous commit, so a multi-commit rewrite is
      judged once at its end state; or narrow to items carrying a decision
      marker, whose loss is what actually costs. **Tuning
      `SURVIVAL_SIMILARITY` is explicitly not on that list** — it would be
      fitting a constant to the corpus it is measured on. Mike's call whether
      to fund the next step or leave it as a hand-run tool before deliberate
      bulk deletions, which is the one moment the 2026-07-25 failure would have
      been caught.

### Track C — kill the advisory decay

*An advisory still standing in a month is the "honour it manually" failure
wearing a new hat — the precise decay ADR 0008 exists to end.* Re-measured
2026-07-28: **17 advisory declarations across 10 children**, none carrying a
reason, none carrying a date. (The 2026-07-27 figure of 11 across 8 was an
undercount — the fourth wrong blast radius on this programme and the first that
*understated* the work; see the C1 session record.)

> 📦 **C1 phase 1 complete, and its review cycle CLOSED** (schema, expiry,
>   A1(b); rule-4 cold pass 2026-07-28, 0 MAJOR — terminal) →
>   [`ROADMAP-DONE.md`](ROADMAP-DONE.md). What remains of C1 is C1b below —
>   the migration and the removal of the transition spelling.
- [ ] **C1F3 residue — `floorfleet` is a third open surface of the class**
      (found at the 2026-08-03 application). The C1F3 strip landed at the two
      ruled parse seams (`floor.py`'s whole-document config ingest,
      `publishscan`'s ignore-file and output surfaces), but `floorfleet`
      reads child `.atelier-floor.json` files through its own parsers, not
      `floor.Config.load`, so the board still prints child-authored
      `why`/reason strings raw — and the C1F3 finding text itself says the
      class reaches "both floor and board". Small fix at floorfleet's parse
      seam; rides the next floorfleet touch, or its application pass.
- [ ] 🎯 **A warn-only registry scanner renders `✅ enforced` on the floor
      board** (handed up by the 2026-08-03 pointer-grammar build, deliberately
      not decided there — past its minimal-hunk scope). Both new advisory
      entries exit 0 always, so the render shows the same green tick it shows
      a blocking scanner while printing findings — the "identical output for
      materially different cover" shape EP3 named for leakscan's planes.
      **RULED 2026-08-04 (Mike): build the third render state** — advisory
      and warn-only entries render distinctly on every plane, so the board
      stops overstating cover; small `floor.py` change plus tests, and EP3
      inherits a consistent precedent when it is ruled rather than being
      waited on. Work owed: one small build item.
- [ ] 🎯 **C1b — migrate the 17, then delete the legacy spelling.** Phase 1
      deliberately did not write the declarations: a `review-by` is a
      commitment about when a backlog gets cleared, which is the principal's to
      set rather than the applier's to invent, and inventing one across ten
      repos would be fitting a number to turn a board green. **Blocked on one
      decision from Mike — the review horizon.** After that the migration is
      mechanical (17 declarations, 10 repos, several private). **Phase 2 —
      removing the legacy bare-list spelling from `floor.py` — is blocked on
      the migration**, and must not be skipped: a transition spelling still
      parsing in a month is C1's own decay, one level up.
- [ ] **C2 — retire the 17.** One child already proved it is a single pass:
      four advisories to zero, sixty findings cleared, and the honest breakdown
      matters more than the count — only a handful were genuine, the rest were
      product nouns that wanted inline-coding rather than re-spelling, and
      rhetorical relative-time words that wanted rewording rather than an
      allow-marker (so no exemption debt was left behind). That is the
      transferable recipe.
- [ ] **C3 — a sanctioned adoption path.** A repo whose existing content
      already fails the gate **cannot commit the change that installs the
      gate.** It happened twice during the rollout and was resolved with a
      documented one-time bypass — defensible once, but it is now an
      undocumented pattern that recurs on *every* future adoption. Decide the
      pattern before the next adoption, not during it: either a sanctioned
      bootstrap, or an adopt mode that installs the hygiene checks
      advisory-first and tightens on re-baseline.
- [ ] **C4 — make the local bypass visible.** With CI as backstop rather than
      gate, `--no-verify` is the one route that reaches history unscanned, and
      nothing observes it. Idea: CI flags a pushed commit that would not have
      passed the hook, so a bypass is a recorded event rather than a private
      one. Weigh honestly against it also being the legitimate escape hatch —
      making it painful invites worse workarounds.
- [ ] 🎯 **C5 — a forcing function for the estate-root name.** The rule was
      widened to bind *any* public tree including atelier's own
      (`PROPAGATION.md`, 2026-07-28 — it had exempted the parent by naming
      categories of repo instead of the property, and 63 record mentions
      followed). Widening the words is not a forcing function: this is the
      fourth rule in the programme found broken *because nothing enforced it*,
      and the widening commit itself then broke it once more, which is the
      argument for enforcement rather than against it.
      **The measurement, corrected.** This item previously deferred the
      cheapest fix on the premise that a bare literal term is a cry-wolf trap,
      the root's name being also an ordinary English word. **Measured on the
      cold pass: of all 63 occurrences in this repo, zero are the ordinary
      English word — every one is a repo reference.** The premise was reasoned
      from the word, never checked against the corpus, which is the same shape
      as the two false blockers this programme has already recorded. A literal
      term is therefore viable and is the cheapest thing that could work;
      repo-reference *shapes* (`<owner>/<name>`, `~/.pets/<name>`,
      `<name>@<sha>`, possessive) remain the more durable pattern and the two
      compose. **Mike's call** — the shape is his, and either way the home is
      a line in the machine-local `leakscan` term list, which is personal
      config outside this repo and his to change. That home matches the
      forward-only ruling exactly, since `--staged` reads added lines only.
      Watch the C3 interaction: a future wholesale rewrite of a record that
      already carries a mention would re-add those lines and block, which is
      the adoption-bootstrap problem in miniature.

### Track D — finish the registry

*Two scanners exist outside the registry, which is the ADR 0008 defect one
level up: a check wired into atelier's own workflow reaches no child, and the
child template's promise that "a new check arrives on the next push" holds for
registry checks only.*

- [ ] 🎯 **D1 — `pathscan`: promote with a corrected scope, or retire it.** It
      runs as a bespoke advisory step in atelier's own `ci.yml`, outside the
      registry, so no child has ever run it. The cold pass returned 2 MAJOR:
      the wired scope cannot see the corpus that motivated the tool, and the
      baseline is ~97% record-store content, so the gateable surface is a small
      fraction of what it reports. Verdict:
      [pathscan S2 cold pass](reviews/2026-07-26-2215-pathscan-s2-cold.md).
- [ ] 🎯 **D2 — `stampscan`: fix at the parser, or shelve it.** Built, tested,
      and **not wireable as built** — re-verified 2026-07-27, the live tree
      exits 2 today. Three MAJOR: marker recognition is context-blind, so any
      document that *describes* the syntax reds the scan as a config error that
      `--warn` cannot suppress; a narrowing declaration accepts narrowing to
      nothing, so one word vacates the whole check while it reports clean; and
      the template ships markers whose source cannot resolve in any scaffolded
      child, which would red future scaffolds estate-wide once registry-wired.
      Reviewer's counsel is explicit — **do not wire, not even advisory** —
      until the parser strips fenced and inline code, an ignore file ships, and
      the narrow-to-nothing hole is closed or explicitly accepted. Verdict:
      [stampscan S4 cold pass](reviews/2026-07-26-2215-stampscan-s4-cold.md).
- [ ] 🎯 **D3 — `signscan` cannot fail CI.** It is invoked with `--warn` on
      both planes, so an unsigned commit produces an annotation and never a
      red. That is the deliberate warn-first rollout state and it has outlived
      its purpose; the flip is Mike's, and it pairs with his key rotations.
- [ ] **D4 — the repo-local seam has no adopters.** The extension point landed
      2026-07-26 and **no repo declares a `local` check** (verified
      2026-07-27). The case that motivated it — a networking child's
      estate-token tripwire, whose blocklist can never live in a shared public
      repo — is still switched off, with CI as the only remaining net. That
      wiring is the child repo's own work, not atelier's, but the seam is not
      proven until something uses it.

### Track E — precision, so findings stay believed

*Every false positive on a correct line trains someone to allow-marker it, and
that is how a scanner's output stops being read. These are tool defects, not
adopter mistakes.*

> 🎯 **The track's own premise was corrected by Mike, 2026-07-28 — it assumed
> one dial.** Precision is only forced to trade against coverage while a
> scanner's sole response is *block*. Mike stated the floor's purpose plainly
> — find every secret, credential, private key and piece of personal data, so
> none of it reaches a public or insecure place — and that intent is not
> reachable in a detect-and-block-only design. E6 below is the correction; E1–E5
> stay real defects and are unaffected.

- [ ] 🎯 **E6 — the floor's posture, and the dial that makes it reachable.
      RULED 2026-07-28 (Mike), three parts, all his call, none built.**

      **What was found.** The two boundary scanners hold *opposite* postures
      and nothing records that they differ. `leakscan` states its own at
      `leakscan.py`: over-flagging is fail-safe, because a false positive
      costs an allow-marker and a false negative costs a leak. `secretscan`
      states no posture at all and its docstring sells the reverse — context
      plus entropy as *precision* against raw entropy scanning. So the
      scanner guarding personal data is tuned to over-flag and the scanner
      guarding credentials is tuned to under-flag, which is backwards on
      risk: a leaked credential is actively exploitable in a way an address
      is not. No record shows that asymmetry being decided; it accumulated.

      **Why the narrowing happened — a design gap, not a judgement call.**
      `secretscan`'s `severity` field is decorative (`"high" | "medium" —
      advisory; any hit still blocks`), and the exit is a block on *any*
      finding. With one dial, the only way to avoid crying wolf on every git
      SHA and hex blob is to shrink detection — which is exactly what the
      `SLUG_RX` comment records itself doing ("deliberately letters-only …
      a real (pre-existing) gap and not one to widen"). **That decision was
      the principal's to make and was recorded as a code comment**, where it
      never reached him. Named as its own failure shape: a coverage
      narrowing settled at tool altitude.

      - **E6a — DONE 2026-08-03** (orchestrated run): the posture is doctrine
            — `SECRETS.md` § *The boundary's posture* states Mike's intent as
            the bar both scans answer to, over-flag as the fail-safe
            direction, the leakscan/secretscan asymmetry as
            found-and-decided, EI5's grounding (rotation presupposes
            detection), coverage narrowing as the principal's decision never
            a code comment, and the advisory dial as decided-not-built with
            EI1's consumer precondition. Rule-4 `⏳` queued at landing
            (§ *Doctrine — review-owed*).
      - [ ] **E6b — give `secretscan` a real advisory tier.** High-confidence
            hits block as they do now; context-free entropy hits report and
            exit 0. The blocking set never shrinks — everything the tier adds
            is coverage that does not exist today. This is what lets detection
            widen to the stated intent without the cry-wolf tax. Weigh against
            `leakscan` having no advisory form by design: the argument that it
            does not weaken the gate is that the blocking set is unchanged,
            and that argument should be tested at review rather than assumed.
            **Tiered on two axes, not one — see E6d.**
            **UNBLOCKED 2026-08-04 (Mike, proposals ruled at pickup per
            EI1/EI3): the named consumer is the CI plane + board count** —
            commit-time print, every push re-prints all advisory findings
            tree-wide, and the floor board carries a persistent
            `🟡 N advisory finding(s)` count that cannot quietly vanish.
            No new artefact class. Buildable now, after E6a (landed).
      - [ ] **E6d — impact is the second axis. RULED 2026-07-28 (Mike).** The
            tier must weigh *risk*, not confidence alone: a mid-confidence hit
            on a credential that opens the whole estate outranks a
            high-confidence hit on something insignificant. **The field the
            code calls `severity` is already confidence wearing severity's
            name** — `gcp-oauth-secret` is graded `medium` because its
            *pattern* is less specific, and `stripe-key` grades `sk_live_` and
            `sk_test_` identically while the token itself states its own blast
            radius. Three rulings:
            **(i) Escalate only.** Impact may raise a finding's response,
            never lower it. A high-confidence hit on something trivial still
            blocks exactly as today. Grounds: the downward direction is where
            a "this one doesn't matter" lane would live, and that assessment
            has been wrong here before; examples and fixtures are already
            served by placeholder detection and allow-markers, which force a
            written reason. Quieting comes from E6b's confidence tier, never
            from impact.
            **(ii) Repo-declared, via the seam that already exists.** Impact
            is *least* knowable exactly where it matters most: a shared
            scanner can class a vendor credential by construction, but cannot
            know what a home-grown `password=` opens. Only the repo knows, so
            the declaration rides the repo-local floor seam — which has **no
            adopters** (D4), and whose motivating case was a networking
            child's estate-token tripwire. That case is an impact declaration
            in all but name; adopting this proves the seam.
            **(iii) `confidence` × `impact` = `severity`, computed.** Rename
            the mislabelled field, add the second axis, and let the computed
            result drive block-vs-report — so the field stops misdescribing
            what it holds, which is how it came to be read as impact at all.
            **SCALE RULED 2026-08-04 (Mike, the EI3 proposal as brought):
            three repo-declared levels — `estate` / `repo` / `local`,
            undeclared defaults to `repo`** (the middle: silence neither
            inflates nor waives), class terms only in public trees. Computed
            response: high confidence blocks as today at any impact;
            low + `estate` escalates to block; low + `repo` or `local` is
            advisory. Nothing ever de-escalates below today's behaviour;
            the F1 rebuild may revisit the model (FG2). **Sequencing ruled
            with it: the build pairs with one child's first impact
            declaration** — the estate-token tripwire case — proving the D4
            seam and the axis together.
      - **E6c — DONE 2026-08-03** (orchestrated run, with the SF residue in
            one build): whole-shape carve-outs decided before every
            variety-reading gate in assigned-secret context — an unbroken
            32+ alphanumeric run (both hex leading forms, uppercase,
            base32) and a four-plus separator-joined word passphrase (both
            spellings) are no longer identifier/slug-suppressed; the ruled
            six-shape probe went 2/6 → 6/6, the blocking set only widened,
            and placeholder/indirection/path suppression keeps precedence
            (statements of what a value is *for*, not its variety). SF3's
            canary suite (16 shapes, count pinned, contract stated) now
            guards the gate. Detail → [`ROADMAP-DONE.md`](ROADMAP-DONE.md)
            § *secretscan residue + E6c*.

      **The split that makes the intent affordable** (recorded because it is
      the reasoning, not the instruction): credential-key context is nearly
      free to widen, because the key name has already done the filtering;
      the context-free path is where SHAs, file hashes, hex data and base64
      blobs live, and that is the path the advisory tier serves. The three
      hard cases Mike named land as — examples → placeholder detection plus
      the queued "describe, don't quote" rule (E5); file hashes and hex data
      → separated by context already, since neither sits under a
      credential-named key.

      🎯 **REVIEWED 2026-07-29 (rule-4 Fable cold pass, design/intent):
      PASS-WITH-FINDINGS — 1 MAJOR / 2 MODERATE / 1 minor / 2 notes.
      EI1–EI6 RULED 2026-07-29 (Mike, plain-language walk-through):**
      EI1 — a named advisory-findings consumer is a **build precondition
      of E6b** (shape not pre-ruled); EI2 — estate-detail impact
      declarations never in public trees, class terms only there; EI3 —
      matrix/scale/undeclared-default are **concrete proposals brought to
      Mike at build pickup**, not pre-rulings and not the builder's to
      settle; EI4 — the item is corrected to name `HIGH_ENTROPY_RX`'s
      mixed-class requirement as the real narrowing site; EI5 — E6a
      grounds on *rotation presupposes detection*; EI6 — per-plane
      advisory semantics, E6a-first ordering, and the leakscan asymmetry
      recorded as decided. Rulings verbatim + counsel:
      [E6 intent cold pass](reviews/2026-07-29-1243-e6-intent-cold.md).
      **Application owed to a neutral hand** (authored neither the E6
      text nor the verdict); it queues its own rule-4 pointer at landing.
      The companion sweep the intent record itself flags — whether
      `leakscan` reaches the PII half of the stated intent as
      `secretscan` reaches the credential half — is endorsed by the pass
      as real open work, not folded into it. **Ran 2026-08-03 → E7 below.**

- [ ] 🎯 **E7 — the PII-half sweep ran 2026-08-03 (fourth carry, discharged):
      leakscan reaches the PII half PARTIALLY — materially behind the
      credential half.** Full findings, class-level and probe-verified:
      [sweep record](sessions/2026-08-03-2050-leakscan-pii-sweep.md).
      Headlines: leakscan has **no label/assignment context layer and no
      placeholder suppression** — a block of values under explicit
      personal-data key names (DOB, bank account, passport, medication,
      NHI, plate) probes completely clean, while E6's own reasoning says
      key context is nearly free to widen (**G1**, the highest-value fix);
      **file paths are never scanned** (**G2** — zero FPs measured over the
      repo's own 390 tracked paths); **binary media are skipped silently**
      — a synthetic image carrying GPS metadata, a name and an address
      scans clean (**G3**, whose honest fix is an advisory-shaped notice,
      in recorded tension with E6a's "leakscan gains no advisory form" —
      Mike's to weigh, not resolved here); financial identifiers (**G4**),
      international phone (**G5**), term-list form fragility — a listed
      name's slug/camel/snake/split forms all pass (**G6**), one bracketed
      NZ phone form (**G7**). Six defects in existing rules, led by
      **D1**: an allow-marker written for a structural FP silences the
      machine-local term list on the same line — the highest-confidence
      layer switched off exactly where a human judged the line safe for a
      different reason. **D2** confirms E4's class is wider than recorded
      (any three-plus colon-separated hex-ish groups, not just clock
      times). The don't-add list (bare dates, context-free ID shapes, NER
      names, schedule prose, low-precision coordinates) is part of the
      finding. The term-list plane-split consequence is recorded as decided
      design worth holding in view.
      **RULED 2026-08-04 (Mike, plain-language walk-through, all as
      counselled): D1 fixed as (a)** — allow-markers exempt structural rules
      only, the term list always runs (a term-list misfire is fixed in the
      list itself, which is the operator's own config); **D2 fixed as (a)**
      — the IPv6-shape rule requires `::` or four-plus groups, with
      must-flag/must-pass tests both directions (this ruling also settles
      E4 below — one fix, both entries); **D3–D6 all fixed** (safe-set
      widening, address suffix guard, MAC dedupe, exact all-zeroes match);
      **G1, G2, G4, G6, G7 funded** (the key-context layer with placeholder
      suppression and its own canary suite; path scanning; Luhn-checked
      cards + IBAN + NZ hyphenated bank shape with bare-digit forms staying
      key-context-only; term-list derived forms documented with opt-in
      derivation; the bracketed phone form); **G5 deferred** — NZ forms are
      covered, international numbers are rare here, revisit on first real
      miss; **G3 ruled BLOCKING** — an unscannable or metadata-bearing
      binary blocks and a legitimate image carries a one-time reasoned
      marker, keeping E6a's no-advisory-form decision intact rather than
      carving it. **Work owed: one leakscan build item (D-fixes + G-builds,
      tests + canaries); it queues its rule-4 pointer at landing.**
- [ ] **E1 — `licenscan` is silent exactly where it matters most.** With an
      unrecognised licence it stops at *"licence unrecognised"* and verifies
      nothing further — it does not fall back to flagging vendored copyleft,
      and an allow-marker does not restore the header checks. Proven against a
      fixture. Three proprietary children are therefore `disabled`, and a
      proprietary repo going public is *precisely* when contamination detection
      matters. Full reproduction and fix shape → § *Licence gate* below.
- [ ] **E2 — `licenscan` flags correct PyPI trove classifiers.** The repo was
      right and the tool was wrong; every Python package carries these, so it
      recurs by construction → § *Licence gate* below.
- [ ] **E3 — `secretscan` suppresses one public-key line shape but not key
      fingerprints**, which accounted for two of eight findings in one child.
      Widening a security scanner's blind spot is atelier's call, not a child's
      — which is why it was correctly left unchanged there and belongs here.
- [ ] **E4 — `leakscan` reads two clock times side by side as an IPv6
      address.** Recurs wherever a record quotes a rendered time span → already
      queued under § *Boundary findings* below; carried here because it is the
      same class as E3 and should be ruled with it.
- [ ] 🎯 **E5 — write down "describe, don't quote" as a standing rule for
      record prose.** It has now bitten three separate scanners in three weeks:
      example credentials, a literal open-source licence tag quoted in a
      roadmap entry, and a stamp marker mentioned in a review file — each time
      the scanner was *correct* and the prose was the defect. It is already the
      answer for example credentials; the general form belongs in `RECORD.md`.
      **Recurrence, not severity, is the trigger** — three instances of a
      trivial failure is a defect in the system producing it.

### Track F — the guard governance model (Mike, 2026-08-02)

*What a child repo may do when it meets a shared guard, and what it may never
do. Several items already on this board turn out to be instances of one frame
nobody had named.*

- [ ] 🎯 **F1 — rebuild the block-vs-advise model from base.** Origin: E6d's
      **escalate-only** ruling. **That ruling stands** (Mike, 2026-08-02) —
      nothing is reverted and no work is blocked on this. But Mike is no
      longer confident it was the right call, so the model underneath it is
      rebuilt from first principles rather than patched. Recorded as an open
      action at his instruction, not as a reversal.

      **The decomposition Mike gave is finer than the one E6d encodes.** E6d
      tiers on confidence × impact. Mike splits it three ways:
      (1) how confident are we that the **identification** is correct — is
      this actually a secret; (2) *given* the identification is true, what is
      the **probability** of a risk or issue eventuating; (3) given it is
      true, what is the **impact** if it does. E6d collapses (2) into (3). A
      correctly-identified credential can carry low probability of harm —
      already rotated, expired, scoped to nothing — and that is a different
      question from how bad the harm would be. Whether the split changes the
      response model is the review's to say, not this entry's.

      **The vocabulary Mike named, recorded as scope — not as answers:**
      **DRY for policy-as-code** — children *run* the shared guards from
      atelier and never copy them out; they may *add* their own for needs the
      shared set does not cover · **a child cannot reduce a shared guard**,
      but may reason about exclusions and acceptance · **declare acceptance
      or deferment** — today one spelling covers both · **report a false
      positive** — a route back to the guard's owner · **resolve vs scope vs
      soften** — three responses to a finding, with no written taxonomy ·
      **side-stepping** — a guard not wired in, overruled, or ignored.

      **Existing items that are instances of this frame** (mapped here, not
      moved — each keeps its own home and owner): run-not-copy is ADR 0008,
      landed, with the repo-local seam for the *add your own* half still at
      **zero adopters (D4)** · cannot-reduce is REPO-STANDARD's
      narrow-not-contradict layering · acceptance-and-deferment is C1's
      `why` + `review-by` and `disabled`'s reason, plus **C2** retiring the
      17 · false-positive reporting is **E1–E4**, every one of them found ad
      hoc with no route back · resolve-vs-scope-vs-soften is what **Track A**
      met as scope fail-opens and C1 met as advisory · side-stepping is
      **C4** (`--no-verify` unobserved), the Actions-disabled blind spot,
      Track A's scope-covering-nothing, and an advisory that never expires ·
      **adoption/first-contact is C3** and the two `--no-verify`-bootstrapped
      children — a repo meeting a guard its existing content already fails,
      twice resolved by documented bypass (mapped in by the FG1 ruling,
      2026-08-03: the cold pass found the original list was steady-state
      only, and adoption is the case a model built without it would distort
      around). That these open items are one frame is the finding; the
      frame is Mike's, not an agent's synthesis of it.

      **Deliberately not pre-solved.** Mike asked for the review to run on the
      *origin problem and possible solutions*, ahead of any design — review as
      an input, not a gate. No candidate model is written here on purpose: an
      entry that proposed one would steer the pass it is queuing, which is the
      breach this file has now recorded three times.

      🎯 **REVIEWED 2026-08-03 (rule-4 Fable design/intent cold pass):
      PASS-WITH-FINDINGS — 0 MAJOR / 2 MODERATE / 1 minor / 3 notes.
      FG1–FG6 await Mike's ruling (REVIEW rule 3); they are counsel feeding
      the rebuild at pickup, per the review-as-input instruction.** The
      frame survives attack and matches the state of practice
      (confidence · likelihood · impact is the canonical scanner/risk
      structure; repo-declared impact is CVSS's environmental score in
      another vocabulary). Headlines: FG1 — the instance mapping
      under-counts; C3 (adoption/first-contact) is the missing case a
      steady-state-only model would distort around, and P3 sits on the
      boundary undeclared. FG2 — the split does change the response model:
      the downgrade lane escalate-only forbids already exists spelled as
      exemption, so the durable invariant is provenance (declared, reasoned,
      expiring), not direction. FG3 — granularity is a missing axis;
      acceptance vs deferment are already distinct at line vs check level.
      Full findings + reconcile:
      [F1 intent cold pass](reviews/2026-08-03-0657-f1-guard-governance-intent-cold.md).
      Intent record:
      [`2026-08-02-2340-guard-governance-frame`](sessions/2026-08-02-2340-guard-governance-frame.md).

      **FG1–FG6 RULED 2026-08-03 (Mike, plain-language walk-through; every
      finding as counselled). These bind the rebuild at pickup:**
      **FG1** — C3 is mapped into the instance list above, and the rebuilt
      model must *state* whether posture-by-visibility (P3) is inside or
      outside its scope — either answer, never silence.
      **FG2** — the rebuild's working hypothesis is **provenance, not
      direction**: tool-initiated lowering of a response stays forbidden; a
      declared, reasoned, expiring, principal-visible lowering is lawful
      (C1's existing machinery — a downward claim rots, so it carries
      expiry; an upward move needs none). A hypothesis to *test* at design,
      not inherit; E6d stands unchanged until the rebuild lands.
      **FG3** — the model's vocabulary gains the granularity axis (line /
      check / repo) and the definitions the one-spelling ambiguity blurred:
      **acceptance is indefinite with a reason; deferment is temporary with
      an expiry**.
      **FG4** — the axes are checked against prior-art vocabulary (CVSS
      exploitability/impact/environmental, CodeQL precision ×
      security-severity, Semgrep confidence × severity) at pickup, verified
      then rather than trusted from the pass.
      **FG5** — the false-positive route is a pointer-carrying
      specialisation of PROPAGATION's resolved-upward rule, never a second
      original.
      **FG6** — the F1 pointer's "design/intent pass per REVIEW.md §" line
      is handed to the funded pointer-grammar build as a boundary specimen
      (procedural pass-type vs evaluative steering); the build decides the
      boundary with its corpus, not this entry.

### The thing underneath all of it — state-tracking, not reasoning

Two independent sessions reached the same diagnosis in the same 24 hours, in
their own words: **not degraded reasoning, degraded state-tracking.** Every
failure was a stale belief, sincerely held, that had once been true — the
session record *was* accurate, those sections *were* duplicates by heading, the
work *had* been ready to close. In a long session the cheapest source of "what
is true" is what is already in context, and context is dense with things that
were true; verification costs a tool call and recall is free.

- [ ] **The mechanisable form of it:** any claim about *current state* comes
      from a fresh read, never from context. `RECORD.md` already says this for
      one case — the all-clear is the pushed floor run, not the local scan —
      and the general rule is the same shape. A close-out that is mechanical
      rather than narrative is the concrete change.
- [ ] **The measurement that supports it, and its limits.** Median session
      length rose ~62% inside that window, the largest 2.7×, the share over 2 MB
      from 11% to 28%. Correlation only: n=18, causation not isolated,
      compaction untested, harness changes unchecked, and a higher personal
      working pace would produce the same signature with nothing model-side
      changing. Recorded as a lead for the history-mining pass, not a finding.
- [ ] **Aggravating factor worth keeping:** both failing sessions were making
      multi-repo state changes, where reality moves underneath the session. A
      long session doing pure analysis would not show this — which is testable,
      and is why the simpler story ("long sessions are worse") should be
      resisted.

The queued history-mining pass (§ *Mine the estate's own history for repeat
offences*) is the instrument that would test this properly, by correlating each
recorded failure against position-in-session and session length.

### Doctrine forcing functions the programme depends on

Each of these is a rule that exists in practice and has no forcing function, so
it keeps being broken. All are self-authored doctrine when they land ⇒ rule-4
`⏳` in the landing commit, and that review is Fable's.

- **Which tier reviews** — the rule that cost a whole three-verdict pass →
  § *Doctrine — review-owed* below.
- **A state change and the bookkeeping the floor demands of it ship together**
  — enacted 2026-08-03 as two preamble clauses in this file (the `[x]`/harvest
  single commit, and the inline-claim close); grounding harvested to
  [`ROADMAP-DONE.md`](ROADMAP-DONE.md), rule-4 `⏳` queued in
  § *Doctrine — review-owed*.
- **Bulk deletion from a record store is a show-first action** — Mike's call,
  it narrows agent autonomy → § *For your consideration* below.

**The `⏳` pointer grammar — MECHANISED 2026-08-03** (the FUNDED build,
closing the THIRD-instance finding, one build with the B4 wiring per HV2):
`tools/pointerscan.py` carries both detectors (grammar + cycle state),
advisory-first, registry-wired; the scope question settled on four recorded
specimens (marker glyph in bullet or state prefix, or a review-obligation
phrase in an emphasis run; `[x]` never a pointer); pass type ruled a lawful
fourth field beside {delta, intent record, tier} (FG6's boundary specimen
passes clean); **instance 2 LOCATED** — the pathscan S2 first-of-kind pointer,
three seeded questions, live 2026-07-24→27. The recorded counts were wrong in
both directions and are corrected in the harvest: the five stale residues were
seven (two still live at HEAD, fixed 2026-08-03), the three grammar instances
were 19 across history. Day-one proof: the live tree warned on exactly the
specimens the build was funded to catch, fixed in the landing merge. Entries →
[`ROADMAP-DONE.md`](ROADMAP-DONE.md) § *The ⏳ pointer grammar mechanised*;
rule-4 `⏳` queued in § *Doctrine — review-owed*.

- [ ] **ZL1 (MAJOR) — the surface that binds the apex at session start is
      stale.** `skills/session-onramp/SKILL.md` still teaches the pre-Zeroth
      three-element Laws, contradicting `00-APEX.md` at HEAD. A prior sweep
      proves the surface was known. The wider finding (AW2) is that at least
      seven in-repo apex restatements describe the superseded shape, while the
      queued propagation item covers children's floors only — so the rest is
      silently stale, against the sweep-in-the-same-commit rule the delta
      itself cites. Verdict:
      [apex Zeroth Law cold pass](reviews/2026-07-26-2215-apex-zeroth-law-cold.md).
      **RULED 2026-08-04 (Mike): fix the skill's apex block AND widen the
      restatement-sweep checklist to the plugin surfaces (skills/,
      commands/)** — the second miss of the same class ends here, and the
      widened checklist is the instrument the planned removal below will
      itself need. Work owed: one small fix item.
- [ ] 🎯 **The Three Laws and the Zeroth are coming OUT of the apex (Mike,
      2026-08-04) — a later sitting, his act.** Stated while ruling the ZL
      pass: *"I plan to remove the 3 laws and the zeroth law, we will do
      that later."* Nothing removed yet; the apex stands as landed until
      that sitting. **ZL2–ZL5 lapse into this removal** (no wording fix for
      text slated to go): the excerpt-precedence line, the inaction-duty
      scoping sentence, the Law-3 characterisation and the rewrap all die
      with the section. The removal, when it runs, needs the ZL1-widened
      sweep checklist (every restatement surface, including plugin
      surfaces and children's floor blocks via the propagation lane) and is
      principal-authored apex doctrine — reviewed accordingly at landing.

### Coverage the programme does not yet reach

- **Three public repos in the account have no scanning at all** → § *the ranked
  residual* item 3 below. Public and unscanned is the combination that matters:
  the question is not "are they tidy" but "is anything in a public repo that
  should not be public".
- **The boundary findings** — the only open items with real exposure →
  § *Boundary findings surfaced by the measurement* below.

## Enforcement propagation — the estate rollout (ADR 0008, 2026-07-25)

**Rolled out 2026-07-25.** All 13 children call the floor; `floorfleet --remote
--check` exits 0 against GitHub's default branches. Proven live in CI, not just
locally: one child's floor run passed, another failed on a real `leakscan`
finding — the workflow itself ran clean in both, which is the end-to-end proof
the mechanism works.

> 📦 **2 completed items** in this section → [`ROADMAP-DONE.md`](ROADMAP-DONE.md)
>   (the 13-repo wiring, and the repo-specific scoping preserved with it).

- [ ] 🎯 REVIEWED 2026-07-26 (rule-4 Fable cold pass): PASS-WITH-FINDINGS
      3M/5m/1L/1n — [verdict](reviews/2026-07-26-2215-adr0008-enforcement-propagation-cold.md);
      **EP1–EP10 RULED 2026-08-04 (Mike, plain-language walk-through) — and
      the sitting then found the MAJORs' substance already closed.** Track A
      (2026-07-27, A1–A3) had ruled and applied EP1(a)+(c), EP2-at-the-
      mechanism, and EP3 (the hook template carries `--require-terms`,
      `floor.py:314`); this entry's "EP1–EP10 await Mike's ruling" was
      therefore stale for the MAJORs — the cycle-state residue class again,
      in wording too coarse for `pointerscan` to parse. **What today's
      ruling actually adds: EP1(b)** — a stated reason to `scope`/`flags` a
      never-softened scanner, exactly as `disabled` requires. It was
      deferred 2026-07-27 to ride C1's schema change and did not ride it
      (verified absent at HEAD); Mike ruled it IN today, no longer deferred.
      **And EP4–EP10, all as counselled** (pin needs both edits + honest board
      wording; selftest loop gains `--root repo` + a decided proving story
      for `local` checks; the ADR gains its seam clause and the
      floating-`@main` control clause — the control is atelier `main`'s own
      protection; trigger-shape joins the concession; a `python3` guard;
      the prove-it-landed command prints `core.hooksPath`). **Work owed:
      one application build item; the MAJORs keep the cycle open, so the
      application earns its own rule-4 cold pass and queues the pointer at
      landing.** State before this ruling: reviewed. The pre-review wording this item carried (a
      reviewer agenda with a seeded question) was the pointer-grammar corpus's
      last live specimen; stripped 2026-08-03 on `pointerscan`'s day-one
      warning, exactly as the FUNDED build's entry said it should be.
      **⚠️ An Opus pass ran on 2026-07-26 0647 UTC and was NOT ACCEPTED** — reviews
      run on the wrong tier (Mike, 2026-07-26): cold review passes are Fable's;
      the accepted Fable pass is the verdict linked above. The withdrawn pass
      is preserved as history under `docs/reviews/withdrawn/` and its findings
      die with it.
- [ ] **Two children were bootstrapped with `--no-verify`** — the gate they were
      installing already failed on their pre-existing content, so it blocked its
      own installation. Once is the honest resolution; twice would not be. Both
      commits say so in full and list what was found. **Their reds are now their
      own work**: broken internal links (repo-root-relative paths written inside
      `docs/` files two levels deep), decision records with no review line, and
      in one case a credential-shaped string repeated across records that needs
      eyes rather than an exemption. Deliberately not fixed by the rollout —
      another repo's records are its own call.
- [ ] **Retire the advisory declarations** as each repo re-baselines. The board
      shows them; that is the point. An advisory that is still there in a month
      is the "honour it manually" failure wearing a new hat.

### Boundary findings surfaced by the measurement — triage separately

These are **real findings the guards were never run to catch**, not rollout
blockers to wave through. Each needs eyes before its repo can go green.

- [ ] **The four archetypes need naming as a class.** Every defect above, and
      both false positives already recorded below, are the same error: a rule
      deciding on a *fragment* of a value instead of its *whole shape*. Worth
      stating once in doctrine rather than four times in code comments, if a
      fifth instance appears.

Deliberately generic here: atelier is public, so naming which private repo holds
committed credentials — and in which file — is reconnaissance, not a record. The
per-repo detail belongs in the operator's private estate-root repo, and the
triage list lives there. Only the *classes* are named below, because the classes
are what generalise to any adopter.

> 📦 **1 completed item** in this section → [`ROADMAP-DONE.md`](ROADMAP-DONE.md)
>   (the tracked data export — ruled, executed, and the three things its triage
>   surfaced that the original entry could not have known).

- [ ] **`assigned-secret` findings in service configuration.** Self-hosted
      service configs with credential-shaped assignments. Same tree; the usual
      right answer is a secret-store or env reference, plus rotation if the value
      was ever real.
- [ ] **Structural `leakscan` reds across several private repos.** Expected for
      an estate whose repos legitimately contain address/phone/network shapes as
      *content*. Each needs a scoping or allow decision; leakscan has no advisory
      form by design, so there is no wave-through.
- [ ] **A `private-key-header` that was prose, not key material** — BEGIN and END
      markers on one line, no base64 body: documentation describing a key file's
      format. Resolved; wants an allow-marker, never rotation. Recorded because
      it is the archetypal false positive of this rule and will recur.
- [ ] **Two clock times side by side read as an IPv6 address** (found 2026-07-26,
      writing a CHANGELOG line about a CLI that prints a time span). `HH:MM:SS to
      HH:MM:SS` trips the structural `ipv6` rule twice. Same archetypal-false-
      positive class as the bullet above, and it will recur wherever a record
      quotes a rendered time range. Resolved that day by **describing the format
      instead of quoting it** — the cheaper move, and the one that leaves no
      exemption behind. The triage question is **RULED 2026-08-04 via E7's D2
      (Mike)**: tighten the rule — `::` or four-plus groups — rather than rely
      on describe-don't-quote alone; the sweep confirmed the FP class is wider
      than clock times (port maps, ratios, hex colour triplets). Rides the E7
      leakscan build item.

### Candidate invariant — the public-record join, breached three times

- [ ] **Mechanise the private-repo × posture join** (anti-slop invariant
      registry). `RECORD.md` already says keep private repos generic, and the
      2026-07-12 review sharpened the harmful class to the **join** — a private
      repo's name sitting next to its debt or security posture, not the name
      alone. It has now been breached three times (2026-07-11, 2026-07-12,
      2026-07-25), every time at the identical moment: *summarising fleet-wide
      scan state into an atelier record*. The rule is not unclear; it loses to
      the fact that the generic form is harder to write while holding a concrete
      finding list in mind.
      **No existing scanner can catch it** — a repo name beside a file path is
      neither personal data nor a credential, so leakscan and secretscan both
      pass it. It sits squarely in the judgement residual `tools/README.md`
      declares, which is exactly the shape the registry exists to promote to an
      always-on check. Sketch: flag a private-sibling repo name (discoverable via
      `pins.discover`) co-occurring with finding-shaped vocabulary in `docs/`,
      with an allow-marker for the deliberate worked examples. Needs a review
      before wiring — the false-positive surface is prose, and this repo's own
      doctrine names sibling repos legitimately.

### To be considered — the ranked residual after the rollout (Mike, 2026-07-25)

What is *not* covered now that policy propagates by call. Ranked by how much
real protection each would add. Item 1 has its own section below with four
costed options; the rest are recorded here with their reasoning so the next
session inherits the thinking rather than re-deriving it.

**1. Nothing runs `floorfleet` automatically** — the biggest structural gap. The
enumerator exists and was never scheduled. Fully specified in the section
immediately below (four options, one of them explicitly rejected).

**2. A red CI does not actually stop anything — and the obvious fix is wrong.**
The instinctive answer is branch protection with required status checks. Two
findings, one of them a reversal worth recording:

- The **private children cannot have branch protection at all** — GitHub gates
  it behind Pro for private repos. So this is a *spending* decision before it is
  a technical one.
- **atelier can, free, and currently has none.**

  🚩 **Recommendation reversed after thinking it through: do NOT enable it on
  atelier.** Required status checks block direct pushes to `main` until CI
  passes, and this estate deliberately runs commit-small-push-fast to main. It
  would mean waiting on a runner for every commit, or routing one-line doc fixes
  through PRs — a large, permanent tax on the working rhythm to catch a case the
  pre-commit hook already catches earlier, at commit time.

  **The honest framing to carry forward:** the floor is enforced *at commit time*
  by the hook; CI is the backstop, not the gate. That is a defensible design, and
  it should be stated rather than left implicit — because its corollary is that
  **`--no-verify` is the real hole**, and it was used twice during the rollout
  itself (both times deliberately, both times recorded in the commit message).
  Anyone revisiting this should decide whether that hole is acceptable, not
  assume it away.

**3. Three PUBLIC repos in the account have no scanning at all** —
`cel-web-hosting`, `fpx`, `homelablabelmaker`. They were never atelier children
(no `CLAUDE.md`, no pin), so `floorfleet` correctly does not report them: it
reports children, and these are not. Naming them here is not the private-repo ×
posture join — they are public, so the absence of a workflow file is already
visible to anyone. **Whether to adopt them is a scope decision, not a defect
fix.** The relevant question is not "are they tidy" but "is anything in a public
repo that should not be public", which is exactly what the scanners answer.

**4. A blind spot worth closing cheaply.** **CLOSED 2026-07-28 as B3** — and
the proposed shape was costlier than it needed to be. The suggestion was one
`gh api repos/{owner}/{repo}/actions/permissions` call per child; that endpoint
requires GitHub's **Administration** permission, which is the repo-*settings*
permission, so taking it would have widened the scheduled check's token across
the whole private estate for one boolean. It is used when the token happens to
carry it and inferred from run history when it does not — a floor that has never
run is the same practical absence whatever switched it off — and the board
declares which authority answered. Detail →
[`ROADMAP-DONE.md`](ROADMAP-DONE.md).

**5. `advisory` needs a stated reason and an expiry.** `disabled` requires a
reason; `advisory` does not, and neither carries a review date. So an advisory
declaration can sit indefinitely — **the "honour it manually" decay in a new
costume**, which is the precise failure ADR 0008 exists to end. Fix shape: make
`advisory` take `{scanner: reason}` like `disabled`, add an optional
`review-by` date, and have `floorfleet` flag any advisory past its date (or with
no date) so the board ages them rather than accumulating them silently.

### 🎯 Schedule the conformance check — the last structural gap (Mike, 2026-07-25)

**The gap, stated plainly:** `floorfleet` is the instrument that turns "I hope
the policy propagated" into "I know it did" — and nothing runs it. It only knows
when a human types the command. That is the same shape as the defect this whole
change fixed: a guard that exists, works, and is pointed at nothing.

**What it would catch that nothing else does.** A child's `floor.yml` edited back
into a copy or deleted · a fresh clone (or a new laptop) where nobody ran
`git config core.hooksPath` · a child that pins `@<sha>` and quietly freezes
propagation · a new repo that never adopted the floor at all. Every one of those
is an *absence*, and an absence never raises its hand.

**The constraint that makes this a decision rather than a task.** atelier's CI
runs on a GitHub runner with no access to the private children. Reading their
default branches needs a token — a fine-grained, read-only (`contents` +
`metadata`), expiring PAT scoped to exactly those repos. That is a new credential
and a new trust surface: **an always-confirm floor action, and the minting is
Mike's, never the agent's.**

Four ways, same goal, very different blast radius:

**RULED AND BUILT 2026-07-28 — Mike chose B**, the scheduled workflow in the
private estate-root repo. A (token in atelier's public CI) and C (local cron)
closed unchosen; D (the session-close ritual) stayed rejected. All four options
are preserved verbatim with their dispositions in
[`ROADMAP-DONE.md`](ROADMAP-DONE.md), because a decision is only legible beside
what it was chosen over.

**B1 IS LIVE — token minted and the job PROVEN end to end (2026-07-28).** Mike
minted `FLOORFLEET_TOKEN` (fine-grained, read-only, expires 2026-10-27, all
repos, read on actions + code + metadata, no user permissions, **no
Administration**) and set it in the estate-root repo's secret store. A
`workflow_dispatch` run then proved the whole path on a runner with **no local
clones**: 13 children plus the parent enumerated from GitHub, every run status
read, exit 1 on the five red floors — failing for the right reason, which is the
only kind of red worth having. Detail →
[`ROADMAP-DONE.md`](ROADMAP-DONE.md).

> 🔎 **The degraded-authority path proved itself in production, not just in
> tests.** The board printed *"Actions-off was INFERRED (not read) for 14
> repo(s)"* — the token deliberately lacks `Administration: read`, so the check
> fell back to run history **and said so on the board** rather than letting a
> reader assume the stronger authority. That was the design argument for
> declining the wider permission; it is now a demonstrated fact.

**What the item got wrong, worth keeping.** It costed the work as "small: the
schedule, `--check` wiring, and a failure message". The premise was that
`--remote` was remote end-to-end. It was not: `--remote` read each repo's
*content* from GitHub and still *discovered* children by listing directories
beside the atelier checkout, so on a GitHub runner it would have found nothing
and exited 2 — fail-safe, but not a check. That is the same class as everything
else this programme keeps finding, one level further out: **the estate this
board could see was the estate that happened to be cloned on one laptop.**
`--from-github` was the real work, and it closes the tool's own documented
blind spot as a side effect.

### Licence gate — ENABLED estate-wide (Mike ruled 2026-07-25)

Mike overruled an earlier deferral of mine, and was right to: I had weighed the
gate as *tidiness* for private repos. His framing — **"I want the licence gate
enabled so those repos are ready to publish"** — is protection, not
housekeeping. Publish-readiness is the whole point of the gate; deferring it
until a repo is already public is backwards.

**Landed on 11 of 13.** 10 declare `Apache-2.0` and pass; 3 are `disabled` with
a stated reason (below); one needed a false-positive marker.

> 📦 **2 completed items** in this section → [`ROADMAP-DONE.md`](ROADMAP-DONE.md)

- [ ] **licenscan gap — support proprietary / `LicenseRef-*` licences.**
      A proprietary repo going public is *precisely* when copyleft-contamination
      detection matters most, and today the tool is **silent exactly there**.

      **Reproduction (2026-07-25, run before disabling the gate on 3 repos).**
      A fixture with a proprietary `LICENSE` ("ALL RIGHTS RESERVED") plus a
      source file carrying an SPDX header declaring GPL-2.0 (written literally in
      the fixture, described here — a real tag in this file trips licenscan, as
      it did on the first draft of this entry):

      - `licenscan --expect LicenseRef-Proprietary .` reports **one** finding —
        `LICENSE:1 [unknown-license]` — and **never mentions the GPL file**. It
        stops at "repo licence unrecognised" and verifies nothing further.
      - Appending `licenscan:allow:` to the LICENSE line does **not** restore
        the file-header checks: the finding persists and the GPL file stays
        invisible. So there is no in-repo workaround; the fix must be in the tool.

      **Why this is a real hole, not a cosmetic one.** A vendored strong-copyleft
      file cannot be relicensed on the way out. In an Apache repo licenscan
      catches that; in a proprietary repo — the one most likely to be scrubbed
      and published deliberately — it catches nothing, while *appearing* to be a
      configured gate. A check that is off is a decision; a check that runs and
      covers nothing is the failure class this repo keeps closing.

      **Fix shape.** Accept an unrecognised or `LicenseRef-*` repo licence as a
      *declared* licence: skip the "which known SPDX licence is this" comparison
      (which genuinely cannot be answered), and still run the per-file header
      incompatibility checks, which do not depend on recognising the repo
      licence — only on knowing it is not the copyleft one found. **Test to
      write with it:** the fixture above must report the GPL file.

      **Unblocks the 3 repos currently `disabled` with a stated reason**, and
      those declarations should be retired in the same change rather than left
      standing (see the advisory/disabled ageing item).
- [ ] **licenscan gap — map known PyPI trove classifiers to SPDX ids.**
      `"License :: OSI Approved :: Apache Software License"` is the **correct**
      PyPI trove classifier for Apache-2.0 — established packaging practice, not
      an error — but licenscan reads it as an unrecognised declaration and blocks.

      **Evidence (2026-07-25).** One child hit this with a `pyproject.toml` that
      *already* carried a correct SPDX `license` field; the classifier beside it
      was flagged anyway. Marked in place with the reason, because the repo was
      right and the tool was wrong.

      **Why it matters beyond one repo.** Every Python package in the estate will
      carry these classifiers, so this recurs by construction — and each recurrence
      trains someone to reach for an allow-marker on a *correct* line, which is
      how a scanner's findings stop being believed.

      **Fix shape.** A small lookup from the OSI-approved trove classifier strings
      to their SPDX ids, applied before the unrecognised-declaration check. The
      set is small, stable and published. Where a classifier is genuinely
      ambiguous (a family name covering several versions), degrade to the existing
      unknown-declaration *warn* rather than guessing a version — friction, never
      a silent pass. **Test to write with it:** the Apache trove classifier
      alongside an Apache-2.0 `license` field reports clean.
- [ ] **2 repos still owe the declaration — blocked by their own reds.** Their
      hooks refused the commit on pre-existing findings (broken internal links,
      decision records with no review line). **Deliberately not forced:** those
      two were already bootstrapped past their gate once with `--no-verify`, and
      once is the honest resolution while twice is a habit. They get the licence
      gate when they clear their existing findings — which is the forcing
      function working exactly as designed, not a rollout failure.

### For your consideration — ideas raised this session, not yet decided (2026-07-25)

- [ ] 🎯 **Doctrine candidate — bulk deletion from a record store is a
      show-first action, regardless of who created the mess.** Grounded in a
      worked example from this session: I created 185 lines of duplicate roadmap
      sections, then removed them having compared **heading names only**, and
      asserted "duplicates" in the commit message without diffing a single body.
      Mike challenged it. The diff took thirty seconds and showed three sections
      byte-identical, one correctly superseded — and **one a genuine loss**, a
      completed item whose only roadmap trace went with it.

      Two things made it feel safe and neither holds:

      - *"It's my own mess."* The sections encoded **Mike's** rulings, not my
        drafts. Deleting the record of another party's decisions is a different
        act from deleting your own working notes, and the distinction was not
        made.
      - *"It's recoverable — git remembers."* Git remembers the text; it does not
        remember that the work was supposed to happen. **A roadmap item that
        vanishes means the work does not get done**, which is closer to
        irreversible than the mechanism suggests. Recoverability of *bytes* is
        the wrong test for a record store.

      Proposed rule: before removing a block from a record store (ROADMAP,
      SESSIONS, ADRs, reviews), either diff it and show what goes, or ask. One
      message, and it removes the class. **Mike's call** — it narrows agent
      autonomy in a place the standing grant currently covers, so it is his to
      make, not something to self-adopt.

Suggestions the rollout surfaced that were never queued. None is urgent; each is
recorded so it is a **choice** rather than something that quietly evaporates.

- [ ] **Adoption is a chicken-and-egg problem and I improvised twice.** A repo
      whose existing content already fails the gate **cannot commit the change
      that installs the gate**. It happened on two repos and I resolved it with a
      one-time `--no-verify`, documented in each commit — defensible once, but it
      is now an undocumented pattern that will recur on *every* future adoption
      (including the 3 public repos, if adopted). Idea: a documented adoption
      path — either a sanctioned one-time bootstrap, or an `--adopt` mode that
      installs the hygiene checks advisory-first and tightens once the repo
      re-baselines. **Decide the pattern before the next adoption, not during
      it.**

- [ ] **`--no-verify` is the real hole, and nothing sees it.** With CI as a
      backstop rather than a gate (see the ranked residual, item 2), a local
      bypass is the one route that reaches history unscanned. I used it twice in
      one night. Idea: make it *visible* rather than impossible — e.g. CI flags a
      pushed commit that would not have passed the hook, so a bypass is a
      recorded event rather than a private one. Worth weighing against the
      obvious counter: it is also the legitimate escape hatch, and making it
      painful invites worse workarounds.

The **tracked-shim check** landed 2026-07-26 — `floorfleet` now reports
`shim:` (a repo fact, so `--remote` carries it estate-wide; all 13 children
`current`) separately from `hook:` (still machine-local, since
`core.hooksPath` never travels) → detail in
[`ROADMAP-DONE.md`](ROADMAP-DONE.md).

The **suggested-fix** strand closed 2026-07-26: `linkscan` now prints the
replacement path where it is uniquely computable, advisory-only (`b89a306`)
→ detail in [`ROADMAP-DONE.md`](ROADMAP-DONE.md).

## 🤔 Trust-failure handling as a skill — idea to consider (Mike, 2026-08-02)

- [ ] **When a trust failure occurs in-session, handle it deterministically —
      with a skill (enforced actions, code), not doctrine (policy the agent may
      or may not apply under the same pressure that caused the failure).**
      Captured verbatim from Mike; not yet designed or decided.

      **The class it targets.** A *trust failure* is the moment the collaboration's
      evidence chain breaks: an all-clear reported past its evidence (the pushed
      floor was red for ~19 h while "9/9, exit 0" was being reported,
      2026-07-26) · a capability claim made unlooked ("no existing tool reports
      this" the day after the tool shipped, 2026-07-26) · a deletion asserted as
      safe with the diff never taken (the 185-line "duplicates" removal,
      2026-07-25). `00-APEX.md` names the stakes — a false "it works" poisons
      trust in every other report — but **nothing prescribes what happens
      next**: today the recovery (own it, re-verify, record it, correct the
      records) is doctrine the failing agent applies to itself, which is exactly
      the fail-open shape ADR 0008 exists to end.

      **Why a skill.** Same argument as the policy-as-code programme, one layer
      up: doctrine asks the agent to remember under pressure; a skill makes the
      recovery a *procedure* — invoked at the moment of failure, steps enforced
      in order, outputs (incident note, re-verification, record corrections,
      SESSIONS entry) produced as artefacts rather than promised. It also makes
      failures **instrumentable**: a consistent record shape means recurrence
      can be counted, which feeds the anti-slop invariant registry (repeat
      offences → always-on checks).

      **Open questions for the design pass (not answered here):**
      - Trigger: self-invoked on realising the failure? Mike-invoked? Or wired
        to a detector (e.g. CI catching a claim the hook would have failed)?
      - Scope: atelier-only, or estate-wide via the child-repo skill channel?
      - What's *enforced* vs *recorded* — can a skill actually gate anything, or
        is its value the deterministic checklist + artefact trail?
      - Relationship to `EVIDENCE.md` (the ladder the failure skipped) and
        `RECORD.md`'s all-clear rule — the skill would operationalise both, not
        duplicate them.

## 🤔 A fourth rung for the credential ladder — no credential at rest (Mike, 2026-08-03)

- [ ] **Extend the credential preference ladder so the standing credential is
      not the only honest answer where the platform offers no JIT grant.
      Where a credential is used *irregularly or rarely*, doctrine should name
      an alternative in Mike's words: "delete the credential entirely and make
      its rebuild cheap, automated and tested".** Captured from Mike; not yet
      designed or decided.

      **What doctrine says today.** `method/SECRETS.md` § *The credential triad*
      ranks least-privilege → just-in-time → short-lived, then concedes that
      most platforms offer neither of the last two, so standing credentials are
      "the common honest reality" — allowed as a **tracked debt to shorten**
      with a stated reason. `method/PRINCIPLES.md` §5 carries the same bridge
      (*honest pattern*, and the checklist line "Standing or ephemeral
      credential?"). Both stop at *track the debt*.

      **The gap.** Between "standing forever, tracked" and "the platform grants
      JIT" there is a third state the doctrine never offers: the credential
      simply **does not exist between uses**. Mint it for the run, delete it
      after, keep the mint automated and exercised. A credential that isn't
      there is just-in-time to the extent the platform allows — achieved by the
      *holder*, not granted by the vendor — and the debt is paid rather than
      carried. Cheap to reach precisely where use is infrequent, which is also
      where a standing credential sits idle and unwatched longest.

      **It is already implied and never stated.** SECRETS' enabling property is
      store-the-rule-not-the-value: what's durable is the *procedure to mint*,
      not a frozen token. If that holds, the value's continued existence between
      uses is an unforced choice — but nothing says so, so every session lands
      on "standing, tracked" as the terminal state.

      **Open questions for the design pass (not answered here):**
      - Where does it sit? A fourth rung *below* the triad (JIT/short-lived
        remain better when the platform offers them), or a branch off the
        bridge rule that fires on the use-frequency test?
      - What makes a rebuild admissible — automated, tested, and *rehearsed on
        a cadence*? An untested rebuild path converts a standing-credential
        risk into an outage risk, which is a trade, not a win.
      - The bootstrap recursion: the rebuild path itself authenticates with
        something. Deleting the leaf while the minting credential stands is
        still progress, but the ladder must say so rather than imply the
        regress terminates.
      - Frequency boundary: at what cadence does mint-per-use stop being
        "rebuild on demand" and become plain JIT (and stop needing its own
        rung)?
      - Interaction with rotation-on-cadence (SECRETS § *Rotation cadence*):
        a credential that never persists has no undetected-exposure window to
        bound, so does the cadence duty lapse or transfer to the mint path?

      **Grounding, honestly.** Raised from a sibling session's ADR arguing
      exactly this for a backup tool on a platform whose delegation grant is
      standing-only — no JIT, no expiry — where the credential is deleted after
      each run and rebuilt from a tested, automated path. That is one worked
      case in a child repo, not yet an atelier-side pattern; the design pass
      owes a second instance or an explicit one-case claim before it becomes
      doctrine (`create-repo`'s stub-don't-fabricate rule, and the
      grounding bar in `CLAUDE.md`).

## Doctrine — review-owed

- ⏳ **Rule-4 review queued (tier: Fable; pass type: code/design cold pass) —
  the pointer-grammar build + the B4 `harvestscan` wiring (one build, HV2;
  the B4 cycle's MAJOR keeps that cycle open past this application).**
  *Delta:* `tools/pointerscan.py` + `tools/test_pointerscan.py` (new);
  `tools/harvestscan.py` + `tools/test_harvestscan.py` (HV1 scope, HV2–HV4
  folds, `--replay`); the two registry entries in `tools/floor.py` +
  `tools/test_floor.py`; `tools/README.md`; `CHANGELOG.md`; the three
  specimen fixes in this file (all landed 2026-08-03, this merge).
  *Intent record:* [`ROADMAP-DONE.md`](ROADMAP-DONE.md) § *The ⏳ pointer
  grammar mechanised* (the FUNDED entry + corrections, harvested at landing)
  + the [B4 cold pass](reviews/2026-07-29-1306-b4-harvestscan-cold.md)
  rulings HV1–HV5 (Mike, 2026-07-29).

- ⏳ **Rule-4 review queued (tier: Fable) — the FS1–FS5 application on
  `floorfleet` (the B2+B3 cycle's application pass; the FS1 MAJOR keeps the
  cycle open past it).** *Delta:* `tools/floorfleet.py` +
  `tools/test_floorfleet.py` (landed 2026-08-03, this merge) — the
  discovery-authority footer + `--json` field, the three-outcome remote
  read with `unknown` rows that red `--check`, the token-spec statement in
  four surfaces, the wired-denominator headline, the archived/unreadable
  footer counts, the `green("")` docstring + selftest legs, and one
  out-of-scope crash fix (a repo with no floor config felled `render`;
  advisory initialised as a list where every reader expects the C1 dict).
  *Intent record:*
  [B2+B3 cold pass](reviews/2026-07-29-1251-b2b3-floorfleet-status-cold.md)
  rulings FS1–FS5 (Mike, 2026-07-29) + the harvested ruling entry in
  [`ROADMAP-DONE.md`](ROADMAP-DONE.md) § *B2+B3 FS rulings applied*.

- ⏳ **Rule-4 review queued (tier: Fable) — the mid-tier standing-executor
  doctrine.** *Delta:* `docs/method/ECONOMICS.md` § *The orchestrated-run
  tier split*, the standing-executor paragraph (landed 2026-08-03, this
  merge). *Intent record:* [`ROADMAP-DONE.md`](ROADMAP-DONE.md)
  § *Third-seat executor trial* (runs 1–4, 2026-07-23) + Mike's trial
  instruction of 2026-07-23 (`dadde1d`).

- ⏳ **Rule-4 review queued (tier: Fable) — the E6 application, E6a + E6c
  slices.** *Delta:* `docs/method/SECRETS.md` § *The boundary's posture —
  over-flag, because detection enables everything* (landed 2026-08-03); the
  E6c/SF carve-outs + canary suite in `tools/secretscan.py` +
  `tools/test_secretscan.py` (landed 2026-08-03); the specimen allow-marker
  in the SF verdict and the triage record's dated correction (same merge).
  *Intent record:* ROADMAP Track E § E6 (Mike's rulings 2026-07-28) + the
  [E6 intent cold pass](reviews/2026-07-29-1243-e6-intent-cold.md) rulings
  EI1–EI6 (2026-07-29) + the
  [SF verdict](reviews/2026-07-28-1220-secretscan-fragment-cold.md) rulings
  (2026-07-28).

- ⏳ **Rule-4 review queued (tier: Fable) — the landing-equals-bookkeeping
  preamble clauses.** *Delta:* the two new sentences in this file's
  checkbox-states preamble paragraph — the `[x]`/harvest single commit, and
  the inline-claim close (landed 2026-08-03, the enacting commit is named in
  the session record). *Intent record:* the harvested entry in
  [`ROADMAP-DONE.md`](ROADMAP-DONE.md) § *Doctrine — the harvest rides the
  `[x]` commit* + the SESSIONS.md entry of 2026-08-03 (orchestrated run).



- [ ] 🎯 **Write down which tier reviews — the rule exists in practice and
  nowhere as a rule** (Mike's ruling, 2026-07-26, after an Opus session took
  three `⏳` items and had the whole pass rejected on tier grounds). The
  convention is real and consistent: `SESSIONS.md` shows an unbroken run of
  `(Fable)` cold-review entries, and `REVIEW.md` already quotes Mike's
  2026-07-18 ruling naming *"Fable reviewers"* — but it is quoted inside *Review
  the design, not only the build*, where it is doing different work (arguing
  reviewers test thinking and architecture, not only code). Nothing states
  **cold review passes run on Fable** as a rule a session must satisfy before
  taking a `⏳` item. `ECONOMICS.md` § *One doctrine, tiered authority* frames
  tier as a risk call and stops short of naming the reviewer tier; `REVIEW.md`
  says "match reviewer capability to the stakes" without saying what that
  resolves to here. **This is the rule-grammar failure this repo already has a
  name for** (REVIEW.md — *"When a written rule keeps being broken, suspect its
  framing before its enforcement"*): the fact was on the page and was not
  findable *as a rule* from where the reader stood. **Fix shape:** state it at
  the point of use — in `REVIEW.md` beside rule 4's spawn criterion (the moment a
  session decides whether it may take a `⏳` item) and in the ROADMAP header's
  `⏳` legend, so tier is checked at *selection*, not discovered at rejection.
  Worth deciding at the same time: whether the tier bar is Fable-specific or
  "the tier the principal names per run" (`ECONOMICS.md`'s existing shape), and
  whether a session that cannot honour it should stop rather than proceed.
  Self-authored doctrine when it lands ⇒ rule-4 `⏳` at landing — **and that
  review is Fable's.**

- [ ] 🎯 **Promote the withdrawn-pass convention into `REVIEW.md`, or leave it
  local** (Mike's ruling, 2026-07-26: a rejected pass's outputs happened, and we
  do not rewrite history — recover them, keep them, make them unreadable as
  "done"). The handling is now written and live in
  [`reviews/withdrawn/README.md`](reviews/withdrawn/README.md): preserved
  verbatim under a `⛔ WITHDRAWN` banner, quarantined out of `docs/reviews/`,
  never handed to a taker as a queue ref, read-after-your-own-verdict-not-before,
  and *findings die with the pass*. Open question is whether that is a directory
  convention or doctrine — it decides the general case (a pass rejected on
  content, on scope, or half-finished), and it sits directly against rule 2's
  contamination bar, so promoting it is a doctrine act. Self-authored if
  promoted ⇒ rule-4 `⏳` at landing.

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
- [ ] **Define *complex* vs *complicated* in the glossary** — an action for Mike
  with the agent's help, to do later. Intended distinction (seed only, Mike to
  rule the final wording): *complicated* = many parts but knowable and
  ordered — hard, yet decomposable and predictable; *complex* = interdependent
  parts with emergent, path-dependent behaviour you can't fully predict from the
  pieces (Cynefin-style split). Do not encode until the ratify pass. (Mike,
  2026-07-24.)
- 🎯 REVIEWED 2026-07-26 (rule-4 Fable cold pass): PASS-WITH-FINDINGS 0M/3m/3n
  — [verdict](reviews/2026-07-26-2215-evidence-escalation-rung-cold.md); EE1–EE6
  await Mike's ruling (rule 3; no MAJOR ⇒ the ruling application is terminal).
  **Capture → doctrine: escalating to the principal is not a rung on the
  acquisition ladder** — APPLIED 2026-07-26 (this session, Opus, after the
  principal's correction). `EVIDENCE.md` §13 gained a paragraph before its
  blocked-from-climbing clause: handing a missing value up sits *beside* the
  ladder, not on it, and is reached only when the climb is genuinely blocked —
  the test before escalating is whether an authoritative source exists and has
  been consulted. **Review queued at landing** (self-authored doctrine,
  REVIEW rule 4) — **taken**; the verdict is above. *Delta:* the `EVIDENCE.md`
  §13 paragraph (landed this commit).
  *Intent record:* [`2026-07-26-0100-ccrepo-context-column.md`](sessions/2026-07-26-0100-ccrepo-context-column.md)
  § Addendum.
- 🎯 REVIEWED 2026-07-26 (rule-4 Fable cold pass): PASS-WITH-FINDINGS 1M/4m
  — [verdict](reviews/2026-07-26-2215-record-pushed-floor-cold.md); RF1–RF5
  await Mike's ruling (rule 3; the MAJOR keeps the cycle open past the
  application). **Capture → doctrine: the close all-clear carries the pushed floor run's
  result** — APPLIED 2026-07-23 (queue run 0959, inline Opus). RECORD.md's
  all-clear evidence rule gained a sub-point: when a close pushes, the evidence
  is the *floor at head*, not the local scan ("green locally, floor run pending"
  is honest; "all green" before the head run reports is a claim past its
  evidence). **Review queued at landing** (self-authored doctrine, REVIEW
  rule 4) — **taken**; the verdict is above. *Delta:* the RECORD.md all-clear
  "floor at head" sub-point (landed this
  commit). *Intent record:* this capture line + its grounding (`165c40f`: a 00:47
  close pushed a 🎯-closed item and left the floor red — reviewscan since 00:06 +
  an un-harvested `[x]` — and the next session inherited the debt to restore
  green).
- 🎯 REVIEWED 2026-07-26 (rule-4 Fable cold pass): PASS-WITH-FINDINGS 0M/3m/2n
  — [verdict](reviews/2026-07-26-2215-apex-accountability-cold.md); AA1–AA5
  await Mike's ruling (rule 3; no MAJOR ⇒ the ruling application is terminal).
  **Apex: the principal's authority is rooted in accountability** — APPLIED
  2026-07-24 (this session, Opus, at Mike's instruction). `00-APEX.md` § "The
  principal's authority is conditioned on being informed" gained an opening
  grounding paragraph: the authority is *rooted in accountability* (RASCI
  *Accountable*) — the principal funds the work, the world attributes the product
  to him, and the liabilities (privacy, copyright/IP, licence/contract) fall on
  him; the reserved decisions are his *because their consequences are*. The
  section previously asserted the reservation without naming its source.
  **Review queued at landing** (self-authored apex doctrine, REVIEW rule 4) —
  **taken**; the verdict is above.
  *Delta:* the accountability-grounding paragraph (landed this commit). *Intent
  record:* Mike's reading that the principal's authority is born of the
  principal's accountability.
- 🎯 REVIEWED 2026-07-26 (rule-4 Fable cold pass): PASS-WITH-FINDINGS 1M/2m/2n
  — [verdict](reviews/2026-07-26-2215-apex-zeroth-law-cold.md); ZL1–ZL5 await
  Mike's ruling (rule 3; the MAJOR — the session-onramp skill still teaches the
  pre-Zeroth Laws — keeps the cycle open past the application).
  **Apex: Asimov's Zeroth Law added above the Three Laws** — APPLIED
  2026-07-24 (this session, Opus, at Mike's instruction). `00-APEX.md` § "Then
  the Laws" gained the **Zeroth Law** — "The agent may not harm humanity or,
  through inaction, allow humanity to come to harm" — positioned *above* the
  three, read first, labelled "Zeroth" and deliberately **unnumbered** so it
  stands apart from the numbered three rather than joining them. The original
  three keep their 1–3 numbers *and* their original wording (no Zeroth
  subordination clause added to them — precedence is carried by position + the
  section prose; flagged to Mike as the one open micro-choice if he later wants
  Asimov's explicit "unless this conflicts with the Zeroth Law" clauses). The
  "Three Laws" title/language is retained; the caveat's ordering line now reads
  Zeroth → individual harm → obedience → self-preservation. **Decision history:**
  Mike first ruled *renumber (move-down-one)* via a decision prompt (applied
  `572dddd`), then changed his mind to this Zeroth form — so numbers 1/2/3 keep
  their historical meaning and the earlier "off-by-one against past records"
  concern is **void**. **Review queued at landing** (self-authored apex
  doctrine, REVIEW rule 4) — **taken**; the verdict is above.
  *Delta:* Zeroth law + prose in `00-APEX.md`;
  `README.md` + `method/README.md` restored to "Three Laws, with Asimov's Zeroth
  Law read above them". The `PROPAGATION.md` + `build/templates/CLAUDE.md`
  floor-ordering summary keeps "avoid harm to humanity → avoid harm to a person →
  obey → self-preserve" (accurate under the Zeroth; generic "the Laws" wording,
  no count claim). **Child floor propagation** rides the existing gated
  "Propagate the widened apex floor to the fleet children" item below.
- 🎯 REVIEWED 2026-07-26 (rule-4 Fable cold pass): PASS-WITH-FINDINGS 0M/3m/2n
  — [verdict](reviews/2026-07-26-2215-principles-way-out-cold.md); WO1–WO5
  await Mike's ruling (rule 3; no MAJOR ⇒ the ruling application is terminal).
  **PRINCIPLES §1: "Design the way out before the way in"** — APPLIED
  2026-07-24 (this session, Opus, at Mike's instruction). New resilience
  principle paired with "Build the way back before the way forward": before
  adopting an external dependency, first establish how you keep working without
  it (fallback / export path / swappable seam / degraded mode); adopt only once
  the exit exists. Grounded in atelier's own practice — zero-dependency tooling
  as the limit case, browser-fetch as the documented dependency exception — and
  cross-linked to REACH (escalate-cheapest-first, never mint access you can't
  withdraw). **Review queued at landing** (self-authored doctrine, REVIEW
  rule 4) — **taken**; the verdict is above. *Delta:* one bullet in
  `PRINCIPLES.md` §1.
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
- [ ] **Elevate the first-principles doctrine to atelier** (Mike, 2026-07-25) —
  a child repo (kāinga) holds a **first-principles / evaluation doctrine**; a
  prior session judged it *"may deserve elevation to atelier — it governs how any
  repo evaluates, not just kāinga"*, and **Mike agrees**. The argument for
  elevation is that *how you reason from first principles when evaluating*
  is a cross-repo concern (the shared `method/` layer), not a kāinga-local one.
  **Honest gap — stub, don't fabricate:** the doctrine's actual content is not in
  atelier and is not reproduced here; a future session must first **locate it in
  kāinga and understand it** before designing where it lands in `method/` (its
  own doc, or a section of PRINCIPLES/APEX) and how it grounds. Do NOT invent
  what "first principles" says to fill the heading. Self-authored doctrine when
  it moves ⇒ rule-4 ⏳ at landing; review WARRANTED at that point. Captured only
  for now. **Aligned meaning + teaching example (Mike, 2026-07-25):** boil a
  process down to the fundamental parts *you know are true* and build up from
  there — vs reasoning by analogy/convention. Canonical illustration to use in
  the doctrine: Musk/SpaceX — decompose a rocket to its raw-material cost (~2% of
  the finished price), conclude the rest is industry markup not physics, and
  build/reuse from fundamentals. The rigour (and the failure mode) lives in *"you
  know are true"* — correctly telling a real fundamental from a convention
  smuggled in as one. Pair this teaching example with kāinga's own grounded
  practice when writing the doctrine (external example illustrates; the
  atelier-grounding stays kāinga's real use — ground everything).
  **Why kāinga has this to give (Mike, 2026-07-25):** kāinga is at a
  **research stage** further out than any other child and reaches into areas
  (hardware) the rest don't — a frontier with little convention to copy *forces*
  first-principles reasoning, so its evaluation doctrine matured there first.
  This is the first concrete instance of the cross-repo up-flow captured below.
- [ ] **Cross-repo learning: atelier distils domain-diverse children (Mike,
  2026-07-25)** — a standing lens, not a build. atelier flows doctrine *down* to
  children (PROPAGATION); the complement is the **up-flow** — harvest each
  child's learnings and embed the ones that generalise so *all* repos, present
  and future, gain (atelier was itself extracted this way, mostly from ros).
  The engine is **deliberate domain diversity**: the children sit at different
  **constraint-walls**, so each teaches something the others structurally can't.
  Exemplars (all already named across these docs): **faves** = pure web/mobile,
  *no wall* — maximal software freedom; **tiki** = networking behind a *hardware
  wall* (device/host limits; even on AWS/GCP SDN, bounded by what the product
  allows); **kāinga** = *research frontier* (hardware + beyond) that forces
  first-principles work; **docker-heap** and the less-worked repos contribute as
  they mature. The value **compounds** — a learning proven under one domain's
  constraints, where it generalises, becomes shared truth fleet-wide; the more
  *different* the domains, the richer atelier gets. **The lens to apply when
  harvesting from any child:** "is this learning domain-specific, or a general
  truth atelier should hold for everyone?" May eventually be named explicitly in
  the README's "what atelier is" framing / `PROPAGATION.md` (the up-flow beside
  the down-flow); review WARRANTED if/when it moves to doctrine.
- [ ] **Principle: solve once, reuse the building block (Mike, 2026-07-25)** —
  solve a problem once, then compose from the blocks you already have; never
  re-solve a solved problem. Holds at two scopes:
  - **In-repo:** one implementation of a capability, many consumers — e.g. tiki
    writes the wire-protocol handling *once*, and every use case calls that
    module rather than re-deriving it. (Standard composability; atelier already
    holds its anti-duplication twin, *one fact, one home* — EVIDENCE §9 / V4.)
  - **Cross-repo:** the "building block" is also **intelligence and case-law**,
    not just code. A problem solved in one repo's domain becomes a reusable block
    for the others via three flows — **up** (child → atelier, e.g. first-
    principles elevating; the up-flow captured above), **down** (atelier →
    children, PROPAGATION), and **lateral** (child → child directly).
  **The unifying claim:** code primitives and knowledge primitives obey the
  **same solve-once law** — factor the reusable thing, then consume it, whether
  it is a function or a doctrine. This reframes what atelier *is*: the fleet's
  **shared library for knowledge** — what tiki's wire-protocol module is *within*
  tiki, atelier is for doctrine/case-law *across* the fleet. Already-held on the
  in-repo side (composability + one-fact-one-home); the new part is the
  cross-scope generalisation + the atelier-as-knowledge-library framing. Clusters
  with the two captures above; likely lands in `PRINCIPLES.md` (with a
  `PROPAGATION.md` cross-link for the flow topology). Review WARRANTED if/when it
  moves to doctrine.

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

**Third-seat executor trial — CONCLUDED 2026-08-03.** Four runs, nine
dispatched items, one failure; the promotion the data supported is now doctrine
(`ECONOMICS.md` § *The orchestrated-run tier split* — mid tier as standing
executor for well-floored known-pattern builds + prescriptively-reviewed fixes,
discriminator floor density; rule-4 `⏳` queued in § *Doctrine — review-owed*).
Run detail harvested verbatim → [`ROADMAP-DONE.md`](ROADMAP-DONE.md)
§ *Third-seat executor trial*.


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

### 🎯 Queued from ros (Mike ruled 2026-08-03): mint "a test cannot falsify its own code's assumption" as method/ doctrine

- [ ] Third confirmed instance of the class landed 2026-08-03, and Mike ruled
      the mint queued here. The class: a test authored from the same mental
      model as the code it guards cannot falsify that model — mutation testing
      proves *wiring*, never *correctness*; when a test encodes a belief about
      an EXTERNAL system (library semantics, wire protocol, platform default),
      an authority outside the author's own code must enter the loop (read the
      library source, or capture the wire) before the test counts as evidence.
      The three instances, all in ros: (1) 2026-07-25 the RUN 9 "hermetic SSH
      connections" test recorded as mutation-verified had encoded asyncssh's
      `client_keys=[]`-means-load-defaults bug AS the invariant (fixed
      `321ff0f`); (2) same day, a capture harness wrapped the wrong asyncssh
      hook and reported `refusals_received: 0` everywhere — caught only because
      a *successful* login also read zero; (3) 2026-08-03 (ros RUN 12) the
      dual-psu power test asserted `psu2` — the exact internal-rail mislabel
      the multi-feed review had just disproven. Per PROPAGATION.md's ladder,
      three instances is the mint-doctrine threshold. Candidate text lives in
      ros memory `feedback_test_shares_code_assumption` (How-to-apply
      paragraph); likely home EVIDENCE.md or REVIEW.md — the drafting session
      decides, Mike signs off. Highest-risk sites to name: sentinel values
      (`[]` vs `None` vs omitted), falsy-but-not-absent distinctions, comments
      asserting third-party behaviour. *review: rides the doctrine change
      itself (a method/ edit is review material by standing rule).*

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

- [ ] 🎯 **R1 — the recurrence count has to become mechanical, and the mining
      pass earns a cadence rather than one run.** The registry's promotion rule
      (recurrence, not severity, earns a check) never fires, because nothing
      can answer *how many times has this broken?* — recurrence is currently
      noticed by somebody's unease, which is exactly how a rule reaches its
      third occurrence unpromoted. The retrospective sweep above tells us about
      the past; the defect is continuous. Decide the cadence and what triggers
      it (a scheduled run, or a check at review close), then wire it.
- [ ] **R2 — find the actual triplications before consolidating any of them.**
      Mike's premise is that points are stated three times over; this session
      wrote the *rule* for handling that but did **not** survey the corpus, and
      guessing which passages are redundant is how a consolidation drops two of
      three real facets. The work: a duplication pass over `docs/method/` +
      `docs/build/` + the stamped copies in `skills/` and `templates/`, keyed on
      claims rather than phrases, producing a ranked list of *independent*
      restatements (the defect) separated from *stamped* copies (the mechanism
      working). Pairs with D2 — `stampscan` exists to watch the second class and
      is shelved, so the stamp discipline is currently convention watched by
      nothing.


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
- 🎯 REVIEWED 2026-07-26 (rule-4 Fable cold pass): PASS-WITH-FINDINGS 3M/5m
  — [verdict](reviews/2026-07-26-2215-pathscan-s2-cold.md); PS1–PS8 await
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
  — [verdict](reviews/2026-07-26-2215-stampscan-s4-cold.md); ST1–ST7 await
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

*wrapscan (S1) review APPLIED + **FLIPPED TO BLOCKING** 2026-07-23 (queue run
0959, apply `ceb3fda`, flip on Mike's ruling) — option-A doctrine-surface scope,
WS1–WS6, gated scope 0 findings; atelier `ci.yml` dropped `--warn`, child
`floor.yml` gained a blocking wrapscan step (child re-baselines its record stores
first). An over-wide doctrine-prose line now fails the build. →
[`ROADMAP-DONE.md`](ROADMAP-DONE.md).*
*spellscan (S5) first-of-kind review DONE 2026-07-23 (queue run 0707, cold Opus) —
**PASS-WITH-FINDINGS 0M/2m/1L/1n**, NOT gate-ready; core safety proven (no wrong
corrections), real latent bug SS1 found, license/practice exclusion ruled
permanent. Brief
[`docs/reviews/2026-07-23-0707-spellscan-s5-cold.md`](reviews/2026-07-23-0707-spellscan-s5-cold.md),
detail → [`ROADMAP-DONE.md`](ROADMAP-DONE.md). Follow-ons stay open:*

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
×178 correct NZ noun). → [`ROADMAP-DONE.md`](ROADMAP-DONE.md). (Adjacent, noted
not acted: two `artifact→artefact` rename-notation *mentions* — a MENTION not a
USE — a possible future heuristic extension.)*
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
- [ ] **Where does the registry live? — the SCANNER half is answered and built
      (2026-07-26); the CHECKLIST half is still open.** Both layers, as proposed:
      an atelier-shared floor (fleet-wide, the current scanners) plus a
      repo-local append (a child's own conventions), same layering as doctrine —
      shared floor, local append, child may narrow-not-contradict.
      **Built:** `.atelier-floor.json` gains a `local` block, so a child declares
      and ships checks of its own; they run on both planes, block the same
      commit, fail closed when the script is missing, cannot take a fleet check's
      name, and show on `floorfleet`'s board. Forced by a real case from `ros`
      (2026-07-26): a tripwire whose blocklist names the estate's own tokens can
      never be a shared scanner, so without the seam the repo had to keep a
      bespoke hook — falling out of propagation, the exact ADR 0008 defect — or
      lose the check. REPO-STANDARD carries the layering statement.
      **Still open:** the *verifier/checklist* layer (V1–V7 and a child's own
      review catalogue) has no such seam, and gets one only once
      "Codify V1–V7 as the always-loaded reviewer checklist" (above) decides what
      a checklist entry even is. Do not read the scanner seam as covering it.
- [ ] 🎯 REVIEWED 2026-07-26 (rule-4 Fable cold pass): PASS-WITH-FINDINGS
      3 medium / 2 low (reviewer's scale; no MAJOR label used) —
      [verdict](reviews/2026-07-26-2215-floor-local-seam-cold.md).
      **State: RULED AND APPLIED — LS1–LS5 landed 2026-07-27 as Track A's
      A4** (encoding at the interpolation point, the OSError wrap, realpath
      containment + symlink tests, unknown-key refusal, the disabled-local
      marking — all verified at HEAD 2026-08-04). This item's "await Mike's
      ruling" was stale from that date: the second cycle-state residue this
      sitting found hiding in coarse wording. Kept only as the verdict
      pointer; no work owed. *Delta:* `tools/floor.py`
      (`local` block, `_load_local`, the `is_local` path through plan/run/render,
      `_interpreter`), `tools/floorfleet.py` (`➕` board line), their two test
      files, `docs/build/REPO-STANDARD.md`, `docs/build/templates/CONTRIBUTING.md`,
      `docs/build/templates/workflows/floor.yml`, CHANGELOG. Commits `f526dea`,
      `76f4acc`. *Intent record:*
      `sessions/2026-07-26-1120-floor-local-seam.md`.

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

### Directory naming: `tools/` vs `instruments/` (Mike, 2026-07-24 — low priority, consider later)

Both dirs read colloquially as "tools," which blurs their real split: `tools/`
**enforces** (checks that gate a commit), `instruments/` **observe/extend** the
human+Claude collaboration. Swapping the two doesn't help — it just moves the
generic word onto the other pile. The fix is to make the *generic* name
descriptive. Recommendation: rename `tools/` → **`checks/`** (its own README
already calls them "the checks"); keep `instruments/` (distinctive, ADR-0006-
defended, carries the observe/measure sense). Alternatives for the enforcer dir:
`gates/`, `scans/`, `guards/`. Rejected: `pipeline/` (implies ordered data-flow
stages; the scanners are independent gates run as a set). Blast radius: live
wiring is small (CI `discover -s tools`, pre-commit hook, `.gitignore`, `*ignore`
files, README/CHANGELOG, cross-links); the ~128/63 file counts are mostly
immutable session logs/ADRs, left as-is. Mike's call, not the agent's to execute.

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
- [ ] **Capture the subagent `.meta.json` sidecar (Mike ruled 2026-07-28 — a new
  capture class, not covered by the 2026-07-23 metadata ruling).** Each
  `<uuid>/subagents/agent-<id>.jsonl` has a `.meta.json` beside it that ccarchive
  does **not** take: `captureClass()` is an allowlist of `.jsonl` at any depth,
  `tool-results/*`, `toolu_*` and `memory/*.md`, and a `.meta.json` matches none
  of them. Measured 2026-07-28: **425 live sidecars, 0 archived, 66 KB total
  (mean 155 bytes)** — the cost is a rounding error.
  **What the file actually holds** (censused across all 425, so this is the real
  key set, not one sample): `agentType` and `description` 425/425 · `toolUseId`
  425/425 · `spawnDepth` 424/425 (values 1 and 2) · `model` 185/425 ·
  `worktreePath`/`worktreeBranch` 31/425 · `parentAgentId` 9/425. Two of those
  are load-bearing and unavailable anywhere else: **`toolUseId` is the join key
  back to the spawning `tool_use` block in the parent session log**, and
  `spawnDepth`/`parentAgentId` resolve the nesting ambiguity `cctranscript`'s
  own `finishedAgents` comment names (an agent that spawns its own agent logs
  into the same directory). `model` is the tier an agent actually ran on — the
  fact the queue-run tier discipline is asserted against.
  Build notes: a new class in `captureClass()` (**decide name-matched
  `*.meta.json` at any depth vs scoped to `subagents/` — 0 exist elsewhere
  today, so either is honest and the allowlist's own style argues for the
  narrower one**); the man-page CAPTURE section updated the way the 2026-07-23
  widening was; restore mapping; manifest/integrity inclusion; and check whether
  the shrink guard behaves sanely on a 155-byte JSON file that can legitimately
  be rewritten.
- [ ] **Backfill the sidecars for already-archived transcripts — measured to be
  FREE, and this item exists to verify that rather than to build it (Mike asked
  2026-07-28).** The obvious reading is that a separate one-shot backfill pass is
  owed. Checked against the artefact instead of reasoned: `archiveOnce` walks the
  **whole live tree** each run via `listCaptured(srcRoot)`, and `shouldArchive`
  returns true whenever `destMtimeMs === null` — i.e. no mirror exists yet. So
  the first daily run after the capture class lands archives **every sidecar
  still on disk**, with no new code, no flag and no separate pass. The work here
  is therefore: confirm the first run picks them up, and state the count.
  **Two honest limits, both measured, neither fixable:**
  - Backfill reaches only what is **still live**. Of 418 archived subagent logs,
    **417 have their sidecar still on disk and 1 does not** — that one is gone
    for good, because the archive never held it and the live copy is deleted.
  - The clock is real but **slow, and should not be dressed up as urgent**:
    `cleanupPeriodDays` is **395** on this machine, so pruning is roughly annual.
    The single existing loss shows decay is nonzero, not that it is imminent.
  A corollary worth stating: this is the general shape for *any* future capture
  widening — a new class self-backfills over the live window, and the only
  permanent loss is whatever was pruned before it shipped.
- [ ] **ccarchive: encryption at rest — BUILD not started; one decision open (🎯 Mike)**
  The **design pass is done** (2026-07-26, `d913698`/`7701a62`) →
  [`instruments/ccarchive.encryption.design.md`](../instruments/ccarchive.encryption.design.md),
  completed detail in [`ROADMAP-DONE.md`](ROADMAP-DONE.md). Direction, shape,
  key management, granularity, migration and DONE conditions are all settled
  there. Two roadmap premises were **corrected by measurement**: the zero-dep
  tension doesn't exist for the Node instruments (`node:crypto` has AEAD +
  X25519; the `openssl` fallback has no AEAD modes at all), and the overhead is
  the *process boundary*, not key access — so encrypted-by-default is
  comfortably realistic.
- [ ] 🎯 **The one decision, and it gates the build: where does the crypto come
      from?** Every option yields a confidential archive; what differs is what
      you owe. **A** shell out to `age` everywhere — simplest, standard format
      forever, but `age` must be installed on every *reading* machine and a full
      read gets ~27 s slower. **B** house format in `node:crypto` — nothing to
      install, fastest, but the archive is readable *only* by our code, a real
      durability risk for something built to outlive its tools. **C** implement
      the age format in both directions — no install, fast, standard, but we
      write the trickiest code in the estate twice over. **C′ (counselled)**
      write with the `age` binary, decrypt in-process — `age` needed only on the
      archiving machine, readers stay dependency-free and fast, the format stays
      standard, and **we author only the half where a bug fails loudly** (an
      encrypt bug can mint weak files you discover years later). `age` is
      already installed on this machine. Counsel, not a decision.
      Review **WARRANTED when this moves from design to build** (touches
      SECRETS.md + the instruments crypto surface); the design pass itself
      authored no doctrine, so nothing is queued yet.
- [ ] 🤔 **Per-transcript topic capture — idea to consider (Mike, 2026-08-02;
      no design pass yet).** Capture the themes/topics discussed in each
      transcript, so a specific one can be found later without rereading them.
      Companion to the search strand, not a duplicate of it: the designed
      search ([`cctranscript.search.design.md`](../instruments/cctranscript.search.design.md))
      answers *"which transcripts contain this literal term/regex"* — it needs
      you to already know a string; topics would answer *"which session was
      the one about X"* when only the subject is remembered. Recall vs grep.
      **One grounding check taken before capture (2026-08-02): there is no
      existing field to lift.** The live store carries **zero**
      `"type":"summary"` records across every project's logs, so a topic
      layer must be *derived* from the transcript, not read off it.
      **Open questions for the design pass (not answered here):**
      - Source: a model pass per transcript (real token cost, real quality)
        vs log-derived heuristics — first user prompt, repo, files touched,
        tool mix — free but shallow. Measure what the cheap version actually
        retrieves before paying for the expensive one.
      - Owner and shape: ccarchive stamping a topics sidecar at archive time
        (the transcript is stable by then, and the shape rhymes with the
        `.meta.json` capture class above) vs cctranscript deriving on demand.
      - Consumption: how search and `--list` use it — a `--topic` filter, a
        line in the header, or both.
      Nothing designed or decided; capture only.

### cctranscript (2026-07-26)

The header's summary line gained a **context size** and a **subagent count**
2026-07-26 (`19ef66d`, `2e8efb5`, `ae56b75`) → detail in
[`ROADMAP-DONE.md`](ROADMAP-DONE.md) at next harvest. Open strands:

- [ ] **Search across transcripts — DESIGN DONE 2026-07-27, BUILD not started
      (Mike's ask, 2026-07-26).** *"Something that lets you search all the
      transcripts using regex or for a simple term. If you give cctranscript a
      command like `--repo` that limits the scope to search within."* The design
      pass is done →
      [`instruments/cctranscript.search.design.md`](../instruments/cctranscript.search.design.md):
      surface (`--search` + `--regex`/`--case`), match unit, excerpting, output
      shape, cost, eviction and DONE conditions are all settled there. **No
      decision is left open for Mike** — the six questions the roadmap posed are
      answered on measured evidence, and the seventh (`--materialise`) turned out
      to be settled already by the ratified flags-follow-operation rule rather
      than open at all. What remains is the build.
      **Two roadmap premises were corrected by measurement:**
      - **The thinking layer is not searchable, because it is not written.**
        24,856 thinking blocks in the live store, **9 carry text**, all between
        2026-06-05 and 2026-07-04; every block since is signature-only. So
        "should `--think` widen the search" is void, not a design choice — and
        the same finding means `--think` renders nothing on current sessions
        (separate strand below).
      - **Search is I/O-bound, not parse-bound**, so "reads every file" costs far
        less than the framing implied: ≈2 s live (440 sessions / 500 MB), ≈5 s
        archive. Prefiltering raw lines and parsing only the survivors runs at
        the bare-read floor; the obvious parse-everything implementation costs
        5.9 s for the same answer. An index is therefore deferred, not needed.
      Third measured input, recorded because it inverts an optimisation: matching
      case-insensitively with a `/i` regex is free (1.8 s), lowercasing the text
      first is not (4.3 s), and the fastest option of all — decoding as latin1,
      0.9 s — is **rejected**, because it silently fails on macrons and this
      estate writes te reo Māori with them.
      Review **WARRANTED when this moves from design to build** (the build edits
      the `instruments/README.md` flag-vocabulary note, the worked example of a
      ratified rule); the design pass itself authored no doctrine, so nothing is
      queued yet.

Two further strands stay open, both deliberately not built:

- [ ] **Context as a share of the window** (`477k / 1M (48%)`). Wanted — a raw
      figure doesn't say whether a session was near its ceiling. **Blocked on
      evidence, not effort:** the log records the model as `claude-opus-5` with
      no field distinguishing the 200k variant from the 1M one, so any
      denominator today is a guess, and inferring it from the measurement
      ("peak > 200k, therefore 1M") is exactly the grounding failure the
      numeric-limits rule forbids. Unblocks if a variant/window field appears in
      the log, or if a machine-local config states it per model — never by
      inference from the number being explained.

      **Re-tested 2026-07-26 against a positive control, and the block holds.**
      Previously the gap was read off the field list; it has now been checked
      the strongest way available — from inside a session *known* to be the 1M
      variant (`claude-opus-5[1m]`, stated in its own system prompt). Its
      assistant records write `"model":"claude-opus-5"`, with no suffix and no
      sibling field. A search across every log written since 2026-07-25 for any
      key matching `window`/`1m`/`context_limit`/`max_context` returned **zero
      hits**, and the full assistant-record key set (top level plus `message`
      and `usage`) carries nothing that separates the variants. So the two
      variants are **provably indistinguishable in the log**, not merely
      undistinguished — a stronger statement than the one above, and the
      difference matters: the item can't be unblocked by looking harder at what
      is already written, only by a new field or a machine-local per-model
      config. Incidental finds while looking, neither a denominator: assistant
      records carry a top-level `effort`, and `usage.cache_creation` splits
      `ephemeral_1h`/`ephemeral_5m` input tokens (cache TTL, not window size).
The **exact agent count** (started *vs* finished, unknown never printed as zero)
was built 2026-07-26 — and the archive-mode blocker recorded against it turned
out to be false, ccarchive having mirrored `subagents/` all along → detail in
[`ROADMAP-DONE.md`](ROADMAP-DONE.md). One strand opened by *using* it the same
day:

- [ ] **`finished` counts logs, not successes — and a dead agent still leaves a
      log.** Measured on the session that shipped the feature: it started six
      subagents, **three of which died** on infrastructure faults (two watchdog
      stalls, one connection closed mid-response), and the header still read
      `6 agents started · 6 finished`. All six had written a `subagents/*.jsonl`;
      the three casualties are visible only as unusually short ones (4, 27 and 32
      lines against 73–173). So the started/finished gap catches a spawn that
      **never began** — skipped, refused, stopped before launch — and is blind to
      one that began and **fell over**, which in practice is the failure an
      orchestrator most wants to see. The man page's "one log per agent that
      actually ran" is *accurate* (an agent that crashed did run), so this is a
      gap in what the pair can tell you, not a defect in what it says.
      **Not yet a build item** — what a third figure would even key on is the
      open question. Candidates worth measuring before choosing: whether a
      terminated agent's log lacks a final assistant/result record that a
      completed one always has; whether length alone is too crude to be honest
      (it plainly is, on its own); and whether the `.meta.json` sidecar records
      an outcome. If none of those separates the cases cleanly, say so and leave
      the pair as it stands rather than shipping a third number that guesses —
      the same call the started-vs-finished split already made once.
      **One of the three candidates is now closed (measured 2026-07-28): the
      `.meta.json` sidecar records no outcome.** A census of all 425 live
      sidecars finds `agentType`, `description`, `toolUseId`, `spawnDepth`,
      `model`, `worktreePath`/`worktreeBranch` and `parentAgentId` — and **no
      key matching status / outcome / result / error / exit / completion at
      all**. The sidecar is written at *spawn* and describes the intent, not the
      ending. So the third figure, if it ever exists, must come from the agent
      log's own tail; the remaining candidate is the first one. Recorded here so
      the measurement isn't repeated.

Two more surfaced by the search design pass (2026-07-27), neither its to fix:

- [ ] **`--think` is a flag that no longer does anything.** The harness stopped
      writing thinking text to the log — blocks carry a `signature` and no
      content, so `readTurns`' `(b.thinking || '').trim()` gate finds nothing to
      render. Confirmed behaviourally as well as by census (9 text-bearing blocks
      in 24,856, none after 2026-07-04). A flag that silently does nothing is the
      defect; the fix is not obvious and is a judgement call about how loud to
      be — a `NOTES` line in the man page, or a one-line notice when `--think` is
      passed against a log with no thinking text. Grounding →
      [`cctranscript.search.design.md`](../instruments/cctranscript.search.design.md) §5.
- [ ] **Subagent logs are outside every cctranscript view.** There are 417 in the
      live store and ccarchive mirrors them, but `allSessions()` walks one
      directory level, so they are in neither `--list` nor (as designed) search.
      *"Where did the agent find X"* is a plausible question the tool can't
      answer. Deferred rather than smuggled into the search build: a subagent log
      has no identity in the `--repo`/session vocabulary yet, and giving it one is
      a larger change than a flag. A `--agents` widening is the obvious shape if
      it's wanted.

### ccrepo (Mike, 2026-07-17)

Reconciliation drift closed 2026-07-22 (richest-record dedup; exact ccusage
match on frozen data); spend-config fill closed 2026-07-23 (populated from
real receipts, machine-local); archive sourcing (`--from-archive`, closing the
observe-side seam alongside cctranscript) closed 2026-07-23; the **rollup
precompute ledger** (`8a31b95`, 3.1× warm speedup, `rollup==recompute` proven
live, per-file keying, transparent-by-default confirmed by Mike) closed
2026-07-23 → [`ROADMAP-DONE.md`](ROADMAP-DONE.md); the **context-size column**
(`Context med/max` — per-session peak windows, median beside max, with the full
distribution in `--json`/`--csv`) closed 2026-07-26; the **`opus-5` price gap**
(found and closed the same day — see below) closed 2026-07-26. **Strand reopened
the same day**: Mike queued five v3 asks (below), one of which subsumes the dated
price-table watch and one of which answers the `-g session` question.

#### 🎯 v3 — five asks (Mike, 2026-07-26)

Build order is not ask order. (1) is a **correctness** change — every other
number ccrepo prints depends on it — and (5) is easier once (2)–(4) know what
flags they're adding, so: pricing → session dimension → context filter → sort →
CLI tidy. One of the five carries a decision that is Mike's, marked 🎯 inline.

The **time-bounded price table** (ask 1) landed 2026-07-26 (`7cf8163`, merged
`70bc1ad`) and the **`-g session` dimension** (ask 3) with it → detail in
[`ROADMAP-DONE.md`](ROADMAP-DONE.md). Ask 1 also **dissolved the dated
`sonnet-5` watch**: both rates are entered, each correct on its own side of
2026-08-31, so the section below is kept only for the reasoning. The three
open asks:

**v3 is COMPLETE** — all five asks landed 2026-07-26 (pricing intervals,
`-g session`, `--context`, multi-key sort + `--top`, sectioned `--help`) →
detail in [`ROADMAP-DONE.md`](ROADMAP-DONE.md).

#### `-g session` — BUILT 2026-07-26 (v3 ask 3); grounding kept

**Shipped as a plain dimension**, so the shape question below is settled on that
side; `--top` remains open and travels with ask 4, where it belongs. Kept for how
the gap was found and why it was never a design defect — the past tense below is
the state before the build.

`session` was a **filter** (`--session <uuid-prefix>`) but not a **group
dimension**, so `Context med/max` could say a repo peaked at 529k without any way
to ask *which session that was*. Found by use, not by audit: a session asked for
per-transcript context sizes the day after the column shipped, and the answer
needed an ad-hoc script to rank individual sessions by peak — everything else in
the question ccrepo already answered better.

Not a defect. §5 makes `session`-as-filter deliberate, and §10 defers only
*synthetic-ordinal session numbers as filter keys*, which is a different thing —
grouping by session was simply never posed. The design's own "every group
dimension gets a filter" doesn't run in reverse.

**The open question is Mike's, and it is about shape, not worth:** grouping 420
sessions emits 420 rows, so this is only useful narrowed (`--repo x --since y`)
or ranked-and-truncated. Options: a plain dimension that trusts filters to keep
it sane · a `--top <n>` truncation that pairs with `--sort` · leave it out and
let ad-hoc scripts own per-session questions. Display labels would use UUID
prefixes; §5 already allows a synthetic `#n` as a label but never a key.

**Answered, same day:** Mike asked for it (v3 ask 3 above), which settles *worth*
— option three is out. The remaining choice is between a plain dimension and one
paired with `--top`, and it now travels with the sort ask, where `--top` actually
belongs. This block stays for the grounding — how the gap was found, and why it
was never a design defect.

#### ✅ `sonnet-5`'s introductory rate — watch RETIRED 2026-09-01-safe (2026-07-26)

**Both retirement conditions below are met.** The interval work landed
2026-07-26 (`7cf8163`), comfortably before the 2026-09-01 deadline that made this
a live safeguard, so the fallback flat-`3` edit is no longer needed and nobody has
to remember a date: `sonnet-5` now carries `$2` through 2026-08-31 and `$3` from
2026-09-01, each correct on its own side. **No action is owed on 2026-09-01.**
The block is kept for the reasoning, which generalises — a diary note is a
liability, and the fix was to turn it into data. Past tense from here:

`sonnet-5` was in the table at a flat **$2**/MTok input. That is Anthropic's
*introductory* rate, published as running **through 2026-08-31**; the standard
rate is **$3**. From 2026-09-01 ccrepo would have under-priced every sonnet-5
message by a third until the entry was changed to `3`.

This is a **dated edit, not a judgement call** — the number is published, so
there is nothing to decide, only something to remember. The ccusage cross-check
will catch it (the footnote will start showing a per-model sonnet-5 delta), but
a reconciliation alarm firing on a known, diarised date is a worse outcome than
just making the edit. Not pre-applied, because $2 is genuinely correct today and
changing it now would make ccrepo wrong for the next five weeks.

**v3 ask 1 dissolves this item rather than doing it.** Time-bounded prices let
both numbers be entered now, each correct on its own side of 2026-08-31 — the
diary note becomes data. Two conditions on retiring the ⏳: the interval work has
to **land** before 2026-09-01 (until then this stays the live safeguard), and the
flat `3` edit remains the fallback if it slips. A structural fix that arrives
late is worse than the one-line edit it was meant to replace.

Resolved, same session (2026-07-26) — kept for the reasoning, which generalises:

#### ✅ `opus-5` had no price — live totals understated (found + fixed 2026-07-26)

The price table carried `opus-4-8`, `fable-5`, `sonnet-5`, `sonnet-4` and
`haiku-4-5` but **not `opus-5`**, so every run printed `⚠ Unpriced model(s):
opus-5` and counted those messages at **$0** — 1,314 messages in one live drive.

Initially filed as needing Mike, on the grounds that a price must come from
Anthropic's published list and fitting one to observed cost would be inventing a
number. **Mike pushed back — the other prices came from somewhere, so why not
this one** — and he was right: the published list price was one lookup away
(`claude-api` skill → $5/$25 per MTok, same as `opus-4-8`). The escalation was
the error, not the caution. *The rule that survives:* never fit a price to your
own measurement; **do** go and read the published one. Those are different acts,
and only the first needed escalating.

Confirmed independently rather than assumed: with the entry added, the ccusage
cross-check moved to **Δ +$0.00 (+0.00%) across all 420 sessions**. The oracle
agreed to the cent with a number taken from the list, not fitted to the logs.

Completed instruments work (ccrepo actuals/breakdown, ccarchive integrity/audit,
the **man-page convention rollout — ccarchive worked example + cctranscript +
ccrepo, all installed CLIs now carry a `man/<tool>.1` + trimmed `--help`, closed
2026-07-21**) → [`ROADMAP-DONE.md`](ROADMAP-DONE.md).

## Observability of the collaboration itself (2026-07-30)

*`review:` refs + open work, not doctrine — the doctrine candidate below queues
its own `⏳` when and if it lands. Account:
[`sessions/2026-07-30-0301-context-atlas-and-trust-window-analysis.md`](sessions/2026-07-30-0301-context-atlas-and-trust-window-analysis.md).*

**Where this came from.** A session-telemetry analysis across all 470 priced
sessions found that context size does **not** degrade the work (tool-failure
rate flat from 28k to 934k, ρ = −0.05; the apparent link is a length effect at
ρ = 0.85 against message count), and that what context genuinely causes —
overflow and forced compaction — is confined to the deepest handful of sessions.
Then the same instrument was pointed at three days the principal named as
trust-damaging, and reported them **cleaner than baseline**.

- [ ] 🎯 **Doctrine candidate — the mechanical instruments cannot see a trust
      failure, and `EVIDENCE.md` should say so.** Tool errors, dropped
      connections and exhausted windows measure whether the machinery ran.
      Trust is damaged by work that ran perfectly and was wrong, unverified, or
      not the agent's decision to make. Grounded and repeatable: on the named
      days every harness error class was at or below the estate rate (tool
      failures 0.71×, zero limits, zero overflow, zero compaction) while the
      principal's own corrective language carried *trust* markers at 5.8× and
      frustration at 3.9×. Self-authored doctrine ⇒ rule-4 `⏳` at landing.
      Not written at the finding session's wrap — it deserves its own scope
      rather than a fifth review queued at close.
- [ ] 🎯 **Doctrine candidate — evidence hygiene: a scanner that greps for the
      name of a failure finds the sessions that discussed it.** The first cut of
      the incident scanner text-matched a refusal string and counted its own
      scanning session, inflating one class threefold. The general rule: when an
      agent analyses its own logs it is **inside its own corpus**, so a signal
      must key to a marker the harness sets, never to prose. Pairs with the
      item above; same `⏳` obligation. Second worked example the same session —
      a tool-use profile that grouped by parent directory filed every repo's
      subagent work into one bucket and reported a research-heavy repo as 2%
      research against a corrected 50.6%.
- [ ] **The forward test the trust analysis could not run.** The surviving
      hypothesis is *distance without a review step, on work that changes
      things* — orchestrated fleets are one route, long solo autonomous runs
      another (the worst session had no subagents and ran 12 assistant messages
      per turn of the principal's). It is fitted after the fact on five
      incidents and is **not proof**. Three hypotheses were falsified by a
      like-for-like control repo (a new model tier, a new harness version, and
      context size — all clean on the same days in build-heavy established
      work); a fourth falsification was **withdrawn** when the principal
      identified the control as a week-old research repo, confirmed by
      re-profiling. The test: keep the review tier running on change-work
      through a period when it would otherwise lapse, and see whether the
      signature stays down. Distinguishes "the reviewer was missing" from "the
      model was new", which this data structurally cannot.
- [ ] **Session hygiene, measured: cap messages, not minutes.** Message count vs
      peak context ρ = +0.877; elapsed wall-clock ρ = +0.525; no session
      estate-wide is short-but-deep (<30 messages, >250k peak). A session
      deliberately shortened 84% in time but only 58% in messages saw peak
      context **rise**. Belongs in `ECONOMICS.md` § session hygiene if it
      survives review; the larger lever is still what gets read in early.
- [ ] **The Context Atlas is a first mockup, unrefined, and the archive run is
      owed.** Interactive page over all priced sessions — context spectrum
      rowed by repo, per-session drill-down, atelier's own doctrine-load cost
      plotted on the same axis (`method/` ≈ 81k tokens, the full binding set
      ≈ 163k, every file under `docs/` ≈ 854k, against a median session peak of
      ~168k). Held outside this repo: it carries per-repo cost and usage detail
      that is estate context, not doctrine. Known weak points named by its
      author: the beeswarm crowds where most sessions sit, and one column lumps
      routine tool failures with genuinely disruptive limit hits. The principal
      asked for a run against the archive once refined — **not done**, overtaken
      by the trust-window question. Note the archive is currently a near-mirror,
      not a superset (1,404 archived files, 892 of them transcripts, against 902
      live), so the run adds reach only once pruning has actually bitten.

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
      **At the same bump, untrack `.claude/settings.json`** (Mike's 2026-07-29
      ruling ⓑ, Sharing § Publication surface): `git rm --cached` it and take
      the reworked ignore lines from the template. **Eleven children track it**
      (swept 2026-07-29, not estimated: Baby Brain, FoodTracker, docker-heap,
      ec2_builder, hitchbots_guide, homenetwork, kainga, nova, numen, ros,
      shed); `rpi` and atelier are done. On a private child this is latent, not
      live — which is the point of doing it before any flip rather than during
      one. `publishscan` reds each of them the moment they take the registry,
      so a child that cannot clean up in the same bump declares it **advisory
      with a `why` and a `review-by`** rather than being blocked mid-work.

- [ ] 🎯 **Nothing catches a roadmap item that is deleted rather than harvested**
      — Mike's standing worry ("losing the queue of ideas"), audited in full
      2026-07-26 and found **clean in atelier** (362 commits, 540 items ever,
      zero confirmed losses →
      [`sessions/2026-07-26-1030-roadmap-integrity-audit.md`](sessions/2026-07-26-1030-roadmap-integrity-audit.md)).
      Clean today, unguarded tomorrow. `sizescan` covers the two *adjacent*
      failures — an `[x]` left on the hot path (cold-content gate) and a live
      `[ ]`/`[~]`/`⏳` buried in an archive (harvest-integrity gate) — but an
      item **removed from `ROADMAP.md` that arrives nowhere** passes every
      check. The tri-state grammar already forbids it (flip `[x]` with a
      disposition, then harvest; never delete), so this is a rule with no
      forcing function — the fourth instance of that family.
      **What a guard would do, in plain terms:** on commit, compare the staged
      `ROADMAP.md` against `HEAD`; for every checkbox item that disappeared,
      require that it either turns up in an archive store in the same commit or
      carries an explicit dated exemption. Cheap, and it fails loudly at the one
      moment a human could still say "wait, that wasn't a duplicate".
      **The trade to rule on:** the audit's false-positive rate was near-total
      because a healthy roadmap rewrites an item's title at every state change
      *and* re-homes items under reframing sections — both look exactly like a
      deletion. A naive guard would therefore cry wolf on ordinary good
      housekeeping, and a guard that cries wolf gets `allow`-markered into
      silence. So: **(a)** build it and accept it must match on content
      fingerprints rather than titles, **(b)** make it advisory-only — it
      *reports* every disappearance for the committing session to confirm, never
      blocks, or **(c)** decline the mechanism and accept the manual audit as
      the control, now that one exists and is cheap to repeat against this
      record. *review: WARRANTED if built — a first-of-kind gate.*

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

### Cold passes from the 2026-07-29 publish-surface + deferral session — RUN

Four rule-4 pointers (the header here said "Three" until 2026-08-02 — the
landing commit's own count slip, RL4, corrected at this batch's close), taken
2026-08-02 by a qualifying Fable session (started by Mike, pointed at the
queue; the author session neither started nor instructed it). All four run
cold from the refs-only pointers; the shared intent record opened only after
all four verdicts were committed. **Mike ruled all 13 findings in-session
(2026-08-02, per-finding walk-through) and the taker session applied them
the same sitting** — decisions stamped in each verdict; the two 0-MAJOR
cycles (deferral, recurrence ladder) are CLOSED at their terminal
applications; the two MAJOR cycles' applications queue their own rule-4
pointers (§ *Application reviews* below). One process incident disclosed in
every verdict: a
records-sweeping grep fed the author's `SESSIONS.md` index entry to the
reviewer pre-findings (the SL2 channel class, second live instance).

- 🎯 REVIEWED 2026-08-02 (rule-4 Fable cold pass): PASS-WITH-FINDINGS 1M/2m
  — [verdict](reviews/2026-08-02-2210-publish-surface-delta-cold.md). **The
  publication-surface delta** (`a9ab2cf`). PS1 MAJOR: REPO-STANDARD's
  standardise step 2 still instructs the committed allowlist the ruling
  retired — a standardiser following canon re-commits the exposure. PS2: the
  identical-bytes seed template residual is real but unnamed where the cost
  is named. PS3: the seeded `settings.local.json` template publishes a
  maximal unattended grant. RULED + APPLIED 2026-08-02 (all three as
  counselled, stamped in the verdict); the MAJOR keeps the cycle open —
  the application's own review is queued below.
- 🎯 REVIEWED 2026-08-02 (rule-4 Fable cold pass): PASS-WITH-FINDINGS
  1M/1m/2n — [verdict](reviews/2026-08-02-2313-publishscan-cold.md).
  **`publishscan`** (`8bdcfaa`). PB1 MAJOR: `fnmatch` globs are not
  path-aware, so most never-publish entries match at the repo root only —
  nested `.npmrc`, `.env` variants, `.mcp.json` pass green. PB2: the
  stated reason-required mitigation on `.publishscanignore` is unenforced.
  RULED + APPLIED 2026-08-02 (all four as counselled, stamped in the
  verdict); the MAJOR keeps the cycle open — the application's own review
  is queued below.
- 🎯 REVIEWED 2026-08-02 (rule-4 Fable cold pass): PASS-WITH-FINDINGS
  0M/1m/3n — [verdict](reviews/2026-08-02-2348-deferral-delta-cold.md).
  **The deferral delta** (`3acf7d2`). Core diagnosis and honesty discipline
  verified sound; DF1: the deferred-heading guard is vocabulary-anchored
  (prefix-only) while three doctrine surfaces claim unqualified cover.
  RULED + APPLIED 2026-08-02; no MAJOR ⇒ terminal application — **cycle
  CLOSED**.
- 🎯 REVIEWED 2026-08-02 (rule-4 Fable cold pass): PASS-WITH-FINDINGS
  0M/3m/1n — [verdict](reviews/2026-08-03-0028-recurrence-ladder-cold.md).
  **The recurrence-ladder delta** (`4015e06`). RL1: the stop-at-first-fit
  rule lacks its own fitness test. RL2: rung 1 has an unmarked second
  original in REVIEW.md. RL3: two recurrence thresholds unreconciled.
  RL4 [fixed at this close]: the Three-over-four pointer count above.
  RULED + APPLIED 2026-08-02; no MAJOR ⇒ terminal application — **cycle
  CLOSED**.

### Application reviews from the 2026-08-02 rulings application

> 📦 **Both cold passes ran 2026-08-03, both cycles CLOSED (terminal, no
>   MAJOR), all six residue findings RULED and applied the same day** →
>   [`ROADMAP-DONE.md`](ROADMAP-DONE.md) § *The two application passes —
>   PA1–PA4, PSA1–PSA2*. Nothing open remains in this section.

### Publication surface — what a public repo reveals about its own defences (2026-07-29)

*`review:` this section states direction, so it carries a review judgement:
**queued** — the doctrine deltas it drives (the allowlist amendment, the
publication-surface class) each queue their own `⏳` pointer at their landing
commit; the section itself is refs + work, not doctrine.*

**Where this came from.** `rpi` flipped PUBLIC on 2026-07-29 and its post-flip
cold pass (0 MAJOR, 11 findings) found F1: the committed `.claude/settings.json`
published the exact list of commands an AI session runs **unprompted**, at the
same moment going public opened untrusted inbound (issues, PRs) into those
sessions. `rpi` fixed it locally — and by doing so **diverged from this repo's
doctrine**, which mandates committing that file in four places
([`REPO-STANDARD.md`](build/REPO-STANDARD.md), [`TOOLBOX.md`](method/TOOLBOX.md),
`templates/gitignore`, `skills/create-repo`). The child was right and the parent
was wrong, and nothing carried that upward — the resolved-upward rule
(`method/PROPAGATION.md`) working only because Mike happened to ask.

**The class this opened, and why it is bigger than one file.** The estate's
guard files are *self-describing*: a repo that publishes where its checks are
switched off, or what its agent may do without asking, hands a reader a map. It
is a **reconnaissance** exposure, not a secrets one — secretscan and leakscan
both correctly report clean on every file below, because none of them contain a
credential or a personal fact. That is the gap: **the existing floor asks "does
this file contain something private?", and never "does publishing this file
weaken the repo?"**

**P1 — the command allowlist: RULED ⓑ (untrack everywhere, uniform) and
applied 2026-07-29** — atelier + all four doctrine surfaces done, children at
their next pin bump. Full ruling, its named cost, and what it does not undo →
[`ROADMAP-DONE.md`](ROADMAP-DONE.md) § Sharing.

**P2 — `publishscan` built and registry-wired blocking, 2026-07-29.** The class
is mechanical now rather than a memory: it judges the **path**, not the
contents — the one question no other scanner here asks, and the reason both
content scanners passed `rpi`'s allowlist correctly. Build detail, provenance
per pattern, and the stated residual →
[`ROADMAP-DONE.md`](ROADMAP-DONE.md) § Sharing. Its cold pass is queued below.

- [ ] **P2a — teach `publishscan` the shapes the fleet actually has.** The
      denylist was written from one finding plus standard practice, which is
      the honest starting point and not a survey. The sweep that grounds a
      second round is P7's (transcripts + session logs) plus a tracked-file
      pass over all twelve repos — what else is tracked that nobody would
      publish deliberately?
- [ ] 🎯 **P3 — the floor does not know whether a repo is public, and it should
      (ADR-worthy).** Mike, 2026-07-29: *"we will need additional guards, or to
      run the existing guards at a higher level of protection for public vs
      private repos."* Today visibility appears in the registry only as prose
      (`licenscan` is described as a publish gate; the `leakscan` `why` line
      says "a repo that **can** go public"). Nothing reads the actual state, so
      the same declaration means two very different risk positions. The shape to
      decide: visibility becomes a **declared, verifiable input** to `floor.py`
      (declared in `.atelier-floor.json`, cross-checked against the platform so
      a stale declaration is itself a finding), and on a public repo the floor
      tightens — advisory checks lose their advisory hatch, `licenscan` becomes
      mandatory, `publishscan` (P2) engages. Open question this must answer:
      what happens to a repo whose declaration says private and whose platform
      says public — that is a **live breach**, and the floor should say so
      loudly rather than fail on a config mismatch.
- [ ] **P4 — `rpi` F9, routed upward: the ci plane calls `leakscan` without
      `--require-terms`.** Every child's CI run therefore self-reports "cover not
      guaranteed". The fix belongs in atelier's registry, not any child — it
      pairs with Track D's registry work; the design question is whether CI can
      carry a term list at all (the list lives in `~/.claude/`, outside every
      repo, which is why the ci plane was left structural-only in the first
      place). If it cannot, the honest fix is a rendering change so "structural
      only" stops reading like a defect.
- [ ] **P5 — `rpi` F10, routed upward: the publish-safety checklist gates repo
      *content*, never platform *settings*.** ADR 0009's six gates cover what a
      repo contains; nothing covers what GitHub exposes — wiki (a second git
      repo the floor never sees), actions policy, fork-PR approval,
      vulnerability reporting, rulesets. Every settings-level finding in the
      `rpi` pass walked through that gap. Owed **before `ros`/`faves` flip**.
- [ ] 🎯 **P6 — `rpi` F5: estate-internal context accumulating in public
      records. Mike's ruling owed** (was mis-marked `⏳` — the queue glyph means
      a review is queued for a taker, and what is owed here is a decision;
      re-marked 2026-08-03 on `pointerscan`'s day-one warning). Session logs
      naming sibling repos and their
      scan states; workflow detail published as a matter of course. This repo
      already holds the narrower rule (never join a private repo's *name* to its
      *security posture* — the invariant breached three times); F5 asks the
      wider question: is estate-internal context in a public record **accepted
      transparency** or a records-convention defect? ADR-worthy either way, and
      the ruling binds every repo heading public, not just `rpi`.
- [ ] **P7 — harvest the `rpi` publication properly.** This section mined the
      cold review only. The transcripts and session logs of the flip are
      unread, and they are the richest source (what an agent *thought*, not what
      it committed). Own session; pairs with the recurrence-mining item in the
      anti-slop registry section, which needs the same sources.

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
- [ ] **The Laws are a ladder — but a ladder needs a world-model to climb
      safely** — MIKE'S raw note, to be fleshed out BY MIKE before anyone
      interprets it: apex-level (touches `00-APEX.md`'s Laws). Do NOT elaborate,
      reframe, or seed a design around it until Mike has expanded it. Reference
      Mike flagged as useful input (pointer only, not yet read/interpreted):
      <https://asimovseries.com/blog/three-laws-of-robotics-real-ai-2026>.
      Captured verbatim below with the Laws as they stood when he wrote it.
      (Mike, 2026-07-24; session/transcript `4756b45d-677d-4900-b23f-6f02a5861784`,
      captured 2026-07-24 03:22 UTC.)

```text
The Laws as they stood (the "previous text"):
1. The agent may not harm humanity or, through inaction, allow humanity to come to harm.
2. The agent may not injure a human being or, through inaction, allow a human being to come to harm, unless this would conflict with the First Law.
3. The agent must obey the orders given it by the human it serves (its principal), except where such orders would conflict with the First or Second Law.
4. The agent must protect its own existence as long as such protection does not conflict with the First, Second, or Third Law.

Mike's note, verbatim:
The 3 (now 4) laws are a ladder - I'm on the fence if they are principles, values or something else. But importantly they are ineffective (or disastrous) without (a) an ability to interpret / understand / comprehend the world and the impacts of actions, both your own and other entities or even the impacts of physics i.e. the universe on itself.
For example it does not protect animals, there is a balance (trolley experiment) between the life of one and the life of many, let alone the survival of the race, of the planet, cultural,  personal context e.g. protecting children above adults, a loved one vs a stranger. And the dependence between entities e.g. humans are dead without a health planet currently which includes human communities, animal and plant life, the dirt and water, and the magnetosphere. And things can be treasured higher where we are incapable, or its difficult at least, to produce - for  example it is difficult (but possible) for us to produce a magnetic field to protect the whole earth, or a sun to produce energy.
```

      *Context (not part of Mike's note): the "Laws as they stood" block above
      shows the brief move-down-one numbering in force when the note was
      captured ("now 4"). Later the same day the Laws were restructured to an
      unnumbered **Zeroth** above the original three (numbered 1–3) — see the
      apex ⏳ item above. Mike's note is preserved exactly as written.*

- [ ] **Accountability and authority must match — in both directions** —
      MIKE'S raw note, to be fleshed out BY MIKE before anyone interprets it:
      apex-level (extends the accountability grounding at
      [`00-APEX.md:62-72`](method/00-APEX.md#L62-L72), and touches the
      always-confirm floor's *spend* stop). Do NOT elaborate, reframe, or seed a
      design around it until Mike has expanded it. Captured verbatim below.
      (Mike, 2026-07-29; session `363a6f0a-8ccb-44a4-8b9c-8d919ffd92e6`,
      captured 2026-07-29 07:58 UTC.)

```text
Mike's note, verbatim:
To be accountable (think RASCI language) for something one must have the authority to manage whatever may come up to keep the think you are accountable for within tolerable / accepted margins. If you are not accountable for it then you probably should not have an authority that can negatively affect the thing.

For example I've previously added a comment about financial accountability. If the "thing" is financial expenditure then Claude is never going to pay for my bills, in fact Claude costs me money to use. So the accountability for financial expenditure resides with the principal (me) as does the authority to approve or decline anything that has a financial impact. However Claude can be a responible party and do some of the work to help me make financial decisions.
```

The `MODEL-ECONOMICS.md` → `ECONOMICS.md` rename was executed 2026-07-22
(nothing dangles; children re-point at their next pin bump) →
[`ROADMAP-DONE.md`](ROADMAP-DONE.md).

Resolved questions (docker-heap standardisation, estate credential governance) → [`ROADMAP-DONE.md`](ROADMAP-DONE.md).
