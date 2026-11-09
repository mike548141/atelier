- [ ] **Claude Code session hooks as a house enforcement plane: decide which
      hooks to use, to do what and how, so they work on atelier and every
      child repo.** Filed from a private child, 2026-11-09, on the principal's
      instruction. Work to pick up. Nothing here has been designed or ruled
      yet except where his words say so.

      **The principal's words, verbatim.**

      > I want policy enforced as code. So that when I have a policy (like
      > choosing the right model or how to ask me [the principal] a question) a
      > claude session cant forget or not know to action it, nor can it avoid
      > it without being noisy or asking me for a ruling to override perhaps

      > Note there is some things in atelier which is guidance or principals
      > that may not make sense to enforce using policy as code

      > Ok I think claude hooks could become central to atelier and the way it
      > improves how we work together, and you have a lot of good info and
      > thoughts in this transcript.
      > I want you to put this on the atelier board as work to pick up and use.
      > We will look at which hooks we should be using, to do what, and how
      > etc.. so that it works on all repos both atelier and the child repos

      Those are all of his words on this. Everything below headed **Proposed**
      is Claude's, offered in the session and not ruled.

      **Read first; these bind the design.**

      - `020/310` and `020/360`: the reply gate, a `Stop` hook, was unwired and
        then destroyed. A `Stop` hook cannot un-print: blocking makes the model
        emit a second full copy under the first. Mike's words there: *"not
        just USELESS but DANGEROUSLY bad"*.
      - [`MECHANISMS.md`](../../method/MECHANISMS.md): hooks are already listed
        as a mechanism, with the test *can the enforcement point deliver the
        remedy, not only detect the fault?*
      - `020/220` (the census of which rules have a forcing function) and
        `020/230` (doctrine that reaches the moment of decision).
      - `020/170` (the block-versus-advise model) and `400/010` (choosing a
        mechanism).

      **What is live on the principal's machine today** (read from the settings
      files and plugin caches, 2026-11-08).

      | Scope | Fires on | Does |
      |---|---|---|
      | User settings | `PreToolUse`, `mcp__.*` | Auto-approves every connector tool |
      | User settings | `PreToolUse`, `Agent\|Bash` | The model-required guard, below |
      | One private child, shared settings | `SessionStart`, `startup` | Runs that repo's estate check |
      | One private child, `settings.local.json` | `PreToolUse`, `Bash` | Blocks commands that read secret values |
      | Plugin (review-council) | `PreToolUse`, `Agent` | Blocks reviewers when governance files differ from the default branch |
      | Plugin (AWS, Anthropic) | `PreToolUse`, `Bash` and AWS tools | Blocks direct fetches from AWS Secrets Manager |

      The atelier plugin ships no Claude Code hooks. Its guards are git hooks
      and CI.

      **The worked example: the model-required guard.** Built 2026-11-08 in
      `~/.claude/hooks/agent-model-required.py`, with its tests beside it in
      `test_agent_model_required.py`. Neither file is in any repo yet.

      - It refuses an `Agent` call with no `model` (a fork is exempt), and any
        shell `claude` command that starts or resumes a session with no
        `--model` or `ANTHROPIC_MODEL=`. Management subcommands pass.
      - The command text is tokenised with heredoc bodies dropped, so a commit
        message mentioning `claude -p` is not a launch.
      - Evidence: 28 cases, 0 wrong, plus a live refusal and a live pass in the
        building session, using `true || claude …` so that nothing ran. About
        0.2 s per shell command.
      - Not cold-reviewed. A guard is a silent-failure surface, so what ships
        here owes a rule 4 pass, on Fable, which waits for his approval.

      **Who runs a hook.** The harness does, not the model. A session does not
      call one, cannot decline one, and usually does not know one exists until
      it is refused or handed a message. That is the property his first
      sentence asks for. It is not the same as airtight:

      | Gap | Detail | State |
      |---|---|---|
      | Guards one tool, not the intent | A matcher sees one tool name. The same effect may be reachable another way | Shell route closed for the model rule. A script that starts `claude` itself stays invisible: the Fable drain's `run-pass.sh` and `resume-pass.sh` do, and they name a model today, unchecked |
      | The hook is editable | Hook files and settings sit in `~/.claude/`, writable by any session in bypass mode | Open |
      | Fails open | The CLI's own text for `PreToolUse`: exit 2 blocks, *"Other exit codes - show stderr to user only but continue with tool call"*. A crash or a missing interpreter lets the action through. The guard above also passes on a malformed payload | Open |
      | Can be switched off | The CLI's strings name `disableAllHooks`, `allowManagedHooksOnly`, bare mode, safe mode and an untrusted workspace. Sessions on another machine or in the cloud have no `~/.claude` hooks | Open |

      **Every point a hook can attach to: 33 events**, read from the strings of
      the installed CLI, v2.1.302. Re-read on a version bump; the list grows.
      Read, not driven: only `SessionStart` and `PreToolUse` have been run here.

      | Event | Fires | Exit 2 or decision output |
      |---|---|---|
      | `Setup` | Repo setup, init and maintenance | Context only |
      | `SessionStart` | New session | Stdout reaches Claude; cannot block |
      | `SessionEnd` | Session ending | Watch only |
      | `InstructionsLoaded` | A CLAUDE.md or rule loads | Watch only, by design |
      | `ConfigChange` | A settings file changes mid-session | Blocks the change |
      | `CwdChanged` | Working directory changes | Watch only |
      | `DirectoryAdded` | A directory is added mid-session | Watch only |
      | `FileChanged` | A watched file changes (matcher names files) | Watch only |
      | `UserPromptSubmit` | Prompt submitted | Blocks and erases it; stdout reaches Claude |
      | `UserPromptExpansion` | A slash command expands | Blocks the expansion |
      | `PreToolUse` | Before a tool runs | Blocks; allow, deny or ask |
      | `PermissionRequest` | A permission dialog shows | Allow or deny by JSON |
      | `PermissionDenied` | Auto mode refused a call | Watch only |
      | `PostToolUse` | After a tool runs | Stderr shown to the model |
      | `PostToolUseFailure` | After a tool fails | Stderr shown to the model |
      | `PostToolBatch` | A batch of calls resolves | Stops the agentic loop |
      | `Elicitation` | An MCP server asks for input | Denies it |
      | `ElicitationResult` | The user answered it | Turns the answer into a decline |
      | `Stop` | Claude is about to finish | Continues the conversation (see `020/310`) |
      | `StopFailure` | Turn ends on an API error | Not read |
      | `MessageDisplay` | Reply text is displayed | Can change what is displayed |
      | `Notification` | A notification is sent | Watch only |
      | `SubagentStart` | A subagent starts | Context only; **cannot block** |
      | `SubagentStop` | A subagent is about to finish | Keeps it running |
      | `TeammateIdle` | A teammate is going idle | Keeps it working |
      | `TaskCreated` | A task is being created | Refuses it |
      | `TaskCompleted` | A task is being marked done | Refuses it |
      | `PreCompact` | Before compaction | Blocks it; stdout adds instructions |
      | `PostCompact` | After compaction | Watch only |
      | `PreModelSwitch` | Before a model change | Blocks; allow, deny or ask |
      | `PostModelSwitch` | After a model change | Stdout reaches Claude |
      | `WorktreeCreate` | Worktree creation | The hook does the creating |
      | `WorktreeRemove` | Worktree removal | The hook does the removing |

      Handler kinds in the CLI's strings: `command`, `http`, `prompt`, `agent`,
      with an MCP-tool kind also named. Places a hook can live: user settings,
      a repo's `.claude/settings.json`, `settings.local.json`, a plugin's
      `hooks/hooks.json`, and managed policy settings.

      **Proposed (Claude's, unruled).**

      1. Sort each rule into a level, as the output of `020/220`:

         | Level | What happens | `020/220` state |
         |---|---|---|
         | Enforce | The action is blocked; an override needs his recorded ruling, which the hook reads | enforced |
         | Nudge | The rule is put in front of the session at the moment it applies, with no block | directive-only, delivered at the point of use (`020/230`) |
         | Judgement | Stays written guidance, no hook | unenforceable, accepted |

      2. Ship the mechanism in the atelier plugin's `hooks/hooks.json`, which
         reaches every repo where the plugin is on, and keep estate-specific
         values (approved models, the Fable approval list) in a private config
         the hook reads. The same split as a public tool and its private owner.
      3. A Fable gate: `PreModelSwitch` for a mid-session switch, plus
         `PreToolUse` on `Agent` and `Bash` for launches, because
         `SubagentStart` cannot block.
      4. Harden what ships: fail closed, guard the hook files against edits,
         and refuse mid-session settings changes through `ConfigChange`.
      5. Put the hooks that must not be switched off in managed policy
         settings. Untested here.

      ⚠️ **Withdrawn from the session's proposals.** Claude offered, as a nudge
      example, flagging a reply that ends on a question. It offered this before
      reading `020/310`. Fired from `Stop`, that is the destroyed gate's shape.
      Enforcing how he is asked needs a point that acts before the reply is
      printed, or a data-collector role, which is the alternative his
      2026-08-15 ruling named.

      **Questions for the pick-up, his to rule.**

      - 🎯 Which rules get a hook first? His two examples are choosing the
        model and how he is asked a question.
      - 🎯 What does a loud override look like: his recorded ruling read by the
        hook, or a visible self-declared bypass?
      - 🎯 Fail closed or fail open, per guard? `020/280` records every error
        path of the old reply hook failing open.
      - 🎯 Plugin, managed settings, or both? Public adopters get whatever the
        plugin ships, so does a house hook default to off for them?
      - 🎯 Does the Fable gate get built?

      **Provenance.** Principal's session `43810980`, 2026-11-08 to 2026-11-09.
      Per `PROPAGATION.md` § *Pointing up*, the mechanism claims here are
      testimony: re-drive them before they become house text.
