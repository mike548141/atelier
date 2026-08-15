- [ ] **Adapt the exposure doctrine so it distinguishes what can be rotated from
      what cannot, and admits history rewriting as a right action in the second
      case.** Captured verbatim from Mike, not yet designed or decided:

      > Doctrine has various points about keeping history, rotating exposed
      > secrets etc.. That stands true but we need to adapt the doctrine to
      > differenitate between things like secrets that can be rotated and
      > confidential, classified, and private information that can't be changed
      > once its exposed. For example there might be situations that rewriting
      > git history is the right action to clear information that was exposed

      **What doctrine says today** (starting points for the design pass, not a
      verdict on them):
      - [`method/SECRETS.md`](../../method/SECRETS.md) is built end-to-end on the
        cheap-burn model — *detect → rotate → the burn cost is minutes* — and
        already names the exception in one line without giving it a remedy:
        "a leak of personal data is the one exposure no rotation undoes"
        (§ *the advisory asymmetry*).
      - [`method/AUTONOMY.md`](../../method/AUTONOMY.md) § *Recoverability ends at
        push* says a pushed secret "is burned even after a history rewrite", and
        classes force-push / history rewrite on a shared branch as
        **truly destructive / irreversible** — the floor that would have to bend
        for a rewrite to ever be the correct move.
      - [`decisions/0005-going-public.md`](../../decisions/0005-going-public.md)
        rejected a pre-flip rewrite ("irreversible effort spent") — a decided
        instance the reframing has to be consistent with, since that case was
        identity, not exposure.
      - [`method/REVIEW.md`](../../method/REVIEW.md) and
        [ADR 0002](../../decisions/0002-sha-is-the-version.md) both lean on
        *this repo does not rewrite history* — review outputs preserved
        verbatim, and child pins that a force-push would orphan.

      **The shape of the gap.** Every rule above is calibrated for the rotatable
      class, where the burned value is replaced and the old commit is inert.
      For the unrotatable class — confidential, classified, personal — the
      exposed bytes *are* the harm and they stay live in history for as long as
      history does, so "keep history, rotate the value" gives no remedy at all.
      Rewriting is not a clean fix there either (clones, forks, caches, the
      orphaned-pin cost), which is exactly why the doctrine needs to say when
      partial containment is worth its price rather than leaving each session to
      improvise.

      **Open questions for the design pass** (none answered here): where the
      class boundary is drawn and whether the scanners can tell the classes
      apart at the point of blocking; what the decision test is for rewrite vs
      accept-and-disclose; who authorises it (this is Mike-floor territory, not
      agent discretion); how it interacts with the ADR 0002 pin contract and the
      signing floor; and what the honest ceiling on containment is once a public
      repo has been cloned.
