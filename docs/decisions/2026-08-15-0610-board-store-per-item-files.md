# The board store: one file per item, a generated index

**Status**: accepted • **Date**: 2026-08-15

**Review**: queued — the ⏳ pointer in the board's migration item
(`docs/roadmap/010-board-store-migration-per-item-files-mik/`), rule-4 cold
pass on the landing delta.

## Context

Three problems, one root. Mike asked for research on: (a) parallel sessions
corrupting each other's edits to the shared record files; (b) the size of
those files; (c) work reaching `ROADMAP-DONE.md` while still owed. The
research session measured all three (transcript sweep of 566 sessions, the
git history of 968 commits, and the live fleet), then a second pass on a
different model tier re-tested every load-bearing claim adversarially.

What survived the re-test:

- **Read cost was the strongest fact.** `ROADMAP.md` was 4,063 lines
  (~67k tokens), ordered read at every session open, and had grown 13× in
  three weeks. Rotation (`ROADMAP`→`ROADMAP-DONE`, the designed answer) was
  running and losing across the fleet.
- **The concurrency mechanism protects selection, not editing.** The
  claim-on-main design works, but every session then edits one shared file.
  Three recorded incidents were all file-granularity failures — a wholesale
  `git checkout -- docs/ROADMAP.md` destroying a sibling's 21 in-flight lines
  the worst of them. No work was permanently lost; the cost was recovery
  effort and risk.
- **"Done" was asserted in prose, never derived from evidence.** The
  cycle-state residue class: five-plus recorded instances in both directions,
  including a whole duplicated Fable review pass (2026-08-09) run off a stale
  ⏳. Nine of nineteen scanners parse these files, several existing chiefly to
  police drift the store's shape makes possible — `harvestscan` fingerprints
  item bodies by bag-of-words precisely because no item has a stable identity.
- **Over-measured and discounted:** commit-density and transcript-hit figures
  first read as contention evidence turned out to mostly measure the designed
  hygiene working (claim commits, orchestrated waves, reads).

The board's congestion (67 items awaiting Mike's ruling) is a separate,
larger bottleneck no store fixes; the same ruling that accepted this
migration set a weekly ruling sitting for it.

## Decision

Mike's ruling, verbatim (2026-08-15): *"I accept your recommendation.
Proceed"* — accepting the recommendation as put: a weekly ruling sitting,
then **option B — one markdown file per roadmap item, with `ROADMAP.md` kept
as a short auto-rebuilt index**, atelier as the worked example before any
fleet rollout.

The shape as built:

- **`docs/roadmap/<NNN>-<section>/<NNN>-<slug>.md`** — one item per file,
  the existing checkbox grammar verbatim (`[ ]`/`[~]`/`[x]`/`⏳` first line,
  continuations beneath). No frontmatter: a second state vocabulary would be
  one fact in two homes, and every scanner already speaks the checkbox one.
- **`docs/ROADMAP.md` is generated** by `tools/board.py` — a ~250-line index
  of state glyph + linked title + eye-flags. Done items render `✅`, never
  `[x]`, so `sizescan`'s cold-content gate cannot fire on a generated line.
  The index links the board preamble rather than inlining it: one text cannot
  have correct relative links at two depths (found live in this build).
- **`board` is a floor scanner** (hook + CI, enforced): a commit whose index
  is stale against the item files fails with the remedy printed. After a
  merge conflict on the index, rebuilding *is* the resolution. Repos without
  `docs/roadmap/` pass as out-of-scope, said aloud.
- **Provenance replaces assertion.** An item's own `git log` shows which
  commit flipped its state and what work that commit carried. The original
  `closed_by: <sha>` idea was dropped: a commit cannot cite its own SHA, and
  the landing-equals-bookkeeping rule (2026-08-03) requires flip and work in
  one commit.
- **`ROADMAP-DONE.md` is frozen** as the pre-split verbatim archive. A done
  item now stays in its file; the harvest step — and the red-window failure
  mode the one-commit rule existed to close — disappears with it.
- **Claiming is unchanged in shape**: the claim edits the item file's
  checkbox line on `main` before the worktree; a same-item collision still
  fires as a same-line git conflict. Sessions on different items now conflict
  on nothing.
- `harvestscan` watches the board directory (a deletion of an item file whose
  body survives nowhere is the loss it exists to catch — expanded at the OLD
  revision, so a deleted file is enumerated, not skipped). `pointerscan`
  takes item files by directory and skips the generated index.

## Rejected

- **SQLite as the store:** a committed `.db` is binary — git cannot merge it,
  and the claim mechanism depends on same-line collisions git can see. As a
  machine-local primary it breaks the moment a session runs off this machine,
  and the record leaves the repo, which `RECORD.md` forbids. Fine as a
  *derived, gitignored* query cache; never the truth.
- **Append-only event log, state by replay:** the strongest concurrency
  answer on paper, rejected because it optimises the property the re-test
  showed was over-measured, and pays in exactly the human readability the
  estate values most.
- **git-bug (issues as merge-able git objects):** data lives in refs, not
  greppable files, and it puts a third-party tool under the estate's spine.
- **GitHub Issues:** the record leaves the repo (offline-dead, ungreppable at
  session start) and collides with the open ruling on estate-internal context
  in public records.
- **Thin-item discipline in the single file:** the cheap fallback (hard
  per-item line budget, essays exiled). Fixes the read cost, leaves the
  wholesale-revert class and prose-asserted state untouched.

## Consequences

- The session-start read drops from ~4,000 lines to a ~250-line index; item
  detail loads per item, on demand.
- Parallel sessions editing different items cannot conflict; the one shared
  write surface left is the generated index, whose conflicts are resolved
  deterministically by regenerating.
- Sections' programme narrative lives in per-section `README.md` files —
  kept, but items' position *within* that narrative is no longer expressed;
  cross-item prose references ("see below") degrade to section-level. Known
  cost, accepted.
- Item files are ordered by a numeric filename prefix; re-prioritising means
  renaming, which git tracks. Order granularity is advisory.
- The fleet still runs monolithic boards; `board` passes there as
  out-of-scope. Rollout is a queued follow-up, gated on this cycle's review.
- The migration script lives in the session's scratch space by design; the
  artefact under review is the migrated tree itself (verified: linkscan
  clean, harvestscan clean — every pre-split item survives, all 4,063
  original lines accounted for).

## Amended 2026-08-17 — the hook-plane guarantee, said plainly

The Decision above says a commit whose index is stale against the item files
fails. **On CI, unconditionally. At the hook, only when worktree and index
agree** — the hook-plane check reads the worktree, so a rebuilt-but-unstaged
index and a rebuild that absorbed a sibling's dirty item line both pass the
hook and are caught on CI after the push (BS1, the board-store cold pass,
2026-08-15). The principal's ruling 2026-08-17: state the residual on every
surface that asserted the guarantee, and fund the staged-plane check
(board item `010/020`) as the fix; this amendment is the doctrine half.

## Amended 2026-08-23 — the condition restated plainly

The 2026-08-17 amendment's condition — "at the hook, only when worktree and
index agree" — named the state in which the hook *misses*, not the one in
which it catches (BW1, the BS1-wording cold pass; the principal's re-wording,
2026-08-23). Said straight: the hook reads the worktree, so it vouches only
for a commit whose staged board files match the worktree — a rebuild that ran
but was not staged escapes the hook and is caught on CI. The rest of the
amendment, including the funded staged-plane check, stands unchanged.
