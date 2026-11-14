# Held back — the evidence-window rule, the check declaration standard, the pre-flip settings gate, and the pinned review bound

Opened only once the reviewer's own findings are durably written (`REVIEW.md` rule 1). A floor,
never a fence. Written by the brief-writer (`cclive` lists it as session `fef270f6`), which did not
author the delta. Nothing here is a finding: these are questions, and facts read off the machine.

## The pointer's own questions

1. Do the census's marks hold against the checks themselves?
2. Does reading *enforce* as excluding warn-only checks swallow the rule?
3. Does the settings gate read every setting it claims?

## The brief-writer's questions

4. The rule's grounds are "the board's count, not re-measured", yet it lands as doctrine that can
   refuse a build and judge every existing check. Is a rule whose own test was never run on its
   grounds stated with the strength its evidence supports (V1)? Can the four cold passes and four
   killed builds be re-derived from the record, and does each really show a licensing context
   outside the window?
5. "It applies to existing checks too, and a check that fails it is a finding for the principal."
   The census marks Window short of the bar on several checks that block. Did the delta, or
   anything since, file those findings? If not, is the clause inert?
6. As landed, the rule left open whether an allow-marker brings the licensing context inside the
   window, while several blocking checks lean on markers. Was the rule decidable for those checks
   on the day it landed? (`2a6d7a41` answered it later; that edit is `160/1440`'s subject.)
7. A warn-only check escapes the rule. What makes a check that later moves from warning to block
   face the window question again? The design note says a move to blocking is a separate decision
   "with a date and a fleet probe first"; does any doctrine tie that move to this test?
8. `GUARDS.md` says the rule was "adopted" and the standard binds "as a review question"; the design
   note's status is "proposed". Which one binds a session building a new check today, and does a
   reader of either learn that?
9. `Window.fits` is one value per check, but the rule asks about "every plane the check runs on",
   and `hook` and `ci` are separate strings. Can the schema state a check that is inside on one
   plane and outside on another? Has the rule's third outcome, "the check is not built", any value,
   or is it meant to have none?
10. The machine column passes Grounding as `met` "if every replay resolves", while the doctrine
    says a replay passes only if "the test fails if the check stops firing". Is a machine `met` on
    that field consistent with "citation is not catch"? What would catch a replay that still
    passes with the check removed?
11. The citation grammar admits `board 320/200`. A board item is a record that changes, closes and
    moves to the archive store. Is a board item a rule a check can serve, by the standard's own
    "never restated" test?
12. The gate names "rulesets or branch protection" and reads `rules/branches/<branch>`. That
    endpoint returns ruleset rules; classic branch protection is a separate endpoint (fact 9). Does
    the gate read classic protection at all?
13. Settings the gate does not name: the repo-level `security_and_analysis` block (secret scanning,
    push protection, Dependabot), Pages, Discussions, Projects, forking, deploy keys, webhooks,
    environments and their secrets, Actions secrets and variables, collaborators and teams. Which
    does a flip change the exposure of? Is "every settings finding in the first child's post-flip
    review came through that gap" grounds for the five named, or for completeness?
14. LA7: is it true on the current free plan that branch protection and rulesets cannot be set on a
    private repo, and that fork-PR approval (a public-repo setting) cannot be set before the flip?
    If an organisation or paid plan changes that, does the gate say so? Is "One flip's
    observation" enough grounds for doctrine that accepts an unprotected window?
15. The rule-4 sentence says the taker "pins the bound to a fixed SHA in its claim". Any fixed SHA,
    including `HEAD` at claim time, which in the recorded case already sat four commits past the
    landing. Does the sentence say the pin is the landing commit? Rule 4 already puts the pointer in
    the landing commit, so the commit that adds the pointer is the landing: is that derivable now,
    without part (b)?
16. The principal's answer was put to him with `115/120`'s options; `115/010` said the decision to
    land its rule at all was his. Did *"Everything, on every check now"* answer that? `GUARDS.md`
    says both "adopted on Mike's 2026-11-09 answer" and "the wording is a proposal from
    `115/010`"; can both hold? `260/070` adds to the always-confirm list and `320/420`(a) changes
    rule 4, with no word of his recorded on either: was one needed?

## Facts read off the machine (2026-11-14 UTC, worktree at `2c1f0296`)

1. Re-run lines, all exit 0: `merge-base --is-ancestor dd3d60d4 HEAD`; `coldsweep --commit
   dd3d60d4`; `floor.py --list`; `floor.py --declarations`; `reviewscan` ("clean — 8
   post-2026-07-21 decision record(s) carry a review line; 238 review brief(s) …"); `pointerscan`
   ("clean — every queued-review pointer is refs-only and current"); the unit-test line, 113 tests
   OK in about 35 s. Python 3.14.6.
2. `dd3d60d4` touches no file under `tools/`. At that commit `tools/floor.py` holds 16 `why="`
   registry strings, matching the census's 16.
3. The census table is internally consistent: its ✅ counts are 5 + 3 + 9 + 5 + 2 = 24 of 80, so 56
   owed; no row has five ✅; three rows (`leakscan`, `pointerscan`, `sizescan`) have three. The
   brief-writer did not check any mark against its tool.
4. The replays the census marks ✅ exist at HEAD: `tools/test_indexscan.py` `DateRule` line 226 and
   `test_a_line_dated_before_its_file_is_flagged` line 242; `tools/test_pointerscan.py`
   `test_the_live_specimen_is_flagged` line 106; `tools/test_publishscan.py`
   `test_the_grounded_pattern_reds` line 43; `tools/test_board.py` `StagedPlane` line 836. Whether
   each fails when its check stops firing was not probed.
5. At HEAD `floor.py --declarations` prints "21 checks, 0 meet all five". `--list` shows 19 checks
   on the hook and CI planes; `--list --plane msg` shows the other two, `namescan` and `quotescan`.
6. At HEAD `tools/floor.py` lines 614–621 still say the allow-marker question is "carried, not
   settled" (`_MARKER_OPEN`), and `leakscan`'s window line in `--declarations` prints it, while
   `GUARDS.md` since `2a6d7a41` says a reasoned marker counts.
7. The design note's status line reads "proposed (design only; nothing built and no check
   changed)", unchanged at HEAD; `GUARDS.md` § *Before building a check* says "Adopted on Mike's
   2026-11-09 answer".
8. The gate's reads against atelier, each answered: wiki off, visibility public; Actions enabled,
   `allowed_actions: all`; default workflow permissions `read`, cannot approve reviews; fork-PR
   approval `first_time_contributors`; private vulnerability reporting `enabled: true`; one active
   ruleset; `rules/branches/main` returns `deletion`, `non_fast_forward` and `required_signatures`,
   all from that ruleset.
9. `gh api repos/mike548141/atelier/branches/main/protection` returns 404 "Branch not protected":
   no classic protection is set, and the protection `main` has comes from the ruleset alone.
10. `gh api repos/mike548141/atelier` returns a `security_and_analysis` block of five settings, and
    `has_pages`, `has_discussions`, `has_projects` and `allow_forking`; the gate names none of
    them. Their values are not recorded here, since this file is public.
11. A sweep of `skills/`, `docs/build/templates/` and `commands/` for `wiki` or `hasWikiEnabled`
    finds nothing.
12. Outside the board and the barred records, only `docs/method/REVIEW.md` (lines 225, 229 and 511) and
    `CHANGELOG.md` carry the rule-4 pin wording or "landing = queuing" (`coldsweep`).

The probes are not in the tree; each fact above is reproducible from the brief's re-run lines and
live reads, or a one-line `grep`.
