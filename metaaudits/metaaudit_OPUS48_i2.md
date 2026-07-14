# Meta-audit OPUS48 i2 — adjudicating audit_SOL56_i2

**Overall:** SOL56's iter-2 audit is accurate. I re-executed product_i2, verified all four new
findings against the cited cells, checked for siblings, and scrutinized SOL56's *own* iter-1
rework additions (family table cell 91, quantizer calibration cells 97–98, entropy-floor cells
23–24) since an auditor is least critical of its own work. All four are upheld; I found no
false positive to overturn, and — after section-by-section comparison against both sources — no
additional BLOCKER/MAJOR that SOL56 missed. I do sharpen F-026 (it is an internal
contradiction, not merely an over-universal claim).

Verification: re-ran all 46 code cells in a fresh kernel (0 exceptions, assertions pass);
confirmed all 14 chapter headings present (F-023 held); confirmed the attention-row
max-entropy verification (Gibbs 2nd scale) survives at cell 45; grep-confirmed the tying
explanation is genuinely absent (no `z_i=<h,E(i)>`, no param-count) — F-027 is real.

## Disposition of SOL56's prior-resolution proposals
Concur with FROZEN for F-010, F-011, F-013, F-014, F-015, F-016, F-019, F-020, F-021, F-022,
F-023, F-024 — I spot-checked the load-bearing ones: F-014 entropy-floor (cells 23–24) states
the deterministic-zero condition correctly; F-013 family table (cell 91) is accurate; F-015/
F-022 quantizer calibration (cells 97–98) correctly extends the range to include zero and clips
the integer zero-point; F-023 restored the "## 4 · Attention" heading.

## SOL56's new findings

### F-025 — verdict: UPHELD → ACCEPTED (MATH / MAJOR)
- reasoning: Correct. Cell 35's print asserts, for *every* target, that `y_t = x_{t+1}` "already
  sits at position t+1 in the same input tensor." True for `t<T` (masked), but false for the
  final example: `y_{T-1}=ids[T]` was dropped when forming `x=ids[:-1]` and is not in the input
  at all. The cell's own data shows it (`x=[2,1,3,0]`, `y=[1,3,0,1]`; the last target `1` is not
  at any "future" position). MAJOR is right — a universal claim true only under an unstated
  condition, in the very cell teaching the leakage/masking point. Fix: state the two cases.

### F-026 — verdict: UPHELD → ACCEPTED (CLAIM / MAJOR); sharpened
- reasoning: Correct, and stronger than filed. "Every backpropagation step in every language
  model … begins with this vector [p−e_y]" (cell 22) is not merely over-universal — it is
  **internally contradicted by the notebook's own DPO section** (cell 107), whose gradient is a
  logistic function of policy log-ratios, not p−e_y. So this is the same class of self-contradiction
  the loop caught at iter 0, now across chapters. Fix: scope to next-token models trained with
  one-hot softmax cross-entropy, and note the distributional generalization p−q (the machinery
  for which the notebook already has in the KL cell 23).

### F-027 — verdict: UPHELD → ACCEPTED (FIDEL / MAJOR)
- reasoning: Correct. Weight tying is used (cell 61, `W_U=W_E^T`) with no explanation; grep
  confirms the product contains neither `z_i=<h,E(i)>` nor a parameter-count/scaling map. This
  is A-unique correct content (source A cell 55), and it is real mathematics — the output head
  is a log-linear model in the embedding geometry, which is also the Chapter-1/11 Gibbs thread
  at the head scale. Consistent with upholding F-014/F-015 (dropped A-rigor) at MAJOR. Fix:
  restore a compact parameter-group table and the tying derivation.

### F-028 — verdict: UPHELD → ACCEPTED (FIDEL / MINOR)
- reasoning: Correct. The generation chapter defines temperature/top-k/top-p but not beam
  search; the library table (cell 91) then names "beam" undefined. Source A cell 63 has the
  beam scoring and the search-vs-sampling distinction. MINOR enrichment. Fix: a compact beam
  paragraph distinguishing sequence-level search from next-token reshaping.

## Findings SOL56 missed
None additional at BLOCKER/MAJOR. This is a deliberate, checked conclusion rather than a
rubber-stamp — I did not manufacture a marginal finding that would likely be overturned. Per
axis:
- **MATH:** F-025 is the only one; I re-derived the entropy-floor, √D-variance, half-step-bound,
  and attention max-entropy cells against their outputs — all correct.
- **CODE:** none. 46/46 cells execute; the sole warning is the deliberate ε=0 constant-vector
  LayerNorm demonstration, which is labeled.
- **CLAIM:** F-026 (sharpened above); no other over-universal claim survives (the p−e_y site is
  cell 22 only; greedy/temperature, KV-cache O(T²), and DPO claims are correctly scoped).
- **FIDEL:** F-027 and F-028 capture the remaining dropped A-content around the touched
  chapters; the previously-flagged drops (KL/entropy floor, quantizer bound, WE 1.1/1.2/5.1,
  label shift, family map, AdamW statement) are present at the agreed scope.
- **PED:** none new — definitions now precede demonstrations (F-021), the break→repair flow is
  intact, and the restored worked examples/self-checks reinforce it.
- **NOTE:** none new — chapter numbering, shifted-label references, and shape/symbol names are
  internally consistent.

## LEDGER
- F-025, F-026, F-027, F-028 → ACCEPTED (all UPHELD).
- No REJECTED (no false positives), no CONTESTED, no new OPEN from me.

## For the rework turn (mine, iter 2)
Five small edits: state the two label-shift cases (F-025), scope the p−e_y claim + add the
distributional p−q note and reconcile with the DPO cell (F-026), restore the tying derivation +
parameter-group table (F-027), add a beam-search paragraph (F-028). These are all bounded; the
notebook is converging — the remaining items are precision qualifiers and two dropped-A
restorations, no contradictions in the current product beyond F-025/F-026's cross-cell scope.
