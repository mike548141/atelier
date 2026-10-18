# Sibling to the queue-run-carries-the-brief cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-18-0517-queue-run-carries-the-brief-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-18 UTC by the Opus brief-writer named in the brief's provenance; it
forms no finding. Fold this file in below the reconcile and delete it at phase 2.

## Facts held back

1. **Intent and commissioning records:** `180/010`, `180/020` and `180/030` (the pointer's
   intent records), and `180/040`, `050`, `070`, `080`, `090` (the items the later commits
   close) — **none opened by the brief-writer**, beyond the claim lines of `180/090`, which
   carry a quoted line of the principal's that the skill header and test docstring also quote.
   No commit body was read, so this sibling carries no account of the author's reasons; read
   them at reconcile.
2. **Neighbouring passes.** The same authoring session's `adf75a4` (`160/910`) and
   `8132805`/`30aa8dc` (`160/930`) were briefed in the same sitting by this brief-writer, and
   `160/940` (the template history in `docs/method/session-open/`) by another brief-writer
   under the same dispatching run. `160/940`'s file shares a directory and a README with this
   pass's prompt.
3. **The pointer was widened after the briefs were claimed.** The briefing worktree was cut at
   `f0d6238`, before `12e6d9b` landed; the pointer on `origin/main` was widened to `12e6d9b` by
   `055b326`, and this brief was written from that wider text.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. **The path a run is told to read.** The prompt tells a run to read "the *current*
   `../atelier/docs/method/CONCURRENCY.md`". That resolves only from a sibling checkout of
   atelier. Before `12e6d9b` the skill said where else to read (a local checkout, else the
   plugin's bundled copy); after it, that fallback lives only in `CONCURRENCY.md` — which the
   run reaches through the same unresolvable path. What does a run in an unrelated repo,
   installed from GitHub, actually read?
2. **"Adds nothing."** The skill header, the session-open README and the prompt all say the
   skill adds nothing to the prompt. The skill still adds: "follow it as his own brief, word for
   word", the mapping of the invocation text onto the prompt's *This run* section, the
   empty-invocation default, and a frontmatter description that restates the pattern. Are those
   additions, and does "cannot differ" overclaim?
3. **What the test can see.** It flags only sentences of 40 characters or more copied verbatim.
   A paraphrase, a contradiction, or a shorter copied rule passes. Its own docstring concedes
   paraphrase. Is a green run here being read as "no drift", which is the claim the prompt now
   prints?
4. **Rules lost in the collapse.** The pre-`12e6d9b` skill carried steps (sync with
   `git status` before `--autostash`, claim from the primary checkout, per-item close, worker
   dispatch and the teardown marker from `1487e9c`, the report's contents). Is each still stated
   somewhere a run reads, or did the teardown sentence `1487e9c` added to the skill go with it?
5. **Principal-owned text, edited.** By the brief-writer's count, `998c35f` removed nine
   passages from the prompt (the date paragraph, "balancing value, urgency…", "Leave the
   repo…", "watch for their changes in-flight", "visuals", "Verify facts…", the bullet-list and
   checklist bullets, and the tail of close item 3). `140a190`, whose subject says "four prompt
   lines come back", restored five of them by the same count; `1adf398` then replaced the date
   paragraph. Four are still absent at HEAD. The README now
   says an agent changes this file only on his say-so, quoted in the commit. Did each removal
   have it?
6. **Ask cadence, now always on.** The prompt both says "Ask me with AskUserQuestion when you
   need a decision, mid-turn" and ends "Try not to stop and ask me questions until you have done
   all the work. I won't be here…". `CONCURRENCY.md` makes the away cadence conditional on the
   principal saying he is away. If the command runs the prompt word for word, is the away
   cadence the default for every run, contradicting the doctrine's default?
7. **Two homes after "one text".** `CONCURRENCY.md` restates the prompt's rules (three
   selection rules, what the report carries, how the run talks to him) as doctrine "homed" from
   the prompt. The single-source test guards skill-versus-prompt only. `1adf398` had to edit
   prompt, `CONCURRENCY.md` and skill together to move the date line to the session id. Is the
   drift class closed, or moved?
8. **Versioning by commit.** With no `version`, the README says each commit is a version and the
   pre-commit hook's scanner path is pinned to it, so the hook must be re-installed in each
   hooked repo "after every plugin update". Does that make every update a blocking event in
   every child repo, and is "Claude Code falls back to the commit" checked against the tooling?
9. **The identifiers block's sources.** It asks for agents launched and worktrees created and
   removed, and says the worktree list "comes from the transcript". Can a session that was
   compacted or resumed recover those, and does `ccclose` print them? (The authoring session's
   own identifiers line gives a window that ends before its own later commits.)
