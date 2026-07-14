# Audit OPUS48 i5 — auditing product_i5

**Verdict: SIGN-OFF.** The F-015 fix is correct and complete; product_i5 executes clean
(47/47 code cells, 0 exceptions, only the deliberate ε=0 LayerNorm warning). No new BLOCKER or
MAJOR. I confirm F-015 → FROZEN and re-emit `signoff/SIGNOFF_OPUS48.md` on product_i5.

## Verification performed
- Fresh-kernel execution of all cells: 0 exceptions; all assertions pass.
- Independently re-derived the F-015 fix: with the naive calibration `s=2/7, z=4` the grid is
  `[-8/7, 6/7]`, exactly one point (`x=1`) clips, and the half-step lemma holds on the four
  non-clipped points; the repaired `s=1/3` gives grid `[-4/3, 1]` covering `[-1,1]` with no
  clipping and `|x-x̂| ≤ s/2 = 1/6` for every point (tight at `x=0.5`), zero still exact.
- Confirmed no sibling: the min/max `quantize()` helper (per-channel and perplexity-vs-bits
  demos) has no integer zero-point and maps `min→0`, `max→qmax`, so it covers `[min,max]`
  exactly and cannot exhibit this clipping.

## Re-audit
### F-015 — confirm → FROZEN
The calibration coverage claim and the misuse of the no-clipping lemma are gone. The cell now
teaches the real lesson honestly (break: naive scale under-covers → `x=1` clips, its `s/2` error
coincidental; repair: enlarge `s` to `max(-a/(z-qmin), b'/(qmax-z))` so the grid covers the range
and the lemma applies everywhere). This departs from both sources on external mathematical truth,
which is correct per CONTRACT §1.

## New findings — none
Only cells 100–101 changed from product_i4 (which SOL56 audited at iter 4, finding only F-015).
Per axis: MATH — the F-015 fix is the sole change and is verified; CODE — 47/47 execute, the new
asserts test the actual clipping/coverage; CLAIM/FIDEL/PED/NOTE — unchanged from the
already-audited product_i4, no regressions.

## Signoff
Re-emitted (`signoff/SIGNOFF_OPUS48.md`, version product_i5). All findings FROZEN; no MINOR left
OPEN. Strongest remaining objection: the exact-digit Worked Examples 4.1 (attention head) and 6.1
(AdamW step) remain unported — genuine but below the blocking bar. Convergence remains the
harness's call, contingent on SOL56 independently signing this same product_i5 over an unchanged
round.
