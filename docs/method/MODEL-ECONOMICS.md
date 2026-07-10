# Model economics

<!-- TODO: extraction in progress — not yet the canonical copy. -->

> **Status: stub.** The worked policy currently lives in the `ros` repo at
> `docs/MODEL-ECONOMICS.md`.

The general shape, to be extracted here:

- **Match the model to the job.** A capable plan-included model does the
  *building*; a separate, usage-billed model does *review* (code, docs,
  approach, real-world validation) — work is trusted only after that
  independent pass. Reviews are **scoped and short**; builds are the bulk.
- **Know which pool you're spending.** Before token-heavy work, state which
  model you're running as and which billing pool it draws on — because a
  usage-billed model silently doing a *build* is the expensive mistake. Flag it
  before spending.
- **Session hygiene.** Watch context growth; a bloated session wastes the plan.
  Log where you got to and start fresh rather than dragging a huge context.
- **One doctrine, tiered authority — not tiered rules.** Every model runs the
  *same* doctrine (see 00-APEX "who it binds"). What scales with capability is
  **authority over live/irreversible systems**, not which rules apply: match the
  model to the task's *risk* — pattern-following work runs on a cheaper model; a
  mechanical gate (validators/CI) holds the floor regardless of which model ran,
  which is what makes cheap-model work safe; first-of-kind or structural work
  escalates to the capable model, and a smaller model that hits it **logs and
  hands up** rather than improvising.
- **Triggering reviews — inline or batched, the building model's call.** When
  economics allow, the building (Opus) session may **spawn a design/build review
  as a background agent inline** — verify as you go, no context switch (this is
  how the atelier foundation review ran). When they don't, **queue a batch** to
  run together later. Both are sanctioned; pick per cost and how blocking the
  result is. A review is still *scoped and short* either way, and it's still
  spend — so it stays inside the "know which pool" rule.
- **Cost is the lowest precedence** (see PRINCIPLES) — optimised last, never by
  weakening honesty, safety, or correctness.

The estate-specific numbers (which exact models, their pools, the session
overhead figure) stay in `ros` / machine-local — those are this operator's plan
details, not general doctrine.
