# instruments/ — tools for working with Claude as a teammate

Where `tools/` **enforces** the doctrine (checks that gate a commit),
`instruments/` **observes** the collaboration itself — what it costs, and what
happened when. They have no purpose outside the human+Claude working
relationship; that's what earns them a place in atelier rather than in a
personal infra repo (see `docs/decisions/0006-instruments-in-atelier.md`).

Unlike the `tools/` scanners (Python, zero-dep, hook-wired), these are small
zero-dependency **Node** CLIs you run interactively from anywhere. Each reads
the local Claude Code logs under `~/.claude/projects/` **read-only** — nothing
here writes to those logs.

| Instrument     | Lens         | What it does                                                         |
|----------------|--------------|---------------------------------------------------------------------|
| `ccrepo`       | DevFinOps    | Per-repo Claude Code token & cost totals (`--by-model`, `--by-day`). |
| `cctranscript` | Observability| Timestamped transcript of a session — the timestamps the chat UI hides. |

Every instrument has `-h`/`--help`.

## Install (and on a new machine)

These aren't run from this folder directly — instead each is symlinked into
`~/.local/bin` (which is on `PATH`). The installer is idempotent; re-run it
after adding an instrument or on a fresh laptop:

```sh
./instruments/install
```

Requirements: `node` on `PATH` (any recent LTS) for all of them; `ccrepo` also
needs `ccusage` (`npx ccusage` or a global install). If `~/.local/bin` isn't on
your `PATH`, the installer prints the one line to add to your shell profile.

## What belongs here (and what doesn't)

The boundary is purpose, not runtime: an instrument earns a place here only if
its value is *the Claude teammateship* — costing it, observing it, steering it.
General machine/infra utilities (macOS, TrueNAS, networking) that you or Claude
merely *use* from time to time do **not** belong here — they live with the estate
they serve. `docs/decisions/0006-instruments-in-atelier.md` records that line.

## Schema caveat

Both read Claude Code's session `.jsonl` logs, whose format is internal to the
tool and can shift between releases. A clean run today can need a small nudge
after an update; each instrument isolates the parsing so the fix is local.
