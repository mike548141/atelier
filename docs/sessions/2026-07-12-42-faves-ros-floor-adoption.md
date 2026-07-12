# 2026-07-12 · faves + ros adopt the house floor (Fable)

**Ask:** the open follow-up from session 41 — faves and ros run bespoke
`ci.yml`, never adopted `floor.yml`, so the fleet signing retrofit skipped
their verification. Mike weighed full adoption vs injecting signing steps into
their bespoke CI, and chose **full adoption**.

**Outcome: both floors green on first run, verification verifying.** Current
template landed beside each repo's bespoke `ci.yml` (floor gates
publish-safety; their `ci.yml` keeps gating correctness). Two-plane signature
verification ran for real — faves 9/9 good, ros 2/2 good, zero warnings.

## What the pass actually took (the honest part)

- **Both pins predated `allowed_signers`** — adopted as-was, the floor would
  have gone green while *silently skipping* signature verification (the
  trust-list step warns and exits 0 on an old pin). The pin bump to a
  trust-resolving SHA was load-bearing, not hygiene.
- **ros wasn't signing its HEAD.** Its newest commit predated the global
  signing flip and sat unpushed — amend-signed (local-only, no published
  history moved) rather than carving the boundary around it. Boundaries:
  each repo's true last unsigned commit.
- **Green-by-charter, not green-by-scrub.** Unlike the three children left
  red on genuine scanner debt, these repos' findings were their *content*:
  a listings site's addresses/phones/coordinates; a network-inventory repo's
  ipv4/ipv6/mac shapes on nearly every line (leakscan `--disable`'s own
  documented example). Encoded via the designed hatches — repo-type
  `--disable` in each floor's leakscan step (commented in place), reasoned
  ignore globs for chartered content, inline allow-markers for a handful of
  shape false positives (cert names phone-shaped, a QR finder ratio
  ipv6-shaped, well-known DNS/loopback literals). Every ros exemption states
  it does **not** survive the publish-time scrub-and-fresh-export pass.
- **Working tree ≠ CI tree.** The bulk of the local findings (hundreds of
  thousands) sat in *gitignored* dirs CI never sees — the
  CI-parity pre-run was done against the tracked tree (`checkout-index`)
  before concluding anything. Local full-term leakscan cover stays on the
  pre-commit hooks, which both repos have wired.
- **Riders:** licenscan enabled in both (settled Apache-2.0 — the template's
  stated trigger), with an in-file caveat in ros that a green licence check
  is not publish-readiness there. Four real broken links fixed (sibling-path
  doctrine links → atelier's public GitHub URLs; two `LICENSE` links that
  404'd from a subdir).

**Fleet state:** all floor children now verify signatures; warn→block flip
(separate ROADMAP item) still waits on the three debt-red children and
Mike's call.
