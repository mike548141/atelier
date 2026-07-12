# 0006 — Teammate instruments live in atelier, in their own `instruments/` layer

**Status**: accepted • **Date**: 2026-07-11

## Context

Two small CLIs were built to support working with Claude: `ccrepo` (per-repo
token/cost totals — a DevFinOps view of what the collaboration costs) and
`cctranscript` (a timestamped transcript of a session — observability of when
Claude or the principal did something). They were first dropped into the private
`homenetwork` infra repo next to unrelated machine config, because that's where
an earlier one-off (`ccrepo`) had landed.

That placement was expedient, not reasoned. The real question surfaced: do these
belong in atelier? atelier's stated purpose is *the operating model for working
with Claude as a teammate*. Both instruments have **no value outside that
relationship** — they read Claude Code's own session logs to cost and observe the
work. By purpose they are atelier material, not home-infra material.

The counter-objection was that atelier is doctrine-only and adding runnable tools
expands its scope. But atelier already ships executable tools (`tools/` — the
Python control-scanners) and a skill (`create-repo`). It is already a repo that
ships instruments, not only prose. So the scope objection doesn't hold; what's
needed is to draw the boundary deliberately.

## Decision

Move both instruments into atelier, in a **new top-level `instruments/` layer**
distinct from `tools/`:

- **`tools/` enforces** — Python, zero-dep, hook/CI-wired checks that gate a
  commit (leakscan, secretscan, licenscan, linkscan, worktree, pins).
- **`instruments/` observes** — Node, user-invoked CLIs that cost and observe the
  collaboration itself (ccrepo = DevFinOps, cctranscript = observability).

The membership rule is **purpose, not runtime**: an instrument belongs here only
if its value *is* the Claude teammateship — costing it, observing it, steering it.
General machine/infra utilities (macOS, TrueNAS, networking) that the principal or
Claude merely *use* stay with the estate they serve (`homenetwork` et al.).

Install stays as it already worked: a per-tool symlink into `~/.local/bin` via an
idempotent `instruments/install`, not the folder on `PATH`.

## Rejected

- **Leave them in `homenetwork`:** keeps the pair together and private, but files
  them by accident of where the first one landed, not by what they are. Their
  whole reason to exist is the Claude relationship — the operating-model repo is
  their honest home. Private-vs-public isn't the deciding axis: the code carries
  no personal data (paths are derived at runtime), so publishing them is safe.
- **Put them inside `tools/`:** one dir, matches "atelier already has a tools
  folder". Rejected because `tools/`'s charter is explicit — *"Doctrine informs; a
  check enforces. These are the checks."* These aren't checks and aren't Python;
  folding them in blurs a sharp, load-bearing framing (the enforcement floor) with
  a different species (interactive observability). A clean second layer keeps both
  honest.
- **A dedicated public micro-repo (`cc-tools`):** over-fragments for two scripts
  and re-poses the same "where does this belong" question. atelier is the answer.

## Consequences

- atelier now has a first-class `instruments/` layer; the README structure table
  and this ADR record the tools/instruments split. Future teammate-support tools
  land here by the purpose rule; infra tools are explicitly out.
- atelier gains a **Node** runtime dependency for this layer (the `tools/` layer
  stays pure-`python3`). Stated, not silent.
- Publishing: the instruments enter the public repo. Verified clean of personal
  data before the move (no hardcoded paths/names; logs read at runtime). The
  leakscan/secretscan pre-commit gate covers every commit as usual.
- They leave `homenetwork` entirely — no duplicate, no stale copy. The
  `~/.local/bin` symlinks re-point to atelier; `homenetwork/bin/` is removed.
- The instruments are currently untested (unlike the `tools/` scanners). Test
  coverage for them is a future item if they grow beyond throwaway.

## Addendum (2026-07-12) — the layer admits *capability* tools, not only observers

**Decision (Mike):** `instruments/` widens to admit **capability tools** — ones
that extend what the teammate can *do* — where their value is wholly the
working-together relationship. The membership rule is unchanged (purpose, not
runtime); what widens is the *kind* of value that counts: not just **observing**
the collaboration (ccrepo, cctranscript) but **extending its reach**.

Prompted by adopting **`browser-fetch`** (Mike, 2026-07-12): an MCP server that
drives Chrome so the teammate can get through when `WebFetch`/curl are blocked
(and so the operator can help clear a captcha the agent can't). It passes the
purpose test squarely — it exists only for the teammateship — but it breaks
every prior *sub-norm* of the layer, and those norms are now understood as
descriptive of the first two instruments, not constitutive of the layer:

- **acts, not observes** — the layer is now three verbs: `tools/` enforce,
  observer instruments (ccrepo/cctranscript) observe, capability instruments
  (browser-fetch) extend reach.
- **Python + dependencies, not zero-dep Node** — a browser tool cannot be
  zero-dep. The zero-dep ethos holds where it can (`tools/`) but **flexes for
  capability tools whose value requires deps**; the price is paid honestly —
  deps pinned (`requirements.txt`) and constrained (`constraints.txt`), the
  runtime a regenerable venv outside the repo, the code versioned in-repo.
- **an MCP server, not a `~/.local/bin` CLI** — it installs via its own `setup`
  (build the venv, print the `~/.claude.json` registration), not the shared
  symlink `install`.

**Boundary still holds:** a *general* browser-automation utility Claude merely
uses would be estate/infra, not an instrument. browser-fetch qualifies because
it is built for, and only makes sense within, the Claude teammateship.

**Consequences:** the `instruments/` charter is "value is the teammateship",
observing **or** extending it. CI does not unit-test a browser (disproportionate);
the floor scanners still cover its source, and it is verified by live use — the
same honest-scope stance the scanners take. Pre-public scrub done (the
`Mike`/machine specifics and pre-SDK history removed before the code entered the
public repo).
