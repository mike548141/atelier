# 2026-07-11 · session 39 — the signing doctrine drafted (Fable)

Mike: "Can you draft the signing doctrine" — executing the doctrine half of
session 38's code-signing capture. The drafting was never blocked; only
activation (key registration) is, and the two are now cleanly separated.

## What landed

**`docs/method/SIGNING.md`** — new method doc, listed in the meta section of
`method/README.md` beside RECORD/PROPAGATION (it is provenance *for* the
record). The shape, all from the decided session-38 split, none invented:

- **What a signature honestly claims, stated first** (the apex applied to
  cryptography): machine-key custody + tamper-evidence — *not* "the human
  typed this". Most house commits are agent-authored under the owner's git
  identity and the same machine key signs them; authorship nuance stays in
  the `Co-Authored-By` trailer. Selling the signature as more would be an
  over-claim.
- **Layer 1 (the standard): SSH-native commit/tag signing fleet-wide.**
  Dedicated ed25519 signing key (least-privilege: auth and signing burn
  independently — GitHub allows one key for both; the coupled blast radius is
  why we don't). Machine-global config as the mechanism + create-repo baking
  repo-local `commit.gpgsign=true` as belt-and-braces. **One canonical
  append-only `allowed_signers` tracked in atelier** (public keys are public;
  one-fact-one-home) — the durable verification plane; GitHub's "Verified"
  badge is UI sugar that dies if the key is ever deregistered.
- **Adoption boundary:** history is never rewritten to sign it (append-only
  main, ADR 0002 — a force-push would orphan every child pin). Verification
  gates from each repo's first signed commit; unsigned prior history is a
  stated fact, not a defect.
- **Key handling under SECRETS' scope boundary:** person-level identity
  infra, operator's vault, outside the cheap-burn store — but with *cheap
  loss* (unlike the store master key, nothing becomes unreadable) and cheap
  exposure (revoke + re-mint + `valid-before` the old entry; history stays
  verifiable).
- **Layer 2 (artifact signing + SBOM) stays deferred** with the stated
  trigger: the first real published artifact; GitHub native attestations as
  the lightest route then.
- **Activation ladder:** (1) Mike registers a dedicated signing key — trust
  surface, his act, never the agent's; (2)–(5) agent-executable same-day:
  machine config + `allowed_signers` → create-repo step → fleet retrofit
  with boundaries recorded → CI verify step.

**ADR 0007** (`0007-ssh-commit-signing.md`) — accepted, activation pending.
Rejected and why: GPG (keyring + install, no capability gained),
sigstore/gitsign (OIDC dance + tooling that children and CI would inherit),
no-signing (spoofable identity under load-bearing SHAs), artifact-signing-now
(nothing published exists to sign). Indexed in `decisions/README.md`.

## Judgement calls worth naming

- **ADR marked accepted, not proposed.** The shape was Mike's steer in
  session 38 and "draft the signing doctrine" executes it; what stays his is
  the *activation* (the key — the trust surface), which the ADR and doc gate
  explicitly. If he wants the shape itself re-opened, the ADR is one commit
  old and supersession is cheap.
- **Doctrine written before the practice is live** — flagged inside the doc
  itself ("decided but dormant") per stub-honestly. Grounded in the decided
  split, not fabricated practice; writing it first means the wiring lands
  against a standard.
- **No literal identity strings** in doc or ADR (placeholders only) — the
  house email in `CLAUDE.md` needs a leakscan allow-marker; the doctrine
  shouldn't multiply that exemption.

## Bookkeeping

ROADMAP: code-signing item restructured — doctrine sub-item ticked DONE,
activation ladder now the open sub-item (step 1 Mike), artifact layer
unchanged. CHANGELOG entry added. Review-owed with the standing debt.

## Floor at close

Scanners + full tool suite run locally before commit; see the commit that
carries this entry for the result asserted at the time.
