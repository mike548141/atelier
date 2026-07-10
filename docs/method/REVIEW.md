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

## What a review actually checks — three lenses

Not just "are there bugs". A real review runs all three:

1. **Approach & assumptions** — the most important lens. *Is this the right
   problem, solved the right way?* Attack the load-bearing assumptions by name;
   if one is false, the work is mis-built no matter how clean the code.
2. **Correctness & quality** — does it do what it claims; is it honest about
   what's done vs stubbed; any overclaim, any silent scope-cut.
3. **Completeness / harvest** — what the work *should* have covered and didn't;
   what already exists that it duplicated or ignored.

## The lifecycle — brief on top, verdict below, one file

Grounded in the `ros`/atelier practice. A review is a **durable artifact**, not a
throwaway chat:

1. **Brief** — before the review runs, write a scoped brief to
   `docs/reviews/<date>-<slug>.md`: what the work is, the three lenses, and the
   **specific assumptions to attack**. Add a `[ ]` pointer in the ROADMAP. The
   brief is *ask on top*.
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
   conflicts). Fixes consolidate onto one ROADMAP follow-ups item; then tick the
   ROADMAP pointer and add a `SESSIONS.md` entry.
5. **Close** — a finding is only closed when its fix is itself verified, with a
   live proof where one exists. "Addressed the review" without exercising the fix
   is the apex violation the review existed to catch.

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
