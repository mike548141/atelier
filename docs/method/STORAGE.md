# Storage & backup — where the work lives and how it survives

A project is worth more than the laptop it sits on. Every repo is arranged so
that losing any one location loses nothing.

## Three locations, three jobs

| Location | Role | Property it provides |
|---|---|---|
| **Laptop working copy** | where the work happens | offline access — no internet required to keep working |
| **iCloud Drive** (`~/Library/Mobile Documents/com~apple~CloudDocs/Pet Projects/`) | continuous backup + device portability | if the laptop dies or is stolen, the work is already on the next device; no restore step |
| **GitHub** | master / source of truth | versioned history with metadata, and the shareable origin peers pull from |
| **Time Machine → local NAS** | full-machine backup | device-level restore of the *whole machine* — config, tools, and work not yet synced or committed |

The repos live *inside* iCloud Drive, so the working copy and the backup are the
same folder — you get offline editing and continuous off-device protection with
no extra ritual. GitHub is the authoritative master and the sharing surface.

Two *different* classes of protection, not redundancy: iCloud and git protect
the **project files** (and git alone carries history + provenance); Time Machine
protects the **whole machine state** — the tools, config, and any work that
hasn't been synced or committed yet. The first gets a project back; the second
gets a *machine* back. macOS devices back up to a local NAS acting as a Time
Machine target in addition to the per-project protection above.

## The rule

- **GitHub is the source of truth** for anything shared or released. Where a
  public and a private edition both exist, the published repo is canonical for
  the package; the private repo re-exports into it, never merges history back.
- **iCloud is protection, not truth.** Never resolve a conflict by trusting the
  iCloud copy over git — git history wins.
- **The laptop is disposable.** The acid test: if this machine vanished right
  now, could the project be rebuilt from GitHub + iCloud + the secret store
  alone? If not, that gap is a defect to close, not a risk to carry.

## The one gotcha: keep churny/volatile state out of iCloud

iCloud sync + tooling that rewrites many files fast = trouble. Two known traps:

- **Virtual environments live *outside* iCloud** (e.g. `~/.venvs/<project>/`).
  An in-repo `.venv/` gets evicted/half-synced by iCloud and breaks. Reference
  the external venv from the repo; never commit it. *(Learned the hard way on
  the tiki venv.)*
- **Build/cache dirs** (`__pycache__/`, `.pytest_cache/`, `dist/`, `build/`,
  `node_modules/`) are gitignored and best regenerated locally — they're churn,
  not content.
- **Throwaway git worktrees go outside iCloud** too (see CONCURRENCY) — they'd
  otherwise generate sync churn for no benefit.

## Secrets are a fourth thing

Secrets are neither backed up casually nor committed in plaintext. They follow
their own regeneration doctrine: prefer *re-mint from code* over *hand-keep an
irreplaceable token*, and store at rest encrypted (e.g. sops + age), with the
encrypted form safe to commit and the plaintext gitignored. Losing the secret
store should mean "regenerate", not "lost forever".
