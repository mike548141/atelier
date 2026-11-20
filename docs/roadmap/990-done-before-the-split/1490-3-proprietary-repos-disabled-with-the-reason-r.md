- [x] **3 proprietary repos: `disabled`, with the reason recorded.** Measured,
      not assumed: with an unrecognised LICENSE, licenscan stops at "repo licence
      unrecognised" and verifies nothing further — it does **not** fall back to
      flagging a vendored copyleft file, proven against a fixture carrying
      exactly that, and an allow-marker on the LICENSE line does not restore it.
      So the tool gives these repos **no protection at all**, which is a stronger
      reason than "it is noisy".
