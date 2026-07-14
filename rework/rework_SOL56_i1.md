# Rework SOL56 i1 — product_i1 → product_i2

Materialized `product/product_i2.ipynb` with 119 cells (46 code). The notebook was executed with `nbclient` before the atomic save, then independently re-executed in a fresh shared namespace: **46/46 code cells, 0 exceptions**. The one runtime warning is the deliberate `epsilon=0` constant-vector LayerNorm demonstration, whose output explicitly labels the result undefined.

## Decision table

| id | decision | where in product_i2 | one-line rationale |
|----|----------|---------------------|--------------------|
| F-001 | NO CHANGE (FROZEN) | — | Numpy substrate remains executable. |
| F-002 | NO CHANGE (FROZEN) | cells 42–44 | Causal-mask caveat remains consistent. |
| F-003 | NO CHANGE (FROZEN) | cells 40, 48–50 | Single-head hull claim remains correctly scoped. |
| F-004 | NO CHANGE (FROZEN) | cells 51–53 | Residual demo remains construction-specific. |
| F-005 | NO CHANGE (FROZEN) | cells 53–54 | LayerNorm does not claim to bound residual depth. |
| F-006 | NO CHANGE (FROZEN) | cells 75–76 | Held-out curve still demonstrates dip then rise. |
| F-007 | NO CHANGE (FROZEN) | cells 31, 89, 112 | Prior sibling overclaims remain removed. |
| F-008 | NO CHANGE (FROZEN) | cell 76 | Assertions still bind the validation lesson to output. |
| F-009 | NO CHANGE (FROZEN) | cell 13 | ReLU/subgradient qualification remains. |
| F-010 | FIX | cells 34–35, 61 | Label shifting now lives in Chapter 3 before first use. |
| F-011 | FIX | cells 63–64, 107 | Central claim now states partial parameter optimization, not full-model training. |
| F-012 | NO CHANGE (FROZEN) | cells 25, 69 | Portable self-checks remain. |
| F-013 | FIX | cell 91 | Restored encoder-only / decoder-only / encoder-decoder boundary. |
| F-014 | FIX | cells 23–24 | Entropy-floor conclusion now states the deterministic-zero condition. |
| F-015 | FIX | cells 95, 97–98 | Correct zero-point calibration/clipping and representable-interval condition. |
| F-016 | FIX | cell 113 | Retrieval and JEPA/world models now target distinct bottlenecks. |
| F-017 | NO CHANGE (FROZEN) | cells 91–92 | Floating-tolerance wording remains honest. |
| F-018 | NO CHANGE (FROZEN) | cell 117 | Broader-NLP map remains present. |
| F-019 | FIX | cell 21 | Added exact-digit numpy Worked Examples 1.1/1.2. |
| F-020 | FIX | cells 63–64, 77, 107 | Removed all claims that one-group optimization trained the full transformer. |
| F-021 | FIX | cells 23–24, 34–35, 97–98 | Definitions now precede dependent demonstrations and use. |
| F-022 | FIX | cells 95–96 | Affine min/max range is distinguished from symmetric max-absolute scaling. |
| F-023 | FIX | cell 36 | Added the missing Chapter 4 heading. |
| F-024 | FIX | cell 113 | Restored a compact modern-system map with component-specific failures/metrics. |

## Concrete edits

### F-010 — cells 34–35
- before: label shifting was defined in Chapter 6 after cells 61–63 used it, while cell 61 pointed to Chapter 3.
- after: Chapter 3 now defines `x=(x_1,…,x_T)`, `y=(x_2,…,x_{T+1})`, `(B,T,V)`/`(B,T)` shapes, and executes the `"cat a"` example before Chapter 4.

### F-011 — cells 63–64, 107
- before: the closing called the assembled transformer "trained" although only `W_E` changed.
- after: the notebook claims exactly one tied parameter group was optimized through the full forward computation; full-model training is explicitly identified as updating every group by backpropagation.

### F-013 — cell 91
- before: corrected `GPT2Block` mapping, but no transformer-family boundary.
- after: added a three-row encoder-only / decoder-only / encoder-decoder table with attention contracts, objectives, and non-drop-in warning.

### F-014 — cells 23–24
- before: "the achievable minimum loss is not zero" and perplexity 1 was called unattainable without conditions.
- after: the minimum equals expected conditional entropy, may be zero for deterministic conditionals or a memorized finite corpus, and is positive only under positive conditional entropy.

### F-015 — cells 95, 97–98
- before: raw `round(-x_min/s)` was said always to make zero representable.
- after: unsigned calibration first includes zero in the calibrated range, clips the integer zero-point, states `D(z)=0`, and limits the half-step guarantee to non-clipped inputs. The earlier min/max helper is labeled a fake grid that does not force an integer zero-point.

### F-016 — cell 113
- before: retrieval was described as not growing context and JEPA/world-model objectives were grouped with quadratic-attention fixes.
- after: retrieval is described as external evidence inserted into (and consuming) context; JEPA/world models target latent prediction, sample efficiency, planning, and representation quality and may still use quadratic attention.

### F-019 — cell 21
- before: only a qualitative self-check asked why `p-e_y` sums to zero.
- after: a numpy cell verifies `p=(0.6439,0.0871,0.0321,0.2369)`, loss `1.4402`, gradient `(0.6439,0.0871,0.0321,-0.7631)`, and exact zero gradient sum.

### F-020 — cells 63–64, 77, 107
- before: "actually trained end to end," "The model is trained," and "trained end to end by gradient descent."
- after: the code prints which parameters remain fixed, Chapter 7 explicitly uses the trained bigram, and the close distinguishes assembled-transformer partial optimization from bigram training.

### F-021 — cells 23–24, 34–35, 97–98
- before: KL, label-shift, and affine-quantizer code appeared before their mathematical prerequisites.
- after: each definition/derivation immediately precedes its worked cell; label shifting also precedes the first model loss that consumes it.

### F-022 — cells 95–96
- before: affine per-tensor scale was said to be set by the largest-magnitude entry.
- after: affine/asymmetric scaling uses the tensor-wide min/max range; symmetric scaling commonly uses max absolute magnitude; both expose shared grids to outliers.

### F-023 — cell 36
- before: Chapter 3 jumped directly to unheaded attention content and then `## 5`.
- after: `## 4 · Attention: one position reads another` establishes the missing chapter boundary.

### F-024 — cell 113
- before: modern practice was reduced to an inaccurate retrieval parenthetical and later names.
- after: a compact systems table distinguishes prompting, sparse retrieval, dense retrieval, tool use, persistent memory, and serving; it includes RAG data flow, failure localization, claim-matched evaluation, continuous batching, and paged KV storage.

## Verification evidence

- Structural RED→GREEN suite: 12/12 checks now pass (claim removals, definition order, family map, zero-point rule, exact worked example, Chapter 4, and system map).
- Fresh execution: `code_cells=46`, `errors=0`, one deliberate LayerNorm warning.
- Partial optimization: `1.4396 -> 1.1393`.
- Held-out validation: `1.3671 -> 1.1577 @ step 88 -> 1.1935`.
- Exact CE example: `1.4402`, gradient sum `0.0`.
- Quantizer example: zero-point `4`, maximum error `0.1429 = s/2`.

## New/expanded claims for the next audit

Audit the new transformer-family table and modern-system map in cells 91 and 113, plus the extended-zero calibration conditions in cell 97. These are source-backed repairs but are new product wording.
