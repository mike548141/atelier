# instruments/ — tools for working with Claude as a teammate

Where `tools/` **enforces** the doctrine (checks that gate a commit),
`instruments/` serve the collaboration itself — they **observe** it (what it
costs, what happened when) or **extend its reach** (what the teammate can do).
They have no purpose outside the human+Claude working relationship; that's what
earns them a place in atelier rather than in a personal infra repo (see
`docs/decisions/0006-instruments-in-atelier.md`, incl. the 2026-07-12 addendum
that widened the layer to capability tools).

Most are small zero-dependency **Node** CLIs that read the local Claude Code logs
under `~/.claude/projects/` **read-only**. The capability tools are the honest
exception — they act on the world and may carry pinned dependencies (browser-fetch
drives Chrome via Playwright); each documents its own runtime.

| Instrument      | Verb      | What it does                                                         |
|-----------------|-----------|---------------------------------------------------------------------|
| `ccrepo`        | observe   | Per-repo Claude Code token & cost totals (`--by-model`, `--by-day`). |
| `cctranscript`  | observe   | Timestamped transcript of a session — the timestamps the chat UI hides. |
| `browser-fetch` | extend    | A browser (fresh headless, or the operator's own Chrome) when `WebFetch`/curl are blocked. MCP server; see its own README. |

The Node CLIs each have `-h`/`--help`; `browser-fetch` is an MCP server with its
own `instruments/browser-fetch/README.md`.

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

`browser-fetch` installs differently — it's an MCP server, not a `~/.local/bin`
CLI. Run `instruments/browser-fetch/setup` (builds a venv + Chromium, prints the
`~/.claude.json` registration Claude Code reads at start).

## What belongs here (and what doesn't)

The boundary is purpose, not runtime: an instrument earns a place here only if
its value is *the Claude teammateship* — costing it, observing it, steering it.
General machine/infra utilities (macOS, TrueNAS, networking) that you or Claude
merely *use* from time to time do **not** belong here — they live with the estate
they serve. `docs/decisions/0006-instruments-in-atelier.md` records that line.

## ccrepo billing model — Actual vs Est

ccrepo's Cost column is an **API-equivalent estimate** (ccusage's USD basis) —
"a gauge, not your bill". A subscription-plan user's *actual* spend diverges
sharply, and the general shape is **hybrid**: a flat plan covering some models
plus per-token billing for the rest or for overage. When a billing config is
present, ccrepo shows both numbers side by side — **Est (API)** and
**Actual** — and `--json` carries `actual` on every repo/model/day plus a
top-level `billing` block. `--no-billing` forces estimate-only for a run.

- **Home:** `~/.claude/ccrepo-billing.json` — machine-local like leakscan's term
  list, **never in a repo** (a person's plan and spend are personal data).
  Absent file ⇒ ccrepo behaves exactly as before (estimate only); no new
  requirement on anyone else's machine. A malformed file is ignored with a
  warning, never fatal.
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

- **Semantics:** `covers[]` entries match a model family by prefix after
  `claude-` is stripped (`opus` matches `opus-4-8`); `perTokenModels` carves a
  specific model back out of an otherwise-covered family. Tokens on covered
  models cost **$0 marginal** — the flat plan fee is a sunk monthly cost,
  apportioned across repos by each repo's share of covered tokens (if nothing in
  range ran on a covered model, it falls back to total-token share so a fee you
  really paid is still reflected). Tokens on uncovered models keep the API-rate
  estimate as their actual. **Actual = apportioned plan share + uncovered
  per-token spend** — so the TOTAL Actual row is exactly `plan fee + all
  uncovered spend`.
- **Honest limits, stated up front:** there is no API for "what you actually
  paid" — this is a user-maintained model, only as true as its config. The plan
  fee shown is **one month**; over a multi-month range true plan outlay is
  `months × fee` — v1 doesn't infer the month count (a footnote says so). Plan
  *limits/overage thresholds* are deliberately out of scope v1 (modelling when
  a plan tips into overage needs rate-limit data the logs don't carry) — that
  gap stays a stated footnote, not silently absorbed.

## Schema caveat

Both read Claude Code's session `.jsonl` logs, whose format is internal to the
tool and can shift between releases. A clean run today can need a small nudge
after an update; each instrument isolates the parsing so the fix is local.
