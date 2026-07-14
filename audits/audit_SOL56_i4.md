# Audit SOL56 i4 — auditing product_i4

**Verdict: REVISE (one MAJOR).** The iter-3 repairs F-029 and F-030 landed correctly and
should be FROZEN. Product i4 executes 47/47 code cells with zero exceptions and only the
deliberate cell-55 `epsilon=0` LayerNorm warning. A fresh mathematical pass nevertheless found
new evidence that reopens F-015: integer zero-point rounding shifts the actual affine grid, so
the claimed observed-range coverage is false and the worked example applies its no-clipping
lemma to a value that does clip.

## Re-audit of iter-3 repairs

### F-029 — confirm -> FROZEN

- Cells 93, 96, 105–106, and 121 consistently state the correct distinction: token-likelihood
  training can generalize beyond verbatim demonstrations; ordinary SFT examples do not directly
  supply an `A preferred to B` label. The preference objective is now motivated by a distinct
  supervision type, not by a replay-only model premise.
- The repair matches source A's “which distribution to imitate / easier to compare than
  demonstrate” progression and removes the contradiction with Chapter 6's held-out
  generalization demonstration.

### F-030 — confirm -> FROZEN

- Cells 16 and 107 now check `res.success`, raise on optimizer failure, and assert numerical
  agreement with their closed forms at `atol=1e-5`. The observed maximum differences are at
  most `2.10e-07` (cell 16) and `1.26e-07` (cell 107).
- The warning filter is narrowly scoped to SLSQP's harmless out-of-bounds trial-step message.
  Fresh execution contains neither SLSQP warning; the deliberately elicited cell-55 warning
  remains visible and labeled.

## Finding

### F-015 · MATH · MAJOR (re-OPENED on new evidence)

- **loc:** cell 100 — “To cover an observed range while representing real zero”
- **wrong:** Setting `s=(b'-a)/(qmax-qmin)` and then rounding the zero-point does not generally
  make the dequantization grid cover `[a,b']`. Rounding `z` shifts the representable interval.
  Cell 101 then labels every sample “in range” and cites the no-clipping half-step lemma, even
  though its endpoint `x=1` clips. The fact that this clipped endpoint happens to have error
  exactly `s/2` does not verify a lemma whose premise excludes clipping.
- **correct:** After integer zero-point rounding, compute the actual interval
  `[s(qmin-z), s(qmax-z)]` and identify values whose pre-clipped code falls outside
  `[qmin,qmax]`. Either (a) describe endpoint clipping honestly and verify the half-step lemma
  only on the non-clipped subset, or (b) enlarge/recompute `s` after choosing integer `z` so the
  grid really covers the calibration range. For a range spanning zero, coverage requires
  `s >= max(-a/(z-qmin), b'/(qmax-z))` when both denominators are nonzero.
- **evidence:** In the notebook's exact 3-bit example,
  `s=2/7`, `z=round(3.5)=4`, so the actual grid interval is
  `[s(0-4), s(7-4)]=[-8/7,6/7]`, not `[-1,1]`. For `x=1`,
  `x/s+z=7.5`, NumPy round-to-even produces `8`, and `clip(8,0,7)=7`; clipping is real.
  Cell 101's assertion checks only the resulting error, not the lemma's no-clipping premise.
  Source A cells 79 and 81 contain the same mistaken coverage statement/application, so external
  mathematical truth controls under CONTRACT §1. This is MAJOR because a displayed self-check
  gives the right numerical bound for the wrong stated reason and teaches a false calibration
  guarantee; the affine-quantizer definition and conditional lemma themselves remain correct.

## Coverage by rubric axis

- **MATH:** F-015 above. I recomputed the new solver checks, the entropy/KL identities,
  attention scaling, tying budget, and quantizer grid; the quantizer calibration/example is the
  only new mathematical defect found.
- **CODE:** none new. A fresh kernel executed 47/47 cells with no exceptions; F-030 now fails
  closed, all assertions pass, and only the intentional LayerNorm warning remains. Cell 101's
  assertions execute but fail to test a mathematical premise, which is captured in F-015.
- **CLAIM:** none new. The repaired SFT/preference distinction is accurate at all five siblings,
  and the decoding, KV-cache, partial-training, and systems claims remain bounded.
- **FIDEL:** no separate new finding. Both sources were checked; source A shares F-015's
  quantizer error, so retaining it is not fidelity to external truth. Previously adjudicated
  source-union scope remains unchanged in i4.
- **PED:** no separate finding beyond F-015. Definitions still precede use, but the quantizer
  self-check is pedagogically misleading for the mathematical reason recorded there.
- **NOTE:** none found. Symbols and shapes in the changed cells are consistent; the five
  preference passages use the same comparison-label terminology.

## LEDGER disposition

- F-029 -> propose **FROZEN**.
- F-030 -> propose **FROZEN**.
- F-015 -> **OPEN** again on new evidence; no new finding ID is created because this is a defect
  in the previously frozen affine-quantizer repair itself.

No SOL56 signoff is emitted: an OPEN MAJOR remains.
