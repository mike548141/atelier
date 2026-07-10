# Toolbox — know what's available, don't rediscover it

Every session that has to re-learn "is ripgrep here? where's the venv? is `gh`
authenticated?" spends attention on something already known. The fix is a
**tool manifest**: a maintained record of the capabilities available and
approved, so the agent starts each session knowing its toolbox instead of
probing for it.

## Two things, kept separate

This is atelier's layering applied to tools:

- **The practice (shareable — this doc).** *Keep a manifest. Record approved
  tools and how to install them. An approved-but-missing tool may be installed;
  an unapproved one is confirmed first. Keep the manifest current.*
- **The instance (personal — NOT in this repo).** The actual list of *this
  operator's* tools — accounts, credentials scopes, venv paths, connected
  services (mail, calendar, finance, drive) — is personal/estate context. It
  lives machine-local (`~/.claude/`), never in a shareable repo. Naming a
  colleague's connected mail account in a doc you hand them is exactly the leak
  atelier exists to prevent.

## What the manifest records, per tool

- **Name + what it's for** — one line.
- **Status** — installed / approved-not-installed / needs-approval.
- **How to get it** — the install command, so "approved-not-installed" is a
  one-step fix.
- **Any auth/scope** — *machine-local manifest only* (e.g. which account a CLI is
  authenticated as, what a token can reach). Never in the shareable layer.

## The install rule (ties to AUTONOMY)

- **Approved but not installed → proceed.** Installing a pre-approved tool from a
  trusted package manager is reversible (uninstall) and already sanctioned — it
  falls under "reversible and local" in `AUTONOMY.md`. Install it, use it,
  record it in the manifest.
- **Not on the approved list → confirm first.** New tooling is a new capability
  and a new trust surface; that's the owner's call.
- **After installing or first-using a tool, update the manifest** — so the next
  session inherits the knowledge (one source of truth; a rediscovery later is a
  manifest gap to close, not a fact to re-derive).

## The command allowlist is part of this

A repo's committed `.claude/settings.json` allowlist is the machine-checkable
half of the manifest for *shell commands* — the commands the agent may run
unprompted. It's the "approved" column for the command layer. The manifest in
this doctrine sits one level up: it also covers higher-level tools and connected
services that aren't single shell commands, and it says how to acquire the ones
that are approved but absent.

*Bearing: the concrete instance for this estate is captured machine-local (the
digital-estate map + the per-repo allowlists already record most of it); this
doctrine is the shape that keeps it current and makes it portable to a peer
without carrying the personal inventory with it.*
