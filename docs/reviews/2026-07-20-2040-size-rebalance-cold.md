# Cold pass — size-signal rebalance: line-count budget → cold-content gate (delta `5e68923..910085f`)

- **Date/time**: 2026-07-20 2040 UTC
- **Spawn provenance (rule 4)**: taken from the ROADMAP `⏳` queue by a session
  Mike spawned with "do any review or fable dependent work" (Fable). This
  session authored none of: the rebalance delta (`5e68923`, `3ec8823`,
  `b5dc12d`, `7418b41`, `910085f`), the sizescan tool it reworks, the doctrine
  files it edits, or any record of the authoring session (Opus,
  wt: atelier-size-signal-rebalance). Claim landed on `main` (`c8a1222`)
  before this worktree was created; this brief is taker-written.
- **Named exposure**: before claiming, the taker read the full ROADMAP `⏳`
  entry — which is **not** refs-only: it carries the author's complete
  evaluative account (the ruling's rationale, the "shipped" list, "green **the
  right way**") and a *review:* paragraph seeding two attack sites ("reverses
  a dated ruling + reworks a gate with a **silent-failure mode**"; "SR2's
  re-grounding rides"). The taker also read the SESSIONS.md index line for the
  authoring session (another evaluative summary) and the five commit
  *subjects*. All of that is author framing — treated as claims to re-derive,
  not facts; the seeded sites sit below the divider until this pass's own
  findings are committed. The pointer's breach of rule 4's refs-only ceiling
  is itself in scope as a compliance observation.
- **Deferred material (opened only after findings are committed)**: the
  ROADMAP entry's *review:* paragraph (re-read for reconcile); the authoring
  session's record `docs/sessions/2026-07-20-2025-size-signal-rebalance-cold-content-gate.md`;
  the CHANGELOG entry; commit message *bodies* of the five delta commits; the
  records commit `910085f`'s diff except its two-line `sizescan.py` /
  `test_sizescan.py` touch (which is code, in scope immediately); the
  2026-07-19 ruling record the delta supersedes.

## What the work is (refs only)

Commits `5e68923` (tools/sizescan.py + test_sizescan.py rework;
.github/workflows/ci.yml; docs/build/templates/workflows/floor.yml),
`3ec8823` (docs/ROADMAP.md → docs/ROADMAP-DONE.md harvest), `b5dc12d`
(docs/method/RECORD.md module doc), `7418b41` (docs/method/PROPAGATION.md
child-block size spec, "SR2"), `910085f` (records + a two-line code touch).
In-scope at HEAD: those files, plus every other doc/template/skill that
states or relies on the size signal (REPO-STANDARD, PROPAGATION child block,
create-repo, tools/README).

## Lenses and the taker's attack surface

Lens 1 — approach & assumptions (named by the taker as its first act):

- **A1 — the cold-content definition must be decidable at scan time.** The
  gate now fires on "a completed `[x]` item on a checkbox-worklog file". Both
  halves are classifiers: what makes a file a *checkbox-worklog* file, and
  what counts as a *completed item*? Attack both edges: false positives
  (`[x]` inside code fences, templates, doctrine that *quotes* checkbox
  syntax, and above all **ROADMAP-DONE.md itself** — if the archive is
  classified as a worklog, the gate demands harvesting the harvest, an
  infinite regress) and false negatives (`- [X]` uppercase, `* [x]`,
  indented sub-items, a done-item written without checkbox syntax).
- **A2 — dropping length as a *gate* must not open an unbounded hole.** The
  claim is that prose-shaped cold content and thinness are "caught at
  review, not measured". Is that the standing one-sided honesty applied
  correctly, or does it retire the only mechanical bound on hot-path growth
  with nothing mechanical left? What, concretely, still fires on a hot doc
  that doubles in pure prose?
- **A3 — the new gate must fail loud, not silent.** A regex-shaped detector
  that misses is indistinguishable from a clean repo — gate green either
  way. Does the tool distinguish "scanned and found nothing" from "didn't
  recognise anything as scannable", and does the suite prove the miss modes?
- **A4 — SR2's "~50 lines" must be grounded in the class, not the current
  measurement.** The standing rule (grounded-budgets correction, 2026-07-18)
  bars setting a number from what the artefact currently measures. "Class-
  grounded on the block's seven-concern shape" is the author's claim: if the
  block as shipped is ~50 lines and the derivation is a restatement of that
  fact, the number is the anti-pattern wearing the rule's clothes. Re-derive
  it: does 7 concerns × stated lines-per-concern actually produce ~50
  independently of the current block?
- **A5 — the advisory must have a consumer.** Line count now "reports but
  never fails". Who reads the report? If nothing consumes it, it is dead
  code plus noise; if humans read it in CI logs, it can still induce the
  line-golf the ruling set out to kill — check what the advisory looks like
  in output and whether its framing invites minimisation.
- **A6 — "lossless" harvest is a diff-checkable claim.** The harvest commit
  removes ~66 lines from ROADMAP.md and adds ~19 to ROADMAP-DONE.md. A
  lossless *move* should conserve content up to formatting; a 3:1 ratio is
  prima facie compression. Verify item-by-item what was dropped and whether
  the drop is defensible summarisation-into-archive or silent loss.
- **A7 — fleet semantics flip silently at pin bump.** Children copy
  `floor.yml` statically; a pin bump swaps their gate's meaning (length →
  cold content) in one move. Is that transition stated where a child
  session will actually see it, and is the old gate's vocabulary
  (budget/GATED/limit) fully retired from every surface children copy?

Lens 2 — correctness & quality: re-run everything stamped "proven": the
suite count (267→282) and its pass; floor green at `main` HEAD; the retitled
ci.yml/floor.yml actually running sizescan in cold-content mode; no stale
line-count-gate phrasing at HEAD (grep sweep across method docs, build
templates, tools/README, skills); the two-line `910085f` code touch is what
its subject says (a date fix) and nothing more.

Lens 3 — completeness / harvest: what states the old size signal and wasn't
caught — REPO-STANDARD, the PROPAGATION child block *as templated for
children*, create-repo's scaffold, ROADMAP items elsewhere that reference
the line-count gate as live; whether the 07-19 tripwire-split artefacts are
coherently superseded or half-retired.

Live re-runs owed in scope: `test_sizescan.py` suite (count + pass);
`sizescan.py` against the worktree HEAD (and against a synthetic worklog
fixture probing A1's edges); the A6 item-by-item diff; the grep sweeps.

---

# Verdict — 2026-07-20 2047 UTC

**Provenance repeated (rule 4):** reviewed by the rule-4 taker named in the
brief — Fable, Mike-spawned ("do any review or fable dependent work"), author
of none of the rebalance, the tool, or their records. Findings below were
committed before any deferred material was opened. **Added exposure
discovered mid-run, named not denied:** (a) `git show` on `b5dc12d` printed
its commit *body* (an author account) before the taker switched to
`--format=`; (b) a date-sweep grep resurfaced the SESSIONS.md index line for
the authoring session, including its "2 were duplicate stubs already in DONE;
2 moved verbatim" claim — the A6 diff comparison below was derived from the
diff itself, and that claim is tested, not taken.

## Lens 1 — approach

**The rework is sound.** Gating only on content whose remedy is a lossless
move (a `[x]` item on a checkbox worklog) and demoting length to advisory is
the right shape: the gate can no longer demand a reword, and the advisory
remains the pointer to review-caught prose bloat, so dropping the length
*gate* opens no silent hole (A2 held). The A1 regress edge holds —
`ROADMAP-DONE.md` can never be a candidate (its basename is unmetered), so
the gate cannot demand harvesting the harvest. Fail-loud posture survives
(A3): missing path/root exit 2, the F1/F2 fail-open regressions are covered
in suite and selftest, and the budget hatch provably cannot silence the gate.
Fleet transition (A7) is coherent: `floor.yml`'s header tells an adopting
child that a red means harvest, and child adoption is tracked as an open
ROADMAP item.

## Live re-runs — all reproduce

- Suite: **282 tests, OK** (test_sizescan alone: 40) — the "267→282" claim is
  the full tools suite and checks out. `--selftest` OK.
- Floor at HEAD: `sizescan --check --root . .` → **✓ clean, exit 0** — green
  re-proven, and green *because* the four `[x]` items are gone, not because
  anything was trimmed (the harvest diff shows moves, no line-golf).
- Date correction (`910085f`): complete — every remaining `2026-07-21` at
  HEAD is a deliberate mention of the local-date discrepancy, not a stamp.
- A6 harvest: all four `[x]` items' content survives — two were stubs whose
  detail already lived in `ROADMAP-DONE.md` (triple cycle incl. the tiki→ros
  pointer at DONE:21; ccarchive audit), two were moved (see SR4 below).

## Findings

- **SR1 (MEDIUM, lens 2/3 — stale doc, adopter-facing).** `tools/README.md`
  § sizescan (~line 386) still documents the dead model at the same commit
  that removed it: "reports any **current-truth file over its line budget**",
  "Budgets are starting points, not law", the old per-file budget list — and
  no mention of the cold-content gate, which is now the tool's whole point.
  The module doc was rewritten; the adopter-facing README was not. This
  breaches the same-commit-currency principle the estate ratified the same
  day (DOCUMENTATION doctrine), on the surface a peer adopter reads first.
  *Counsel: rewrite the section to the cold-content frame (gate = `[x]` on a
  worklog, length = advisory reference); ~15 lines.*
- **SR2-C (MEDIUM, lens 2 — the re-grounded number is circular by the
  delta's own standard).** `PROPAGATION.md`'s new figure is **~50 lines**;
  the block as shipped measures **49**. The same delta's module doc defines
  exactly this as the anti-pattern: "a number picked to sit just above
  today's line count is circular: it can't be exceeded the moment it's
  written." The claimed derivation — seven concerns + heading/intro → ~50 —
  asserts the step from concern-count to line-count without grounding it
  (that step's ~6–7 lines-per-concern *is* the current block's density), and
  the earlier draft of the same text (`3ec8823`) said the quiet part aloud:
  "class-grounded on the block's **measured** shape". Mitigations are real:
  nothing gates on the figure, the text explicitly forbids reading it as a
  target, and the house's own SIZE_REFERENCE grounding ("where the fleet's
  healthy instances sit") is also measurement-of-healthy-instances — but
  there the class has n>1; here n=1 and the instance certifies itself.
  *Counsel — either: (a) keep ~50 but state the arithmetic (7 concerns ×
  ~6 lines each as tight-but-complete + ~4 heading/intro), making the
  derivation checkable when a concern is added or removed; or (b) drop the
  number entirely — the structural rule (one bullet per irreducible concern,
  each as tight as full statement allows; growth means detail belongs behind
  a pointer) already does all the work, and nothing consumes the figure.
  The taker leans (b): a number that nothing enforces and that tracks the
  measurement is decoration with a circularity liability.*
- **SR3 (LOW, lens 2 — detector edges).** `_COLD_ITEM` counts a `[x]` bullet
  *inside a fenced code block* on a worklog file (false positive — fail-loud,
  a red someone inspects) and misses `+ [x]` and `1. [x]` items (false
  negative — fail-silent, but requires non-house bullet style). Probed live;
  the suite covers neither. *Counsel: a fence-state toggle in
  `cold_item_count` plus two suite cases; the `+`/ordered forms can be added
  to the regex in the same touch.*
- **SR4 (LOW, lens 2 — overclaim in the record).** The authoring session's
  index entry claims the two non-stub items "moved verbatim". The
  hooks.atelierTools item did; the tripwire-split item was **compressed and
  reworded** in the move — the supersession note added (good), but the
  live-proven evidence detail and artifact list dropped, and "Children adopt
  at pin bump" survives only via the separate open fleet item. Defensible
  archive compression; not "verbatim". *Counsel: one-word fix in the session
  record/index ("moved, one with supersession annotation"), or accept as
  noted here — the archive content itself needs no change.*
- **SR5 (LOW, compliance — the rule-4 handoff ceiling, second consecutive
  breach).** REVIEW.md rule 4 caps the queue pointer at "refs only, no
  evaluative account". This cycle's `⏳` entry is a full evaluative account —
  the ruling's rationale, the shipped list, "green **the right way**", and a
  *review:* paragraph seeding two attack sites. The 2026-07-20 1355 pass
  named the same breach on the previous cycle's pointer. Per the estate's
  own rule-grammar principle, a rule breached by every author who meets it
  has a framing problem at the point of use, not a compliance problem.
  *Counsel: put the ceiling where authors write the pointer — one line in
  the ROADMAP header block (which already explains `⏳`), e.g. "pointer =
  refs only; the account lives in the session record."*

## Verdict

**PASS — 0 MAJOR / 2 MEDIUM / 3 LOW.** The mechanism is right, proven, and
honestly recorded almost everywhere; the two MEDIUMs are a stale adopter-facing
doc and a number that fails the delta's own circularity test. Per rule 3,
all findings on this self-authored doctrine are **Mike's to decide**; counsel
above, nothing applied by this pass.

## Reconcile — deferred material opened after the findings commit (`e2aa0a5`)

Opened: the authoring session record (2026-07-20-2025), the CHANGELOG entry,
the `⏳` entry's *review:* seeds, and the delta commit bodies.

- **The seeds landed where this pass had already looked.** "Silent-failure
  mode" → covered by A3/SR3; "SR2 rides" → SR2-C. No seeded site was missed;
  no finding here originated from a seed.
- **The author flagged three judgement calls; two were independently covered
  (detector = `[x]` only; advisory numbers retained — both endorsed under
  A2). The third deserves its own line: SESSIONS.md moved from gated to
  advisory-only.** The old gate could red a flat-log SESSIONS; the new one
  never can (SESSIONS is not a checkbox worklog). The author's reading of
  the ruling is faithful — a flat-log's fix is a split, not a machine-
  nameable lossless move — and RECORD.md documents the advisory as the
  regression signal. The residual is visibility: an advisory on a green
  build is only seen if someone reads the log. This pass endorses the
  change and names the residual for Mike rather than raising it as a
  finding — it is the ruling's own one-sided honesty, applied consistently.
- **SR2-C and SR4 both survive the author's account.** The session record
  restates the SR2 derivation ("derived from the block's *structure*, never
  from what it weighs today (measured 49)") — restating independence is not
  deriving it; the concern-count→line-count step remains ungrounded. And
  both the record and `3ec8823`'s body repeat "moved verbatim" — the diff
  shows the tripwire-split item compressed and re-tensed in the move, so
  SR4 stands as written.
- Nothing in the deferred material contradicts a finding or adds a new one.
