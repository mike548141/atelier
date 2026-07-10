# 0002 — the commit SHA is the version

**Status**: accepted • **Date**: 2026-07-10

## Context

Children pin the doctrine version they were last reconciled against
(`PROPAGATION.md`). A pin needs an identifier: something a child `CLAUDE.md`
can carry, a drift check can diff against, and a human can cite. Doctrine
changes are frequent and small (a wording fix is a real doctrine change);
release ceremony per change would either lag the truth or become noise.

## Decision

**The commit SHA is the version.** A child pins `atelier@<SHA>`; the drift
check is `git -C <atelier-path> log --oneline <PIN>..HEAD`; `CHANGELOG.md`
carries one human-readable line per doctrine change as the index. Tags are
reserved for milestones a peer would cite (e.g. a first public release) —
optional, never required for propagation.

## Rejected

- **Semver tags per change:** ceremony on every doctrine edit; the major/minor/
  patch distinction is meaningless for prose doctrine (is a floor change a
  major?); lagging tags would make the pin point at something other than the
  actual truth.
- **Date-based versions:** several changes can land in a day; a date doesn't
  identify a tree state; the SHA already encodes strictly more.
- **No version (children track HEAD):** silent staleness returns — a child has
  no record of what it last reconciled against, so the drift check has no
  anchor and "inspected up to here" can't be expressed.

## Consequences

Zero release overhead; the pin is exact and mechanically diffable. The costs,
accepted: a SHA is opaque to humans (mitigated by the CHANGELOG line), and
pins are meaningful only while history is never rewritten — atelier's `main`
is therefore append-only; a force-push would orphan every child's pin.
