# Rework OPUS48 i6 — product_i6 → product_i7

Materialized `product/product_i7.ipynb` (122 cells). Re-executed all cells in a fresh kernel:
**0 exceptions, all assertions pass.** One-sentence fix (F-031); no code touched.

## Decision table

| id | decision | where (product_i7) | one-line rationale |
|----|----------|--------------------|--------------------|
| F-031 | FIX | cell 100 | Turned the false "for a nondegenerate two-sided range, `qmin<z<qmax`" (interior zero-point as automatic) into the correct feasibility implication. |

## Concrete edit — cell 100
- before: "For a nondegenerate two-sided range, `qmin<z<qmax` and this reduces to
  `s ≥ max(-a/(z-qmin), b'/(qmax-z))`."
- after: "**If** fixed-`z` coverage of a nondegenerate two-sided range **is feasible, then**
  `qmin<z<qmax` and this reduces to `s ≥ max(-a/(z-qmin), b'/(qmax-z))`; if the rounded `z`
  instead lands on a boundary — which a highly asymmetric range can force (e.g. `[-0.001,1]`
  rounds `z` to `qmin`) — then `c_-` or `c_+` is `+∞`: no fixed-`z` scale covers that side, so
  move `z` inward and recompute `s` (or report coverage impossible with that fixed `z`)."
- This matches SOL56's suggested wording and makes the piecewise `c_-/c_+` definition and the
  interior-`z` reduction mutually consistent.

## LEDGER
- F-031 → RESOLVED (the iter-7 audit confirms → FROZEN).
- No REJECT-WITH-RATIONALE; nothing CONTESTED. This is the sole remaining item; product_i7 now
  has no open findings pending confirmation.
