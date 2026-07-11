# 2026-07-11 · instruments/ test floor — ccrepo & cctranscript earn their coverage (Opus)

The `instruments/` layer shipped in session 34 untested — stated honestly in the
ROADMAP, not silent, but a gap. `tools/`'s scanners each carry a unittest +
`--selftest`; the instruments carried nothing, and `cctranscript` had since grown
real rendering logic (wrapping, light markdown, per-message model tags,
right-align, exchange rules). This session closes the gap.

## The decision worth recording: the Node layer's test convention

This is atelier's **first Node test surface**, so whatever it picked set the
layer's pattern. Chosen: **Node's built-in `node:test` + `node:assert`** — zero
third-party dep, mirroring the `tools/` layer's "stdlib only, no pytest" floor.
No npm, no `package.json`, nothing for CI to install beyond Node itself. A child
repo copying atelier's floor inherits a Node test surface that needs only a
runtime, exactly as the Python one needs only `python3`.

## What shipped

- **Minimal, behaviour-preserving testability refactor.** Each CLI entrypoint
  guarded by `if (require.main === module)`; pure functions `module.exports`ed.
  ccrepo's disk-index build (which ran at module load and would throw on a
  runner with no `~/.claude/projects`) moved into `buildIndex()`, called only
  from `main()`. Three colour/tz-dependent functions (`fmtTime`, `dateOf`,
  `styleInline`) gained a defaulted param so a test can pin colour/UTC without
  touching globals — the default reproduces the exact prior behaviour for every
  real caller.
- **Schema-drift contract test** (`test_cctranscript.js`) — the whole rationale.
  A checked-in synthetic fixture (`fixtures/session-sample.jsonl`, hand-authored,
  no personal data) is driven through the real CLI; the `--json` output is
  asserted for role classification (user-prompt vs tool-result carrier), model
  mapping, timestamp/text extraction, and `--think`/`--tools`/`--full` gating.
  The Claude Code `.jsonl` schema is internal and shifts between releases — this
  is the test that fails loudly instead of the tool silently mis-rendering.
- **Pure-function units** — cctranscript: `friendlyModel` (incl.
  `claude-opus-4-8 → Opus 4.8`, bare `fable`, `<synthetic> → null`, unknown
  pass-through, trailing-date drop), `wrap`, `styleInline`, `humanDelta`,
  `fmtTime`/`dateOf` under `--utc`, `visLen`/`padLeftTo`, `extractText`. ccrepo:
  `symbolFor`, `shortModel`, `dayOf`, `zeroAgg`/`addTo`/`addChild`, the `label`
  dash-decode fallback, and the aggregation fold.
- **ccrepo integration, honestly scoped.** ccrepo shells out to `ccusage`
  (`execFileSync`). Rather than fake a pass, the aggregation was factored into a
  pure `aggregate(sessions, index, groupBy)` and tested over fixture ccusage
  rows (flat, `--by-model` with cache tokens folded into totals, `--by-day`
  bucketing, unmatched-session counting). Residual stated in ROADMAP + CHANGELOG:
  the `ccusage` invocation, JSON parse, FX conversion, and table render still sit
  behind an untested seam.
- **One stated fix, not a silent one.** The contract test surfaced that
  `cctranscript`'s explicit-`.jsonl`-path branch never recovered `cwd`/label via
  `cwdFromLog`, though every other session-selection route does — so passing a
  path printed "unknown repo". Fixed as a separate, stated step (it also lets the
  contract test guard the `cwd` log field).
- **Wired + recorded.** `ci.yml`'s floor job gains `setup-node` and an
  `instrument test suite` step (`node --test instruments/test_*.js`), zero-dep.
  ROADMAP item ticked with residual; CHANGELOG line added; publish-safety triad
  (leak/secret/licence) + linkscan re-run clean over the tree — one leakscan
  false positive (a bare `HH:MM:SS` clock time in a test reading as
  IPv6-structural) annotated `leakscan:allow` with reason.

## Grounding

EVIDENCE §14 — "an instrument you built is a source; it must not lie for you" —
is the doctrine this closes against: an instrument's self-report is a claim the
apex binds, and §14's "enforce by machine" clause names a test driving the
instrument as the cheapest place to catch a phantom-success. The instruments
now have that floor. 20 tests, all green.
