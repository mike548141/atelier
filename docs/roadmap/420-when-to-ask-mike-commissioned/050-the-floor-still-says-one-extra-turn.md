- [ ] **The floor's *Asking* bullet still says "(one extra turn)".** A
      hand-up from a private child, found 2026-11-13 UTC at a pin bump to
      `2a6d7a4`. `COMMUNICATION.md` § *Asking for a ruling* now says the
      account is written as text first and the device follows **in the same
      turn** (`420/040`, fixed 2026-11-12). The canonical `floor` region in
      `PROPAGATION.md` was not changed with it: its *Asking* bullet still
      reads "always as a finished message of its own, ahead of the device, in
      every view (one extra turn)". Every child copies the floor verbatim, so
      every bumped child now carries the old instruction on its read path,
      and the onramp is read before `COMMUNICATION.md`.
      **Evidence:** `git show origin/main:docs/method/PROPAGATION.md`, the
      *Asking* bullet of the floor region, against the 2a6d7a41 hunk in
      `COMMUNICATION.md`.
      **Owed (atelier's):** align the floor region with `COMMUNICATION.md`
      and say so in the fleet's next pin bump. The child stopped at the
      report and copied the floor as it stands.
