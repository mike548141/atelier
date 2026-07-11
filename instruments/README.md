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

## ccrepo billing model — designed, not yet built

ccrepo's Cost column is an **API-equivalent estimate** (ccusage's USD basis) —
"a gauge, not your bill". A subscription-plan user's *actual* spend diverges
sharply, and the general shape is **hybrid**: a flat plan covering some models
plus per-token billing for the rest or for overage. The roadmap item wants both
numbers side by side; per its design-before-code rule, the config is designed
here first:

- **Home:** `~/.claude/ccrepo-billing.json` — machine-local like leakscan's term
  list, **never in a repo** (a person's plan and spend are personal data).
  Absent file ⇒ ccrepo behaves exactly as today (estimate only); no new
  requirement on anyone else's machine.
- **Shape** (all fields optional beyond `plan.monthlyCost`):

  ```json
  {
    "currency": "USD",
    "plan": {
      "name": "Max 20x",
      "monthlyCost": 200,
      "covers": ["opus", "sonnet", "haiku", "fable"]
    },
    "perTokenModels": ["some-uncovered-model"],
    "notes": "covers[] matches model-family prefixes after claude- is stripped"
  }
  ```

- **Semantics:** tokens on `covers` models cost **$0 marginal** (the plan is a
  sunk monthly cost, reported as its own line, apportionable per repo by share
  of covered tokens); tokens on `perTokenModels` (or any model not covered)
  keep the API-rate estimate as their actual. Actual = plan share + uncovered
  per-token spend. Both columns render side by side: *Est (API)* and *Actual*.
- **Honest limits, stated up front:** there is no API for "what you actually
  paid" — this is a user-maintained model, only as true as its config; plan
  *limits/overage thresholds* are deliberately out of scope v1 (modelling when
  a plan tips into overage needs rate-limit data the logs don't carry — that
  gap stays visible in the output as a footnote, not silently absorbed).

## Schema caveat

Both read Claude Code's session `.jsonl` logs, whose format is internal to the
tool and can shift between releases. A clean run today can need a small nudge
after an update; each instrument isolates the parsing so the fix is local.
