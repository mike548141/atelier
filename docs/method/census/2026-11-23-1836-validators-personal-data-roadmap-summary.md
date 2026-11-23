# Enforcement census — the validators' own rules, the closed list, the board legend

Board item `020/220`, slice 8 of the census, the last. Run 2026-11-23 (UTC) by a
worker of queue run 608d. This is a measurement record, not doctrine: it changes
no rule, and it builds no guard. It uses slice 1's method, states and row format
(`docs/method/census/2026-11-16-1142-record-review-concurrency.md`) and the fold
conventions of slices 2 to 7, so the eight slices add up. Slice 7
(`docs/method/census/2026-11-23-1813-decisions-skills-commands-plugin.md`) is the
one this continues. It ends with the census-wide summary.

## What this asks

The earlier slices asked of each doctrine rule: if it is broken, what sees it?
The validators are different. They state rules about *themselves*: what each
check is, what it reads, what it passes on purpose, when it blocks. So the
question here is often reflexive: **does a validator's stated contract have a
test, a check or a host setting that reads a breach of it?** Each rule gets one
state, defined as in slice 1.

- **enforced**: a mechanical check reads the breach. The row names the check,
  the plane it runs on (the pre-commit hook, the commit-message hook, CI, a
  harness hook, a tool's own guard at the call) and whether it **blocks** or
  **warns**. *partial* means the check covers some of the rule.
- **directive-only**: nothing mechanical sees a breach. Where a self-run
  instrument would report it, the row says *instrument* and the state stays
  directive-only.
- **unenforceable, accepted**: the fact that would license or condemn the act is
  outside any check's evidence window, or the house has recorded a decision not
  to build the check. Accepted as of 2026-11-23.

A directive-only rule also gets the place its breach could be seen: **diff**,
**record** or **invisible**, as in slices 1 to 7.

## Method, and what it did not do

1. Read in full, at commit `a5a42bf6` (the commit the worktree was cut from):
   `tools/floor.py`'s module docstring and its registry (all 21 entries, read as
   data through `floor.SCANNERS`, with `floor.py --list` and `--declarations`);
   `tools/README.md` (3,333 lines, every section); `docs/PERSONAL-DATA.md`;
   `docs/roadmap/README.md`. Read for the folds: `tools/test_floor.py`,
   `tools/test_personal_data.py` and the test-name list of every registry
   scanner's suite.
2. **Not read in full, and not censused: `instruments/README.md` and
   `instruments/man/ccfleet.1`.** See *Remaining*. I read enough of the first
   to find one defect (below) and none of the second beyond its headings. Not
   half-censused: neither has a row.
3. A rule is a sentence that tells a future agent, or a check, to do or not do
   something. **A scanner section of `tools/README.md` counts its contract, not
   its description**: a block-versus-advise response, a fail-closed behaviour, an
   acceptance lane and its reason requirement, a date after which a response
   hardens, a prohibition on the reader. Not counted: usage lines; option
   lists; the lists of what a scanner cannot see (a declared residual is a
   measurement of cover, and each is named where the row it limits is); grounding
   stories; and design history. A scanner section that only describes what
   its code does, and whose breach would be a bug in that code, is graded on
   whether a test pins the description.
4. **The registry rows (`CHK1` to `CHK21`) are the one new kind of row in the
   census.** Each is the registry's own `why` for a check, read as a claim:
   "this check guarantees X". It is graded *enforced* when the check's own suite
   pins that behaviour, which is a lower bar than the doctrine rules' *enforced*,
   because the guard is the thing being graded. *Partial* here means the `why`
   says more than the check reads. *Doubts* gives the totals both ways.
5. Before writing *enforced*, I read the test names (every row cites them) and,
   for the claims that looked wider than their pin, ran the check or read the
   code: all 21 registry scanners' `--selftest` under the system `python3`
   (3.9.6) and the default `python3` (3.14.6); `floor.py --plane ci`;
   `pdlistscan.py` and
   `python3 -m unittest test_personal_data` over this tree; `board.py --check`
   over a scratch board with a fourth bracket; `ast.parse` over every
   non-test `tools/*.py` at `feature_version=(3, 9)`. Tests named in a row were
   checked to exist by script (*Doubts*).
6. Did not read the retired session index or the session records under
   `docs/sessions/` (the run's bounds).

### Folds

A rule these files restate from a censused document is not counted again.

- **`floor.py`'s docstring** restates, and slices 2 to 7 already count:
  advisory and disabled need a reason and a review date, and a lapsed date
  reports (`GRD20`); `sizescan` barred from 2026-12-09 (`GRD21`); `scope` and
  `flags` on a never-softened check state a reason and may not neuter it
  (`GRD22`); a local check may not shadow a fleet name and a missing script
  blocks (`RST15`); a mandate's date never moves later (`GRD17`, `GRD18`); the
  visibility declaration and its one red (`AUT2`, `AUT3`); the five declaration
  fields (`GRD9`, `GRD1`, `GRD7`); the coverage line (`GRD24`); a child holds no
  list of checks (`PRO41`, `PRO42`); the registry's own tests (`DEC19`); the
  report-only rules (`SCT13`).
- **`tools/README.md`** restates: zero third-party dependencies (`DEC8`);
  SHA-pinned actions and the floating `@main` call (`TPL8`, `TPL6`, `PRO41`);
  the trust list at the child's pin and the deferred SBOM (`SGN6`, `SGN16`);
  the marker and ignore-file reason rules, the malformed-marker grace and the
  per-glob `review-by` (`GRD8`, `GRD14`, `GRD15`); the cold-content gate takes
  no acceptance (`GRD16`); the harvest, board and session-log stores
  (`REC22`, `REC24` to `REC27`); the decisions-index and review-line rules
  (`DEC2`, `REV33`, `REV41`); `coldsweep`'s bar (`REV7`, `REV9`, `REV10`);
  the commit-message plane's quote and name rules (`SOP1`, `PRO27`); the
  hook install and its failure modes (`TPL3` to `TPL5`, `CRP9`, `CRP10`);
  `blockscan`'s map and the stamp convention (`PRO3`, `PRO7`, `PRO8`); the
  review-tier hook (`modelguard`: `CON21`, `ECO` rows); `signscan`,
  `signfleet` and `floorfleet`, whose own docstrings the README says are their
  manuals (`SGN`, `PRO41`; see *Remaining*).
- **`docs/PERSONAL-DATA.md`** restates the closed list, who grants it, what it
  must say and that it is kept true by a test (`RST23` to `RST25`, `AUT10`);
  the new rows below are what the list adds beyond the standard's words.
- **`docs/roadmap/README.md`** restates the per-item layout, the generated
  index and its never-hand-edited form, the harvest's retirement, `[x]` flipped
  in the finishing commit, landing as queuing, the refs-only pointer and the
  claim form (`REC22`, `REC23`, `RST19`, `REV14`, `REV15`, `CON` claim rows).
  Its template twin was censused in slice 6; the live file differs from it in
  the legend's detail, which is where the new rows come from.

## tools/floor.py — the registry's own stated contract

New rules only; the folds above carry the rest. `FLR1` to `FLR12` come from the
module docstring and the contract tests beside it; `FLR13` is the one place a
test says in so many words that a drift is accepted.

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| FLR1 | A check that cannot run blocks and never passes: a missing scanner, an unparseable or unreadable `.atelier-floor.json`, an unknown scanner name and a request to soften a check that has no advisory form all stop the floor and print the remedy (*FAIL CLOSED*) | enforced (blocks, hook + CI) | `floor.py`'s `Config` loaders and `run`; `test_floor.py`: `test_missing_scanner_blocks_and_names_itself`, `test_unusable_config_blocks`, `test_rejects_unknown_scanner`, `test_rejects_softening_a_boundary_check`, `test_unreadable_config_raises_rather_than_defaulting` |
| FLR2 | The hook plane reads staged content at full cover and the CI plane reads the whole tree; `leakscan` carries `--require-terms` on the hook so its cover is full or the commit does not happen, and never on CI, where the machine-local term list cannot be (*The planes*) | enforced, partial (blocks, CI test) | `test_the_hook_plane_demands_the_term_list_it_claims_to_have`, `test_ci_never_demands_the_machine_local_term_list`, `test_every_scanner_runs_on_both_planes`. Which scanners read the staged diff and which read the whole tree is the registry's argv, not pinned scanner by scanner: `linkscan` reads the whole tree on the hook for a stated reason (a link breaks when a different file moves) and no test says so |
| FLR3 | A plane that gives less than full cover does not render as a plain pass (`full_cover_flag`; the 🟡 partial mark) | enforced (CI test, blocks the run) | `test_a_plane_without_full_cover_does_not_render_as_a_plain_pass` |
| FLR4 | The commit-message plane runs only checks that declare a `msg` template; the message file is required with `--plane msg` and refused elsewhere; on CI the same checks read the pushed range and only report; a child's `flags` cannot reach the message modes; a clone without the hook is told at its next commit | enforced (blocks, CI test) | `MsgPlaneTest`: `test_only_a_check_written_for_it_declares_msg`, `test_msg_plane_needs_the_message_file_and_refuses_it_elsewhere`, `test_namescan_reads_the_message_and_reports_only_on_ci`, `test_quotescan_reads_the_message_and_reports_only_on_ci`, `test_a_child_cannot_reach_the_message_modes_through_flags`, `test_commit_msg_note` |
| FLR5 | Three states, not two: **enforced** blocks, **warn-only** reports and can never block, **advisory** is a child's declared softening. The state is derived from the registry entry and never from a list of names; a child's declaration wins the state column; a warn-only check does not soften the exit code (*Three states*) | enforced, partial (CI test, blocks the run) | `ThirdRenderStateTest`: `test_the_three_states_render_distinctly`, `test_warn_only_is_derived_from_the_entry_not_a_list_of_names`, `test_warn_only_does_not_soften_the_exit_code`, `test_a_child_declaration_still_wins_the_state_column`. Partial: the derivation reads the registry argv for `--warn`, so a warning period inside a scanner is invisible to it (defect 1) |
| FLR6 | Which checks may be softened is the registry's call: a scanner is softenable exactly when its entry carries an advisory form, and a prose list of the exceptions is kept in step with the registry or retired (AP2) | enforced, partial (CI test, blocks the run) | `SoftenableListsPinnedToRegistry.test_floor_docstring_no_advisory_list` and `test_contributing_template_no_advisory_list` read the docstring's list and the template's list against `Scanner.advisory`. A third home, `tools/README.md`'s per-scanner prose, names none and is not read; ADR 0008's restatement is `FLR13` |
| FLR7 | An expired `review-by` is reported and blocks nothing (red on the floor line for an advisory, a warning for a disabled check and for an ignore-file deferment): a commit failing on a date set months earlier is how a forcing function becomes a `--no-verify` habit | enforced (CI test, blocks the run) | `test_an_expired_advisory_reports_but_never_blocks`, `DisabledEndDateTest.test_a_passed_date_warns_with_age_and_exits_zero`, `DefermentLineTest.test_the_exit_status_is_what_it_is_with_no_dates`. The property graded is the non-block; `GRD20` counts the date's presence |
| FLR8 | A local check's `run` resolves inside the repo (a symlink out is refused) and is invoked directly, never through a shell; a non-Python script needs its execute bit; an unrunnable script blocks cleanly; a local `why` cannot forge an Actions annotation (*The repo-local seam*) | enforced (blocks, hook + CI) | `LocalSeamTest.test_run_path_must_stay_inside_the_repo`; `LocalSeamInvocationTest`: `test_a_symlink_out_of_the_tree_does_not_execute`, `test_a_non_python_check_needs_the_execute_bit`, `test_an_unrunnable_script_blocks_cleanly_instead_of_crashing`, `test_a_child_authored_why_cannot_forge_an_actions_annotation` |
| FLR9 | Text a child writes into the config (`why`, reasons, keys) is stripped of control characters and bidirectional overrides before it reaches the floor line or the board | enforced (CI test, blocks the run) | `ControlCharacterTest`: `test_a_why_cannot_carry_an_escape_sequence`, `test_bidi_overrides_and_isolates_are_escaped_visibly`, `test_two_keys_collapsing_after_the_strip_refuse_loudly`, `test_the_rendered_line_carries_no_control_characters` |
| FLR10 | A `scope` path stays inside the repo (no `..` that climbs out, no symlink out, none starting `-`), and a scope that resolves to nothing blocks a check that may not be softened | enforced (blocks, hook + CI) | `test_scope_outside_the_repo_is_refused_at_parse`, `test_scope_escaping_via_symlink_blocks_at_the_guard`, `test_unresolvable_scope_blocks_a_check_that_may_not_be_softened`, `test_a_case_variant_scope_over_a_staged_secret_blocks_the_hook`, `G3GraceCannotBeExtendedTest.test_a_scope_path_cannot_carry_a_mode_flag` |
| FLR11 | A scanner that carries an advisory count prints exactly one count line a run, zero included; the floor reads it as a whole line from that scanner's own output; a missing line is `-1`, never `0`; drift reads red | enforced (CI test, blocks the run) | `AdvisoryCountContract`: `test_the_registry_declares_who_carries_a_count`, `test_a_missing_count_line_is_minus_one_never_zero`, `test_a_finding_line_cannot_pose_as_the_count_line`, `test_a_path_that_reads_like_the_count_does_not_move_the_board`, and a real-output match per carrier |
| FLR12 | `--declarations` and the `decl N/5` column only report: no exit code on any plane reads a declaration (*floor.py --declarations*) | enforced (CI test, blocks the run) | `DeclarationSurfaceTest.test_declarations_never_change_an_exit_code`, `test_the_ci_plane_carries_the_one_line_and_the_hook_plane_nothing`. Measured at this commit: 0 of 21 checks meet all five fields and 22 of 105 fields are met (six checks meet 2 of 5, ten meet 1, five meet none) |
| FLR13 | ADR 0008 Decision 2 restates the softenable set and is deliberately not tested: after acceptance an ADR is appended to and never edited, so a registry change must not be able to fail a test by way of text the repo has committed never to edit | unenforceable, accepted | The reason is the test's own docstring (`SoftenableListsPinnedToRegistry`: "A drift there is accepted, not caught"). It does not carry a date; accepted here as of 2026-11-23 on that reason, to `GUARDS.md`'s bar (the fact that would condemn the act is a change to a frozen record) |

## The 21 registry checks — each `why`, read as a claim

One row per `SCANNERS` entry, in registry order. The Guard column names the
suite that pins the claim and, where the claim reaches past what the check
reads, the gap. 21 `--selftest` runs pass under `python3` 3.9.6 and 3.14.

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| CHK1 | `secretscan`: no plaintext credential enters git history | enforced, partial (blocks, hook + CI) | `test_secretscan.py` (272 tests: `CanarySuite`, `Named`, `Assigned`, `BlockingSetNeverShrinks`, `BoundedMemory`). Partial by its own README: a context-free credential under 32 characters, a literal secret that begins like an indirection, and a novel vendor shape pass. Declaration `0/5` |
| CHK2 | `leakscan`: the shape of personal and estate data is caught before it is committed | enforced, partial (blocks, hook + CI) | `test_leakscan.py` (460 tests: `PIICanarySuite`, `BlockingSetPinned`, `RequireTerms`, `BinaryGate`). Partial: structural-only on CI by design, a paraphrased fact passes (its declared purpose gap), and the term list is machine-local so no repo test reads its content |
| CHK3 | `conflictscan`: no unresolved merge-conflict marker reaches git history | enforced (blocks, hook + CI) | `test_conflictscan.py`: `OpenerAndCloser`, `AmbiguityGate`, `Diff3Base`, `WholeTree`; runs over every tracked file type. A marker folded mid-line is not a marker line (stated) |
| CHK4 | `linkscan`: internal links resolve; thin anchor, fat pointer needs live pointers | enforced, partial (blocks, hook + CI) | `test_linkscan.py` (89 tests: `EndToEnd`, `ReviewFindings`, `SuggestedFix`). Partial by its README: reference-style links, links in raw HTML and a link whose destination spans two lines are invisible; external URLs are not fetched |
| CHK5 | `reviewscan`: a decision record states its review judgement, and a review brief keeps deferred material in a sibling file | enforced, partial (blocks, hook + CI) | `test_reviewscan.py`: `LineTest`, `DeferralPlacementTest`, `NotInScopeTest`. Presence only: whether "not warranted" was the honest call is unread (declared purpose gap) |
| CHK6 | `publishscan`: no file whose publication weakens the repo is tracked | enforced, partial (blocks, hook + CI) | `test_publishscan.py`: `PatternTest`, `PlaneTest`, `HistoryTest`. A denylist of path shapes; a novel file mapping the repo's defences passes (declared) |
| CHK7 | `sizescan`: current-truth files stay honest; archive stores hold no live state; no repo's board is a flat running log, and neither a report-only switch nor an off switch may be used to keep one | enforced, partial (blocks, hook + CI) | `test_sizescan.py`: `Hatches`, `HarvestIntegrity`, `ExitContract`; `BarredAdvisoryTest` (`test_the_date_is_the_ruled_one`). Partial until 2026-12-09: the two switches the `why` forbids still work as warned exceptions until then (`GRD21`), so the clause is aspiration for 16 more days. Prose-shaped cold content is read by nothing (`REC26`) |
| CHK8 | `board`: the generated roadmap index never drifts from its item files | enforced (blocks, hook + CI) | `test_board.py`: `Index.test_item_edit_flips_check_red`, `test_missing_index_is_stale_and_rebuild_heals`; the staged plane `StagedPlane.test_slip_a_is_caught_on_the_staged_plane` (the replay the declaration cites) |
| CHK9 | `datescan`: records date in absolute UTC, never a drifting "today" | enforced, partial (blocks, hook + CI) | `test_datescan.py`: `RelativeTimeWords`, `NonIsoDates`, `InvalidIsoDates`. **The `why` says more than the check reads**: a bare "today" with no date cue beside it passes by design and a test pins the pass (`TodayNarrowing.test_bare_today_far_from_cue_not_flagged`; about 2,650 such hits across the estate, per the README). The declaration's purpose gap names a different gap (the dated maintenance edit) and not this one (defect 2) |
| CHK10 | `wrapscan`: doctrine prose stays within its column budget | enforced, partial (blocks, hook + CI) | `test_wrapscan.py`: `BoundaryLength` (85 clean, 86 flagged), the five exemption classes. Partial: tables, headings, reference definitions, fenced and indented code and a single unbreakable token are exempt, and atelier scopes the check to `docs/method`, `docs/build` and `docs/decisions` (`.atelier-floor.json`, reason stated) |
| CHK11 | `spellscan`: NZ-English spelling across the doc surface | enforced, partial (blocks, hook + CI) | `test_spellscan.py`: `IzeFamily`, `StandalonePairs`, the exemption classes. A missing macron passes (declared); `license` and `practice` are deliberately off the denylist (`test_license_deliberately_not_denylisted`); atelier scopes it to the three doctrine directories |
| CHK12 | `harvestscan`: a roadmap item removed in a bulk deletion arrived somewhere | enforced, partial (warns, hook + CI) | `test_harvestscan.py`: `MustNotFireTest`, `MustFireTest`, `InvocationTest.test_it_never_fails_a_build`. Scoped to a change shedding 50 or more net lines; the similarity threshold is ungrounded (the reason it never blocks) |
| CHK13 | `pointerscan`: a queued-review pointer stays refs-only and stays true | enforced, partial (warns, hook + CI) | `test_pointerscan.py`: `GrammarTest`, `CycleStateTest`, `QueueStateTest`. Whether a phrase steers the pass is judgement-adjacent text (declared window) |
| CHK14 | `pathscan`: a repo path named in prose or a backtick span still resolves | enforced, partial (warns, hook + CI) | `test_pathscan.py` (179 tests); `PathscanPromotionTest`. Records are excluded by default (a closed board item, a session, a review), so "still resolves" holds for the live surface only; `.atelier-floor.json` narrows it further |
| CHK15 | `indexscan`: a hand-maintained index names every file in the directory it maps, and no dated line predates the file it links | enforced, partial (warns, hook + CI) | `test_indexscan.py`: `Unlisted`, `DateRule`, `AllowMarker`. **Opt-in per index**: an index with no `indexscan:maps` comment is never checked, so the `why` holds for the three indexes atelier declares and nowhere else. A date later than the file passes by design |
| CHK16 | `attribscan`: an attribution to the principal carries a quotation of him, a citation of where he said it, or says it is an agent's decision | enforced, partial (warns until 2027-02-08, then blocks) | `test_attribscan.py`: `DetectorTest`, `StagedPlaneTest.test_it_warns_before_the_date_and_blocks_from_it`. Reads the form, never the truth. Registered as `enforced` and rendered ✅ although it cannot block for 77 days (defect 1) |
| CHK17 | `pdlistscan`: in a public repo, personal data stands only where the closed list names it, and a marker is not a grant | enforced, partial (warns until 2027-03-08, then blocks) | `test_pdlistscan.py`: `PublicRepoTest`, `ScopeTest`. In scope only for a repo that declares itself public. **It reports 1 finding over this repo at this commit** (see `PDL3`) |
| CHK18 | `sweepscan`: where sibling worktrees exist, a commit names its files or declares the whole index | enforced, partial (warns, hook only) | `test_sweepscan.py`: `CommitFormTest`. Hook plane only, by construction (the signal exists only inside a commit); fires on most commits by its own measurement, which is why it never blocks (`CON6`) |
| CHK19 | `namescan`: in a public repo, no private name in a branch name or commit title | enforced, partial (warns until 2027-05-03, then blocks; msg plane) | `test_namescan.py`: `MessagePlaneTest`, `RangePlaneTest`. Term source is `leakscan`'s, so its cover is the machine-local list; on CI it only reports |
| CHK20 | `quotescan`: a commit touching the principal's prompt, or the agent's grant of authority, carries his words | enforced, partial (warns until 2027-05-31 for the prompt; the authority surfaces advisory always; msg plane) | `test_quotescan.py`: `MessagePlaneTest`, `AuthoritySurfaceTest`. Reads the form of a quotation, never whose it is; a floor copy with no stamp and a widening through a settings key other than `permissions` are invisible (declared) |
| CHK21 | `licenscan`: the declared licence is the one actually asserted | enforced, partial (blocks, hook + CI; opt-in) | `test_licenscan.py`: `TwoResponses`, `Expect`, `ScanRepo`. Runs only where the repo declares a `licence` (`ConfigTest.test_licenscan_is_opt_in`). A vendored file with a prose-only licence header is invisible (declared) |

## tools/README.md — the scanners' and tools' stated contracts

Rows `TRM1` to `TRM45`, in the README's order. Every row is a contract the
README states for the check or tool, where the folds above have not counted it.

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| TRM1 | A scanner's `--selftest` prints one verdict line and nothing else, in the form `selftest OK — <scanner>` when it passes (*the opening paragraph*) | enforced, partial (CI test, blocks the run) | `test_selftest_quiet.py` generates one test for each of eight scanners (seven of them registry entries: `board`, `datescan`, `pathscan`, `spellscan`, `wrapscan`, `conflictscan`, `sizescan`). Measured at this commit: all 21 print exactly one line, but only 12 print the stated form; nine print another (`secretscan`, `leakscan`, `linkscan`, `indexscan`, `licenscan`: `selftest OK`; `reviewscan`, `publishscan`: `<name> selftest: OK`; `harvestscan`, `pointerscan`: `<name> selftest: ok (0 failure(s))`). The README states the form as general (defect 3) |
| TRM2 | A relative path argument resolves against `--root`, never the working directory; an absolute target is taken as given; a path that is not there exits 2, so a scan covering nothing never reads clean (*`--root` and path arguments*) | enforced (blocks, CI test) | `test_mixed_root.py`: `test_relative_target_resolves_against_root_not_cwd`, `test_absolute_target_is_still_taken_as_given`; the exit-2 half is pinned per scanner (`test_nonexistent_path_is_an_error_not_a_pass` in `test_conflictscan.py`, `test_nonexistent_path_arg_is_usage_error` in `test_linkscan.py`, `test_missing_path_is_error_not_pass` in `test_sizescan.py`) |
| TRM3 | Under `--require-terms` a missing, empty or unreadable term list is exit 2 and never a degraded pass; without the flag it degrades with a loud "structural only" line; the CI form never passes the flag (*leakscan, Two layers*) | enforced (blocks, hook) | `test_leakscan.py` `RequireTerms`: `test_require_terms_fails_closed_without_list`, `test_an_empty_term_list_is_refused_under_require_terms`, `test_an_unreadable_term_list_is_exit_2_with_a_remedy`, `test_default_still_degrades_to_pass`; the CI half is `FLR2` |
| TRM4 | A tracked binary blocks until `.leakscanbinaries` accepts its exact bytes with a reason, and each metadata set it carries needs its own reasoned line; no glob, no `--disable` and no flag softens the gate (*Binary files*) | enforced (blocks, hook + CI) | `test_leakscan.py` `BinaryGate`: `test_an_unlisted_binary_blocks`, `test_a_changed_binary_blocks_again`, `test_a_reasonless_entry_is_a_config_error`, `test_an_ignore_glob_does_not_skip_the_gate_for_a_binary`, `test_disable_cannot_switch_the_gate_off`, `test_no_command_line_route_softens_the_gate`. "Look at each file, strip what you do not need" is the reviewer's act and is read by nothing |
| TRM5 | `--disable` refuses an unknown rule name and a withdrawn rule's name; a disabled rule's hits still report and the blocking set is pinned (*Networking repos*) | enforced (blocks, CI test) | `test_leakscan.py`: `test_disable_cannot_name_a_withdrawn_rule`, `test_disabled_rule_reports_without_blocking`, `test_disable_keeps_other_rules_blocking`, `BlockingSetPinned` |
| TRM6 | A staged positional is a repo-root-relative path in git's own spelling; `.`, `./docs` and `docs//` mean what git means; an absolute path, one that climbs out, one git does not know and a `--root` that is not the process's repo all exit 2 (*Wiring it in*; *report.py*) | enforced (blocks, hook) | `test_report.py` `StagedScopeResolution`; `StagedPositionalScope` in `test_secretscan.py` and `test_leakscan.py`; the per-scanner `Staged*` classes. Eight scanners read their positionals through `resolve_staged_scope` (stated); which eight is not pinned by name |
| TRM7 | `secretscan` has two responses: every named format, `assigned-secret` and `high-entropy` block and the blocking set never shrinks; `low-variety-entropy` and `exempt-private-key` report and never move the exit code, and ship with their consumers (hook prints them, CI re-prints all, the board carries the count) | enforced (blocks, CI test) | `test_secretscan.py`: `BlockingSetNeverShrinks`, `AdvisoryTier`, `AdvisoryRender`, `Suppression` |
| TRM8 | The carve-outs for safe indirections are bounded: a fingerprint carve-out is off on any line that names a credential key (AB1); a URL's host and path are excluded but its query string and fragment are scored; `!secret`, `${VAR}` and placeholders pass | enforced (blocks, CI test) | `test_secretscan.py`: `Fingerprints`, `UrlEntropyExclusion`, `UrlExclusionScopedToHostAndPath`, `HighEntropy` |
| TRM9 | A public certificate or public-key PEM body is exempt from the entropy rule only when all of: the label is exactly `CERTIFICATE` or `PUBLIC KEY`, the END line is found within 2048 body lines, every line is pure base64 of at most 76 characters on consecutive lines, and the decoded body is one DER sequence opening with a sequence; one stray line voids the block (*A public certificate's body*) | enforced (blocks, CI test) | `test_secretscan.py`: `PublicPemBody`, `PublicPemBodyWholeFile`, `PublicPemBodyStaged`; "each condition pinned by a test" is the README's claim and the class names bear it out |
| TRM10 | A file a `.secretscanignore` glob skips keeps one narrow check, real private-key material judged on decoded bytes; a hit is advisory and counted, and `--disable exempt-private-key` turns it off (*What an exemption still checks*) | enforced (warns, hook + CI) | `test_secretscan.py`: `ExemptPem`, `ExemptBareRun`, `ExemptBoundary`, `ExemptStaged`, `ExemptPrivateKeyBase`. Known gaps stated: a bare run under 100 decoded bytes, base64url, PGP blocks and a key split over comma-separated literals pass. The README says a later item may make it blocking |
| TRM11 | Peak memory is bounded by a constant independent of tree or file size: a streamed walk, fixed-size chunked reads, and a cap on findings held in memory; `memprobe` measures the real peak and `BoundedMemory` is the template every guard reuses (*Bounded memory*) | enforced, partial (CI test, blocks the run) | A `BoundedMemory` class (a `memprobe` subprocess measurement) exists for 14 of the 21 registry scanners (`secretscan`, `leakscan`, `conflictscan`, `linkscan`, `reviewscan`, `publishscan`, `sizescan`, `board`, `datescan`, `wrapscan`, `spellscan`, `pointerscan`, `pathscan`, `licenscan`); `harvestscan` has a time bound (`BoundedTime`); **six have neither**: `indexscan`, `attribscan`, `pdlistscan`, `sweepscan`, `namescan`, `quotescan` |
| TRM12 | Findings past `MAX_MATERIALIZED_FINDINGS` (50,000) are counted and printed and never dropped, so the headline total and the exit code stay true | enforced, partial (CI test, blocks the run) | `test_sizescan.py` `ColdItemListing.test_cap_holds_and_the_rest_are_counted_not_listed`; `test_pathscan.py` `FindingCap`; `test_linkscan.py` and `test_secretscan.py` carry the cap in their bounded classes. Not every scanner has a cap test (the README names `sizescan`, `linkscan`, `pathscan`, `secretscan` only) |
| TRM13 | `licenscan` has two responses: `high` (no LICENSE, a declaration contradicting it, a copyleft header in a permissive or custom repo, a failed `--expect`) blocks; `medium` is advisory, shown in its own block, counted on a line printed every run; a severity the tool does not know blocks | enforced (blocks, hook + CI) | `test_licenscan.py`: `TwoResponses`, `ScanRepo.test_copyleft_header_blocks`, `test_permissive_header_is_medium_only`, `Allowances` |
| TRM14 | `licenscan` is wired into the pre-publish scrub and CI's release job, "not the per-commit hook" | directive-only | diff: the registry's `licenscan` entry, which runs on both the hook and CI for a repo that declares a `licence` (defect 4). The README's advice to an adopter and the registry disagree; nothing reads either against the other |
| TRM15 | `conflictscan` flags an opener and a closer always, and a separator or diff3 base only inside an open region; the separator is exactly seven `=`; it reads every tracked file type and has no fenced-code exemption; an unclosed opener leaves the rest of the file open (*Four marker shapes*) | enforced (blocks, hook + CI) | `test_conflictscan.py`: `AmbiguityGate` (six tests), `Diff3Base`, `UnclosedResidual`, `WholeTree.test_all_file_types_are_scanned_not_just_markdown` |
| TRM16 | Tool-call markup saved into a file is an advisory finding, never blocking, counted every run; the flip to blocking is one edit once the estate is clean (*A fifth shape*) | enforced (warns, hook + CI) | `test_conflictscan.py` `ToolMarkupAdvisory`: `test_each_shape_is_an_advisory_finding`, `test_anything_not_exactly_the_shape_is_clean`, `test_it_never_blocks_but_is_reported_and_counted` |
| TRM17 | `worktree start` refuses an iCloud base and branches off the integration branch; `land` refuses `main` onto itself and uncommitted work; `remove` refuses uncommitted or unmerged work without `--force`; every command takes `--json` and exits 0 ok, 1 a guard tripped, 2 an environment error | enforced (tool's own guard, blocks at the call) | `test_worktree.py`: `test_start_refuses_icloud_base`, `test_start_off_main_not_current_branch`, `test_land_refuses_from_main`, `test_remove_guards_unmerged`, `test_remove_still_refuses_genuinely_unmerged`, `test_remove_refuses_when_no_integration_ref_exists`. Only when a session uses the tool (`CON2`'s class) |
| TRM18 | `pins` is read-only and never edits a child; the floor-copy report compares the copy with the floor at the child's own pin, not today's text; from 2026-12-09 `drift`, `unstamped`, `no-reference` and `malformed` fail `--check`, `skipped` and `unchecked` stay report-only, an archived repo is exempt only when GitHub confirms it, and no flag, variable or key moves the date (*The floor-copy report*) | enforced, partial (warns until 2026-12-09, then blocks) | `test_pins.py`: `test_a_child_at_an_older_pin_is_compared_with_the_floor_at_its_own_pin`, `test_states_that_cannot_be_compared_are_reported_and_blocking_states_are_named`, `test_report_only_before_the_date_blocking_from_it`, `test_an_archived_repo_is_exempt_and_only_a_confirmed_one`, `test_the_gh_lookup_is_fail_closed`. Self-run (`pins` is an instrument): a child whose owner never runs it is not read, and `floorfleet`'s CI use is not wired |
| TRM19 | `pins --floor --child .` is a child's own verbatim check: exit 0 identical, 1 a copy that is `drift`, `unstamped`, `malformed` or `skipped`, 2 no answer; it never passes on no answer, runs offline and ignores the 2026-12-09 date | enforced (blocks, CI test) | `test_pins.py`: `test_floor_mode_is_the_childs_own_verbatim_check`, `test_floor_mode_no_answer_is_never_a_pass`, `test_floor_mode_reds_a_differing_copy_before_the_cut_off`, `test_floor_mode_json_carries_each_verdict` |
| TRM20 | `linkscan` reads internal links only, with the on-disk casing matched exactly, the target inside the repo root and an anchor matched exactly; code spans and fences are ignored; a scan it could not complete is exit 2 (*linkscan*) | enforced (blocks, hook + CI) | `test_linkscan.py` `ReviewFindings`: `test_case_mismatch_flagged`, `test_link_escaping_root_flagged`, `test_wrong_case_anchor_flagged_with_hint`; `EndToEnd.test_fenced_link_skipped`; `test_nonexistent_path_arg_is_usage_error` |
| TRM21 | A child's inlined floor block is not scanned for paths in a repo that does not hold the canonical file, and a stamped copy is still scanned where the canonical source is in the tree (320/610) | enforced (CI test, blocks the run) | `test_pathscan.py` `FloorRegionSkipped` |
| TRM22 | The cold-content gate takes no acceptance, and every hatch that does nothing is named and counted and changes no verdict: an unscoped marker, a glob and a leftover budget marker on a hot file are inert; a scope that names nothing recognised on an archive store reads as unscoped and is named; the retired `size-advisory` scope is still recognised (*sizescan*) | enforced (blocks, hook + CI) | `test_sizescan.py`: `Hatches.test_check_exits_1_through_every_hatch_and_says_so`, `InertHatches.test_inert_hatches_never_change_an_exit_code`, `test_a_marker_that_still_exempts_is_not_inert`, `test_a_scope_that_does_not_cover_an_archive_store_is_inert_and_does_not_exempt`. `GRD16` counts the no-acceptance half; the inert and unrecognised-scope behaviours are new |
| TRM23 | The gate names what it counted: each flagged file lists every completed item by line and text (60 characters, control and format characters dropped) so the move is a lookup, and the list is capped run-wide with the rest counted | enforced (CI test, blocks the run) | `test_sizescan.py` `ColdItemListing`: `test_names_each_item_by_line_and_text`, `test_a_title_cannot_carry_a_terminal_escape_or_a_bidi_override`, `test_cap_is_run_wide_across_files` |
| TRM24 | On the hook plane `sizescan` and `reviewscan` judge the whole staged copy of each file the commit touches, a deletion-only edit included, and leave an untouched file to CI | enforced (blocks, hook) | `test_sizescan.py`: `test_a_deletion_only_edit_is_judged_whole`, `test_false_block_an_unstaged_roadmap_does_not_block`; `test_reviewscan.py`: `test_a_deletion_only_edit_that_drops_the_review_line_is_judged` |
| TRM25 | `sizescan`: a bare run reports and exits 0, `--check` gates and only on cold content and archive integrity, never on length, and a scan that read nothing is exit 2 | enforced (blocks, CI test) | `test_sizescan.py` `ExitContract`: `test_default_exit_zero_even_with_cold_content`, `test_check_gates_on_cold_content`, `test_check_does_not_gate_a_long_all_open_roadmap`; `NoSizeCheck` pins that the length reference points are gone |
| TRM26 | `reviewscan` reads decision records dated 2026-07-21 or later; a frozen record is never flagged; the review line needs a non-empty value and a fenced one does not count; an explicitly named path is always scanned; a scan that matches no record says "not in scope" and counts the numbered records it did not read | enforced (blocks, hook + CI) | `test_reviewscan.py`: `ScopeTest`, `LineTest`, `NotInScopeTest`, `ExitCodeTest` |
| TRM27 | `reviewscan` reads roadmap sections never: a design entry there rests on convention alone, because a lint demanding a review line under every roadmap heading fires on prose (record 2026-07-18-0820) | directive-only | diff: a change to `reviewscan`'s scope list that adds `docs/roadmap/` or `docs/ROADMAP.md`. No test names the exclusion; the scope tests list what is in |
| TRM28 | `publishscan` judges the path and never the contents; its only hatch is a glob in `.publishscanignore` (no line marker, deliberately: a reason written inside a file that should not exist is never seen); a glob matches the full path, case-sensitively, from the root file only; every run prints the suppressed count, zero included; `--history` is opt-in and not in the registry; a shallow clone is exit 2 | enforced (blocks, hook + CI) | `test_publishscan.py`: `PatternTest`, `HatchAndModeTest.test_ignore_file_exempts_with_a_reason`, `RoundTwoCounselTest.test_pl2_zero_is_printed_and_a_plain_path_is_not_counted`, `test_pl7_an_ignore_glob_stays_case_sensitive`, `HistoryTest`. "Not in the registry" is the registry's argv and unpinned |
| TRM29 | `datescan`, `wrapscan`, `spellscan` and `sizescan` on the hook plane read each staged file whole from the index and keep only findings on added lines: an unstaged draft cannot block someone else's commit, and a staged defect fixed on disk after `git add` still blocks | enforced (blocks, hook) | `test_false_block_an_unstaged_draft_does_not_block` and `test_false_pass_a_staged_defect_fixed_on_disk_still_blocks` in each of `test_datescan.py`, `test_wrapscan.py`, `test_spellscan.py`; the `sizescan` twins `test_false_block_an_unstaged_roadmap_does_not_block` and `test_false_pass_a_staged_defect_fixed_on_disk_still_blocks` |
| TRM30 | A blockquoted line never blocks under `datescan`: each check runs on it, hits are listed and counted on a line printed every run, and none moves the exit code; the blocking set is pinned | enforced (blocks, CI test) | `test_datescan.py` `BlockingSetPinned`; `CodeAndQuoteExemptions.test_blockquote_exempt` |
| TRM31 | `archivecut` proves a cut before it writes (a multiset over every non-heading line, a byte rebuild, every re-pointed link mapping back) and moves the file whole where the proof fails; retiring the session log has no fallback and writes nothing unless the proof passes; `--plan` writes nothing | enforced (tool's own guard, blocks at the call) | `test_archivecut.py`: `test_plan_writes_nothing`, `test_cut_writes_items_readme_and_proves_from_disk`, `test_fallback_when_a_line_looks_like_the_cuts_link_line`, `test_fallback_when_a_reference_link_loses_its_definition`, `test_retires_index_and_archive_into_files_with_proof`, `test_verify_catches_a_changed_item` |
| TRM32 | `harvestscan` and `pointerscan` never block: a check whose similarity threshold cannot be grounded may not red a build (`harvestscan`); and `pointerscan`'s three detectors only warn | enforced (warns, hook + CI) | `test_harvestscan.py` `InvocationTest.test_it_never_fails_a_build`; `test_pointerscan.py` `InvocationTest.test_it_never_fails_a_build` |
| TRM33 | `pathscan` is warn-only in the registry through one visible `--warn` argument, because dropping it is the estate-wide flip to blocking and must never happen as a side effect; records are excluded by default and `--include-records` widens deliberately | enforced (CI test, blocks the run) | `test_floor.py` `PathscanPromotionTest.test_the_promotion_did_not_smuggle_in_the_blocking_flip`, `test_the_registry_reproduces_the_step_it_retired`; `test_pathscan.py`: `test_records_are_excluded_by_default_when_a_dir_expands`, `test_include_records_selects_them`, `test_a_closed_board_item_is_a_record` |
| TRM34 | `indexscan`'s allow marker lives in the index, exempts exactly one named entry and needs a reason; a marker that exempts nothing (the entry is listed, gone or outside every `match=`) is reported stale; a marker of any other scope exempts nothing; a malformed declaration, a `dir=` that escapes the root and a bad `before=` are exit 2 that `--warn` never downgrades | enforced (warns, hook + CI) | `test_indexscan.py`: `AllowMarker`, `DateRule.test_an_unknown_marker_kind_exempts_nothing`, `test_a_differently_cased_kind_is_unknown_too`, `test_the_scoped_marker_on_the_line_exempts_that_line_only` |
| TRM35 | `attribscan` reads additions only on both planes (records are append-only history, so an old `ruled` cannot be fixed), reads a whole-tree run as measurement that never blocks, passes and says so on a repo's first commit, and treats an unresolvable revision as a broken scan; its response hardens on `ATTRIBUTION_WARN_UNTIL` (2027-02-08), a constant no flag moves | enforced (warns until 2027-02-08, then blocks) | `test_attribscan.py`: `StagedPlaneTest.test_only_added_lines_are_read`, `AgainstPlaneTest.test_a_first_commit_passes_and_says_so`, `test_an_unresolvable_revision_is_a_broken_scan`, `TreePlaneTest.test_whole_tree_is_report_only_on_the_date`, `DateTest.test_the_date_is_read_strictly_before`. "No flag moves the date" is a property of the code and no test tries to move it |
| TRM36 | `namescan`, `quotescan` and `pdlistscan` harden on their own dated constants (`NAME_WARN_UNTIL` 2027-05-03, `QUOTE_WARN_UNTIL` 2027-05-31, `PERSONAL_DATA_WARN_UNTIL` 2027-03-08), each a constant no flag moves, and until then a finding reports and exits 0; a bare `--warn` never downgrades a broken scan | enforced (warns, then blocks on the date) | `test_namescan.py` `test_it_blocks_on_the_flip_date` and `test_it_does_not_block_the_day_before`; `test_quotescan.py` the same pair; `test_pdlistscan.py` `test_it_warns_before_the_date_and_blocks_from_it` and `DateAndSelftest.test_the_date_is_read_strictly_before`. The three dates in the README match the constants in the code (read at this commit) |
| TRM37 | `namescan` is in scope only for a repo that declares itself public; what counts as a private name is what `leakscan` counts, from its term sources, with no new list; a finding names the rule and a redacted excerpt, never the term; `--require-terms` with no list is exit 2; a marker in the message body exempts and a subject cannot exempt itself | enforced (warns until 2027-05-03, then blocks; msg plane) | `test_namescan.py`: `ScopeTest.test_a_repo_not_declared_public_is_out_of_scope`, `MessagePlaneTest.test_one_source_exactly`, `test_require_terms_with_no_list_is_broken`, `test_a_reasoned_marker_in_the_body_exempts`, `test_a_bare_marker_exempts_nothing`. "Never names the term" has no test by that name |
| TRM38 | `quotescan`'s authority surfaces (`AUTONOMY.md`, the floor region and every stamped floor copy in a `CLAUDE.md`, the `permissions` value of a `.claude/settings*.json`) are advisory on every plane and every date: they never block and the prompt date does not reach them; a repo with none of the files gets nothing | enforced (warns) | `test_quotescan.py` `AuthoritySurfaceTest`: `test_an_autonomy_edit_warns_and_never_blocks`, `test_the_permissions_key_is_a_surface_other_keys_are_not`, `test_a_stamped_copy_in_claude_md_is_a_surface`, `test_a_repo_with_none_of_the_surfaces_is_clean`. This is a guard slice 2 ranked first and graded absent (defect 5) |
| TRM39 | `pdlistscan` reports `no-list`, `unlisted-marker` and `unlisted-holder`; a private or undeclared repo is out of scope and says so; atelier's own `tools/` and `instruments/` are not read (their sources hold invented fixtures) and a child's are; an entry with no pinned string contributes none | enforced, partial (warns until 2027-03-08, then blocks) | `test_pdlistscan.py`: `ScopeTest`, `PublicRepoTest.test_a_marker_in_an_unnamed_place_is_a_finding`, `test_tools_are_exempt_only_with_the_mechanism_present`, `test_an_unpinned_entry_contributes_no_strings`. Partial: reads strings the list pinned and never whether an entry's reason is good (stated) |
| TRM40 | `leakscan --messages` is read-only: it exits 0 whatever it finds and 2 if the log cannot be read, a marker in a message exempts nothing, and authorship trailers are skipped; it is not on the commit-message plane | enforced (CI test, blocks the run) | `test_leakscan.py` `CommitMessages`. "Not on the commit-message plane" is the registry (`namescan` carries the message-plane read) |
| TRM41 | A Claude Code hook the tools ship never blocks a session from opening: `floorhook`, `prefixhook`, `idhook` and `stashscan --hook` always exit 0; a failure to answer prints `no result`, never "current"; a malformed payload is never an error | enforced, partial (CI test, blocks the run) | `test_floorhook.py` (`test_a_failed_fetch_is_no_result_with_pins_own_reason`, `test_a_hang_is_no_result_inside_the_time_limit`, `test_unparseable_output_is_no_result`), `test_prefixhook.py::test_bad_stdin_never_errors`, `test_idhook.py::test_bad_stdin_never_errors`, `test_stashscan.py::test_hook_survives_bad_stdin`. Whether a user wired them is outside the repo: the plugin wires none, by decision (*Doubts*) |
| TRM42 | `modelguard` denies an `Agent` call with no `model` and a Bash command that starts a `claude` session with no `--model`; it fails closed after a head it does not know, passes a lookup of the binary, and never blocks on a malformed payload; every bypass found joins its deny table | enforced, partial (harness hook, blocks at the call) | `test_modelguard.py`: `test_every_known_bypass_is_denied`, `test_a_lookup_of_the_binary_passes`, `test_malformed_payload_never_blocks`. Only where a user or repo wired it; it checks that a model is named, never which; a launch from inside a script is invisible (all stated) |
| TRM43 | `secretguard` denies a Bash stage that runs a printing verb on a path from config; the secret paths come from config and never from the script; a malformed payload or an unreadable config never blocks; `--try` and `--show` explain a verdict | enforced, partial (harness hook, blocks at the call) | `test_secretguard.py`: `test_original_cases`, `test_defaults_alone`, `test_defaults_off`, `test_malformed_payloads`, `test_repo_exemption`, `test_reveal_without_a_configured_flag_is_not_judged`. "A seatbelt against the reflex `cat`, not a wall" (stated): `python -c "print(open(...).read())"` passes |
| TRM44 | `deadhook` exits 1 while a floor hook sits in a hooks directory git has been pointed away from, and `--status` answers "are my commits being scanned?" from outside the hook; it is deliberately not a floor check (clone-local state a CI checkout never has) | enforced, partial (instrument, self-run) | `test_deadhook.py` (26 tests: `test_unset_hooks_path_with_no_hook_fails_from_both_trees`, `test_worktree_with_an_edited_hook_is_warned_not_failed`). Self-run: `/atelier:install-hook` runs `--status` as its proof (`CMD1`); nothing runs it when the hook has quietly gone |
| TRM45 | `treeline` names the root a check actually read, passed in and never derived from the cwd, never raises and never changes an exit; `ATELIER_NO_TREE_LINE=1` turns it off | enforced (CI test, blocks the run) | `test_treeline.py`: `test_cwd_does_not_move_the_answer`, `test_the_floor_line_changes_nothing_about_the_exit`, `test_the_switch_turns_it_off`. "Other scanners do not yet" print it (stated) |

### The shared modules' stated contracts

Rows `TRM46` to `TRM60`: `report.py`, `anchoredrx.py`, `filewalk.py`,
`estate.py`, `allowmarker.py`, the tests paragraph, `coldsweep.py`, `flipcheck.py`
and `stampscan.py`, in the README's order.

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| TRM46 | The exit-code contract is stated once: 0 nothing blocking (clean, advisory-only, or `--warn`), 1 blocking findings, 2 the scan itself is broken; `--warn` turns 1 into 0 and never touches 2; every difference between scanners is a parameter and none is a shared default | enforced (CI test, blocks the run) | `test_report.py` `TestExitContract`, `TestScannerLinePins` (what a scanner prints reaches every child's CI, so each converted scanner's lines are pinned as literals). The marker pair `exitcodes:begin` and `exitcodes:end` has no reader: nothing compares the quoted contract with `report.py` |
| TRM47 | A `--staged` guard reads the diff by its structure, not its look: a header is only what git writes between `diff --git` and the first `@@`, a hunk's counts say where its body ends, a diff that does not fit its counts is exit 2, each added line carries its real line number, and the diff command is pinned against user settings (`diff.suppressBlankEmpty`, `diff.interHunkContext`, `GIT_DIFF_OPTS`) | enforced (blocks, CI test) | `test_report.py` `ParseAddedLinesTest`, `TestGitPathReading`; the per-scanner `StagedPosedHeaderTest` and `StagedRealLineNumbers` classes. The stated unbounded residual (the staged plane holds the whole diff in memory) is named in `TRM11`'s class of gap |
| TRM48 | Each of nine scanners ends a finding with a namespaced ID `<scanner>:<kind>`, and the kind is exactly the scope that scanner's allow-marker accepts, so the ID copies into the narrowest marker | enforced, partial (CI test, blocks the run) | `test_report.py`: `TestFindingIdHelpers`, `TestFindingLinePins`, `TestFindingIdRoundTrip`. The round trip is pinned; "nine" and which nine are not |
| TRM49 | A regex that opens with a greedy character class must be linear in line length: `AnchoredRx` stands in for `leakscan`'s `email` and `secretscan`'s two URL rules, and a regex known to be quadratic is listed with its reason, the test failing when the entry has become linear | enforced (blocks, CI test) | `test_anchoredrx.py` `Equivalence`, `Linear`; `test_scanner_rules.py` `RuleTablesScaleLinearly`; `test_support_regex.py`. A new greedy-run rule added to a scanner is covered only if its rule table is one of those the test runs |
| TRM50 | Every rule's gate (its cheap necessary condition) is declared beside its regex, derived into one table the scan loop reads, and proven necessary against a corpus generated from the rule's own regex; the three rules the two scanners copy are pinned to each other | enforced (blocks, CI test) | `test_leakscan.py::GatesAreNecessary`, `test_secretscan.py::GatesAreNecessary`, `test_scanner_rules.py` `SharedRuleParity`, `test_support_regex.py` |
| TRM51 | The one file walk streams `git ls-files` inside a work tree and reads tracked files even under a skip name for the three boundary guards; no yielded path has a symlinked parent; every git call runs with `core.fsmonitor=false`; a fallback that hides a git failure says so on stderr | enforced (CI test, blocks the run) | `test_filewalk.py`: `TestTrackedUnderSkipNames`, `TestSymlinkedParent`, `TestTreeConfiguredCommands`, `TestFallbackVoice`, `TestShapeMatrix`. Stated gap: `linkscan`, `reviewscan` and `pointerscan` walk with their own code (GW7), so "guards stop reading ignored trees" is not yet true of them |
| TRM52 | A `../<sibling>` reference resolves to the same place from a linked worktree, the main checkout and a group folder, through `estate.py`'s one answer; `ATELIER_ESTATE_ROOT` or the git config names the folder, and a value that is not an absolute directory is reported and ignored | enforced (CI test, blocks the run) | `test_estate.py`: `test_worktree_and_main_name_the_same_checkout`, `test_the_git_config_carries_it_where_the_environment_does_not_reach`, `test_a_value_that_is_not_an_absolute_directory_warns_and_is_ignored`, `test_linkscan_gives_a_worktree_the_main_checkouts_verdict` |
| TRM53 | An allow marker needs a reason that starts with a letter, digit, underscore or opening quote; a scope with no reason exempts nothing, at once; a marker inside an inline code span is a mention in every scanner; a line carrying the marker word but no recognised allowance gets one stderr note per distinct head per run | enforced (blocks, hook + CI) | `test_allowmarker.py`: `TestMarkerGrammar`, `TestCodeSpans`, `TestUnparseableNote`, `TestScannerParametersPinned`. The malformed-scoped-marker grace is `GRD14` |
| TRM54 | An ignore file's globs match by `fnmatch` on the repo-relative path and not as gitignore: `*` crosses `/`, `**` means `*`, a leading `/` never matches, `!` negates nothing, and a glob that can never match exempts nothing silently | enforced, partial (CI test, blocks the run) | `test_allowmarker.py` `TestIgnoreFile`. A glob that never matches is silent by the README's own words: the divergence from gitignore is pinned and the dead glob is read by nothing |
| TRM55 | A glob's `review-by: YYYY-MM-DD` is read with the same grammar as the loader; a lapsed or unreadable date is reported and never dropped, the comparison is against the UTC date, and it changes no exit status and no floor or board verdict; twelve scanners read it | enforced (warns, hook + CI) | `test_allowmarker.py` `TestReviewBy`; `test_ignore_deferments.py` `Adopters`, `LeakscanBinaries`; `test_floor.py` `DefermentLineTest`. "Twelve" is the README's count of adopters and the test runs the same checks over eleven plus `wrapscan` |
| TRM56 | `allowmarker.py` stays loadable by file path without a `sys.modules` entry (no `dataclass`), because a child's own hook loads it that way | enforced (CI test, blocks the run) | `test_allowmarker.py` `TestLoadsByFilePath` |
| TRM57 | The tools run on Python 3.9 and later, and the tests need 3.11 or later | directive-only | diff: a 3.10-only construct (`match`, a parenthesised `with`) in a non-test `tools/*.py`. CI pins 3.12 only (`ci.yml`, `floor.yml`). Measured: `ast.parse(..., feature_version=(3, 9))` over every non-test `tools/*.py` raised 0 errors and all 21 registry `--selftest` runs pass under the system 3.9.6. A syntax tripwire reads syntax, not the standard library (a 3.10 call passes it) |
| TRM58 | `coldsweep` walks with `pathlib` and filters on path parts, so `./docs/sessions`, `docs/sessions/` and `docs//sessions` bar the same files and a sibling directory with the same prefix is not swept up; every run prints its exclusion set; `--commit` prints no message body past the subject and leaves out the board store unless a path names it; a broken sweep exits 2 | enforced (instrument's own guard, self-run) | `test_coldsweep.py` (both directions of the bar are pinned, per the README). Self-run: `REV9` and `REV10` already count that nothing makes a reviewer use it |
| TRM59 | `flipcheck` is report-only: every call is a bare `gh api` GET, a read it cannot make prints "not available" with the reason and never reads as set, and it exits 0 whatever it could not read | enforced (CI test, blocks the run) | `test_flipcheck.py`: `test_every_call_is_a_bare_get`, `test_the_one_gh_call_site_is_a_bare_api_get`, `test_an_unreadable_part_is_partial_never_set`, `test_a_field_absent_from_a_good_response_is_not_a_value` |
| TRM60 | `stampscan` recognises markers only outside fences and code spans; a stray marker, a malformed stamp and a `source=` that resolves outside `--root` are exit 2 that `--warn` never downgrades; `--require-stamps` and `--require-floor-stamp` fail closed (exit 2); a stamp of the safety floor is compared whatever markers it carries | enforced (blocks, CI test) | `test_stampscan.py` (125 tests: `test_unterminated_stamp_is_malformed`, `test_stray_end_is_malformed`, `test_traversal_source_is_a_config_error`, `test_floor_compressed_without_narrow_is_drift`, and the `--require-stamps` class around line 1106). Wired advisory in atelier's own `ci.yml` and not in the registry (stated), so the child side is `pins`' report (`TRM18`); nothing wired passes either `--require` switch |

## docs/PERSONAL-DATA.md — the closed list

`PDL1` to `PDL6`. The standard's own words on the list are folded (`RST23` to
`RST25`); these are what the list file adds.

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| PDL1 | This file is the only place atelier lists the personal data it holds; a session that finds personal data not on it has found a breach and does not document around it | enforced, partial (blocks, CI test + hook) | `tools/test_personal_data.py` `RegisterMatchesTreeTest.test_every_holder_of_a_listed_string_is_a_named_place` reads every tracked file for each pinned string; `leakscan` (hook) reads the shapes and the machine-local terms. Partial: a string the list never pinned is read by the shapes only, and PD4 (a given name) is pinned to nothing |
| PDL2 | The list is kept true by a test: a listed string standing in a file no entry names fails the suite, an entry naming a place where its string no longer stands fails it, and so does a personal-data allow-marker in a file no entry names; edit this file and the files together | enforced (blocks, CI test) | `test_personal_data.py`: `test_every_holder_of_a_listed_string_is_a_named_place`, `test_every_named_place_still_holds_the_string`, `test_named_places_exist`, `test_personal_data_markers_stand_only_in_named_places`, `test_personal_scopes_are_real_leakscan_rules`. **The first of these fails at this commit** (`PDL3`) |
| PDL3 | The record stores (session logs, review verdicts, board items, the roadmap indexes) are append-only history listed as stores: a new entry in one may repeat a listed string and may not add an unlisted one | enforced (blocks, CI test), and breached | `test_personal_data.py`. A new kind of record store, the census files under `docs/method/census/`, is named in no entry's *May stand in*: slice 7's file stands PD1's account name in a `gh api` command at its line 179, and at this commit `python3 -m unittest test_personal_data` fails (1 of 11) and `pdlistscan` reports 1 finding. The rule is enforced and it is being broken: nothing runs `unittest` before a commit, and CI's run is after the push (defect 6) |
| PDL4 | Each entry states why it is held, how it was granted and the narrowest set of files it may stand in; "his words" is a verbatim quotation of him and "his call" a decision a record keeps, never an agent's own choice | enforced, partial (blocks, CI test) | `test_personal_data.py` `test_every_entry_says_why_and_how_granted_and_where` reads that the three fields are present. Whether a quotation is verbatim, whether a "his call" record says what the entry says, and whether the place list is the narrowest are read by nothing |
| PDL5 | An entry pinned to no files is exactly the declared one (PD4, a given name that is an ordinary word); no other entry may be unpinned | enforced (blocks, CI test) | `test_personal_data.py` `test_unpinned_entries_are_exactly_the_declared_ones` |
| PDL6 | A session never adds an entry on its own judgement: it stops, asks the principal through the question device, and writes his answer here only when it is a grant | directive-only | diff: a new `## PDn` heading or a widened *May stand in* with no quotation or "his call" record beside it. `PDL4`'s test sees the field is present, not that he granted it. `attribscan` reads an attribution word in a commit's prose, which a new entry does not carry. This is `RST24` restated at the list's own home, which the file says in its first paragraphs |

## docs/roadmap/README.md — the board legend

`RMP1` to `RMP9`. The live file is the original its template copies; the rules
the template shares are folded.

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| RMP1 | The index shows what is owed and not what is done: a summary table of sections with open, claimed, `🎯` and `⏳` counts, then only unfinished items; a section with nothing owed keeps its table row marked `✅`; `🎯` and `⏳` are read off the state line and a glyph in a code span lifts nothing | enforced (blocks, hook + CI) | `board.py` generates the index and the `board` check compares it with the item files: `test_board.py` `Index.test_done_is_not_listed_and_never_renders_bracket_x`, `test_a_backticked_glyph_is_a_mention_not_a_flag`, `test_flags_lift_but_title_stays_clean`. Until 2026-12-04 the previous full form is also accepted with a warning (`FULL_FORM_ACCEPTED_UNTIL`) |
| RMP2 | The checkbox states are a work-owed tri-state and never a disposition: `[ ]` work owed, `[~]` claimed, `[x]` no more work owed; a fourth bracket is not a state | enforced (blocks, hook + CI) | `board.py`'s state-line grammar. Probed on a scratch board: an item opening `- [-]` is reported "no state line — an item file opens with its checkbox line" and the check fails. A side effect of the grammar, found by no test that names the case (as `DEC20`'s front matter is); `2026-11-09-board-states-design` (proposed) would add two brackets |
| RMP3 | `[x]` says its disposition in the item's own text, as a dated note, whether delivered, superseded or declined | directive-only | diff: a state line flipped to `[x]` with no dated note in the item. Nothing reads the item's body for a disposition |
| RMP4 | A `[~]` item is not started by another session; the claim is `(claimed <date>-<HHMM>, wt: <branch>)`, extended in place with a resume breadcrumb | directive-only | record: the claim is read by `cclive` and `ccopen` when run; `sweepscan` and the board read no claim. `CON` rows count the claim rule; the form is counted here only as the legend states it |
| RMP5 | `⏳` means one thing: a review queued whose pass has returned no verdict, and a pass running under a claim keeps it; the commit that lands a verdict takes the `⏳` off that state line, and the review queue is the count of `⏳` state lines and never of titles that say "queued" | enforced, partial (warns, hook + CI) | `pointerscan` `QueueStateTest`: `test_a_landed_pass_still_wearing_the_glyph_is_flagged`, `test_a_queued_review_without_the_glyph_is_flagged`, `test_a_claimed_pass_still_running_is_not_landed`, `test_a_verdict_link_alone_is_not_landing`. The count itself is generated by `board.py`. Warn-only (`CHK13`) |
| RMP6 | A pointer's delta list stays complete: a later commit that touches a queued delta's doctrine surfaces, even for hygiene, widens the pointer's list in the same commit (AW6, ruled 2026-07-23) | directive-only | diff: a commit changing a path named in a `⏳` item's pointer with no change to that item. A join of the commit's paths against every open pointer's paths; `pointerscan` reads the pointer's grammar and state and never its list |
| RMP7 | An inline claim (`wt: none`) closes in the commit that lands its work: a worktree merge forces a return to the item's file and an inline claim has no such step | directive-only | record: a `[~]` item with `wt: none` that outlives its landing commit. `cclive` lists a claim when run; the item in the cited case sat open for hours after `b89a306` shipped |
| RMP8 | State changes rebuild the index in the same commit, and the `board` check makes that mechanical | enforced (blocks, hook + CI) | `board` registry check (`CHK8`; `REC22` counts the rule, folded here for the legend's own sentence) |
| RMP9 | Sequencing rule from the 2026-07-10 review: mechanism before more content, because a repo that inherits docs without the propagation and review cadence has inherited the costume and not the doctrine | directive-only | invisible: a choice of what to build next leaves nothing in a diff. The census itself is the standing instance (`020/220` is this rule's own child) |

### The reviews README that is not there

The brief for this slice, and slice 6 and 7's *Remaining* lists, name atelier's
own reviews README as "the live original the templates copy". **There is none.**
`docs/reviews/` holds the review files and one `README.md` under `withdrawn/`,
and `git log` for the root path is empty: it was never added. The reviews README
exists only as the template, `docs/build/templates/docs/reviews/README.md`,
which slice 6 censused (`TPL10`). `reviewscan`'s tests treat a README there as
"not a brief" (`DeferralScopeTest.test_readme_and_deferred_siblings_are_not_briefs`),
which presumes one. The template's cross-reference (`CONTRIBUTING.md`, line 131)
points at it:
the link `docs/reviews/README.md` resolves only in a child. <!-- pathscan:allow: the absent file this names -->
No rule is counted for the absent file. Named as defect 7.

## Counts

Each rule counted once, under the state and place it first shows. Slice 8:

| Area | Rules | Enforced (partial) | blocks | warns | Directive-only | diff | record | invisible | Accepted |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| floor.py's contract | 13 | 12 (3) | 12 | 0 | 0 | 0 | 0 | 0 | 1 |
| registry checks | 21 | 21 (19) | 12 | 9 | 0 | 0 | 0 | 0 | 0 |
| tools/README.md | 60 | 57 (11) | 46 | 11 | 3 | 3 | 0 | 0 | 0 |
| PERSONAL-DATA.md | 6 | 5 (2) | 5 | 0 | 1 | 1 | 0 | 0 | 0 |
| roadmap/README.md | 9 | 4 (1) | 3 | 1 | 5 | 2 | 2 | 1 | 0 |
| Slice 8 | 109 | 99 (36) | 78 | 21 | 9 | 6 | 2 | 1 | 1 |
| Slice 7 | 116 | 45 (34) | 43 | 2 | 71 | 15 | 23 | 33 | 0 |
| Slice 6 | 68 | 25 (19) | 24 | 1 | 43 | 19 | 12 | 12 | 0 |
| Slice 5 | 73 | 19 (14) | 15 | 4 | 54 | 12 | 15 | 27 | 0 |
| Slice 4 | 106 | 5 (5) | 4 | 1 | 99 | 60 | 9 | 30 | 2 |
| Slice 3 | 94 | 9 (9) | 8 | 1 | 81 | 20 | 7 | 54 | 4 |
| Slice 2 | 129 | 27 (19) | 15 | 12 | 101 | 36 | 23 | 42 | 1 |
| Slice 1 | 158 | 19 (11) | 14 | 5 | 133 | 35 | 33 | 65 | 6 |
| Running total | 853 | 248 (147) | 201 | 47 | 591 | 203 | 124 | 264 | 14 |

Reading the table. The validators are the most-tested part of the repo, so
slice 8 has 99 of 109 rules (91%) with a check, against 39% for slice 7, and the
share is an artefact of what was asked: of the 94 rows from `floor.py`, the
registry and `tools/README.md`, the 90 enforced are a scanner's own suite pinning
what the scanner's README says it does. That is a lower bar than a doctrine rule
having a guard (method 4), and the totals below are given both ways. Only 36 of
the 99 are partial, because the README states a contract and a test pins it; the
partial ones are where the `why` or the README says more than the check reads
(`CHK9`, `CHK15`, `CHK7`) or a dated warning period is still running (`CHK16`,
`CHK17`, `TRM18`, `TRM35`, `TRM36`). The two files that carry doctrine and not
mechanism, the closed list and the board legend, grade like earlier slices: of
`PERSONAL-DATA.md`'s 6 rules, 5 are read by `test_personal_data.py` and one of
those is being broken; of `roadmap/README.md`'s 9, 4 are read and 5 are not, and
the five are the legend's judgement calls (a disposition note, a complete delta
list, an inline claim's close, the sequencing rule).

On slice 8's own sums: running total over eight slices is 853 rules, one counted
twice (EVIDENCE section 17 as `EVI24` and `CON21`), so 852 distinct. State
changes recorded since earlier slices are not applied to the totals (*Doubts*).

## Top five guard candidates

Directive-only or unpinned, breach visible in the diff, ranked by what a first
run on the live tree would find. Slice 8's directive-only rules are few (9), so
the list is led by what the registry contract tests do not yet pin:

1. **A registry-wide contract test, in the shape `FLR12` already has.** For each
   of the 21 `SCANNERS`: a memory-bound class exists (`TRM11`: 6 scanners have
   none and a seventh has a time bound only), and `--selftest` prints the form
   the README states (`TRM1`: 9 of 21 print another form, and the quiet test
   names 7). It reads the registry and the suite, so a new entry cannot arrive
   without the companions the older ones have. First run: 15 findings (6 and 9),
   all genuine. Same shape as slice 4's `PRI12` (a `--json` test over the
   registry) and slice 6's installer-tool-set test; one file could hold all
   three.
2. **`test_personal_data` at the hook plane.** `PDL2` is pinned by a 0.5-second
   test that CI runs after the push; at this commit it fails on one file, the
   file slice 7 committed, because `pdlistscan` (hook, warn until 2027-03-08)
   warned and the commit went through. Running that test when a commit touches a
   tracked file that stands a listed string, or giving atelier alone the blocking
   form of `pdlistscan`, would have refused the commit that broke it. First run:
   1 finding (and it is the live one).
3. **The dated constants the floor cannot see.** Seven scanners and tools carry a
   date after which a response hardens (`ATTRIBUTION_WARN_UNTIL`,
   `NAME_WARN_UNTIL`, `QUOTE_WARN_UNTIL`, `PERSONAL_DATA_WARN_UNTIL`,
   `COPY_BLOCKS_FROM`, `MALFORMED_GRACE_UNTIL`, `FULL_FORM_ACCEPTED_UNTIL`); the
   README's dates match the code on all seven at this commit. A test that every
   module-level `*_UNTIL` or `*_FROM` constant in `tools/` is named in the
   floor's state column, or carried by the registry entry, closes defect 1 and
   keeps the README honest. First run: 2 findings (`attribscan`, `pdlistscan`
   render as enforced while unable to block).
4. **The Python 3.9 floor, as syntax.** `TRM57`: the tools claim 3.9 and CI runs
   3.12 only. `ast.parse(..., feature_version=(3, 9))` over every non-test
   `tools/*.py`: 0 errors; all 21 registry selftests and `floor.py --list` pass
   under the system 3.9.6. It lands clean, reads syntax and not the standard
   library (a call added in 3.10 passes it), and costs one CI step. The hooks run
   under that interpreter, so a breach is a blocked commit on every machine.
5. **A dated disposition on a closed board item (`RMP3`).** A state line flipped
   to `[x]` with no dated note. Measured: 342 closed item files outside the
   archive, 0 with no ISO date anywhere in the file; the weak proxy lands clean
   and a stricter read (a date on or under the state line) was not tried. The
   cheap form is a tripwire on the flip itself in the commit that makes it.

Next after these, each measured:

- Scope `docs/method/census/` (and the other new record kinds) into the closed
  list's places or out of the string search, which is a ruling for the principal
  (`PDL6`): today the file kind is named nowhere and the first one that mentions
  the account name reds the suite.
- A README heading must use the registry's state vocabulary: `harvestscan`,
  `pointerscan` and `pathscan` are headed "advisory only", which in the floor's
  three states means a child's declared softening (defect 8). 3 headings.
- `tools/README.md` states `licenscan` is for the pre-publish scrub and not the
  hook; the registry says the opposite for a repo that declares a licence
  (`TRM14`). One sentence either way.

**Not diff-visible.** `TRM41`, `TRM42` and `TRM43`: the session hooks, `modelguard`
and `secretguard` bind only where a user or a repo has wired them, and the plugin
wires none by decision. Whether a given machine has them is a read of that
machine's settings, which no commit carries.

## Doctrine defects found, not fixed here

Each is owed its own board item where it has none; none is changed by this file.
Not in this file's gift: the census item is not edited, and the principal alone
grants a closed-list place.

1. **The floor's "enforced" mark is not a claim a dated warning period can
   break, and two checks break it.** The docstring says the green tick means "a
   gate that held" and derives the state from the registry argv. `attribscan`
   (warns until 2027-02-08) and `pdlistscan` (warns until 2027-03-08) render
   `enforced` on the hook plane although a finding cannot block them. The
   in-scanner date is invisible to `Scanner.warns_only`. `namescan` and
   `quotescan` render warn-only on CI by the registry's `--warn` and are silent
   about their own hardening dates. `FLR5`, `CHK16`, `CHK17`.
2. **`datescan`'s registry `why` overstates the check.** "Never a drifting
   'today'" is not what it reads: a bare "today" with no date beside it passes by
   design and a test pins the pass; the declaration's purpose gap names the dated
   maintenance edit and omits this one. `CHK9`.
3. **The README states the `--selftest` verdict as one form and 9 of 21 print
   another.** All 21 print one line, so the property the test cares about holds,
   but the sentence "a passing run prints `selftest OK — <scanner>`" does not,
   and the quiet test names 7 registry scanners of the 21. `TRM1`.
4. **`licenscan`: the README and the registry give opposite wiring advice.** The
   README says to run it at the pre-publish scrub and CI's release job and not the
   per-commit hook; the registry runs it on both planes whenever a repo declares
   a licence, which atelier's `.atelier-floor.json` does. `TRM14`.
5. **Slice 2's `AUT14` row, and `115/110`'s headline, are stale.** Both say a
   change to the agent's own grant is read by nothing. `quotescan`'s authority
   surfaces (`AUTONOMY.md`, the floor region and its stamps, the `permissions`
   value) landed on 2026-11-17 (commit `b462fd7d`), advisory and never blocking.
   `AUT14` is now enforced, partial (warns); `AUT15` is partly read (a grant
   edited in `AUTONOMY.md`). Re-grade noted, not applied. `TRM38`.
6. **`test_personal_data` fails on `main`'s own tree, and the list has no home
   for the census.** `PDL3`: slice 7's file stands PD1's account name at its
   line 179, inside a command the file quotes, in a directory no entry's *May
   stand in* names. Remedies, both the principal's to choose: the cheap one is to
   rewrite that command in the file without the name (the list says "remove the
   data"); the durable one is a ruling on whether a census file is a record store
   and may repeat a listed string. Until then each commit that reaches CI reds
   the unittest step.
7. **The reviews README that three records name does not exist in atelier.** See
   *The reviews README that is not there*. Slices 6 and 7 inherited the premise from
   the board item's wording. If the template is the only copy, the brief's, the
   scanner's and the template's references are right only inside a child.
8. **Two words for the same state.** The floor's vocabulary reserves *advisory*
   for a child's declared softening and calls the parent's own report-only wiring
   *warn-only*. `tools/README.md` heads `harvestscan`, `pointerscan` and
   `pathscan` "(advisory only)" and `indexscan`, `sweepscan` "(warn-only)". A
   reader of the README cannot tell which kind of 🟡 they will see. `FLR5`.
9. **`instruments/README.md` contradicts itself about `ccarchive`'s schedule**
   (found while sizing the file, which is not censused). Its install section says
   `ccarchive --install-schedule` sets up a daily calendar schedule; its
   *Run by hand* bullet says it installs none and "refuses the old
   `--install-schedule` family of flags by name". The code accepts the flags and
   `ccarchive.test.js` is titled "the old removal refusal is gone". The second
   statement is the stale one.

Checked and found sound: all seven date constants in code match the README;
`floor.py --selftest`, every registry `--selftest`, and `ast.parse` at 3.9 pass;
the registry's softenable set matches the docstring and the contributing
template (`FLR6`); `floor.py --declarations` is read-only by test (`FLR12`); the
fourth-bracket rule holds by the board grammar (`RMP2`).

## Doubts and unverified points

- **The registry rows are graded on a lower bar than the doctrine rows.** A check
  whose own suite pins its behaviour is *enforced* here; the doctrine rules ask
  whether a guard exists at all. Counted without the 21 `CHK` rows: 832 rules,
  227 enforced (27.3%). Without the 94 rows that come from the validators
  (`FLR`, `CHK`, `TRM`): 759 doctrine rules, 158 enforced (20.8%). Slices 1 to 7
  alone: 744 rules, 149 enforced (20.0%). All three are fair; the first is what
  the table adds.
- **The grain of `tools/README.md` is a judgement.** The `sizescan` section
  alone states about sixty behaviours and became five rows. A finer count would
  raise the total by perhaps a third, and the enforced share with it, since
  the suites are fine-grained.
- **No scanner's own module docstring was read, bar `floor.py`'s.** The README
  says each docstring is canonical for its scanner's mechanism (`board`) or its
  manual (`signscan`, `signfleet`, `floorfleet`). The README was read for the
  contract; the seven dates and the 21 `why` strings were checked against the
  code; nothing else was diffed against a docstring. A drift between a README
  statement and its docstring is invisible here.
- **Not every cited suite was run for this slice.** The whole `tools/` suite was
  (`unittest discover -s tools`, 17 minutes): 3,441 tests, one failure, which is
  `test_personal_data`'s `test_every_holder_of_a_listed_string_is_a_named_place`
  and is `PDL3`. The node suites and the `instruments/` Python suites were not
  run. Each cited test name was checked to exist by script, and the dozen checks
  that carry a claim were run by hand. This file passed the same test.
- **`TRM5` and `TRM9` credit tests by class and name, not by body.** Where the
  README says a test pins a condition ("each condition pinned by a test"), the
  class names agree and the bodies were not read.
- **`PDL3` is a finding about the tree at one commit.** If `main` has moved and
  the file was rewritten, it is closed there. The worktree's own `pdlistscan`
  and unittest runs are what is cited.
- **A hook-wired `floorhook`, `prefixhook`, `idhook` and `stashscan` were graded
  on their tests only** (`TRM41`); that any user has them on is a fact about a
  machine.
- **State changes since earlier slices are still not applied.** `AUT14` and part
  of `AUT15` (defect 5), `AUT17` (slice 5), `PRI8` (slice 4's `browser-fetch`
  correction), and the commits since slices 1 to 3 were censused (16 commits
  touched slice 1 to 3 files by slice 5's count, more since).

## Remaining, outside this slice

- **`instruments/README.md` (804 lines) and `instruments/man/ccfleet.1` (1,418
  lines)**, with `ccfleet --doc`. Named in slice 7's *Remaining* and in this
  slice's scope. Neither has rows. Read enough of the README to find defect 9 and
  to see its shape: each instrument's section is a behaviour spec of the kind
  `tools/README.md` has, pinned by `instruments/*.test.js` and `test_ccfleet.py`
  (88 tests); the fixed launch contract in `ccfleet.1`'s *What every launch does*
  is the part most worth a row set. They are a fresh slice (9), not a fold.
- **The `*.design.md` notes** (`ccclose`, `ccopen`, `cclive`, `ccrepo`,
  `ccarchive.encryption`, `cctranscript.search`, `datescan.off-rules`,
  `leakscan.off-rules`), which slice 7 listed with the validators. Design
  records, read by none of the eight slices.
- **Each scanner's module docstring** and the three docstring-only manuals
  (`signscan`, `signfleet`, `floorfleet`).
- **The generated `docs/ROADMAP.md` index's standing rules**, which are
  `RMP1`'s generator and carry no prose of their own.
- Everything outside `docs/`, `tools/`, `skills/`, `commands/`, `.claude-plugin/`
  and the root files: `instruments/browser-fetch/README.md`, `.github/workflows`
  as doctrine (read by slice 6's candidate, not graded), `allowed_signers`'
  content.

## Census-wide summary

### Totals across the eight slices

| Slice | Subject | Rules | Enforced (partial) | Directive-only | Accepted |
| --- | --- | --- | --- | --- | --- |
| 1 | RECORD, REVIEW, CONCURRENCY | 158 | 19 (11) | 133 | 6 |
| 2 | APEX, AUTONOMY, GUARDS, PROPAGATION | 129 | 27 (19) | 101 | 1 |
| 3 | EVIDENCE, ECONOMICS, COMMUNICATION, DATA-PROTECTION | 94 | 9 (9) | 81 | 4 |
| 4 | ACCESS to PRINCIPLES (six files) | 106 | 5 (5) | 99 | 2 |
| 5 | REACH to session-open | 73 | 19 (14) | 54 | 0 |
| 6 | `docs/build/`, root files | 68 | 25 (19) | 43 | 0 |
| 7 | decisions, skills, commands, plugin | 116 | 45 (34) | 71 | 0 |
| 8 | validators, closed list, board legend | 109 | 99 (36) | 9 | 1 |
| **All** | | **853** (852 distinct) | **248** (147) | **591** | **14** |

**29.1% of the 853 rules have a mechanical check; 59% of those are partial.**
Read as the table above says to: 20.0% of the first 744 (slices 1 to 7); 20.8% of
the 759 rules that are doctrine and not a validator describing itself; 27.3%
without the 21 registry rows. By plane, of the 248 enforced: 201 block (hook,
CI, a test, a tool's own refusal or a host setting) and 47 warn. Of the 591
directive-only: 203 (34%) have a breach visible in the commit's own diff, 124
show only by joining records, and 264 (45%) leave nothing in the tree.

The enforced share by slice runs from 5% (slice 4, conventions and principles:
prose standards with no scanner at the grain) to 91% (slice 8, the validators
describing themselves). The slices that govern *agent behaviour* (1 to 3) sit at
10% to 21%, and the slice that governs *structure* (6) at 37%.

### Where a guard would pay most

The directive-only rules whose breach shows in the diff are 203, and they gather
in four clusters. Each is one shape a commit-plane check could read, and each
cluster's evidence is already collected in the slice named.

1. **Append-only records and their shape (slices 1, 7, 8).** A change to an
   accepted decision record above its last addendum (`REC19`); the status
   vocabulary (`DEC3`: two `proposed` records fire a check on its first run); a
   record file's name shape (`REC7`, `CON23`); an `at HEAD` claim (`DEC1`); a
   review file with no provenance (`REV19`); a bulk deletion outside the roadmap
   (`REC24`, `REV36`); a `[x]` with no dated disposition (`RMP3`); a closed-list
   entry with no grant (`PDL6`). The checks are file-shape and diff-shape and read
   no judgement. The cheapest cluster to build and the one every slice touches.
2. **Authority, grants and allowances (slices 2, 3, 8).** The agent widening its
   own authority (`AUT14`, now advisory through `quotescan`); a grant recorded
   without his words (`AUT15`); a guard or a check's response lowered outside the
   declared lane (`GRD2`, `GRD19`); an over-wide allowance, a new glob, `disabled`
   entry or unscoped marker (`GRD13`); a decision recorded with no mark
   (`COM19`, `COM20`); a new closed-list entry (`PDL6`). The evidence reader
   already exists in `quotescan` and `attribscan` (form of a quotation, never
   whose); extending a form check to each of these surfaces is the shared work.
3. **Landing companions (slices 1, 2, 7, 8).** A commit that changes a governed
   surface carries its companion line: the review pointer (`REV15`), the
   `CHANGELOG` line (`PRO1`: 17 of the last 40 plugin-surface commits had none),
   the review line against the review that exists (slice 7: three of eight
   records read "queued" beside a finished pass), the pointer's delta list
   (`RMP6`). All are "a diff touching path X must also touch path Y or carry a
   reasoned marker", the shape `blockscan` already is for one pair.
4. **Workflow and registry hygiene (slices 3, 4, 6, 8).** No scanner reads
   `.github/workflows` or the templates: a path filter on the floor workflow
   (`ECO15`), a self-hosted runner (`ECO17`), a dearer runner (`ECO13`), actions
   not SHA-pinned and workflows with no `permissions:` (`TPL7`, `TPL8`: 2 of 5
   workflow files declare none), a timer with no stated need (`PRI16`); and, on
   the registry side, a test over the 21 entries (slice 8's candidate 1, slice 4's
   `PRI12`, slice 6's installer-tool-set test). One reader over `.github/` and
   one test over `floor.SCANNERS` would carry most of the cluster.

### What the census did not do

- **Slices 1 to 3 have not been re-swept.** They were run on 2026-11-16; sixteen
  or more commits have touched their files since, and doctrine moved. Every
  slice's counts are a count at a time and stay as that slice found them.
- **Re-grades noted in later slices were not applied to the totals:** `AUT14` and
  half of `AUT15` (defect 5), `AUT17` (slice 5), `PRI8` (slice 4), and slice 7's
  `DEC` status-vocabulary reading. If all were applied the enforced count rises
  by two or three and no other number moves materially.
- **It is a count of rules, not of risk.** A rule's weight (a burned secret, a
  leaked name, a colon in a heading) is not in the count, so 29% enforced does not
  say 29% of the risk is guarded. The guard candidates are ranked by what a first
  run would find and by what a breach costs, not by the share.
- **Grain varies by slice.** Slice 4 counted prose sentences; slice 7 counted
  skill constraints and not steps; slice 8 counted README contracts and not
  sentences. Shares across slices are not strictly comparable and the 91% of
  slice 8 above all is not a finding about the validators' quality.
- **"Enforced" is graded by reading a test's name and, where a claim looked wide,
  the code.** It does not say the check has no false negative. Each partial names
  the gap the document or the registry states; the gaps that nobody has stated are
  by definition not in the census.
- **The 264 invisible rules were not examined for a before-plane guard**, bar the
  notes slices 5 and 7 made. That is `115/100`'s work, and the census is its
  input (the rules a harness hook could read at the call).
- **No guard was built, tested for false positives against a live tree, or priced
  beyond the first-run counts above.** `020/240` takes the five lists and the four
  clusters from here.
- **Instruments and the ccfleet reference were not censused** (*Remaining*);
  defect 9 was found by sizing the README, not by reading it through.

The census as the board item asked for it, all doctrine on `REVIEW.md` rule 3's
function-not-file-type definition, is complete except for the instruments'
reference pages; a ninth slice for them, and a re-sweep of slices 1 to 3, are the
whole of what is left.

