# Cold review — lean current-truth files: `sizescan` + RECORD.md roadmap doctrine

**Scope:** commit `47c5ea6` (2026-07-14) — `tools/sizescan.py` + `test_sizescan.py`,
`method/RECORD.md` § "The roadmap" (the current-truth/history split, the growth
dynamic, the harvest-at-close trigger), `tools/README.md` § sizescan, and the
dogfood harvest (`docs/ROADMAP.md` 1091 → 180, `docs/ROADMAP-DONE.md` created).
Review gates wiring `sizescan` into any gate (`ci.yml` / child `floor.yml`
`--check`).

**Reviewer:** Fable, fresh session 2026-07-14; not the author (work authored by
an Opus session, 2026-07-14-1948). Un-briefed pass — no author brief exists.

**Independence note, stated honestly:** the author's four seeded questions live
*inside the ROADMAP queue item itself* (budget defensibility, root-only masking,
line-count-as-proxy, advisory toothlessness), so the reviewer read them at
selection time — they could not be structurally deferred. Mitigation is this
section: the attack surface below was drawn up and committed from the reviewer's
own reading of the code, tests, and doctrine *before* the seeded four are
reconciled; the reconcile happens in the verdict, after. Rule 3 applies
regardless: the doctrine under review is agent-authored, so findings on it are
the principal's to decide, not any agent's.

## Attack surface (reviewer's own, committed before verdict)

Lens 1 — approach & assumptions:

- **A1. Basename-keyed budgeting** assumes the fleet's conventions are the
  world's — a roadmap named `TODO.md`/`BACKLOG.md` is invisible. Acceptable for
  a house tool; is the narrowing stated?
- **A2. The tool has no firing point yet** — the exact no-trigger decay it was
  built to fix. Not in the read order, not in the hook, not in CI. Does the
  doctrine's real trigger (harvest at session close) carry the weight until
  wiring, and is advisory-in-CI a signal anyone will ever see?
- **A3. The append-only SESSIONS index is budgeted as current-truth.** RECORD.md
  says the index is *never rewritten*; sizescan says it must stay ≤250 lines.
  What is the prescribed fix when an already-split index outgrows its budget?
  (atelier's is 75 lines after ~5 days of sessions — this is near-term, not
  hypothetical.)
- **A4. Excluding the growth stores** is right (don't punish the destination),
  but confirm the residual is honestly stated somewhere a reader will meet it.

Lens 2 — correctness (code + record):

- **C1. Absolute-path skip check.** `iter_candidates` tests
  `SKIP_DIR_NAMES & set(p.parts)` on the *absolute* path. A repo checked out
  under any ancestor directory named `sessions`, `reviews`, `decisions`,
  `archive`, `_archive`, or `intake` (e.g. `~/archive/<repo>`) silently skips
  every file — a scan that read nothing reporting clean, the exact fail-open the
  tool's own docstring forbids. Reproduce it. Check whether the sibling
  scanners share the pattern.
- **C2. Whole-file marker matching.** `sizescan:allow` / `sizescan:budget=N`
  match anywhere in the text. A budgeted file that merely *mentions* the marker
  in prose (a roadmap item about sizescan budgets, a CLAUDE.md documenting the
  hatch) silently exempts or re-budgets itself. Per-file blast radius — blunter
  than the sibling scanners' per-line allows. Reproduce it; grep the budgeted
  files at HEAD for near-misses.
- **C3. Re-run every recorded proof:** 24 sizescan tests, the full suite
  ("240 tests OK"), `--selftest`, sizescan + linkscan clean on the harvested
  result, the fleet claim (sharp on ros 3197 / faves 1157, silent on healthy
  repos), and the harvest's **zero-checkbox-lost / verbatim-move** claim —
  verify mechanically against `47c5ea6^`, not by reading the assertion.
- **C4. Smaller checks:** `.sizescanignore` fnmatch `*` crosses `/` (gitignore
  it is not); rglob enumerates `.git`/`node_modules` before filtering (no
  prune); duplicate findings if overlapping paths are passed; explicit
  non-budgeted path scans nothing and prints clean.

Lens 3 — completeness / harvest:

- **H1. The harvest itself:** every checkbox item in the pre-harvest ROADMAP
  accounted for across the post-harvest pair; moved text verbatim; links in
  both files resolve; ROADMAP-DONE's framing doesn't contradict RECORD.md.
- **H2. What the work should have covered:** does the store hint for SESSIONS
  point at a fix that exists for an already-split index (ties to A3)? Does
  CHANGELOG's entry match what shipped? Is the not-wired state consistently
  stated everywhere it matters (code docstring, tools/README, ROADMAP)?

---

# Verdict — PASS-WITH-FINDINGS · 1 MAJOR · 2 MEDIUM · 1 LOW bundle

The mechanism is sound and the record is honest: every recorded proof
reproduced, the harvest is verified lossless, and the doctrine text says what
the tool actually does. The MAJOR is in the scanner's file-selection logic, not
in the doctrine. **Wiring `sizescan` into any gate stays blocked until F1 is
fixed** — a fail-open scanner behind a green CI badge is worse than no gate.

## Proofs re-run (all reproduce, 2026-07-14)

- Full suite: **240 tests OK** (`tools/ python3 -m unittest`); `sizescan
  --selftest` OK; worktree selftest OK.
- `sizescan` and `linkscan` **clean on the harvested repo** at HEAD.
- **Zero-loss harvest verified mechanically** against `47c5ea6^`: all **94**
  pre-harvest checkbox lines present across the post-harvest pair (16 kept in
  `ROADMAP.md`, 83 in `ROADMAP-DONE.md`, 5 items new that session); every
  `ROADMAP-DONE.md` line except its 13 header/framing lines is **byte-verbatim**
  from the old file. "Preserved verbatim, zero lost" holds.
- **Fleet claim re-run**: ros `ROADMAP.md` 3317 (+3017, grown since recording —
  the 3197 figure was true at its time), faves SESSIONS 1157 / ROADMAP 766 /
  ARCHITECTURE 276, shed SESSIONS 255 (+5); atelier clean. Matches the record.

## Findings

### F1 · MAJOR (code) — ancestor-named directory silently blanks the whole scan

`iter_candidates` tests `SKIP_DIR_NAMES & set(p.parts)` on the **absolute**
path. The default invocation (`sizescan`, root resolved absolute) and the fleet
form (`--root <abs> <abs>`) therefore skip **every file** when any ancestor
directory of the repo — not just a directory inside it — is named `sessions`,
`reviews`, `decisions`, `archive`, `_archive`, or `intake` (e.g. a checkout
under `~/archive/<repo>`). **Reproduced:** a 400-line `docs/ROADMAP.md` under
`…/archive/myrepo` reports *"✓ sizescan clean"*, exit 0; the identical repo
under `…/ctrl/myrepo` flags (+100). Relative invocation (`--root . .`) behaves
correctly — the bug is invocation-inconsistent as well as fail-open, and it
violates the tool's own contract ("a scan that read nothing is NOT a pass",
exit 2 for a typo'd path — this is the same defect class with a worse
symptom: a *clean* verdict).

**Fix shape:** test skip names against the path **relative to the scanned
base** (`p.relative_to(base).parts`), and pin it with a test that scans a repo
under a store-named ancestor. **Related residual:** all four sibling scanners
share the `set(p.parts)` idiom, but their skip names (`.git`, `node_modules`,
`venv`…) are implausible ancestors; sizescan's added store names are ordinary
English words — the practical hazard is sizescan's, the idiom is shared.

### F2 · MEDIUM (code design) — a prose *mention* of a marker exempts the file

`sizescan:allow` and `sizescan:budget=N` match **anywhere in the file's text**.
A budgeted file that merely mentions a marker in prose silently exempts or
re-budgets itself — **reproduced both ways** (a roadmap item reading "set an
inline sizescan:budget=9999 on the ros roadmap when harvesting" made a 400-line
ROADMAP scan clean; same for a prose `sizescan:allow` mention). This is blunter
than the sibling scanners' allows, which are per-line — there a prose mention
exempts only its own line; here it exempts the whole file. The tool's own
report text invites writing exactly this prose into a roadmap item ("add
'sizescan:budget=N' inline…"). No near-miss existed at HEAD when grepped — and
then this review's own ROADMAP status paragraph quoted the allow marker
literally and silently exempted the ROADMAP itself, caught only because the
reviewer re-checked before committing. The trap fired on the first person to
walk past it, same day.

**Fix shape (code-owner's pick):** require the comment form
(`<!-- sizescan:budget=N -->`) or restrict markers to the first ~10 lines; at
minimum, document the footgun beside the hatch instructions.

### F3 · MEDIUM (doctrine — the principal's per rule 3) — the SESSIONS budget collides with the append-only rule, and the store hint has no move to offer

`RECORD.md` § session log: *"`SESSIONS.md` is an append-only index — never
rewritten; history is not edited."* `sizescan`: `SESSIONS.md` ≤ 250, hint
*"move to a one-line-per-session index + docs/sessions/ detail files."* For a
flat log the hint is right. For an index that is **already split** the budget
will trip and the doctrine offers no sanctioned move — the only fix it names is
the one the file has already done. This is near-term, not hypothetical:
atelier's index is 75 lines after ~4 days (≈19/day → over budget in about two
weeks of this cadence); shed's is over **today** (+5), and shed's log is
flat-by-declared-design, so its sanctioned answer is an allow-marker — a hatch
doing a policy's job.

**Options for the principal:** (a) prescribe **index rotation** — the recent
tail stays in `SESSIONS.md`, older lines relocate verbatim to a
`SESSIONS-ARCHIVE.md` growth store; "append-only" sharpened to *append-only
content, relocatable home* (relocation-never-deletion, the same shape as the
roadmap harvest); (b) exempt already-split indexes from budgeting (but sizescan
cannot tell split from flat — this collapses to per-repo allow-markers);
(c) raise the budget (defers the collision, doesn't resolve it).
*Reviewer's counsel, labelled as such:* (a) — it is the existing
current-truth/history pattern applied to the index itself, and it keeps the
budget meaningful.

### F4 · LOW (bundle, code)

- `.sizescanignore` fnmatch `*` crosses `/` — a `*.md` glob ignores every
  markdown file in the repo (gitignore intuition says one level). Over-ignore
  risk only; consistent with the sibling scanners' globbing.
- `rglob("*")` enumerates `.git`/`node_modules` fully before filtering — no
  traversal prune; perf only, tolerable at fleet sizes.
- Overlapping positional paths (`sizescan . docs/`) double-report a finding.
- First `sizescan:budget=` match anywhere wins (subsumed by F2's fix).

## The seeded four, reconciled (opened after the attack surface was committed)

1. **Budgets defensible or arbitrary?** Defensible as grounded heuristics: the
   fleet's healthy files sit well under, the offenders clear them by multiples,
   and the stated value is *signal + hatch*, not a tuned threshold. One
   interaction: the SESSIONS 250 figure is entangled with F3 — the number is
   fine; what's missing is the sanctioned move when an index trips it.
2. **Root-only README/CLAUDE masking reference-doc bloat?** No change owed. A
   nested README is genuinely read-on-demand; its growth is a different cost
   class, and the residual is stated honestly in `tools/README.md`. (That file
   itself is 434 lines and grows linearly with the tool count — on-demand, so
   out of sizescan's scope by its own design, correctly.)
3. **Line-count an honest proxy?** Yes, as framed: it claims to proxy the token
   cost of always-loaded files, not bloat itself, and the "cannot tell padded
   from dense" residual is already stated where a reader will meet it.
4. **Advisory exit-0 toothless?** Half-true. Advisory output in CI is a log
   line nobody reads, so as a *mechanism* advisory mode alone would recreate
   the no-trigger decay. But the design doesn't lean on it alone: RECORD.md's
   harvest-at-close trigger is the working mechanism, and `--check` is the
   intended tooth. *Reviewer's counsel on wiring (gated on this review, the
   principal's call):* after F1 is fixed — atelier `ci.yml` in `--check` mode
   now (repo is clean, hatches exist); children stay unwired until their
   harvest backlog clears (ros and faves would red instantly), then `--check`
   in `floor.yml`.

## Disposition

All findings go to **Mike** to decide ([fixed]/[backlog]/[rejected]): F3 is
doctrine and rule 3 makes it his outright; F1/F2 sit in a scanner whose budgets
and skip-lists are policy-as-code destined for a gate, and the author isn't
present to take the ordinary code-owner path — so the whole set is handed up
rather than split. The reviewer applied nothing.

**Close-rule reminder:** F1's fix needs its own live re-proof (re-run the
`archive/`-ancestor reproduction) before the wiring item unblocks.
