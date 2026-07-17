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
| `ccrepo`        | observe   | Claude Code token & cost totals, grouped/filtered any way (`-g repo,model`, `--branch`, message-grain cost reconciled against ccusage). |
| `cctranscript`  | observe   | Timestamped transcript of a session — the timestamps the chat UI hides. |
| `ccarchive`     | preserve  | Durably mirror every raw `.jsonl` transcript into a compressed, append-only archive that outlives Claude Code's cleanup. |
| `browser-fetch` | extend    | A browser (fresh headless, or the operator's own Chrome) when `WebFetch`/curl are blocked. MCP server; see its own README. |

The Node CLIs are converging on a concise `-h`/`--help` digest plus a fuller
`man <tool>` page — the two-register convention in
[`build/REPO-STANDARD.md`](../docs/build/REPO-STANDARD.md) (`--help` = one-screen
reminder; `man` = plain-language reference with `FILES`/`EXAMPLES`/`NOTES`).
`ccarchive` is the worked example (`man/ccarchive.1`); `cctranscript` and `ccrepo`
follow (ROADMAP; ccrepo after its v2 rewrite). `browser-fetch` is an MCP server
with its own `instruments/browser-fetch/README.md`.

## Install (and on a new machine)

These aren't run from this folder directly — instead each is symlinked into
`~/.local/bin` (which is on `PATH`). The installer is idempotent; re-run it
after adding an instrument or on a fresh laptop:

```sh
./instruments/install
```

It symlinks each CLI into `~/.local/bin` and each `man/*.1` page into
`~/.local/share/man/man1` (auto-found by `man` because `~/.local/bin` is on
`PATH`), so `man ccarchive` works after install.

Requirements: `node` on `PATH` (any recent LTS) for all of them. `ccrepo`
computes cost itself from the logs, but uses `ccusage` (`npx ccusage` or a global
install) for its reconciliation cross-check — skip it with `--no-reconcile` if
ccusage isn't present. If `~/.local/bin` isn't on your `PATH`, the installer
prints the one line to add to your shell profile.

`browser-fetch` installs differently — it's an MCP server, not a `~/.local/bin`
CLI. Run `instruments/browser-fetch/setup` (builds a venv + Chromium, prints the
`~/.claude.json` registration Claude Code reads at start).

`ccarchive` has one extra step to keep it *running*: after `install` puts it on
`PATH`, `ccarchive --install-schedule` registers the daily launchd agent (macOS).
This is the whole new-machine recovery — `./instruments/install` then
`ccarchive --install-schedule` — and `ccarchive --schedule-status` confirms it.

## What belongs here (and what doesn't)

The boundary is purpose, not runtime: an instrument earns a place here only if
its value is *the Claude teammateship* — costing it, observing it, steering it.
General machine/infra utilities (macOS, TrueNAS, networking) that you or Claude
merely *use* from time to time do **not** belong here — they live with the estate
they serve. `docs/decisions/0006-instruments-in-atelier.md` records that line.

## ccrepo grouping, filters & the cost engine

**Grouping** is an ordered dimension list — `-g repo,model` nests model under
repo, `-g model,repo` inverts it, `-g month` totals per month, `-g total` is one
grand total. Dimensions: `repo · model · branch · kind · entrypoint · cc-version
· agent · year · month · week · day · hour`. Default is `-g repo`, cost-desc.
The reader is a tree by default (`Sessions` is a *distinct* count at every level);
`--flat` gives one column per level, `--json`/`--csv` give one tidy record per
leaf (each dimension a named field, a `meta` block up top).

**Filters** mirror that exact vocabulary — `--repo`, `--model`, `--branch`,
`--kind`, `--entrypoint`, `--cc-version`, `--agent`, `--session`, plus
`--since`/`--until`. Comma = OR within a dimension, leading `!` excludes, `*`
globs; sessions match by UUID prefix. `--sort` overrides the per-dimension
defaults (time chronological, else cost-desc), aligned to the group levels.

**Cost is computed here, per message**, from a local list-price table across five
token classes — input, output, cache read, and the 5m/1h cache-*write* split
(they price differently). branch/kind/version/hour vary *within* a session, so
this message grain is what lets ccrepo group by them; the price table lives at
the top of the script, overridable at `~/.claude/ccrepo-pricing.json`.

**Reconciliation** keeps that honest: every run cross-checks ccrepo's own total
against `ccusage session` and prints the drift (`Δ` in $ and %, largest
per-model). A small drift is expected (token-counting edge cases); a large one
means the price table has gone stale — the guard says so instead of lying
quietly. `--no-reconcile` skips the ccusage call.

## ccrepo billing model — Actual vs Est

ccrepo's Cost column is an **API-equivalent estimate** (list prices, reconciled
against ccusage) — "a gauge, not your bill". A subscription-plan user's *actual*
spend diverges
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

## ccarchive — keeping transcripts past Claude Code's cleanup

Claude Code deletes session logs older than `cleanupPeriodDays` (default 30). The
raw `.jsonl` under `~/.claude/projects/` *is* the complete word-for-word record —
every timestamp, model, token count, tool call and thinking block — so losing it
loses history the chat UI can't reconstruct. `ccarchive` mirrors every `.jsonl`
(sessions **and** nested subagent logs) into a compressed archive that outlives
that cleanup:

- **Incremental gzip mirror**, not one monolithic tarball: each
  `<rel>/<name>.jsonl` becomes `<dest>/<rel>/<name>.jsonl.gz`. Each session stays
  individually readable (gunzip, then `cctranscript <path>`; or `zgrep`), and only
  sessions changed since the last run are recompressed — cheap to run often and
  light on a synced dest (only new/updated files upload). ~2.8× smaller than raw.
- **Append-only by contract:** it never deletes from the archive. When Claude
  Code's cleanup removes a source log, the archived copy stays — that is the point.
  It doesn't parse the `.jsonl`, it preserves the bytes, so it's immune to schema
  drift (unlike the observers below). Append-only is not overwrite-proof, so two
  guards protect the sole durable copy: a **shrink guard** refuses to overwrite
  when a newer source is *smaller* than the size recorded at capture (sessions
  only grow; a shrink means truncation or corruption upstream — `--force` is the
  deliberate override), and a source yielding **zero transcripts** against a
  non-empty manifest exits non-zero instead of logging success while the archive
  quietly stops growing (the live dir moved). A dest inside a git work tree is
  also refused (`--allow-repo-dest` overrides): transcripts are personal data,
  and a repo dest is one commit away from publication.
- **Integrity — sha256 manifest + `--verify`.** gzip's CRC-32 catches a corrupted
  `.gz` on decompression, but it's weak and only proves the file is
  self-consistent. So ccarchive records a **sha256 of each transcript's raw bytes**
  in `<dest>/manifest.json` when it archives; `ccarchive --verify` re-hashes every
  archived `.gz` and compares, reporting any **mismatch** (mutation/bit-rot/sync
  glitch) or **missing** file and exiting non-zero if the archive doesn't verify.
  The manifest tracks the *archive* (append-only), not live sources — a pruned
  session keeps its recorded hash because its `.gz` is kept. An archived file
  *absent* from the manifest fails the verify (injected, or lost history — both
  need a human eye), and entries backfilled from the `.gz` after their source was
  pruned are counted distinctly (`fromArchive`: the archive attesting itself, a
  weaker anchor than raw bytes). It's the trust
  anchor: it defends against accidental corruption; for tamper-resistance keep a
  copy of `manifest.json` somewhere separate from the archive (a mutation that
  also rewrote the manifest would pass). Run it any time, and after any restore.
- **Live-store audit — `--audit`.** `--verify` asks whether the *archive* is
  intact; `--audit` asks the other question — has the *live* store drifted from
  what was preserved? It hashes every live `.jsonl` and buckets it: **synced**
  (matches the recorded sha256), **grown** (the archived bytes are a strict
  prefix — a plain append the next run will capture), **mutated** (rewritten or
  truncated — the archive no longer equals the session's history), **renamed**
  (content matched under an archived path now gone from the live store), **new**
  (unarchived, matches nothing) and **pruned** (archived, no live counterpart —
  the expected steady state after cleanup). Only **mutated** and **renamed** are
  drift: they're listed by name and exit non-zero; growth, new and pruning are
  normal and only counted. Read-only over both trees.
- **Default dest is the operator's iCloud Drive** (`--dest` / `CCARCHIVE_DEST` to
  override) — derived at runtime from `$HOME`, so no personal path lives in this
  code. It's the first *writing* instrument (see ADR 0006 addendum); `--dry-run`
  previews, and it reads the source read-only.
- **Self-scheduling.** `ccarchive --install-schedule` writes and loads a launchd
  agent (macOS) that runs it daily and at login — no hand-wired cron, and it
  re-establishes on a new machine with one command (`--schedule-status` /
  `--uninstall-schedule` round it out; non-macOS prints the cron line instead).
  The agent, its plist and log live under `~/Library` — machine-local, outside
  any repo; the tool that generates them is data-free (paths derived at runtime).
- **Retention pairing.** A daily run captures every session well inside Claude
  Code's `cleanupPeriodDays`, so the archive alone is the durable copy — a large
  `cleanupPeriodDays` is optional (a longer *live* working window for the other
  instruments, and a buffer if the agent is ever down for a stretch), never
  required for survival. Idempotent, exits 0 with nothing to do.

**The durable substrate for the *other* instruments too.** `ccrepo.design.md` §8
defers a *retention ledger* — persisting cost/usage rollups so ccrepo's
month/quarter views survive the prune. ccarchive **subsumes that idea's survival
purpose**: it keeps the full raw logs losslessly (~1.2 GB/yr), in a tree that
mirrors `~/.claude/projects/` exactly, so *any* historical view — ccrepo's time
grouping included — can be recomputed at full fidelity from the archive. A rollup
ledger, if ever built, is then a *precompute/speed* layer, not a *data-survival*
one. The open seam is sourcing: `ccrepo`/`cctranscript` read `.jsonl` from the
live dir, not `.jsonl.gz` from the archive — a `--source <archive>` with
transparent gunzip (or a `ccarchive` hydrate mode) is what turns preservation into
usable extended history. Not built here; noted so the two ideas stay reconciled.

## Schema caveat

The observers (`ccrepo`, `cctranscript`) read Claude Code's session `.jsonl` logs,
whose format is internal to the tool and can shift between releases. A clean run
today can need a small nudge after an update; each instrument isolates the parsing
so the fix is local. `ccarchive` is exempt — it copies bytes, it doesn't parse.
