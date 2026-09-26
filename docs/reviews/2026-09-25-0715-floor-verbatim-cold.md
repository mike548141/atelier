# Cold pass — the floor is copied verbatim — one doctrine change and the scanner half that enforces it

**Pass type:** doctrine + code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-09-25 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/340-rule-4-cold-pass-queued-the-floor-verbatim-ruling.md`.
**Why it earns a review:** the rule decides what a child may and may not change
in the doctrine block it inherits, and the scanner reds every child whose block
differs; a wrong identity test either lets a narrowed floor pass or reds every
child in the fleet at its next pin bump.

## Spawn provenance

- **Author of the work under review:** the session(s) that landed the commits
  named under *What the work is*. This brief-writer was not that session, was
  neither started nor instructed by it, and has edited none of the delta's
  paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-09-20 and
  re-pointed on 2026-09-24 with the prompt "Please deliver all fable dependent
  work, and work that would be best delivered using fable", on the Fable tier
  (`claude-fable-5-1`), orchestrating this batch of twenty rule-4 passes. It
  wrote this brief from the queue pointer, the landing commits' subjects and
  file lists, and the delta paths' names; it did not open the intent record or
  any prior verdict on these surfaces.
- **Who takes the review:** a fresh Fable subagent (`claude-fable-5-1`) spawned
  by the brief-writer with this brief as its only framing. It is not the
  author's session and was not instructed by the author. The reviewer repeats
  its own provenance in the verdict.
- **Orchestration shape, disclosed per rule 4:** reviewer-plus-orchestrator. The
  orchestrator holds the `.deferred.md` sibling outside the worktree, commits
  the reviewer's phase-1 findings unrevised, then releases the sibling's text by
  message; the reviewer appends a reconcile section; the orchestrator folds the
  sibling in and updates the pointer. The orchestrator forms no finding and
  writes no severity. Both seats are Fable, so the off-tier clause is not
  invoked; the shape is stated anyway so the record is auditable.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material it met before
  writing): the `docs/SESSIONS.md` index entries of 2026-09-11 to 2026-09-19
  (the last three summarise the 2026-09-18 and 2026-09-19 runs in the authors'
  words); the first 30 lines and the last ~3,000 characters of
  `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md`, read during an
  interrupted-session sweep on 2026-09-20; every queued `⏳` pointer on the board
  in full, including each pointer's own "lens that matters" paragraph — that
  paragraph is the author's framing and has been moved to this pass's sibling;
  the pass file `docs/reviews/2026-08-17-1000-coldsweep-cold.md` in full (brief
  and verdict) and lines 1–80 of
  `docs/reviews/2026-08-21-0820-pointing-up-cold.md`, both as formatting
  templates; the landing commits' subjects and `--stat` file lists (never the
  diffs); and, as doctrine read at onramp, `docs/method/CONCURRENCY.md` §§ *On a
  split board*, *Claiming at a dirty primary checkout* and *Surviving an
  interrupted session*, `docs/method/REVIEW.md` and `docs/method/00-APEX.md` at
  HEAD. Per-pass additions are marked ⚠️ under *Deferred reading*.

## What the work is

Landing commits (diff these; review the paths at HEAD):

- `f0ddeb0` (2026-09-20) — the doctrine half
- `f706bde` (2026-09-20) — the scanner half (`stampscan` reds `narrow=` on the
  atelier floor)
- ⚠️ `3d73e49` and `db9a785` (2026-09-20) — later, separately-queued work
  (`160/370`, `160/410`) converted `stampscan` to stream and to prune linked
  worktrees. Review the floor branch as it stands at HEAD

Delta paths:

- `docs/method/PROPAGATION.md` — the fourth boundary bullet in § *The standard
  child doctrine block*; the *may compress* sentence beneath it; the carve-out
  in § *One statement, stamped copies — never three originals*
- `tools/stampscan.py` — `FLOOR_SOURCE` / `FLOOR_REGION`, `_is_floor_block`, the
  floor branch in `evaluate_block`, the module header section, the selftest
  cases
- `tools/test_stampscan.py`

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether the identity the scanner uses for "the floor" — a `source=` string and a
region name — is the identity the doctrine means, and what slips it: a child
that renames the source, stamps a second copy of the region, stamps the region
under a different marker, or carries the block with a trailing-whitespace or
line-wrap difference. Whether the doctrine now reads consistently about who may
compress what (the *may compress* sentence beside a *verbatim* rule is the
tension to test). Whether the scanner's verdict is inverted anywhere (the board
records a prior inversion class for this tool — form your own view from the code
first). **Non-goal:** the ruling itself (`115/030`).

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself.
   "Verbatim" presumes the canonical region is stable enough that every child
   can match it byte-for-byte at its pin — test that against how often the
   region has changed since 2026-08-25 (`git log -L` on the region) and what a
   child sees between pin bumps.
2. **Correctness & quality.** Read all of `stampscan.py`. Run `--selftest`; run
   the tool over a scratch child carrying each variant in *Scope* and record the
   verdict for each. Check `_is_floor_block` cannot be satisfied by a block that
   only *mentions* the source string.
3. **Completeness / harvest.** Every other surface that tells a child what it
   may change in the block: `docs/build/templates/CLAUDE.md`'s own comments,
   `skills/create-repo/SKILL.md`, `docs/build/REPO-STANDARD.md`,
   `tools/README.md` § stampscan. Does the template's block *itself* pass the
   scanner at HEAD?
4. **Security & privacy** — mandatory. The scanner reads child repos'
   `CLAUDE.md`. Check it cannot be made to read outside the declared root by a
   crafted `source=` path, and that its output never prints file contents beyond
   the marker line. Discharge the house scanner by grounds in one line.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 tools/stampscan.py --selftest`; `python3 -m unittest
  tools.test_stampscan`; the full Python suite once
- the scanner over this repo's own template and over a scratch child for each
  variant in *Scope*
- the floor on both planes at HEAD

## House rules for this run

- You work in the shared review worktree
  `/Users/mike/worktrees/atelier-review-batch-0925` (branch
  `review-batch-0925`), read-only except for THIS brief file. Other reviewers
  are working there at the same time on their own briefs; never open another
  `docs/reviews/2026-09-25-0715-*` file — it is another pass's framing.
- Run **no git command that writes** in the worktree (no add, commit, stash,
  checkout, worktree, reset, clean). Read-only git (`log`, `show`, `diff`,
  `blame`, `branch -r`) is fine. Mutation probes, checkouts of older commits,
  scratch children and scratch linked worktrees go in your own clone: `git clone
  <worktree> <scratchpad>/<PREFIX>/probe` under the session scratchpad, named by
  your prefix so parallel reviewers do not collide.
- One heavy process at a time on this machine: run the full Python suite
  (`python3 -m unittest discover -s tools`, in the foreground, ~minutes) at most
  once, never scan any tree outside the worktree or your scratch clone, and
  never point a scanner at the machine's other repos.
- `/security-review` is **discharged by grounds** for this batch: it reads the
  session's pending diff, which in the shared worktree is other passes' unstaged
  drafts, and this is a landed-delta review. State that line in your lens-4
  answer and deliver the code-altitude read by hand, checked against the OWASP
  catalogue where the work has a code surface.
- Dates in your verdict are absolute ISO-8601 from `date -u` (the hook-plane
  `datescan` reds relative words such as "yesterday" or "next week" tree-wide,
  and would block the orchestrator's commit). Wrap prose at ≤ 100 columns. NZ
  English. Never quote a secret, a placeholder token, an email address or any
  personal detail — this repo is PUBLIC; describe, don't quote.
- Review deep, not fast. A finding needs a probe or a re-driven claim behind it,
  not reasoning alone; a clean lens needs the trail that earned it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held by the orchestrator outside the worktree under the rule-1 split and released only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/340-rule-4-cold-pass-queued-the-floor-verbatim-ruling.md`
(it carries the author's own lens hints), and:

- `docs/sessions/2026-09-19-0038-queue-run-the-morning-rulings.md`
- the board items `docs/roadmap/115-*/030-*.md` and any
  `docs/roadmap/*/…stampscan-s-verdicts-are-inverted…`,
  `…narrowed-floor-and-now-reds…` items

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-batch-0925 --also-exclude
docs/roadmap/160-doctrine-review-owed/340-rule-4-cold-pass-queued-the-floor-verbatim-ruling.md
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `FV`: `FV1`, `FV2`, …) and severities (MAJOR / MODERATE
/ minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger with the commands and their results, and a follow-up checklist.
Then STOP and report to the orchestrator that phase 1 is written. Do not open
the sibling (it is not in the tree); do not edit the queue pointer, the board,
or any file but this one.

**Phase 2.** On receipt of the sibling's text, append `### Reconcile` beneath
your verdict: per-finding notes against the seeded questions and the intent
records, any finding formed at reconcile marked as such, and the overall line
restated. Never revise phase-1 text. The orchestrator folds the sibling in below
your reconcile.

Findings on doctrine are the principal's to decide (rule 3): record all, apply
nothing; your counsel per finding is welcome, labelled as counsel and kept
beneath the finding.

---

# Verdict — phase 1, written 2026-09-25 07:30 UTC

## Provenance, repeated

- **Spawn.** A fresh Fable subagent (`claude-fable-5-1`), spawned by the batch orchestrator
  with this brief as its only framing. Not the author's session; neither started nor
  instructed by the author of `f0ddeb0` / `f706bde`. Reviewer-plus-orchestrator shape as the
  brief discloses; the orchestrator formed no finding. Tier checked at claim: Fable.
- **Where.** The shared review worktree at `c4b9cd0`, read-only; probes ran in a scratch clone
  of that worktree and in scratch children under the FV scratch area. No git command that
  writes was run in the worktree; the only file edited is this one.
- **Read (in scope).** This brief; `docs/method/REVIEW.md` and `00-APEX.md` at HEAD; the delta
  at HEAD (`tools/stampscan.py` whole, `tools/test_stampscan.py` whole,
  `docs/method/PROPAGATION.md` lines 95–265 and 815–845); `git show f0ddeb0 --
  docs/method/PROPAGATION.md` and `git show f706bde` (the two landing diffs); the `--stat` of
  `3d73e49` and `db9a785`; `.github/workflows/ci.yml` lines 170–240; `.githooks/pre-commit`;
  `tools/floor.py` (grep only); `.stampscanignore`; `.atelier-floor.json`;
  `docs/build/templates/CLAUDE.md` lines 1–120; `tools/README.md` lines 995–1056;
  `skills/create-repo/SKILL.md` lines 110–200; `docs/build/REPO-STANDARD.md` lines 125–140
  and 248–261; `tools/test_mixed_root.py` lines 1–63; `git log -L` subjects for the floor
  region; the OWASP Top 10:2025 category list (fetched).
- ⚠️ **Exposure, disclosed.** `git show f0ddeb0` prints that commit's message body, which is
  the author's own account: it names board items `115/200`, `115/210` and `160/340` and
  summarises each in one line. I read that body before forming findings. I did not open any
  board item, session record, prior verdict, `ROADMAP-DONE.md` or `SESSIONS.md`. No
  tree-wide sweep was run, so `coldsweep.py` was not needed: every grep was scoped to named
  files under `tools/`, `skills/`, `docs/method/PROPAGATION.md` and `docs/build/`.
- **Interpreters.** The machine's `python3` on PATH is 3.14.6 (a framework install ahead of
  `/usr/bin/python3` 3.9.6); CI pins 3.12. Re-runs below name which one ran.

## Assumptions named (lens 1 first act)

- **A1 — "verbatim" is a per-line byte identity** (trailing whitespace ignored, boundary
  blank lines trimmed). The doctrine says "word for word". The two differ on a re-wrap.
- **A2 — the floor's identity is the spelling `docs/method/PROPAGATION.md` + `floor`.** The
  doctrine's identity is "the `floor` region of PROPAGATION.md" — a file and a region.
- **A3 — the canonical region is stable enough for children to match it at their pin.** The
  doctrine does not say *at which SHA* a copy must be verbatim.
- **A4 — something runs the scanner over a child's block.** The brief's *Why it earns a
  review* rests on "the scanner reds every child whose block differs".
- **A5 — `narrow=` is the only excuse the floor could be given.** `stampscan:allow:` is the
  other one.

## Per-lens answers

### Lens 1 — approach & assumptions

A1 holds in the fail-safe direction: a word-identical re-wrap reds (`v11`), so the scanner is
stricter than the prose, never looser (FV7). A2 is where the delta is weakest: the identity
is a string compare on the attribute as written, and four in-root spellings of the same file
each pass a declared narrowing of the floor clean (FV1). A3: the region has changed 27 times
since 2026-07-10 and twice since 2026-08-25 — `a134270` and `54201e0`, both 2026-09-18, 86 →
91 lines. A child verbatim at a pre-2026-09-18 pin reads `drift` against HEAD (`v17`), the
same kind a reword gets; that is ST3, a documented open residual the delta neither widened nor
closed, but bullet 4's "word for word" is silent on *at which SHA* (FV8). A4 is false as a
mechanism (FV3). A5 is false (FV2).

The doctrine's internal consistency — the brief's stated tension — is clean at HEAD: the
*may compress* sentence (PROPAGATION.md lines 240–245) now attributes compression to
atelier's canonical text and verbatim to the child's copy, and the § *One statement* bullet
(lines 832–836) carries the matching carve-out. The heading count above the boundary list did
not keep up (FV4), and bullet 4 keys the rule on a region *name* where the scanner keys on a
pair (FV5).

### Lens 2 — correctness & quality

Read all 1,332 lines of `stampscan.py`. The floor branch sits inside the ordered-subsequence
branch, after the empty-payload check and before the generic `narrow` pass; order is right
(empty first, because the empty list is a subsequence of everything). `_is_floor_block` is
a parse-based pair compare on `StampBlock.source` / `.region`, so a payload line that merely
*mentions* the pair string cannot satisfy it (`v13`: `is_floor=False`, kind `narrow`); a
second `stamp:begin` inside a payload is a nested-stamp `malformed` config error, not a
match. **No verdict inversion found**: exit codes probed 0 (`identical`, `narrow`,
`skipped`), 1 (`drift`), 2 (`missing-region`, `malformed`, `unconfined-source`), and `--warn`
downgrades drift only (selftest plumbing, re-run). The JSON `clean` field agrees with the
human verdict in every probed case.

Twenty-four scratch children were built from the *real* region at HEAD (91 lines) and
scanned from their own root and, for five of them, in the mixed-root fleet-check shape
(`--root <atelier> <child>/CLAUDE.md`), which resolves correctly:

| case | shape | exit | kind |
|---|---|---|---|
| v01 | verbatim copy | 0 | identical |
| v02 | exact pair, `narrow=`, genuine subset | 1 | drift (floor message) |
| v03 | `source=./docs/method/PROPAGATION.md`, `narrow=`, subset | 0 | **narrow** |
| v04 | `source=docs/build/../method/PROPAGATION.md`, same | 0 | **narrow** |
| v05 | `source=docs//method/PROPAGATION.md`, same | 0 | **narrow** |
| v06 | `source=docs/method/propagation.md` (APFS, case-insensitive), same | 0 | **narrow** |
| v07 | two stamps: verbatim + narrowed | 1 | identical, drift |
| v08 | two stamps, both verbatim | 0 | identical ×2 |
| v09 | exact pair, subset, `stampscan:allow:` line inside | 0 | **skipped** |
| v10 | trailing spaces and tabs on every line | 0 | identical |
| v11 | word-identical re-wrap of one line | 1 | drift |
| v12 | child's own `docs/FLOOR.md` copy as `source=`, `narrow=` | 0 | **narrow** |
| v13 | other source, payload mentions the pair string | 0 | narrow |
| v14 | the block with no markers at all, narrowed | 0 | (no findings) |
| v15 | `region=Floor` | 2 | missing-region |
| v16 | `narrow= ` (blank reason) | 1 | drift (silent drop) |
| v17 | verbatim at the pre-2026-09-18 region | 1 | drift |
| v18 | CRLF line endings | 0 | identical |
| v19 | UTF-8 BOM | 2 | malformed |
| v20 | `docs/method/PROPAGATION.md` is a symlink out of root | 2 | unconfined-source |
| v21 | `narrow=` + subset + re-wrap | 1 | drift |
| v22 | verbatim + allow marker on the begin line | 0 | skipped |
| v23 | exact pair, `narrow=`, payload byte-equal | 0 | identical |
| v24 | NUL byte inside `source=` | 1 | uncaught `ValueError` |

Bold rows are the slips. Tests are a faithful pin of the *string* identity the code
implements (`FloorIsVerbatim`, the two end-to-end `ScanPaths` cases, two selftest cases); none
exercises a spelling variant, the allow marker on the floor, or a narrow on a byte-equal
copy, so they pass while FV1, FV2 and FV5 stand.

### Lens 3 — completeness / harvest

The template's own block passes at HEAD (`identical`, 91 lines, exit 0 with and without
`--warn`). Of the surfaces that tell a child what it may change in the block, none carries
the new rule: `tools/README.md` § stampscan still says "or *legitimately narrow* it, declared"
and lists two boundaries; the template's guidance comment and `create-repo` step 5 say
"stamped copy, not a second source" / "don't paraphrase it" but never "never `narrow=`"
(FV6). More important: nothing automated reaches a child's block at all — the ruling's
scanner half enforces it on atelier's own template only (FV3).

### Lens 4 — security & privacy

`/security-review` is **discharged by grounds**: it reads the session's pending diff, which in
the shared worktree is other passes' drafts, and this is a landed-delta review. Threat
enumeration for the work's class, checked against OWASP Top 10:2025 (fetched 2026-09-25):
**A01 Broken Access Control** (path traversal via `source=`) — ST4 confinement holds:
`../`, an absolute path (selftest, re-run) and an in-root symlink resolving outside root
(`v20`) all exit 2 with nothing echoed; **A05 Injection** — no shell, `eval`, or SQL sink;
`source=` reaches `open()` only after confinement; **A09 Logging failures** — the drift hint
echoes one child line and one canonical line (`_first_offending_line`, `{ln!r}`), so "never
prints file contents beyond the marker line" holds only as *never more than one line of each
in-root file*; the floor-narrow branch prints counts only; **A10 Mishandling of exceptional
conditions** — a NUL byte in `source=` escapes the `OSError` catch and tracebacks (FV9): not
a silent pass, but exit 1 rather than the fail-safe 2. The scanner reads only Markdown under
the given paths and the resolved in-root source; `.stampscanignore` globs must carry a
reason (`IgnoreFileError`, exit 2). No personal data surface. Design altitude: the allow
marker is the one exemption that reaches the floor and it is undocumented as such (FV2).

## Findings

**FV1 — MODERATE — the floor's identity is a spelling, not a file.** `_is_floor_block`
compares `block.source` as written to `docs/method/PROPAGATION.md`. Four in-root spellings that
resolve to the same file (`v03`–`v06`) each pass `narrow=` on a genuine subset as a
legitimate `narrow`, exit 0, from the child's root and in the mixed-root shape. The
case-folded spelling passes on this APFS host and would exit 2 (`missing-source`) on CI's
Linux — the two planes disagree. Counsel: key the floor test on the *resolved* source
(`resolve_source(root, block.source)` equal to `(root / FLOOR_SOURCE).resolve()`, or
`os.path.samefile`), keep the region compare literal, and add the four spellings as tests.

**FV2 — MODERATE — the allow marker bypasses the verbatim rule, and the tool recommends it on
the floor's own red.** `v09`: exact pair, narrowed payload, one `stampscan:allow:` line →
`skipped`, exit 0. The human footer printed under the floor-narrow drift (`v02`) reads "add
`narrow=<reason>` to stamp:begin if the narrowing is deliberate" — the act the finding above
it just redded — and then "A deliberate exemption: append `stampscan:allow:` inside the
stamped block", a working bypass. PROPAGATION.md bullet 4 says `narrow=` reds "instead of
excusing anything" and is silent on allow. Counsel: (a) suppress the `narrow=` line of the
footer when any drift is on the floor pair; (b) the principal decides whether allow may
reach the floor — if yes, bullet 4 says so; if no, `evaluate_block` checks `_is_floor_block`
before honouring `block.allow`. Recurrence-prevention: a test that asserts the floor footer
never names the excuse it just refused.

**FV3 — MODERATE — enforcement reach is overstated; nothing automated reaches a child's
block.** `stampscan` is not in `tools/floor.py`'s registry (zero mentions), not in the child
`floor.yml` template, and not in `create-repo`'s prove-the-stamp step (a placeholder grep plus
`git log`). A child running it over its own root gets `missing-source` exit 2 (the template's
`source=` exists only in atelier — ST3); a child running it with no path argument scans
`docs/` and never reaches a root-level `CLAUDE.md` (`v02` default scope: no findings, exit
0); and an unstamped copy is invisible (`v14`). The only path to a child's floor is a
hand-run mixed-root invocation, which does work (`v02` → drift). So the brief's "the scanner
reds every child whose block differs" and `f706bde`'s "1 … will go red once this lands" are
true only under a hand run. Counsel: say so in bullet 4 and in `tools/README.md` (atelier
template + hand fleet check), and make the pin-aware child-side run the item that lets the
ruling bite.

**FV4 — minor — doctrine: "Three boundaries on that:" heads four bullets** (PROPAGATION.md
line 216 vs 218–238). Counsel: "Four boundaries".

**FV5 — minor — doctrine keys the rule on `region=floor` by name; the scanner keys on the
pair, and passes a `narrow=` that narrows nothing.** Bullet 4: "`narrow=` on a `region=floor`
stamp reds instead of excusing anything". The scanner deliberately matches the (source,
region) pair, so `region=floor` against the child's own copy (`v12`) or any other source
(`v13`) keeps the generic `narrow` pass; and `narrow=` on a byte-equal floor copy reads
`identical` (`v23`), not red. Counsel: word the bullet as "a stamp of PROPAGATION.md's
`floor` region" and either "a `narrow=` that narrows it reds" or make the scanner red any
`narrow=` on the pair — a two-line change that matches the ruling's wording literally.

**FV6 — minor — harvest: the child-facing surfaces don't carry the rule.** `tools/README.md`
lines 1009 and 1021–1022 (two boundaries, "or legitimately narrow it"); the template comment
`docs/build/templates/CLAUDE.md` lines 4–12; `skills/create-repo/SKILL.md` step 5. Counsel:
one clause each — "the floor is verbatim; never `narrow=`" — and README's boundary list
brought to four.

**FV7 — note — "verbatim" is stricter than "word for word".** A word-identical re-wrap reds
(`v11`, `v21`). Fail-safe and consistent with the sibling scanners; named so a child that
re-wraps to its own column limit is not surprised.

**FV8 — note — verbatim at which SHA?** Region changed 27 times since 2026-07-10, twice since
2026-08-25; a child verbatim at its pin reads `drift` against HEAD (`v17`). ST3 (documented,
unchanged by the delta). Counsel: bullet 4 says "word for word *at its pin*".

**FV9 — note (security, A10) — NUL in `source=` tracebacks, exit 1** (`v24`). Not a silent
pass. Counsel: catch `ValueError` beside `OSError` in `_main`.

**FV10 — note — by-design passes confirmed, recorded for the trail.** Trailing whitespace
and CRLF pass (`v10`, `v18`); BOM and case-variant region are config errors (`v19`,
`v15`); symlinked source out of root is `unconfined-source` (`v20`); two stamps evaluate
independently (`v07`, `v08`).

## Overall

**PASS-WITH-FINDINGS — 0 MAJOR, 3 MODERATE (FV1–FV3), 3 minor (FV4–FV6), 4 note
(FV7–FV10).** The delta does what it claims for the literal pair and every previously-red
shape stays red; what it under-delivers is the *identity* the doctrine means and the reach
the record claims for it. No MAJOR, so the cycle closes on this pass per REVIEW.md.

## Re-run ledger (all 2026-09-25 UTC, foreground)

| command | interpreter | result |
|---|---|---|
| `python3 tools/stampscan.py --selftest` | 3.14.6 | `selftest OK`, exit 0 |
| `python3 -m unittest tools.test_stampscan` | 3.14.6 | 90 tests, OK, exit 0 |
| `/usr/bin/python3 -m unittest tools.test_stampscan` | 3.9.6 | 90 tests, OK, exit 0 |
| `python3 -m unittest discover -s tools` (once) | 3.14.6 | 1,564 tests, OK, exit 0; 07:19–07:29 |
| `python3 tools/stampscan.py --root . .` | 3.14.6 | clean; 1 block identical (91 lines); exit 0 |
| `python3 tools/stampscan.py --warn --root . .` (ci.yml form) | 3.14.6 | same, exit 0 |
| `python3 tools/floor.py --plane hook --root . --tools tools` | 3.14.6 | exit 0; 12 ✅, 3 warn-only |
| `python3 tools/floor.py --plane ci --root .` | 3.14.6 | exit 0; secretscan 22 advisory; rest ✅ |
| `variants.py` / `probe2.py` over 24 scratch children (+5 mixed-root) | 3.14.6 | table above |
| `git log -s -L105,199:docs/method/PROPAGATION.md` | — | 27 commits; 2 since 2026-08-25 |

The 3.9 run of the stampscan suite was green here; I did not run the full suite under 3.9,
so this pass says nothing about the whole-suite-on-3.9 claim in `f0ddeb0`'s body.

## Follow-up checklist

- [ ] FV1 — resolved-path floor identity + four spelling tests (code; principal decides —
      it encodes doctrine).
- [ ] FV2 — footer suppression on the floor pair; allow-on-floor ruling; footer test.
- [ ] FV3 — bullet 4 and README state the real reach; child-side pin-aware run queued as the
      enabling item.
- [ ] FV4 — "Four boundaries".
- [ ] FV5 — bullet 4 names the pair; decide whether any `narrow=` on the pair reds.
- [ ] FV6 — README, template comment, SKILL step 5: one clause each.
- [ ] FV8 — "at its pin".
- [ ] FV9 — catch `ValueError` in `_main`.
- [ ] Phase 2 reconcile against the sibling and the barred items (`115/030`, `115/200`,
      `115/210`, the inversion-class item) — FV3 and FV8 may already be carried there.

### Reconcile — phase 2, written 2026-09-26 14:18 UTC

Phase 1 was committed unrevised (`d1ac3e0`, merged to `main` in `1109d49`) before the
sibling's text reached me. Opened after that, in this order: the sibling (by message); the
queue pointer `160/340`; `115/030` (the ruling, and the board's stampscan-inversion item —
they are the same file); `115/200`; the intent record
`docs/sessions/2026-09-19-0038-queue-run-the-morning-rulings.md` in full. Nothing above
this heading has been edited.

**The seeded question, answered.** The pointer's one lens hint asks whether the pair match
is the right identity — "a renamed doctrine file or a second copy of the region would slip
the check" — and whether the doctrine reads consistently about who may compress what.

- *A renamed doctrine file* (atelier renaming `PROPAGATION.md`): not probed by hand, but the
  code path is unambiguous — `resolve_source` returns `missing-source` before
  `_is_floor_block` is ever reached, exit 2, `--warn` or not. That direction fails loud. The
  slip is the **opposite** direction, which the hint did not name: the *child* respelling
  the source string (FV1). The hint's own phrase "stamps the same `source=` string" is the
  assumption FV1 falsifies — the string is what the child writes, not what the file is.
- *A second copy of the region*: two stamps in one child evaluate independently and slip
  nothing (`v07`, `v08`); a second copy of the region *as a different source* — the child's
  own `docs/FLOOR.md` — does slip (`v12`, FV5's evidence). A second `floor:begin` pair
  inside `PROPAGATION.md` itself was not probed; the module header names it first-wins.
- *Who may compress what*: consistent at HEAD (lens 1); FV4 and FV5 are the residue.

**Per finding, against the intent records.**

- **FV1** (spelling identity) — *not anticipated.* `115/030`'s DONE line and the session
  record both praise the worker's pair match for *not* sweeping in generic `floor`
  regions; neither asks whether the source half of the pair is a string or a file. This is
  the board's own **inversion class returning through a side door**: `115/030` defines the
  defect as "declares a narrowing and drops lines, passes clean" — `v03`–`v06` are exactly
  that, one `./` away. The ruling closed it for the literal spelling only.
- **FV2** (allow marker; footer recommends the excuse) — *not anticipated* anywhere: the
  ruling was offered against two alternatives (declared deletions visible-but-red; a
  renamed `omits=`), and `stampscan:allow:` is in none of the three. Not ruled, not
  rejected — undecided, so the principal's call stands as counselled.
- **FV3** (nothing automated reaches a child) — *partly anticipated, and the anticipated
  half is undelivered.* `115/030`'s owed list (3) reads "the fleet — a child whose floor
  copy is shortened goes red once … which `pins`/`floorfleet` should show before it
  surprises anyone"; its DONE line records (3) as a one-off read-only measurement, and
  `pins`/`floorfleet` carry no stamp check (grep, phase 1). `115/200` premises its red on
  "its next `stampscan` run", a run the child cannot make (`missing-source`, or nothing
  scanned under the default `docs/` scope); it then closed correctly on the child's own
  report via `320/360` / PR #83 — the child complied because a *person* measured, not
  because a scanner ran. FV3 stands; its severity is unchanged.
- **FV4** (three/four boundaries) — *not anticipated*; the DONE line says "gains a fourth
  boundary" and the heading was not swept.
- **FV5** (name vs pair; `narrow=` on a byte-equal copy) — *created at landing, visible in
  the record.* `115/030`'s DONE line states the scanner keys on the pair **and**, in the
  same paragraph, that "`narrow=` on a `region=floor` stamp reds" — the name-keyed
  sentence was carried into PROPAGATION.md verbatim. The record holds both wordings
  without noticing they differ. Not ruled either way.
- **FV6** (child-facing surfaces) — *not anticipated*; the owed list named doctrine,
  scanner and fleet, no harvest of README / template comment / SKILL.
- **FV7** (stricter than word-for-word) — *consistent with the ruling.* The session record:
  "Mike ruled the doctrine rather than the scanner … the exact-copy comparison becomes
  simply correct". A re-wrap redding is that ruling working; FV7 stays a note.
- **FV8** (at which SHA) — *anticipated in intent, absent in text.* `115/030` (3) and
  `115/200` both say "at its next pin bump", so the pin semantic was in the author's head;
  bullet 4 does not carry it. Counsel unchanged.
- **FV9**, **FV10** — *not anticipated*; not in scope of the ruling. Notes stand.

**The inversion item itself.** `115/030` documents the pre-ruling inversion (compression
red, declared deletion green). Phase 1 formed its view from the code first and found no
inversion in the *exit-code* sense; on the *doctrine* sense the item defines, the
inversion is closed for the exact pair and open for any respelling of it (FV1) and for the
allow marker (FV2). The item's `[x]` is right for what it owed; FV1/FV2 are the residue,
not a reopening.

**The session record's suite-on-3.9 claim** ("red on this machine, green in CI",
`115/210`): my 3.9 run of `tools.test_stampscan` was green (90 tests) — the three named
modules are evidently not among stampscan's imports, or were fixed between 2026-09-19 and
2026-09-25. I ran the full suite once, on 3.14 only, so this pass neither confirms nor
denies the whole-suite claim; recorded as unverified, not as contradicted.

**Finding formed at reconcile.**

**FV11 — minor (formed at reconcile) — the fleet leg of the ruling is recorded as done
on a measurement, while its own wording owes an instrument.** `115/030` owed (3) as
"`pins`/`floorfleet` should show [a shortened floor] before it surprises anyone" and closed
it with a one-off read-only count; `115/200` closed on the child's report. Both closures
are honest about what happened, but the instrument the owed line named does not exist,
and nothing on the board I opened carries it. Counsel: either a `floorfleet` column that
runs the mixed-root stampscan over each child's `CLAUDE.md` against the atelier checkout
at the child's pin (which is ST3's pin-aware story, and would discharge FV3 and FV8
together), or a line in `115/030` saying the fleet leg is a hand check until ST3 lands —
the principal's pick.

**Overall, restated:** **PASS-WITH-FINDINGS — 0 MAJOR, 3 MODERATE (FV1–FV3), 4 minor
(FV4–FV6, FV11), 4 note (FV7–FV10).** No MAJOR; the cycle closes on this pass per
REVIEW.md.

## Deferred material — folded in at reconcile

# Deferred material — floor-verbatim (open only after your findings are durably written)

Sibling of `docs/reviews/2026-09-25-0715-floor-verbatim-cold.md` under REVIEW.md
rule 1's split; held by the orchestrator outside the worktree. Folded into the
brief below the verdict when the verdict lands.

## Intent records

- `docs/sessions/2026-09-19-0038-queue-run-the-morning-rulings.md` — the run's
  account. **Not opened by the brief-writer**; index entry read at onramp.
- `docs/roadmap/115-*/030-*.md` — the principal's ruling that the floor never
  narrows. **Not opened.**

## Prior verdicts and barred items on the same surfaces

- `docs/sessions/2026-09-19-0038-queue-run-the-morning-rulings.md`
- the board items `docs/roadmap/115-*/030-*.md` and any
  `docs/roadmap/*/…stampscan-s-verdicts-are-inverted…`,
  `…narrowed-floor-and-now-reds…` items

## The queue pointer's own lens hints — the author's seeded questions, verbatim

**The lens that matters most here:** whether the pair match is the
right identity for "the floor" — a child repo stamps the same
`source=` string, but a renamed doctrine file or a second copy of the
region would slip the check — and whether the doctrine now reads
consistently about who may compress what.

## Brief-writer's seeded questions (a floor, never a fence)

Generate your own before reading these; a question you did not think of is a
prompt to re-read the surface, not an agenda.

None beyond the pointer's own.
