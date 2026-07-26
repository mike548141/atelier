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
| `ccrepo`        | observe   | Claude Code token & cost totals, grouped/filtered any way (`-g repo,model`, `--branch`, message-grain cost reconciled against ccusage), plus how large sessions' context windows got. Reads the live logs, or ccarchive's mirror (`--from-archive`). |
| `cctranscript`  | observe   | Timestamped transcript of a session — the timestamps the chat UI hides, plus how big its context grew and how many subagents it started vs finished. Reads the live logs, or ccarchive's mirror (`--from-archive`). |
| `ccarchive`     | preserve  | Durably mirror every raw `.jsonl` transcript into a compressed, append-only archive that outlives Claude Code's cleanup. |
| `browser-fetch` | extend    | A browser (fresh headless, or the operator's own Chrome) when `WebFetch`/curl are blocked. MCP server; see its own README. |

The Node CLIs are converging on a concise `-h`/`--help` digest plus a fuller
`man <tool>` page — the two-register convention in
[`build/REPO-STANDARD.md`](../docs/build/REPO-STANDARD.md) (`--help` = one-screen
reminder; `man` = plain-language reference with `FILES`/`EXAMPLES`/`NOTES`).
`ccarchive` is the worked example (`man/ccarchive.1`); `cctranscript` and `ccrepo`
follow (ROADMAP; ccrepo after its v2 rewrite). `browser-fetch` is an MCP server
with its own `instruments/browser-fetch/README.md`.

## Flag vocabulary across the cc-tools

A flag that means the same thing in more than one tool uses the **same word**,
judged from a user who moves between them. Verified 2026-07-23 by reading all
three `--help` texts, man pages and argument parsers end to end — the tools
were already consistent; this table is the standing reference so they stay
that way.

| Flag | Meaning | `ccarchive` | `cctranscript` | `ccrepo` |
|------|---------|:-----------:|:---------------:|:--------:|
| `--dest <dir>` | Where the archive lives (default iCloud Drive, or `$CCARCHIVE_DEST`) | write target | read target (implies `--from-archive`) | read target (implies `--from-archive`) |
| `--from-archive` | Read `ccarchive`'s mirror instead of the live logs | — (it *is* the archive) | ✅ | ✅ |
| `--materialise` | Also read an iCloud-evicted (dataless) file, faulting its bytes back | ✅ (`--verify`/`--audit`) | — (see note) | ✅ |
| `--json` | Machine-readable output; never styled | ✅ | ✅ | ✅ |
| `--repo` | The repo dimension | — | `--repo <name>` selects one repo to read | `--repo <list>` filters/groups (comma = OR, `!` excludes, `*` globs) |
| `-h`, `--help` | One-screen usage summary | ✅ | ✅ | ✅ |

**Note — the `--materialise` asymmetry is deliberate, not a gap.** `ccarchive`
and `ccrepo` both read *every* file in the archive on an ordinary run (a full
verify/audit; a full cost total), so an evicted mirror is a bulk-download risk
worth a skip-by-default/opt-in-override pair. `cctranscript` never reads every
file: `--list` only peeks each candidate for its first prompt and skips an
evicted one outright (no override needed — there's nothing to materialise for
a listing), and rendering one chosen session already deliberately faults an
evicted mirror back with no skip step to override in the first place. There is
no bulk-read operation on `cctranscript` for a `--materialise` flag to name, so
it doesn't carry one.

**Standing rule (flags-follow-operation — ratified by Mike 2026-07-23):**
vocabulary is uniform *whenever the operation is shared* — same word, same
meaning, no exceptions. But a flag is added to a tool only when that tool
actually performs the operation it names; it is never added to a tool for
symmetry's sake alone. The `--materialise` asymmetry above is the worked
example: bolting a `--materialise` no-op onto `cctranscript` would imply a
bulk-read control that doesn't exist there, which is worse than the current
honest gap. The alternative — force every shared-sounding flag onto every
tool regardless of whether the operation exists — was considered and rejected:
it optimises for a surface-level checklist over telling the truth about what
each tool does, and this codebase's own convention (e.g. `ccarchive` itself
carries no `--from-archive`, since it *is* the archive) already leans this way.

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
grand total. Dimensions: `repo · session · model · branch · kind · entrypoint ·
cc-version · agent · year · month · week · day · hour`. Default is `-g repo`,
cost-desc. `-g session` keys on the full UUID and *shows* an eight-character
prefix — the same prefix `--session` takes; `--json`/`--csv` keep the whole id,
because a truncated id you can't look up is worse than a wide one you can.
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

A price is **effective from a date to a date**. An entry is either a bare number
(that price, always) or a list of `{from, to, base}` intervals — ISO dates, UTC,
both ends inclusive, either end omitted for open-ended. Each message is priced at
the rate in force when it was *sent*, so a rate change no longer rewrites
history. A timestamp inside no interval is **unpriced** — $0 and flagged, exactly
as an unknown model is, never snapped to the nearest interval; the footnote names
which of the two gaps it is, because one needs a price added and the other needs
an interval widened.

**Reconciliation** keeps that honest: every run cross-checks ccrepo's own total
against `ccusage session` and prints the drift (`Δ` in $ and %, largest
per-model). A small drift is expected (token-counting edge cases); a large one
means the price table has gone stale — the guard says so instead of lying
quietly. `--no-reconcile` skips the ccusage call.

**Context med/max** answers the question the token columns don't: not how much a
group *consumed* but how *large its windows got*. Context at one request is
everything sent — input + cache create + cache read, the cached prefix included,
output excluded — the same definition `cctranscript` reports per session. It is
the one metric here that's **never summed**: every message carries the session's
whole cached prefix, so a "total context" would be that window counted over and
over. Each session contributes its *peak*, and the column shows the **median**
(what a typical session weighs) beside the **max** (the worst one). Both, because
either alone misreads — a repo sitting at 110k that once hit 578k reads dangerous
on max, calm on median; the pair says *usually fine, once wasn't*. There's no
percentage-of-window: the logs name the model but not its window size, and the
200k and 1M variants log identically, so a share figure would be a guess.

**The machine-readable forms are wider than the table, on purpose** — a terminal
column is width-bound and a data file isn't, so everything computed ships in
`--json`/`--csv` even where no column fits it: the full context distribution
(`contextMin/P25/Median/P75/P90/Max/Mean`, where the table shows two of the
seven — `contextP90` is what separates a lone outlier from a fat tail), and,
under a billing config, the `coveredTokens`/`uncoveredCost` split that `Actual`
is derived from, so the apportionment can be re-derived rather than trusted. The
grand total rides in `meta.total`, not as a row: leaf records stay subtotal-free,
and peaks genuinely can't be re-aggregated from leaves once a session is split
across groups.

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
    "spend": {
      "mode": "usage",
      "periods": { "2026-06": 200.00, "2026-07": 214.50 }
    },
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
### Actual spend vs the estimate

The `Actual` column reprices usage under the plan, but on its own it doesn't
answer the money question Mike actually asks: over the range, is **what I
genuinely pay** more or less than the API list price would have been? An optional
`spend` block supplies the genuine outlay and ccrepo reconciles it against its own
estimate — the **money-side analog of the ccusage cross-check** — in a footnote
that's a peer of the ccusage one:

```
  Actual spend vs estimate: $200.00 billed (Max 5x, $100.00/mo × 2 mo) vs $50.00 API-list-price estimate — Δ +$150.00 (+300.00%) over 2 month(s).
```

- **`spend.mode`** (default `plan`):
  - `plan` — billed = plan fee × distinct months in scope **+ uncovered per-token
    spend**. This makes the `months × fee` true outlay (previously only gestured
    at in a footnote) observable and reconciled. Works with any existing config —
    no new keys needed, since `plan.monthlyCost` is already there.
  - `usage` — billed = Σ of an invoiced/metered figure you record per month in
    `spend.periods` (`{ "YYYY-MM": amount }`, in `currency`). This is exact for a
    metered bill or a tier change mid-range. A month with **no** recorded figure
    is a stated gap (`⚠ … partial`), never smeared into the delta.
- **Scope:** like the ccusage cross-check, the comparison runs over the whole
  **date-comparable** scope, not a dimension-filtered slice — the subscription fee
  is global, so a per-repo estimate against the whole plan fee would be
  apples-to-oranges. `--json`/`--csv` carry it under `meta.spendReconciliation`
  with the same inputs the footnote shows (observable-by-design).
- **Backwards compatible:** no `spend` block ⇒ plan mode with no periods, so a
  pre-existing billing config gets the plan-mode comparison for free.
- **Degrades honestly, never fabricates:** a range the config can't answer for
  (`usage` mode with no matching invoice, or no usage at all) prints
  `Actual spend vs estimate: unavailable — <reason>`, not a guessed figure.

- **Honest limits, stated up front:** there is no API for "what you actually
  paid" — this is a user-maintained model, only as true as its config. In `plan`
  mode the billed figure assumes the plan was live for every month with usage in
  range; a month you didn't hold the plan needs `usage` mode with the real
  invoices. Plan *limits/overage thresholds* are deliberately out of scope
  (modelling when a plan tips into overage needs rate-limit data the logs don't
  carry) — that gap stays a stated footnote, not silently absorbed.

## cctranscript's header line — and what a missing figure prints as

Under the session title sits one dense summary line, read left to right:
turn counts, then **agents started · finished**, then the context peak, then the
clock span. It is designed to be read by **comparing two sessions side by side**,
which fixes one rule: the *field set* never varies between runs.

**Agents started vs finished** is a deliberate pair. *Started* counts the spawn
tool calls (`Agent`, legacy `Task`) — a ceiling, since a skipped or stopped spawn
still counts. *Finished* counts the per-agent logs in the session's sibling
`<uuid>/subagents/` directory, one per agent that actually ran. The gap is where
a spawn that never became a run shows up. Neither bounds the other: a nested
spawn (an agent spawning its own agent) logs into the same directory while
*started* sees only the principal's calls, so finished can legitimately run
ahead, and the figures are left unclamped rather than hide that. Both figures
survive `--from-archive` — ccarchive captures every `.jsonl` at any depth and
mirrors it at the same relative path, so the per-agent logs are in the archive
too (their `.meta.json` sidecars are not, which is why the count keys on logs).

**Where the two rules meet.** A zero the log *proves* is a fact worth printing;
a figure the log never recorded is *unknown*, and printing that as zero would be
a claim the evidence doesn't support. Against that sits the stable-field-set
rule above. They are reconciled by splitting set from value: both agent chips
print on **every** run, and where no per-agent store is reachable the second one
reads `finished unknown` rather than dropping out — the chip holds its position
and the *value* carries the honesty. `--json` gives `agents.finished: null` with
`agents.finishedKnown: false`, so unknown is distinguishable from a zero and the
key is never simply absent. A zero still prints wherever it is proved: no spawn
call in the log means no agent can have run. The context figure is the case with
*no* fixed pair to keep aligned, so it simply omits itself when a log carries no
usage records — the opposite treatment, for the opposite reason.

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
  weaker anchor than raw bytes). The sha256 manifest defends against *accidental*
  corruption; the **signature** below raises it to *tamper-evident*. Run `--verify`
  any time, and after any restore.
- **Tamper-evidence — a signed manifest.** The hash manifest alone isn't
  tamper-proof: a tamperer with write access to the archive volume (iCloud) could
  rewrite a `.gz` **and** recompute the manifest hash, and a hash-only `--verify`
  would pass. So ccarchive **signs** the manifest — an **HMAC-SHA256** over its
  exact bytes, with a secret key kept *off* the archive volume — writing a detached
  `manifest.json.sig` beside it; `--verify` recomputes the MAC and a forged manifest
  no longer matches. HMAC not asymmetric (design call): signer and verifier are the
  same machine/user, so a local symmetric key is the KISS fit — a public key shipped
  *inside* the archive would just be swapped by the same tamperer. The key lives at
  `~/.claude/ccarchive-signing.key` (mode `0600`, off-archive; `CCARCHIVE_KEYFILE`
  overrides — the cron/launchd and test seam), a **file** rather than the Keychain
  because a background/scheduled run can read a file without a Keychain prompt and
  the key guards tamper-*evidence*, not confidentiality. It's minted at first use
  (32 bytes of entropy) and **re-mintable**: `ccarchive --rekey` rolls it and
  re-signs the current manifest (the signature only ever attests the current
  manifest, so a roll loses nothing) — roll on suspected exposure or on a cadence,
  but keep an **out-of-band backup** of the key, because a *new machine* needs it to
  verify (SECRETS.md's redundancy obligation, applied). Every manifest write
  re-signs, and a pre-signing archive is migrated on the next run. `--verify` fails
  **safe and honest**, never green on doubt: it separates a `MISMATCH` (tamper) from
  a `different-key` signature, an `unsigned` manifest (migrate), and an
  `unverifiable` one (no key here). What it does **not** stop: a tamperer who also
  **steals the key** can forge a valid signature (hence the key's confidentiality
  and cheap rotation), and it's evidence at *verify* time, not prevention of the
  write.
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
- **Restore — `--restore` (full) and `--restore --delta`.** The inverse of the
  audit: gunzip archived transcripts back into the live store. Plain `--restore`
  targets the whole manifest (rebuild a wiped store or seed a new machine);
  `--restore --delta` targets only what `--audit` flags — the **mutated**,
  **pruned** and **renamed** buckets — repairing in place. Safety is
  **content-first**: it never overwrites an identical file, and never a live file
  the archive is a strict prefix of (the **grown** bucket — an in-flight append;
  clobbering it would drop the live tail, so grown is *not* a restore target). A
  file that diverged *another* way but is **newer** than the archived copy is
  **refused** (possible in-flight rewrite) unless `--force` — a loud, deliberate
  override. The **renamed** bucket restores the *old* archived path and leaves the
  live renamed copy untouched (byte-identical content, so a copy under the old
  name, never a move). Writes only under the source tree — a manifest key that
  would escape it is refused — and `--dry-run` previews the plan without writing.
- **iCloud dataless-file awareness.** The default dest is iCloud Drive, whose
  "Optimise Mac Storage" can *evict* an archived `.gz`'s local bytes — leaving a
  **dataless** placeholder that faults back on read. Reading one re-downloads it,
  so a whole-archive `--verify` would drag the entire history back onto disk and
  defeat the eviction. `ccarchive` detects it (the `SF_DATALESS` bit in `st_flags`,
  read via `stat` — Node exposes no `st_flags` of its own) and by default
  `--verify` **skips** evicted files, reporting them `evicted` (distinct from
  `missing`/`mismatch`, and *not* a failure — the bytes are intact in the cloud);
  `--audit` likewise leaves a changed file whose archive copy is evicted
  *undetermined* rather than faulting it back. `--verify --materialise` /
  `--audit --materialise` reads them anyway (re-downloading). `--restore` reads
  evicted files deliberately — restoring *is* getting the content back. Detection
  is metadata-only (`stat` and the mtime check don't fault), so ordinary archiving
  never triggers a bulk re-download; off macOS or on a non-iCloud volume it cleanly
  no-ops. (The real `SF_DATALESS` read was verified read-only against a genuinely
  evicted file; fixtures can't be truly evicted, so the tests drive it through a
  simulation seam.)
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
deferred a *retention ledger* — persisting cost/usage rollups so ccrepo's
month/quarter views survive the prune. ccarchive **subsumes that idea's survival
purpose**: it keeps the full raw logs losslessly (~1.2 GB/yr), in a tree that
mirrors `~/.claude/projects/` exactly, so *any* historical view — ccrepo's time
grouping included — can be recomputed at full fidelity from the archive. The
sourcing seam is **closed on the observe side** (2026-07-23): both observers take
`--from-archive` and read the mirror directly, sharing `--dest`/`$CCARCHIVE_DEST`
resolution with ccarchive and one transparent-gunzip read path, so a pruned
session is still fully readable. `cctranscript --from-archive` renders it word for
word (eviction-aware listing — a `--list` never faults iCloud-evicted bytes back);
`ccrepo --from-archive` prices the whole preserved history past the prune horizon.
Because ccrepo must read *every* file to sum spend, it skips an evicted (dataless)
mirror by default and counts it as a stated gap — `--materialise` opts into reading
(re-downloading) them — and it turns the ccusage cross-check off in archive mode,
since ccusage reads the live store the pruned sessions have already left.

With survival settled by the archive, the ledger the design deferred is now built
as **exactly what remains — a pure precompute/speed layer**, never a data one
(2026-07-23). A wide `--from-archive` run re-gunzips the whole ~1 GB/yr mirror
every time; the rollup ledger (`~/.claude/ccrepo-rollup.json`, machine-local, the
same class as the pricing/billing configs) caches each source file's parsed,
priced messages under a cheap `(mtime,size)` fingerprint. The archive is
append-only, so an existing file is always a hit and only genuinely new sessions
are re-read — a warm whole-history run drops from ~12 s to ~4 s on the live
machine at unchanged numbers. It is keyed **per file, not per calendar period**:
a month can't be fingerprinted without first reading files to learn each message's
timestamp, and a boundary-straddling session would be misfiled by any date proxy,
so file-grain keying is the simpler thing that keeps *rollup == full recompute*
(month/quarter grouping is computed downstream from true timestamps, identical to
an uncached run). Baked cost/covered depend on the price table + covers-list, both
folded into a recipe signature that rebuilds the ledger when either moves. Used
transparently when present; `--no-rollup` bypasses it for a from-scratch re-walk.
`man ccrepo` § ROLLUP LEDGER has the full contract.

## Schema caveat

The observers (`ccrepo`, `cctranscript`) read Claude Code's session `.jsonl` logs,
whose format is internal to the tool and can shift between releases. A clean run
today can need a small nudge after an update; each instrument isolates the parsing
so the fix is local. `ccarchive` is exempt — it copies bytes, it doesn't parse.
