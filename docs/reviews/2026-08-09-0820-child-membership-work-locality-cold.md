# Cold pass — the child-membership and work-locality rules

**Pass type:** doctrine cold pass (REVIEW.md rule 4 — self-authored doctrine).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04).

## Spawn provenance

- **Author of the work under review:** the session that landed the delta on
  2026-08-09 (see *What the work is*).
- **Who spawned this review:** the principal (Mike), in a session he opened on
  2026-08-09 and pointed at the review queue — rule 4's worked example. His
  words: *"Please do any review work that waiting."*
- **Author's non-involvement:** the taker session authored no part of this
  delta, was neither started nor instructed by the authoring session, and wrote
  this brief as the non-author taker. Rule 4's single criterion is met, and the
  tier was checked at selection.
- **Orchestration shape:** the review runs under an orchestrator holding a
  context partition — the intent-record references are withheld from this brief
  and handed to the reviewer only after its own findings are durably written
  (REVIEW.md rule 1, the one arrangement honestly called structural).

## What the work is

Doctrine landed 2026-08-09, reviewed at HEAD:

1. [`docs/method/PROPAGATION.md`](../method/PROPAGATION.md) — the new
   *Who is a child, and what a child may hold* subsection under
   § *layer-override*.
2. [`docs/method/CONCURRENCY.md`](../method/CONCURRENCY.md) — the
   work-locality paragraphs under § *Stay in your lane*.
3. The `CHANGELOG.md` entry that landed with them.

## Scope

Widest the work admits (REVIEW.md § *What a review actually checks*): the
intent behind the rules, their wording as it will bind future sessions, their
fit with the surrounding doctrine, and any conflict or duplication with sibling
method docs. **Non-goals — one, and it does not fence the risk:** the reviewer
does not decide any finding. This is self-authored doctrine; findings are the
principal's to rule on (rule 3). Counsel may be recorded, labelled as such.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. Is child-membership-by-default the right frame? Does work-locality
   solve the problem it names?
2. **Correctness & quality** — do the new rules say what they mean; are the
   edge cases a future session will actually hit answered or honestly stubbed?
3. **Completeness / harvest** — what should the rules have covered and did
   not; what existing doctrine do they duplicate, contradict, or ignore?
4. **Security & privacy** — mandatory. atelier is PUBLIC: check whether the
   new text joins any private repo's name to its posture or otherwise leaks
   estate detail; check what the membership rule causes future records to
   carry. If the lens genuinely has no surface beyond that, discharge it in
   one explicit line with grounds. The house security scanner reads pending
   diffs; this is a landed-delta review, so state the reach case that applied.

## Re-run obligation

Any claim in the delta text stamped as measured, live-proven, or grounded is
re-run, not read, where the repo admits it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the intent-record refs are orchestrator-held under the rule-1 context partition, handed over only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/sessions/`, every prior verdict in
`docs/reviews/`, and the intent-record item for this delta (its reference is
held by the orchestrator and will be provided on receipt of your committed
findings). Reconcile after, never anchor before.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `CM`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then report; the deferred
references arrive; append a reconcile section and finalise.

---

# Verdict — cold pass, phase 1

**Provenance, repeated.** Reviewer: a cold session under the batch
orchestrator, holding the rule-1 context partition — the intent-record
references are withheld until this verdict is durably written. The reviewer
authored no part of the delta and was neither started nor instructed by the
authoring session; the review was spawned from the principal's queue
instruction of 2026-08-09. Tier: Fable, checked at selection (ruling
2026-08-04). Delta reviewed at HEAD (`5f2e4c7`); the delta commit is
`03bcfeb`, plus the CHANGELOG entry that followed in the next commit
(see CM10).

**Load-bearing assumptions, named first (my own list, before any deferred
reading):**

1. Membership needs a fact of the matter, and default-in is safer than
   opt-in because an ungoverned repo is an invisible failure.
2. DRY applies to doctrine across repos: a restatement is a falsifiable
   copy; pointers and stamped copies cover every legitimate need to repeat.
3. A ruled divergence must be distinguishable from drift, and recording it
   in the child suffices.
4. For fixes, the target repo's context (tests, floor, full picture)
   dominates the finder's context, and queueing into the target's roadmap
   preserves the finding — which assumes the target has a roadmap and a
   future session that reads it.
5. The enumerating boards' denominator can be made honest by rule alone.

Assumptions 1, 2 and the core of 4 hold under attack; 3 and 5 are where the
findings cluster.

## Per-lens answers

**Lens 1 — approach & assumptions.** Child-membership-by-default is the
right frame, and I verified its grounding independently: the enumeration
instrument's own header records the 2026-07-25 case (12 of 13 children
running a frozen scanner list, nothing reporting it) — exactly the
invisible-failure class a default-in rule closes. Opt-in would recreate the
"repo nobody decided about" category the rule exists to abolish.
Work-locality does solve the problem it names: the sideways-fix temptation
is real in audit shape, and the queue lane keeps the finding without the
context-free fix. But the membership wording overshoots its own frame
(CM1), and the honest-denominator claim outruns what any instrument can
measure (CM4).

**Lens 2 — correctness & quality.** The rules mostly say what they mean.
Re-runs, where the repo admits them: `tools/floorfleet.py` and
`tools/pins.py` exist and answer "is it current / is it wired" as the text
claims — verified. The parent economics doctrine does hold
billing-state-of-the-marginal-token and tier-by-risk — verified in
`ECONOMICS.md`, so "the parent had already superseded" is true as written.
The "third fence" account of CONCURRENCY § *Stay in your lane* is accurate,
and the new paragraph genuinely sharpens rather than restates it. The
cross-reference to § *One statement, stamped copies* resolves. The
four-child restatement case itself lives in private repos this tree cannot
reach; it is taken as the audit's claim, to be checked against the intent
record at reconcile. Edge cases not answered: CM2, CM6.

**Lens 3 — completeness / harvest.** No competing membership statement
exists elsewhere in `method/`, `build/` or the README (swept) — the new
subsection is the first written home, correctly placed. Gaps: the exemption
lane has no estate-visible register or revisit trigger (CM3); the new
three-verb list partially restates the adjacent layer-override bullets
(CM5); the glossary still has no *Child* entry (CM11).

**Lens 4 — security & privacy.** Substantive surface exists and was
examined; not discharged as blank. Scanner reach, stated: this is a
landed-delta review of markdown doctrine — `/security-review` excludes the
file class, so its pass would be definitionally empty and was not run. The
house scanners were run instead at HEAD: leakscan clean (exit 0,
`local-term×3` as expected), wrapscan and datescan clean; every delta line
wraps within 85 columns. The grounding paragraph names four private
siblings and joins them to doctrinal state; measured against `RECORD.md`
§ *The record is public*, the regulated class is name × *sensitive*
posture, and doctrinal staleness is not that class — all four names are
already published on other public surfaces of this repo, and each is
load-bearing for the lesson (the sibling-as-canonical case needs two
names to state at all). Compliant as written; the residue is CM8, and the
membership rule's forward pressure on records is CM7.

## Findings

**CM1 (MODERATE, lens 1/2) — membership is unbounded by ownership or
estate.** "Every repo the principal works an agent in" literally annexes
repos the principal does not own or control: an upstream open-source
checkout, a fork held to send a patch, a client's repo worked under their
rules. Child-wiring there is impossible or wrong, yet as written each such
repo needs its own principal-ruled exclusion. The rule needs a bound — the
principal's estate, or ownership/control — or a class-exclusion lane, so
the exclusion mechanism is reserved for the deliberate cases it was built
for. Counsel: one clause ("every repo of the principal's estate…" or "…the
principal owns or controls") closes it without weakening the default.

**CM2 (MODERATE, lens 2) — an exclusion ruling has no recorded home.** The
subsection opens by condemning rules "applied without being written down",
yet the specific exclusion — the only thing keeping the denominator honest
— is given nowhere to live. An excluded repo has, by construction, no child
block to carry the record, and the public parent must not enumerate private
names. The estate already has the pattern: the private estate-root repo,
which the parent points at by property, not name. One sentence naming that
home closes the gap; without it, exclusions are oral rulings — the exact
defect this delta was written to end.

**CM3 (MODERATE, lens 3) — ruled exemptions have no register and no
revisit trigger.** An exemption recorded only in the child means the estate
learns its exemption set solely by opening every child, and when the parent
rule later moves, nothing re-tests the exemptions granted against its old
wording — a ruled exemption can silently outlive its grounds, which is
drift wearing a permission slip. It also diverges, unreconciled, from
REVIEW.md step 4's "the resolution lands in the parent" for parent/child
doctrine conflicts. Counsel: give the child-side record a fixed, greppable
grammar (the child block is the natural carrier) so a fleet instrument can
enumerate exemptions machine-locally — names stay off the public parent —
and state which of the two rules governs where the record lives.

**CM4 (minor, lens 2) — "answerable" overclaims.** "This rule is what
makes 'is it a child at all' answerable too" — the rule makes the question
*decidable* (there is now a fact of the matter); nothing *enumerates* the
denominator. Discovery in the instruments is directory-local to one
machine, so a repo worked elsewhere never appears on any board, and no
instrument can list "every repo the principal uses". The sentence
half-concedes this; tighten it to decidable-not-enumerable, or name the
discovery gap outright — the honest-claims discipline this repo applies
everywhere else.

**CM5 (minor, lens 3) — the three-verb list partially restates the
bullets directly above it.** *Add* ≈ narrow/append; *Conflict* ≈
never-silently-contradict. The section now states one rule twice in
adjacent blocks — inside the very delta that forbids a restatement as "a
second original that drifts silently". Intra-file and cross-referenced, so
the risk is low, but the drift mechanism is identical: an edit to one block
will miss the other. Counsel: fold the old bullets and the new subsection
into a single statement next time either is touched.

**CM6 (minor, lens 2) — the queue lane dead-ends on an unwired child.**
The repos an estate audit most often finds wanting are the not-yet-wired
ones — which may have no roadmap to queue into. Where the finding goes then
is unanswered: the finder cannot fix (work-locality), cannot queue (no
queue), and the membership rule says the repo is nonetheless a child.
Counsel: name the fallback (queue in the estate root, or "wiring the queue
surface is the one sideways act permitted").

**CM7 (minor, lens 4) — queued findings cross visibility boundaries
unwarned.** The queue lane moves audit evidence from the finder's context
into the *target* repo's roadmap, and nothing reminds the writer that the
target's visibility governs what the evidence may carry: an estate-audit
finding queued into a public child can join a private sibling's name to its
posture in a repo whose records rule the writer may not have loaded. One
line pointing at `RECORD.md`'s join rule closes it. The membership rule
adds the same forward pressure on enumerating boards and records — the
"honest denominator" is a list of every repo the principal uses, which must
never materialise on a public surface.

**CM8 (note, lens 4) — the grounding thickens the grey band an open draft
ADR is measuring.** The paragraph is a doctrine-band instance of name ×
operational state (four named private siblings, one "misled a session"),
the class the 2026-08-05 estate-internal-context ADR holds un-ruled.
Compliant with the narrow rule as it stands, and doctrine worked examples
are the sanctioned 4% band — recorded so that if the principal rules
posture B there, this paragraph is on the sweep list; no action otherwise.

**CM9 (note, lens 2) — unattributed quotation.** "drifted 17 days behind a
provider change, and misled a session into arguing from a falsified fact"
carries quotation marks with no named source; a cold reader cannot tell
whose words they are — an audit record, the principal, or emphasis. House
style attributes its quotes. Name the source or drop the marks.

**CM10 (note, process) — landing = queuing ran in the TA9 shape again.**
The doctrine commit (16:06:17) carried neither pointer nor CHANGELOG and
was pushed on its own (a separate floor run exists for it); both followed
at 16:12:28 in the records commit. TA9 (2026-07-28) ruled minutes-later
pointer-in-the-completing-commit as meeting the rule's intent, and this
matches that shape — but the pattern is now recurring, and rule 4's
grammar still names no commit for the single-commit-landing case. Also:
the brief's "the CHANGELOG entry that landed with them" is loose — it
landed six minutes later in a different, separately pushed commit. Pointer
location itself is unverified here (its probable commit is the barred
intent record); to be closed at reconcile.

**CM11 (note, lens 3) — the glossary never defines *Child*.** *Floor* and
*Bearing* are defined against "child repo", and membership is now ruled
doctrine; a one-line glossary entry pointing at the new subsection is the
cheap harvest.

## Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE · 4 minor · 4 note.**

The rules are sound, correctly homed, honestly grounded where this tree can
check, and the re-runnable claims all re-ran true. The MODERATEs are
boundary and bookkeeping gaps in an otherwise right rule, not challenges to
its substance. All findings are the principal's to rule; everything marked
"counsel" above is the reviewer's counsel, nothing more.

## Follow-up checklist

- [ ] Principal rules CM1–CM7 (CM8–CM11 are notes; CM8 rides on the open
      estate-internal-context ADR, CM10's pointer check closes at
      reconcile).
- [ ] Reconcile section below, after the intent-record references arrive:
      verify the four-child restatement case against the audit record;
      verify the queued pointer's commit and refs-only grammar (CM10);
      note agreements, divergences, and anything missed.
- [ ] Decided fixes consolidate onto one ROADMAP follow-ups item
      (REVIEW.md lifecycle step 4); application inherits rule-4 status.

## Reconcile

Deferred references received 2026-08-09 after the verdict above was durably
written: the *Estate duplication + exception audit* roadmap item (opened
alone; the rest of the roadmap, the archive, sessions, and all other
verdicts stayed barred), plus read-only git over the landing commits for
CM10.

**Agreements — the intent record strengthens four findings.**

- **CM1 confirmed live, not hypothetical.** The audit's own coverage check
  met exactly the edge CM1 names: a third-party clone of an upstream
  project sits beside the estate and was dismissed from the denominator on
  never-worked-in grounds — the only ground the rule as written offers.
  One session's work in that clone would, by the current wording, demand a
  principal-ruled exclusion for a repo the principal does not own.
- **CM2 confirmed forward-binding.** The record closes "no repo needs an
  exclusion ruling today" — so no exclusion yet exists, and the question of
  where one would be recorded remains unanswered rather than answered
  elsewhere.
- **CM3's cost is in the record.** The exception half enumerated eleven
  ignore-file globs and roughly 120 line markers by opening every child,
  and says of itself that it is "recorded here so the next sweep does not
  re-derive it" — the open-every-child cost CM3 names, paid live, with the
  re-derivation risk acknowledged in the record's own words.
- **CM7/CM8's pressure is visible in the record itself.** The child-owned
  findings list joins private siblings' names to operational and doctrinal
  state at length, on the public roadmap — the records-band accumulation
  the draft 2026-08-05 ADR measures, and the forward pressure CM7
  predicted the membership rule would add.

**Resolved or softened by the intent record.**

- **CM9 — source found.** The quotation is a child repo's own record: the
  intent record attributes it ("`faves` recorded that its copy…" — name
  already published in the doctrine paragraph under review). The finding
  narrows to attribution-in-text: the doctrine paragraph should say whose
  words they are, as the intent record does. Severity unchanged (note).
- **CM4 — softened, stands.** The denominator *was* enumerated in
  practice: the record cross-checked every project path the agent has been
  used in against the child list (12 worked repos, all children). So a
  machine-local discovery source exists; the overclaim narrows to "no
  instrument does this — it was a hand sweep". The cheap fix is now
  cheaper: name that source in the doctrine sentence, or teach it to the
  enumeration instruments.
- **CM10 — verified, closed.** The queued pointer sits in the records
  commit (`a6af6d3`, 2026-08-09 16:12:28 +1200), refs-only and
  grammar-compliant: delta (both files plus the CHANGELOG entry), intent
  record, tier (Fable), pass type (doctrine cold pass), no evaluative
  account, plus the author-may-not-spawn line. The completing-commit
  reading holds (TA9 shape): the pointer landed with the commit that
  finished the series. The residual counsel stands — the doctrine commit
  was pushed alone at 16:06:17 with its own floor run, so a roughly
  six-minute pushed-but-unpointed window existed, and rule 4's grammar
  still names no commit for this recurring shape.

**Post-reconcile additions — findings the intent record revealed.**

**CM12 (minor, lens 2, post-reconcile) — the practised queue lane is
stricter than the written one, and the findings are parked meanwhile.**
The doctrine grants the finder a sideways queue-write: "the auditing
session may queue what it found in the target repo's own roadmap". The
intent record declines to exercise exactly that — its child-owned findings
are "recorded here only so the estate has one list; each needs queueing in
its own repo's roadmap by a session working that repo". Two consequences:
the written rule and the ruling-as-practised diverge on whether the
sideways queue-write is permitted, and until someone queues, the findings
live only in the finder's repo — which the doctrine's own rationale calls
a finding at risk ("a finding nobody can act on later is a finding lost";
the target's next session does not read atelier's roadmap). Counsel:
either exercise the lane the doctrine grants, or amend the doctrine to the
practised shape and name who moves a parked list, and by when.

**CM13 (note, lens 2, post-reconcile) — the intent record's "landed this
commit" is one commit off.** Its frame sentence says the two doctrine
sections landed "this commit"; they landed in the prior, separately pushed
commit (`03bcfeb`). The queue pointer's own "this commit" claim — about
the CHANGELOG entry — is accurate. Same looseness class as CM10; worth a
one-word correction whenever the record is next touched.

**Grounding check owed from phase 1.** The four-child restatement case is
evidenced in the intent record at file level — paths, line counts, the
superseded billing model and role mapping, the sibling-named-as-canonical
quotation — matching the doctrine's grounding paragraph on every point
this tree can check. Taken as verified to the limit the review's reach
admits; the child repos themselves are outside this checkout by design.

## Final tally — post-reconcile

**PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE · 5 minor · 5 note**
(CM1–CM11 from phase 1, CM10 verified and closed at reconcile, CM9
narrowed; CM12–CM13 added post-reconcile). No phase-1 finding changed
severity; the overall line is unchanged. All findings remain the
principal's to rule; counsel is labelled where given.
