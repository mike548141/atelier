**2026-07-10 (Opus) — parallel-work tooling: `worktree.py`.** Session-start drift
check fired: atelier had moved 4 commits past ros's pin (957fa08) — the leakscan
build from the prior session, not doctrine drift; noted, pin bump left to a ros
session. Review gate holds (method/ Fable review still un-run) so extraction stays
blocked; picked the un-gated, Mike-requested line instead. Built
`tools/worktree.py` — the one-command delivery of `method/CONCURRENCY.md`'s
worktree-per-line (`start`/`list`/`land`/`remove`). The doctrine's rules are baked
in as guards, not left to memory: refuses an iCloud base (a live `.git` index
corrupts under sync — the #1 forgotten rule), branches off the integration branch
so a new line never inherits a half-done branch, `list` flags stale (merge-hazard)
and dirty (leaked-file-handle) trees, and `remove` refuses to delete uncommitted
or unmerged work without `--force`. Zero-dep, `--json` on every command, fail-safe
exit codes, `--selftest`; 12 stdlib tests over real throwaway repos + a live
start→list→remove round-trip on atelier itself (main working tree left untouched).
leakscan-clean, README + CHANGELOG + ROADMAP in lockstep. **Meta:** mid-build Mike
asked whether he could open a *second* atelier session in parallel — so he was
handed the exact worktree recipe (`git worktree add ~/worktrees/atelier-method-review`)
and a kickoff prompt to run the gated method/ Fable review as an independent
line. The doctrine this tool encodes, used to structure the very session that
built it.
