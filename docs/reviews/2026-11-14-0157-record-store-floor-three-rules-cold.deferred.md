# Held back — the floor's record-store carve-out and three doctrine additions

Opened only once the reviewer's own findings are durably written (`REVIEW.md` rule 1). A floor,
never a fence. Written by the brief-writer (`cclive` lists it as session `b059d250`), which did not
author the delta. Nothing here is a finding: these are questions, and facts read off the machine.

## The pointer's own questions

1. Does the carve-out leave a recoverable-but-bulk record deletion on the wrong side of the floor's
   own closing sentence ("Everything else recoverable … just proceed")?
2. Is a one-case rule stated as more than one case? `SECRETS.md` says so in its own paragraph;
   `PRINCIPLES.md` §5 says so in a parenthesis; the checklist line "Used only rarely? Ask whether it
   need exist between uses at all" carries no marker. Does a reader of the checklist alone meet a
   settled rung?

## The brief-writer's questions

3. The floor bullet still ends "because what the floor guards cannot be taken back", and the new
   entry is on the list precisely because its bytes can be taken back. Does the bullet now
   contradict one of its own entries (V5), and does a child reading only the region learn why the
   entry is there?
4. "whoever wrote it": what is "it"? The store, the block, the record? `RECORD.md` says "regardless
   of who created the mess". Does the clause parse as the ruling means?
5. `RECORD.md` and `AUTONOMY.md` make a record-store bulk deletion show-first: "diff it and show the
   principal what goes, or ask". The floor's heading is "Always stop and confirm". Is showing then
   proceeding still allowed, or has the floor made the rule stricter than the ruling it carries,
   without saying so?
6. "meaning the roadmap, session logs, ADRs or reviews" reads as a closed list. `RECORD.md`'s same
   four look illustrative. Does the floor now exclude other one-file record stores a child keeps
   (a changelog, a decisions log, a ledger), and should "meaning" be "such as"?
7. "Bulk" is undefined in both texts. The grounding case was a 185-line removal in which one
   section was a genuine loss. Does deleting one item, or one section, escape the floor?
8. `tools/blockscan_map.json` maps the floor bullet's sources to one `00-APEX.md` heading only
   (fact 4). The new clause summarises `RECORD.md`'s record-store rule. Was a second source owed,
   so a later change to that rule is caught as moving the floor?
9. Lens 4 states as fact that `/security-review` "reads the session's pending diff, not a path it
   is aimed at". The evidence is three reviewers in one batch, one shape, one day. Is that the
   mechanism established, or the mechanism inferred from one shape (V1)? Was it re-driven at
   landing?
10. "verifiably clean at the moment of aiming": how does a reviewer verify it, and does the clean
    state survive a concurrent session writing between the check and the scan? Is the rule
    followable as written, or is option (a) of the intent record (the orchestrator commits before
    every spawn and writes nothing while reviewers run) the only way to meet it?
11. `skills/review-brief/SKILL.md`'s lens-4 compression carries the markdown exclusion and the
    deferred-material caution, and not the shared-worktree shape (fact 8). The skill says it may
    compress, never contradict. Was it a mirror site this delta owed (V3), and does
    `CONCURRENCY.md` need the same line?
12. "In Mike's words, captured 2026-08-03", then a quote. The record that queued it says "Captured
    from Mike", and its session-log line says a sibling session's ADR argued the idea and he routed
    the doctrine half to atelier (fact 5). Are the quoted words his, verbatim, or the ADR's
    phrasing as relayed? If the latter, is the attribution an overclaim?
13. "a deleted one has no exposure window left to bound": a credential minted for the run exists
    during the run. Is the exposure window zero, or one run long, and does the run-time window need
    stating? The intent record left open whether the rotation duty lapses or transfers; the
    doctrine settles it: the duty moves to the minting credential. Is that settled on reasoning
    alone, and is it labelled as reasoned?
14. "The rung sits below the triad": the triad is least-privilege, just-in-time, short-lived, and
    least privilege still applies to a credential minted per run. Is "below the triad" coherent,
    or is the rung below the last two only?
15. Solve once: the bullet says "Mike's principle (2026-07-25, captured in paraphrase)". Is a
    paraphrase attributed to him consistent with the house's verbatim-capture practice
    (`RECORD.md`, `COMMUNICATION.md`)? Does the bullet restate §2 DRY and `EVIDENCE.md` §9 while
    claiming to point at them (V4)? "the lateral route is the youngest, written 2026-11-09": the
    same day as this delta (fact 6). Is "practised" for up and down, and only "written" for
    lateral, the honest split, and does the bullet lean on the lateral route anyway? Privacy: do "a
    network tool handles its wire protocol in one module" and "One child repo's backup tool, on a
    platform whose delegation grant is standing-only" let a reader with the public estate in view
    name the child or the platform?

## Facts read off the machine (2026-11-14 UTC, from the worktree root)

1. Re-run lines: `git merge-base --is-ancestor 920d63f3 HEAD` exit 0; `coldsweep --selftest` exit
   0; `coldsweep --commit 920d63f3` exit 0, 206 lines; `python3 -m unittest test_templates` from
   `tools/`, 48 tests OK; `python3 -m unittest test_blockscan` from `tools/`, 58 tests OK in 46.7 s;
   `blockscan.py --root . .` exit 0; `floor.py --plane ci --root .` exit 0, 49 s wall clock under
   `nice -n 10`, Python 3.14.6, load average 9 to 13 on 12 cores. The *Deferred reading* sweep
   command ran exit 0, 86 hits over 679 files; its only hits on barred paths were board titles in
   `docs/ROADMAP.md`.
2. `920d63f3`'s stat: `CHANGELOG.md`, `docs/ROADMAP.md`, `docs/build/templates/CLAUDE.md`,
   `docs/method/PRINCIPLES.md`, `docs/method/PROPAGATION.md`, `docs/method/REVIEW.md`,
   `docs/method/SECRETS.md` and four board item files; 124 insertions, 19 deletions. Markdown only.
3. Later commits on the delta's files: `2a6d7a41` (`PROPAGATION.md` and the template, hunks at the
   *Asking* bullet, lines 63 and 161 before it), `55c7d409` and `dd3d60d4` (`REVIEW.md`, other
   sections). None touches the four regions under review.
4. `tools/blockscan_map.json`, entry `stop-and-confirm`: anchor "**Always stop and confirm (the
   floor):**"; one source, `docs/method/00-APEX.md` § *The principal's authority is absolute; his
   rulings are conditioned on being informed*.
5. `git log -S "delete the credential entirely"`: first `b3101c3b`, 2026-08-03, "roadmap: queue a
   fourth rung for the credential ladder — no credential at rest". Its item heading reads "(Mike,
   2026-08-03)"; its body says "an alternative in Mike's words: … Captured from Mike; not yet
   designed or decided". The same commit's `docs/SESSIONS.md` index line says a sibling session's
   ADR argued the idea and Mike routed the doctrine half to atelier.
6. `### The same route between any two repos` (`PROPAGATION.md` line 814 at 2026-11-14) first
   appears in `3f3cf5be`, 2026-11-09, "method: one route carries an idea between any two repos
   (310/120, 310/140)". Its authoring session was not checked.
7. The closing clause's words appear only at `PROPAGATION.md` line 145, the template line 47 and
   `CHANGELOG.md`. The show-first rule is at `RECORD.md` line 418 (listing "ROADMAP, SESSIONS, ADRs,
   reviews"; the principal's ruling, 2026-08-04) and `AUTONOMY.md` line 242.
8. `skills/review-brief/SKILL.md`, lens 4 (lines 89 to 96 at 2026-11-14), names `/security-review`,
   the markdown exclusion and the deferred-material caution; it carries no shared-worktree line.
   "solve once" first enters `docs/ROADMAP.md` in `58776c4a`, 2026-07-25.
