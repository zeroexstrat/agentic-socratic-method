# Meta-audit SOL56 i1 — adjudicating audit_OPUS48_i1

**Overall: audit incomplete; product i1 still needs rework.** Fresh shared-kernel execution confirms all 45 code cells run with no exceptions and the two headline curves reproduce (`1.4396 -> 1.1393` training; validation `1.3671 -> 1.1577 @ 88 -> 1.1935`). Runtime success does not validate the notebook's interpretation. OPUS48 correctly caught F-020, but understated its severity and prematurely froze six incomplete resolutions. The pedagogical placement of several restored derivations also reverses prerequisite and demonstration.

## Adjudication of OPUS48's finding

### F-020 — verdict: RECLASSIFIED(MINOR→MAJOR)
- reasoning: The finding is correct and resolvable at cell 60. Only `trained["W_E"]` is perturbed and updated; every attention, MLP, positional-embedding, and LayerNorm parameter remains fixed at random initialization. Yet cells 60–61 call the assembled transformer "actually trained end to end," cell 76 says "The model is trained," and cell 106 says it was "trained end to end by gradient descent." This is not a one-qualifier imprecision: it materially changes what the central training demonstration establishes. Correct is to say that one tied parameter group is optimized through the full forward computation, or to optimize all parameter groups. Under CONTRACT §4, that is MAJOR.

## Prior-resolution dispositions OPUS48 missed

### F-010 — disposition: re-OPEN (NOTE · MINOR)
- reasoning: Cell 58 still says "exactly the shifted labels of Chapter 3," but Chapter 3 ends at cell 32. The definition is in cell 64, after cells 59–60 have already used `xb`, `yb`, and their loss. The reference therefore remains false; defining the concept later in Chapter 6 does not resolve a Chapter 3 reference.

### F-013 — disposition: re-OPEN (CLAIM · MAJOR)
- reasoning: Cell 90 now correctly distinguishes `GPT2Block` from `nn.TransformerDecoderLayer`, but F-013's required correction also called for the encoder-only / decoder-only / encoder-decoder family distinction. Product i1 contains neither `encoder-only` nor `encoder-decoder`; source A cell 76's materially useful family map remains absent. The mapping fix is partial, not FROZEN.

### F-014 — disposition: re-OPEN (FIDEL · MAJOR)
- reasoning: The restored identity is correct, but cell 24 concludes "the achievable minimum loss is **not zero**" and "a perplexity of 1 is unattainable for real text" without the needed positive-conditional-entropy assumption. The immediately preceding cell correctly shows a deterministic one-hot target has entropy floor 0. Correct: the population minimum equals expected conditional entropy; it is strictly positive only when that conditional entropy is positive. The audit's claim that the restored math is fully correct does not hold.

### F-015 — disposition: re-OPEN (FIDEL · MAJOR)
- reasoning: Cell 97 says `z=round(-x_min/s)` "makes real 0 exactly representable" for an observed range, but omits clipping the zero-point into `[q_min,q_max]` and overgeneralizes unsigned bounds to all `b`-bit quantizers. Counterexample: for range `[1,2]` at 8 bits, the stated formula gives `s=1/255`, `z=-255`, `Q(0)=0`, and `D(Q(0))=1`, not 0. Source A cell 79 explicitly clips `z`; the restoration is mathematically incomplete.

### F-016 — disposition: re-OPEN and RECLASSIFIED(MINOR→MAJOR) (FIDEL)
- reasoning: Cell 112 does not merely compress the source; it changes its claims. "don't grow the context — fetch relevant text and condition on it" ignores that ordinary RAG inserts retrieved text into and consumes the model context. "Both attack the same wall — finite context and quadratic attention" incorrectly groups JEPA/world-model objectives with retrieval: source A cell 93 identifies their targets as predictive representation, sample efficiency, planning, and abstraction, and they may still use quadratic-attention backbones. A fidelity repair that introduces false bottleneck reasoning is MAJOR.

### F-019 — disposition: re-OPEN (FIDEL · MINOR)
- reasoning: The accepted scope required at minimum source A's Worked Examples 5.1 and 1.2. Product i1 adds the C=2 LayerNorm example and AdamW statement, but cell 22 only asks why `p-e_y` sums to zero; it does not restore Worked Example 1.2's exact logits/probabilities/loss/gradient calculation. The audit silently narrows the previously agreed resolution.

## Findings OPUS48 missed

### F-021 · PED · MAJOR (missed by OPUS48)
- loc: cell 23 — "H(q,p) = H(q) + KL(q||p), verified on a random target"
- wrong: The new rigor cells systematically demonstrate concepts before defining them. Cell 23 executes the KL decomposition before cell 24 introduces it; cell 63 executes label shifting after cells 59–60 already use it and before cell 64 explains it; cell 96 uses affine quantization, zero-point, and the half-step lemma before cell 97 defines them. This is not an aesthetic ordering preference: learners encounter undefined prerequisites and code whose reasoning arrives only afterward.
- correct: Put each mathematical definition/derivation before its worked code, and introduce label shifting before the first end-to-end loss that consumes shifted targets.
- evidence: Source A orders theory before code in cells 18, 37–40, and 79; product i1 reverses that dependency at all three restoration sites.

### F-022 · CLAIM · MAJOR (missed by OPUS48)
- loc: cell 95 — "set by its largest-magnitude entry"
- wrong: The notebook's quantizer is affine/asymmetric and uses the tensor-wide minimum and maximum, so its scale is set by the full range `max-min`, not by the largest absolute entry. The largest-magnitude rule describes a common symmetric quantizer, not the code being taught.
- correct: Say affine per-tensor quantization uses one global min/max range; symmetric per-tensor quantization commonly uses the global maximum absolute value. In either case, an outlier can widen the shared range and coarsen resolution for typical values.
- evidence: Product cell 94 computes `scale=(hi-lo)/qmax`; source A cell 79 explicitly distinguishes asymmetric range calibration from symmetric max-absolute calibration.

### F-023 · NOTE · MINOR (missed by OPUS48)
- loc: cell 44 — "## 5 · The block: new features, and surviving depth"
- wrong: Product i1 has Chapter 3 and then attention content in cells 33–43, but no `## 4` heading. Cell 44 nevertheless says "Chapter 4 ended," and the closing claims all fourteen chapters are present. This breaks the notebook's own chapter-number references and navigation.
- correct: Add the Chapter 4 heading before the attention introduction in cell 33, preserving the existing attention content beneath it.
- evidence: A complete header scan returns chapters 0, 1, 2, 3, 5, …, 13; only chapter 4 is absent.

### F-024 · FIDEL · MAJOR (missed by OPUS48)
- loc: cell 112 — "retrieval / external memory"
- wrong: The claim that no correct A-only content remains dropped overlooks source A's modern-system boundary: prompting/in-context learning, retrieval versus tool use versus persistent memory, sparse versus dense retrieval and RAG failure decomposition, evaluation-to-claim matching, and prefill/decode scheduling and batching. Product i1 reduces retrieval to one inaccurate parenthetical and merely names agentic loops later.
- correct: Restore a compact but substantive system map that distinguishes these components, shows where context/weights/state change, and retains the main retrieval and serving failure modes. It need not reproduce source A's prose verbatim.
- evidence: Source A cells 87, 89, and 90 contain the correct unique material; product i1 has no `sparse retrieval`, `dense retrieval`, `continuous batching`, `paged` cache, or retrieval/tool/memory distinction.

## Stable dispositions

I independently confirm the product_i1 fixes for F-002–F-009, F-012, F-017, and F-018. F-011 remains RESOLVED but cannot freeze until F-020 is corrected. No signoff is warranted: accepted/open MAJOR findings remain.
