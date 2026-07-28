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

- [ ] 🎯 **TA-application-pass residue — TAA1–TAA3, Mike's ruling.** The
      terminal cold pass returned 0 MAJOR / 1 minor / 3 notes
      ([verdict](reviews/2026-07-28-1136-ta-application-cold.md)); the cycle
      is closed, and per rule 3 the residue is Mike's to decide. In plain
      language: **TAA1** (minor) — a comment in `floor.py`'s scope guard
      still labels two fail-opens "(open)" that the same series shut; a
      two-line comment edit makes it true (reviewer counsel: fix). **TAA2**
      (note) — the two 🟡 notes share one report field via `elif`, so a
      future softenable scanner with a cover flag would silently drop its
      scope-drift note; a comment naming the invariant, or a joined note,
      pins it. **TAA3** (note) — AW6 doesn't say whether a second queued
      pointer over the same files discharges the delta-list widening duty;
      second recorded case, a third earns the one-line grammar
      clarification.

### Track B — make the enumerator real

*`floorfleet` is what turns "I hope the policy propagated" into "I know it did",
and nothing runs it.* Three of the four items below already have costed entries
further down this file; they are pointed at, not restated.

- **B1 — schedule the conformance check.** Four costed options, one explicitly
  rejected → § *🎯 Schedule the conformance check* below. **UNBLOCKED
  2026-07-28**: the fact was never unknown so much as never written down. The
  operator confirmed it, and it is now recorded in the estate root's own records
  where it belongs. It stays unnamed here, and that is not an oversight —
  `PROPAGATION.md` binds *any* public tree including atelier's own, so writing
  the answer into this file to close a blocker would be committing the breach
  the blocker exists to avoid. A public tree references it by local-path
  convention. B1 can now proceed.
- **B2 — `--status` mode** (wired *and* passing, not just wired) and
  **B3 — the Actions-disabled blind spot** → § *For your consideration* and
  § *the ranked residual* item 4 below.
- [ ] **B4 — the roadmap-deletion guard.** `sizescan` catches the two adjacent
      failures — an un-harvested completed item, and a live checkbox buried in
      the archive. An item **removed from `ROADMAP.md` that arrives nowhere
      passes every check.** The tri-state grammar forbids it with no forcing
      function; this is the fourth member of that family. It must fingerprint
      *content*, not titles: the 2026-07-26 audit walked 362 commits and found
      title-matching has a near-total false-positive rate, because a healthy
      roadmap rewrites titles and re-homes items and both look identical to
      deletion. Advisory-only is the lean — it fails loudly at the one moment
      the committing session could still say *"wait, that was not a
      duplicate"*, without the cry-wolf trap that gets a guard `allow`-markered
      into silence.

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
- [ ] 🎯 **C1-pass residue — C1F1–C1F3, Mike's ruling.** The terminal pass
      returned 0 MAJOR / 1 minor / 2 notes
      ([verdict](reviews/2026-07-28-1204-c1-advisory-cold.md)); cycle
      closed, residue Mike's per rule 3. In plain language: **C1F1**
      (minor) — on the floor's human line, an advisory's `why` displaces
      the "N of M scope paths missing" drift note (it survives only in
      `--json`), so a softened check with shrinking cover shows the reason
      but not the shrink; joining the notes fixes it (reviewer counsel:
      fix). **C1F2** (note) — the record says an expired advisory shows
      how many days it has stood "on the floor and the board", but the
      count renders on the board only; add the count to the floor line or
      correct the claim — either answer works, one of them should land.
      **C1F3** (note) — config-authored strings (`why`, disabled reasons)
      print raw to terminals; a hostile child config could embed escape
      sequences. Pre-existing class, two fields wider now; stripping C0
      controls at parse closes the class if ever wanted.
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
- [ ] 🎯 **Estate-root widening pass residue — ER1–ER4, Mike's ruling.**
      The rule-4 pass ran 2026-07-28: **0 MAJOR / 1 minor / 3 notes, cycle
      CLOSED** ([verdict](reviews/2026-07-28-1216-estate-root-widening-cold.md));
      every count re-swept independently (63/19 exact; zero new mentions
      since landing). In plain language: **ER1** (minor) — the widened rule
      is silent at the private→public *flip*: a private child's onramp
      names the root by design, and nothing says the making-public
      confirmation includes scrubbing that name first — yet pre-flip is the
      one moment a scrub buys everything back (reviewer counsel: one line
      in the always-stop floor's making-public entry). **ER2** (note) —
      "reference it by local-path convention" points at a convention no
      text says where to find; one sentence closes it. **ER3** (note) — the
      "10 lines beside what it holds" figure is net-dependent (8–9 on
      re-sweep); restate as approximate or pin the net. **ER4** (note) —
      the intent-record pointer links a file that does not contain the
      record (the record is the SESSIONS.md entry); addendum pointers
      should say so.
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
  — three instances now, from two directions → § *Doctrine candidate — the
  harvest rides the `[x]` commit* below.
- **Bulk deletion from a record store is a show-first action** — Mike's call,
  it narrows agent autonomy → § *For your consideration* below.
- [ ] **The `⏳` pointer steered its own reviewer.** Two queued pointers
      carried their authors' full reviewer agendas inline, against the
      ROADMAP's own refs-only ceiling; the taker read them before a brief
      existed to defer them, and it measurably steered the pass — two of three
      seeded questions pointed away from the load-bearing problem. The ceiling
      is stated in this file's own preamble and was not enforced by anything.
- [ ] **ZL1 (MAJOR) — the surface that binds the apex at session start is
      stale.** `skills/session-onramp/SKILL.md` still teaches the pre-Zeroth
      three-element Laws, contradicting `00-APEX.md` at HEAD. A prior sweep
      proves the surface was known. The wider finding (AW2) is that at least
      seven in-repo apex restatements describe the superseded shape, while the
      queued propagation item covers children's floors only — so the rest is
      silently stale, against the sweep-in-the-same-commit rule the delta
      itself cites. Verdict:
      [apex Zeroth Law cold pass](reviews/2026-07-26-2215-apex-zeroth-law-cold.md).

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
      EP1–EP10 await Mike's ruling (REVIEW rule 3; MAJORs keep the cycle open
      past the application). **ADR 0008 review owed** — self-authored, so this session may not review
      it (REVIEW.md rule 4). Aim a reviewer at the one real trade: moving every
      repo onto a floating `@main` caller swaps a slow silent failure for a fast
      loud estate-wide one. Is that right for a security floor?
      **⚠️ An Opus pass ran on 2026-07-26 0647 UTC and was NOT ACCEPTED** — reviews
      run on the wrong tier (Mike, 2026-07-26): cold review passes are Fable's.
      The item is re-queued unchanged and still awaits its first accepted review.
      The withdrawn pass is preserved as history under `docs/reviews/withdrawn/`
      and is **not reading for the redo** — open it only after your own verdict
      is written and committed.
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

- [ ] 🎯 **secretscan pass residue — SF1–SF4, Mike's ruling.** The rule-4
      pass ran 2026-07-28 (Fable): **0 MAJOR / 1 minor / 3 notes, cycle
      CLOSED** ([verdict](reviews/2026-07-28-1220-secretscan-fragment-cold.md)).
      All four red legs reproduced old-vs-new; the FP fixes hold; the
      estate figures verified (the 26→4 delta is the ruled untrack). In
      plain language, one family decision and two smaller calls:
      **SF1+SF2** (minor+note, rule together) — the low-charset-diversity
      family: the new kebab exemption un-flags hyphenated passphrases
      (`password=<diceware-style>` was caught before, is clean now; the
      snake twin was already exempt), and the pre-existing lowercase-hex
      gap is half its stated size (digit-leading hex already flags;
      letter-leading slips). Reviewer counsel: whole-shape carve-outs in
      assigned context — full-match 32+ hex, and 4+ hyphenated lowercase
      words — are not identifier/slug-suppressed; cry-wolf risk is git
      SHAs, which rarely sit assigned to credential-named keys. Also
      carried: the triage record's "entropy net catches ≥32 chars" aside
      is true only for mixed-class values — probed false for this family.
      **SF3** (note) — the corpus re-scan question answered: sound
      regression floor, insufficient acceptance test; counsel is a
      standing canary suite of credential *shapes* that must always flag,
      run beside the corpus re-scan on gate changes (it would have caught
      SF1). **SF4** (note) — resolved at reconcile, no action.
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
      exemption behind. Open question for triage: whether the `ipv6` rule should
      require more than two colon-separated groups, or whether describe-don't-
      quote is simply the standing answer for record prose (it already is for
      example credentials).

### Doctrine candidate — the harvest rides the `[x]` commit (found 2026-07-26)

- [ ] **State, at the point of use, that marking `[x]` and harvesting to
      ROADMAP-DONE are one commit — not two.** The ROADMAP preamble defines the
      `[x]` state but says nothing about *when* the harvest happens, and the
      cold-content gate fires the moment an `[x]` lands on the hot path. So
      marking three items done in one commit and harvesting in the next leaves a
      window in which the **pushed** floor is red — which is exactly what
      happened on 2026-07-26 (`d847866` red, `0485540` green). Local scans were
      green throughout, because the harvest was already done on disk before the
      first push was checked; only the pushed floor saw the window.
      **This is the same shape as a ruling already made**, which is what makes it
      a candidate rather than a one-off: AWA2 put the `⏳` pointer *in the commit
      that lands the work* so no window exists where landed doctrine sits
      unpointed. Same argument, different marker — an `[x]` and its harvest
      belong in one commit so no window exists where a completed item sits
      stranded on the hot path. Both are instances of a more general rule worth
      naming if a third case appears: **a state change and the bookkeeping the
      floor demands of it ship together.**
      Not enacted here on purpose: this is doctrine, and REVIEW rule 4 binds the
      author out of reviewing it, so a future session should write it into the
      preamble and queue its `⏳` in the landing commit (per AWA2 itself).

      **A third instance arrived the same day, from the opposite direction — and
      it names the mechanism.** A post-outage recovery sweep found one item still
      `[~]` **claimed** whose work had shipped hours earlier (`b89a306`). Of the
      three states that is the worst to leave behind: a later session reads `[~]`
      as *a live session owns this* and skips it, so delivered work sits looking
      permanently in progress. The reason it was missed is structural, not
      carelessness — **every other item that run was claimed with a worktree, and
      merging the worktree forced a return to the roadmap. This one was claimed
      `wt: none — inline on main`, so nothing ever forced the return.** The
      forcing function was the worktree, and the item that skipped the worktree
      skipped the closing step with it. So the rule wants a second clause aimed
      at exactly that case: **an inline claim is closed in the commit that lands
      its work**, because there is no merge step later to remember it. Same
      family as the `[x]`/harvest pairing above — a state change and its
      bookkeeping ship together — and the same reason it keeps recurring: the
      bookkeeping is only reliable when something *makes* you do it.

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

**4. A blind spot worth closing cheaply.** `floorfleet` reads the workflow
*file*, so a repo with GitHub **Actions disabled** reads as perfectly wired while
running nothing. One `gh api repos/{owner}/{repo}/actions/permissions` call per
child would catch it. Small, and it removes a way for the board to be confidently
wrong — which is worse than the board being unavailable.

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

- [ ] **A — PAT in atelier's CI.** True continuous enforcement, catches drift
      within a day, no human in the loop. Cost: a read token spanning the whole
      private estate, living in the **public** repo's secret store. GitHub does
      withhold secrets from fork PRs, so it is not trivially stealable, but it is
      the largest concentration of the four. Needs rotation discipline.
- [ ] **B — scheduled workflow in a PRIVATE repo.** Identical automation and
      identical benefit to A, with the token in a private secret store instead of
      the public one. Runs on GitHub's schedule regardless of whether any machine
      is on. Open question: which repo hosts it — the doctrine references a
      "private estate-root repo" as atelier's counterpart, but which repo that
      actually is has never been written down. **Answer that first; it is
      reusable well beyond this item.**
- [ ] **C — scheduled local run (cron/launchd).** `floorfleet --remote --check`,
      shouting on failure. **No new credential** — uses the existing `gh` login.
      Failure mode: a machine that is off does not check, so drift can sit for
      as long as the laptop does.
- [ ] **D — add it to the session-close ritual.** Cheapest, zero infrastructure,
      and *rejected on this session's own evidence*: it is a discipline, not a
      mechanism, and the entire finding behind ADR 0008 is that a discipline
      logged as an intention decays silently. Recorded so the option is visibly
      considered and dismissed, not quietly skipped.

**Recommendation: B, or C if the preference is to mint nothing.** B is strictly
better than A for the same outcome. D is not a real option and is listed only to
close it off.

**Whichever is chosen, the work is small:** the schedule, `--check` wiring, and a
failure message naming which child dropped the floor and what to do about it. The
credential, if any, is Mike's to create; the agent wires around an existing
secret and never mints one.

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

- [ ] **`floorfleet` proves a repo CALLS the floor, never that its floor is
      GREEN.** That limit is stated honestly in the tool, and it means the board
      can read "all 13 ✓" while several repos are failing every run. Idea: a
      `--status` mode reading each child's latest floor run conclusion via
      `gh run list`, giving one board that answers *wired **and** passing*.
      Cheap (one API call per child) and it closes the gap between conformance
      and compliance, which are currently two separate questions with only one
      instrument.

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

## Doctrine — review-owed

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
  been consulted. **⏳ review queued for a non-author** (self-authored doctrine,
  REVIEW rule 4). *Delta:* the `EVIDENCE.md` §13 paragraph (landed this commit).
  *Intent record:* [`2026-07-26-0100-ccrepo-context-column.md`](sessions/2026-07-26-0100-ccrepo-context-column.md)
  § Addendum. Rides the normal review cycle when a qualifying session takes it.
- 🎯 REVIEWED 2026-07-26 (rule-4 Fable cold pass): PASS-WITH-FINDINGS 1M/4m
  — [verdict](reviews/2026-07-26-2215-record-pushed-floor-cold.md); RF1–RF5
  await Mike's ruling (rule 3; the MAJOR keeps the cycle open past the
  application). **Capture → doctrine: the close all-clear carries the pushed floor run's
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
  section previously asserted the reservation without naming its source. **⏳
  review queued for a non-author** (self-authored apex doctrine, REVIEW rule 4).
  *Delta:* the accountability-grounding paragraph (landed this commit). *Intent
  record:* Mike's reading that the principal's authority is born of the
  principal's accountability. Rides the normal review cycle when a qualifying
  session takes it.
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
  concern is **void**. **⏳ review queued for a non-author** (self-authored apex
  doctrine, REVIEW rule 4). *Delta:* Zeroth law + prose in `00-APEX.md`;
  `README.md` + `method/README.md` restored to "Three Laws, with Asimov's Zeroth
  Law read above them". The `PROPAGATION.md` + `build/templates/CLAUDE.md`
  floor-ordering summary keeps "avoid harm to humanity → avoid harm to a person →
  obey → self-preserve" (accurate under the Zeroth; generic "the Laws" wording,
  no count claim). **Child floor propagation** rides the existing gated
  "Propagate the widened apex floor to the fleet children" item below. Rides the
  normal review cycle when a qualifying session takes it.
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
  withdraw). **⏳ review queued for a non-author** (self-authored doctrine, REVIEW
  rule 4). *Delta:* one bullet in `PRINCIPLES.md` §1. Rides the normal review
  cycle when a qualifying session takes it.
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
  - **Run 4 outcome — 2026-07-23 (0959 Opus-orchestrated queue run) — NOT a
    clean sweep, and the exception is the useful data.** Four Sonnet items: the
    two review-applies (wrapscan, spellscan — prescriptively-reviewed-fix) and
    the **pathscan (S2)** build (fresh build of a *known* pattern — reused
    linkscan-shaped path resolution) all **PASSED no-rework**. The fourth,
    **stampscan (S4)**, did **not**: a genuinely-new mechanism (marker parsing)
    whose failure mode — parsing its own documentation as real markers and
    exit-2-blocking the floor — its fixtures couldn't anticipate. The defect
    surfaced **at head** and needed an orchestrator correction (unwire). This
    *confirms* the tier split's safety logic (catchable failure caught by
    floor + Opus review, precisely where the split says to pay for capability)
    and **sharpens the promotion line**: the discriminator is **floor density,
    not nominal class** — a fresh build of a *known* pattern is Sonnet-safe, a
    fresh build of a *novel mechanism* keeps Opus-verify-at-merge earning its
    keep (its floor is necessarily thin — fixtures can't cover an unknown
    failure mode). So the standing-executor doctrine line (still owed, future
    session) should read "well-floored builds of *known* patterns +
    prescriptively-reviewed fixes", and must **not** generalise to "any
    first-of-kind build". Four runs of data now; the promotion edit stays a
    future session's rule-4 doctrine act.

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
      [verdict](reviews/2026-07-26-2215-floor-local-seam-cold.md); LS1–LS5
      await Mike's ruling (rule 3).
      **The repo-local floor seam — review owed** (self-authored, so this
      session may not review it — REVIEW.md rule 4). *Delta:* `tools/floor.py`
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

The `MODEL-ECONOMICS.md` → `ECONOMICS.md` rename was executed 2026-07-22
(nothing dangles; children re-point at their next pin bump) →
[`ROADMAP-DONE.md`](ROADMAP-DONE.md).

Resolved questions (docker-heap standardisation, estate credential governance) → [`ROADMAP-DONE.md`](ROADMAP-DONE.md).
