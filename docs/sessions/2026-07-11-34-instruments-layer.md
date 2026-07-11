# 2026-07-11 · instruments/ layer — ccrepo & cctranscript move into atelier (Opus)

Started as a plain how-to ("can I see timestamps on VS Code messages?") and
ended in a doctrine decision. The answer to the question: the chat UI shows no
timestamps, but every message is timestamped in the session `.jsonl` under
`~/.claude/projects/`. So a small tool was built — `cctranscript` — to render a
timestamped transcript (prompts + replies, elapsed deltas, `--full` for
thinking/tools, `--json`), sibling to the existing `ccrepo` (per-repo token/cost
totals). Both are zero-dep Node CLIs reading the logs read-only.

## The real decision: where do these belong (ADR 0006)

They first landed in `homenetwork/bin` — by accident of where the earlier
one-off `ccrepo` sat, not by reasoning. Mike pushed on it: both tools have **no
value outside working with Claude as a teammate** — `ccrepo` is the DevFinOps
view of what the collaboration *costs*, `cctranscript` is *observability* of
what happened when. That is atelier's stated purpose, so atelier is their honest
home. The scope objection (atelier is doctrine-only) doesn't hold: atelier
already ships `tools/` and the `create-repo` skill.

Placement fork, put to Mike, he chose the clean split: a **new top-level
`instruments/` layer**, distinct from `tools/`. The line is drawn by *purpose*:

- **`tools/` enforces** — Python, zero-dep, hook/CI-wired *checks* that gate a
  commit. Its README framing is explicit ("these are the checks"); folding
  interactive Node observability in would blur a load-bearing distinction.
- **`instruments/` observes** — Node, user-invoked CLIs that cost/observe the
  collaboration itself.

Membership rule (recorded in the ADR and `instruments/README.md`): an instrument
belongs only if its value *is* the teammateship. General infra utilities (macOS,
TrueNAS, networking) the principal or Claude merely *use* stay with the estate
they serve — they do **not** come to atelier.

## What shipped

- `instruments/{ccrepo,cctranscript,install,README.md}`; `install` is the
  idempotent per-tool symlink-into-`~/.local/bin` installer (folder isn't on
  `PATH` — that mechanism was undocumented before and is why a newly-added tool
  silently wasn't found; now scripted).
- `docs/decisions/0006-instruments-in-atelier.md` (accepted); decisions index
  updated — and it was also **missing 0005**, now added.
- README structure table gains the `instruments/` row.
- Verified before commit: leakscan / secretscan / linkscan all clean on the new
  files (code carries no personal data — paths derived at runtime, so publishing
  into the public repo is safe). Symlinks re-pointed homenetwork→atelier and both
  smoke-tested from the new location.
- `homenetwork/bin/` removed entirely (no duplicate, no stale copy); that repo's
  commit points here.

## Process note (the meta-lesson, saved to memory)

Two corrections happened live and both trace to one root: I assumed how a thing
was wired instead of checking. First I wrote PATH-export install docs when the
working sibling (`ccrepo`) actually used a `~/.local/bin` symlink; then I
mischaracterised atelier as doctrine-only when it already ships tools. Memory
`verify-sibling-wiring-before-documenting` now captures: trace the working
precedent (`which` → `ls -l`, read the actual config) before documenting or
assuming by analogy.

## Housekeeping — parallel-session loose ends audited and closed

Mike asked for a sweep of anything left open by past parallel sessions (PRs,
branches, worktrees) across the estate. Findings and closures:

- **nova `tidy-up`** — initially misreported this session as "unpushed, at
  risk" (a `rev-list --left-right` read inverted; the memory lesson bit its
  author within the hour). Truth: merged into nova main *and* pushed; pure
  stale branch. Deleted local + remote.
- **atelier `gate-calibration`** — merged via PR #2 (`4b2cf6f`), 0 commits
  outside main; branch lingered only because the repo doesn't auto-delete on
  merge. Remote branch deleted.
- **atelier `atelier-method-review`** — the recurring one, now closed for
  good. PR #1 was closed-not-merged; the branch held 2 commits main lacks.
  Mechanical comparison (per-file branch-vs-main line sweep, then whole-tree
  grep for branch-only lines) showed it is the *same* session-08 method-layer
  review rendered twice: branch `8407b37` per-question (Q1–Q12), main
  `6fd64ba` per-lens with the [fixed] dispositions — main's is operative.
  Then found a past session had already salvaged the real residue: tag
  **`archive/2026-07-10-method-review-parallel-verdict`** (same tip,
  `3bfcbbc`) records "E3 salvaged to main in `48fa5ff`; P2/PR2 consciously
  not carried". That session archived but didn't delete — which is exactly
  why the branch kept resurfacing. The branch is now **deleted**; the
  archive tag keeps every commit reachable forever. (A duplicate tag this
  session minted before spotting the original was removed — one archive, one
  name.) Pattern worth keeping: **branches are for active work; archive tags
  are for closed-not-merged history — salvage, tag, delete, record.**
- **atelier PR #3 (`plugin-bundle`)** — open *by design* (merge = go-live,
  Mike's call). Untouched.

Mike then asked the right follow-on: how do we stop this repeating? Root cause
named: "branch exists" had been allowed to mean both *open work* and *closed
work nobody finished putting away*, so every session re-derived which. Fix in
the house's three layers: **doctrine** — CONCURRENCY gains "Every branch ends
put away" (landed→deleted, or salvage→tag→delete→record; both end with the
branch gone; review-owed, flagged); **mechanism** — delete-branch-on-merge
flipped ON across all 8 active repos (atelier, nova, numen, faves, ros,
homenetwork, docker-heap, rpi), killing the merged-branch-lingers class at the
source; **inheritance** — ROADMAP backlog: create-repo's `gh repo create` step
sets the flag so future repos are born with it.

## Left open

- The instruments are **untested** (unlike the `tools/` scanners). Test coverage
  is a future item if they grow beyond throwaway — noted in the ADR consequences.
- `ccrepo` needs `ccusage` on `PATH`; `instruments/` introduces a Node runtime
  dependency for that layer (the `tools/` layer stays pure-`python3`) — stated in
  the ADR, not silent.
