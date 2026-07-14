# Rework OPUS48 i0 — product_i0 → product_i1

Materialized `product/product_i1.ipynb` (118 cells; +15 over i0). All 40+ code cells
re-executed top-to-bottom in one fresh kernel: **0 exceptions, every assertion passed**
(nbclient). The root cause of the five BLOCKERs was mine — I had corrected each overclaim in
one cell but left sibling cells (headers, plot titles, prints, transitions) still teaching it,
so i0 contradicted itself. i1 propagates every correction to all siblings.

## Decision table (every non-REJECTED finding)

| id | decision | where (product_i1) | one-line rationale |
|----|----------|--------------------|--------------------|
| F-001 | (FROZEN) | — | Substrate call already frozen; no action. |
| F-002 | FIX | cell 39 | Rewrote the "order enters only via position signal" cell to unmasked-only equivariance + causal-mask caveat, consistent with cell 41. |
| F-003 | FIX | cells 34, 37, 38 | Rewrote "escaping…job of the MLP" to single-head-projected-values; scoped the hull-demo title/prints to the W_V=I setup; header "how the block escapes it". |
| F-004 | FIX | cells 45, 47 | Retitled "Depth kills gradients — unless…" to "helps, but guarantees nothing"; scoped the demo plot title/print to the near-identity construction. |
| F-005 | FIX | cell 50 | Rewrote the closing transition so LayerNorm is credited with standardizing sublayer-input statistics, not bounding activation scale across depth. |
| F-006 | FIX | cells 74–75 | Held-out section now backed by a run that actually demonstrates the lesson (see F-008). |
| F-007 | FIX | cells 30, 88, 111 | cell 30 "differentiable random parameterization" (not "generalizes"); cell 88 print "direct loss term is 0 / supervised targets are response tokens"; cell 111 table "growing exact cache vs fixed compressed state". |
| F-008 | FIX | cell 75 | New held-out demo: small train (40) + large val (600) from a fixed true bigram; val NLL 1.367 → **min 1.158 @ step 88** → 1.194, asserted (dip-then-rise). |
| F-009 | FIX | cell 13 | "non-smooth maps have no usable derivative" → smoothness is convenient; ReLU trains via subgradients. |
| F-010 | FIX | cell 64 | Restored explicit label shifting (WE 3.2) at the start of Ch6; the "shifted labels" references now resolve. |
| F-011 | FIX | cells 60–61 | Added a bounded **end-to-end training** of the assembled transformer (finite-difference GD on tied W_E): loss 1.4396 → 1.1393, asserted. Qualified the "trained" close. |
| F-012 | FIX (as MINOR) | cells 22, 87 | Added portable self-checks at Ch1 and Ch6 (not all 16; 99c's break→repair pedagogy is deliberate per §3). |
| F-013 | FIX | cell 90 | Table now names `GPT2Block` as the decoder-only match and flags that `nn.TransformerDecoderLayer` adds encoder cross-attention; "one-to-one" → "close counterpart / conceptual analogues". |
| F-014 | FIX | cells 24–25 | Restored A's cross-entropy = entropy + KL decomposition and the population conditional-entropy floor (Thm 1.9), with a numpy check. |
| F-015 | FIX | cells 97–98 | Restored A's affine quantizer (scale, zero-point), the half-step bound \|x−x̂\|≤s/2 with clipping caveat (WE 10.1): max err 0.1429 = s/2, asserted. |
| F-016 | FIX (as MINOR) | cell 112 | Restored a 4-question paper-reading rubric + one line each on retrieval/external-memory and world-model/JEPA directions. |
| F-017 | FIX | cells 89, 90 | "byte-for-byte" → "numerically equal to fp tolerance"; code uses `np.allclose` + a note that no framework `F.cross_entropy` is called (numpy-only env). |
| F-018 | FIX (as MINOR) | cell 116 | Restored a portable NLP task-family map (tagging/parsing/IE/coref/discourse/speech/agents) + the "fluent generation ≠ every behavior" warning. |
| F-019 | FIX | cells 54, 70 | Restored WE 5.1 (LayerNorm C=2 catastrophe, reinforcing F-005) and the precise AdamW update statement; WE 1.2 gradient-sums-to-zero is covered by the existing CE-gradient cell + new KL self-check. |

## Representative concrete edits

### F-002 — cell 39
- before: "Order enters only when we add a per-position signal to each token vector"
- after: "unmasked attention (with positionwise maps) is permutation-equivariant … the causal mask is itself position-dependent and already breaks full permutation-equivariance … position embeddings are not strictly necessary for order — they are a stronger, direct signal."

### F-004 — cells 45 / 47
- before: title "Depth kills gradients — unless you add the identity back"; print "the residual path preserves what the plain path annihilates"
- after: title "Depth and gradients: the residual path helps, but guarantees nothing"; print "in THIS small-Jacobian construction, residual preserves what the plain path annihilates"

### F-008 — cell 75
- before: narrative asserted "validation loss falls with training loss" while the run's val NLL rose monotonically from step 0.
- after: `train_small = sample_pairs(40,1); val_large = sample_pairs(600,2)` from a fixed true bigram; asserts `0 < argmin(val) < end`, `val[min] < val[0]`, `val[-1] > val[min]`. Output: `start 1.367 → min 1.158 @ 88 → end 1.194`.

### F-011 — cell 60
- before: assembled model only run at random init (`loss 1.4396`, one forward pass).
- after: 20 bounded finite-difference GD steps on the tied `W_E` (signal flows through every block): `1.4396 → 1.1393`, `assert losses[-1] < losses[0] - 1e-3`.

## New material introduced this rework (flagged for the iter-1 audit)
Per turn_rework, new claims are fair game next round. Newly added/executed cells to audit:
KL-decomposition text+check (24–25), Ch1/Ch6 self-checks (22, 87), label-shift WE (63–64),
LayerNorm-C=2 WE (54), end-to-end training (60–61), AdamW statement (70), quantizer
half-step-bound text+code (97–98), reading rubric (112), NLP map (116). All execute clean;
the finite-difference training is a bounded teaching demo (not backprop) and is labeled as such.

## LEDGER
- F-002 … F-019 → RESOLVED (each FIXed; the next audit should confirm → FROZEN or re-OPEN).
- F-001 stays FROZEN. No REJECT-WITH-RATIONALE this round (no ACCEPTED finding overruled),
  so nothing new is CONTESTED.
