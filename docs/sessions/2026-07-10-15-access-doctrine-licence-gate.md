**2026-07-10 (Opus) — safe-access-onboarding doctrine + the licence gate.** Mike:
"keep going on Atelier work until economics says start a new session." Session 14
closed with a growing review batch and the sequencing note *don't stack delivery
on unreviewed text* — so the create-repo rewire (the Q1 fix) stayed blocked on
REPO-STANDARD's review. Picked two items that don't stack on that unreviewed
text: one net-new doctrine doc, one self-validating mechanical control (a
validator run is most of its own enforcement, so it adds little review debt).

**1. `docs/method/ACCESS.md` — safe-access-onboarding, the ordered runbook.** The
last unbuilt safety-doctrine (ROADMAP safety section). The *active* onboarding
counterpart to the DATA-PROTECTION/SECRETS/AUTONOMY posture — what you do the
moment access to a new domain (network/cloud/NAS/workspace/API) is granted, so a
fresh broad credential doesn't become a fresh broad blast radius. **Invents no
rule; sequences the existing ones** into a precondition chain: grant-recorded-not-
originated (AUTONOMY) → narrowest credential + plane-split (SECRETS/DATA-PROTECTION)
→ credential-into-store-before-anywhere-else (SECRETS) → read-only first ring +
reconcile-or-stop (DATA-PROTECTION) → **destructive gate encoded before you hold
destructive power** → widen-in-rings, each ring earned → Zero-Trust the domain.
Every step points up to its governing doc, none copies (PROPAGATION layer rule).
Honest pointer discipline: PRINCIPLES' "widen in rings" is about change *rollout*
(bench→node→fleet); ACCESS says so and applies the *same shape* to access-widening
rather than claiming PRINCIPLES already covers access. Encodes the estate-access
expansion (Google/Cloudflare/AWS/TrueNAS) as doctrine, not memory — the "encode
it, don't remember it" principle Mike ratified. Concrete estate access map stays
person-local in ros (sensitive topology, protected under DATA-PROTECTION).
method/README #6 (after SECRETS); the rest renumbered 7–11. Commit `b96c6a3`.

**2. `tools/licenscan.py` (A11) — the pre-publish licence-consistency gate.** The
third member of the publish triad: leakscan (no personal data) · secretscan (no
credentials) · **licenscan (no licence surprise)**. Three checks, rising
specificity: LICENSE present + identified to a known SPDX licence (an open repo
with no LICENSE defaults to all-rights-reserved — the opposite of intent); every
licence *declaration* (pyproject / package.json / Cargo.toml / *.gemspec /
setup.cfg / README shields.io badge) agrees with the LICENSE body; no incompatible
`SPDX-License-Identifier` header — **copyleft (GPL/AGPL/LGPL/MPL) into a permissive
repo is a block** (can't be relicensed on publish), permissive-into-permissive is a
warn. Compatibility is deliberately conservative + advisory (flags for a human, not
legal advice; doesn't encode Apache/GPLv2-class depth). `--expect <SPDX>` asserts
the licence for CI. Zero-dep stdlib, allow-marker + `.licenscanignore` hatches,
`--selftest`, `--json`, fail-safe exit codes — matches the sibling scans exactly.
Unlike them it's a **pre-publish** gate, not an every-commit hook: private repos
carry licence mess harmlessly; it bites at the public boundary AUTONOMY already
gates. Commit `c38e4ce`.

**Two live-caught issues during the build** (honest-instrument — the tool proved
itself before I trusted it): (a) the tool flagged its *own* source — detection
pattern + selftest fixtures look like real SPDX headers — the same self-scan case
secretscan handles with allow-markers; applied the marker (proving the hatch) +
de-coloned one docstring mention. (b) that surfaced a genuine line-number bug: the
first cut located findings by re-searching the file for the captured text, which
mislocates when a fragment recurs (reported line 122 for a match on line 185);
fixed to compute the line from the match offset, with a regression test
(`test_line_number_accuracy`). Also loosened the package.json regex off a
line-start anchor so minified/inline JSON is caught. 35 tests; full tools suite
98→133 green; live scan of atelier clean at `--expect Apache-2.0`.

**A5 deferred, deliberately:** SBOM + keyless signing needs syft/cosign — an
external tool install (AUTONOMY floor) that breaks the zero-dep house-tool pattern.
Recorded as a design call in the ROADMAP, not a skipped build; revisit when a real
release needs it.

Lockstep each (RECORD): CHANGELOG Added entries, ROADMAP ticks with review-owed
notes, README index updates, leak+secret scans clean before each commit. Both
pushed.

**Model:** Opus, plan-included — one doctrine doc + one stdlib tool, not
token-heavy; no flag. **ros pin:** left at `3ba6275` — no ros files changed; the
new atelier content is review-owed and ros's inlined CLAUDE.md floor is unchanged,
so no floor-driven bump (consistent with session 14's deliberate hold). **Review
debt is now the standout item:** EVIDENCE §13/§14 + SECRETS + REPO-STANDARD +
REPO-BOUNDARY + ACCESS (doctrine text → a REVIEW.md sampling pass) and the two
scans + licenscan (approach reviews of the pattern sets). The honest recommendation
to Mike: the next atelier session is a strong candidate for a **Fable review
sweep** over this batch rather than more building. **Remaining build queue:**
rewire create-repo to inherit (still blocked on REPO-STANDARD review) + templates
move; safe-access-onboarding is now DONE.
