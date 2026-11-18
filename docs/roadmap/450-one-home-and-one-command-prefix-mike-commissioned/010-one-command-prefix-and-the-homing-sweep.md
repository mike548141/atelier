- [ ] 🎯 **Every slash command under `/atelier:`, and every
      collaboration tool homed in atelier** `[L][instruments][skills]`.
      Mike commissioned this, 2026-11-18 (his words in this section's
      README). Assessed 2026-11-18 by session 84b7932e (Opus 5.5,
      principal-opened); nothing moved yet. **Tell Mike before each move
      into atelier**: his condition, verbatim, *"tell me before you make
      changes like pulling a tool from another repo into atelier"*.

      **What the assessment found.**
      - The prefix is mostly there already. Every skill and command the
        atelier plugin ships is `/atelier:<name>` (six skills, four
        commands). Only two of Mike's commands sit outside it, both
        user-level skills: `/estate-health` and `/fable-drain`. The
        claude.ai-synced skills are Anthropic's, not his, and stay out.
      - **The catch is visibility.** `/atelier:` comes from this plugin,
        and this repo is public. Both stragglers quote the principal's
        rulings and name every estate repo, which is why they were kept
        out on 2026-11-13 (`210/440`: the general parts here, the estate
        parts in a private config). So the route is not to move them in:
        it is to switch the estate onto the general skills that already
        exist here (`/atelier:fleet-sweep`, `/atelier:review-drain`,
        `instruments/ccfleet`) with the private config held privately,
        then retire the two old commands. `210/440` already names that
        switch as the principal's to choose.
      - **Colon, not space.** The plugin system namespaces a plugin's
        skills `/<plugin>:<skill>`, and typing `/atelier` lists them all
        together, which is the grouping asked for. A single `/atelier`
        router taking a word (`/atelier estate-health`) would hide each
        command's description from the picker. Recommendation: the colon
        form; the principal's to confirm.
      - **Things outside atelier that help the collaboration** (scan of
        every repo under the estate root, 2026-11-18; named here by class,
        since this repo is public and the holders are mostly private):

        | # | What it is | Where now | Size | Waits on |
        |---|---|---|---|---|
        | 1 | `/estate-health` → `/atelier:fleet-sweep` + ccfleet + private config | estate-root kit | M, 1–2 sessions | principal's pick to switch; `160/1450` |
        | 2 | `/fable-drain` → `/atelier:review-drain`; re-add the API-credit lane `210/440` dropped | estate-root kit | L, 2–4 | as 1, plus the lane's own pass |
        | 3 | Rule + guard: a new skill or command is born `/atelier:<name>` | none | S | nothing |
        | 4 | Model-required hook: wire `tools/modelguard.py`, retire the estate copy | estate-root kit | S | `160/1450` |
        | 5 | Status-line badge when the model is not the build model | `~/.claude`, in no repo | XS | nothing |
        | 6 | Hook refusing a command that would print a secret file | one service-estate child | M (path list → config) | nothing |
        | 7 | Guard: the stash stack is shared across worktrees, so an old stash is a peer's | one app child | S–M | nothing |
        | 8 | Check: a dead `.git/hooks/` copy shadowing the live `.githooks/` | one service-estate child | S | nothing |
        | 9 | "Which tree did this gate read" second line for every check | one app child | S | nothing |
        | 10 | Two children's own floor-verbatim verifiers → `stampscan`, once its two recorded blockers are fixed | two children | M | nothing |
        | 11 | Four separate "review on the API" runners (SDK lane, split reviewer, batch trial, a client batch reader) → one atelier lane | estate root + a private child | L, 3–5 | the principal's 2026-11-16 batch conditions (runner built, own cold pass, `030/420` MAJORs fixed) |
        | 12 | The review-queue reader (reads `docs/reviews/*.deferred.md`, atelier's own shape) → ccfleet's default queue | estate root | M | after 2 |
        | 13 | Private-pointer guard for an export tree: check overlap with `pointerscan` first | one infra child | S to judge | nothing |
        | 14 | A bare `/atelier` that prints the menu of every `/atelier:` command | new | S | nothing |

        💬 Row 14 was offered after the principal pressed Enter on `/atelier`
        and `/atelier:` expecting the list (the picker shows it only while
        typing). Asked whether to add it, his answer, 2026-11-18, verbatim:
        *"yes"*. How: a plugin skill is always `/atelier:<name>`, so a bare
        `/atelier` has to be a user-level skill named `atelier`. Version its
        definition here and link it into `~/.claude/skills/`, the way the
        estate kits are linked. Build the menu at run time from the plugin's
        `skills/` and `commands/` front matter, never from a typed list, so a
        new command appears without an edit.

        Stays where it is: business connectors (an accounting MCP),
        service and infrastructure tools, and each estate's repo list,
        rulings and run results (private by the 2026-11-13 split). The
        children's `.githooks/` are floor copies at several pins: pin
        drift for a health sweep, not a homing question.
      - **Total, roughly:** 12–18 build sessions on the build tier, plus
        one owed cold pass per strand under rule 4, about 5–7 review-tier
        passes, each waiting for the principal's approval of review-tier
        time.

      **Decisions owed when this is picked up** (ask in the device):
      the colon form; whether to switch the two estate kits to the
      general skills now; the order of rows 6–13; review-tier time for
      the passes. **How to re-run the scan**: list each repo's tracked
      `tools/ scripts/ bin/ hooks/ .claude/` files, keep those dense in
      collaboration terms (claude, fable, transcript, subagent, worktree,
      session log, board, cold pass), and drop floor copies; plus
      `~/.claude/{skills,hooks,settings.json}` and `~/.claude.json`'s MCP
      servers.
