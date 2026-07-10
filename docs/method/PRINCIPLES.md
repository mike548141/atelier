# Design principles

<!-- TODO: extraction in progress — not yet the canonical copy. -->

> **Status: stub.** The canonical, fully-worked design doctrine currently lives
> in the `ros` repo at `docs/PRINCIPLES.md` — the design principles (resilience,
> structure, events-over-polling, stateless/async, security/privacy/cost by
> design, legibility, reproducibility), the **precedence ladder** that resolves
> collisions between them, and the **situation tests** (each grounded in a real
> decided case). The apex above all of it — honesty absolute, then the Laws — is
> already extracted here as [`00-APEX.md`](00-APEX.md).

What's owed here is the **general spine**: the named principles + the precedence
order + the situation tests, lifted out of their RouterOS/tiki examples so they
read as estate-wide doctrine. The tiki-specific *bearings* and the review
*case-law* stay in `ros` — they're the same ideas applied to one product, not
the general statement.

Deliberately a stub rather than a blind copy: copying the ros doc verbatim would
drag tiki specifics into a shareable repo and create a second source of truth to
diverge (a DRY violation the principles themselves forbid). Extraction is a
ROADMAP item.
