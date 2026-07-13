# Review — the enforcement half of the doctrine

*`PROPAGATION.md` names the category error: **a doctrine that is read is not a
doctrine that is complied with.** Documents inform; they do not enforce. This is
what enforces — an independent review of the work, before the work is trusted.
The build makes the claim; the review is what earns the right to believe it.*

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
`MODEL-ECONOMICS.md`: the most capable available model reviews irreversible or
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
written by, or on the framing of, the work's author; rule 3 whenever the work
is self-authored doctrine, however the review was commissioned:

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
   ADR, a schema, a validator, or a CI gate — encoding a policy as code does not
   keep the escape. The `[rejected: grounds]` escape below stays sound for
   ordinary code, where a wrong rejection is caught mechanically; it is unsound
   where one agent both wrote the rule and judges the challenge to it. There the
   author records the verdict verbatim and applies nothing on its own; it may
   argue its case per finding, labelled as the author's position and kept below
   the reviewer's text — the decision is the principal's.

This is the independence the external-reviewer rule was always reaching for —
the REACH case showed fresh context alone doesn't deliver it.

## What a review actually checks — three lenses

Not just "are there bugs". A real review runs all three:

1. **Approach & assumptions** — the most important lens. *Is this the right
   problem, solved the right way?* Attack the load-bearing assumptions by name;
   if one is false, the work is mis-built no matter how clean the code.
2. **Correctness & quality** — does it do what it claims; is it honest about
   what's done vs stubbed; any overclaim, any silent scope-cut.
3. **Completeness / harvest** — what the work *should* have covered and didn't;
   what already exists that it duplicated or ignored.

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
   `docs/reviews/<date>-<HHMM>-<slug>.md`: what the work is, the three lenses,
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
with the principal's decision without defending either. An application review
cannot fully honour rule 2 — the delta it reviews carries the prior verdicts'
decision stamps — so its sequence is: review the edited doctrine at HEAD and
commit findings *first*, open the verdict-file hunks after; the residual
exposure is named, not denied. And the cycle terminates (law of diminishing
returns — the principal's ruling, 2026-07-13): it **closes when a pass returns
no MAJOR finding** — what remains is decided into the backlog, and that
application does not spawn another full ceremony. The escape valve if it *isn't*
converging: when the MAJOR count is not falling from pass to pass, do not keep
cranking — stop and ask the principal for direction.

## Whether a change earns a review at all — calibrate to risk

The lifecycle above is the *full* ceremony; **not every change earns it.** Match
the gate to the cost of being wrong (`MODEL-ECONOMICS.md` — "match the ceremony to
the risk"): first-of-kind or structural work, a silent-failure mode, doctrine
text, and irreversible or public actions earn the independent fresh-context
review; a change whose tests and dogfooding exercise it end-to-end over
*already-reviewed* machinery is **self-verifying** — there the mechanical floor
*is* the review, and a brief→verdict cycle is overhead, not safety. Under-review a
risky change and the defect ships; over-review a safe one and the ceremony crowds
out the work. Same "layers, not alternatives" split as *What review is not* below,
applied one level up — to the decision to review at all.

## When to review — inline or batched (the building model's call)

Both are sanctioned; pick per cost and how blocking the result is
(`MODEL-ECONOMICS.md`):

- **Inline background agent** — when economics allow, the building session spawns
  the review as a background agent and verifies as it goes, no context switch.
  (This is how the atelier foundation review ran.) The spawn prompt *is* a brief,
  and the spawning session is usually the work's author with its framing at its
  warmest — so the independence rules bind it in full: seeded questions deferred
  (a section or file the reviewer opens only after committing its own attack
  surface), never a fence.
- **Batched queue** — when they don't, queue the briefs and run them together
  later.

Either way the review stays **scoped and short**, and it is still spend — so it
lives inside the "know which pool you're spending" rule.

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
