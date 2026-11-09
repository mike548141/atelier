# Decision records

<!-- indexscan:maps dir=. match=*.md exclude=template.md -->

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
ADR replaces it (the full lifecycle is `method/RECORD.md`). An addendum that
states a live state of the world dates it "as of <date>" — never "at HEAD",
which a later reader takes to mean their HEAD — and carries the read beside
the claim (AR1, AR5).

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
- [2026-07-18](2026-07-18-0820-review-the-design-not-only-the-build.md) — review applies to design and direction as much as to a diff — the earliest review is the cheapest, and every durable design record must carry a `review:` line or an explicit "not warranted" judgement so a decline is visible, not silent.
- [2026-07-19](2026-07-19-0100-review-trigger-is-commitment-not-artefact.md) — the review trigger is re-keyed on commitment ("what will come to rest on this") rather than artefact shape, fixing the framing upstream in `REVIEW.md` and converting the drifted child-template reviews README (`docs/build/templates/docs/reviews/README.md`) from a silent fork into a pointer.
- [2026-07-21-0744](2026-07-21-0744-review-line-artefact.md) — the `review:` line becomes an artefact, not just a convention — the ADR template and decisions README gain the field, and `tools/reviewscan.py` reds a decision record dated after 2026-07-21 that omits it; records frozen before that date are blameless.
- [2026-07-21-0748](2026-07-21-0748-deinstance-create-repo-for-the-plugin.md) — `create-repo` is de-instanced for the plugin: the house-identity facts it stamps move into an adopter-owned `~/.atelier/instance.yaml`, filled on first run, with doctrine sourced live (SHA-pinned) or bundled (plugin-version-pinned) depending on what the adopter has installed.
- [2026-07-23](2026-07-23-0001-billing-state-of-the-marginal-token.md) — billing state (plan-included / capped / usage-billed) belongs to the marginal token, not the model — risk still assigns which tier builds vs reviews, a plan cap is a stop-or-pay boundary never a down-tier trigger, and a model past its depth fails noisily up the ladder rather than silently degrading.
- [2026-08-05](2026-08-05-1233-estate-internal-context-in-public-records.md) — in a public record a private repo's internal state is described by its type only (posture C, decided 2026-11-08); naming it in any other context stays allowed; forward only.
- [2026-08-15-0610](2026-08-15-0610-board-store-per-item-files.md) — the board store is one markdown file per roadmap item under `docs/roadmap/`, with `ROADMAP.md` a short index generated by `tools/board.py` and gated by the `board` floor check; atelier is the worked example before any fleet rollout.
- [2026-10-03-0641](2026-10-03-0641-the-exception-register.md) — **draft, reworked 2026-11-09 to one central file on Mike's answers; re-review and ruling owed** — one append-only register file per repo replaces inline markers, ignore-file lines and binary-manifest lines; each entry records why, who (short session ID; ruled, answered, agent or unrecorded), when, and is narrowed down to one string by digest and count; old and new forms both work until a ruled retirement, so no child goes red; replaces `GUARDS.md`'s git-supplies-who-and-when.
- [2026-11-09](2026-11-09-board-states-design.md) — **proposed, review and ruling owed** — board items get two state tiers: a live-or-closed box plus a required word on closed-not-delivered items, so the tick means done; `[/]` part-delivered splits `[~]`, a parent carries a counted roll-up, and waiting is a field, never a state; additive, so no child goes red.
