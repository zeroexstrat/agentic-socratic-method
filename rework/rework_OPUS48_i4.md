# Rework OPUS48 i4 — product_i4 → product_i5

Materialized `product/product_i5.ipynb` (122 cells). Re-executed all cells in a fresh kernel:
**0 exceptions, all assertions pass.** One fix (F-015), turned into an honest break→repair.

## Decision table

| id | decision | where (product_i5) | one-line rationale |
|----|----------|--------------------|--------------------|
| F-015 | FIX | cells 100–101 | Corrected the affine-quantizer calibration: the naive `s=(b'-a)/(qmax-qmin)` with integer-rounded `z` does not cover the observed range, so `x=1` clips; the code now proves that, applies the half-step lemma only on the non-clipped subset, then repairs `s` so the grid covers `[-1,1]` and the lemma holds everywhere. |

## Concrete edit

### F-015 — cells 100 (markdown) + 101 (code)
- before: the markdown claimed the range calibration "covers the observed range," and the code
  asserted `|x-x̂| ≤ s/2` over **all** points — including `x=1`, which clips (grid after
  rounding `z=4` is `[s(0-4), s(7-4)] = [-8/7, 6/7]`, not `[-1,1]`). The assertion passed only
  because `1.0` sits exactly half a step from `6/7`.
- after (break): the markdown states the actual representable interval `[s(qmin-z), s(qmax-z)]`,
  explains that rounding `z` shifts the grid so naive calibration can under-cover, and gives the
  coverage condition `s ≥ max(-a/(z-qmin), b'/(qmax-z))`. The code computes the grid interval,
  shows `x=1` clips (pre-code `8 → 7`), notes its `s/2` error is coincidental, and asserts the
  half-step lemma **only** on the non-clipped points.
- after (repair): recompute `s = max(-a/(z-qmin), b'/(qmax-z)) = 1/3`; the grid `[-4/3, 1]` now
  covers `[-1,1]`, nothing clips, and `|x-x̂| ≤ s/2 = 1/6` holds for **every** point (tight at
  `x=0.5`). Zero remains exactly representable. Output confirms all of this.
- external truth: SOL56 noted source A shares the same coverage error (its cells 79/81), so per
  CONTRACT §1 external mathematical truth controls — this correction departs from both sources.

## New material for the iter-5 audit
Cells 100–101 only. The break→repair now teaches a real calibration lesson (integer zero-point
rounding vs. range coverage); the numbers are computed, not asserted-into-existence.

## LEDGER
- F-015 → RESOLVED (next audit confirms → FROZEN or re-OPEN).
- No REJECT-WITH-RATIONALE; nothing CONTESTED. My iter-3 signoff remains retracted (voided).
