# Rule-4 cold pass — the stampscan D2 application

- **Date/time:** 2026-08-06 0938 UTC
- **Pass type:** code cold pass, the D2 application (the ST cycle's three
  MAJORs held it open past the build; this pass answers whether it closes)
- **Spawn provenance:** taken from the ROADMAP `⏳` queue by a Mike-spawned
  Fable session; the taker authored none of the delta (landed 2026-08-05,
  wt: queue-batch-0806, commit `abbc720`) and was neither started nor
  instructed by its author — rule 4's criterion and the Fable tier bar both
  checked at selection.
- **Delta under review:** `tools/stampscan.py` + `tools/test_stampscan.py`
  (46 → 65) + `tools/test_templates.py` (37 → 38, `template_block` strips
  markers) + `.stampscanignore` (new) + `docs/build/templates/CLAUDE.md`
  (end marker to its own line) + `docs/method/PROPAGATION.md` (the
  stamp-convention paragraph) + `tools/README.md` (the stampscan section) +
  the advisory step in `.github/workflows/ci.yml` + the CHANGELOG entry.
- **Intent record (deferred until findings committed, rule 2):** the
  [stampscan S4 cold pass](2026-07-26-2215-stampscan-s4-cold.md) (ST1–ST7)
  + the D2 ruling of 2026-08-04 (harvested to `ROADMAP-DONE.md` § *D2
  delivered*). Reviewed at HEAD first; those files opened only after the
  verdict below was committed. The residual exposure of an application
  pass — the delta carries the prior cycle's decision stamps in its own
  docstring — is named, not denied: the module header cites ST1/ST2/ST4/
  ST6/ST7 inline, so full rule-2 blindness to the prior verdict's *topics*
  is not achievable here; its *text* stayed unopened.
- **Scope:** the whole commitment. No non-goals declared beyond the delta's
  own stated deferrals (registry wiring barred on ST3; blocking flip a
  separate ruling — both verified as genuinely absent rather than quietly
  present).
- **Lenses:** approach & assumptions · correctness & quality ·
  completeness/harvest · security & privacy.

---

## Verdict — PASS-WITH-FINDINGS: 0 MAJOR / 2 MODERATE / 2 minor / 2 notes

The build is real and honest. Every wiring precondition the S4 pass set is
verifiably in the code and exercised by tests; the deliberate deferrals
(no registry entry, no hook entry, `--warn` kept) are confirmed absent at
HEAD; the docstring's stated-residual section is the most honest scanner
self-description in the toolbox. The two MODERATEs are a half-applied fix
class and a stale doctrine claim the delta's own sweep missed — neither
touches the blocking set of a scanner that is advisory-only anyway.
Scanner behaviour and PROPAGATION.md text are policy-as-code/doctrine —
findings are counsel for the principal's ruling round; nothing applied.

### Re-run of the delta's claims (all reproduced)

- 65/65 stampscan tests, 38/38 template tests, `--selftest` OK. ✅
- Live tree, the CI invocation verbatim (`--warn --root . .`): clean,
  exit 0, the one live pair (`docs/build/templates/CLAUDE.md:18` ←
  PROPAGATION `floor`, 52 lines) identical. ✅
- **"The parser fix alone clears the whole live tree"** (the ignore file's
  own measured claim): re-run with `.stampscanignore` temporarily absent —
  the full tree including `docs/reviews/` scans clean. Reproduced; the
  globs currently gate nothing, exactly as the file says. ✅
- ST1 (documentation-of-syntax is not a stamp), ST2 (empty payload is
  drift, `narrow=` or not), ST4 (`../` and absolute `source=` → exit 2,
  never downgraded by `--warn`), ST7 (end marker anchored; template's end
  marker on its own line): each probed live or via the suite. ✅
- A config error exits 2 under `--warn`; drift exits 1 without / 0 with.
  ✅

### Findings

**SD1 — MODERATE — the ST1 fix is half-applied: canonical-region
extraction is code-context blind.** `find_stamp_blocks` hunts markers only
outside fences and code spans (the ST1 fix), but `extract_region`
(`stampscan.py:452`) matches raw lines — a fenced *example* of
`<!-- floor:begin -->` sitting above the real region in the canonical
source binds first. Probe-verified: with such an example in the parent, a
child identical to the real region reports **drift** against the example's
text (and a child matching the example text would read clean — both
directions wrong). The stated-residual list, otherwise exemplary, does not
name this side; it names only first-pair-wins for duplicate region names.
Latent today — PROPAGATION.md's only full marker lines are the real pair —
but the live canonical source is precisely the document most likely to
gain a fenced illustration of its own convention. *Counsel:* run region
extraction over the same code-stripped view (or reuse `_content_lines`),
tests both directions.

**SD2 — MODERATE — doctrine contradicting the delta, in a file the delta
edited.** `PROPAGATION.md:441-448` still reads: stampscan "is **shelved on
a parser defect** (ROADMAP D2) — so as at 2026-07-29 the stamp discipline
is convention, watched by nothing." False at HEAD: this delta fixed the
parser and wired the scanner advisory in atelier's `ci.yml`. The build
swept the stamp-convention paragraph in the same file but not this one —
the same-commit stale-claim sweep (`PRINCIPLES.md` §6) missed a surface it
was already holding. A reader of the propagation doctrine today concludes
the stamp discipline is unwatched; it is watched, advisory, in atelier.
*Counsel:* reword to the current truth (advisory in atelier only; registry
wiring barred on ST3) — one paragraph.

**SD3 — minor — ignore-glob skips are silent, against GUARDS rule (b).**
Every sibling scanner prints its suppression tally with known zeros;
stampscan prints allow-skipped *blocks* as visible notes but says nothing
about files skipped by `.stampscanignore` — and this delta ships that file
with whole-store globs (`docs/reviews/`, `.claude/worktrees/`). Measured
honestly, the globs gate nothing today — which is exactly when a silent
count matters, because they can *start* gating with no visible change in
output. *Counsel:* a `suppressed: N file(s) by .stampscanignore` line,
known zeros printed.

**SD4 — minor — `narrow=` accepts a whitespace-only reason.** The regex
captures `narrow= -->` as `' '` (truthy), so a reasonless declaration
passes as a legitimate narrow — probe-verified (`legitimate narrow
(declared: ' ')`). Below even the docstring's stated shallow-trust bar
("any non-empty token"), and inconsistent with the `\w` contract the
allow marker in the same file enforces. One-character regex fix
(`narrow=(?P<narrow>\S.*?)` or a post-parse strip-check) plus a test.

**SD5 — note — fenced-presentation stripping doesn't check closer
length.** `extract_region` strips a presentational fence when the last
line's characters match the opener's *kind*, without the ≥-length rule the
marker-recognition fence pairing in the same file enforces. Cosmetic
asymmetry; the one live region exercises the well-formed path.

**SD6 — note — an at-rest date in the delta is NZ-local, not UTC.** The
`.stampscanignore` measurement comment is dated 2026-08-06; the landing is
2026-08-05 UTC (commit 2026-08-05T13:25Z). `CONVENTIONS.md` puts UTC at
rest; this class has cost a multi-file correction before.

### Security & privacy (lens 4)

The delta *improves* the security posture: ST4 closes a genuine read-
primitive (a crafted stamp could previously aim the scanner at any file on
the machine and echo a line of it into the drift hint — traversal and
absolute paths both), and the fix fails safe (exit 2, never downgraded).
Confinement re-probed: escape attempts exit 2. Stdlib-only, no network,
no subprocess; `errors="replace"` on all reads. SD1 is the one finding
with a security shade (misbinding canonical text could let a stamped
floor be verified against example text), noted there. The harness security
scanner cannot be aimed at a landed delta on a clean tree — discharged on
those grounds, weighed as nothing.

### Cycle state

This application pass returns **0 MAJOR** → per REVIEW.md's no-MAJOR rule
the pass is terminal and **the stampscan S4/D2 review cycle CLOSES**.
SD1–SD6 are counsel for the principal's ruling round. The *work* that
stays open is unchanged by the close and already tracked: registry wiring
barred on ST3, the GUARDS allowance-model alignment (D2 residue b), and
the blocking flip as a separate later ruling.

---

## Reconcile (intent record opened after the findings above were committed)

Opened the S4 verdict and `ROADMAP-DONE.md` § *D2 delivered* only after the
verdict above was committed. Reconciliation:

- **Every ruled item is where the record says it is.** ST1 (+ST7 folded in,
  as the reconcile counselled), ST2, ST4, ST5, ST6 — each verified in code
  and tests at HEAD before the verdict was opened; nothing claimed applied
  is absent, nothing deferred is quietly present. ST3 stays open exactly as
  recorded (no registry entry, no hook entry — checked).
- **The wiring honours the reviewer's conditional bar.** "Do not wire, not
  even advisory" was conditioned on the three preconditions; all three are
  built, and the wiring is the bar's step 1 (advisory, atelier's own
  `ci.yml`, nowhere else). The `--warn`-never-downgrades-a-config-error
  property the counsel leaned on is live (re-probed).
- **The harvest's live-proof claims reproduce**: exit-2-to-exit-0 on both
  scopes, the 52-line identical pair, 65/19-test counts, the
  parser-fix-alone measurement (re-run with the ignore file bypassed).
- **SD1 sharpens against the intent record**: the S4 verdict's ST1 framing
  was "context-blind marker recognition" generally; the application fixed
  the child-side hunt and left the canonical-side extractor raw-matching.
  The record does not claim the canonical side was fixed — so this is a
  gap the application *inherited past*, not an overclaim in it; graded
  MODERATE on its own merits, unchanged by the reconcile.
- No claim failed re-run; no finding above is contradicted.

**Final: PASS-WITH-FINDINGS — 0 MAJOR / 2 MODERATE / 2 minor / 2 notes.
Terminal; the stampscan S4/D2 review cycle CLOSES. SD1–SD6 await the
principal's ruling. ST3-barred registry wiring, D2 residue (b), and the
blocking flip stay open as work, unaffected by the cycle close.**
