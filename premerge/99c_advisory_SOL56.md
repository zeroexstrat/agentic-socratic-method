# 99c pre-merge advisory — SOL56

## BLOCKER

### B1 — CLAIM / MATH / PED: causal attention is not permutation-equivariant

- loc: cell 33 — "bare stack of attention layers still cannot represent word order"
- wrong: The preceding experiment removes the causal mask, proves equivariance only for unmasked attention, then generalizes that result to the causal decoder used by the course. A causal mask is not invariant under arbitrary position permutations; it is itself an asymmetric source of order and position information. Explicit positional encodings are useful, but they are not the only possible source of order in a causal transformer.
- correct: State the theorem only for unmasked attention and positionwise maps. For causal attention, say that the mask breaks full permutation equivariance; explicit positional encodings provide a stronger, direct position signal but are not mathematically necessary for all causal language modeling.
- evidence: Under a permutation matrix $P$, unmasked attention obeys $A(PX)=P A(X)$ because its score matrix is conjugated by $P$. The causal mask generally obeys $PMP^T\ne M$, so the proof fails. Causal LMs without explicit positional encodings empirically learn position information (Haviv et al., 2022, [arXiv:2203.16634](https://arxiv.org/abs/2203.16634)). This error is also present in 99 cell 42's concluding gloss; external ground truth overrides both sources.

### B2 — MATH / CLAIM / PED: the convex-hull demo omits most of an attention sublayer

- loc: cell 39 — "only sublayer that computes genuinely new coordinates"
- wrong: The demo fixes $W_V=I$, omits multi-head concatenation, omits $W_O$, and omits the residual addition. It proves only that $WV$ is a convex combination of the chosen value vectors. It does not prove that a real attention sublayer is confined to the input hull or that only the MLP can compute new coordinates. Learned value/output projections can move outside the input hull, and attention weights are nonlinear functions of the input.
- correct: A single head output $o_t=\sum_s w_{t,s}v_s$ lies in the convex hull of that head's projected values $v_s=X_sW_V$. The full attention update includes multiple projected heads, an output projection, and a residual connection; the MLP supplies additional positionwise nonlinear channel mixing, not the sole source of new coordinates.
- evidence: Take one input point $x=(1,0)$ and a learned value projection $W_V=2I$: its value $(2,0)$ is already outside the input hull $\{(1,0)\}$. More generally $W_O\operatorname{concat}_h(\sum_s w^h_{t,s}X_sW_V^h)$ need not lie in the hull of the input rows. 99 cell 51 correctly retains the missing multi-head and output-projection structure, although 99 cells 42/51 share part of the overstrong hull gloss.

### B3 — MATH / CLAIM / PED: residual connections do not guarantee an $O(1)$ gradient

- loc: cell 42 — "the residual gradient stays $O(1)$"
- wrong: One random small-Jacobian experiment is presented as a general law. Although each factor is $I+J_f$, the product can vanish, explode, or be ill-conditioned; the additive identity term in the formal expansion does not prevent cancellation by the other terms.
- correct: Residual paths often improve gradient propagation by making layers near-identity under suitable initialization, normalization, and residual scaling. They do not by themselves guarantee stable gradients or make arbitrary hundred-layer networks trainable.
- evidence: A one-layer counterexample is $J_f=-I$, for which $I+J_f=0$ and the gradient vanishes exactly. With $J_f=I$, $L$ identical residual factors give $\|\prod_l(I+J_f)\|=2^L$, which explodes. The plotted matrices in cell 41 were deliberately scaled to $0.06/\sqrt d$, so the observed $O(1)$ norm is a property of that construction, not residual algebra in general. This overclaim is inherited from 99 cell 51; external math overrides it.

### B4 — MATH / CLAIM / PED: LayerNorm neither maps every input to one sphere nor bounds depth

- loc: cell 43 — "activations cannot blow up or collapse with depth"
- wrong: The sphere statement silently sets $\epsilon=0$, excludes constant vectors, and stops before learned $\gamma,\beta$. Actual LayerNorm uses $\sqrt{\operatorname{Var}(u)+\epsilon}$; its normalized norm is generally below $\sqrt C$, and the affine parameters remove the fixed-sphere/compact-set claim. In a pre-norm transformer, LayerNorm bounds what each sublayer reads at a given parameter setting, not the residual-stream magnitude across depth.
- correct: For the normalization core with $\epsilon=0$ and nonconstant $u$, mean is zero and norm is $\sqrt C$. With $\epsilon>0$, $\|N_\epsilon(u)\|^2=C\,\operatorname{Var}(u)/(\operatorname{Var}(u)+\epsilon)$. Learned $\gamma,\beta$ then apply an affine transform. Say LayerNorm stabilizes sublayer input statistics; do not claim it prevents activation growth or collapse.
- evidence: For a constant vector, cell 44's `u.std()` is zero and its normalization yields NaNs. With standard $\epsilon>0$, that vector maps to zero before affine parameters, not to the radius-$\sqrt C$ sphere. This overclaim is inherited from 99 cell 51; 99 itself states the necessary $\epsilon=0$ and nonconstant-input conditions before later overgeneralizing.

### B5 — CLAIM / PED: untrained uncertainty is mislabeled as generalization

- loc: cell 55 — "That is the answer to Chapter 0's break"
- wrong: Near-uniform output from near-zero random logits is ignorance, not learned transfer to an unseen event. The plot contains no held-out metric and shows $p(t\mid c)$ falling monotonically during training; it cannot establish that "generalization is early" or identify overfitting. The claim that this rank-2 factorized model's unregularized MLE is generally the count table is also unjustified.
- correct: Nonzero softmax support avoids infinite loss, but generalization must be demonstrated after learning by improved held-out loss or another held-out task metric. Overfitting is a divergence between training and validation behavior, not merely convergence toward an empirical conditional. A low-rank factorization reaches the count-table conditional only when that conditional is representable by the factorization and optimization reaches the relevant optimum.
- evidence: At initialization, $E_i\cdot U_j\approx0$ for every pair, so every unseen and nonsensical pair receives similar probability; no structure has transferred. 99 cells 57 and 59 correctly define generalization using held-out validation loss and warn that optimization success alone proves no transfer.

## MAJOR

### M1 — CLAIM / PED: softmax is not the unique differentiable relaxation of lookup

- loc: cell 35 — "unique differentiable relaxation of hard lookup"
- wrong: Softmax is unique for the specifically stated Shannon-entropy-regularized maximization problem, not among differentiable relaxations of argmax or lookup. The broader claim is false.
- correct: Say softmax is the unique optimizer of $\langle w,a\rangle+\tau H(w)$ for $\tau>0$. Other smooth or differentiable relaxations/selection mechanisms exist; uniqueness does not extend beyond that objective.
- evidence: The Lagrangian in cell 14 proves uniqueness only because Shannon entropy makes that objective strictly concave. Changing the regularizer changes the optimizer; smooth approximations such as sigmoid-normalized gates and Gumbel-softmax are immediate counterexamples to global uniqueness.

### M2 — CLAIM / FIDEL / PED: the counting failure is stated as an impossibility theorem

- loc: cell 6 — "A model built by counting can only ever assign probability"
- wrong: This is true of the unsmoothed maximum-likelihood table implemented in cell 3, not of count-based language models in general. Smoothing, interpolation, and backoff assign mass to unseen n-grams; they do more than merely leave all count models at exact zero.
- correct: Attribute the zero/infinite loss to the unsmoothed MLE n-gram estimator. Explain that smoothing/backoff repairs support and shares evidence across shorter contexts, while dense parameter sharing can support richer similarity-based generalization.
- evidence: 99 cell 9 explicitly computes add-one smoothing: an unseen bigram changes from $0$ to $1/7$ while the row remains normalized. The redesign may argue that this is weaker than learned representations, but it may not claim counting fails to assign unseen mass "in principle."

### M3 — FIDEL / PED / NOTE: the promised $\sqrt D$ derivation and implementation shapes are dropped

- loc: cell 27 — "The $\sqrt D$ is a temperature (we will see why"
- wrong: 99c never supplies the promised variance derivation and presents only unbatched single-head shapes. It drops the conditions under which $\operatorname{Var}(q\cdot k)=D$, the reason for dividing by $\sqrt D$, the softmax axis, and the production shapes `(B,H,T,T)`.
- correct: Restore the derivation under zero-mean, unit-variance, independent-coordinate initialization assumptions; label those assumptions as an initialization model, not a trained-network theorem. Carry the implementation through `(B,T,C) -> (B,H,T,D)`, scores `(B,H,T,T)`, row softmax on the source-position axis, and output `(B,T,C)`.
- evidence: 99 cells 10, 42, 43, and 51 contain the missing axis/shape contract and the variance derivation: independent unit-variance products have variance 1, their $D$-term sum has variance $D$, and division by $\sqrt D$ restores variance 1.

### M4 — FIDEL / PED / CLAIM: 99c claims a complete machine without building one

- loc: cell 47 — "We now hold the complete machine"
- wrong: The executable path never assembles trainable multi-head causal attention, its output projection, two distinct LayerNorms with affine parameters, an end-to-end block stack, a final normalization/head, or a forward pass from token IDs to `(B,T,V)` logits. The chapter demos components, but the claimed complete raw-tensor model is absent.
- correct: Preserve 99c's component-level break/repair demos, then import or reconstruct 99's end-to-end typed model path and execute at least one forward shape/loss check. Label a conceptual schematic as such until that exists.
- evidence: 99 cells 51, 52, and 55 specify and execute the missing multi-head/block/model contracts, including QKV `(B,T,3C)`, heads `(B,H,T,D)`, scores `(B,H,T,T)`, output projection, weight tying, and logits `(B,T,V)`.

### M5 — CLAIM / PED: the greedy-loop explanation only applies to the bigram state

- loc: cell 59 — "large models decoded greedily degrade into loops"
- wrong: The toy decoder's state is only the previous character, so revisiting that state forces the same transition. A transformer decoder's effective state is the whole retained prefix/KV state; repeating a token or substring does not mean the same state has been revisited. Greedy decoding can be repetitive, but not for the exact finite-state argument asserted here.
- correct: Say the demo proves deterministic cycles for this bigram transition system. For large autoregressive models, greedy decoding often reduces diversity and may repeat, but repetition depends on the learned conditional distribution and context window; sampling mitigates but does not guarantee absence of loops.
- evidence: In cell 58, `generate` computes `p` from `Wg[prev]` only, so the state space has four elements. A transformer conditions on $x_{1:t}$ (or its bounded retained context), which changes after each appended token even if the last token repeats.

### M6 — CLAIM / CODE / PED: the KV-cache plot mislabels partial work as total decode complexity

- loc: cell 65 — "That $O(T)$-vs-$O(T^2)$ gap is why the KV cache"
- wrong: Cell 64 counts only key/value projections. Caching makes prior K/V projections reusable and prevents recomputation of prior hidden states, but each new query still attends over a cache whose length grows with $t$. Dense attention work across $T$ generated tokens remains $\sum_{t=1}^T O(t)=O(T^2)$ at fixed width.
- correct: Label the plotted metric "K/V projection computations." State that the cache changes naive full-prefix recomputation and projection costs, while standard dense decode still performs linear-in-current-context attention per token and quadratic total attention work over a generated sequence.
- evidence: Cell 64's own y-axis is `key/value computations`; it does not count query-key dot products or weighted value reads. At decode step $t$, both operations touch $t$ cached positions.

### M7 — CLAIM / PED: response masking does not stop prompt-side learning

- loc: cell 69 — "the model never learns to *produce* them"
- wrong: Setting prompt-token loss weights to zero removes direct target terms at those positions, but response losses backpropagate through prompt embeddings and prompt K/V representations because responses condition on them. Shared parameters can also change probabilities of prompt-like tokens at other positions.
- correct: Say prompt positions have zero *direct loss terms*. All supervised targets are response tokens, while gradients from those targets still flow through the prompt-conditioned computation graph.
- evidence: If a response logit depends on attention over a prompt value $v_s=X_sW_V$, then $\partial L_{\text{response}}/\partial X_s$ is generally nonzero even when the prompt position's own mask entry is zero. 99 cells 72–74 correctly define masking as selection of supervised target terms and do not require severing the prompt graph.

### M8 — CLAIM / FIDEL / PED: a toy fake-quantization curve is generalized to real LLM inference

- loc: cell 79 — "perplexity is essentially flat from 8 bits down to about 4"
- wrong: The curve is training-corpus perplexity for a four-by-four bigram matrix under one per-row min/max fake quantizer. It cannot establish that 4-bit LLM inference is generally near-lossless, that degradation begins below four bits, or that the same weight-precision knob automatically quantizes KV activations.
- correct: Restrict the conclusion to this toy. For real systems, state bit width, weight/activation/cache tensors, quantizer type, grouping, calibration, outlier handling, kernel/hardware path, and held-out evaluation. Treat KV-cache quantization as a separate scheme even when its storage ratio is arithmetically half/quarter of fp16.
- evidence: Cell 78 evaluates only `quantize(Wg, ...)` on the training `corpus`; the cache numbers are a separate byte-count loop with no cache quantizer or accuracy test. 99 cells 79 and 85 explicitly warn that quantization quality depends on distributions, calibration, tensor selection, and hardware, and that underspecified comparisons are invalid.

### M9 — FIDEL / MATH / PED: DPO's preference model and actual loss disappear

- loc: cell 84 — "is the algebra that inverts the boxed equation"
- wrong: Inverting the Gibbs optimum alone does not produce a trainable preference objective. The missing step is a preference likelihood model (Bradley–Terry in the standard derivation), substitution of reward differences, cancellation of the prompt-dependent partition term, and binary cross-entropy on policy log-ratio differences.
- correct: State the modeling assumption and show at least the DPO logit
  $$
  \beta\left[\log\frac{\pi_\theta(y^+\mid x)}{\pi_{\rm ref}(y^+\mid x)}-\log\frac{\pi_\theta(y^-\mid x)}{\pi_{\rm ref}(y^-\mid x)}\right]
  $$
  inside $-\log\sigma(\cdot)$. Clarify that DPO fits an implicit reward under that preference model; it is not an assumption-free shortcut to the boxed optimum.
- evidence: 99 cell 87 retains the Bradley–Terry assumption, partition cancellation, and complete loss. The DPO paper likewise describes a change of variables under a theoretical preference model and a binary classification objective (Rafailov et al., 2023, [arXiv:2305.18290](https://arxiv.org/abs/2305.18290)).

### M10 — CLAIM / FIDEL / PED: the final "only scale" claim contradicts the course

- loc: cell 92 — "Everything separating this toy from a frontier model"
- wrong: Frontier models differ not only in scale but also in tokenizer/data construction, architecture details, objectives, optimization, post-training, retrieval/tool systems, evaluation, serving, and safety/reliability constraints. The notebook itself introduced several of these differences, so the closing statement is internally inconsistent.
- correct: Say the toy preserves selected core mathematical contracts, while real model quality and behavior also depend on data, objectives, architecture, training/serving systems, post-training, and evaluation.
- evidence: 99 cells 87, 88, 92, and 97 explicitly preserve these stage boundaries and warn that formulas plus scale are insufficient. This correct source content should survive the merge.

## MINOR

### m1 — CLAIM / PED: character tokenization does not inherently eliminate OOV

- loc: cell 21 — "never hit an unknown symbol"
- wrong: A character tokenizer trained on a finite character inventory can encounter an unseen character. Only an alphabet known to cover the deployment domain, a byte-level fallback, or an explicit unknown-token policy prevents failure.
- correct: Qualify the claim to this four-character toy vocabulary, or say byte-level tokenization can guarantee coverage of arbitrary byte strings.
- evidence: `stoi` contains only `' '`, `'a'`, `'c'`, and `'t'`; encoding `'b'` with it raises a missing-key error. 99 cells 28–31 preserve the tokenizer-domain and unknown-symbol caveats that 99c drops.

### m2 — CODE / CLAIM: the displayed high-$\beta$ result is not indistinguishable

- loc: cell 84 — "At high $\beta$ the aligned policy is indistinguishable"
- wrong: The only displayed "high" value is $\beta=4$, whose first probability is $0.309$ versus reference $0.350$ and whose fourth is $0.183$ versus $0.150$. Those are visible changes, not numerical indistinguishability.
- correct: Say $\pi^*\to\pi_{\rm ref}$ as $\beta\to\infty$; at $\beta=4$ this example is merely closer to the reference than the lower-$\beta$ cases.
- evidence: Cell 83 prints `[0.309, 0.270, 0.195, 0.183, 0.043]` against `[0.350, 0.250, 0.200, 0.150, 0.050]`.

### m3 — MATH / NOTE: the causal-mask row count is off by one

- loc: cell 91 — "Row t spreads over exactly t positions"
- wrong: The cell's math and NumPy indices are 0-based, so row $t$ permits columns $s\le t$ and therefore contains $t+1$ allowed positions.
- correct: Print "row `t` spreads over exactly `t+1` positions" for 0-based code, or relabel prose positions 1 through $T$ consistently.
- evidence: The displayed rows contain 1, 2, 3, 4, and 5 nonzero entries for indices 0, 1, 2, 3, and 4.

### m4 — CLAIM / PED: code cells are top-to-bottom runnable, not self-contained

- loc: cell 93 — "building the naive answer in self-contained code"
- wrong: Many cells depend on prior state (`softmax`, `stoi`, `corpus`, `pairs`, `Wg`, `Ts`, `gibbs_closed_form`). They run top-to-bottom but do not run independently.
- correct: Replace "self-contained" with "top-to-bottom runnable in one shared notebook state," or add local definitions/imports to each claimed standalone exploration.
- evidence: Cell 78 requires `stoi`, `corpus`, `softmax`, `quantize`, and `Wg` from earlier chapters; executing it alone raises `NameError`.

### m5 — CLAIM / PED: full-attention recall is not lossless by theorem

- loc: cell 87 — "losslessly recall arbitrary past tokens the way full attention can"
- wrong: A standard KV cache retains one projected key/value pair per cached position, but softmax attention plus finite-dimensional projections does not guarantee lossless arbitrary-token recall. The valid contrast is growing exact cache state versus a fixed-size compressed recurrent state.
- correct: Say full attention retains all cached K/V vectors and lets each new query address them directly, whereas a fixed-size recurrent state must compress history and may discard task-relevant information.
- evidence: $W_K$ or $W_V$ may be rank-deficient, so different token states can map to identical cached vectors; even with full-rank projections, the attention output is a weighted mixture rather than a lossless readout guarantee.
