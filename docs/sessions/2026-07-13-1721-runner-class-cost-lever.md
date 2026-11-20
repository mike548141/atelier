# 2026-07-13 · 17:21 — runner class as a CI-cost lever (Opus)

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 82+1 -->
- [2026-07-13 · runner class as a CI-cost lever (Opus)](2026-07-13-1721-runner-class-cost-lever.md) — Mike found the Actions wastage runs deeper: **`ros` ran macOS runners for everything** — one of the dearest classes — when it's multi-platform by design and only two `tiki` pieces are genuinely macOS-specific. The compute-pool doctrine (session 55) named **run count** as the private-repo lever but was silent on **runner class**, the per-minute multiplier that sits above it (GitHub standard: **Linux 1× · Windows 2× · macOS 10×** — a whole suite on macOS burns the allowance ten-fold, almost always for no portability gain). Worse, the build layer *shipped* the anti-pattern: `ci-python.yml` ran lint + type-check + tests across a full `os:[ubuntu,macos]` matrix, manufacturing the ros waste in every repo that copied it. Landed: MODEL-ECONOMICS gains **"Runner class — the multiplier lever"** (multipliers; larger runners bill even on public; rule = *default every job to Linux, escalate only for the OS-specific slice in its own job*; ros the worked multi-platform case; blanket matrix named as anti-pattern); the private-repo lever line now names class as the other, larger lever; `ci-python.yml` rewritten to Linux-default with a commented, slice-scoped macOS/Windows job. **Owed:** fixing ros's own live workflows (its repo's follow-up); children adopt the new template at next pin bump.
<!-- archivecut:log-entry docs/SESSIONS.md 83+1 -->
- [2026-07-13 · addendum: the "when" lever + ros CI review (Opus)](2026-07-13-1721-runner-class-cost-lever.md) — Mike asked if *triggering* deserves the same scrutiny as runner class. Verdict: mostly already covered (path filters + `cancel-in-progress` were doctrine; every-push-vs-main is the visibility trade), one real un-named lever — **duplicate triggers** (unfiltered `push` + `pull_request` fires *twice* per push on a branch with an open PR). Added one cost-hygiene line to MODEL-ECONOMICS: scope `push` to the branches that need it unless the second run earns its minutes (merge-preview scan a tip-push can't see; fork-PR coverage). Skip-ci/debounce/gating the floor named as the over-engineering to avoid. atelier's own `floor.yml` template carries the overlap — two-sided, touches the deliberate N4 every-push call, so **logged under ROADMAP *Open questions*** for a future per-repo decision, not auto-fixed. **ros review** (Mike: queue, don't implement): its new CI is already good (Linux matrix, macOS gated off PRs, `push` scoped to main → no overlap); two minor trims — the 10× macOS job still runs lint+mypy+full-suite when only the Keychain test needs it, and `ci.yml` lacks `cancel-in-progress` — **queued in ros's own ROADMAP**, untouched otherwise.


Follow-on to the 15:44 compute-pool session. Mike found the Actions wastage runs
deeper than first thought: **`ros` was using macOS runners for everything** — one
of the dearest classes — when it's multi-platform by design and only two `tiki`
pieces are genuinely macOS-specific. The insight to encode: each repo should use
the **cheapest runner class** that does its work.

## The gap

The compute-pool doctrine (session 55) named **run count** as the private-repo
lever but was silent on **runner class** — the per-minute multiplier that sits
*above* run count and usually dwarfs it. GitHub's standard multipliers are
**Linux 1× · Windows 2× · macOS 10×**; a private repo running its whole suite on
macOS burns its allowance ten times as fast, almost always for no portability
gain (lint, type-check, build and most tests are platform-independent).

Worse, the build layer **shipped the anti-pattern**: `ci-python.yml` ran lint +
type-check + tests across a full `os: [ubuntu-latest, macos-latest]` matrix — so
every platform-independent check ran twice, once at 10×, for a "portability"
claim those checks don't actually test. The template was manufacturing the exact
ros waste in every repo that copied it.

## Landed (`22e8941`… → this commit)

- **MODEL-ECONOMICS**, compute-pool section — new subsection **"Runner class —
  the multiplier lever"**: the multipliers, that larger runners bill even on
  public repos, and the rule — *default every job to Linux; escalate to a dearer
  class only for the OS-specific slice, isolated to its own job so the multiplier
  lands on the minimum surface.* Single-platform → all Linux; multi-platform →
  Linux for everything portable + a narrow macOS/Windows job. **`ros` named as
  the worked case.** The blanket `os:[ubuntu,macos]` matrix named as the
  anti-pattern.
- Private-repo lever line updated: run count is *one* lever, runner class the
  other "and often the larger".
- **`ci-python.yml` template** rewritten: defaults to Linux across Python
  versions; the macOS/Windows job is now commented, scoped to marked OS-specific
  tests only (`-m macos`), one Python version, no lint/type-check — added
  deliberately, never by default. A runner-class rubric heads the file.

Scanners clean, pushed. No memory written — this is now repo doctrine, so the
existing "Actions minutes pool" memory needn't duplicate it.

## Owed

- **Fix `ros` itself** — this session hardened atelier's doctrine + template, but
  ros's live workflows still run macOS-for-everything. Retargeting them to Linux
  (bar the two tiki macOS pieces) is ros's own follow-up, in its repo.
- Children pick up the strengthened `ci-python.yml` at their next pin bump / when
  re-scaffolded; existing copies of the old matrix are each owner's cleanup.

## Addendum — the "when" lever + ros review (same session)

Mike asked whether triggering deserves the same scrutiny as runner class, or
whether that's over-engineering. Verdict: **mostly already covered, one real
lever, the rest is too much.** Path filters and `cancel-in-progress` were already
doctrine; every-push-vs-main-only is the documented visibility trade. The one
un-named lever is **duplicate triggers** — an unfiltered `push` + `pull_request`
fires *twice* per push on a branch with an open PR. Added one line to
MODEL-ECONOMICS cost-hygiene (`26f…`-ish): scope `push` to the branches that need
it unless the second run earns its minutes (merge-preview scan a tip-push can't
see; fork-PR coverage). Skip-ci tokens / debounce / gating the safety floor named
as the over-engineering to avoid (cost is optimised last).

**Left as a decision, not auto-fixed:** atelier's own `floor.yml` template carries
that overlap (`push:` all-branches + `pull_request`) — free on public atelier,
metered on private children. Two-sided (merge-preview + fork-PR coverage is real)
and it touches the deliberate N4 every-push call, so logged under ROADMAP *Open
questions* for a future session to decide per repo.

**ros review (Mike: review, but queue findings — don't implement).** ros's
freshly-updated CI is already good: Linux routine matrix, macOS gated to
`if: github.event_name != 'pull_request'`, and `push` scoped to main in both
workflows (so no duplicate-trigger overlap). Two minor trims found and **queued in
ros's own ROADMAP** (`roadmap:` commit there, not implemented): (1) the on-demand
macOS job still runs `ruff`+`mypy`+full suite at 10× when only the Keychain macOS
test needs the runner — narrow to `-m macos`, drop lint/type-check; (2) `ci.yml`
lacks the `cancel-in-progress` that `floor.yml` has. Both left for a ros session.
