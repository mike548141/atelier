# Session — Track B: making the enumerator real

- **Date**: 2026-07-28 12:33 UTC (claim) → 13:15 UTC (close)
- **Tier / spawn**: Opus, Mike-spawned. Mike opened with *"I am thinking the
  policy as code and pipeline/CI/runners work but you may have things that are
  more important or more urgent"* — and the roadmap's own sequencing agreed:
  Track A (the only track with live exposure) closed 2026-07-28, nothing else
  carries a 🔥, and Track B **is** the CI/runners track.
- **Worktree**: `track-b-enumerator`. Five commits, plus one in the estate root.
- **Subject**: Track B end to end — B1 (schedule the conformance check), B2
  (`--status`), B3 (the Actions-disabled blind spot), B4 (the roadmap-deletion
  guard).

## The decision Mike made

**B1, option B** — the scheduled `floorfleet` run lives in the private
estate-root repo, not in atelier's public CI. Asked with the token cost stated
up front, because the credential is the whole substance of the choice. A, C and
D closed unchosen in the same pass, all four preserved verbatim with their
dispositions in `ROADMAP-DONE.md`.

## What happened

**B2 + B3 landed together** because they are one defect: a board answering *is
it wired* while reading as though it answered *is it working*. Wiring is a fact
about a FILE, and a file cannot tell you the runner was ever switched on.

🔎 **The first live run is the finding.** `--remote --status` reported all 13
children `wired ✅` — and **5 of 14 repos had been RED on their default branches
since the 2026-07-25 rollout**, three days unnoticed, every one of them fully
conformant on the old board. Verified against the Actions API run-by-run before
being believed. The roadmap entry had predicted this exact shape; it was not a
hypothetical. Those five reds are now open work belonging to the child repos,
recorded generically here — a private repo's name beside its posture is the join
this repo has already breached three times.

**B3's proposed shape cost more than it needed to.** The item suggested reading
`actions/permissions` per child. That endpoint requires GitHub's
**Administration** permission — the repo-*settings* permission — so requiring it
would have widened the scheduled check's token across the whole private estate
for one boolean. Read authoritatively when the token carries it, inferred from
run history when it does not, and the board **declares which authority
answered**: a board that cannot say how well it knows something is the same
failure as one that reports green on nothing. Permission requirements were read
from GitHub's published reference, not assumed.

🔎 **B1's costing was wrong, and the reason generalises.** The item read "the
work is small: the schedule, `--check` wiring, and a failure message", on the
premise that `--remote` was remote end-to-end. It was not — it read each repo's
CONTENT from GitHub and still DISCOVERED children by walking directories beside
the atelier checkout, so a runner would have found nothing and exited 2.
Fail-safe, but not a check. At the right altitude: **the estate this board could
see was the estate that happened to be cloned on one laptop.** `--from-github`
was the real work, and it closes the blind spot the tool documented about itself
as a side effect. It also lists unenrolled repos: swept 6, of which 3 are public
and are exactly the three the roadmap already names, so that figure was right.

**Two bugs found in the building, both the programme's organising class — a
check that runs and covers nothing:** `users/{owner}/repos` returns PUBLIC repos
only (4 of 20 here), so an enumeration tool would have enumerated a quarter of
the estate and reported clean; and `_gh_json` accepted a `--jq` projection, which
prints a bare string that is not valid JSON, so the parse failed, the caller read
`None` as "head unknown", and the `behind` check **was inert on its first live
run without ever erroring**. The unit test had agreed with the defect because its
fixture modelled the wrong contract — noted at the fixture rather than quietly
corrected.

**B4 was built, measured, and deliberately not wired.** `harvestscan` catches
the one member of the harvest family that loses work: an item removed from
`ROADMAP.md` that arrives nowhere. Replayed over all 390 commits touching that
file, three successive *cause* fixes took the firing rate 42.3% → 30.8% → 26.9%,
each buying less than the last. One roadmap commit in four would still warn,
which is the rate that gets a guard `allow`-markered into silence. Counsel to
itself is `stampscan`'s: do not wire, not even advisory. `SURVIVAL_SIMILARITY`
was left alone on purpose — moving it to improve the number would be fitting a
constant to the corpus it is measured on. The signal is real, though: replayed
against `dd7fcb74` (the 185-line heading-only deletion that lost a completed
item) it reports 2, including work that genuinely vanished. The detector works;
the discriminator does not.

## State at close

Suite 759 → 795 Python tests, plus 207 Node, all green. Floor green on every
commit. `floorfleet --remote --check` exits 0 (conformance intact);
`--remote --status --check` exits 1, correctly, on the five red floors.

## Owed

- ⏳ **Two rule-4 cold passes queued in their landing commits**: B2+B3
  (`floorfleet --status`) and B4 (`harvestscan`). The B4 pointer asks its
  reviewer to test the *verdict* as well as the code — the author reached
  "do not wire" on his own instrument.
- ✅ ~~B1 blocked on the token~~ — **CLEARED the same session.** Mike minted
  `FLOORFLEET_TOKEN` (read-only, expires 2026-10-27, all repos, actions + code
  + metadata, no Administration) and set it himself, so the value never passed
  through an agent. A dispatch run then proved the path on a runner with no
  local clones: 14 repos enumerated from GitHub, all run statuses read, exit 1
  on the five red floors — failing for the right reason, not on a config
  fault. 🔎 **The degraded-authority fallback proved itself in production**:
  the board printed *"Actions-off was INFERRED (not read) for 14 repo(s)"*,
  which is the design argument for declining `Administration: read` turned
  into a demonstrated fact. Full detail in `ROADMAP-DONE.md`.
- 🎯 The five red child floors, and B4's next step (fund the discriminator, or
  leave it as a hand-run tool before deliberate bulk deletions).

## Addendum — the B4 pointer, re-read at Mike's request (`7ca1f1d`)

Mike asked for the B4 review to be queued. It already was, in its landing
commit — but re-reading it found the pointer breaching the ROADMAP's own
**refs-only** ceiling: it seeded the pass's first question and volunteered the
author's doubt about his own verdict, which is precisely the material a taker is
supposed to meet cold.

🔎 **That is the third recorded instance of the same failure, and the sharpest
one.** The finding that records the first two lives in this same file and was
read hours earlier in this same session. Refs-only survived being *written down
as an open finding* and was then broken by the session that had just read it —
which is the argument for a forcing function rather than for restating the rule
again. The finding was updated to carry the third instance and a fix shape
(`reviewscan` knows the `⏳` grammar; a field not in {delta, intent record,
tier} is a finding), left as Mike's call to fund.

Two smaller corrections rode with it: both pointers named `SESSIONS.md` as their
intent record when the record is the session *file* — **ER4's exact shape,
reproduced before ER4 has even been ruled on** — and the B2+B3 delta list was
widened to what actually landed rather than the subset that existed when the
pointer was first written.
