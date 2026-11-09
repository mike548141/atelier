# Every check declares five things: the schema, the report, and how far each check is

**Status**: proposed (design only; nothing built and no check changed) •
**Date**: 2026-11-09

**Review**: owed. A rule-4 design cold pass before this is built to, because
every check in the estate would carry this schema. Queued at landing by the
run that lands it; Fable work, so it waits for Mike's approval.

Commissioned on `115/120` and `115/010`; the folded-in fourth requirement is
the 2026-08-23 PT1 ruling (`GUARDS.md` § *The home*). Mike's answer of
2026-11-09, to options a session offered and so an answer, not a ruling in his
words: *"Everything, on every check now"*. Each check states every field now,
even where it fails the bar. The standard itself, what each field means and
what passes, is `GUARDS.md` § *What every check declares*. This note is the
schema, the readers, the report and the census. No `tools/` file is changed by
it.

## Outcome

A `Declares` entry beside `why` in the floor registry, read by `floor.py` and
reported without ever affecting an exit code. **All 16 registry checks fail the
bar today**, on at least one field; the best meet three of five. That is what
*"on every check now"* commits the build to, and the census below sizes it: 56
of 80 fields owed.

## The registry entry

One new optional field on `Scanner`, the dataclass in `tools/floor.py`:

```python
@dataclass(frozen=True)
class Unmet:
    """A field the check cannot honestly meet yet. Stating it is what the
    standard asks for; it is marked as failing the bar."""
    reason: str              # required, non-empty: why it is unmet
    owed: str = ""           # the board item that would close it, if any

@dataclass(frozen=True)
class Grounding:
    incident: str            # a board item, a verdict path, or "injected: <defect class>"
    replay: str | Unmet      # "tools/test_x.py::Class.test_name"

@dataclass(frozen=True)
class Window:
    hook: str                # what the hook plane reads, in words
    ci: str                  # what the CI plane reads, in words
    licensing_context: str   # the facts that would make a match acceptable
    fits: Literal["inside", "outside-directive", "outside-warn-only",
                  "outside-widened"]

@dataclass(frozen=True)
class Declares:
    rule: tuple[str, ...] | Unmet             # citations, see grammar below
    grounding: tuple[Grounding, ...] | Unmet
    purpose_gap: str | Unmet                  # one sentence, a need of the rule
    window: Window | Unmet
    posture: Literal["cheap-failure", "forbids-the-act"] | Unmet
    posture_cost: str = ""                    # the recovery built, or the freedom given up
    reviewed: str = ""                        # the verdict that read the rule against the check
```

`Scanner` gains `declares: Declares | None = None`. `None` means *missing*,
which is a state the transition passes through and is the only state a child's
`local` check can be in until it declares. The registry is where the field
lives because the principal ruled it so (2026-08-23), and `why` stays.

**Citation grammar for `rule`** (each string one of): `docs/method/<file>.md § Heading`,
a path under `docs/decisions/`, `ADR 0008`, or `board 320/200`. Prose is not a
citation, which is the point: a restated rule is the thing being retired.

**Replay grammar:** `path::Class.test_name`, a test the suite already runs.

A worked entry, `indexscan`, from what its docstring already says:

```python
declares=Declares(
    rule=("board 200/010",),
    grounding=(Grounding("board 320/430",
        "tools/test_indexscan.py::DateRule."
        "test_a_line_dated_before_its_file_is_flagged"),),
    purpose_gap="whether a file belongs in the index is the index-keeper's "
                "call; the check sees presence and date only",
    window=Window(hook="whole tree", ci="whole tree",
        licensing_context="the index-keeper's judgement that a file is listed "
                          "correctly or left out on purpose",
        fits="outside-warn-only"),
    posture="cheap-failure",
    posture_cost="an unlisted file still commits; the fix is one line",
),
```

## What reads it

1. **`floor.py --list`** adds one column, `decl 2/5`. Today's columns are
   unchanged.
2. **`floor.py --declarations`** (new) prints the full table per check, and
   `--json` carries a `declarations` key on every run, always present, so a
   consumer's field set stays comparable.
3. **The CI plane and `floorfleet`** carry one summary line, for example
   `🟡 declarations: 16 checks, 0 meet all five (floor.py --declarations)`. The
   hook plane prints nothing, so an unrelated commit never pays for this.
4. **`tools/test_floor.py`** pins that every registry entry has a `Declares`
   and that every `replay` string resolves to a real test method (`ast`, no
   import and no run). The replays themselves run as ordinary tests in the
   ordinary suite, so no new runner exists.

Per field the reader computes one of `met`, `resolves`, `unmet` or `missing`:

| Field | Machine can say | Only a reviewer can say |
|---|---|---|
| Rule | `resolves` (the path and heading, ADR or board item exists) | `met`, recorded in `reviewed` |
| Grounding | `met`, if every replay resolves | Whether the replay really fails when the check stops firing |
| Purpose gap | `met`, if non-empty and not the `why` text | Whether it names a need of the rule |
| Window | `met`, if `fits` is present | Whether the licensing context is really inside |
| Posture | `met`, if one of the two words | Whether the cost is honest |

## How a miss is reported

**Warning first, and only a warning.** A check that fails the bar is marked on
the surfaces above; none goes red, and no exit code changes on any plane, in
keeping with his order for the six new checks: *"all six, warnings at first and
then move to blocking action"* (`320/810`). This design proposes no move to
blocking. That is a separate decision of his, with a date and a fleet probe
first. A malformed `declares` in a child's `.atelier-floor.json` is reported as
*missing* and is never a `ConfigError`: a warn-first field must not be able to
fail the floor closed.

`missing`, `unmet` and a failed field all render the same way: a mark, with the
reason. The difference is whether a reason exists, which is what the field
exists to surface.

## How the build splits

**Step 0, one lane:** the dataclasses, the `Scanner` field, the reader, the
`--list` column, `--declarations`, the `--json` key, the CI line and the
`test_floor.py` pins, with all 16 `Declares` written from the census below,
`Unmet` wherever the census has no ✅. One lane, because `tools/floor.py` is a
contended file and registry entries are its most-edited part. After step 0
every check states every field, which is his instruction, and the rest of the
build only turns `Unmet` into met.

**Then one lane per group, run in series on `floor.py`:**

| Group | Checks | Owed fields | What the lane does |
|---|---|---|---|
| A, boundary | `secretscan`, `leakscan`, `publishscan`, `licenscan` | 14 | Tie canaries to named incidents or mark them `injected`; settle the allow-marker question (below) with Mike or a cold pass first |
| B, integrity that blocks | `conflictscan`, `linkscan`, `reviewscan`, `board`, `sizescan` | 18 | Name replays for incidents already on the record; write missing rule citations |
| C, prose conventions | `datescan`, `wrapscan`, `spellscan` | 11 | Least grounded: `wrapscan` and `spellscan` have no named incident |
| D, warn-only | `harvestscan`, `pointerscan`, `pathscan`, `indexscan` | 13 | Window is mostly settled by being warn-only; the work is citations |

**Group E, outside this census and owed by the same answer:** the checks that
are not `SCANNERS` entries (`signscan`, `stampscan`, `blockscan`, the
`visibility` line in `floor.py`), each child's `local` checks, and the six new
checks being built under `320/810`, which should arrive with a `Declares`.

## Census, 2026-11-09

Read from `tools/floor.py`'s `SCANNERS`, each tool's module docstring and its
test module, read-only. One reader's pass, not a review. Each cell states what
is there now, against the standard's pass bar:

- ✅ meets it · 🟡 something real, short of the bar · ❌ nothing found
- **Rule:** ✅ names a passage · 🟡 names a document, a board item or a review
  with no section · ❌ no rule text cited. The registry's `why` strings cite
  nothing in any of the 16; every citation is in a docstring.
- **Incident and replay:** ✅ a test that names the incident · 🟡 an incident
  named with no replay, or a canary or fixture not tied to a named incident ·
  ❌ none named.
- **Purpose gap:** ✅ states what the rule needs and the check does not
  measure · 🟡 technique limits only · ❌ none.
- **Window:** ✅ states what would license a match or why it cannot judge it ·
  🟡 the plane is readable from the registry's argv and comments, the licensing
  context is not stated · ❌ neither.
- **Posture:** ✅ declared · ❌ undeclared.

| Check | Rule | Incident and replay | Purpose gap | Window | Posture |
|---|---|---|---|---|---|
| `secretscan` | 🟡 names the SECRETS doctrine | 🟡 `CanarySuite`, shapes | ❌ | 🟡 | ❌ |
| `leakscan` | ✅ REPO-STANDARD § Personal data | 🟡 `PIICanarySuite`, shapes | ✅ | ✅ | ❌ |
| `conflictscan` | 🟡 `320/200` | 🟡 incident named; fixtures of its shape, none names it | 🟡 | 🟡 | ❌ |
| `linkscan` | 🟡 PROPAGATION.md | 🟡 `020/320` tested; none for the rule itself | 🟡 | 🟡 | ❌ |
| `reviewscan` | ✅ REVIEW.md and the 2026-07-18-0820 record | 🟡 F6 named, no replay | ✅ | 🟡 | ❌ |
| `publishscan` | ❌ F1 cited, not the rule | ✅ `test_the_grounded_pattern_reds` | ✅ | 🟡 | ❌ |
| `sizescan` | 🟡 his ruling, restated | 🟡 three-thousand-line roadmap, no replay | ✅ | ✅ | ✅ forbids |
| `board` | ✅ ADR 2026-08-15 | ✅ `StagedPlane` (BS1's slips) | ❌ | 🟡 | ❌ |
| `datescan` | 🟡 seam S3 | 🟡 five-file sweep, no replay | ✅ | ✅ | ❌ |
| `wrapscan` | 🟡 seam S1 | ❌ regression proves an exemption | 🟡 | 🟡 | ❌ |
| `spellscan` | ✅ CONVENTIONS.md, quoted | ❌ | ✅ | 🟡 | ❌ |
| `harvestscan` | 🟡 HV1 | 🟡 `--replay` over real history, by hand, not in the suite | 🟡 | ✅ | ❌ |
| `pointerscan` | ✅ REVIEW.md rule 4 | ✅ `test_the_live_specimen_is_flagged` | 🟡 | ✅ | ❌ |
| `pathscan` | 🟡 seam S2 | 🟡 | ✅ | 🟡 | ❌ |
| `indexscan` | 🟡 `200/010` | 🟡 `320/430` residuals tested | ✅ | 🟡 | ✅ cheap |
| `licenscan` | ❌ | ❌ | ✅ | 🟡 | ❌ |

**Totals, of 16:** Rule ✅ 5, 🟡 9, ❌ 2. Incident and replay ✅ 3, 🟡 10, ❌ 3.
Purpose gap ✅ 9, 🟡 5, ❌ 2. Window ✅ 5, 🟡 11, ❌ 0. Posture ✅ 2, ❌ 14.

**Figures the board carried.** `115/120` said *"7 of 15 docstrings"* carry a
purpose gap; this pass finds 9 of 16 meeting the bar and 5 more with technique
limits. The two are not comparable: the 15 predates `conflictscan` and
`indexscan`, and neither count defines its line the same way. Its two canary
suites stand (`secretscan`, `leakscan`). Its *"at least four current guards fail
the bar"* is on this reading a low estimate.

## Not decided here

- **Whether an allow-marker brings a licensing context inside the window**
  (`GUARDS.md` names it as open). Group A cannot finish without it, and every
  scanner with a marker depends on the answer.
- **Where the threat-model declaration lives** (`GUARDS.md` § *Declare the threat
  model*, not decided there). The `Declares` shape has room for it; whether it
  joins this slot is a separate call.
- **When, if ever, a missing field goes red.** Not proposed.
- **The wider sweep** `GUARDS.md` § *The home* queues over the open board is
  unchanged by this note.

## Consequences

Every check will state its gaps where a reader can see them, and most of what
it states will read as unmet. That is the cost item `115/010` named, and his
answer accepts it. The registry grows by about 240 lines of `Declares`, in
one contended file. Nothing changes for any repo's exit code.
