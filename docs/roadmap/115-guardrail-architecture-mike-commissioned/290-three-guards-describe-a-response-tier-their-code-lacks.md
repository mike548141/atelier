- [ ] 🔎 **Three guard descriptions disagree with their own code**
      `[S][tools]`. Found 2026-10-16 by the `090` audit and checked against
      the code before filing. Not fixed in passing:
      1. **licenscan promises a warn tier that does not exist.** Its
         docstring (`licenscan.py:35-38`) and its README section say a
         permissive-into-permissive mix, or an unknown declaration, is a
         *warn*: "friction, never a silent pass". In the code,
         `compatibility()` returns `warn`, which becomes a `medium` finding,
         and every finding counts toward exit 1
         (`report.exit_code(len(rep.findings))`, `licenscan.py:726`). So a
         "warn" blocks. Either the text or the code is wrong. Which one is
         a question about the guard's posture.
      2. **pathscan's docstring says it is not in the registry**
         (`pathscan.py:15-20`). It has been registered since 2026-08-05
         (`floor.py`, `tools/README.md`, `ci.yml`). This is a plain fix.
      3. **floor.py says boundary checks have no advisory form "by
         design".** publishscan is a boundary check, and it carries one, as
         an adoption aid rather than a severity tier (the comment beside it
         says so). The general sentence needs that exception.
      **The work:** 2 and 3 are plain fixes. 1 needs the posture read
      before choosing between the code and the text. It is the cheapest
      second dial on the board (`090`).
