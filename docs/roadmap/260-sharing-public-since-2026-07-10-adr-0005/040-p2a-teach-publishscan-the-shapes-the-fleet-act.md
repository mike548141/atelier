- [x] **P2a — teach `publishscan` the shapes the fleet actually has.** The
      denylist was written from one finding plus standard practice, which is
      the honest starting point and not a survey. The sweep that grounds a
      second round is P7's (transcripts + session logs) plus a tracked-file
      pass over all twelve repos — what else is tracked that nobody would
      publish deliberately?
      ---
      ✅ **The tracked-file half LANDED 2026-10-03 (queue run, merge
      `a91d9b6`). The transcript half stays with P7 (`090`), so the item
      stays `[ ]`.** A names-only survey covered all 29 sibling repos' tracked
      sets. File contents were not read, except a first line where a shape
      needed it. The survey found few shapes, all in private repos. Logs,
      local databases and compiled-Python caches are recorded as
      "measured". Secret-carrier shapes are recorded as standard practice
      only, because a public file must not describe a private repo's posture,
      even unnamed. Round 2 adds those plus about 55 standard-practice shapes:
      key and keystore files, history files, dumps and captures, tool
      caches, agent-local files (`CLAUDE.local.md`, `.claude/worktrees/`) and
      OS cruft. **Considered and left out, with reasons in the source:**
      generic `*.pem` (public chains are tracked legitimately),
      `credentials*.json` (a no-secret registry and fixtures wear the name),
      `*.rsc` (source and device exports share it), archives, `*.jsonl` and
      `*.pub`.
      📏 **Blast radius, measured old against new over every sibling:** 3
      private repos newly red, 23 files. Public repos 0, archived 0 new.
      atelier itself stays clean (884 paths).
      ⚠️ **Corrected the same day.** This first said children "meet it at their
      next pin bump". They do not: children call `floor.yml@main`, and their
      scanners float at `main` by design ("newest scanner = safest"). So the
      3 private repos go red at their **next CI run**, which is the design
      working on latent findings. The claim came from reasoning without
      checking the workflow. `020/150`'s build caught it. 30 tests pass and the selftest is OK. Code pass
      queued at `160/470`.

      ✅ **Closed 2026-10-05.** The tracked-file half landed earlier, as
      recorded above. The transcript half was held for P7 (`090`), which has
      now run. Its answer, one new shape (`*.egg-info/`) and the larger gap
      that `publishscan` reads only the current tree while a flip publishes
      all history, is carried forward as item 3 of `110` (P9). No work is owed
      in this item; P9 holds what remains.
