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
- **Cost is the lowest precedence** (see PRINCIPLES) — optimised last, never by
  weakening honesty, safety, or correctness.

The estate-specific numbers (which exact models, their pools, the session
overhead figure) stay in `ros` / machine-local — those are this operator's plan
details, not general doctrine.
