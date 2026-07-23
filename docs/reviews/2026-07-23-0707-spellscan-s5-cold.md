# Review brief — spellscan (S5) first-of-kind scanner (cold)

- **Stamped**: 2026-07-23 07:07 UTC (brief written before the reviewer opened
  `spellscan.py`).
- **Subject**: `tools/spellscan.py` — the S5 "NZ-English spelling" scanner,
  advisory (`--warn`, exit 0) in `.github/workflows/ci.yml`. Delta: the S5 build
  + `4061334` (advisory CI wiring). Intent record:
  `docs/sessions/2026-07-22-1036-invariant-candidates.md` § S5.
- **Why it earns a review**: first-of-kind tooling **and** a silent-failure
  class — and for a *spelling* tool the worst failure is a confident wrong
  correction (silent damage). PASS-and-clean is the precondition for flipping.
  S5 was approved on ROI over a borderline finding count, so the review also
  weighs whether the cheapest-scanner ROI actually holds.
- **Nature of the review**: **code + enforcement behaviour**, not self-authored
  doctrine — rule 3 applies to the gate-flip; code findings are ordinary.

## Spawn provenance (rule-4 clearance for taking the ⏳)

The S5 delta was authored by a **prior queue-run chain** (the chain that queued
the ⏳ pointer). This review was taken by a **separate, Mike-started orchestrated
queue run** (0707) that neither started nor instructed that build. The taker
wrote this brief and spawned one independent cold reviewer (Opus, no hand in
building spellscan). Independence is against the *author*, which taker and
reviewer both clear.

## Scope handed to the reviewer

1. Do the generative `-ise`/`-isation` families ever invent a wrong word (a
   confident false correction)? — the key silent-DAMAGE risk.
2. Exemptions' honest limits, esp. the license/practice exclusion — permanent or
   revisit with a narrower lowercase-bare heuristic?
3. Baseline signal-vs-noise (~68 findings) — is `catalog` (~10) genuine or a
   repo term-of-art?
4. Does it handle te reo Māori macrons, or is that out of scope and honestly
   declared so?

## Verdict (transcribed from the cold reviewer)

**PASS-WITH-FINDINGS — 0 MAJOR / 2 minor / 1 Low / 1 nit.** The engine is sound
where it matters most: **no confident wrong correction exists** — every generated
`-isation` suggestion is a valid NZ spelling, and no both-correct word is flagged.
All findings are tuning/honesty calibration, none correctness-breaking. Advisory
wiring is correct and it is absent from every blocking gate. But it is **NOT
gate-ready** — the live corpus signal ratio is ~1-in-5 (~76–88% noise).

**Orchestrator verification** (re-ran before transcribing): `--selftest` →
`selftest OK` exit 0 ✅; `cd tools && python3 -m unittest test_spellscan` →
`Ran 60 tests … OK` ✅; baseline over `docs` → **68 findings** ✅; **`artifact`
alone accounts for 53 hits** ✅; minor-1 confirmed — `hypothesize`, `jeopardize`,
`penalize` are all in `IZE_NOUN_CAPABLE` (`spellscan.py:172–173`). Numbers and
findings confirmed.

### Findings

- **SS1 — minor (over-detection + docstring overclaim).** `spellscan.py:163–174`:
  the docstring says `IZE_NOUN_CAPABLE` *deliberately* excludes stems with
  irregular nouns (cites synthesize→synthesis, emphasize→emphasis excluded), but
  the set **includes `hypothesize`** (noun: hypothesis — the exact `-esis`
  parallel to the excluded synthesize), **`jeopardize`** (→jeopardy), and
  **`penalize`** (→penalty). Their generated `-isation` nouns are near-nonwords.
  *Live damage ≈ nil* (those US forms essentially never appear in prose, and the
  z→s transform stays internally valid) — so it's **latent over-detection + a
  docstring honesty gap**, not a correctness break. *Direction:* drop those three
  from `IZE_NOUN_CAPABLE` (keep their verb forms), matching synthesize's handling.
- **SS2 — minor (honesty gap: macrons undeclared).** The docstring grounds the
  tool in CONVENTIONS.md's *"NZ English with macrons"* default but has **zero**
  macron logic and never says the macron half is unhandled — a reader could infer
  it checks tohutō. A missing macron ("Maori" for "Māori") is the same
  silent-failure class this scanner exists for. Out-of-scope is defensible (needs
  a te-reo wordlist) **but must be declared**. 0 live findings (corpus already
  uses "Māori" correctly), so honesty-only. *Direction:* one line — "macron
  correctness on te reo Māori is out of scope, not checked here."
- **SS3 — Low (ROI premise weaker than the mining record claimed).** The
  promotion premise ("`artifact` recurs 15+× → pervasive under-detected breach")
  **does not survive the corpus**: ~48 of 53 `artifact` hits are the legitimate
  CI/build/SBOM/"release-artifact-signing" term-of-art, where "artefact" would be
  *wrong*; only ~5 are the general "produced thing" sense. Genuine NZ breaches
  actually caught are thin (`finalize`→finalise at ROADMAP-DONE:1106; a few
  general-sense artifact). *Direction:* keep as a low-cost/low-yield advisory —
  ROI isn't negative (engine is cheap and sound), but the "surfaces a pervasive
  hidden breach" selling point is largely a mis-count of a correct technical term.
- **SS4 — nit (dotted unittest invocation).** `python3 -m unittest
  tools.test_spellscan` → ModuleNotFoundError; `discover -s tools` / `cd tools &&
  …` work. Sibling-consistent wart (matches datescan DSR7 / WS5). No action unless
  the fleet fixes it everywhere.

### Reviewer recommendations on the scoped questions

- **license/practice exclusion → PERMANENT** (empirically vindicated; do NOT add
  a lowercase-bare heuristic). `practice` appears 178× in docs, overwhelmingly the
  NOUN ("good practice", "standard practice") — **correct NZ English** (NZ splits
  noun *practice* / verb *practise*); a bare-lowercase heuristic would fire on all
  178 and be wrong on ~170. `license` (75×) similar (Apache `LICENSE`, "MIT
  License"). No POS-free heuristic separates noun "a licence" from verb "to
  license". Naming the exclusion in the docstring rather than hiding it is a
  positive.
- **`catalog` (~10 hits) → a one-line decision for Mike, NOT a scanner
  exemption.** Not a proper noun; every hit is atelier's own coinage ("invariant
  catalog", "repo-specific catalog"). "catalogue" is the NZ spelling, so these are
  true NZ deviations — but a *consistent house coinage*. Rule it: rename to
  "catalogue" fleet-wide, or accept "catalog" as a deliberate term-of-art. See the
  🎯 below.

### Honest positives (reviewer, unprompted)

The core safety property holds — no invented wrong correction, no both-correct
word flagged; the z→s engine is provably safe across all 46 noun forms + every
stem/standalone pair. Exemption stack thorough and well-tested (fenced/inline
code, blockquote, path/URL blanking, quote-flanked mention, ALL-CAPS, allow-marker,
`.spellscanignore`) — 60 tests green, fail-open guards asserted. Fail-safe exit
codes (2 on config error). The license/practice exclusion is the correct judgement
and named openly. Wiring exactly as specified: selftest + advisory `--warn` in
`ci.yml`, absent from every hook/floor.yml.

### Gate-readiness call: NOT ready to flip advisory → blocking

Concrete preconditions: (1) fix the genuine handful (`finalize`→`finalise`; rule
on `catalog`); (2) neutralise the ~52 noise findings — inline-code or allowlist
the CI-"artifact" technical sense and the OWASP ASVS/SAMM proper-noun chapter
names (`sanitization`/`organization`); this is a real sweep, not a formality;
(3) land SS1 + SS2 (both cheap) so the docstring's honesty claims hold before the
tool becomes load-bearing. **ROI holds only partially** — worth keeping as a
low-yield advisory *provided* the artifact/OWASP noise is tamed before it gates.

### Method results

- `python3 tools/spellscan.py --selftest` → `selftest OK`, exit 0 ✅
- `cd tools && python3 -m unittest test_spellscan` → `Ran 60 … OK` ✅
- `discover -s tools -p 'test_spellscan.py'` → `Ran 60 … OK` ✅
- `python3 -m unittest tools.test_spellscan` → FAILS, ModuleNotFoundError (SS4)
- `--warn --root . docs` → 68 findings, exit 0 ✅
- Absent from pre-commit hook / floor.yml; selftest + advisory only in ci.yml ✅

## Disposition (taker)

No MAJOR ⇒ the review is **terminal as a review**. The core spelling-tool safety
property (no confident wrong correction) is proven, so the tool ships correctly as
advisory. Follow-ons queued to the ROADMAP, neither this run's to complete:
(1) apply SS1–SS4 + neutralise the artifact/OWASP noise + `finalize`→`finalise` —
ordinary code work; (2) the advisory→blocking flip stays Mike's call, with the
concrete precondition of a near-zero re-baseline; (3) a **🎯 for Mike**: rule
`catalog` — rename "catalog"→"catalogue" fleet-wide, or accept it as a deliberate
house term-of-art (this decides whether ~10 findings are real or exempt). spellscan
stays advisory meanwhile; no wiring change this run.
