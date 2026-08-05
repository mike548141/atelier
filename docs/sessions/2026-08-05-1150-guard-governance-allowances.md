# Session — the guard governance model rebuilt, and Mike's three allowance rules enforced across all twelve scanners

- **Date:** 2026-08-05, 1150–1300 UTC
- **Model:** Opus 5 (1M context), wt: `guard-governance-allowances`
- **Ask:** Mike had given three rules to `card-guard` in the estate-root repo
  and asked whether they should be built into atelier's scanners. Answer: they
  already were, unevenly. He then asked for all three applied to all scanners,
  and — when the split I proposed looked over-cautious — for F1 done too.

## The three rules, as Mike stated them

Granting a named exception, narrowing a scanner, reducing scope:
**(a)** as narrow an allowance as possible, so nothing else is excluded by
mistake · **(b)** it fails noisy as it is scanned, and the exceptions are then
applied to remove the expected, explicitly accepted noise · **(c)** a clear
reason recorded — who, why, when.

Narrow, noisy, reasoned. They are now `method/GUARDS.md`'s stated intent.

## What was found before building

The survey mattered more than the build. Against the three rules the estate
scored: **(a)** largely met (line-scoped markers everywhere, `reviewscan`
already carrying a rule-scoped variant) · **(c)** met in **3 of 12** markers
and **1 of 8** ignore-file loaders · **(b)** met in **1 of 12** — `stampscan`,
which reports an exempted block as a `skipped` finding rather than dropping it.

The structural cause is worth keeping: the convention lived as twelve
copy-pasted module headers with no single doctrine page, so whichever variant
got copied next propagated. Nine of twelve carried the weak one.

**`floor.py` was already the exemplar** — it refuses a bare `disabled` list,
demands `{scanner: reason}`, requires `why` + `review-by` on every advisory,
and reports both. (a)+(b)+(c), complete, built before the rules were written
down. The per-scanner hatches were the laggards, not the model.

## F1 — the rebuild, and why it was buildable now

I first proposed holding rule (a) back because F1 (the guard governance frame)
was open with a ruled design owed. Mike asked why it could not all be done now.
He was right and I was wrong: F1's rulings FG1–FG6 *were* the constraints, this
session was the pickup, and nothing was blocked. The only real constraint was
that self-authored doctrine cannot be reviewed by its author — which governs
closing, not building. The `⏳` pointer is queued accordingly.

`method/GUARDS.md` discharges all six:

- **FG1** — visibility (P3) declared **in** scope as a *rule* (a repo's
  visibility adjusts the response — CVSS's environmental group in our
  vocabulary) and **out** of scope as *mechanism* (declaration + platform
  cross-check stays P3's build). Adoption/first contact mapped in as
  repo-granularity deferment rather than bypass (C3). Silence was the one
  answer FG1 forbade.
- **FG2** — tested, not inherited, as ruled. *The test:* does a lawful downward
  lane already exist? *The result:* it does, in three places — allow-marker,
  ignore glob, floor advisory. So escalate-only never described this estate; it
  described the *tool's* authority in words that also forbade what we do daily
  and correctly. Restated as **provenance**: a guard may never lower its own
  response; a declared, reasoned, principal-visible act may, carrying an expiry
  where the claim rots. E6d(i)'s supersession is flagged for Mike; (ii) and
  (iii) untouched.
- **FG3** — granularity as an explicit axis (line / check / repo), which is
  what makes rule (a) checkable at all; acceptance (indefinite + reason) and
  deferment (temporary + expiry) separated at every level rather than by
  granularity accident.
- **FG4** — prior art verified at pickup rather than trusted from the pass, and
  **it moved on two points**. Semgrep carries the full three-way split as
  distinct fields (`confidence` · `likelihood` · `impact`) and computes severity
  from likelihood × impact — the pass had claimed only that confidence and
  severity were distinct, so the frame is *more* exactly prior art than the
  review endorsing it knew. CodeQL separates assessment (`@precision`,
  `@security-severity`) from response (`@problem.severity`) explicitly. And
  CVSS v4.0 quarantines its time-varying metrics into the Threat group by
  definition, which independently grounds the expiry rule this estate had
  reached on its own reasoning. GitHub's validity checks verified too.
- **FG5** — the false-positive route specialises `PROPAGATION.md`'s
  resolved-upward with a pointer; no second original.
- **FG6** — untouched here; it belongs to the grammar build.

## The build, and what it caught

Twelve scanners, five commits. Rule (a) added rule-scoped markers where a
scanner genuinely has more than one rule — and **deliberately did not** where
it has one, with the reason stated in each `parse_allow` docstring so the
asymmetry reads as a decision. `stampscan` needed no change at all.

Three real defects surfaced, none of them theoretical:

1. **A prose mention was holding a live exemption.** A session log naming a
   loopback address, followed by the words "marked `leakscan:allow`", was
   exempt *because the sentence mentioned the marker*. CI runs leakscan
   structural-only full-tree, so it would have gone red there.
2. **A dual-marker form where only the second marker carried a reason** —
   `# secretscan:allow / leakscan:allow: fixture` — honoured on a bare
   substring match, in three live lines including the pre-commit test's planted
   secret.
3. **My own rule-(c) regex was wrong**, caught by datescan's existing DSR8
   test. I used `\S` for the reason's first character, which accepts `-->`, so
   `<!-- datescan:allow: -->` — a marker with no reason, in the commonest
   Markdown spelling — parsed and exempted. The house form has always been
   `\w`. Corrected across all seven scanners I had touched. That is rule (c)
   failing inside the change meant to enforce it.

**D1 (Mike ruled 2026-08-04)** rode along: an allow-marker exempts structural
rules only, the term list always runs. No test had covered it. Its consequence
is surfaced, not worked around — see below.

Ignore files got the other half of rule (c): a glob must state a reason, by
trailing `# reason` **or** a stanza comment. Accepting the stanza form was a
call — this estate's ignore files already document themselves that way, better
than a trailing fragment would, and publishscan's exact spelling would have
meant rewriting 31 live entries and losing that prose. All 31 pass unchanged.
An unreasoned glob is exit 2, not a warning.

## Honest notes

- **The tree now reports 3 findings a clean tick used to hide, and they are
  D1's doing.** The author's own published git identity (ADR 0005's named
  worked example) is exempt from leakscan's *structural* email rule by a
  reasoned marker, and D1 correctly stops that marker silencing the local term
  list too. But the reason on those markers is the same reason — ADR 0005 —
  not the different-reason case D1 was ruled against. D1 says fix it in the
  term list, which is machine-local config, but that list cannot express "this
  name is public in *this* repo". **Mike's call**, unresolved here. Hook plane
  (`--staged`) and CI plane (structural-only) are both unaffected; only a local
  full-cover scan is red.
- **Rule (b)'s numbers were invisible until now, and they are not small:** 37
  suppressions in leakscan, 14 in secretscan, 4 declarations in licenscan, all
  previously behind a bare `✓ clean`.
- **Full-tree spellscan (8) and wrapscan (11) findings are pre-existing** —
  measured identical before and after, in stores CI never scans. pathscan's 280
  likewise, and it is not in the floor registry at all. Checked rather than
  assumed, per the figures-wrong-both-ways rule.
- **`sizescan`'s counts travel by out-param**, not a changed return type: a
  dozen callers across selftest and tests would have churned for no gain.
- **A parallel session was live throughout** (`fable-cold-passes-0805`, five
  queued cold passes). It claimed on `main` before working; I stayed in a
  worktree, kept records to one late commit, and rebased twice — once over its
  claim, once over seven further commits. No conflicts.
- **This session was interrupted mid-flight** and resumed. State was
  re-established from a fresh read, not from context.

## State at close

Twelve scanners on the model; 993 tests green; hook and CI planes green. The
`⏳` rule-4 pointer for `GUARDS.md` is queued, refs-only. E6d(i)'s supersession
and the D1 term-list consequence are the two things owed to Mike.
