# Review brief — v2-plugin de-instance build + ADR (rule-4 cold pass)

- **Date/time:** 2026-07-22 1215 UTC
- **Reviewer:** fresh-context subagent (two-hop spawn — see provenance).
- **Subject:** the single commit `1516ae1` on branch `v2-plugin-deinstance`
  (checked out read-only at `/Users/mike/worktrees/atelier-v2-plugin-deinstance`):
  `skills/create-repo/SKILL.md` (new, relocated into the bundle),
  `skills/create-repo/instance.yaml.example`, `commands/worktree.md`,
  `commands/fleet-pins.md`, `skills/session-onramp/SKILL.md` wiring,
  `.claude-plugin/plugin.json` + `marketplace.json` (0.1.0→0.2.0),
  `CHANGELOG.md`, and
  `docs/decisions/2026-07-21-0748-deinstance-create-repo-for-the-plugin.md`
  — the queued pointer directs ADR + build reviewed **as one**.
- **Composition check in scope:** the delta was cut from `4da0340`
  (2026-07-21); `main` has moved ~130 commits since. Whether the delta still
  composes with current `main` (naming, cross-references, doctrine it cites)
  is part of the subject, not an aside.
- **Intent record:** the branch's `docs/SESSIONS.md` index entry and
  `docs/ROADMAP.md` delta — **deferred material**, not opened before the
  reviewer's findings are committed (REVIEW.md rules 1–2). No prior review of
  this delta exists.

## Spawn provenance (REVIEW.md rule 4)

The principal opened this orchestrating session and pointed it at the queue —
the worked example rule 4 names. The delta's authoring session (2026-07-21,
recorded in the commit) neither started nor instructed this session; this
taker authored none of the delta. QR1's chain-spawn caution checked on the
criterion itself: started-or-instructed, not authorship. **Exposure, named:**
the taker read the delta's commit message (an evaluative account) and the
1018 run's closing note on the stray worktree during its onramp. So the
review runs **two-hop** (the 2026-07-21 2208 precedent): this brief is
refs-only above the divider, and a **fresh-context subagent** is the
reviewer; its prompt carries refs only. The reviewer names its own attack
surface first; the deferred material and all session records stay closed to
it until its findings are durably committed.

## Status of the work

Self-authored doctrine (doctrine by function — the skill stamps behaviour
into other repos; the ADR forks ADR 0002 for plugin-only adopters).
**Findings are Mike's to decide** (REVIEW.md rule 3); nothing is applied by
this review; each finding carries plain-language what/why/likely-impact.

## Scope

Widest the work admits: the de-instancing design and its assumptions; the
ADR as doctrine; the skill wording future adopter sessions will obey; the
two commands as behaviour-stamping surfaces; consistency with sibling
doctrine at **current main** (PROPAGATION stamped-copy discipline, ADR 0002,
ECONOMICS, CONCURRENCY, REVIEW); manifest/version hygiene; the mechanical
floor re-run on the branch. No non-goals declared; nothing fenced off.

## Lenses

All four REVIEW.md lenses, both altitudes. Lens 4: the file class is
markdown/JSON config — if `/security-review` is definitionally empty here,
discharge on those grounds and weigh it as nothing; the manual lens-4 pass
still runs (an adopter-profile that stamps identity has real design-altitude
surface: what travels in a public bundle, what stays adopter-local).

---

## Deferred — reviewer opens only after its findings are committed

- Intent record: `docs/decisions/2026-07-21-0748-deinstance-create-repo-for-the-plugin.md`
  §context (the ADR's normative text is subject; its narrative context is the
  author's account), the branch's `docs/SESSIONS.md` entry, and the branch's
  `docs/ROADMAP.md` delta.
- The author's commit message for `1516ae1`.
- No seeded questions: the taker defers none (it has read only the material
  named above and declines to relay it).
