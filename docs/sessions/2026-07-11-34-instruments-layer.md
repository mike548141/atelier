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

## Left open

- The instruments are **untested** (unlike the `tools/` scanners). Test coverage
  is a future item if they grow beyond throwaway — noted in the ADR consequences.
- `ccrepo` needs `ccusage` on `PATH`; `instruments/` introduces a Node runtime
  dependency for that layer (the `tools/` layer stays pure-`python3`) — stated in
  the ADR, not silent.
