- [x] **Mechanical leak-scan** — built 2026-07-10 as `tools/leakscan.py`
      (+ README, `pre-commit.sample`, `leakscan-terms.example.txt`, unittest).
      Shareable structural patterns (always run) + machine-local literal-term
      list (`~/.claude/leakscan-terms.txt`, never in a repo); graceful
      degradation to structural-only with a loud warning; `--staged` hot path,
      `--json`, fail-safe exit codes; `.leakscanignore` + `leakscan:allow`
      escape hatches; `--disable <rules>` + `--staged <subtree>` for networking
      repos / private-repo-with-shareable-subtree. Proven: caught real address/
      coordinate/name leaks in its own first-draft fixtures; **local term list
      SEEDED** in `~/.claude/`; **hooks INSTALLED** (atelier whole-repo; ros
      `tiki/`-scoped with network-shape rules off) and block/pass proven live.
      Full-cover scan validated the earlier tiki scrub — 1 residue (the intended
      OSS author name in `pyproject.toml`, allow-marked) out of 738 raw hits.
      **Owed:** CI wiring (a hook only guards the machine it's on); portability
      of the term list to Mike's other devices (north-star); extend patterns as
      gaps appear. Reviewed 2026-07-10 (batch review — B4 renamed-file staged
      hole fixed + proven live, B5 `--require-terms` fail-closed flag for
      hooks/CI, B7 residual false-negative surface now stated in tools/README).
