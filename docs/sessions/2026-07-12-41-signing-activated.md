# 2026-07-12 · session 41 — commit signing activated (Opus)

Mike: "Lets register a signing key — guide me through." The signing doctrine
(SIGNING.md + ADR 0007) had been decided-but-dormant since session 39 and cleared
by the session-40 cold review; the only thing owed was step 1 of the activation
ladder — the principal's act. This session walked steps 1–3 and left 4–5 for a
scoped follow-up.

## The split held: step 1 stayed Mike's, steps 2–3 the agent's

Doctrine puts key generation + GitHub registration on the principal (a new trust
surface on his identity infra, AUTONOMY floor), and it was honoured literally:
Mike ran `ssh-keygen` (passphrase set — the intended posture) and, after a
`gh auth refresh -s admin:ssh_signing_key` scope top-up, `gh ssh-key add --type
signing`. The passphrase never passed through the agent. Registered as key id
`1048805`, type `signing`.

## Step 2 — machine wired, boundary set, proven on both planes

- Canonical **`allowed_signers`** written to atelier root: one entry,
  `namespaces="git",valid-after="20260712"` (quoted — the review's G-fix against
  the "missing start quote" parse failure on macOS ssh-keygen), append-only header.
- Global git config: `gpg.format=ssh`, `user.signingkey`, `commit.gpgsign=true`,
  `tag.gpgsign=true`, `gpg.ssh.allowedSignersFile` → the atelier file.
- **Adoption boundary = atelier `958b1ea`** (the commit that landed
  `allowed_signers` itself). Verification proven on both planes the doctrine
  requires: `git verify-commit` → *Good "git" signature for mike@cxi.nz* (durable <!-- leakscan:allow: author's own git identity in a live verify-commit output quote; same case as the CLAUDE.md convention line (ADR 0005) -->
  plane, against the trust list), and `gh api …commit.verification.verified` →
  `true, reason: valid` (badge plane). Both review traps dodged live — quoted
  timestamp parsed, boundary set *forward* (no history rewrite, ADR 0002 pins
  intact).
- Two operational facts surfaced by driving it, not predicting it: (1) the
  passphrase key must be loaded — `ssh-add --apple-use-keychain` caches it in the
  login keychain so signing runs unattended (SIGNING.md's passphrase-in-agent);
  (2) leakscan blocks `allowed_signers` on its principal email — a false positive
  (the emails are the data the format holds), exempted via a narrow
  `.leakscanignore` glob, same category as the plugin-manifest exemptions.

## Step 3 — the intent baked into new repos

`create-repo`'s git-init block and REPO-STANDARD's new-repo process now both bake
repo-local `commit.gpgsign=true` (belt-and-braces so a new repo signs even where
global config drifted; signing itself stays a machine property).

## shed — the credential remembered (Mike's steer)

Mike's instinct — "shouldn't shed have a script for this?" — was half-right and
sharpened the boundary. **No script:** an SSH signing key is generated locally
and registered once, not minted from a provider root, so shed's mint pattern
(`mint_cloudflare.py`) doesn't apply and a `mint_github.py` would be ceremony.
**But a registry entry, yes:** a distinct `signing_keys` array under shed's
`github` provider now records the key's id, location, and roll story (metadata
only — validate.py green). Two house-consistent calls: the fingerprint is *not*
stored (its 40+ char base64 run trips validate.py; recompute via `gh`/`ssh-keygen`),
and the principal is *referenced* to atelier's `allowed_signers` rather than
duplicated (one-fact-one-home, and it sidesteps leakscan without a scanner hole).
The entry flags the live boundary question: this key's **secret** is person-level
(Apple Passwords), yet the whole fleet **trusts** it as estate provenance infra —
the open "where estate credential governance lives" ADR.

## Left for a scoped follow-up (ladder steps 4–5)

Both gate on Mike's steer, so they weren't ploughed unilaterally:
- **Step 4 — fleet retrofit.** Turn on signing across the 11 children and record
  each adoption boundary (the boundary's home is still the stub: a SHA in each
  child's `floor.yml`). Needs a retrofit order.
- **Step 5 — CI verification step** in the floor workflows: both planes
  (machine-key + `gh api`), `fetch-depth: 0`, trust list at the child's pin, the
  known-signed-fixture selftest. Needs the block-or-warn-first call.
- Vigilant mode left **off** until the fleet is retrofit (else pre-boundary
  history reads "Unverified" everywhere).

SIGNING.md ladder, ROADMAP item, and this log updated to say steps 1–3 live,
4–5 pending — honest done-vs-stubbed per the apex.
