# Rule-4 cold pass — the licenscan E1+E2 build

- **Date/time:** 2026-08-06 0903 UTC
- **Pass type:** code cold pass (tier: Fable — bar checked at selection)
- **Spawn provenance:** taken from the ROADMAP `⏳` queue by a Mike-spawned
  Fable session ("do any review work that depends on Fable"). The taker
  authored none of the delta: the build landed 2026-08-05 from worktree
  `queue-batch-0806` (commit `ae056a2`, README row follow-up `68d23bf`);
  this session's only prior contact with it is the refs-only pointer. The
  author neither started nor instructed this session — rule 4's criterion
  holds.
- **Delta under review:** `tools/licenscan.py` + `tools/test_licenscan.py`
  (37 → 52 tests) + the CHANGELOG entry + the corrected check-1 row in
  `tools/README.md`.
- **Intent record (deferred until findings committed, rule 2):**
  `ROADMAP-DONE.md` § *The licence gate learns proprietary*.
- **Scope:** the whole commitment — intent, decisions, code, tests, docs,
  live behaviour. No non-goals declared.
- **Lenses:** approach & assumptions · correctness & quality ·
  completeness/harvest · security & privacy.

---

## Verdict — PASS-WITH-FINDINGS: 0 MAJOR / 1 MODERATE / 2 minor / 2 notes

The E1 and E2 behaviours are real, probe-verified at HEAD, and the design
reasoning (an unrecognised LICENSE is a *declared* custom licence; the
copyleft judgement needs no licence name) is sound and honestly documented,
including what the tool still cannot see. The suite runs 54/54 green under
the house discovery invocation; `--selftest` proves both fixes standalone.
The findings are consistency defects at the edges, none reaching the
blocking set. Scanner behaviour is policy-as-code — doctrine by function —
so every finding below is counsel awaiting the principal's ruling (rule 3);
nothing was applied.

### Re-run of the delta's claims (all reproduced)

- Proprietary LICENSE + vendored `GPL-2.0` header → high `incompatible`
  block; same under an explicit `LicenseRef-` body. ✅ (tests + fresh probe)
- Reasoned allow-marker on the LICENSE body retires the `unknown-license`
  warn and the header checks keep running. ✅
- `--expect Apache-2.0` cannot pass on an unnameable body, marker or not. ✅
- 16 unambiguous trove classifiers resolve (`Apache Software License` →
  `Apache-2.0`); the ambiguous family names (`BSD License`, unversioned
  GPL/LGPL) still degrade to the `unknown-declaration` warn. ✅
- `-only` / `-or-later` / `+` suffixes resolve to the base id and a
  `GPL-2.0-only` header still blocks end-to-end. ✅
- Test count: discovery runs **54**, not the recorded 52 — see LC3.

### Findings

**LC1 — MODERATE — the unknown-license suppression accepts a reasonless
marker, against GUARDS rule (c) as enforced elsewhere in the same file.**
`licenscan.py:416` keys the suppression on a raw substring
(`ALLOW_MARKER not in txt`), not on `parse_allow`. Probe-verified both
ways: a bare `licenscan:allow` with no reason, and a *prose mention* of the
marker text inside the LICENSE body, each silently retire the
`unknown-license` finding. The same file's `ALLOW_RX` was tightened the
same day precisely so that "a bare marker is a mention, not an exemption",
and the prose-mention form is the exact defect class the 2026-08-05
allowance sweep caught elsewhere and fixed. The CHANGELOG's own line —
"the allow marker now means what it says" — is not yet true at this one
site. Blast radius is bounded: only the medium warn is suppressible; the
header checks, `--expect`, and every high finding are unaffected
(probe-verified). *Counsel:* replace the substring test with a per-line
`parse_allow` over the LICENSE body, must-pass/must-fail tests both
directions.

**LC2 — minor — that suppression is invisible to the rule (b) tally.**
When the marker retires the `unknown-license` warn, `suppressed_declarations`
stays 0, so a clean report is indistinguishable from an exempted one at
exactly the site E1 widened — the "identical output for materially
different cover" shape. *Counsel:* count it in the suppression line when
LC1 is fixed.

**LC3 — minor (cross-delta provenance, stated honestly) — two allowance
tests sit after `unittest.main()` and the recorded count matches the broken
invocation.** `class Allowances` was appended below the
`if __name__ == "__main__": unittest.main()` block by the parallel
allowances commit (`9ac8fdb`, F1 cycle — already closed 0-MAJOR), not by
this delta. Direct invocation (`python3 tools/test_licenscan.py`) therefore
runs 52 of 54 tests, silently dropping exactly those two; discovery runs
all 54. The CHANGELOG's "37 → 52" is the direct-run count, so the record
and the house suite disagree by the two dropped tests. *Counsel:* move the
class above the main block; correct the count when next touching the entry.

**LC4 — note — four dead alias entries.** The `-or-later` entries in
`_SPDX_ALIASES` (`gpl-3.0-or-later`, `gpl-2.0-or-later`,
`lgpl-3.0-or-later`, `agpl-3.0-or-later`) are unreachable: the suffix is
stripped before the alias lookup. Harmless; misleading to a future editor.

**LC5 — note — pre-existing, out of delta.** With multiple LICENSE-class
files present (`LICENSE` + `COPYING`), `license_bodies[0]` picks by
directory-walk order, not name priority — probe showed `COPYING` winning.
Filesystem-order dependent in principle. Predates E1; recorded for the
backlog, not against this delta.

### Security & privacy (lens 4)

Stdlib-only, no network, no subprocess, no dynamic evaluation; reads the
tree it is pointed at and nothing else. Regexes are anchored or bounded —
no catastrophic-backtracking shapes on the paths user content reaches. The
one security-relevant behaviour change is E1's, and it *widens* detection
(copyleft under an unnameable licence now blocks). The harness security
scanner cannot be aimed at this work: it scans pending changes, and the
delta is landed with a clean tree — discharged on those grounds, weighed
as nothing.

### Cycle state

0 MAJOR → per REVIEW.md's no-MAJOR rule this pass is **terminal and the
licenscan E1+E2 cycle CLOSES**. LC1–LC5 are counsel for the principal's
ruling round; none blocks the close.

---

## Reconcile (intent record opened after the findings above were committed)

Opened `ROADMAP-DONE.md` § *The licence gate learns proprietary* only after
the verdict above was committed (`732aa11`). Reconciliation:

- **E1 fix shape honoured exactly**: declared-licence reading, header
  checks kept running, copyleft-only judgement under a nameless licence —
  all as the item specified, and the item's required test (the proprietary
  fixture must report the GPL file) exists twice over (unittest +
  `--selftest`), re-run green here.
- **E2 fix shape honoured exactly**: lookup before the
  unrecognised-declaration check, ambiguous family names deliberately
  degrade to the warn; the required clean-classifier test exists and
  passes.
- **The reproduction sharpens LC1 rather than excusing it.** The item's
  2026-07-25 reproduction appended a bare `licenscan:allow:` (no reason)
  and correctly got nothing; the delivered fix makes exactly that
  reasonless form effective. So the build satisfied the *item* while
  crossing the rule (c) tightening that landed the same day in the same
  file — LC1 stands as written, now with its likely origin visible.
- **"Module tests 37 → 52, full suite green, live tree clean"** — the
  live-tree and suite claims reproduce (licenscan clean on this tree;
  54/54 under discovery); the count is the direct-run figure per LC3.
- No claim in the intent record failed re-run; no finding above is
  contradicted by it.

**Final: PASS-WITH-FINDINGS — 0 MAJOR / 1 MODERATE / 2 minor / 2 notes.
Terminal; the licenscan E1+E2 cycle CLOSES. LC1–LC5 await the
principal's ruling.**
