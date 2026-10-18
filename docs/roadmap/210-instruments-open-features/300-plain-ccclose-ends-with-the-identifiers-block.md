- [x] **DONE 2026-10-18** (wt: atelier-qr-180-090)
      **Plain `ccclose` ends with the identifiers block.** Mike, 2026-10-18,
      on the claim that every close now ends with an identifiers block: *"is
      that written into the ccclose out command, not just in prompt or
      doctrine?"* Measured: partly. `ccclose --identifiers` prints the block
      (`210/280`), but the plain run a session makes at close prints only the
      checks, and `RECORD.md` still says "`ccclose` prints most of them"
      without naming the flag. So the block depends on a session choosing to
      ask for it. Owed: the plain run ends with the block, and `RECORD.md`
      names the command.

  **Closed 2026-10-18** (commit `bdb1aba`). A plain `ccclose` prints the
  block after the verdict, from the same gather as the checks. `--json` keeps
  the checks alone, and `--identifiers` still prints the block by itself.
  `RECORD.md` names the command. Instruments suite 476/476. The accuracy
  defect is still open at `210/290`. Cold pass: `160/920` widens to this
  commit.
