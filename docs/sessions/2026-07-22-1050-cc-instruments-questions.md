# cc-instruments — two open questions answered (2026-07-22)

*Analysis session. Two questions queued by Mike (2026-07-22): (1) does `ccarchive`
miss any metadata worth preserving, and (2) should `cctranscript` and `ccarchive`
be one instrument? Grounded by reading the instrument source, the man pages, ADR
0006, and a **read-only** enumeration of the live `~/.claude` tree. Nothing from
that tree — no project names, no paths beyond the generic Claude Code layout, no
session content — enters this record; only the structural shape and rough
magnitudes needed to answer the questions. Recommendations are labelled; the
decisions are Mike's.*

---

## Q1 — Is there metadata ccarchive misses?

### What ccarchive actually captures

From the source (`instruments/ccarchive`, `listJsonl` + `run`): the source root is
`~/.claude/projects` (overridable via `--source`/`CCARCHIVE_DEST`). `listJsonl`
walks it **recursively** and collects **every file ending `.jsonl` at any depth**.
Each `<rel>/<name>.jsonl` is mirrored to `<dest>/<rel>/<name>.jsonl.gz`. It copies
bytes; it never parses. So the capture rule is exactly: *`.jsonl`, anywhere under
`projects/`, and nothing else.*

That rule draws two boundaries the archive's stated purpose (ADR 0006 addendum
2026-07-17 — "durably mirror every raw session `.jsonl` … so transcripts survive
Claude Code's cleanup") half-acknowledges and half-doesn't:

1. **Within `projects/`**, non-`.jsonl` files sitting *beside* the transcripts are
   silently skipped.
2. **Outside `projects/`**, the entire rest of the `~/.claude` tree is out of the
   source root by design.

### The real top-level structure (enumerated read-only)

Claude Code's `~/.claude` on this machine holds, top-level:
`projects/` · `file-history/` · `sessions/` · `session-env/` · `shell-snapshots/`
· `plugins/` · `backups/` · `ide/` · `mcp-servers/` · `cache/` · `chrome/` ·
`paste-cache/` · `bin/` · `downloads/` · `history.jsonl` · `settings.json` ·
`settings.local.json` · `CLAUDE.md` · `leakscan-terms.txt` · a statusline script ·
and a few dotfiles. (No `todos/` and no `statsig/` dir exist on this machine —
worth naming because both appear on other Claude Code installs; if a future CC
version reintroduces them under `projects/`-adjacent paths, re-run this check.)

### Classification A — inside `projects/` (ccarchive's own scope)

| Class | What it is | Disposition | Note |
|---|---|---|---|
| `<uuid>.jsonl` | session transcript | ✅ **captured** | the core purpose |
| `<uuid>/subagents/*.jsonl` | nested subagent logs | ✅ **captured** | recursive walk reaches them |
| `<uuid>/tool-results/*.txt`, `*.json` (and older `<uuid>/toolu_*.txt/.json`) | **offloaded large tool outputs** — the transcript keeps a *pointer*, the payload lives here | ❌ **silently missed** | not `.jsonl` |
| `<project>/memory/*.md` | per-project auto-memory (MEMORY index + named entries), one dir per active project | ❌ **silently missed** | not `.jsonl` |
| `<project>/webfetch-*.pdf` | PDFs fetched by WebFetch, cached beside the session | ❌ **silently missed** | not `.jsonl` |

Rough scale: non-`.jsonl` content under `projects/` is ~40 MB across ~640 files
vs ~560 MB of `.jsonl` — i.e. **~7 % of transcript volume**, dominated by the
tool-result sidecars.

### Classification B — outside `projects/` (out of source root)

| Class | What it is | Disposition | Matters to preservation? |
|---|---|---|---|
| `history.jsonl` (top-level) | the prompt/command history you typed | ❌ missed — and notably it **is** `.jsonl`, just not under `projects/` | Low. Prompts are re-derivable from the transcripts themselves. |
| `file-history/` (~210 MB) | per-session checkpoint copies of files Claude edited (undo substrate) | ⚪ excluded by scope | Mostly derivable from repo git history; large; not transcript. |
| `sessions/`, `session-env/`, `shell-snapshots/` | per-session runtime metadata / env / shell snapshots | ⚪ excluded by scope | Ephemeral runtime state, not the record of the work. |
| `plugins/`, `backups/`, `settings*.json`, `CLAUDE.md`, `leakscan-terms.txt` | config, plugin state, config backups | ⚪ excluded by scope | Config/reproducible or personal; belongs in its own backup story, not a transcript archive. |
| `ide/`, `cache/`, `chrome/`, `paste-cache/`, `bin/`, `downloads/`, `mcp-servers/` | locks, caches, scratch | ⚪ excluded by scope | Pure runtime; no preservation value. |

### Do the silently-missed classes matter, and what would capture cost?

- 🔎 **`tool-results/` sidecars — the one that genuinely bites.** When a tool
  output is large, Claude Code offloads the payload to a sidecar file and leaves
  only a reference in the `.jsonl`. So the archived transcript can contain a
  **dangling pointer to content that was never archived** — and once
  `cleanupPeriodDays` prunes the live sidecar, that content is gone for good while
  the archive still *looks* complete. This is the sharpest gap: it silently
  undercuts the "word-for-word complete record" claim the README makes for the
  archive. Cost to capture: **low and clean** — widen the walk to mirror the whole
  `<uuid>/` subtree (or at least `tool-results/` + `toolu_*`) as raw bytes beside
  the `.jsonl.gz`. It fits the byte-copy, schema-immune model perfectly (these are
  opaque payloads); it just needs the manifest/verify/audit/restore paths to treat
  a non-`.jsonl` archived file as a first-class member (today `listArchivedRels`
  and the verify walk key on `.jsonl.gz`). Moderate code change, no new dependency.

- 🔎 **`memory/*.md` — matters, but it's a policy call.** Per-project auto-memory
  is durable working state that evolves across sessions and is **not** in any repo
  (it's the cross-session "what I learned about this project"). Losing it on a
  machine wipe loses real continuity. But it is *not a transcript*, it lives a
  fresh copy in the working tree, and — the catch — it can carry the **most**
  personal content of anything here (it's literally distilled context). Capturing
  it into the same iCloud archive is defensible (the archive is already a personal,
  outside-any-repo store), but it widens what "the transcript archive" means.
  Cost: low technically; the real cost is scope-definition, hence a Mike call.

- **`webfetch-*.pdf` — marginal.** Point-in-time snapshots of fetched web pages;
  broadly re-fetchable, rarely load-bearing after the session. Low value, non-zero
  bytes. Cheapest to just document as excluded.

- **`file-history/` — deliberately out.** Large (~210 MB), and its value (undo)
  overlaps repo git. Preserving it would roughly *double* the archive for weak
  marginal benefit. Exclude and say so.

### 🎯 Recommendation for Mike — Q1

| Missed class | Recommendation | Why |
|---|---|---|
| **`tool-results/` + `toolu_*` sidecars** | 🟢 **Capture** | Fixes a real hole in the "complete transcript" promise — archived pointers to pruned payloads. Byte-copy fits ccarchive's model; low cost. |
| **`memory/*.md`** | 🟠 **Needs-Mike** | Genuine continuity value, but stretches archive scope and is the most personal content. Your call whether the transcript archive is also the memory archive. |
| **`history.jsonl` (top-level prompts)** | 🟠 **Needs-Mike (lean: exclude)** | Re-derivable from transcripts; small. Include only if you want the prompt stream as a first-class artefact. |
| **`webfetch-*.pdf`** | ⚪ **Exclude + document** | Re-fetchable, marginal, adds bytes. |
| **`file-history/`, `sessions/`, `session-env/`, `shell-snapshots/`, config/plugins/caches** | ⚪ **Exclude + document** | Runtime/config/derivable; not the record of the work. Belongs in a separate backup story if at all. |

**Net:** one clear fix (tool-result sidecars), two policy calls (memory, prompt
history), the rest explicitly excluded. Whatever's chosen, ccarchive's man page
`FILES`/`NOTES` should state *what it does not capture* — right now the exclusion
of same-directory non-`.jsonl` payloads is invisible, and an archive that silently
drops referenced content while advertising completeness is exactly the
apex-honesty smell (`00-APEX.md`: no claim stronger than its evidence).

---

## Q2 — Should cctranscript and ccarchive be one instrument?

### Measured duplication (not guessed)

Read both files and diffed the shared surface:

| | `cctranscript` | `ccarchive` |
|---|---|---|
| Lines | 579 | 837 |
| Node deps | `fs`, `os`, `path` | `fs`, `os`, `path`, `zlib`, `crypto`, `child_process` |
| Literally-shared code | `takeValue()` (4 lines, **verbatim**); `~/.claude/projects` derived from `os.homedir()` (1 line); the *concept* of walking `projects/` for `.jsonl` | same |
| Everything else | ~400 lines of **rendering** — ANSI colour, word-wrap, turn headers, model palette, delta formatting, prompt/tool-result discrimination | ~700 lines of **archive mechanics** — gzip mirror, sha256 manifest, shrink guard, `--verify`, `--audit` divergence buckets, `--restore` safety, launchd scheduling |

**Verdict on the premise:** the "they duplicate work" intuition doesn't survive
measurement. Genuine shared code is **~5–15 lines** (`takeValue` + the projects-dir
one-liner). The two file-walkers even differ: `cctranscript`'s discovery is rich
(`allSessions`, `sessionRecord`, `cwdFromLog`, `encodePath` — it decodes the
encoded repo path back to a working dir and picks a session), while ccarchive's is
a bare recursive `.jsonl` collector. There is **near-zero overlap** beyond "both
know where Claude Code puts its logs and how a session file is named."

### Divergent purposes — and one that actively resists merging

| Axis | cctranscript | ccarchive |
|---|---|---|
| Verb (ADR 0006) | **observe** (read/render) | **preserve** (write/verify/restore) |
| Reads/writes | read-only | writes the sole durable copy |
| Schema coupling | **parses** `.jsonl` — schema-fragile, needs nudges across CC releases | **copies bytes** — schema-**immune** by design |
| Run cadence | interactive, on demand | unattended, scheduled (launchd), idempotent |
| Failure meaning | a render glitch | a data-integrity event (shrink guard, non-zero on empty source) |

The schema row is the load-bearing one. The README states it outright:
cctranscript is schema-fragile; **ccarchive is exempt because it doesn't parse.**
Merging them puts a fragile parser and a schema-immune preserver in one file — and
the preserver is the one guarding the *only durable copy of the history*. Coupling
its reliability to a parser that "can need a small nudge after an update" trades
away the single best property ccarchive has. That's not a style objection; it's an
architecture one.

### CLI-surface fit, house pattern, man/install

- **CLI surface.** cctranscript's flags are about *viewing* (`--list`, `--tools`,
  `--think`, `--full`, `--utc`, `-n`, `--repo`). ccarchive's are about *custody*
  (`--verify`, `--audit`, `--restore [--delta]`, `--force`, `--dry-run`,
  `--install-schedule`, `--dest`). A merged tool would be two disjoint flag
  vocabularies under one name — the "mode-switch multitool" anti-shape, not one
  coherent surface.
- **House pattern.** The observers are **single-file, zero-dep Node CLIs** (ADR
  0006). Both already honour it. A merge keeps one file but *widens* it to ~1400
  lines spanning render + custody — the opposite of the pattern's intent (each file
  is one graspable job).
- **man/install.** Each has its own `man/*.1` and its own symlink from `install`.
  There's no shared-install pain to relieve — `install` already loops over every
  CLI generically. Merging would collapse two clear man pages into one that has to
  document two unrelated jobs.

### Cost of merging vs cost of the seam staying

- **Cost of the seam today:** ~5–15 duplicated lines (`takeValue`, a path
  one-liner). That's the entire ongoing tax. It has never diverged meaningfully
  because it's trivial.
- **Cost of merging:** couple a schema-immune preserver to a fragile parser;
  double the file's surface; blur two verbs ADR 0006 deliberately separated; merge
  two disjoint CLI vocabularies and two man pages; and put scheduled unattended
  writes in the same binary as an interactive viewer. High cost, negative benefit.

### What the repo's own PRINCIPLES say

`PRINCIPLES.md §2` cuts against the merge on three of four bullets and barely for
it on the fourth:

- **KISS** — "when two designs work, ship the smaller … don't add accidental
  complexity to an already-complex system." Two small single-purpose files *are*
  the smaller design here.
- **Loose coupling** — "components talk through narrow contracts, not shared
  internals … not merged into a monolith." Directly the federation case.
- **Unix philosophy** — "do one thing well; compose small sharp tools." observe and
  preserve are two things.
- **DRY** — the only bullet pointing toward dedup, and with ~10 shared lines it has
  almost nothing to bite on. DRY is about *authoritative homes for facts/logic*,
  not about co-locating 4-line helpers.

### Middle path

If the shared surface ever grows (e.g. Q1's tool-result capture makes ccarchive
learn more about session-directory structure, or a future `--source <archive>`
lets the observers read `.jsonl.gz`), the right move is a **tiny shared library
file** (`cclib` — session-location + `.jsonl` discovery primitives), *not* a full
merge. But today, at ~10 duplicated lines, extracting a library would **add** an
install/require seam between two currently self-contained zero-dep files to save
almost nothing — DRY's own cost/benefit says leave it. Reassess if shared code
crosses ~40–50 lines or starts diverging.

### 🎯 Recommendation for Mike — Q2

> **Keep them separate. Do not merge.** The premise (shared work) doesn't survive
> measurement — genuine duplication is ~10 lines. The purposes are two of ADR
> 0006's four verbs (observe vs preserve), and merging would couple ccarchive's
> best property — schema-immunity guarding the only durable copy — to
> cctranscript's schema-fragile parser. KISS, loose coupling and Unix philosophy
> all point the same way; DRY has nothing to bite on.
>
> **Middle path if it ever grows:** a small shared `cclib` for
> session-discovery primitives — but only once shared code crosses ~40–50 lines.
> Not now.

**Honest counter-case (the strongest form of the merge argument):** the two are a
natural *pair* in use — you archive with one and read the archived file with the
other (`gunzip … | cctranscript`), and ADR 0006's own seam note flags an open
sourcing gap (observers read the live `.jsonl`, not the `.jsonl.gz` archive). One
could argue a single `cc` tool with `archive`/`show` subcommands would make that
pipeline seamless and give one install/man story. That's the real pull — but it's
an argument for a **thin shared seam or a `--source <archive>` flag on the reader**,
not for fusing the custody engine and the renderer into one binary. The pairing is
a *pipeline* relationship (compose small sharp tools), which is precisely what the
Unix bullet says to keep as two tools joined by a contract, not one monolith.

---

## Deliverables & state

- This record: `docs/sessions/2026-07-22-1050-cc-instruments-questions.md`.
- No instrument code changed (analysis item).
- Two 🎯 recommendation blocks above are the actionable outputs; both defer the
  actual decisions to Mike.
