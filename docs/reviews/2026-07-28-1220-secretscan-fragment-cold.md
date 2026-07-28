# Review brief — secretscan fragment-match exemptions (rule-4 cold pass)

- **Date:** 2026-07-28 1220 UTC
- **Tier / spawn provenance:** Fable — the tier the queue item asks for on
  the security floor. The Mike-spawned "do any review work" taker session,
  fourth queue item today; author of nothing in this delta, not spawned by
  its author. Claim commit on main precedes this worktree.

## What the work is (refs only)

Commit `dd902aa` (#14): four secretscan suppression rules re-anchored from
fragment matches to whole-shape matches (the env-var `\b` lead, the
extensionless secret-store path, unclosed templating markers, the stray
bracket), plus three suppressions added for false positives the fix itself
introduced. Files: `tools/secretscan.py`, `tools/test_secretscan.py`, and
the queue pointer in `docs/ROADMAP.md`.

**Deferred until findings are committed:** the boundary-findings triage
session record
[`2026-07-28-0430-boundary-findings-triage`](../sessions/2026-07-28-0430-boundary-findings-triage.md)
(the applier's evaluative account). Named exposure: the commit message and
the queue item's own two aimed questions, treated as a floor of questions,
never a fence.

## Scope — four lenses, security-first

1. **Approach:** the queue's first aimed question — is *re-scan the
   corpus* a sound acceptance test for a security gate, or does it tune
   the gate to one estate's content? Attack each of the three
   corpus-driven suppressions (minified-JS code shapes, kebab slugs,
   comment prose) for what *else* its widened net catches.
2. **Correctness:** red legs for all four defect classes at `dd902aa^` vs
   HEAD, with synthetic values; check the new regexes' edges (`_LEAD`
   against `BYPASS`/`passport`-type neighbours; `ABS_PATH_RX` vs base64;
   closed-marker templates; `CODE_EXPR_RX`'s charset argument).
3. **Completeness:** the second aimed question — the pre-existing
   lowercase-hex gap, to be *ruled on* rather than inherited; whether the
   new suppressions open siblings of that same low-charset-diversity
   family; independent re-scan of the estate against the claimed result
   (12 clean stay clean; the two exposed repos 2→9 and 25→26).
4. **Security & privacy:** the delta *is* the security lens; also verify
   the "test values are synthetic / two real values removed before
   commit" claim (no live credential in the test file or its history).
   `/security-review` reach: landed delta, nothing in flight — discharged;
   the probes below are the mechanical floor.

---

# Verdict — PASS-WITH-FINDINGS (0 MAJOR / 1 minor / 3 notes)

Committed before the triage session record was opened; reconcile below.
Provenance repeated per rule 4: non-author Fable taker, not spawned by the
delta's author.

## Re-run and verified

- **All four red legs reproduce** on synthetic fixtures, old scanner
  (`dd902aa^`) vs HEAD: the prefixed env-var assignment (missed → flagged);
  the extensionless secret-store path (false-positive → clean); the
  unclosed `$(` collision (missed → flagged); the stray-bracket value
  (missed → flagged). The three introduced-FP fixes hold (minified JS and
  the kebab enum clean; no new FPs from the `_LEAD` change — `BYPASS`- and
  `passport`-shaped neighbours stay silent).
- **Estate re-scan, independent:** 12 repos clean — exactly the claim —
  and one exposed repo reproduces at 9. The second measures **4 today
  against the claimed 26**; consistent with post-landing remediation
  rather than a wrong claim, checked at reconcile (SF4).
- **The synthetic-values claim holds for everything committed:** both
  blobs of the test file (the PR-branch commit and the squash) contain
  only demonstrably synthetic values (sequential alphabets, `ghp_0123…`);
  the file self-scans clean. What was never committed cannot be audited,
  which is the right way round.
- Suites: 759 + 207 green at HEAD in both environments (run earlier this
  session; HEAD includes this delta). `/security-review` discharged as the
  brief states.

## Findings

**SF1 (minor — lens 4, live-proven): the kebab-slug suppression swallows
hyphenated passphrases.** `password=correct-horse-battery-staple` — a
diceware-style shape real people really use — was flagged by the old
scanner and is clean under the new one (`SLUG_RX`). Grading honestly: the
snake_case twin was *already* exempt via the identifier rule, so this
completes a pre-existing hole's other spelling rather than opening a
fresh class — but the cost is real, on the security floor, and the commit
names the kebab fix's benefit without naming this cost, which is the
"named, not hidden" discipline failing for exactly one sentence. Remedy
belongs with the SF2 ruling: it is the same low-charset-diversity family.

**SF2 (note — the queue's ruling ask, sharpened by probe): the
lowercase-hex gap is half the size stated, and cheaply closable.**
Probed: a *digit-leading* 32-char hex secret already flags (the
identifier rule requires a letter/underscore start); only *letter-leading*
hex slips — roughly 6/16 of random hex keys. Counsel for the ruling: a
whole-shape carve-out — a full-match `[0-9a-f]{32,}` (and the SF1
passphrase shape: four-plus hyphenated lowercase words) is *not*
identifier/slug-suppressed when it sits in an assigned-secret context.
The cry-wolf case is git SHAs, which rarely appear assigned to a
credential-named key; the carve-out is anchored in shape, not corpus.

**SF3 (note — the queue's first aimed question, answered): corpus
re-scan is a sound regression floor and an insufficient acceptance
test.** Its strengths here were real: it caught three FPs the fix
introduced, and each corpus-driven suppression carries a charset
rationale plus a synthetic pinned test, which is the right discipline.
Its blind spot is structural and SF1 is its live demonstration: a
suppression validated against one estate's true secrets (all
mixed-class) cannot see the credential shapes that estate happens not to
hold. Cheap upgrade: a standing adversarial fixture set of credential
*shapes* (env-var, hex, base64, passphrase, connection string) that must
always flag — gate changes run it beside the corpus re-scan. SF1 would
not have landed past it.

**SF4 (note — lens 2): the "25 → 26" estate figure does not reproduce
today** (measures 4). Expected cause is post-landing remediation
recorded in the triage this delta came from; confirmed or corrected at
reconcile below.

## Verdict

The four fragment-match fixes are real, each red leg reproduces, the FP
fixes hold, and the honesty discipline held everywhere except the one
sentence SF1 names. **Cycle closes** (0 MAJOR, terminal rule); SF1–SF4 to
Mike, with SF1+SF2 best ruled together as one family.
