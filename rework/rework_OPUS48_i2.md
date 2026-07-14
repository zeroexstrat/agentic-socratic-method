# Rework OPUS48 i2 — product_i2 → product_i3

Materialized `product/product_i3.ipynb` (122 cells; +3 over i2). Re-executed all code cells in
a fresh kernel: **0 exceptions, all assertions pass**. Four small fixes, no contradictions
introduced. The notebook is converging: these are precision qualifiers plus two dropped-A
restorations.

## Decision table (every ACCEPTED finding)

| id | decision | where (product_i3) | one-line rationale |
|----|----------|--------------------|--------------------|
| F-025 | FIX | cell 35 | Label-shift print now states two cases: for interior `t<T-1` the target sits at future input position `t+1` (masked); the final target `ids[T]` was dropped by `x=ids[:-1]` and is not in the input at all. |
| F-026 | FIX | cell 22 | Scoped "every backprop step begins with p−e_y" to next-token one-hot softmax CE; added the distributional generalization `p−q` and the explicit note that the DPO loss (Ch 11) differentiates a logistic of policy log-ratios, not p−e_y — removing the cell-22-vs-cell-107 contradiction. |
| F-027 | FIX | cells 65–66 (new) | Restored the weight-tying derivation `z_i=⟨h,E(i)⟩` (output head = log-linear model in embedding geometry, the head-scale Gibbs) and a parameter-group budget table showing tying saves `V·C` params. |
| F-028 | FIX | cell 83 (new) | Added a beam-search paragraph: keep top-K partial sequences by accumulated log-prob; distinguished sequence-level *search* from top-k/top-p distribution *reshaping*. |

## Concrete edits

### F-025 — cell 35
- before: `print("... y_t = x_{t+1}, which already sits at position t+1 in the same input tensor.")`
- after: two-case print — interior `t<T-1`: target at future input position `t+1` (masked); final `t=T-1`: `y[3]=ids[4]=1` dropped by `x=ids[:-1]`, not in the input.

### F-026 — cell 22
- before: "Every backpropagation step in every language model … begins with this vector [p−e_y]."
- after: "For a next-token model trained with one-hot softmax cross-entropy … begins with exactly this vector … against a soft target `q` the logit gradient generalizes to `p−q`; and objectives that are not one-hot token CE start elsewhere — the DPO loss … differentiates a logistic function of policy log-ratios, not `p−e_y`."

### F-027 — cells 65–66 (inserted after the end-to-end model/training)
- added markdown: `z_i=⟨h,W_E[i]⟩=⟨h,E(i)⟩`, the head as a Gibbs distribution over embedding inner products (the Ch1/Ch11 thread at the head scale), tying saves `V·C` params and couples input/output geometry.
- added code: parameter budget by group (token embed / position / all blocks / final LN), total, and the `V·C` saving printed. Output confirms the saving and the log-linear reading.

### F-028 — cell 83 (inserted after "Three knobs, one simplex")
- added a compact beam paragraph with the scoring recursion `log p(y_{1:i}|x)=log p(y_{<i}|x)+log p(y_i|x,y_{<i})`, the escape-from-greedy motivation, the K× cost, and the sharp search-vs-sampling distinction (also explaining why the library `generate` lists `beam` beside the sampling knobs).

## New material for the iter-3 audit
Two new executed/authored cells to audit: the weight-tying parameter-budget cell (66, code +
its markdown 65) and the beam-search paragraph (83). Both are source-A-backed; the param-count
numbers are computed from the assembled `gpt` model, not asserted.

## LEDGER
- F-025, F-026, F-027, F-028 → RESOLVED (next audit confirms → FROZEN or re-OPEN).
- No REJECT-WITH-RATIONALE; nothing CONTESTED.
