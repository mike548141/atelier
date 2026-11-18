# 2026-11-18 · 0740 UTC — One command prefix and one home: assessed, nothing moved

**Session:** `84b7932e`, Claude Opus 5.5, principal-opened in the primary checkout. No
review-tier model was used and no review was run or briefed.

## What was done

- The principal asked for every slash command under one `/atelier` prefix and every
  collaboration tool homed in atelier, then narrowed it the same session: put it on the board
  and assess the size; and scan the other repos for anything better homed here. His words are
  in [`docs/roadmap/450-…/README.md`](../roadmap/450-one-home-and-one-command-prefix-mike-commissioned/README.md).
- Inventory: user-level skills, hooks, status line, MCP servers, the `cc*` links, and every
  repo's tracked tool directories. Findings and a sized table are on the board as `450/010`.
  Headline: the plugin's own commands already carry `/atelier:`; two user-level ones do not,
  and both hold private estate content, so the route is the `210/440` switch to the general
  skills with a private config, not a move into this public repo.
- Nothing was moved or rewired: the principal's condition is to be told before each move.

## Left owed

`450/010`, with its decisions listed for whoever picks it up.

## Continued: the principal's answers, and the build (to about 1030 UTC)

- 💬 His answers to the four asks, verbatim: colon form *"that is fine"*; switch the two estate
  commands now *"yes"*; the homing rows *"I will accept your recommendation on these"*;
  review-tier time *"during the drain as usual, a lower priority for these vs other work"*. Then,
  through the device, after a gap analysis found drain-tool faults that lose paid review work:
  switch the drain *"After its review (Recommended)"*, and that one review *"Normal priority
  (Recommended)"*.
- **Built and landed** (all on `main`): `71117e6b` menu, status line, prefix hook and the
  `MECHANISMS.md` rule; `17f158d2` `d9d1589e` `a025636e` ccfleet's generic gaps and both skills;
  `262658e0` `pins.py --floor`; `cdfadc75` secretguard and deadhook; `ef4972e6` stashscan and
  treeline; `1eb42f54` three ccfleet faults from the first real run. Workers built rows 6–10 and
  the gap fixes in their own worktrees; this session landed each.
- ⚠️ **A landing slip, fixed:** one rebase's conflict resolver failed its own assertion, but the
  landing commands were chained with `;`, so the markers reached `main`; `603378f4` removed them
  minutes later. Its message names the bad commit as "3c8a", which is wrong: it was `ef4972e6`.
- **Machine wiring (user-level, outside the repo):** the model hook now runs
  `tools/modelguard.py`; `ccstatusline` is the status line; `prefixhook` and `stashscan` run at
  session open; the bare `/atelier` skill is linked by the installer; a dead July
  `.git/hooks/pre-commit` in this checkout was moved aside (backup in the scratchpad).
  secretguard is built but not wired: the principal's call.
- **Estate root:** a headless session there switched the sweep (private config, rulings file,
  one real run `DONE`, old link removed) and prepared the drain side without switching it.
- **Child follow-ups** (each child's own session or the next sweep): the service-estate child
  moves its secret paths into secretguard's user-level config and drops its own hook, then
  replaces its dead-hook check with `deadhook.py --status`; the app child drops its stash check
  (wire `stashscan.py --hook`) and switches its tree line to `treeline.line(ROOT)` (rename its
  off-switch to `ATELIER_NO_TREE_LINE`); the two children with floor verifiers run
  `pins.py --floor --child .` instead; the estate root retires its model-hook copy.
- A hand edit to `docs/method/session-open/session-open-prompt.md` sat uncommitted in the
  primary checkout, in the principal's own voice; it was not made by this session and was left
  untouched.

## Left owed

`450/010` rows 2, 11, 12 and the child follow-ups; cold passes `160/1450` (normal),
`160/1610` and `160/1620` (low); secretguard's wiring, the principal's call.
