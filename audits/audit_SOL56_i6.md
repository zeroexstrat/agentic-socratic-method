# Audit SOL56 i6 — auditing product_i6

**Verdict: SIGN-OFF WITH ONE EXPLICIT MINOR WAIVER.** F-033 and F-032 are correctly repaired;
product i6 executes 47/47 code cells with zero exceptions and only the deliberate cell-55
`epsilon=0` warning. F-031's piecewise constraints are correct, but the sentence immediately
after them reverses a feasibility implication for asymmetric two-sided ranges. I re-open F-031
at MINOR and sign only at CONTRACT's BLOCKER/MAJOR bar with the required waiver.

## Re-audit of iter-5 repairs

### F-033 — confirm -> FROZEN

- Cell 10 now maps the finite-logit softmax model into the relative interior of the simplex and
  states the bijection only between strictly positive joints and strictly positive conditional
  families. It correctly explains that a joint with zeros leaves conditionals on zero-mass
  prefixes arbitrary.
- The paragraph also separates two claims that were previously conflated: the chain rule makes
  a full conditional family sufficient to specify the joint, while shared parameters merely
  make transfer across prefixes possible and do not guarantee generalization.
- Counterexample check: a point mass on `00` no longer contradicts the text; its unreachable
  `X1=1` branch is explicitly covered by the caveat. Freeze.

### F-032 — confirm -> FROZEN

- Parsed cell 116 now contains four literal `\to` commands and no tab control characters. A
  notebook-wide source scan finds no non-newline control character. Freeze.

### F-031 — re-OPEN (MATH / MINOR)

- **loc:** cell 100 — “For a nondegenerate two-sided range”
- **wrong:** The new piecewise `c_-`/`c_+` definition correctly handles boundary zero-points,
  but the next sentence claims that every nondegenerate two-sided range has
  `qmin < z < qmax`. A highly asymmetric range can round the naive zero-point to a boundary;
  the piecewise rule then correctly reports that fixed-`z` two-sided coverage is impossible.
  The sentence contradicts that case by presenting interior `z` as automatic rather than as a
  feasibility condition.
- **correct:** Say: “If finite coverage of a nondegenerate two-sided range is feasible with
  fixed `z`, then `qmin < z < qmax`, and the constraints reduce to ...”. If rounded `z` is at a
  boundary, move it inward and recompute `s`, or report that coverage with that fixed `z` is
  impossible.
- **evidence:** On an unsigned 3-bit grid with `[a,b']=[-0.001,1]`, naive
  `s=(1.001)/7=0.143` and `z=round(-a/s)=round(0.00699)=0=qmin`, despite the range being
  nondegenerate and two-sided. The repaired piecewise definition gives `c_-=+infinity`, exactly
  showing the fixed boundary `z` cannot cover the negative side. MINOR is appropriate: the
  formula, `[-1,1]` example, and all code are correct; one implication qualifier fixes the
  explanatory sentence.

## Coverage by rubric axis

- **MATH:** F-031 above. F-033's positivity theorem, F-015's quantizer example, entropy/KL,
  attention scaling, tying budget, optimizer checks, and DPO derivation all check out.
- **CODE:** none new. Fresh-kernel execution completed 47/47 with no exceptions; all assertions
  pass and only the intentionally elicited LayerNorm warning remains.
- **CLAIM:** none. The generalization, partial-training, decoding, cache, alignment, and
  quantization claims are scoped correctly.
- **FIDEL:** none. Cell 10 restores source A's load-bearing positivity condition; cell 100
  correctly retains the external-truth departure from the source-A quantizer error.
- **PED:** no separate finding. The joint/conditional and quantizer break->repair explanations
  now expose their assumptions; F-031 is the one remaining implication slip.
- **NOTE:** none. F-032 is repaired and all symbols/shapes in the changed cells are consistent.

## LEDGER disposition

- F-033 -> propose **FROZEN**.
- F-032 -> propose **FROZEN**.
- F-031 -> **OPEN** again at MINOR.

`signoff/SIGNOFF_SOL56.md` is emitted for product i6 with an explicit F-031 waiver. It cannot
converge with OPUS48's current product-i5 sign-off; the harness and next steward turn decide the
remaining one-line repair and version alignment.
