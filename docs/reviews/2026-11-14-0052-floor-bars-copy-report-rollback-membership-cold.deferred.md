# Held back — the board-check bar, the rule-copy report, the rollback check, membership, the transcript review

Opened only once the reviewer's own findings are durably written (`REVIEW.md` rule 1). A floor,
never a fence. Written by the brief-writer, session `a2c067e3`, which did not author the delta.

## The pointer's own questions

1. Can the rollback record be silently reset?
2. Does comparing a child to its own pin hide real drift?
3. What goes red on 2026-12-09?

## The brief-writer's questions

4. **The rollback record.** "A machine with no record … simply starts one", and "a volume ahead of
   the record … is adopted". Deleting or losing the 0600 record beside the key resets the check
   with no message. A second machine sharing the same synced archive has no record of the first's
   saves. Is the stated adversary (a writer to the volume, not the machine) the right boundary, and
   does any surface tell the user a record was started rather than continued?
5. `--rekey --accept-unverified` "is the deliberate clear" for `rolled-back`. After it, what does
   the record hold: the rolled-back save number or a new one? Is the clear itself recorded anywhere
   that a later `--audit` can see, or does the archive then read as sound with no trace?
6. "A number that does not check is never believed": drive a save number edited in place, a
   signature file with the number stripped (does it read as a pre-check archive and start a
   record?), and a number far ahead of the record (adopted, then every honest save is "behind").
7. **Comparing to the child's own pin.** A child that never bumps its pin compares clean against
   the text it copied, however far the floor has moved since. Is that drift hidden, or reported by
   the pin-staleness lane? Is the copy check then a test of the copy's fidelity only, and does the
   doctrine say so plainly? The four placeholders are "put back" before comparing: can a child
   carry text in a placeholder slot that changes a rule's meaning?
8. **Who runs the blocking gate.** `pins --check` is the "fleet check" that fails from 2026-12-09.
   Which CI job, hook or session start runs it? If nothing does, the "blocking" date blocks no
   commit and no merge; say what actually happens on the day.
9. `pins --check` already exits 1 for a stale pin. During a pin-bump sweep, does the copy gate add a
   failure a child can fix on its own, as the doctrine says ("each has a fix the child can make"),
   or one that only a parent-side change can clear (a pin to a commit with no floor text)?
10. **The archive exemption.** `gh repo view` runs from the date, for a child that would fail. In a
    run with no `gh` auth or no network the child "is not exempt": fail-closed, as wanted? Is the
    owner/name parsed from the child's remote, and can a crafted remote URL make it query a
    different repo, or pass an argument to `gh`?
11. **What goes red on 2026-12-09, by count.** Patch the dates (`floor._today`, `pins._utc_today`)
    in a scratch copy and run the floor over each child read-only, and `pins` over the fleet. How
    many children red, on which check, and does each red line say what to do? The `CHANGELOG.md`
    says two children declare `advisory.sizescan` and none lists `disabled`; re-count.
12. **The bar's grounds.** The principal clarified that *"Never allow it"* was about a single-file
    board (detail in child files, synopsis in the main board). `sizescan`'s cold-content gate
    flags completed `[x]` items on a hot-path roadmap. Are those the same property? Could a
    single-file board pass `sizescan` clean, or a multi-file board fail it? If they differ, the bar
    removes a lowering from a check that does not enforce what he said.
13. "A specific 'never' beats the general 'declared and expiring'" is new precedence doctrine. Is it
    grounded beyond this one case, and does it now bind every future "never" by default?
14. `06248fba` (after this delta) gave `disabled` an end date across the floor. Does that general
    rule and `DISABLED_BARRED_FROM` agree on a `disabled.sizescan` entry with an end date after
    2026-12-09? Which message wins?
15. **stampscan's floor identity.** Resolution by file: case-folding "where the filesystem agrees"
    differs between a case-insensitive laptop and Linux CI. Does a case-variant `source=` pass on
    one and red on the other? A symlink to the floor file? A `source=` that resolves outside the
    root? And the ignored allow-marker: is `.stampscanignore` (a whole-file skip, still open) the
    same bypass one level up?
16. `report.safe_text` covers one listing; "the other scanners that echo tracked text still do not
    use it". Which ones echo tracked text into a terminal or CI log, and is that an accepted
    residual anyone ruled on, or a known injection path left open?
17. **Membership.** "Owns or controls": is "control" defined anywhere? A client's repo "worked under
    the client's rules" is said to be outside, yet the principal may administer it. Exclusions live
    in "the estate root's private records": can a child, a reviewer or a tool check an exclusion
    exists, or is "decidable" true only for whoever can read the private record?
18. **The mining pass.** It reads every transcript and files board items. Into which repo's board?
    If any land in a public repo, what stops transcript content (private context, other repos'
    names, secrets pasted into sessions) from crossing over? Is "about monthly, on his word" a
    cadence anything tracks, or a statement no check can see kept?
19. **The floor copy and its sources.** `2dd4aafd` changed the floor region and the template stamp
    together. Run `stampscan` on the template; confirm byte-identity at HEAD, after the later
    commits. The onramp skill is now a pointer to `AUTONOMY.md`: is `AUTONOMY.md` bundled where the
    plugin installs, so the pointer resolves for an adopter with no atelier checkout?
20. The `.sizescanignore` comment now says the real protection against a sibling's nested worktree
    is `.gitignore` plus the walk's prune of directories carrying a `.git` file. Re-drive both with
    a nested worktree in a scratch clone.

## Facts held back

- **Re-run lines, 2026-11-14 UTC, machine load about 6 at the start, run from the worktree root
  (the `cd tools` line from `tools/`).** `python3` was 3.14.6. Every `--selftest` exit 0; the seven
  test modules, 835 tests in about 352 s, OK, exit 0; `ccarchive.test.js` 233 tests, 233 pass,
  exit 0; `mandoc -T lint -W style` exit 0; `floor.py --plane ci --root .` exit 0, `sizescan`
  enforced and clean, with `pathscan` warn-only findings.
- **`pins --head`:** exit 1 (stale pins, the pre-existing lane, while a pin-bump sweep was running
  in other sessions). Its floor-copy section: 0 of 22 copies differ; 1 more cannot be compared (a
  pin with no floor region) and "would fail from 2026-12-09 unless archived".
- **Who runs it:** a grep of `.github/workflows/` and `docs/build/templates/workflows/` found no
  `pins --check`; `tools/README.md` describes it as "(CI/hooks)". The brief-writer did not search
  child repos or hooks outside this tree.
- **Dates:** `floor.ADVISORY_BARRED_FROM` and `floor.DISABLED_BARRED_FROM` key `sizescan` to a date;
  `pins.COPY_BLOCKS_FROM = 2026-12-09`. Tests patch `pins._utc_today`; `floor` has `_today()` and a
  `today` parameter on `advisory_barred`.
- **Later commits:** twenty-one commits after `d1189996` touch the brief's path list (to
  `2a6d7a41`), among them `06248fba` (`floor disabled takes an end date`).
- **Not re-run by the brief-writer:** the `CHANGELOG.md` census claims (two children declaring
  `advisory.sizescan`; none listing `disabled`), and the full `unittest discover -s tools` suite.
