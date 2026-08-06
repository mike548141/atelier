# Rule-4 cold pass — the pathscan D1 rescope application

- **Date/time:** 2026-08-06 1002 UTC
- **Pass type:** code cold pass, the D1 rescope application (the PS cycle's
  three MAJORs held it open past the build; this pass answers whether it
  closes)
- **Spawn provenance:** taken from the ROADMAP `⏳` queue by a Mike-spawned
  Fable session; the taker authored none of the delta (landed 2026-08-05,
  wt: queue-batch-0806, commit `b012884`) and was neither started nor
  instructed by its author — rule 4's criterion and the Fable tier bar both
  checked at selection.
- **Delta under review:** `tools/pathscan.py` + `tools/test_pathscan.py`
  (53 → 73) + the rescoped advisory step in `.github/workflows/ci.yml` +
  the residual burn-down (the path fix in `docs/build/README.md`; reasoned
  allow-markers in `docs/build/REPO-STANDARD.md`, `docs/method/00-APEX.md`,
  `docs/method/EVIDENCE.md`, `docs/method/TOOLBOX.md`, ADR 0006, and the
  2026-07-19 review-trigger decision record) + the CHANGELOG entry.
- **Intent record (deferred until findings committed, rule 2):** the
  [pathscan S2 cold pass](2026-07-26-2215-pathscan-s2-cold.md) (PS1–PS8 +
  deferred Q2) + the D1 ruling of 2026-08-04. Reviewed at HEAD first; the
  prior verdict opened only after the verdict below was committed. The
  application-pass residual is named as in the sibling pass: the module
  docstring cites the PS ids inline, so blindness to the prior verdict's
  *topics* is partial by construction; its *text* stayed unopened.
- **Scope:** the whole commitment. The delta's stated deferrals — registry
  promotion (PS5) waits on the open floor.py cold pass; the blocking flip
  stays a separate ruling — verified genuinely absent, not quietly present.
- **Lenses:** approach & assumptions · correctness & quality ·
  completeness/harvest · security & privacy.

---

## Verdict — PASS-WITH-FINDINGS: 0 MAJOR / 0 MODERATE / 1 minor / 2 notes

The cleanest of the three deltas under review this session. The rescope
does what the ruling funded: the fourth anchor kills the dominant
false-positive shape at its cause, the gateable surface is scanned
advisory and comes back clean with every suppression visible and reasoned,
and the docstring is conspicuously honest — the overclaim PS8 caught is
corrected in place with the correction narrated, and the named
false-positive/false-negative modes all reproduced exactly as written when
probed adversarially. The rule (b) tally implementation (`Tally`, known
zeros, per-kind breakdown) is the exemplar of the twelve. Scanner
behaviour is policy-as-code — findings are counsel for the principal's
ruling round.

### Re-run of the delta's claims (all reproduced)

- 76/76 tests under house discovery (see the minor below on the count),
  `--selftest` OK.
- The CI invocation verbatim over the gateable surface
  (`docs/method docs/build docs/decisions README.md CLAUDE.md
  SECURITY.md`): **clean, exit 0, 10 findings suppressed by allow-marker,
  breakdown printed** — the residual burnt to zero, and visibly so. ✅
- PS1 (anchor 4 + root-file scope), Q2 (directory-index retry, only for a
  fully extensionless last segment), PS3 (`YYYY`/`HHMM` only, `MM`/`DD`
  deliberately not cues): all implemented, tested, and probed. ✅
- PS8's corrected claim verified in the shipped text: "THE THIRD CITED
  OCCURRENCE IS NOT CAUGHT" — stated plainly, with the single-segment
  floor defended on its own merits. ✅
- PS5 deferral honest: `tools/floor.py` carries no pathscan (or stampscan)
  registry entry — checked, absent. ✅
- Adversarial probes matched the documentation exactly: anchor-4 masking
  reproduces (stated residual, correctly named as the price of widening);
  a bare `pathscan:allow` mention exempts nothing; a reasoned marker
  exempts and tallies; emphasis-wrapped paths invisible (named FN);
  link-text backticked paths scanned (deliberate). ✅

### Findings

**PD1 — minor (cross-delta provenance, stated honestly) — three allowance
tests sit after `unittest.main()`, and the recorded count predates the
merge.** At HEAD `tools/test_pathscan.py` runs **76** under discovery, not
the recorded 73: the parallel allowances branch contributed a
`class Allowances` placed below the `if __name__ == "__main__"` block
(the file was a named conflict in merge `0228793`), so direct invocation
(`python3 tools/test_pathscan.py`) silently drops those three. Identical
in shape and origin to LC3 in this session's licenscan verdict — one
fix (move the classes above the main block in both files) clears both.
The delta's own "53 → 73" was true on its branch; the record and the
house suite now disagree by exactly the merge-added tests.

**PD2 — note — the burn-down count needs one denominator.** The roadmap
entry says "six false positives marked with written reasons"; on disk the
burn-down is 6 files, 8 marker lines, 10 suppressed token-findings (the
tally's own figure). All three countings are defensible; the record
should say which it is using — this programme has a standing memory of
blast-radius figures going wrong in both directions.

**PD3 — note — a missing path in Markdown link *text* double-reports with
linkscan.** `[see \`docs/x.md\`](docs/x.md)` with a broken target yields a
pathscan finding on the text half and a linkscan finding on the
destination — two findings, one defect, two tools. Deliberate per the
docstring (the text half is in scope by design) and correct in isolation;
recorded so the duplicate isn't later read as a bug in either tool.

### Security & privacy (lens 4)

Stdlib-only; no network, no subprocess. Unlike stampscan there is no
content-read primitive at all — candidates are tested for existence
(`.exists()`), never opened, so no echo channel exists to confine.
Nothing in the delta widens input handling. The harness security scanner
cannot be aimed at a landed delta on a clean tree — discharged on those
grounds, weighed as nothing.

### Cycle state

This application pass returns **0 MAJOR** → per REVIEW.md's no-MAJOR rule
the pass is terminal and **the pathscan S2/D1 review cycle CLOSES**.
PD1–PD3 are counsel for the principal's ruling round. Open work is
unchanged by the close: the registry promotion (PS5) rides the next
floor.py touch after that file's open cycle closes, and the blocking flip
stays a separate later ruling.

---

## Reconcile (intent record opened after the findings above were committed)

Opened the S2 verdict (revised counts: 3 MAJOR — PS1, PS4, PS8; 5 MINOR —
PS2, PS3, PS5, PS6, PS7; Q2 deferred) and the D1 ruling only after the
verdict above was committed. Reconciliation:

- **All three MAJORs are discharged by the delta, verifiably at HEAD.**
  PS1: anchor 4 + the root-file scope, with the S2-cited motivating case
  (a root README naming `docs/decisions/`) now inside the scanned gate
  surface. PS4: the gate story is stated in the docstring's SCOPE section,
  the argparse help, and the ci.yml comment — records named out with the
  reason, not just omitted. PS8: the overclaim corrected in place, the
  correction narrated rather than silently dropped.
- **All four docstring-honesty MINORs (PS2/PS3/PS6/PS7) present as named
  limits**; PS3 additionally got the date-placeholder exemption, and the
  probe set above exercised each documented mode. PS5 deferred exactly as
  the delta says, verified absent from the registry.
- **Q2 (deferred at the S2 pass) is delivered** as the directory-index
  retry, monotone-safe and bounded to fully extensionless tokens, with the
  masking cost named in the residual.
- No claim in the intent record failed re-run; nothing above is
  contradicted by it.

**Final: PASS-WITH-FINDINGS — 0 MAJOR / 0 MODERATE / 1 minor / 2 notes.
Terminal; the pathscan S2/D1 review cycle CLOSES. PD1–PD3 await the
principal's ruling. PS5 (registry promotion) and the blocking flip stay
open as work, unaffected by the cycle close.**
