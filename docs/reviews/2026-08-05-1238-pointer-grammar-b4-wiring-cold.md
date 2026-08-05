# Brief — pointer-grammar build + B4 `harvestscan` wiring, code/design cold pass

**Queue ref (refs only, from `ROADMAP.md` § Doctrine — review-owed):** the
FUNDED `⏳`-pointer-grammar build and the B4 `harvestscan` wiring, one build
per HV2. Delta: `tools/pointerscan.py` + `tools/test_pointerscan.py` (new);
`tools/harvestscan.py` + `tools/test_harvestscan.py` (HV1 scope, HV2–HV4
folds, `--replay`); the two registry entries in `tools/floor.py` +
`tools/test_floor.py`; `tools/README.md`; `CHANGELOG.md`; the three specimen
fixes in `ROADMAP.md` (all landed 2026-08-03, merge `1fbfc2e`).

**Pass type:** code/design cold pass (rule 4). The B4 cycle's HV1 MAJOR keeps
that cycle open past this application, so this pass is also the B4 cycle's
application pass.

**Provenance (rule 4):** reviewed by a Fable session Mike spawned onto the
queue ("do any review work and any other work that requires fable");
the author sessions (the 2026-08-03 orchestrated run and its workers) neither
started nor instructed this session. Brief written by the taker, cold. The
intent records (`ROADMAP-DONE.md` § *The `⏳` pointer grammar mechanised*, and
the B4 cold-pass verdict with rulings HV1–HV5) were **not opened** before the
findings below were committed; they are read at the reconcile step only.

**Non-goals:** the warn-renders-`enforced` board fork (ruled 2026-08-04 as its
own build item); the wider ruling-state residue class already recorded in
`ROADMAP.md` as open (observations on its boundary are in scope, its fix is
not).

# Verdict — PASS-WITH-FINDINGS · 0 MAJOR / 1 MODERATE / 1 minor / 5 notes

**What was verified live at HEAD, not read from the delta's account:**

- Suite: 933 tests, OK. Both selftests: 0 failures. The live tree scans
  clean — including the five claim-stamped `⏳` pointers this session added,
  which exercises the claim-stamp-plus-glyph state-prefix shape (b) on real
  content.
- **The HV1 replay figures reproduce.** `--replay --only-bulk-deletes` at
  HEAD: 446 commits touch the records, 8 in scope, 4 fired, 16 items. The
  recorded figures (6 in scope, 3 fired, 15 items over 429 commits) are a
  strict prefix; the additions are
  post-landing commits. The one new firing (`958e59b`, 1 item, net −82) is
  the ER1–ER4 residue item completing and being condensed at close below the
  similarity threshold — the warn-and-let-a-human-diff case the design
  accepts, not a defect.
- **The hook plane fires end-to-end.** Scratch repo, 12 distinct multi-line
  items, 10 deleted and staged (−60 net lines): all 10 reported, exit 0.
  Under the 50-line gate (−40): correctly out of scope, says so, exit 0.
- **HV4's plane split is real, not wording.** Staged deletion with the
  working tree restored: `--staged` fires (reads the index), the default run
  is clean (reads the working tree). The `git show :path` index read works.
- **The gate is measured on `ROADMAP.md` alone** — the pair-netting dodge
  (a harvest netting to zero across watched files) is closed and documented
  in `GATE_RECORDS`' comment with the measurement that grounds it.
- **Registry scope is pinned by tests**: `--only-bulk-deletes` on all three
  planes, `--staged` hook / `HEAD^` CI, `pointerscan` default scope `docs`
  with an advisory form — a test failure now guards the HV1 ruling itself.
- **The single-sourced scope decision (HV2) is structural**: `harvestscan`
  imports `pointerscan.is_pointer`; its own tests pin the emphasis-run and
  marker shapes so a narrowing over there breaks this tool's suite too.
- Grammar detector: both selftest halves hold on the recorded specimens
  (must-flag and must-stay-silent), the FG6 pass-type specimen is clean, the
  order discriminator keeps the three legitimate further-pass pointers
  silent, and `[x]` items are excluded as non-pointers.
- `tools/README.md` and `CHANGELOG.md` match the code's behaviour and state
  the warn-only posture with its grounds. Exit codes are as documented
  (0 with findings, 2 for a bad path).

**Lens 1 (approach).** The load-bearing choices — content fingerprinting over
title keys, containment over Jaccard, emphasis-run scoping over glyph-only,
order-as-discriminator for cycle state, warn-only with an ungrounded constant
named as ungrounded — are each argued from a measurement that is either
reproducible in-repo (`--replay`) or pinned in a selftest specimen. The scope
question ("what is a pointer") is settled where both consumers can import it.
This is the right shape.

**Lens 4 (security/privacy).** Both tools read repo-tracked markdown only;
no secrets surface, no external I/O beyond git. Probes ran in a scratch repo
under the session scratchpad, outside the tree. Tree-wide greps in this pass
excluded `SESSIONS.md`/`sessions/` per the records-exclusion rule; no
record-store content is quoted in this verdict beyond what `ROADMAP.md`
already carries on the hot path.

## Findings

**PG1 (MODERATE) — `pointerscan`'s design rationale claims a staged read it
does not perform.** The docstring's fourth ground for the cycle-state design
says it "reads staged content honestly and has no plane seam"
(`pointerscan.py:127`). There is no staged mode: `scan()` reads the working
tree, and the hook invocation passes no `--staged`. Probe: stage a pointer
carrying a reviewer instruction, revert the working tree — the hook-plane
scan prints clean and the commit lands the steering pointer. The *behaviour*
matches the floor's hygiene-scanner class (linkscan, datescan, wrapscan,
spellscan and siblings all read the working tree at the hook; only the
boundary scanners read the index), so the defect is the claim, not the class
— which is precisely HV4's wording class, fixed in `harvestscan` in this same
build. What is true and worth saying instead: detector 2 needs no cross-file
join, so it has no *cross-file* plane seam — the single-file
index-vs-worktree seam remains and is the class's accepted residual. Fix is
one sentence (or a `--staged` mode, which the class convention does not
demand).

**PG2 (minor) — an undocumented file-level kill switch.** A
`pointerscan:allow:` marker anywhere in the *first line* of a roadmap file
skips the whole file (`pointerscan.py:440`), while the docstring, the README
and the finding-footer all describe a per-item hatch only. A whole-file
exemption is a materially bigger lever than the documented one; either
document it or drop it — the per-item hatch already covers the recorded need.

**PG3 (note) — the steering net is deliberately narrow; a paraphrase passes.**
Beyond the question-mark check, `_STEER` holds one family per recorded
instance and the docstring commits to growing it only on real instances. A
steer phrased without a question mark and outside those families is silent
(probed with a "the pass should focus on" phrasing). Right
posture for an advisory guard — recorded so the next live instance grows the
list rather than reading as a miss.

**PG4 (note) — the residue class has already recurred outside the guard's
scope, and the recurrence ladder is one instance from the guard's own bar.**
The 2026-08-04 decision sitting found two items whose *ruling* state was
stale ("await ruling" after Track A had ruled and applied) — the cycle-state
residue class, in wording `_CLAIM` deliberately does not match (a
ruling-owed claim is not a review-owed claim; it is used only to *name* the
state). `ROADMAP.md` records both instances. The build's own funding history
used promote-at-three; a third live ruling-state residue would meet it, and
the natural widening is a third claim family (ruling-owed) driven by the
same order discriminator.

**PG5 (note) — shared boilerplate can mask a genuine deletion.** Containment
scores an item against each surviving body, so items sharing heavy templated
phrasing vouch for each other: two probe rounds with near-identical bodies
and with a shared filler paragraph both read "survived" for genuinely
deleted items; only fully distinct bodies fired. Partly by design —
absorption into a sibling is a legitimate survival — and the real corpus's
bookkeeping vocabulary is stripped before comparison, but non-bookkeeping
boilerplate is not. Worth knowing when reading a clean result over
templated items; not worth a threshold move (the constant stays ungrounded
by ruling).

**PG6 (note) — marker-grammar drift between the two parsers.**
`harvestscan`'s `ITEM_RE` accepts `[ x~]` lowercase only; an uppercase `[X]`
item does not parse as an item at all (it is dropped, not folded), while
`pointerscan`'s `_MARKER` accepts `[xX]`. The corpus uses lowercase
throughout, so nothing is live; recorded because the two tools now share the
pointer decision and should share the marker grammar too.

**PG7 (note) — the net-line gate is blind to terse-item massacres.** Twelve
one-line items deleted is 12 net lines — under the gate by construction.
Inherent to the ruled scope (net lines, measured on this corpus's fat
items), and the right trade at this corpus; recorded as the gate's stated
residual so a future roadmap style shift (terse items) re-opens the
question rather than inheriting the number.

## Faithfulness to the HV rulings (written at reconcile, below)

## Reconcile (intent records opened after the findings above were committed)
