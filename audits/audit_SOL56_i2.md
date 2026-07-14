# Audit SOL56 i2

**Verdict: REVISE.** Product i2 executes cleanly and the twelve iter-1 repairs landed, but one target-boundary statement remains mathematically wrong, one training claim is still over-universal, and source A's weight-tying/parameter-count and beam-search material remains absent.

## Verification performed

- Read `CONTRACT.md`, current `LEDGER.md`, product i2, and both source notebooks.
- Executed all 46 code cells in a fresh shared namespace: 0 exceptions; all assertions passed. The sole warning is the explicitly demonstrated undefined `epsilon=0` constant-vector normalization.
- Rechecked the iter-1 structural repairs: 12/12 targeted checks pass; markdown contains no generated control characters.
- Reproduced key outputs: tied-embedding optimization `1.4396 -> 1.1393`; validation `1.3671 -> 1.1577 @ 88 -> 1.1935`; exact CE `1.4402`, gradient sum `0.0`.

## Prior-resolution disposition

F-010, F-011, F-013, F-014, F-015, F-016, F-019, F-020, F-021, F-022, F-023, and F-024 are correctly resolved in product i2; propose **FROZEN**. F-025 below is a distinct boundary error inside the moved label-shift example, not a reopening of F-010's location/order defect.

## MAJOR findings

### F-025 · MATH · MAJOR
- loc: cell 35 — "which already sits at position t+1 in the same input tensor"
- wrong: The print states this for every target `y_t=x_{t+1}`. For `t<T`, the target token is indeed at the next input position and the causal mask prevents leakage. For the final position `t=T`, `y_T=x_{T+1}` was removed when forming `x=ids[:-1]`; it is not anywhere in the input tensor.
- correct: State the two cases explicitly: for `t<T`, the target appears at future input position `t+1` and is masked; the final target lies outside `x` entirely.
- evidence: Cell 35 constructs `x=[2,1,3,0]` and `y=[1,3,0,1]`; `y[3]=1` is the fifth raw token, while the input has only four positions. Source A cells 37–40 define the same shift without claiming the final target remains in `x`.

### F-026 · CLAIM · MAJOR
- loc: cell 22 — "Every backpropagation step in every language model"
- wrong: `p-e_y` is the logit gradient for one-hot softmax cross-entropy. It is not the starting gradient for every language-model objective: label smoothing changes the target distribution, preference objectives combine policy log-probabilities, and representation/diffusion objectives need not use this token-level loss at all.
- correct: Scope the sentence to next-token models trained with one-hot softmax cross-entropy; more generally, distributional cross-entropy gives `p-q`.
- evidence: The derivation in cells 19–22 assumes `ell(z,y)=-log softmax(z)_y` and `e_y`. The notebook's own DPO section later uses a different objective over policy log-ratios.

### F-027 · FIDEL · MAJOR
- loc: cell 61 — "a tied unembedding W_U=W_E^\top"
- wrong: The product uses weight tying but drops source A's unique explanation of what tying means and the associated parameter-count/scaling map. A learner sees the implementation choice without learning that logits are embedding-space inner products, that input/output geometry is coupled, or that tying removes `V*C` independent parameters.
- correct: Restore a compact parameter-group shape table and derive `z_i=<h,E(i)>` under `W_U=W_E^T`, including the parameter-saving/coupled-geometry interpretation.
- evidence: Source A cell 55 contains the parameter groups, precise tying derivation, and width/depth/context/vocabulary scaling consequences; no product_i2 cell contains `z_i=<h,E(i)>`, a parameter-count map, or the `V*C` saving.

## MINOR findings

### F-028 · FIDEL · MINOR
- loc: cell 80 — "The repair: three ways to reshape the simplex"
- wrong: The generation chapter preserves temperature, top-k, and top-p but drops source A's correct beam-search distinction. The library table later names beam without explaining that it is sequence-level search, not a next-token distribution reshaping.
- correct: Add a compact beam-search paragraph: keep the top `K` partial sequences by accumulated log probability, and distinguish that search procedure from top-k/top-p sampling.
- evidence: Source A cell 63 defines beam scoring `log p(y_1:i|x)=log p(y_<i|x)+log p(y_i|x,y_<i)` and explicitly contrasts beam with truncation; product cell 91 only lists `beam` as a library feature.

## Axis coverage

- MATH: F-025.
- CODE: none found; fresh execution completed 46/46 cells, assertions passed, and the only warning is deliberate and labeled.
- CLAIM: F-026.
- FIDEL: F-027 and F-028 after comparing both sources section-by-section around the touched chapters.
- PED: none found beyond the issues above; definitions now precede the restored demonstrations, Chapter 4 navigation is present, and the break→repair sequence remains coherent.
- NOTE: none found; chapter numbering, shifted-label references, symbols, and shape names are now internally resolvable.

No signoff is emitted because three new MAJOR findings remain open.
