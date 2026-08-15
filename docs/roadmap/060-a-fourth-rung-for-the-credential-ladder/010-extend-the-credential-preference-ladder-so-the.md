- [ ] **Extend the credential preference ladder so the standing credential is
      not the only honest answer where the platform offers no JIT grant.
      Where a credential is used *irregularly or rarely*, doctrine should name
      an alternative in Mike's words: "delete the credential entirely and make
      its rebuild cheap, automated and tested".** Captured from Mike; not yet
      designed or decided.

      **What doctrine says today.** `method/SECRETS.md` § *The credential triad*
      ranks least-privilege → just-in-time → short-lived, then concedes that
      most platforms offer neither of the last two, so standing credentials are
      "the common honest reality" — allowed as a **tracked debt to shorten**
      with a stated reason. `method/PRINCIPLES.md` §5 carries the same bridge
      (*honest pattern*, and the checklist line "Standing or ephemeral
      credential?"). Both stop at *track the debt*.

      **The gap.** Between "standing forever, tracked" and "the platform grants
      JIT" there is a third state the doctrine never offers: the credential
      simply **does not exist between uses**. Mint it for the run, delete it
      after, keep the mint automated and exercised. A credential that isn't
      there is just-in-time to the extent the platform allows — achieved by the
      *holder*, not granted by the vendor — and the debt is paid rather than
      carried. Cheap to reach precisely where use is infrequent, which is also
      where a standing credential sits idle and unwatched longest.

      **It is already implied and never stated.** SECRETS' enabling property is
      store-the-rule-not-the-value: what's durable is the *procedure to mint*,
      not a frozen token. If that holds, the value's continued existence between
      uses is an unforced choice — but nothing says so, so every session lands
      on "standing, tracked" as the terminal state.

      **Open questions for the design pass (not answered here):**
      - Where does it sit? A fourth rung *below* the triad (JIT/short-lived
        remain better when the platform offers them), or a branch off the
        bridge rule that fires on the use-frequency test?
      - What makes a rebuild admissible — automated, tested, and *rehearsed on
        a cadence*? An untested rebuild path converts a standing-credential
        risk into an outage risk, which is a trade, not a win.
      - The bootstrap recursion: the rebuild path itself authenticates with
        something. Deleting the leaf while the minting credential stands is
        still progress, but the ladder must say so rather than imply the
        regress terminates.
      - Frequency boundary: at what cadence does mint-per-use stop being
        "rebuild on demand" and become plain JIT (and stop needing its own
        rung)?
      - Interaction with rotation-on-cadence (SECRETS § *Rotation cadence*):
        a credential that never persists has no undetected-exposure window to
        bound, so does the cadence duty lapse or transfer to the mint path?

      **Grounding, honestly.** Raised from a sibling session's ADR arguing
      exactly this for a backup tool on a platform whose delegation grant is
      standing-only — no JIT, no expiry — where the credential is deleted after
      each run and rebuilt from a tested, automated path. That is one worked
      case in a child repo, not yet an atelier-side pattern; the design pass
      owes a second instance or an explicit one-case claim before it becomes
      doctrine (`create-repo`'s stub-don't-fabricate rule, and the
      grounding bar in `CLAUDE.md`).
