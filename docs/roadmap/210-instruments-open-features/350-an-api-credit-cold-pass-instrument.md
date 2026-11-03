- [ ] 🎯 **An API-credit cold-pass instrument: run a briefed review pass on
  the Platform API credit instead of the plan (a hand-up from a private
  child; Mike placed it 2026-11-02; port NOT started)**

  **Mike, 2026-11-02, verbatim:** *"this tool sounds like another that should
  be part of atelier along with ccmail etc"*.

  **What it is.** A private child built a stdlib-Python harness on
  2026-10-28 that runs one `REVIEW.md` brief cold through the Messages API.
  It is a tool loop with three client-side tools (read a file, list a
  directory, run a command), and every command runs under macOS
  `sandbox-exec`. The brief's deferred sibling is held back by name until
  act 2. Spend is metered from each response's own usage into a ledger,
  with a worst-case check against a cap before every call. The
  conversation is saved after each turn, so a pass cut off by the cap or a
  timeout resumes. Act 1 and act 2 are appended to the brief in the house
  format. It ran 18 passes for the child and its siblings over
  2026-10-28/29.

  **Why it is worth a tool.** Claude Code, even when given the API key,
  bills purchased credit. Only direct API calls draw a monthly API grant.
  So credit that would otherwise expire unused can run cold passes only
  through something like this.

  **ADR 0006's purpose test passes.** The tool's only purpose is the review
  cadence of the collaboration. It *extends* reach the way `ccmail` does
  and is not a general utility Claude merely uses. Runtime: Python, like
  `browser-fetch`. It needs the two-register `--help` and `man` page. Its
  unit tests (20) port with it.

  ## 🛑 Gate: its own cold pass FAILED, so port the fixed version

  The child's cold pass on the harness returned **FAIL, 5 MAJOR**. In
  generic terms:
  - **Held sibling still reachable.** Git's object store still serves it,
    so holding it by name does not partition the context.
  - **Sandbox too narrow.** It denies files and network but not other
    system services, so the clipboard and launching processes stay
    reachable.
  - **Reads blocked by a denylist.** Reads are denied by a named list,
    where an allowlist is needed.
  - **Shared temp writes.** Writes into shared temporary directories reach
    other sessions' scratch.
  - **No decision record.** Nothing weighs the Agent SDK route.

  Those rulings are the principal's, and the fixes wait on them. The
  child's re-read of all 18 runs found none of the holes exercised. That
  is evidence about those runs, not about the tool.

  **Sequencing (default; the principal may override):** port and fix as
  **one change**, so that a single cold pass covers the public version.
  That pass is Fable work, so it waits on his approval. If the Agent SDK
  ruling changes the design, porting first would have been wasted work.

  ## What stays in the child

  These stay in the child: the keychain item names, the estate root path,
  which sibling repos are public, the run directory, the ledger and cap
  history, and every record of the passes run. In the port, each becomes a
  flag or environment setting with a neutral default. No record crosses.

  ## Open

  - 🎯 **Name.** A `cc*` working name such as `ccpass` is a placeholder,
    not a choice.
  - **Skill.** The machine-local drain skill that drives the harness then
    points at the instrument, not at the child's path.
