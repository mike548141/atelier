---
description: Fleet view of child-repo atelier pins — who is stale, by how much, and the commits they'd inspect.
argument-hint: "[--child <repo>] [--log] (optional; default: all discovered children)"
allowed-tools: Bash(python3:*), Bash(git:*)
---

Show which child repos are behind the atelier doctrine SHA they pin, and by how
much. Zero-dependency stdlib Python, bundled in this plugin at
`${CLAUDE_PLUGIN_ROOT}/tools/pins.py` — nothing to install.

**What a pin is** (`PROPAGATION.md`): every child repo carries a doctrine block
stamped with the atelier SHA it was last reconciled against. Doctrine propagates by
**pin bump**, not by editing N copies — so a stale pin is a child that has not yet
picked up a doctrine change. This command is the fleet-wide drift view over those
pins.

Run it against your atelier checkout (the tool defaults `--atelier` to the repo it
lives in — inside the plugin that is the bundled tree; pass `--atelier <path>`
explicitly to point at your **live** atelier checkout when running from the plugin,
so the SHAs compare against real history). Pass `$ARGUMENTS` through:

- **default** — discover children under atelier's parent dir and report each one's
  pin status (current / stale, and by how many commits):
  `python3 "${CLAUDE_PLUGIN_ROOT}/tools/pins.py" [--atelier <live-atelier>]`
- **`--child <repo>`** — report only that child (repeatable; bypasses discovery).
- **`--log`** — also print the commits each stale child would need to inspect.
- **`--check`** — exit 1 if any child is stale (for CI / hooks).

Then report: which children are current, which are stale and by how much, and — for
a stale child — that reconciling it is a **pin bump** (re-stamp the block at the new
SHA after reviewing the intervening doctrine commits), not a blind edit. Don't
recommend bumping a pin you haven't shown the intervening commits for.
