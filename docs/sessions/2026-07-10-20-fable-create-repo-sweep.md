# 2026-07-10 · the create-repo delivery-mechanism sweep: PASS-WITH-FINDINGS, gate cleared (Fable)

The brief run cold (`docs/reviews/2026-07-10-create-repo-rewire.md`, range
`f72031c..92c0112` + the machine-local skill read in full), deep not fast, and
**driven, not read**: floor re-run (142 tests, 3 selftests, leakscan/licenscan
clean), all 18 templates re-read fresh, and the mechanism exercised end-to-end
twice — once as written, once after the fixes. Ten findings C1–C10, **all
[fixed] and each fix re-driven same session**; verdict below the brief's
divider.

## The two that were proven live before fixing

- **C1 — protection evaporates on machine two.** Cloned the throwaway scaffold:
  no hook, no `hooks.atelierTools` (git transports neither), and a planted
  `AKIA…` key committed with a green exit. The only mention of hooks in the
  whole scaffolded repo sat inside an HTML comment the template says to delete
  — the fail-open class one hop later, exactly as the brief bet. Fixed at the
  three places a new clone looks: a "Hooks don't travel" bullet in the template
  CLAUDE.md, once-per-clone install lines in CONTRIBUTING (the skill fills
  their `<atelier-path>`), and the hook header. Honest residual stated: docs
  instruct, only CI can enforce on machine N — the deferred
  scanner-distribution item.
- **C2 — the stamped drift check broke run-verbatim.** The block stamped the
  atelier path unquoted; the house path contains spaces
  (`Mobile Documents`, `Pet Projects`), so `git -C` fatals. ros/faves survive
  only because they were hand-stamped `../atelier`; the skill said
  `$PP/atelier`, whose two literal readings *both* break — and session 18's
  "drift-check ran verbatim, read current" wasn't reproducible as instructed
  (the range's own B1 class, recurring). Fixed: canonical block + template
  quote the path; the skill stamps sibling-relative `../atelier` and step 5
  ends in a mechanical prove-the-stamp (grep unfilled placeholders; run the
  block's own drift command verbatim, expect empty).

## The rest, compressed

C3 template-block ≡ canonical now pinned mechanically (`tools/test_templates.py`,
suite 142→145 — the header's "a pin bump reviews this wording" was a hope, and
the test drew blood in its own build). C4 PROPAGATION prose said "three
placeholders", its own block carries four. C5 the prose stamp core was the
rewire's target defect alive inside its fix — now instrument-checked;
`tools/scaffold.py` is [backlog] only if a stamp defect recurs. C6 step 7's
`gh repo create` re-anchored to Mike's ask (not "push is recoverable"). C7 the
"pair with CI" lines implied a wiring children can't have — both artifacts now
state the gap. C8 `templates/LICENSE` added (was copied from faves — second
source, no target line for "set the holder"). C9 `ATELIER_TOOLS` trust surface
stated. C10 the precondition now checks templates are *readable* (iCloud
eviction leaves a present path).

Assumptions that **held**: fail-closed friction (loud, one-command repair,
printed `--no-verify` is honest not theatre), env-wins precedence, template
boundary-cleanliness (leakscan + fresh-eyes read), the contract tests (test 1
*is* the permanent known-bad pin), the stop-and-say-so precondition wording.

## Close

Verdict + dispositions in the review file; ROADMAP gate ticked **cleared —
keeper repos may be scaffolded**. Still owed beyond this review: the single
outward `gh repo create --push` live proof (first keeper run), CI scanner
distribution (existing deferred item), and ros/faves pin bumps to carry the
reworded block down (both are now behind atelier HEAD by design — the pin
mechanism doing its job). ros pin unchanged this session.
