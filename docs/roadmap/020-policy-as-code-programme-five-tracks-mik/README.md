# Policy-as-code programme — five tracks (Mike approved 2026-07-27)

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
>   → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) (A5a fixed 2026-07-27; A1–A4 + A5b
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
  [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md).

### Track C — kill the advisory decay

*An advisory still standing in a month is the "honour it manually" failure
wearing a new hat — the precise decay ADR 0008 exists to end.* Re-measured
2026-07-28: **17 advisory declarations across 10 children**, none carrying a
reason, none carrying a date. (The 2026-07-27 figure of 11 across 8 was an
undercount — the fourth wrong blast radius on this programme and the first that
*understated* the work; see the C1 session record.)

> 📦 **C1 phase 1 complete, and its review cycle CLOSED** (schema, expiry,
>   A1(b); rule-4 cold pass 2026-07-28, 0 MAJOR — terminal) →
>   [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md). What remains of C1 is C1b below —
>   the migration and the removal of the transition spelling.
- **C1F3 residue — CLOSED 2026-08-06** (wt: floor-render-batch-0806):
      `floorfleet` now strips child-authored `why`/reason strings through
      the same public `floor.strip_controls` the two ruled seams use —
      proved against the fork as control (five ESC, a BEL and a NUL from
      one child's declarations were reaching the terminal; now zero, with
      ordinary text byte-identical) — plus a latent board-wide crash on an
      array-shaped child config fixed en route. Detail →
      [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) § *The floor-render batch*.
- 🎯 **A warn-only registry scanner rendered `✅ enforced` — RULED
      2026-08-04 and BUILT 2026-08-06** (wt: floor-render-batch-0806): the
      board now has three legible states — `✅ enforced`, `advisory` (a
      child's softening), and `👁️ warn-only` (the parent's own warn-first
      wiring, "reports findings, can never block this build") — on every
      plane and in `--json`/`--list`, derived from the registry argv
      itself, never a hand-maintained list, pinned both directions by
      selftest + suite. Exit codes unchanged: a warn-only check's
      environment error still blocks. E6b's 🟡 advisory-count note shares
      no wording. Detail → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md)
      § *The floor-render batch*.

### Track D — finish the registry

*Two scanners exist outside the registry, which is the ADR 0008 defect one
level up: a check wired into atelier's own workflow reaches no child, and the
child template's promise that "a new check arrives on the next push" holds for
registry checks only.*

- 🎯 **D1 — `pathscan`: promoted 2026-08-06 (PS5 delivered, wt:
      floor-render-batch-0806).** The registry line replaced atelier's
      bespoke `ci.yml` step — equivalence proved (same 1 finding, same 10
      suppressions), scope moved to `.atelier-floor.json`, children get
      the check warn-only at their next push, and the board renders it
      `👁️ warn-only` honestly. The blocking flip stays a separate later
      ruling; its one open finding was fixed at this landing (a
      distillation in `decisions/README.md` had dropped a path's
      template prefix). Original ruling kept below for the record.
      **RULED 2026-08-04 (Mike): FUND THE RESCOPE**, chosen over the
      counselled retire-to-hand-run; the verdict is the
      [pathscan S2 cold pass](../../reviews/2026-07-26-2215-pathscan-s2-cold.md).
      **THE RESCOPE LANDED 2026-08-05** (wt: queue-batch-0806): the fourth
      anchor and root-file scope (PS1), the doctrine-surface gate story
      with records named out (PS4), the directory-index retry (deferred
      Q2), the date-placeholder exemption (PS3), the docstring corrections
      (PS8 + PS2/PS6/PS7), and the gate-scope residual burnt to zero (the
      one true positive fixed; the false positives marked with written
      reasons — 10 findings as the tally counts them, on 8 marker lines
      across 6 files; the findings figure is the denominator the scan
      itself reports, PD2 ruling 2026-08-06). Tests 53 → 73; the advisory `ci.yml` step now scans the
      gateable surface. Detail → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md)
      § *The 2026-08-06 queue take* (the pointer's delta, harvested at
      the review) and the CHANGELOG entry. **PS5 delivered 2026-08-06**
      (above); the blocking flip stays a separate later ruling.
> 📦 **D2 residue (b) — stampscan joins the GUARDS allowance model —
>   DELIVERED 2026-08-06** with the SD3 ruling (the tally was the only work
>   owed; the loader half was already landed — a parallel session's close
>   (`21f4b36`) independently corrected the same stale claim minutes before
>   this merge, from the tree not the entry) →
>   [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) § *The 2026-08-06 queue take*.

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


- 🎯 **E7 — RULED 2026-08-04 and the funded build DELIVERED 2026-08-06**
      (wt: e7-leakscan-build-0806): D2–D6 fixed as ruled (D1 had landed
      2026-08-05) and G1/G2/G4/G6/G7 built — the key-context layer with
      placeholder suppression and its own canary suite, path scanning on
      both planes, Luhn-checked cards + mod-97 IBAN + the NZ hyphenated
      bank shape, opt-in derived name forms, the bracketed phone form —
      with must-flag/must-pass tests (leakscan suite 53 → 114; tree
      structural run exit 0). E4 and the clock-times boundary entry close
      with the same fix. G5 stays deferred (revisit on first real miss).
      Rulings verbatim + build detail and stated limits →
      [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) § *E7 built*; sweep record:
      [sweep record](../../sessions/2026-08-03-2050-leakscan-pii-sweep.md).
      Rule-4 ⏳ queued (§ *Doctrine — review-owed*).
- **D1's consequence — RULED 2026-08-09 (Mike: scoped markers) and
      APPLIED the same day.** A marker whose scope NAMES `local-term`
      explicitly — with a reason — now exempts term hits on that line;
      the unscoped marker still never reaches the term list, so D1's
      accidental route stays closed and the hatch is deliberate,
      reasoned and counted (`local-term×N` in the tally). Scopes compose
      with commas for lines needing a structural rule exempted too. The
      three published-identity lines carry the scoped form; the full
      local-cover scan is GREEN again (suite 1202 → 1207; the reviewers'
      re-run obligation stops opening on a red).
      **How this lands on C5 (cross-checked 2026-08-09, after both
      changes):** the two items were one gap — the term list could not say
      *where* a term applies — and this ruling closes the **Line** half of
      it. C5 keeps only the **volume** half: 3 lines take markers well,
      118 do not. C5's option 1 is now scoped to that residue rather than
      to the whole gap, and its ordinary-English ground is discharged
      here. See the C5 item for the corrected reading.
- **E1 + E2 — DONE 2026-08-05** (`ae056a2`, wt: queue-batch-0806): an
      unrecognised licence now keeps the header checks (E1), and the sixteen
      unambiguous OSI trove classifiers resolve instead of flagging (E2).
      Rule-4 cold pass 2026-08-06 (0 MAJOR, terminal); LC residue ruled and
      applied the same day. Detail → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md)
      § *The licence gate learns proprietary*. (These two entries stood stale
      as open work until 2026-08-06 — the cycle-state residue class, corrected
      from the tree.)
- **E3 — FIXED 2026-08-06 with the E6b build** (ruled 2026-08-04:
      suppress): whole-shape fingerprint carve-out, both ruled spellings,
      canaried both directions — a fingerprint-prefixed body of the wrong
      length still blocks — and the suppression is counted in the tally,
      never silent. → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) § *E6b built*.
- **`PUBLIC_KEY_RX` subtracts silently — FIXED 2026-08-09.** It was a
      genuinely separate subtraction from the `public-key fingerprint(s)`
      counter that reads like it (E3's carve-out, counted inside the entropy
      loop; this one skipped the loop from outside it), settled by probe not by
      reading. Two real suppressions on the live tree were invisible. Counted
      now, suppression byte-identical, tests 122 → 134. →
      [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) § *secretscan's last invisible
      subtraction*.
- **E4 — FIXED 2026-08-06 with E7's D2** (one fix, both entries): the
      IPv6-shape rule now requires `::` or four-plus groups; clock times,
      port maps, ratios and hex colour triplets pass, real addresses still
      flag, tests both directions. → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md)
      § *E7 built*.
- **E8 — FIXED 2026-08-10**, the first child-reported defect to close under
      Track F. The reported diagnosis was wrong and the correction is the
      useful half: the trigger is a **hyphen** before the token's last `/`,
      not the leading-slash-plus-dot form — `/docs/some-dir/x.md` truncates
      to `dir/x.md` with no dot involved. One character in `_PATH_TOKEN`'s
      lookbehind, which now excludes every character the token class accepts;
      same hole and same fix as the `*`/`?` exclusion beside it. 8 findings
      dropped tree-wide (208 → 200), all of them the defect — including the
      E8 entry itself, which the bug was mangling. Root-anchored paths are
      still skipped whole, the docstring's named false negative, now pinned
      by a test. Module tests 76 → 86. →
      [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) § *E8 — pathscan truncated
      root-anchored paths*.

### Track F — the guard governance model (Mike, 2026-08-02)

*What a child repo may do when it meets a shared guard, and what it may never
do. Several items already on this board turn out to be instances of one frame
nobody had named.*


### The thing underneath all of it — state-tracking, not reasoning

Two independent sessions reached the same diagnosis in the same 24 hours, in
their own words: **not degraded reasoning, degraded state-tracking.** Every
failure was a stale belief, sincerely held, that had once been true — the
session record *was* accurate, those sections *were* duplicates by heading, the
work *had* been ready to close. In a long session the cheapest source of "what
is true" is what is already in context, and context is dense with things that
were true; verification costs a tool call and recall is free.


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
  [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md), rule-4 `⏳` queued in
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
[`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) § *The ⏳ pointer grammar mechanised*;
rule-4 `⏳` queued in § *Doctrine — review-owed*.


### All doctrine directive first, enforced second (Mike, 2026-08-09)

**The aim, verbatim** (Mike, 2026-08-09 — kept in his words because the first
filing of this item paraphrased *all doctrine* into *every rule*, and the drift
is the exact thing an aim this broad cannot afford):

> I would like all doctrine to be enforced i.e. policy as code. But it should
> also be directive so that it influences the thinking before it comes action
> for the policy-as-code to address

Two halves. The programme has only ever tracked the first, and the tracks above
are all instances of it. The restatement below is a reading of the quote, not a
replacement for it — where they differ, the quote governs.


### COMMUNICATION.md enforced — the first census finding, worked (2026-08-09)

Landed `753adb6`, `e61adc4`. An instance of (a) above, found by measurement
rather than by the census, and worth reading as evidence for how the census
should be run: the doc **declared its own unenforced state** in its enforcement
clause and nobody had priced what that cost.

**What Mike said, verbatim** (2026-08-09), because the trigger was a trust
failure and not a feature request:

> In all repos you are continuously failing to communicate to a level that
> lacks honesty, lacks transparency, lacks verification that allows
> falsehoods, I am talking over many days and many many session. This is
> actively diminishing my trust in claude and your work

**The measurement.** 6,704 assistant replies of 200+ characters, across 1,094
session transcripts in 18 repos, 2026-07 to 2026-08: bracketed aside over 25
chars in 67.2% of replies · uncommon acronym unexpanded 55.5% · sentence over
35 words 36.8% · bare reference code 17.4%. Of every reference code's **first
use in a session, 86% arrived with no gloss** (1,457 bare, 236 glossed). The
rate did not fall after the rules were written; reference-code density **rose**
over the month, 4.04 → 7.23 per thousand words.

**What landed.** `plainscan.py` — four rules, each carrying its ground: P1
undefined reference and P2 unexpanded acronym on a published standard
(digital.govt.nz, expand on first use); P4 buried aside on dated house doctrine
(COMMUNICATION.md 2026-07-15); P3 long sentence on a **house call**, because two
plain-language authorities were checked and neither publishes a cap. Warn-only
on both planes. One engine, two planes: the floor registry for committed prose,
and a `Stop` hook (`tools/hooks/plain-reply.py`) that lints the agent's own
reply and blocks it for rewrite.

**Ruled and live 2026-08-09; the reply plane UNWIRED 2026-08-15.** Mike:
*"switch it on, proposed"*. The reply plane blocked at **45 words / 60
characters** and applied in every repo. It came out six days later on measured
evidence that it was the largest single source of the unreadable output it
existed to prevent — a `Stop` hook cannot un-print, so each block appended a
second copy of the verdict rather than replacing it. **Destroy-or-repurpose is
Mike's open ruling** → item *The reply gate is UNWIRED* in this section. The
repo plane is unaffected and stands. Detail harvested to
[`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) § *The communication floor*.

- 🎯 **Repo plane rescoped to prose the principal reads — RULED and DELIVERED
      2026-08-10** (wt: plainscan-rescope-0810). Mike opened by proposing
      removal of plainscan altogether, on the ground that the trust review was
      about session replies and "99% of the documentation … is to keep a record
      … for consumption by yourself (claude) not me as the principal". The
      challenge back: full removal silently kills the reply gate —
      `plain-reply.py` imports `scan_text` from `plainscan.py` and fails open —
      and the repo prose Mike does read (ruling asks, review briefs, doctrine
      in a public repo) is the highest-stakes prose. His ruling, verbatim:
      *"I accept your recommendation"* — keep the engine and reply gate
      untouched; scope the repo plane to human-read docs by excluding records
      (`docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`), the same
      shape as the cold-pass records exclusion. This also settles the records
      half of the backlog item below: records are out by ruling, not deferral.
      Delivered in `e390382`: `RECORDS_GLOBS` in `plainscan.py` skips the three
      records paths when a directory is expanded — an explicitly named records
      file is still scanned, and a test guards `ROADMAP.md` from ever matching
      the `ROADMAP-DONE.md` glob; `--include-records` restores the old scope.
      Measured, not estimated: atelier's advisory tally fell 7,817 → 4,440, so
      records carried 3,377 findings. The reply plane is untouched, because
      `scan_text()` itself has no scoping and every reply is written to the
      principal. Module tests 47 → 51, suite 1,294 → 1,298 green, instrument
      tests exit 0 at the landing tree.
      ⏳ **Review queued** — the scoping was recommended, built, and its
      doctrine rewritten by the same session (delta: `tools/plainscan.py`,
      `tools/test_plainscan.py`, `tools/floor.py`,
      `docs/method/COMMUNICATION.md` § *The meta-rules that make it work*;
      intent record: this item; tier: Fable; pass type: cold).
      Brief written 2026-08-15 by a non-author cold session — REVIEW NOT RUN,
      still open for a cold Fable taker: `docs/reviews/2026-08-15-1033-communication-floor-cold.md`
      (deferred sibling `docs/reviews/2026-08-15-1033-communication-floor-cold.deferred.md`, opened only after
      the reviewer's findings are durably written).
      One brief covers this pointer and the enforcement-clause pointer in item
      `300-generalise-the-finding-don-t-just-fix-this-doc.md` (same doctrine section).
**P5 — the unintroduced-term rule: BUILT, MEASURED, REJECTED (2026-08-09).**
Not a stub and not a deferral: it was written, run over the whole corpus, and
deleted the same day on its own numbers. Recorded because the negative result
is the useful part.

The trigger was a real reply Mike put up as a test case — *"the interlock says
render the record's footprint as absent, diff it via sweep's engine ... its
content is the predicate"*. It passes P1–P4 cleanly and is close to unreadable,
because six terms are used as though already shared. Short confident sentences
read as clear while carrying nothing the reader can hold.

The rule was the classic definite-description test: `the X` where X never
appears earlier in the text. It needs no threshold, and the evidence sits
entirely inside the document. On the sample it worked — it caught *interlock*,
*record*, *predicate*.

Then it met the corpus. **90.6% of 6,764 replies fired**, 23,857 findings, and
two rounds of principled fixes did not move the rate:

| Fix | Firing rate |
|---|---|
| First cut | 90.7% |
| Head-noun shift for `the <X-ed> <Y>'s` | 90.7% |
| Common adjectives excluded (`the exact wording`) | **90.6%** |

The adjective fix cleared the top of the table and changed nothing overall,
which is what identified the real cause. The residual terms are *session*,
*repo*, *roadmap*, *review*, *doctrine*, *estate*, *floor* — checked against
atelier's own docs, where **`review` appears 5,333 times, `session` 3,858,
`floor` 2,326**. They are flagged because they appear with "the" before
appearing without it *in that one reply*.

**Why no fix exists.** The scanner's evidence window is one document; the
reader's knowledge spans years of working together. English marks shared
reference with "the", and in a long-running relationship nearly every domain
noun *is* shared. Nothing inside the text distinguishes a term the reader owns
from one they have never met, so no amount of list-tuning reaches it. Chasing
the rate with a findings-per-reply threshold was considered and refused: that
is fitting a number to the current measurement, which this house forbids.

**What it establishes, and it is worth more than the rule would have been.**
This defect class is genuinely outside policy-as-code, and now demonstrably so
rather than assumed. It belongs to part (b) above — doctrine that reaches the
moment of decision — and it is the first *measured* instance of that half being
the only available answer. The claim "it can't be automated" was right here,
and was only worth believing after it was tried.


### Coverage the programme does not yet reach

- **Three public repos in the account have no scanning at all** → § *the ranked
  residual* item 3 below. Public and unscanned is the combination that matters:
  the question is not "are they tidy" but "is anything in a public repo that
  should not be public".
- **The boundary findings** — the only open items with real exposure →
  § *Boundary findings surfaced by the measurement* below.
