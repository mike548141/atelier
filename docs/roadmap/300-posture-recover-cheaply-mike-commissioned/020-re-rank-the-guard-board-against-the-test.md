- [x] 🚩 **Re-rank the open guard work against the fourth requirement — and
      expect some of it to fail** `[L][docs]` — blocked on `010` landing the
      test. Mike ruled 2026-08-17 that the posture *becomes* the test guard work
      has to pass, having been told to expect exactly this.
      **Why it is its own item and wants a FRESH session.** The open board
      carries guard, policy and review work at roughly three-quarters of its
      volume. Applying a new test to that is a wide-blast-radius pass over
      landed decisions, and it is precisely the shape two sessions in a child
      repo have now declined at the tail of a long run rather than do badly —
      which is `ECONOMICS.md` working, not a lack of takers. Do not pick this up
      as the tail of another sitting.
      **What the pass produces**, so it is not an invitation to re-litigate
      everything: for each open guard item, which of the two the guard does
      (makes failure cheap · forbids the act), stated once; the items where the
      answer is *forbids, and nothing makes the failure cheaper* flagged for
      Mike rather than closed; and no landed guard removed by this pass. A test
      arriving after the work is a reason to **declare**, never a licence to
      revert on the author's own judgement.
      ⚖️ **The honest tension to carry into it.** `PRINCIPLES.md`'s Gate sizing
      test already says an over-restrictive guard trains the operator to loosen
      it. The floor is mostly prevention and blocks commits. Some of it will
      fail the new test on its face, and *that failing is the finding* — not a
      defect to be argued away, and not a mandate to unwire a working gate.

      ---

      📋 **RESULT — the pass, run 2026-10-05 at `97c7ace` (wt:
      atelier-qr-300-020).** Nothing was removed, unwired or changed. No other
      item file and no doctrine was edited. Each row states the declaration
      once, read from what the guard or item actually does.

      **Counts.** 100 guards and guard items assessed: the 20 landed guards
      (the 15 floor-registry checks plus atelier's own CI-only and fail-closed
      checks) and 80 open board items that propose, build or change a guard.
      - Landed, 20: **7 make the failure cheap** · **11 forbid the act, with a
        recovery behind it** · **2 forbid only, flagged**.
      - Open, 80: **8 make the failure cheap** · **10 forbid, with a recovery**
        · **5 forbid only, flagged** · **36 undecided** (the item has not yet
        chosen block or warn, so the declaration is owed at design) · **21
        inherit** an existing guard's declaration (the change is speed,
        coverage, wording or plumbing, not what refuses).
      - **7 flagged in all** — listed in plain language at the end.
      - **Not assessed: 115 open items**, screened out by their titles and
        sections without being read in full: the 52 review-queue entries
        (`160`), 12 instrument features (`210`), this section's own 3, and 48
        doctrine, channel and open-question items. A later pass could confirm
        none of them hides a guard.

      **How it was read.** The landed guards were read from `tools/floor.py`'s
      registry, `floor.py --list`, the hook (`tools/pre-commit.sample`) and
      `.github/workflows/ci.yml`. The 136 candidate open items were each read in
      full by four read-only classifier passes. Every flagged row and every row
      changed from a classifier's call was then re-read by this session. Two
      calls were changed. `260/040` was re-classed from forbids-only to
      *inherits publishscan*, because the flag belongs to the landed guard.
      `020/120` was re-classed from undecided to *forbids, with a recovery*, to
      match `170/010`, which describes the same signscan flip with its
      recovery.

      **Three findings that sit across the rows.**
      1. **Only the hook forbids anything.** CI runs after the push. On a public
         repo the push *is* publication, so on CI every check is detection after
         the fact, however it is labelled. The hook also prints a
         `--no-verify` emergency bypass. For the two flagged landed guards, the
         whole of the prevention is therefore one local hook that can be
         skipped.
      2. **Three blocking checks describe themselves as advisory.** The
         docstrings of `datescan`, `wrapscan` and `spellscan`, and `datescan`'s
         `tools/README.md` heading, say "advisory only" or "never gates".
         The registry wires all three blocking on hook and CI, and
         `floor.py --list` prints them `enforced`. The declarations below follow
         the registry, which `floor.py` names as the authority. The drift is a
         finding for the board, and this pass does not file it.
      3. **Gate sizing, noted and not flagged.** `linkscan`, `sizescan`,
         `datescan`, `wrapscan` and `spellscan` block failures whose fix is
         already one edit. They pass the new test, honestly declared. But §10's
         *prefer cheap failure where the recovery is buildable* is where they
         would be questioned, and `010/130` (a routine claim failing
         `wrapscan`) is a live case of a block making someone reluctant to act.
         `conflictscan` and `board` are different: they cost almost no
         legitimate freedom, because no legitimate act is blocked or the fix is
         free at the moment it fires.

      **Landed guards (floor registry first, then atelier-only).**

      | Guard | Declares | Why, from what it does | Flag |
      |---|---|---|---|
      | secretscan | forbids · recovery: rotate the credential | Blocks any high-confidence credential shape. A leaked rotatable credential is made harmless by rotating it. Unrotatable ones are the gap (`070/010`). | |
      | leakscan | forbids only | Blocks personal or estate data. It has no advisory form by ruling, and publication cannot be taken back. CI runs structural-only, so full cover is the hook alone. | 🚩 |
      | conflictscan | forbids · recovery: fix-forward commit | A committed conflict marker is never right, so the block costs no legitimate freedom. | |
      | linkscan | forbids · recovery: fix the link | Blocks the whole tree on a broken internal link. The repair is one edit. | |
      | reviewscan | forbids · recovery: add the line, or re-run the pass | Blocks a decision record with no review judgement, and a brief carrying deferred material. A contaminated pass can be re-run. | |
      | publishscan | forbids only | Blocks tracking files whose presence helps an attacker. Its own docstring says it "cannot unpublish". Rotation undoes only some of the shapes it catches. | 🚩 |
      | sizescan | forbids · recovery: move cold content to the cold store | Blocks cold content on the hot path. The move is lossless. It has an advisory form. | |
      | board | forbids · recovery: `board.py rebuild` | Blocks a stale index. The fix is one command at the moment it fires. | |
      | datescan | forbids · recovery: rewrite the date | Blocks relative-time words in records. The commit timestamp still anchors them. It has an advisory form. | |
      | wrapscan | forbids · recovery: rewrap | Blocks over-long doctrine lines. The failure is cosmetic. | |
      | spellscan | forbids · recovery: respell | Blocks non-NZ spelling on the doctrine surface. | |
      | licenscan | forbids · recovery: correct the licence | Opt-in, and it blocks licence contradictions. Rights already granted to copies cannot be withdrawn. Every other failure fixes forward. | |
      | harvestscan | cheap failure | Warn-only. A dropped roadmap item stays in git history, and the warning arrives while restoring it is free. | |
      | pointerscan | cheap failure | Warn-only, at the commit that writes the pointer. | |
      | pathscan | cheap failure | Warn-only on every plane. Flipping it to blocking is `320/310`. | |
      | stampscan (CI, atelier only) | cheap failure | Runs with `--warn` and never refuses. | |
      | blockscan (CI, atelier only) | cheap failure | Runs with `--warn`, and the map and the co-change run both stay advisory. | |
      | signscan (CI) | cheap failure | Warns first. An unsigned commit is seen after the push and can be reverted. | |
      | floor runner, fail-closed | forbids · recovery: the remedy it prints | A missing `floor.py`, `python3` or scanner, or an unusable `.atelier-floor.json`, blocks every commit. The fix is a one-line install or config edit. | |
      | CI build checks (selftests, test suites, man lint) | cheap failure | They red a run after the push and refuse nothing. The fix goes forward in the next commit. | |

      The floor already holds one cheap-failure choice by design. A passed
      advisory `review-by` date blocks nothing, "because a commit failing on a
      date set months earlier is how a forcing function becomes a --no-verify
      habit" (`floor.py`).

      **Open board items that propose, build or change a guard.**

      | Item | Guard | Declares | Why | Flag |
      |---|---|---|---|---|
      | `010/130` | wrapscan on claim lines | inherits wrapscan | Scope or exemption only. | |
      | `010/160` | CF3 dirty-sibling stop | undecided | One reading makes the harm cheap through the rebuild flag. The other keeps the stop. | |
      | `020/020` | harvestscan (B4) | cheap failure | Warn-only. The item text predates its registry wiring. | |
      | `020/030` | leakscan composed terms (C5) | undecided | Three options block, and one drops the term to write-time discipline. | |
      | `020/040` | leakscan third verdict state | inherits leakscan | "Exit codes do not move". | |
      | `020/050` | leakscan term for the join | undecided | Rewrite, accept the records, or a scanner term. Not chosen. | |
      | `020/070` | legacy advisory spelling (C1b) | inherits floor advisory model | Removes a transition spelling only. | |
      | `020/090` | sanctioned adoption path (C3) | undecided | An advisory-first adopt mode would be cheap. A bootstrap bypass would not. | |
      | `020/100` | make the local bypass visible (C4) | cheap failure | CI flags a hook-bypassed commit, so it is "visible rather than impossible". | |
      | `020/110` | stampscan to the children | cheap failure | Stays advisory through a soak period. Any later flip is a separate ruling. | |
      | `020/120` | signscan flip to blocking | forbids · recovery: revert and re-sign | Matches `170/010`. The flip is Mike's. | |
      | `020/140` | secretscan impact axis (E6d) | forbids · recovery: rotate | Escalation only, grounded on "rotation presupposes detection". | |
      | `020/150` | leakscan binary media (G3, held PR) | forbids only | No advisory or dated form. Published image metadata cannot be withdrawn. | 🚩 |
      | `020/180` | session close-out checker | undecided | Refuse or report is not stated. | |
      | `020/300` | the unwired reply gate | undecided | Redesign or destroy, after a design review. | |
      | `020/350` | bidi and zero-width characters at the board parse seam | undecided | Strip, escape, or accept. None of the three blocks. | |
      | `020/410` | adoption for a guard with no advisory form | undecided | The leakscan adoption-deferment ruling is owed. | |
      | `030/050` | leakscan scoping in the children | inherits leakscan | Per-repo scope or allow decisions only. | |
      | `030/070` | private-repo-name × posture check | undecided | Block or warn is not chosen. A review comes first. | |
      | `030/090` | adoption chicken-and-egg | undecided | Same choice as `020/090`. | |
      | `030/100` | `--no-verify` made visible | cheap failure | Visible, not impossible. | |
      | `030/130` | record-store deletion confirm | forbids · recovery: restore from history | Show first, then act. The bytes are recoverable. | |
      | `030/140` | CF3 on a monolithic board | undecided | Patch the rule, or split the board. | |
      | `050/010` | trust-failure skill | undecided | Gate, or a checklist and record only. | |
      | `070/010` | history rewrite after an unrotatable exposure | undecided | When a rewrite beats accept-and-disclose, and who authorises it. | |
      | `090/010` | refuse green on a cancelled run | forbids · recovery: re-run on your own commit | Not built. A watch item. | |
      | `110/010` | an allow-marker that parses as nothing | cheap failure | A note beside the finding. | |
      | `110/060` | expiry at every deferment level | forbids · recovery: re-date or fix | Goes red when lapsed. | |
      | `110/100` | exception register | undecided | Block or report on a non-conforming entry is not stated. | |
      | `110/130` | leakscan and secretscan speed | inherits both | Output must stay byte-identical. | |
      | `115/050` | real credential in an exempt fixture | undecided | Canary, prompt, or accept the gap. | |
      | `115/070` | §9 structured-data check | undecided | Blocked on `115/020`. | |
      | `115/080` | single-sourced scanner harness | inherits every scanner | Proved byte-identical part by part. | |
      | `115/090` | a second dial on every guard | cheap failure | Warn at the free-fix moment instead of narrowing detection. | |
      | `115/100` | before-plane | forbids only | Not designed. Flagged on its stated shape: "makes the wrong thing impossible". | 🚩 |
      | `115/110` | authority-widening and visibility checks | undecided | Block or flag is not stated. Both acts are irreversible. | |
      | `115/120` | the declaration slot and its check | undecided | Missing declaration: fail or report. | |
      | `115/130` | report whether the rule fired | cheap failure | Prints coverage and refuses nothing. | |
      | `115/150` | a stale pin may fail something | undecided | A doctrine question for Mike. | |
      | `115/160` | leakscan ignore file outranks no-advisory | undecided | Honour the claim in the loader, or strike it. | |
      | `115/210` | interpreter for the guard suite | inherits the suite | Legibility only. | |
      | `115/220` | shared line readers | inherits each scanner | Refactor. Intents are never merged. | |
      | `115/230` | allow-marker grammar divergences | inherits the line scanners | Tightens exemptions. Refusals are unchanged. | |
      | `130/020` | board and pointerscan pointer states | undecided | "Enforce", with pointerscan's warn-only status not settled. | |
      | `170/010` | signscan flip, fleet signing | forbids · recovery: revert and re-sign | Recovery measures already landed (signfleet, boundaries). | |
      | `200/010` | generic index-drift mechanism | undecided | Design not started. A generated index would make failure cheap. | |
      | `220/060` | ask-channel detector | undecided | Unprobed. It would detect after the fact. | |
      | `230/010` | child pickup of `floor.yml` | inherits the floor gates | Rollout only. | |
      | `230/020` | roadmap-item deletion check | undecided | Build, advisory, or decline. | |
      | `260/040` | publishscan round 2 | inherits publishscan | See the flagged landed guard. | |
      | `260/050` | floor knows public vs private | undecided | Tightens public repos, and a mismatch is "a live breach". | |
      | `260/060` | leakscan terms on CI | undecided | Carry the terms, or re-word the output. | |
      | `260/070` | platform-settings gate | undecided | Gates settings before a repo flips public. Block or report is not chosen. | |
      | `320/010` | pathscan false-positive shapes | cheap failure | Warn-only. | |
      | `320/040` | hook resolves scanners from a working tree | inherits the hook | Which code runs, not what refuses. | |
      | `320/060` | path-scoped commit where siblings exist | forbids · recovery: soft reset, or fix forward | Mike called it forbids-the-act. A sweep loses nothing and misattributes. | |
      | `320/080` | quotescan | forbids only | Self-declared: "There is no cheap recovery". | 🚩 |
      | `320/100` | unquoted attribution flag | undecided | Block or warn is not stated. | |
      | `320/120` | CF3 stop with no exit | undecided | Keep the stop, or sanction claim-after-the-fact. | |
      | `320/130` | stampscan cover switch | inherits stampscan | Landed. The open shapes are about legibility. | |
      | `320/140` | secretscan unit for generated JSON | inherits secretscan | "It forbids nothing; it vouches." | |
      | `320/160` | stampscan across a repo boundary | inherits stampscan | Removes false reds. | |
      | `320/170` | pathscan false-positive classes | inherits pathscan | Noise removal. | |
      | `320/180` | sibling paths in a worktree | inherits pathscan | Resolution fix. | |
      | `320/270` | datescan frame (UTC) check | undecided | Block or warn on clock skew is not stated. | |
      | `320/310` | pathscan block instead of warn | undecided | Measure the residue first. The ruling is Mike's. | |
      | `320/340` | blockscan subsections | inherits blockscan | Advisory, unchanged. | |
      | `320/350` | multi-commit work takes a worktree | forbids · recovery: soft reset, or revert | A stop rule. A sweep is recoverable. | |
      | `320/390` | no check in the same command as its act | forbids only | A proposed rule with no mechanism. The harm it was filed from has no undo. | 🚩 |
      | `320/400` | old-figure survivor grep | undecided | Block or warn is not stated. | |
      | `320/420` | pointerscan moving bound | inherits pointerscan | One more warn class. | |
      | `320/430` | orphaned session-detail file | undecided | "whether it enforces or warns, is atelier's call". | |
      | `320/440` | review file needs a board back-pointer | forbids · recovery: add one line | Through reviewscan, with a boundary date for old files. | |
      | `320/450` | wrapped claim projection | inherits the board check | Changes what the index shows. | |
      | `320/470` | leakscan nz-phone in digests | inherits leakscan | Narrows a false positive. | |
      | `320/480` | cited hash resolves on the branch | undecided | Block or flag is not stated. | |
      | `320/490` | tool-call markup in files | forbids · recovery: delete the lines | Through conflictscan, with an allow-marker for deliberate quotes. | |
      | `370/010` | irreversible act needs artefact evidence | forbids only | A working rule. It applies only where the act is irreversible. | 🚩 |
      | `390/020` | visibility and sharing control | undecided | Forbid by pre-share check or org policy, or detect by audit. | |
      | `430/010` | review never thinned for budget | undecided | reviewscan candidates, none chosen. | |

      🔭 **Watch: undecided items likely to land as forbids-only.** Four
      undecided items guard acts that the record already calls irreversible:
      `390/020` (a private repo made public or shared), `115/110` (an agent
      widening its own authority, and visibility drift), `260/050` (the floor
      learning public vs private) and `260/070` (platform settings before a
      flip). When each is designed, the cheap-failure question should be asked
      before the block is chosen, not after.

      **🚩 The flagged list, in plain language.** Each of these stops something
      outright, and today nothing makes it cheap if that thing happens anyway.
      Flagged for Mike. None is closed, changed or unwired.

      1. **leakscan, the personal-data check (live on every commit).**
         *What it stops:* a commit that would put personal or private-estate
         details (names, addresses, phone numbers, private terms) into a repo
         that is or could become public. *Why there is no cheap way back:* once
         pushed to a public repo the detail is published. Forks, clones and
         caches keep it, and rewriting history does not reach them. It has no
         warn-only mode, by ruling, and in CI it runs without its private term
         list, so the full check is the local hook alone. *A cheaper-failure
         alternative, if wanted:* put a gap between commit and publication.
         Work would land on a private branch or remote first and be promoted to
         the public one only after a full scan, so a miss is caught while it can
         still be withdrawn. Holding less personal data in repos at all shrinks
         what could leak. The same absence of a soft mode is why new rules for
         this check have no lawful adoption period (`020/410`).
      2. **publishscan, the "don't track this file" check (live on every
         commit).** *What it stops:* tracking files whose presence alone helps
         an attacker. Examples are the list of commands an AI session runs
         without asking, environment and credential config files, logs, and
         local databases. *Why there is no cheap way back:* its own
         description says it "cannot unpublish". A published credential file
         can be rotated, and a published command list can be changed so the
         public copy is stale. A published log, database or dump has no such
         undo. *A cheaper-failure alternative:* the same publication gap as
         above, plus making the command-list change routine, so a leaked copy
         describes a configuration that no longer exists.
      3. **The binary-media rule for leakscan (built, held unmerged for
         Mike).** *What it stops:* every tracked image or binary file, until it
         has a reasoned entry tied to its exact bytes. It also blocks hidden
         image metadata such as location or device details. *Why there is no
         cheap way back:* published image metadata cannot be withdrawn, and by
         ruling the check has no warn-only or dated-deferral form. Merging it
         would turn seven repos' CI red at once. *A cheaper-failure
         alternative:* strip image metadata automatically before commit, which
         makes the bad event harmless rather than forbidden. Or allow a dated
         adoption period, which is the ruling `020/410` asks for.
      4. **The before-plane, a class of guard that acts before an agent acts
         (not designed yet).** *What it stops:* an agent action at the moment
         of decision, before the tool call happens. Flagged on its stated aim,
         "makes the wrong thing impossible rather than reportable". *Why there
         is no cheap way back:* the acts it targets, such as an agent widening
         its own authority or quietly settling a dilemma, leave little to undo
         afterwards. The one past attempt showed that a hook firing after the
         output cannot un-send it. *A cheaper-failure alternative:* a
         before-act step that announces or asks instead of denying. The agent
         stays free to act, and the act becomes visible at the one moment when
         stopping is free.
      5. **quotescan, checking quotes attributed to Mike (proposed).** *What
         it stops:* a quotation credited to Mike that cannot be matched to his
         own words in the session transcripts. *Why there is no cheap way
         back:* the proposal itself says so. Once a false quote is in the
         record, later sessions build on it. Built on the wrong transcript set,
         it would also block his real instructions as fabrications.
         *A cheaper-failure alternative:* label instead of block. Every
         attributed quote would carry a visible mark at write time — verified,
         paraphrase, or unverified — so a later reader sees its standing and a
         bad quote costs a correction rather than a rewrite of history.
      6. **"Never run a check in the same command as the act it guards"
         (proposed working rule, no mechanism).** *What it stops:* chaining a
         safety check and the act it protects into one command, where the
         act runs before anyone reads the check. *Why there is no cheap way
         back:* the incident it came from destroyed another session's unsaved
         file, and another was recovered only by luck. *A cheaper-failure
         alternative already exists:* the child that filed it reports that
         separate worktrees per session and naming paths on every commit made
         the whole class disappear. Those remove the collision rather than
         forbidding the habit, so this rule may not be needed once they are
         house practice.
      7. **"For an irreversible act, don't trust a tool's own success report"
         (proposed working rule).** *What it stops:* an irreversible action,
         such as a very large deletion, taken on the strength of a tool saying
         ✅ alone. *Why there is no cheap way back:* the rule only applies
         where the act cannot be undone. *A cheaper-failure alternative:* make
         the act undoable first. Move to a holding area or snapshot, and delete
         later, so a wrong report costs a restore rather than the data. That is
         §10's move exactly.

      ✅ **Closed 2026-10-05 — the pass is delivered** (queue run, Opus 5.5
      orchestrating, an Opus 5.5 worker; merge `27586aa`). The result block
      above declares 100 guards and guard items, 20 landed and 80 open, and
      flags seven where the honest answer is *forbids the act, and nothing
      makes the failure cheaper*. Two of those are landed guards (`leakscan`,
      `publishscan`), and they go to Mike in plain language at the run's
      close. Nothing was removed or unwired, as the item required. The 115
      items screened out by title are named in the block, so a later pass can
      confirm none of them hides a guard. One finding from the pass is filed
      as `115/240`: three enforced scanners still describe themselves as
      advisory.
