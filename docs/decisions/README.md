# Decision records

Short ADRs preserving the *deliberation* behind significant decisions —
the alternatives weighed, why they lost, and the evidence — which
`ARCHITECTURE.md` (current truth, compact) deliberately compresses away.

Write one when a decision (a) rejected a plausible alternative a future
session might re-propose, or (b) rests on evidence that took real work to
gather. Don't write one for reversible implementation choices — a code
comment covers those (the "comments say why" rule).

Format: one file, `<YYYY-MM-DD>-<HHMM>-<slug>.md` (start time, 24-hour —
coordination-free, per `method/CONCURRENCY.md`'s record-identifier rule; files
named under retired schemes keep their names), about half a page. Sections:
**Status** (accepted / superseded by `<file>`), **Date**, **Context**,
**Decision**, **Rejected** (each alternative + why it lost), **Consequences**.
Never edit an accepted ADR's substance — supersede it with a new one.

## Index

- [0001](0001-atelier-is-canonical.md) — atelier holds canonical doctrine; children carry floor + pin + bearings and point up.
- [0002](0002-sha-is-the-version.md) — the commit SHA is the version; CHANGELOG is the index; tags only for milestones.
- [0003](0003-private-first.md) — private-first: one real peer adoption + practice-restructure before any public release.
- [0004](0004-apache-2-licence.md) — Apache-2.0 whole-repo, matching the house standard (ros/faves/rpi).
- [0005](0005-going-public.md) — atelier goes public; the making-public floor is spent, the next deliberate widening is Mike's call.
- [0006](0006-instruments-in-atelier.md) — teammate instruments (ccrepo, cctranscript) live in atelier in their own `instruments/` layer, split from the `tools/` controls.
- [0007](0007-ssh-commit-signing.md) — commit/tag signing via SSH keys fleet-wide (zero-install, dedicated key, tracked `allowed_signers`); artifact signing deferred until a real release exists.
- [2026-07-13](2026-07-13-coordination-free-record-identifiers.md) — record identifiers are date + slug (+ start time for session logs), never a next-N counter; legacy numbered files keep their names.
