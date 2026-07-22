# Cold pass — harvest-integrity gate (delta `0bdccf3`)

- **Date/time**: 2026-07-22 0819 UTC
- **Spawn provenance (rule 4)**: taken from the ROADMAP `⏳` queue by a session
  Mike opened and pointed at the queue ("Please do any review work"). This
  session authored none of: the gate's design, the sizescan/test edits, the
  legend changes, or the intent record. The builder queued the `⏳` pointer and
  stopped; this brief is taker-written.
- **Named exposure**: at selection the taker read (a) the ROADMAP `⏳` pointer,
  (b) `0bdccf3`'s commit message — which carries the author's evaluative
  account ("all four of Mike's taxonomy situations covered", "Suite 302→314
  green", "live repo scan green") — and (c) `docs/method/REVIEW.md` in full at
  HEAD, needed to run the process. Every evaluative claim in (b) is treated as
  a claim to re-run, not a fact. **Deferred until this reviewer's findings are
  committed**: the intent record
  `sessions/2026-07-22-0634-harvest-integrity-gate.md`, and the follow-up
  records commit `2cd4730`'s narrative content. The residual exposure is
  named, not denied.

## What the work is (refs only)

Commit `0bdccf3` — sizescan gains a **harvest-integrity gate**: named archive
stores (`*-DONE.md`, `*-ARCHIVE.md`) must hold no live state markers
(`[ ]`/`[~]`/`⏳` list items). Checkbox grammar ruled tri-state. In-scope files
at HEAD:

- `tools/sizescan.py` — the gate implementation (+176/−24)
- `tools/test_sizescan.py` — `HarvestIntegrity` test class (+88)
- `docs/ROADMAP.md` — tri-state legend rewrite
- `docs/ROADMAP-DONE.md` — header updated to carry the gate's contract

This is **doctrine by function** (REVIEW.md rule 3): a CI gate that governs
future agent behaviour. Findings are the principal's to decide; the reviewer's
counsel below is labelled as such.

## Assumptions to attack (reviewer-named, lens 1 first)

- A1: "Archive stores hold no live state" is the right invariant — vs the
  risk that legitimate archive content *quotes* live markers (verbatim-
  preserved entries, code fences, narrative mentions of `[ ]`).
- A2: The store set (`*-DONE.md`, `*-ARCHIVE.md`) actually covers the
  archive surfaces this repo uses — and won't silently miss a store named
  otherwise (e.g. SESSIONS.md-style history, reviews/).
- A3: Line-based counting (parent/child fire independently) is sound — no
  double-fire or miss on nesting, continuation lines, or non-list `⏳`.
- A4: The tri-state ruling `[x] = no more work owed` is coherently carried
  by all three surfaces (scanner, legend, DONE header) with no drift.
- A5: The fail output's investigate-then-recommend prescription is
  actionable and cannot be discharged by a silent flip.
- A6: "State coherence only, never delivery verification" — the bound is
  actually held in code, not just claimed.

## Four lenses

1. **Approach & assumptions** — A1–A6 above.
2. **Correctness & quality** — does the gate do what the commit claims;
   re-run: full suite (claim: 314 green), `--selftest`, live `--check`.
3. **Completeness / harvest** — untested edge cases; sibling docs that carry
   the old `[-]` counsel or a stale legend; other archive stores unnamed.
4. **Security & privacy** — landed-delta review; `/security-review` scans
   pending diffs and excludes markdown, so there is nothing it can be aimed
   at here — discharged on those grounds, per REVIEW.md lens-4 reach rule.
   Manual pass instead: input handling of scanned file content (the gate
   reads repo files and prints excerpts — check for path/content injection
   into output or exit-code confusion).

## Non-goals

- Verifying that ticked `[x]` items in archives were actually delivered
  (Mike's explicit bound — delivery verification is out of the gate's scope,
  so out of this review's too; the *bound itself* is reviewed under A6).
- The two records commits either side of the delta (`b7b20b3`, `2cd4730`)
  except where they carry the tri-state legend the gate depends on.

---

# Verdict — PASS-WITH-FINDINGS (1 MAJOR, 3 MINOR, 2 notes)

- **Spawn provenance (restated per rule 4)**: reviewed by a session Mike opened
  and pointed at the `⏳` queue; the reviewer authored none of the work. This
  section was written and committed **before** the intent record
  (`sessions/2026-07-22-0634-harvest-integrity-gate.md`) or commit `2cd4730`'s
  narrative was opened; a reconcile note follows separately below.
- **Rule 3**: the gate is doctrine by function (policy-as-code, floor-embedded).
  Every finding below is **the principal's to decide**; reviewer counsel is
  labelled as such and nothing is applied by this session.

## Claims re-run (lens 2) — all reproduce

- ✅ **Suite 314 green** — `python3 -m unittest discover -s tools` → `Ran 314
  tests · OK`; the 302→314 arithmetic checks (12 new methods in
  `HarvestIntegrity`).
- ✅ **Selftest** — `sizescan --selftest` → OK, including the new archive cases
  (gate fires on buried `[ ]`, clean archive silent, prose/fence/backtick
  mentions inert).
- ✅ **Live repo scan green** — `sizescan --check` → exit 0; harvest-integrity
  clean. (One size-advisory on `ROADMAP.md`, 423 lines — advisory never gates,
  so "green" is honest.)
- ✅ **All four taxonomy situations** each have a dedicated test
  (`test_sizescan.py:342-373`) and behave as claimed — parent and child lines
  fire independently.
- ✅ **A6 bound held in code** — the gate counts markers only; nothing verifies
  `[x]` delivery.
- ✅ **Tri-state coherence (A4)** — ROADMAP legend, ROADMAP-DONE header,
  `sizescan.py` module doc, and the `_LIVE_ITEM` comment all carry the same
  work-owed tri-state; the superseded `[-]` counsel survives only in
  preserved-verbatim archive history, with its supersession noted in place
  (`ROADMAP-DONE.md:44`), and in the deliberately captured five-state open
  question (`ROADMAP.md:357`).
- ✅ **Hatches don't silence the gate** — budget override keeps the gate
  (suite + selftest); `allow` exempts wholly, header-only, as documented.

## Findings

### HI-F1 (MAJOR) — archive stores inside skipped directories are silently
### invisible to the gate

`iter_candidates` applies `_in_skipped_dir` before the archive-store branch, so
a store living inside any `SKIP_DIR_NAMES` component — `sessions/`, `reviews/`,
`decisions/`, `_archive/`, `archive/`, `intake/` — is never integrity-checked.
Reproduced: `docs/sessions/SESSIONS-ARCHIVE.md` and
`docs/_archive/ROADMAP-DONE.md` each holding a live `- [ ]` → `--check` exits 0
and prints **"✓ … archive stores hold no live markers"** — an affirmative clean
claim over files it never read. That is the fail-open class the tool's own F1
lesson forbids ("a scan that read nothing is NOT a pass"), reintroduced for the
new check: `SKIP_DIR_NAMES`' rationale is *size-metering* ("never metered" —
`sizescan.py:231-235`), written before integrity checking existed, and the gate
inherited the filter unexamined. The module doc's coverage claim ("the named
archive stores … gate") holds only for stores outside those directories, and
`_archive/`–`archive/` are the most archive-shaped directories in the repo.
**Attenuation**: today's fleet keeps every store directly in `docs/` (verified:
atelier, ros, faves, rpi, shed), so no live incident — the hole is latent, but
silent when it opens. **Counsel (author-side fix shape, principal decides)**:
in `iter_candidates`, let an archive-store basename bypass the skip-dir filter
(integrity-check it wherever it lives; still never size-metered), plus tests
for a store under `sessions/` and `_archive/`.

### HI-F2 (MINOR) — an unclosed code fence swallows the rest of the file

The fence toggle never resets at EOF, so every live marker after an unclosed
``` is treated as quoted. Reproduced: a store whose first line opens a fence
that never closes, with `- [ ]` / `- [~]` below → clean, exit 0. Fail-open and
silent. The class is pre-existing (`cold_item_count` shares the toggle), but
the delta imported it into a gate whose stated posture is fail-safe. Counsel:
either treat EOF-inside-fence as suspect (count conservatively or warn), or
document the accepted gap beside the `_FENCE` comment.

### HI-F3 (MINOR) — RECORD.md's account of the signal is now incomplete

`docs/method/RECORD.md` (§ current-truth lean, ~line 174) still describes
sizescan's gate as cold-content-only. The delta added a second gated condition;
the parent doctrine doc that tells adopters what the signal does was not
updated. A reader of RECORD.md alone learns a narrower contract than the floor
enforces. Counsel: one sentence there naming the harvest-integrity gate.

### HI-F4 (MINOR) — the tri-state grammar doesn't reach children pre-hoc

The child ROADMAP template (`docs/build/templates/docs/ROADMAP.md`) carries no
checkbox legend, so a child repo meets the tri-state rule only when the gate
*fails* and the remedy text explains it — post-hoc, mid-red-build. Attenuated:
the failure text is genuinely prescriptive (flip with disposition note /
un-harvest / never silently fix). Counsel: a two-line legend in the template so
children learn the grammar before the gate teaches it.

### HI-F5 (note) — blockquoted live items are skipped, undocumented

`> - [ ] item` never matches `_LIVE_ITEM` (the `>` breaks the bullet anchor).
Skipping quoted material is arguably *correct* — same rationale as fences — but
it is an accident of regex shape, not a documented decision; the fence
behaviour got a comment, this didn't. One line beside `_LIVE_ITEM` makes it
deliberate either way.

### HI-F6 (note) — unfenced indented code false-positives, inherently

A live marker inside 4-space-indented (unfenced) example code is
indistinguishable line-based from a nested child item — and children *must*
count (situations 2–4). Deliberate trade-off to accept; the remedy being
investigate-then-recommend means a false positive costs a look, never a wrong
fix. Worth one line in the module doc.

## Lens 4 — security & privacy

`/security-review` **discharged with grounds**: this is a landed-delta review —
the scanner reads pending diffs, and the work's file classes (markdown;
stdlib-only Python tooling) include the scanner's own markdown exclusion — so
there is nothing it can genuinely be aimed at; per REVIEW.md's reach rule, run
nowhere, weighed as nothing. Manual pass instead: the gate reads repo files
with `errors="replace"` and prints only counts and repo-relative paths — no
file content is echoed, so no content-injection surface into CI logs; exit
codes stay fail-safe on usage errors (missing path → 2, verified in suite);
stdlib-only, no network, no secrets touched. One negligible fail-open corner:
a non-UTF-8 file could mangle a `⏳` into replacement chars and miss that
marker — recorded, not actionable. No findings at either altitude.

## Assumption verdicts (lens 1)

- **A1 (right invariant)** — holds. The quote-a-marker risk is handled by the
  bullet anchor + fence skip; verbatim-preserved history archives as `[x]` with
  disposition, which the gate permits. HI-F2/F5/F6 are the edges of that
  handling, none invalidating.
- **A2 (store set covers the surfaces)** — the *suffix set* is right for the
  fleet (all stores are `*-DONE.md` / `*-ARCHIVE.md`), but coverage is
  location-conditional — HI-F1.
- **A3 (line-based counting sound)** — holds; four situations tested, no
  double-fire found. Its inherent cost is HI-F6.
- **A4 (tri-state coherently carried)** — holds across all four surfaces.
- **A5 (prescription actionable, no silent discharge)** — holds; the failure
  text prescribes investigate-then-recommend and the hatches can't silence the
  gate short of a header-visible `allow`.
- **A6 (bound held in code)** — holds.

## Overall

The gate is well-built where it looks: the invariant is right (A1), the
grammar is coherent everywhere it's written (A4), the tests encode the
principal's own taxonomy, and every commit claim reproduced. The MAJOR is a
place it doesn't look: the skip-dir filter, designed for size-metering, quietly
bounds the integrity check's coverage, and the clean banner then overclaims.
Fix shape is small; the finding is about silence, not damage — today's fleet
layout is unaffected.

Per rule 3, decisions on HI-F1–F6 are **Mike's**. Per the close rule, a MAJOR
means this cycle stays open: ruling, then application, then the application's
own cold pass via a queued `⏳`.
