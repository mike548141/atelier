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
warm-questioned**: if the work's author writes the brief's attack questions, they
aim where the author was already looking, and the reviewer — however independent
its *context* — inherits the author's blind spots through the *ask*. Grounded in
the REACH case (2026-07-12): the author-briefed review passed the doc clean on
four pre-seeded questions; an un-briefed adversarial re-run of the same doc found
eight findings, zero overlap, two MAJOR — on the exact boundary the seeded
questions steered around. So when the work's author commissions the review of its
own work, three rules bind on top of fresh context:

1. **The reviewer chooses its own attack surface.** No author-seeded questions;
   the brief scopes *what the work is*, not *what to doubt about it*. The reviewer
   names the load-bearing assumptions itself — that naming is the review's first
   act (lens 1 below), not an input handed to it.
2. **Barred from prior reviews until its own verdict drafts.** An earlier verdict
   is another channel for the author's framing; the reviewer reads it only after
   committing its own findings — to reconcile, never to anchor.
3. **Findings on self-authored *doctrine* are the principal's to disposition, not
   the author's.** The `[rejected: grounds]` escape below lets a builder overrule
   a reviewer — sound for code, unsound when one agent both wrote the doctrine and
   judges the challenge to it. There the author records the verdict verbatim and
   applies nothing on its own; the principal decides.

This is the independence the external-reviewer rule was always reaching for — the
REACH case proved fresh context alone doesn't deliver it.

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
   `docs/reviews/<date>-<slug>.md`: what the work is, the three lenses, and the
   **specific assumptions to attack**. Add a `[ ]` pointer in the ROADMAP. The
   brief is *ask on top*. **Exception when the work's author writes the brief:**
   it scopes *what the work is* and stops — the reviewer chooses the assumptions
   to attack itself (see *Independence is more than fresh context*), so the author
   can't steer the review to its own blind spots.
2. **Run** — the reviewer reads the repo and the brief and reviews deep, not
   fast. Findings get stable IDs so nothing is lost in synthesis.
3. **Verdict** — the reviewer's output (per-question answers, findings, a
   follow-up checklist) is appended to the **same file**, below a `---`
   divider. *Answer below the ask.* One file holds the whole exchange, so the
   question and its answer can never drift apart (EVIDENCE §9).
4. **Disposition** — each finding is tagged **[fixed]** (done this session),
   **[backlog]** (a named ROADMAP slice), or **[rejected: grounds]** — the
   builder/owner may disagree with a finding, but the disagreement and its
   grounds are recorded in the verdict file, never resolved by silently dropping
   it (the same rule the layer-override discipline applies to doctrine
   conflicts). **The one carve-out:** findings on doctrine the *author itself*
   wrote are dispositioned by the principal, not the author — the author can't
   both write the doctrine and reject the challenge to it (see *Independence is
   more than fresh context*). Fixes consolidate onto one ROADMAP follow-ups item; then tick the
   ROADMAP pointer and add a `SESSIONS.md` entry.
5. **Close** — a finding is only closed when its fix is itself verified, with a
   live proof where one exists. "Addressed the review" without exercising the fix
   is the apex violation the review existed to catch.

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
  (This is how the atelier foundation review ran.)
- **Batched queue** — when they don't, queue the briefs and run them together
  later.

Either way the review stays **scoped and short**, and it is still spend — so it
lives inside the "know which pool you're spending" rule.

## What review is not

- **Not a rubber stamp.** A review that finds nothing on non-trivial work is
  itself suspect — either the scope was too narrow or the reviewer went fast.
  Briefs say "review deep, not fast" for a reason.
- **Not a substitute for the mechanical floor.** Validators and CI catch the
  regressions cheaply and on every change; the capable-model review is for the
  judgement a validator can't make. They are layers, not alternatives.
- **Not the document's job.** Writing the standard down (all of `method/`) is
  necessary and not sufficient. This practice is the other half. Ship both or
  you've shipped the costume, not the doctrine.
