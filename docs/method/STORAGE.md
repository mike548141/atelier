# Storage & backup — where the work lives and how it survives

A project is worth more than the laptop it sits on. Every repo is arranged so
that losing any one location loses nothing.

*(The specific services below — a home NAS, Apple Time Machine — are this
estate's worked example. A peer substitutes their own: the doctrine is the
**roles**, not the Apple-shaped instances that fill them.)*

## Three locations, four jobs

| Location | Role | Property it provides |
|---|---|---|
| **Laptop working copy** (`~/.pets/`) | where the work happens | offline access — no internet required to keep working; a plain local path no sync engine touches |
| **GitHub** | master / source of truth + device portability | versioned history with metadata, the shareable origin peers pull from, and clone-anywhere recovery if the laptop dies |
| **Time Machine → local NAS** | full-machine backup | device-level restore of the *whole machine* — config, tools, and work not yet pushed |

The repos lived *inside* iCloud Drive until 2026-07-14 — the sync engine
filled the continuous-backup role for free, but it also evicted file
contents under machinery (venvs, editable installs, whole-tree scanners,
pre-commit hooks timing out), and each symptom bred a workaround. The
estate retired that leg: the working copy moved to a plain local path,
and the continuous-backup role split across **push discipline** (small,
frequent pushes — the offsite leg) and **Time Machine** (everything
else). The trade-off is named, not hidden: between a push and the next
Time Machine snapshot, new work exists in exactly one place.

Two *different* classes of protection, not redundancy: git protects the
**project files** (and alone carries history + provenance); Time Machine
protects the **whole machine state** — the tools, config, and any work that
hasn't been committed or pushed yet. The first gets a project back; the second
gets a *machine* back. macOS devices back up to a local NAS acting as a Time
Machine target in addition to the per-project protection above.

## The rule

- **GitHub is the source of truth** for anything shared or released. Where a
  public and a private edition both exist, the published repo is canonical for
  the package; the private repo re-exports into it, never merges history back.
- **A sync copy is protection, not truth.** If a sync service (iCloud,
  Dropbox) holds any copy of a repo, never resolve a conflict by trusting the
  sync copy over git — git history wins.
- **Push early, push often.** With no sync engine mirroring the working copy,
  the push *is* the offsite backup. Unpushed work is the only work at risk.
- **The laptop is disposable.** The acid test: if this machine vanished right
  now, could the project be rebuilt from GitHub + the secret store + the last
  Time Machine snapshot alone? If not, that gap is a defect to close, not a
  risk to carry.

## The one gotcha: never let a sync engine hold the working copy

This estate learned it the hard way: sync services (iCloud Drive, Dropbox)
evict file contents and serve stale reads under tooling that touches many
files fast. If a working copy must live in a synced folder anyway:

- **Virtual environments live *outside* the synced folder** (e.g.
  `~/.venvs/<project>/`). An in-repo `.venv/` gets evicted/half-synced and
  breaks intermittently. *(Learned the hard way on the tiki venv; moot for
  this estate since the 2026-07-14 move — in-repo `.venv` is now the norm.)*
- **Build/cache dirs** (`__pycache__/`, `.pytest_cache/`, `dist/`, `build/`,
  `node_modules/`) are gitignored and best regenerated locally — they're churn,
  not content.
- **Throwaway git worktrees go outside it** too (see CONCURRENCY) — they'd
  otherwise generate sync churn for no benefit.

## Secrets are a thing apart

Secrets are neither backed up casually nor committed in plaintext. They follow
their own regeneration doctrine: prefer *re-mint from code* over *hand-keep an
irreplaceable token*, and store at rest encrypted (e.g. sops + age), with the
encrypted form safe to commit and the plaintext gitignored. Losing the secret
store should mean "regenerate", not "lost forever".
