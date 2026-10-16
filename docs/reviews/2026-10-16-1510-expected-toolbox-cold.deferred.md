# Sibling to the expected-toolbox cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-16-1510-expected-toolbox-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-16 UTC by the Opus brief-writer named in the brief's provenance; it
forms no finding. Fold this file in below the reconcile and delete it at phase 2.

## Intent and commissioning records

- Intent record: `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md` —
  **not opened by the brief-writer**.
- Commissioning board items (single grep lines seen, never read whole):
  `320/500` (sessions cannot find installed tools), `320/510` (sessions credited Mike with a
  private tool list), `420/020` (an answer is not a ruling).
- The landing commit's message body (read by the brief-writer): it quotes the principal, says the
  floor change reaches each child when it re-stamps, and records that `320/510` and `420/020` were
  applied in the same change.

## Prior verdicts on these surfaces (named by filename grep, not opened, not exhaustive)

- `docs/reviews/2026-07-10-atelier-foundation.md`
- `docs/reviews/2026-08-02-2210-publish-surface-delta-cold.md`
- `docs/reviews/2026-08-03-0653-publish-surface-application-cold.md`
- `docs/reviews/2026-10-04-2215-pii-by-purpose-cold.md` — same template file, a later commit

## The pointer's own lens hints

None. The pointer is refs-only; its last sub-bullet is the brief-writer's orchestrator's claim.

## Overlap with sibling passes of this batch

No other 2026-10-16 pass touches TOOLBOX, AUTONOMY or the floor region. The template
`docs/build/templates/CLAUDE.md` was also changed by `1ffefc7` (the 2026-10-04 pii-by-purpose
pass's subject), so a runner should read that region at HEAD, not at `55572b1`.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. TOOLBOX's allowlist section argues that publishing what runs unattended turns reconnaissance
   into a plan. The new table publishes the expected tools — including network and security
   tooling and the estate's own CLIs — together with a grant to install any of them unasked. Is
   that the same exposure in a different shape, and does the closing *Bearing* line reconcile it?
2. "When a session finds a tool the list lacks … it updates this list", plus "Listed and missing
   → install it", lets a session list a tool and install it in one commit. Does that collide with
   AUTONOMY's floor that an agent records a grant and never originates one?
3. "Unapproved tool" survives in AUTONOMY's intro and floor, the apex, the floor region, the
   template, the onramp skill and `docs/method/README.md`; TOOLBOX's own opening still says
   "approved". Is "approved" now "listed", and who approves a row?
4. "Upgrading is a routine ask, not a floor stop": AUTONOMY has two classes. Is a third defined
   anywhere a session would find it, and what does an unattended run do with a stale tool?
5. The heading *Two things, kept separate* now introduces two bullets that both say "this doc".
   Did the practice/instance layering survive, or collapse silently into one public instance?
6. The surrounding text turns the quoted "does not necessarily mean paths need to be published"
   into "never a machine's paths, hostnames, accounts or token scopes" — a stronger rule than the
   quote. Whose rule is the stronger one?
7. Several *Get* routes are `.pkg` or vendor installers that need admin rights, but only Homebrew
   is flagged as Mike's to run; user-level pip and global npm routes pull unpinned packages. Does
   "a trusted package manager" cover them?
