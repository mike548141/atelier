# 2026-11-14 · 0054 UTC — The fleet kits versioned: `ccfleet`, two skills, `modelguard`

**Session:** `559edaec`, Claude Opus 5.5, headless, started inside an atelier worktree by an
estate health sweep, orchestrator session 58027096, for one task. No review-tier model was used
and no review was run or briefed.

## What was done

- **Read** the two user-level kits the task named (the fleet health sweep and the review drain:
  skills, prompts, launch and driver scripts) and the model-required hook with its test. Read only;
  nothing outside this worktree was edited.
- **Built `instruments/ccfleet`** (`210/440`): the per-repo billed runner, the gated parallel and
  serial-per-repo drivers, the queue-driven drain, resume, and `run --in`. Every value that belongs
  to one estate moved to a config; the example config is fictional.
- **Built `skills/fleet-sweep/` and `skills/review-drain/`** with their prompt templates. The
  principal's words are filled in from the private config (`{ASK}`, `{APPROVAL}`), never quoted in
  the skills.
- **Ported the hook** to `tools/modelguard.py` with a unittest-form test; the plugin does not wire it.
- **Queued the rule-4 cold pass** as `160/1450`; no brief, since this session built the subject.

## Evidence worth keeping

- 🔎 The source kits were zsh. Rewritten in Python so a running driver cannot be broken by an edit
  to its own file, the failure the zsh kits recorded; the end-to-end tests stand a throwaway git
  repo with a local bare remote and a stand-in `claude` that records its argv, working directory
  and stdin, so the billing key (worktree basename), the explicit `--model` and stdin from
  `/dev/null` are asserted, not assumed.
- ⚠️ The routing test caught one quote: the answer that started the work was a pick among options
  whose words name a private repo. The item paraphrases it and says why.
- The source's original hook test passed unchanged against the source hook (0 failures) before the
  port; the ported tests pass against the port.
