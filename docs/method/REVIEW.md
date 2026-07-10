# Review — the enforcement half of the doctrine

*`PROPAGATION.md` names the category error: **a doctrine that is read is not a
doctrine that is complied with.** Documents inform; they do not enforce. This is
what enforces — an **independent review** of the work by a separate, capable
model, before the work is trusted. The build makes the claim; the review is what
earns the right to believe it.*

## Why review, and what the reviewer must be

The building model is the worst-placed judge of its own work: it shares every
blind spot that produced the work, and the apex's honesty burden is hardest to
discharge against oneself. So the check is **external** — and what makes it
bite, in order of what actually carries the weight:

1. **Independence** — a separate agent, fresh context: none of the build's
   momentum, sunk-cost framing, or accumulated assumptions.
2. **Different blind spots** — a *different model* errs differently; two
   failure surfaces overlap less than one.
3. **An adversarial brief** — named load-bearing assumptions to attack, not
   "look this over".
4. **Sufficient capability** — the reviewer must be capable enough to judge the
   class of work (a much weaker reviewer rubber-stamps); for structural or
   irreversible work use the most capable reviewer economics allow
   (`MODEL-ECONOMICS.md`). Capability is a **floor and one axis** — not the
   definition of the practice.

*(Honest reframe, from the 2026-07-10 method-layer review of this very doc: it
originally said "review by a **more capable** model". The house's real economics
are a capable plan-included model **building** and a separate usage-billed model
**reviewing** — the reviewer is not uniformly more capable, and the review works
anyway, because independence, not superiority, is the mechanism.)*

A mechanical gate — validators, CI — still holds the floor for the routine. The
review is not a formality tax on good work; it is the thing that lets "done"
mean *verified* rather than *looks right*.

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
4. **Disposition** — each finding is tagged **[fixed]** (done this session) or
   **[backlog]** (a named ROADMAP slice). Fixes consolidate onto one ROADMAP
   follow-ups item; then tick the ROADMAP pointer and add a `SESSIONS.md` entry.
   The review session may land **small, doctrine-consistent fixes** itself;
   structural rework goes back to a build session as named backlog. If builder
   and reviewer disagree, the conflict is **surfaced to the owner**, never
   silently resolved (the layer-override rule's shape, applied to reviews).
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
