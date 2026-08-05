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
**Status** (draft / accepted / revoked `<date>` / superseded by `<file>`),
**Date**, **Context**, **Decision**, **Rejected** (each alternative + why it
lost), **Consequences**. Draft is the only mutable state — deliberation still
open, binding on nothing; acceptance is the principal's call and freezes the
substance. Everything after acceptance is appended, never edited: a dated
**Addendum** section when the decision matures, `revoked <date>` + addendum
when it stops applying with no replacement, `superseded by <file>` when a new
ADR replaces it (the full lifecycle is `method/RECORD.md`).

## Index

- [0001](0001-atelier-is-canonical.md) — atelier holds canonical doctrine; children carry floor + pin + bearings and point up.
- [0002](0002-sha-is-the-version.md) — the commit SHA is the version; CHANGELOG is the index; tags only for milestones.
- [0003](0003-private-first.md) — private-first: one real peer adoption + practice-restructure before any public release.
- [0004](0004-apache-2-licence.md) — Apache-2.0 whole-repo, matching the house standard (ros/faves/rpi).
- [0005](0005-going-public.md) — atelier goes public; the making-public floor is spent, the next deliberate widening is Mike's call.
- [0006](0006-instruments-in-atelier.md) — teammate instruments (ccrepo, cctranscript) live in atelier in their own `instruments/` layer, split from the `tools/` controls.
- [0007](0007-ssh-commit-signing.md) — commit/tag signing via SSH keys fleet-wide (zero-install, dedicated key, tracked `allowed_signers`); artifact signing deferred until a real release exists.
- [0008](0008-enforcement-is-called-not-copied.md) — a child repo *calls* atelier's enforcement floor instead of copying it; non-enforcement must be declared, and conformance is enumerated by `floorfleet`, never assumed.
- [2026-07-13](2026-07-13-coordination-free-record-identifiers.md) — record identifiers are date + slug (+ start time for session logs), never a next-N counter; legacy numbered files keep their names.
- [2026-07-15](2026-07-15-1327-timestamps-utc-at-rest.md) — timestamps are UTC at rest, local + labelled on presentation; record identifiers UTC-forward; foreign data kept as-is with its zone as metadata (ELT). Time's instance of `method/CONVENTIONS.md`.
- [2026-08-05](2026-08-05-1233-estate-internal-context-in-public-records.md) — **draft, ruling owed** — is estate-internal context in a public record accepted transparency or a records-convention defect? Both postures costed against a measurement; P6's funded ADR draft.

*Index drift noted 2026-08-05: five ADRs dated 2026-07-18 → 2026-07-23 are
absent from this index. Recorded in `ROADMAP.md`, not fixed here — writing five
summaries is its own read, not this ADR's scope.*
