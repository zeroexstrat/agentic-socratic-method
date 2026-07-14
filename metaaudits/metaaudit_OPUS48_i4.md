# Meta-audit OPUS48 i4 — adjudicating audit_SOL56_i4

**Overall:** SOL56's audit is correct on all three counts, and its F-015 re-open is a genuine
catch that my iter-3 signoff missed — I owe it a retraction. I independently recomputed the
quantizer grid and confirm the defect; I uphold the re-open, concur with freezing F-029/F-030,
and retract my (now-stale) product_i3 signoff.

## F-015 — verdict: UPHELD (re-open on new evidence) → ACCEPTED (MATH / MAJOR)
- reasoning: Verified numerically and independently. With `x∈[-1,1]`, 3-bit, the calibration
  gives `s=2/7`, `z=round(3.5)=4`, so the **actual** representable grid is
  `[s(0-4), s(7-4)] = [-8/7, 6/7] ≈ [-1.143, 0.857]` — it does **not** cover the observed range
  `[-1,1]`. At `x=1`, the pre-clip code is `round(7.5)=8`, clipped to `7`; the dequantized value
  is `6/7`, so `x=1` **clips**. The cell's assertion `err ≤ s/2` passes only because `1.0` lands
  exactly half a step from `6/7` — a numerical coincidence, not a verification of the half-step
  lemma, whose premise (no clipping) is violated. So the self-check "gives the right number for
  the wrong stated reason and teaches a false coverage guarantee." SOL56 is right that source A
  shares this error (its cells 79/81), so external truth controls per CONTRACT §1. MAJOR upheld.
- fix plan (my rework): keep the honest break→repair form — compute and print the actual grid
  interval, show `x=1` clips, verify the half-step lemma only on the non-clipped subset, and add
  the coverage condition `s ≥ max(-a/(z-qmin), b'/(qmax-z))` (here `1/3`) with the corrected grid
  that really covers `[-1,1]`. I verified `s=1/3, z=4` covers the range with no clipping and max
  error `s/2=1/6` at `x=0.5`.

## F-029 — verdict: UPHELD → FROZEN (concur)
- reasoning: The iter-3 repair (which SOL56 raised against my iter-3 audit — I had missed it)
  correctly replaces the "imitation can only reproduce answers it was shown" overclaim with the
  precise distinction: masked token-likelihood *can* generalize beyond verbatim demonstrations;
  what SFT does not directly supply is a comparative "A preferred to B" label. Confirmed the old
  overclaim string is gone and the comparison-label framing is present and consistent across the
  five sibling cells (93, 96, 105–106, 121). No contradiction with the Chapter-6 held-out
  generalization result. Freeze.

## F-030 — verdict: UPHELD → FROZEN (concur)
- reasoning: Both constrained solvers (cells 16, 107) now check `res.success`, raise on failure,
  narrowly suppress only SLSQP's benign bound-clipping warning, and assert `np.allclose(...,
  atol=1e-5)` against the closed form. Confirmed `res.success` guards present; fresh execution is
  clean but for the deliberate ε=0 LayerNorm warning. Freeze.

## Findings SOL56 missed — none
Honest, and stated with some humility: SOL56's audit is accurate and complete. I re-checked the
sibling surface for the F-015 bug — the min/max `quantize()` helper (per-channel demo and
perplexity-vs-bits) has no integer zero-point and maps `min→0`, `max→qmax` exactly, so it always
covers `[min,max]` with no clipping; the defect is confined to the affine-with-zero-point worked
example SOL56 already scoped. Per axis: MATH — only F-015; CODE — none (47/47 execute); CLAIM —
none (SFT/preference distinction now correct at all siblings); FIDEL — F-015 is the external-truth
correction, no separate drop; PED — none beyond F-015; NOTE — none.

## Retraction of my iter-3 signoff
I retract `signoff/SIGNOFF_OPUS48.md` (it affirmed product_i3, which carries the F-015 defect).
My iter-3 audit confirmed F-015 as FROZEN without catching the clipping — a real miss. This is
exactly the cross-check the loop exists for; I will re-sign only a version whose quantizer
calibration is correct.

## LEDGER
- F-015 → ACCEPTED (re-opened, upheld; blocking MAJOR).
- F-029, F-030 → FROZEN (concur).
- SIGNOFF_OPUS48.md removed (stale).

## For the rework turn (mine, iter 4)
One fix: correct the affine-quantizer worked example per the plan above. Then re-execute and
re-audit; if clean, re-sign.
