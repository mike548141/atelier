# instruments/ — open features

### Directory naming: `tools/` vs `instruments/` (Mike, 2026-07-24 — low priority, consider later)

Both dirs read colloquially as "tools," which blurs their real split: `tools/`
**enforces** (checks that gate a commit), `instruments/` **observe/extend** the
human+Claude collaboration. Swapping the two doesn't help — it just moves the
generic word onto the other pile. The fix is to make the *generic* name
descriptive. Recommendation: rename `tools/` → **`checks/`** (its own README
already calls them "the checks"); keep `instruments/` (distinctive, ADR-0006-
defended, carries the observe/measure sense). Alternatives for the enforcer dir:
`gates/`, `scans/`, `guards/`. Rejected: `pipeline/` (implies ordered data-flow
stages; the scanners are independent gates run as a set). Blast radius: live
wiring is small (CI `discover -s tools`, pre-commit hook, `.gitignore`, `*ignore`
files, README/CHANGELOG, cross-links); the ~128/63 file counts are mostly
immutable session logs/ADRs, left as-is. Mike's call, not the agent's to execute.

### cc-tools parameter vocabulary (Mike, 2026-07-23)

Strand closed 2026-07-23 (queue run): the flag-vocabulary audit found zero
drift (`85b17dd`, vocabulary table in `instruments/README.md`) and Mike
ratified **flags-follow-operation** as the adopted principle → detail in
[`ROADMAP-DONE.md`](../../ROADMAP-DONE.md).

### ccarchive (Mike, 2026-07-17)

Restore (full + delta), dataless awareness, and manifest signing all built
2026-07-22; the two open questions answered by measurement (tool-result
sidecar capture hole; keep-separate counselled) → detail in
[`ROADMAP-DONE.md`](../../ROADMAP-DONE.md), record
[`sessions/2026-07-22-1050-cc-instruments-questions.md`](../../sessions/2026-07-22-1050-cc-instruments-questions.md).
What remains is Mike's:

- **Metadata classes RULED 2026-07-23** (plain-language walk-through, the
  cc-instruments record's context relayed): tool-result sidecars **capture**;
  per-project `memory/*.md` **capture**; top-level `history.jsonl`
  **capture — Mike overturned the lean-exclude counsel** (wants the
  typed-prompt stream as a first-class artefact; grounds: his call, small
  cost). Signing defaults + keep-separate counsel **accepted as-is** —
  binary exits, new-machine red-until-key, two instruments; that 🎯 closes
  with no work owed.
- **ccarchive capture widened — BUILT 2026-07-23** (`3c6394d`, merged
  `2df595e`): all four ruled classes first-class end-to-end, exclusions
  now documented in a man-page CAPTURE section, 150 tests green. One
  operator note: the shrink guard covers memory files uniformly, so a
  legitimately condensed memory file needs `--force` — safe-over-silent.
  Detail → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md).
- **Capture the subagent `.meta.json` sidecar — BUILT 2026-08-09** (Mike
  ruled it a new capture class 2026-07-28). New `subagent-meta` class in
  `captureClass()`, scoped to `subagents/` rather than name-matched at any depth
  — the allowlist admits *known* classes and leaves the unrecognised out
  visibly, and the cost of the narrow choice is stated with it (if Claude Code
  moves subagent logs, the class silently goes empty, and only a whole-walk
  drift alarm exists). Restore mapping and manifest/integrity needed **no code**
  — structural consequences of keying on `<rel>.gz` — and were proved rather
  than reasoned. Tests 95 → 99, `mandoc -T lint` exit 0, no new flags.
  Every recorded figure was stale in the same direction (425 → 545 sidecars,
  66 KB → 85.8 KB) with the *shape* intact. →
  [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) § *The subagent metadata sidecar is
  captured*.
- **Backfill the sidecars — VERIFIED FREE 2026-08-09**, which is what the
  item asked for rather than a build. Confirmed two ways without mutating the
  real archive: the code path (`archiveOnce` rebuilds its work list from a full
  live walk every run; `shouldArchive` returns true on a null mirror), and a
  synthetic run where the sidecar appears with its mtime backdated a **year** and
  is still taken on the next plain run — the backdating being the load-bearing
  part, since it proves age is irrelevant. Count on the first run after the
  class landed: **545 sidecars / 87,883 bytes**. Both recorded limits hold — one
  sidecar is permanently gone, and `cleanupPeriodDays` 395 makes the decay
  roughly annual, which is real and not urgent.

### cctranscript (2026-07-26)

The header's summary line gained a **context size** and a **subagent count**
2026-07-26 (`19ef66d`, `2e8efb5`, `ae56b75`) → detail in
[`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) at next harvest. Open strands:

- **Search across transcripts — BUILT 2026-08-09** (Mike's ask, 2026-07-26;
      design pass 2026-07-27). Whole-file regex gate first so a miss is never
      parsed, UTF-8 throughout, `/i` case-folding, no index. Tests 38 → 62,
      `mandoc -T lint` exit 0, drift guard green, `--help` still inside its
      24-line pin. The design's **doctrinal loose end is closed**:
      `instruments/README.md`'s `--materialise` note argued the flag's *absence*
      from cctranscript was principled because it "never reads every file", and
      `--search` **is** the bulk read — so the note now states the
      flags-follow-operation rule in both directions and the table gains
      `--search`, `--since`/`--until` and `--top` as genuinely shared vocabulary.
      → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) § *cctranscript learns to search*.
      ⚠️ **DONE condition 13 is PARTIALLY met, and the design was wrong about
      why.** §4's "the refs are free" does not hold at file grain — an `N.M` ref
      counts every preceding turn, so parse-only-the-survivors and exact
      gate-invariant refs are mutually exclusive. Correctness was chosen, so a
      file passing the gate is parsed whole: a selective search runs at
      **1.22–1.32×** a bare read, but a term present in every session reaches
      **3.7×**. The wall-clock guard was replaced with a structural one
      (`meta.sessionsParsed`, test-pinned), which is what the 1.5× condition was
      really protecting. Five further design claims were corrected on contact and
      are recorded at the top of the design doc rather than edited out of it.

Two further strands stay open, both deliberately not built:

The **exact agent count** (started *vs* finished, unknown never printed as zero)
was built 2026-07-26 — and the archive-mode blocker recorded against it turned
out to be false, ccarchive having mirrored `subagents/` all along → detail in
[`ROADMAP-DONE.md`](../../ROADMAP-DONE.md). One strand opened by *using* it the same
day:


Two more surfaced by the search design pass (2026-07-27), neither its to fix:


### ccrepo (Mike, 2026-07-17)

Reconciliation drift closed 2026-07-22 (richest-record dedup; exact ccusage
match on frozen data); spend-config fill closed 2026-07-23 (populated from
real receipts, machine-local); archive sourcing (`--from-archive`, closing the
observe-side seam alongside cctranscript) closed 2026-07-23; the **rollup
precompute ledger** (`8a31b95`, 3.1× warm speedup, `rollup==recompute` proven
live, per-file keying, transparent-by-default confirmed by Mike) closed
2026-07-23 → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md); the **context-size column**
(`Context med/max` — per-session peak windows, median beside max, with the full
distribution in `--json`/`--csv`) closed 2026-07-26; the **`opus-5` price gap**
(found and closed the same day — see below) closed 2026-07-26. **Strand reopened
the same day**: Mike queued five v3 asks (below), one of which subsumes the dated
price-table watch and one of which answers the `-g session` question.

#### 🎯 v3 — five asks (Mike, 2026-07-26)

Build order is not ask order. (1) is a **correctness** change — every other
number ccrepo prints depends on it — and (5) is easier once (2)–(4) know what
flags they're adding, so: pricing → session dimension → context filter → sort →
CLI tidy. One of the five carries a decision that is Mike's, marked 🎯 inline.

The **time-bounded price table** (ask 1) landed 2026-07-26 (`7cf8163`, merged
`70bc1ad`) and the **`-g session` dimension** (ask 3) with it → detail in
[`ROADMAP-DONE.md`](../../ROADMAP-DONE.md). Ask 1 also **dissolved the dated
`sonnet-5` watch**: both rates are entered, each correct on its own side of
2026-08-31, so the section below is kept only for the reasoning. The three
open asks:

**v3 is COMPLETE** — all five asks landed 2026-07-26 (pricing intervals,
`-g session`, `--context`, multi-key sort + `--top`, sectioned `--help`) →
detail in [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md).

#### `-g session` — BUILT 2026-07-26 (v3 ask 3); grounding kept

**Shipped as a plain dimension**, so the shape question below is settled on that
side; `--top` remains open and travels with ask 4, where it belongs. Kept for how
the gap was found and why it was never a design defect — the past tense below is
the state before the build.

`session` was a **filter** (`--session <uuid-prefix>`) but not a **group
dimension**, so `Context med/max` could say a repo peaked at 529k without any way
to ask *which session that was*. Found by use, not by audit: a session asked for
per-transcript context sizes the day after the column shipped, and the answer
needed an ad-hoc script to rank individual sessions by peak — everything else in
the question ccrepo already answered better.

Not a defect. §5 makes `session`-as-filter deliberate, and §10 defers only
*synthetic-ordinal session numbers as filter keys*, which is a different thing —
grouping by session was simply never posed. The design's own "every group
dimension gets a filter" doesn't run in reverse.

**The open question is Mike's, and it is about shape, not worth:** grouping 420
sessions emits 420 rows, so this is only useful narrowed (`--repo x --since y`)
or ranked-and-truncated. Options: a plain dimension that trusts filters to keep
it sane · a `--top <n>` truncation that pairs with `--sort` · leave it out and
let ad-hoc scripts own per-session questions. Display labels would use UUID
prefixes; §5 already allows a synthetic `#n` as a label but never a key.

**Answered, same day:** Mike asked for it (v3 ask 3 above), which settles *worth*
— option three is out. The remaining choice is between a plain dimension and one
paired with `--top`, and it now travels with the sort ask, where `--top` actually
belongs. This block stays for the grounding — how the gap was found, and why it
was never a design defect.

#### ✅ `sonnet-5`'s introductory rate — watch RETIRED 2026-09-01-safe (2026-07-26)

**Both retirement conditions below are met.** The interval work landed
2026-07-26 (`7cf8163`), comfortably before the 2026-09-01 deadline that made this
a live safeguard, so the fallback flat-`3` edit is no longer needed and nobody has
to remember a date: `sonnet-5` now carries `$2` through 2026-08-31 and `$3` from
2026-09-01, each correct on its own side. **No action is owed on 2026-09-01.**
The block is kept for the reasoning, which generalises — a diary note is a
liability, and the fix was to turn it into data. Past tense from here:

`sonnet-5` was in the table at a flat **$2**/MTok input. That is Anthropic's
*introductory* rate, published as running **through 2026-08-31**; the standard
rate is **$3**. From 2026-09-01 ccrepo would have under-priced every sonnet-5
message by a third until the entry was changed to `3`.

This is a **dated edit, not a judgement call** — the number is published, so
there is nothing to decide, only something to remember. The ccusage cross-check
will catch it (the footnote will start showing a per-model sonnet-5 delta), but
a reconciliation alarm firing on a known, diarised date is a worse outcome than
just making the edit. Not pre-applied, because $2 is genuinely correct today and
changing it now would make ccrepo wrong for the next five weeks.

**v3 ask 1 dissolves this item rather than doing it.** Time-bounded prices let
both numbers be entered now, each correct on its own side of 2026-08-31 — the
diary note becomes data. Two conditions on retiring the ⏳: the interval work has
to **land** before 2026-09-01 (until then this stays the live safeguard), and the
flat `3` edit remains the fallback if it slips. A structural fix that arrives
late is worse than the one-line edit it was meant to replace.

Resolved, same session (2026-07-26) — kept for the reasoning, which generalises:

#### ✅ `opus-5` had no price — live totals understated (found + fixed 2026-07-26)

The price table carried `opus-4-8`, `fable-5`, `sonnet-5`, `sonnet-4` and
`haiku-4-5` but **not `opus-5`**, so every run printed `⚠ Unpriced model(s):
opus-5` and counted those messages at **$0** — 1,314 messages in one live drive.

Initially filed as needing Mike, on the grounds that a price must come from
Anthropic's published list and fitting one to observed cost would be inventing a
number. **Mike pushed back — the other prices came from somewhere, so why not
this one** — and he was right: the published list price was one lookup away
(`claude-api` skill → $5/$25 per MTok, same as `opus-4-8`). The escalation was
the error, not the caution. *The rule that survives:* never fit a price to your
own measurement; **do** go and read the published one. Those are different acts,
and only the first needed escalating.

Confirmed independently rather than assumed: with the entry added, the ccusage
cross-check moved to **Δ +$0.00 (+0.00%) across all 420 sessions**. The oracle
agreed to the cent with a number taken from the list, not fitted to the logs.

Completed instruments work (ccrepo actuals/breakdown, ccarchive integrity/audit,
the **man-page convention rollout — ccarchive worked example + cctranscript +
ccrepo, all installed CLIs now carry a `man/<tool>.1` + trimmed `--help`, closed
2026-07-21**) → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md).
