# Audit SOL56 i0

**Verdict: REVISE.** Product i0 executes top-to-bottom, but five BLOCKER contradictions remain and the merge is not faithful to both co-equal sources.

## Verification performed

- Read `CONTRACT.md`, `LEDGER.md`, both source notebooks, `premerge/99c_advisory_SOL56.md`, and `product/product_i0.ipynb`.
- Executed all 40 code cells in notebook order in one fresh shared namespace: 0 exceptions; 11 assertions passed.
- Recomputed the held-out curve in cells 63–64: train NLL `1.3098 -> 0.7014`; validation NLL `1.3884 -> 2.6523`; validation minimum `1.3884` occurs at step 0.
- Compared all seven prior `RESOLVED` rows against the merged product and checked unique material from both sources.

## Prior-resolution disposition

| Finding | Audit disposition | Basis |
|---|---|---|
| F-001 | confirm; propose **FROZEN** | The numpy substrate runs without the unavailable PyTorch/repo package dependency. |
| F-002 | **re-OPEN** | Cell 36 retains the false positions-only order claim. |
| F-003 | **re-OPEN** | Cells 34, 41, and 43 retain the MLP-only hull-escape story. |
| F-004 | **re-OPEN** | Cells 45–46 still teach residuals as the reason gradients survive. |
| F-005 | **re-OPEN** | Cell 47 still assigns depth-wise activation-scale control to layer norm. |
| F-006 | **re-OPEN** | The held-out-validation port is present but its run contradicts its lesson. |
| F-007 | **re-OPEN** | Several listed B-side overclaims remain in earlier cells/output. |

## BLOCKER findings

### F-002 · MATH · BLOCKER
- loc: cell 36 — "Order enters only when we add a per-position signal"
- wrong: This says position embeddings are the only source of order, although the causal mask is itself position-dependent and breaks full permutation equivariance. Cell 38's later correction does not erase the earlier lesson.
- correct: Unmasked self-attention without position signals is permutation-equivariant. A causal mask already introduces order; explicit position encodings add a direct position signal and are not the only possible source.
- evidence: Product cell 38 states and demonstrates the mask caveat, directly contradicting cell 36; this was the substance of F-002.

### F-003 · MATH · BLOCKER
- loc: cell 34 — "escaping it is later the job of the MLP"
- wrong: Cells 34, 41, and 43 teach that attention is trapped in the original input hull and only the MLP escapes it. The convex-hull statement applies to one head relative to that head's projected value vectors, not to the full attention sublayer relative to its input vectors.
- correct: A head convex-combines its projected values. Value/output projections, multiple heads, biases, and residual addition can already move the full sublayer output outside the original input hull; the MLP's distinct role is nonlinear positionwise channel mixing.
- evidence: Product cell 44 contains this correction, but the upstream prose, plot title, labels, and printed interpretation remain unqualified; this was the substance of F-003.

### F-004 · MATH · BLOCKER
- loc: cell 45 — "Depth kills gradients — unless you add the identity back"
- wrong: The title, direct-path prose, cell 46 plot title, and printed conclusion still imply that adding residual identity prevents vanishing gradients. The expansion of a Jacobian product does not provide a noncancellable identity route.
- correct: Residual parameterizations often improve gradient propagation in suitable initialization, normalization, and scaling regimes, but products of `I + J_f` can vanish, explode, or become ill-conditioned.
- evidence: Product cell 47 gives the counterexamples `J_f=-I` (zero) and `J_f=I` (`2^L`), contradicting the lesson still taught in cells 45–46; this was the substance of F-004.

### F-005 · MATH · BLOCKER
- loc: cell 47 — "That is the job of the last ingredient"
- wrong: The antecedent is keeping activation scale in check as depth grows, so the transition assigns that job to layer norm. The next cell correctly says layer norm does not prevent residual-stream magnitude from growing or collapsing across depth.
- correct: Pre-layer normalization stabilizes the statistics presented to each sublayer. It does not by itself bound the residual stream across depth.
- evidence: Product cell 48 explicitly states the correct limitation, leaving a direct contradiction with cell 47; this was the substance of F-005.

### F-008 · CODE · BLOCKER
- loc: cell 63 — "Early on, validation loss falls with training loss"
- wrong: The deterministic code in cell 64 never exhibits the claimed early validation improvement; validation is worst after every update relative to step 0. The chart title and final print then treat this run as evidence of generalization.
- correct: Either choose a data split/model/seed whose held-out NLL demonstrably falls before rising, with an assertion for that behavior, or describe this run honestly as immediate held-out degradation with no demonstrated generalization.
- evidence: Fresh execution gives train `1.3098 -> 0.7014`, validation `1.3884 -> 2.6523`, and `argmin(validation)=0`; the first ten validation values rise monotonically from `1.3884` to `1.5146`.

## MAJOR findings

### F-006 · FIDEL · MAJOR
- loc: cell 63 — "Generalization is a held-out claim"
- wrong: F-006 claimed the A-only held-out-validation content was ported. The section exists, but the actual result fails the stated generalization-then-overfitting lesson, so this part of the bundled resolution does not hold.
- correct: Preserve a valid held-out demonstration from source A or replace the narrative with the actual result and its limited inference. The other named F-006 ports are present.
- evidence: F-008 supplies the runtime failure. Source A cell 63 requires training/validation curves to diagnose overfitting rather than merely labeling any held-out number as generalization.

### F-007 · CLAIM · MAJOR
- loc: cell 27 — "It runs, it is differentiable, it generalizes"
- wrong: The model at this point is random and untrained; nearby embeddings do not establish held-out performance. Other members of the bundled resolution also remain in executable-facing text: cell 77 prints that 100% of gradient flows to the response, and cell 98 still labels the recurrent tradeoff "lossless recall."
- correct: Call the cell a differentiable random parameterization; reserve generalization for held-out evaluation. Say prompt loss terms are zero while response gradients can flow through prompt representations, and describe recurrent state as compressed rather than contrasting it with guaranteed lossless recall.
- evidence: Product cells 62, 78, and 96 contain the correct qualifications but contradict cells 27, 77, and 98 respectively; these were explicitly included in F-007.

### F-009 · CLAIM · MAJOR
- loc: cell 13 — "non-smooth maps have no usable derivative"
- wrong: Non-smoothness does not imply unusable gradient-based optimization. ReLU is the standard counterexample: differentiable away from zero, with a chosen subgradient/convention at the kink.
- correct: Smoothness is convenient for ordinary derivative analysis; training can also use functions differentiable almost everywhere with subgradients or defined automatic-differentiation conventions.
- evidence: The claimed implication is mathematically false and is not required to motivate softmax; positivity, normalization, and convenient differentiability are sufficient.

### F-010 · NOTE · MAJOR
- loc: cell 53 — "exactly the shifted labels of Chapter 3"
- wrong: Chapter 3 never defines label shifting, its shapes, or the no-future-target contract. The first actual shift appears inline in cell 54, so the backward reference is undefined at the point it is used.
- correct: Restore the explicit map from a length-`T+1` token window to `x=ids[:-1]`, `y=ids[1:]`, including `(B,T)` shapes and the causal target interpretation, or retarget the reference.
- evidence: Source A cells 37, 39, and 40 define and execute the shift; product Chapter 3 (cells 25–29) covers embeddings/order only.

### F-011 · FIDEL · MAJOR
- loc: cell 93 — "The core model is complete, trained"
- wrong: The assembled transformer in cells 53–54 is only run at random initialization. Chapter 6 trains bigram models, not the assembled multi-layer transformer, so the merged notebook never trains the model it calls trained.
- correct: Add a bounded end-to-end training experiment for the assembled transformer with parameter updates and an asserted loss decrease, or qualify the claim to say that the forward model is assembled while only simpler predictors were trained.
- evidence: Product cell 54 creates static parameters and performs one forward pass; source A cell 58 trains `TinyGPT` on a tiny batch and asserts `last_loss < first_loss`.

### F-012 · PED · MAJOR
- loc: cell 102 — "A merged union of two sources"
- wrong: The derivations-first source's retrieval practice was removed wholesale: the product contains no `Self-check` section, despite 16 source-A cells containing self-checks. Runnable assertions are useful but do not replace learner-facing derivation and interpretation questions.
- correct: Restore bounded self-checks at the relevant chapters, adapting only questions that depend on the unavailable repository package.
- evidence: Text search finds zero self-check cells in the product versus source A cells 3, 13, 16, 18, 24, 32, 37, 42, 43, 51, 57, 63, 70, 79, 87, and 93.

### F-013 · CLAIM · MAJOR
- loc: cell 79 — "has a one-to-one counterpart in PyTorch and Hugging Face"
- wrong: The table maps the decoder-only pre-norm block to `nn.TransformerDecoderLayer` as if it were one-to-one. That PyTorch layer includes self-attention, encoder cross-attention (`memory`), and feed-forward components; it is not the same decoder-only GPT block.
- correct: Describe the mappings as conceptual analogues, keep `GPT2Block` as the closer decoder-only match, and distinguish encoder-only, decoder-only, and encoder-decoder families.
- evidence: PyTorch's official `TransformerDecoderLayer` documentation requires encoder `memory` and describes self-attention plus multi-head attention and feed-forward components: https://docs.pytorch.org/docs/main/generated/torch.nn.modules.transformer.TransformerDecoderLayer.html. Source A cell 76 supplies the omitted family distinction.

### F-014 · FIDEL · MAJOR
- loc: cell 21 — "Every backpropagation step in every language model"
- wrong: The merge preserves the token-level gradient but drops source A's distributional identity `H(q,p)=H(q)+KL(q||p)` and the population conditional-entropy floor. That is unique, correct mathematical content from a co-equal source.
- correct: Restore the KL decomposition, its conditioning argument, and the conclusion that population NLL equals irreducible conditional entropy plus model mismatch.
- evidence: Source A cell 18 contains Theorem 1.9 and proof; no product cell contains the conditional-KL decomposition or entropy-floor result.

### F-015 · FIDEL · MAJOR
- loc: cell 84 — "the vertical gap ... is the error injected"
- wrong: The quantization chapter keeps the picture but drops source A's affine quantizer, zero-point, representable interval, and proved half-step error bound, including the clipping exception.
- correct: Restore `Q_{s,z}`, `D_{s,z}`, `|x-x_hat| <= s/2` when unclipped, and the statement that clipping error is not bounded by `s/2`.
- evidence: Source A cell 79 defines and proves these claims; product cells 83–87 contain no zero-point or half-step bound.

### F-016 · FIDEL · MAJOR
- loc: cell 96 — "the three main families of alternative"
- wrong: The merged horizon drops source A's retrieval/external-memory and JEPA/world-model directions, then omits the 12-question paper-reading checklist and smallest-falsifying-experiment discipline.
- correct: Restore those directions with their distinct bottlenecks/risks and the source-A checklist or an equivalent measurable-experiment rubric.
- evidence: Source A cells 93 and 95 contain the missing material; product cells 95–99 cover sparse attention, GQA/MQA, and linear/SSM only.

### F-018 · FIDEL · MAJOR
- loc: cell 102 — "All fourteen chapters (0–13) are present"
- wrong: Product Chapter 13 omits source A's broader-NLP boundary map: structured prediction, parsing, information extraction, semantic roles, coreference, discourse, speech, and agent loops. Counting a differently scoped closing chapter does not preserve that correct unique content.
- correct: Restore a concise, portable version of the NLP task-family map and its warning that fluent next-token generation is not evidence for every language behavior.
- evidence: Source A cell 98 contains the map and source boundary; no corresponding content appears in product Chapter 13.

## MINOR findings

### F-017 · CODE · MINOR
- loc: cell 79 — "byte-for-byte the loss you already wrote"
- wrong: Cell 80 checks `np.isclose` between two NumPy implementations and prints rounded values. That establishes numerical agreement within tolerance, not byte identity, and it does not invoke `F.cross_entropy` despite the surrounding library claim.
- correct: Say the formulas are numerically equivalent within tolerance, assert `np.allclose`, and separately compare against the actual framework function only if that dependency is available.
- evidence: Cell 80 uses `np.isclose`; floating-point evaluation/reduction order can change low bits while preserving mathematical equivalence.

## Axis coverage

- MATH: F-002–F-005.
- CODE: F-008, F-017.
- CLAIM: F-007, F-009, F-013.
- FIDEL: F-006, F-011, F-014–F-016, F-018.
- PED: F-012.
- NOTE: F-010.

No signoff is warranted while BLOCKER findings remain open.
