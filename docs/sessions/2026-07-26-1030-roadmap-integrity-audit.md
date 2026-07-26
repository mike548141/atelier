# 2026-07-26 · 1030 UTC · roadmap integrity audit — full-history reconstruction

**Session type:** audit / forensics. No doctrine change, no scanner built.
**Tier:** Opus. **Branch:** `main` (read-heavy; one record commit).

## Why this ran

Mike's standing worry, asked directly: *"one of my biggest worries for all
repos is losing the queue of ideas and work from the roadmap"* — items marked
complete that weren't, items moved to `ROADMAP-DONE.md` or back that shouldn't
have been, items deleted as duplicates that were not duplicates. Paired with a
health question on atelier's own CI and floor after an estate-wide push to
enforce policy as code.

The question is answerable, and had never been asked of the whole history.

## Method

Reconstructed every checkbox item that has ever existed in `docs/ROADMAP.md`
across all **362** commits touching it, plus the **50** touching
`ROADMAP-DONE.md`, by walking each commit's blob rather than its diff (a diff
loses items that move).

Per commit: items present in the parent's `ROADMAP.md` but absent from the
child's, then asked whether each landed in `ROADMAP-DONE.md` at that same
commit. Items unmatched there were given a second chance against today's two
files, then against the whole tracked-markdown corpus.

**Counts.** 540 distinct items ever existed; 231 exist today; 143 left
`ROADMAP.md` at some commit without an exact title-match arriving in the
archive. Those 143 were then resolved by hand.

## The finding: nothing is lost

All 143 resolved to one of four legitimate shapes. **Zero confirmed losses
within atelier's scope.**

1. **State-transition rewording (the dominant class).** An item's own title is
   rewritten at every step of a review cycle — `cold pass owed` → `claimed`
   → `RAN, rulings owed` → `applied, cycle closed`. Title-keyed matching reads
   each rewrite as a death plus a birth. Roughly two-thirds of the 143.
2. **Delivered work, reworded on harvest.** The archive entry describes the
   finished thing, not the request that opened it — so the request's wording
   survives nowhere. Verified case by case that the deliverable exists
   (`PRINCIPLES.md`, `EVIDENCE.md`, `SECRETS.md`, `docs/build/`, the wired
   scanners).
3. **Deliberate reduction on the principal's instruction.** `9b4fb63` replaced
   a 34-line premature finding with Mike's raw open question, by his explicit
   ask; the question was later answered and harvested
   (`ROADMAP-DONE.md`, *"ccarchive: is there any metadata it misses?"*).
4. **Correct non-carry of withdrawn material.** The 2026-07-26 0647 pass ran on
   the wrong tier and was rejected in full, findings unread. Its three review
   items are re-queued unchanged; the *fourth* line — a finding of the rejected
   batch — is deliberately absent, because reading it would defeat the
   rejection.

### The six-item capture stream, checked individually

The 2026-07-21 1233 UTC capture-only session parked six items from Mike's
estate note — the highest-risk cohort, since capture-mode items have no
deliverable to anchor them. All six accounted for:

| Parked item | State |
| --- | --- |
| Anti-slop invariant registry | ✅ delivered — S1–S5 scanners built |
| `MODEL-ECONOMICS` → `ECONOMICS` rename | ✅ done |
| Honesty vs truth vs transparency | ✅ live, `ROADMAP.md` — still Mike's, untouched |
| Grab the colleague AI chat | ✅ live, `ROADMAP.md` |
| ccarchive metadata coverage | ✅ answered + harvested |
| ccarchive / cctranscript merge | ✅ answered — keep-separate counselled, accepted |

### Adjacent corruption vectors, both clean

- **Archive truncation.** Exactly one commit ever removed more than 15 lines
  from `ROADMAP-DONE.md` (`30db1f0`, +30/−17) — a flag-rename rewrite of one
  entry, content preserved. The archive has never been meaningfully truncated.
- **Stale claims.** No live `[~]` items. Every `[~]` and `[x]` occurrence in
  `ROADMAP.md` today is legend or prose, not a list item — confirmed against
  `sizescan`'s cold-content gate reporting zero. A `[~]` abandoned by a dead
  session is the worst state to leave behind (a later session skips the item
  forever); there are none.

## The gap this exposed

`sizescan` guards the two *adjacent* failures and neither of them is this one:

- an `[x]` left on the hot path — **cold-content gate**, catches un-harvested;
- a live `[ ]`/`[~]`/`⏳` in an archive store — **harvest-integrity gate**,
  catches botched harvest.

Nothing detects an item **removed from `ROADMAP.md` that arrives nowhere**. The
tri-state grammar already forbids it — an item is flipped `[x]` with a
disposition, then harvested; it is never deleted — but the rule has no forcing
function, and this repo's own case law says a rule without one is a rule that
gets broken. That is the same family as the three prior instances, and it is
the specific mechanism Mike's worry names.

This audit found no instance of it in atelier. It found no *guard* against it
either, and the audit that proves the negative costs a full-history
reconstruction each time it is asked. **Decision owed (Mike):** build the
guard, or accept the manual audit as the control.

## CI and floor health

Green, and honestly so.

- `tools/floor.py --plane ci` exits **0**; nine scanners enforced
  (secretscan, leakscan, linkscan, reviewscan, sizescan, datescan, wrapscan,
  spellscan, licenscan). One advisory: `ROADMAP.md` over the ~300-line
  reference.
- **673** Python tests OK · **207** instrument tests OK.
- Last twelve pushed runs: ten success, two cancelled by the
  newer-push-supersedes concurrency rule — not failures.
- **ADR 0008 honoured in the part that matters.** `ci.yml` and the reusable
  `floor.yml` both drive the one registry, `tools/floor.py`; the policy is
  called, not copied. The two YAML files duplicate *transport* only — a
  deliberate split, since `floor.yml` must two-checkout to fetch atelier's
  tools while `ci.yml` runs in-repo. That duplication is a real drift surface
  and is already named in the roadmap.
- Two scanners short of the registry: `pathscan` runs as a bespoke advisory
  step outside it, `stampscan` is unwired. Both are tracked with stated
  preconditions — honest, not silent.

## Un-queued anywhere: none — and the near-miss worth recording

Two items looked un-queued and both survived. Recording the near-miss because
it is the audit's own sharpest lesson.

1. **Personal context travels with the person, not the device** — alive and far
   advanced, as `ROADMAP.md` § *North star — context follows the person*. A
   design pass is delivered, D1–D5 are ruled with grounds, and two build items
   are open under it. The section even preserves the original 2026-07-10 item
   text verbatim under *"Original item, for context"* — the exact discipline
   this audit was run to test, working.
2. **The machine-local tool manifest** — `TOOLBOX.md` doctrine landed in full,
   and the inventory it prescribes is subsumed by that same north-star item,
   which names *instance/identity/toolbox (accounts, venv paths, domains)* as
   tier-2 content the portable store must carry.

**Lesson for anyone re-running this.** Title-keyed matching is the wrong
instrument, and its false-positive rate is near-total: an item's title is
rewritten at every state change, and a *well-kept* roadmap re-homes an item
under a section that reframes it. Both look identical to a deletion. Only
reading the candidates resolves them — which is why this record exists, so the
reading is done once.

## Owed

- 🎯 Mike: build the deletion guard, or accept the manual audit as the control.
- 🎯 Mike: `ROADMAP.md` is 1534 lines against a ~300 reference, and all of it
  is live current-truth (zero `[x]` on the hot path). Nothing is mechanically
  owed. Trimming live narrative is a judgement call that risks exactly the
  loss this audit was run to disprove, so it was **not** done unprompted.
