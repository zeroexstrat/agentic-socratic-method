# TURN: SIGNOFF  (emitted only when you believe the artifact is done)

**You are {SELF}.** You may emit `signoff/SIGNOFF_{SELF}.md` only when, from your
audit this round, the convergence predicate (CONTRACT §6) looks met: no OPEN or
CONTESTED BLOCKER/MAJOR, and you raised no new BLOCKER/MAJOR this round.

A signoff is INVALID (and the harness will reject it) unless all of the following
hold. Fill each field honestly — an empty or evasive field voids the signoff.

```
# SIGNOFF — {SELF}

version_signed: product_i{n}          # exact version you are approving
round: {n}

findings_i_logged_this_run: {count}   # must be ≥ 3 substantive (MAJOR+ or upheld MINOR)
finding_ids: [F-003, F-011, F-019, ...]

strongest_remaining_objection: >
  {The single thing you would still change if you could, and WHY you judged it
  below the blocking bar. "Nothing" is not permitted — if the artifact were
  perfect the contract would be miscalibrated. Name the least-satisfying part.}

minors_left_open: [F-021]             # each requires explicit waiver below
minor_waivers: >
  {For each MINOR left OPEN, one line on why convergence is acceptable with it open.}

statement: >
  I, {SELF}, affirm product_i{n} meets CONTRACT §2 on all six rubric axes to the
  BLOCKER/MAJOR bar, that I engaged {OTHER}'s findings adversarially rather than
  deferentially, and that my agreement reflects verification, not fatigue.
```

Convergence is declared by the HARNESS, not by either model, only when BOTH valid
signoffs name the SAME `product_i{n}` and that version went a full round unchanged.
