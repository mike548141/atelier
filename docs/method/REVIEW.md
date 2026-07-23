# Review — the enforcement half of the doctrine

*`PROPAGATION.md` names the category error: **a doctrine that is read is not a
doctrine that is complied with.** Documents inform; they do not enforce. This is
what enforces — an independent review of the work, before the work is trusted.
The work makes the claim; the review is what earns the right to believe it.*

## Why review, and who reviews

The building model is the worst-placed judge of its own work: it shares every
blind spot that produced the work, and the apex's honesty burden is hardest to
discharge against oneself. So the check is **external** — a separate agent with
fresh context. That is the irreducible core, and it costs nothing an adopter
doesn't already have: **independence, different blind spots, and fresh context**
deliver most of the value even when the reviewer is the *same* model in a new
session. Capability is the multiplier on top, not the precondition: where a more
capable tier exists, deploy it at review — that is where its marginal value per
token is highest — and match reviewer capability to the stakes (see
`ECONOMICS.md`: the most capable available model reviews irreversible or
structural work; a mechanical gate — validators, CI — holds the floor for the
routine). The review is not a formality tax on good work; it is the thing that
lets "done" mean *verified* rather than *looks right*.

## Independence is more than fresh context

Fresh context is necessary but not sufficient. A review can be **cold-context yet
warm-questioned**: if the brief carries the framing of the party whose work is
under review, its questions aim where that party was already looking, and the
reviewer — however independent its *context* — inherits those blind spots through
the *ask*.

Two terms, because the rules turn on them. The **author** is the agent (or party)
whose judgement produced the work — the entity whose blind spots are in question,
whatever name the commit metadata carries. The **principal** is the deciding
human the agent serves (00-APEX). Rule 3 presupposes the two are *distinct*.
Where they are not — a solo operator adopting this doctrine for work they wrote
themselves — rule 3 gives nothing (rules 1–2 still deliver): the only remaining
independence is the cold reviewer's findings on the durable record, and an
adopter in that position should know the gap rather than assume the rule
covers it.

The grounding is one case — REACH (2026-07-12): an author-briefed review passed
a doc clean on four pre-seeded questions; an un-briefed adversarial re-run of
the same doc found eight findings, zero overlap, two MAJOR — on the exact
boundary the seeded questions steered around. One case is evidence, not proof,
and this one is confounded (the re-run read post-fix text, was primed to be
adversarial, and two cold reviewers diverge anyway) — what the rules encode is
the *mechanism* it exhibited: **framing leaks through the ask, not just the
context.** Standing test to strengthen or weaken the rules: an author-framed
review of doctrine or structural work earns an un-briefed re-run regardless of
its finding count (count is the wrong credibility test — see *What review is
not*); a pass that is clean *on the seeded questions specifically* is the
strongest trigger. Each such pair is a data point.

So these rules bind on top of fresh context — rules 1–2 whenever the brief is
written by, or on the framing of, the work's author; rules 3–4 whenever the
work is self-authored doctrine — rule 3 however the review was spawned, rule 4
governing who may spawn it:

1. **The author's questions are a floor, never a fence — and the deferral is
   structural, not willpower.** The author may seed attack questions — it knows
   where the hard trade-offs were — but seeded questions influence by their very
   existence: their topic and tone suggest where "the risk" lives, and a
   reviewer cannot un-read them. So they sit in a **deferred section of the
   brief, below the divider**, which the reviewer opens only after its own
   attack surface is committed (the same shape rule 2 gives prior verdicts).
   The reviewer names the load-bearing assumptions *itself* as its first act
   (lens 1 below), and treats the brief's framing, including its account of
   *what the work is*, as itself attackable (a "grounded in X" in a brief is
   the author's claim to test, not settled scope).
2. **Barred from prior reviews until its own findings are committed** —
   committed meaning *durably written to its draft*, before any prior verdict
   is opened. An earlier verdict is another channel for the author's framing;
   the reviewer reads it only after that point — to reconcile, never to anchor.
   Verifying a prior review's decisions (its `[fixed]` claims) is
   reconcile-step work, done after that point — not licence to read early.
3. **Findings on self-authored *doctrine* are the principal's to decide,
   not the author's.** Doctrine here is defined by **function, not file type**:
   any rule that governs future agent behaviour, whether it lives in prose, an
   ADR, a schema, a validator, a CI gate, or a template or skill that stamps
   behaviour into other repos — encoding a policy as code does not keep the
   escape. The `[rejected: grounds]` escape below stays sound for
   ordinary code, where a wrong rejection is caught mechanically; it is unsound
   where one agent both wrote the rule and judges the challenge to it. There the
   author records the verdict verbatim and applies nothing on its own; it may
   argue its case per finding, labelled as the author's position and kept below
   the reviewer's text — the decision is the principal's, and taken **informed**:
   the author owes a plain-language what / why / likely-impact before the
   principal rules, never a bare finding to rubber-stamp (`00-APEX.md`, *The
   principal's authority is conditioned on being informed*). An approval given
   without that account is not a decision the doctrine recognises.
4. **Self-authored doctrine earns a cold *spawn*, not just a cold context**
   (the principal's ruling, 2026-07-15, after the MODEL-ECONOMICS F1
   walk-through; sharpened by this rule's own cold pass, ruled the same day).
   The highest-stakes category is stated plainly: **self-authored doctrine**
   — work that is doctrine by function (rule 3's definition, single-sourced
   there) whose wording the author's own judgement produced. For that
   category the deferral discipline of rules 1–2 is necessary but not
   sufficient: its residual risk is the author's own compliance, and a wrong
   rule propagates to every repo and every future session that inherits it —
   the widest blast radius in the operating model. So the spawn test is a
   single criterion: **the review comes from a session the author neither
   started nor instructed.** The principal, a scheduled batch, and a neutral
   working session are *examples that must each pass that test*, not a list
   of exemptions — an author-written brief, queued by the author into a
   batch the author scheduled, fails it whatever the batch is called. The
   author's handoff when such work is finished: queue the review pointer
   (ROADMAP `⏳`, naming the delta and the intent record — a ceiling as well
   as a floor: refs only, no evaluative account, which belongs in the intent
   record where the reviewer's deferral discipline governs when it is read)
   and stop — the
   brief is written by the non-author who takes the item, and any spawner
   passing the criterion may take a `⏳` item (the principal opening a fresh
   session and pointing it at the queue is the worked example). The brief
   states its spawn provenance — who spawned the review and the
   author's non-involvement — and the verdict repeats it; a rule-4 pass with
   no provenance trail is unauditable, and unauditable is non-compliant.
   Routine, non-doctrine work keeps the warm-spawn-plus-deferral pattern of
   *When to review* below; the ban lands only where it pays.

This is the independence the external-reviewer rule was always reaching for —
the REACH case showed fresh context alone doesn't deliver it.

## What a review actually checks — widest scope, four lenses

**Scope is the whole commitment, never just the artefact in hand** (the
principal's ruling, 2026-07-21). The reviewer's scope is the widest the work
admits: the intent or idea that drives it, the decisions and assumptions that
went into it, the design, the documentation, the code, the test code — a wrong
test verifies nothing, so tests are reviewable on the same footing as the code
they exercise — and its real-world behaviour, exercised live where doing so is
possible and re-run from the work's own claims where it is not; a claim that
live exercise is impossible states its grounds, the same discharge shape as
every other (see *Re-run every "live-proven" claim* below). The brief's
**non-goals are the only legitimate narrowing — and the narrowing is itself
reviewable**: anything not named out of scope is in scope, "no source code" is
never grounds to shrink a verdict (the 2026-07-15 dismissal — *Review the
design* below), and a non-goal that fences off the very risk the work carries
is a finding, not a boundary — in a warm brief the author writes the
non-goals, so rule 1's brief-framing-is-attackable extends to them explicitly.
The lenses organise that scope; they do not bound it.

Not just "are there bugs". A real review runs all four:

1. **Approach & assumptions** — the most important lens. *Is this the right
   problem, solved the right way?* Attack the load-bearing assumptions by name;
   if one is false, the work is mis-built no matter how clean the code.
2. **Correctness & quality** — does it do what it claims; is it honest about
   what's done vs stubbed; any overclaim, any silent scope-cut.
3. **Completeness / harvest** — what the work *should* have covered and didn't;
   what already exists that it duplicated or ignored.
4. **Security & privacy** — a must on every review, not a specialist add-on
   (the principal's ruling, 2026-07-21). It runs at every altitude the scope
   reaches: at design altitude, what the work exposes, over-collects, or leaks
   by weakness of design — a privacy defect is a design defect before it is
   ever a code one; at code altitude, the likely threat vectors for the work's
   class — injection, cross-site scripting, authentication/authorisation gaps,
   secret handling, unsafe input paths. *Likely* means checked, not recalled:
   the reviewer is free — and expected — to consult open catalogues (OWASP
   Top 10 / ASVS, or the domain's equivalent) to confirm the likely vectors are
   covered rather than trusting memory. At design altitude the same lens carries
   a build-time obligation, not only a reviewer's after-the-fact check:
   **enumerate the design's threats before building it** — who and what could
   attack this surface, what it exposes, what it trusts — as a first-class,
   right-sized design step. That is a lightweight pass, not full STRIDE
   ceremony: name the handful of threats that actually bear on the work's class
   and show the design answers them, at the altitude where a wrong premise still
   costs a paragraph (lens 1; *Review the design, not only the build* below).
   Absent enumeration is the finding, the same shape as a missing `review:`
   line. (Grounded: the 2026-07-22 security-canon gap map — threat modelling was
   held as a review lens but unnamed as a first-class build activity.) And where
   the working harness ships a
   security scanner — Claude Code's `/security-review` is the house instance,
   sanctioned by the principal (2026-07-21) — the reviewer uses it **where it
   can reach the work**, folding its findings in as the mechanical floor
   layered under this lens (*What review is not* below), never a discharge of
   it, its clean pass a claim to weigh like any other. Reach is per review
   shape, and the verdict says which case applied: a pending-diff review aims
   the scanner at the in-scope diff; a landed-delta or design-time review may
   have nothing the scanner can read — there it runs only where it can
   genuinely be aimed at the work, else it is discharged in one explicit line
   with grounds. Two cautions, both live-proven at the rule's first execution
   (the 2026-07-21 cold pass, SL2): a pending-changes scanner scans whatever
   is dirty — on that cold pass, the review *brief*, injecting its deferred
   section into the reviewer pre-draft — so never run it over a brief or
   other deferred material before findings are committed; and where the
   scanner's own exclusions bar the work's file class (markdown
   documentation, for `/security-review`), its clean pass is definitionally
   empty — weigh it as nothing, and say so. Where the work genuinely has no
   security or privacy surface, the lens discharges in one explicit line with
   grounds — the same shape as `review: not warranted`, and for the same
   reason: omission is the bug, and no one can disagree with a blank.

**A confirmed security finding carries two marks beyond the standard
`[fixed]`/`[backlog]`/`[rejected]` tag** (*The lifecycle* step 4 below): a
**severity**, and a **recurrence-prevention step** — the change that stops the
*class* recurring, not only this instance (the SSDF "respond to vulnerabilities"
third leg). Where the finding sits in tooling this repo ships for others to
adopt, it also routes to the private-disclosure path in the repo-root
`SECURITY.md`. This is the security specialisation of the ordinary findings
flow, not a parallel one — a security finding is a review finding first.
(Grounded: the 2026-07-22 security-canon gap map — the credential-exposure
runbook was held; a general security-finding lifecycle was not.)

## Re-run every "live-proven" claim in scope

A recorded proof is a claim like any other, and it can be **stale by the time
it is durable**: a check that ran clean mid-build may be false at the commit that
recorded it — the fixtures moved, the exemption was never added, HEAD advanced,
or the proof only ever held in a hand-run the record then generalised. So a
review does not *read* the work's "live-proven" / "verified" assertions and take
them; it **re-runs them** within its scope and treats a proof that no longer
reproduces as a finding. Grounded twice: the post-method-review batch caught a
scan's "live-proven clean" that was false at its own recording commit (it flagged
its unexempted fixtures at HEAD), and the create-repo sweep caught the same class
again — a stamped, recorded proof that broke when run verbatim. This is lens 2
(does it do what it claims) applied to the record itself, and it feeds the
close-rule below: a proof you have not re-run is not a proof you can close on.

## The lifecycle — brief on top, verdict below, one file

Grounded in the `ros`/atelier practice. A review is a **durable artifact**, not a
throwaway chat:

1. **Brief** — before the review runs, write a scoped brief to
   `docs/reviews/<date>-<HHMM>-<slug>.md` (`HHMM` in UTC — `date -u`,
   ADR 2026-07-15): what the work is, the four lenses,
   and the
   **specific assumptions to attack**. Add a `[ ]` pointer in the ROADMAP. The
   brief is *ask on top*. **When the brief is written by, or on the framing of,
   the work's author**, the independence rules bind: seeded questions go in a
   deferred section below the divider, opened by the reviewer only after its own
   attack surface is committed — a floor, never a fence — and the brief's
   framing is itself attackable (see *Independence is more than fresh context*).
2. **Run** — the reviewer reads the repo and the brief and reviews deep, not
   fast. Findings get stable IDs so nothing is lost in synthesis.
3. **Verdict** — the reviewer's output (per-question answers, findings, a
   follow-up checklist) is appended to the **same file**, below a `---`
   divider. *Answer below the ask.* One file holds the whole exchange, so the
   question and its answer can never drift apart (EVIDENCE §9).
4. **Decision** — each finding is tagged **[fixed]** (done this session),
   **[backlog]** (a named ROADMAP slice), or **[rejected: grounds]** — the
   builder/owner may disagree with a finding, but the disagreement and its
   grounds are recorded in the verdict file, never resolved by silently dropping
   it (the same rule the layer-override discipline applies to doctrine
   conflicts). **The one carve-out:** findings on doctrine the *author itself*
   wrote (doctrine by function — rule 3 above) are decided by the
   principal, not the author; the author may record its counsel per finding,
   labelled as such, and applies nothing until the principal decides. Where such
   a finding is a parent/child doctrine conflict, this and `PROPAGATION.md`'s
   resolved-upward rule are the same act seen from governance and from layering:
   the principal decides, and the resolution lands in the parent. Once
   decided, fixes consolidate onto one ROADMAP follow-ups item; then tick
   the ROADMAP pointer and add a `SESSIONS.md` entry.
5. **Close** — a finding is only closed when its fix is itself verified, with a
   live proof where one exists. "Addressed the review" without exercising the fix
   is the apex violation the review existed to catch.

**Applying decisions to doctrine — and when the cycle stops.** Applying
decided findings to doctrine text is itself a doctrine edit and earns a
cold pass (ceremony-to-risk below). Prefer an applier that authored neither the
doctrine nor the verdicts — a neutral hand can harmonise a stale recommendation
with the principal's decision without defending either. And where the doctrine
is self-authored in rule 4's sense, the application inherits that status — the
applier's judgement produced the new wording — so while the cycle is open the
applier does not spawn the application review either: it queues the `⏳`
pointer for a non-author to take. For that review, rule 4's criterion tests
the *delta's* author — the applier — at minimum, and prior authors in the
chain where practical. The terminal application — one applying the rulings of
a pass that returned no MAJOR — closes without a queued pointer, per the
close rule below. An application review
cannot fully honour rule 2 — the delta it reviews carries the prior verdicts'
decision stamps — so its sequence is: review the edited doctrine at HEAD and
commit findings *first*, open the verdict-file hunks after; the residual
exposure is named, not denied. And the cycle terminates (law of diminishing
returns — the principal's ruling, 2026-07-13): it **closes when a pass returns
no MAJOR finding** — what remains is decided into the backlog, and that
application does not spawn another full ceremony. The escape valve if it *isn't*
converging: when the MAJOR count is not falling from pass to pass, do not keep
cranking — stop and ask the principal for direction.

## Whether work earns a review at all — calibrate to risk

The lifecycle above is the *full* ceremony; **not all work earns it.** The
trigger is **commitment, not artefact** — the question is never what form the
work took, but *what will come to rest on it once it is trusted*. A design others
will build to, a decision that forecloses alternatives, a diff that ships: each
is a commitment, each is reviewable on the same footing. Asked while holding a
paragraph, a plan, or a patch, the question still parses — which is the point,
and why it is phrased this way (see *Review the design* below for the framing
defect this replaced).

Match the gate to the cost of being wrong (`ECONOMICS.md` — "match the
ceremony to the risk"): first-of-kind or structural work, a silent-failure mode,
doctrine text, and irreversible or public actions earn the independent
fresh-context review; work whose tests and dogfooding exercise it end-to-end over
*already-reviewed* machinery is **self-verifying** — there the mechanical floor
*is* the review, and a brief→verdict cycle is overhead, not safety. Under-review a
risky commitment and the defect ships; over-review a safe one and the ceremony
crowds out the work. Same "layers, not alternatives" split as *What review is not*
below, applied one level up — to the decision to review at all.

## Review the design, not only the build — the earliest review is the cheapest

*The principal's ruling, 2026-07-18: "Fable reviewers are just as much, if not
more so, to test our thinking, assumptions, decisions and architecture. Not
just code… reviewing things before we build them helps us reduce rework and
improve the quality of the things we do build."*

Everything above answers *whether* and *how* a review runs. This answers
**when in the lifecycle** — and it is a distinct claim, because review is an
**input to building, not only a gate after it**. A wrong premise caught at
design time costs a paragraph; the same premise caught after the build costs
the build, and every decision that was stacked on it. Lens 1 is already named
the most important lens — this is the corollary nobody had written down: lens 1
has the most to bite on *before* the code exists, when changing the answer is
still free.

So a **captured feature, a ratified design, or a structural decision earns a
review in its own right** — a review is not something work qualifies for by
containing code. Doctrine, ADRs, roadmap direction, an architecture note, a
decision recorded in a session log: all reviewable, all cheapest to review at
the moment they are written.

**Why this needed writing at all — the framing was the trap.** Every prior
formulation here was phrased around *a change*, and that grammar quietly
presupposes the work already exists: a reader holding a design rather than a
diff found every sentence shaped for the diff, and concluded the answer was no.
The rule was never wrong — its framing encoded a late-review default that its own
lens 1 contradicts. **The correction belongs upstream, not here.** The trigger
above now keys on commitment rather than artefact, so a design-holder is inside
the grammar at the point of asking; this section no longer has to rescue a reader
the previous wording had already turned away. When a written rule keeps being
broken, suspect its framing before its enforcement — restating it louder assumes
non-compliance, where checking the grammar asks whether the rule was ever
findable from where the reader stood. (Mike, 2026-07-19.)

**Enforcement is structural where a machine can reach it, conventional where
it can't — stated per surface, because the written rule demonstrably did not
hold.** Since 2026-07-21 the artefact exists (closing 2026-07-19 cold-pass
F6): the ADR template and decisions README carry the `review:` field, and
`tools/reviewscan.py` reds a new decision record that omits the line — there
the omission is caught mechanically. Roadmap sections carry the same
convention by template prose only: a lint on roadmap headings would fire on
prose and be trained away (the 0820 record's grounds for deferring it), so
for those records the remedy below remains a written rule, honestly named.
Grounded in two incidents, the second decisive: 2026-07-15, a reviewer
dismissed a committed-direction expansion as *"zero source code, so nothing my
verdict should have covered"* — the rule already said otherwise. Then
2026-07-18 (`ros`, model-datasheet catalogue), a building session declined to
queue a review on the same "no code" grounds **while the correct rule sat in
three places it had access to** — the repo's own review policy, this file, and
that session's memory of the 2026-07-15 correction. Writing it a fourth time
is the category error `PROPAGATION.md` names: *a doctrine that is read is not a
doctrine that is complied with.*

The failure mode is not ignorance, it is **invisibility** — *declining* a
review is an omission, and an omission reads identically to nobody having
considered it. So the remedy is to make the decline an act:

> Where a repo records design or direction durably (a roadmap section, an ADR,
> a doctrine change), **each such record carries a review line** — a queued
> pointer, or an explicit `review: not warranted — <grounds>`. **Omission is
> the bug.** A reviewer, or the principal, can then disagree with a stated
> judgement; neither can disagree with a blank.

Calibration still applies — this widens *what* is reviewable and *when*, never
the ceremony. Most design records will honestly carry "not warranted", and that
is the rule working: the cost is one line and a moment's thought, paid at the
point the thought is cheapest. Under-review a premise and the build inherits
it; over-ceremony a routine note and the practice crowds out the work.

## When to review — inline or batched

Both are sanctioned for routine work; pick per cost and how blocking the
result is (`ECONOMICS.md`). For self-authored doctrine the pick is not
the building model's to make: rule 4 puts the spawn in a non-author's hands,
whichever path the economics favour:

- **Inline background agent** — when economics allow, the building session spawns
  the review as a background agent and verifies as it goes, no context switch.
  (This is how the atelier foundation review ran.) The spawn prompt *is* a brief,
  and the spawning session is usually the work's author with its framing at its
  warmest — so the independence rules bind it in full: seeded questions deferred
  (a section or file the reviewer opens only after committing its own attack
  surface), never a fence. One carve-out: **self-authored doctrine cannot take
  this path at all** — rule 4 requires its review be spawned by a non-author.
- **Batched queue** — when they don't, queue the briefs and run them together
  later. The carve-out reaches here too: an author-queued, author-scheduled
  batch is still an author spawn and fails rule 4's criterion — rule-4 work
  enters the queue as a `⏳` pointer for a non-author to take, never as an
  author-written brief.

Either way the review stays **pre-scoped and short — short in ceremony, never
in scope**: "scoped" bounds the *subject* handed to the reviewer, and within
that subject the scope mandate above governs everything examined. It is still
spend — so it lives inside `ECONOMICS.md`'s marginal-cost self-check.

## What review is not

- **Not a rubber stamp.** A verdict earns trust by *showing its work* — the
  load-bearing assumptions named and attacked, the live proofs re-run, the
  sibling docs checked — never by its finding count. A clean verdict with that
  trail is a real result; a clean verdict without it is the suspect one.
  Counting findings is the wrong test in both directions: a busy review can
  still miss the majors (the author-briefed REACH pass found five and missed
  two), and distrusting clean verdicts just pressures reviewers to manufacture
  findings. Briefs say "review deep, not fast" for a reason.
- **Not a substitute for the mechanical floor.** Validators and CI catch the
  regressions cheaply and on every change; the capable-model review is for the
  judgement a validator can't make. They are layers, not alternatives.
- **Not the document's job.** Writing the standard down (all of `method/`) is
  necessary and not sufficient. This practice is the other half. Ship both or
  you've shipped the costume, not the doctrine.
