# LEDGER — append-only finding register

**This file is the single source of truth for state.** The notebooks and audit
markdowns are the *reasoning*; this table is the *record*. Both models append here;
neither deletes or rewrites prior rows. To change a finding's state, append the
change in the STATE LOG at the bottom — never edit a row in place.

## Conventions

- `id`: `F-{NNN}` assigned in order first raised. Never reused.
- `raised_by`: `OPUS48` | `SOL56` | `HUMAN`.
- `iter`: iteration the finding was first raised in.
- `axis`: MATH | CODE | CLAIM | FIDEL | PED | NOTE (from CONTRACT §3).
- `sev`: BLOCKER | MAJOR | MINOR | NIT.
- `status`: OPEN | ACCEPTED | REJECTED | CONTESTED | RESOLVED | FROZEN.
  - `OPEN` raised, not yet adjudicated.
  - `ACCEPTED` meta-audit upheld it; awaiting rework.
  - `REJECTED` meta-audit overturned it (false positive / out of scope / no location).
  - `CONTESTED` the two models disagree; escalates to HUMAN after 2 rounds.
  - `RESOLVED` fixed in a rework; verified in the next audit.
  - `FROZEN` RESOLVED and confirmed stable; may not be reopened without NEW evidence.
- `loc`: `cell {index}` + anchor.
- `note`: what's wrong + what correct looks like / resolution rationale.

## Findings

| id | raised_by | iter | axis | sev | status | loc | note |
|----|-----------|------|------|-----|--------|-----|------|
| F-000 | HUMAN | 0 | — | — | RESOLVED | — | Example row. Delete once F-001 exists. Demonstrates the format. |
| F-001 | OPUS48 | 0 | FIDEL | MAJOR | RESOLVED | cell 0 — "How this notebook was made" | Substrate conflict: A(99)=PyTorch+`llm_from_scratch` library; B(99c)=self-contained numpy. Resolved to numpy — A's substrate cannot execute in the loop env (no torch/lib; human-confirmed) and CONTRACT §2(b) requires executable cells. A's rigor ported as numpy throughout. |
| F-002 | OPUS48 | 0 | MATH | BLOCKER | RESOLVED | cell 38 — "Unmasked attention ... permutation-equivariant" | Both sources overclaimed (B cell 33 / A cell 42 gloss) that a causal stack cannot represent order. External truth: equivariance holds for UNMASKED attention only; the causal mask breaks it and can itself encode position (Haviv 2022). Product states unmasked-only + mask caveat. |
| F-003 | OPUS48 | 0 | MATH | BLOCKER | RESOLVED | cell 44 — "single attention head output" | Both overstated (B cell 39 / A cells 42,51): "only the MLP computes new coordinates". Corrected: a single head convex-mixes its *projected* values; the block leaves the input hull via W_V/multi-head/W_O/residual AND the MLP (whose distinct role is nonlinear channel mixing). |
| F-004 | OPUS48 | 0 | MATH | BLOCKER | RESOLVED | cell 47 — "residual gradient stays O(1)" | Overclaim inherited from A cell 51 (in B cell 42): residuals "guarantee O(1) gradient". Corrected with counterexamples (J=-I→0; J=I→2^L); residuals improve propagation under suitable init/norm/scaling, not guaranteed. Demo relabeled construction-dependent. |
| F-005 | OPUS48 | 0 | MATH | BLOCKER | RESOLVED | cell 48 — "layer norm ... same sphere" | Overclaim inherited from A cell 51 (in B cell 43): LN maps every input to one sphere and bounds depth. Corrected via A's precise Prop 5.2 (ε=0, nonconstant) + ε>0 norm ≤ √C, constant→0, learned γ,β; LN stabilizes sublayer-input statistics, not depth. Code now uses ε. |
| F-006 | OPUS48 | 0 | FIDEL | MAJOR | RESOLVED | cells 8, 31, 53, 63, 93 | A-only correct content B dropped, ported per merge rule: add-1 smoothing (cell 8), √D variance derivation + production shapes (cell 31), executable end-to-end model → (B,T,V) logits + loss (cell 53), held-out validation (cell 63), full DPO preference-model loss (cell 93). |
| F-007 | OPUS48 | 0 | CLAIM | MAJOR | RESOLVED | product_i0 (basis: premerge/99c_advisory_SOL56.md) | B-side overclaims corrected on external truth: softmax-uniqueness scope, counting-vs-smoothing framing, untrained≠generalization, greedy finite-state scope, KV-cache partial-vs-total + axis relabel, response-mask gradient flow, toy quant-curve scope, "only scale" close, char-OOV, β=4 closeness, causal-mask off-by-one, self-contained→shared-state, lossless-recall. |
| F-008 | SOL56 | 0 | CODE | BLOCKER | OPEN | cell 63 — "Early on, validation loss falls with training loss" | Cell 64 contradicts the lesson: fresh run has validation minimum at step 0, then rises from 1.3884 to 2.6523 while train loss falls. Make the demo exhibit the claimed fall-then-rise with an assertion, or narrate immediate held-out degradation. |
| F-009 | SOL56 | 0 | CLAIM | MAJOR | OPEN | cell 13 — "non-smooth maps have no usable derivative" | False implication; ReLU-like functions are differentiable almost everywhere and train with a chosen kink convention/subgradient. Motivate softmax with positivity, normalization, and convenient differentiability instead. |
| F-010 | SOL56 | 0 | NOTE | MAJOR | OPEN | cell 53 — "exactly the shifted labels of Chapter 3" | Chapter 3 never defines label shifting; restore A cells 37/39/40's `x=ids[:-1]`, `y=ids[1:]`, shapes, and causal target contract, or retarget the reference. |
| F-011 | SOL56 | 0 | FIDEL | MAJOR | OPEN | cell 93 — "The core model is complete, trained" | The assembled transformer is only run at random init; only bigram models are trained. Restore a bounded end-to-end transformer training check as in A cell 58, or qualify the claim. |
| F-012 | SOL56 | 0 | PED | MAJOR | OPEN | cell 102 — "A merged union of two sources" | Product has zero Self-check sections versus 16 cells in source A. Restore bounded learner-facing derivation/interpretation checks, adapting only repo-dependent ones. |
| F-013 | SOL56 | 0 | CLAIM | MAJOR | OPEN | cell 79 — "has a one-to-one counterpart in PyTorch and Hugging Face" | `nn.TransformerDecoderLayer` includes encoder cross-attention and is not one-to-one with a decoder-only GPT block. Use conceptual-analogue language and restore the encoder/decoder family distinction. |
| F-014 | SOL56 | 0 | FIDEL | MAJOR | OPEN | cell 21 — "Every backpropagation step in every language model" | Source A cell 18's `H(q,p)=H(q)+KL(q||p)` and population conditional-entropy floor were dropped. Restore the decomposition, conditioning proof, and inference. |
| F-015 | SOL56 | 0 | FIDEL | MAJOR | OPEN | cell 84 — "the vertical gap ... is the error injected" | Source A cell 79's affine quantizer, zero-point, representable interval, half-step bound, and clipping exception were dropped. Restore them. |
| F-016 | SOL56 | 0 | FIDEL | MAJOR | OPEN | cell 96 — "the three main families of alternative" | Source A cells 93/95's retrieval, external memory, JEPA/world models, paper-reading checklist, and smallest measurable experiment were dropped. Restore equivalent portable content. |
| F-017 | SOL56 | 0 | CODE | MINOR | OPEN | cell 79 — "byte-for-byte the loss you already wrote" | Cell 80 checks `np.isclose` between two NumPy paths, not byte identity or actual `F.cross_entropy`. Claim numerical equivalence within tolerance instead. |
| F-018 | SOL56 | 0 | FIDEL | MAJOR | OPEN | cell 102 — "All fourteen chapters (0–13) are present" | Product Chapter 13 omits source A cell 98's broader-NLP boundary map. Restore a concise portable task-family map and its evidence-scope warning. |
| F-019 | OPUS48 | 0 | FIDEL | MINOR | OPEN | Ch 1/4/5/6 worked-example gaps | Merge dropped A-only exact-digit worked examples (WE 1.1/1.2 softmax/CE digits summing to 0, WE 4.1 attention digits, WE 5.1 LayerNorm C=2 catastrophe, WE 6.1 AdamW step) and the precise AdamW algorithm statement; A-unique concrete rigor missed by SOL56. Restore highest-value ones (WE 5.1, WE 1.2) as numpy self-checks. |
| F-020 | OPUS48 | 1 | CLAIM | MINOR | OPEN | cell 60 — "the model it calls 'trained' is trained" | Bounded end-to-end training updates only the tied W_E; block attention/MLP/LN parameters stay at init, so 'trained end to end' overstates it (one parameter group trained, gradient flows through all blocks). Fix: qualify to 'trains the tied embedding end-to-end; other groups train by the same p-e_y backprop signal'. |
| F-021 | SOL56 | 1 | PED | MAJOR | OPEN | cell 23 — "H(q,p) = H(q) + KL(q\|\|p), verified on a random target" | Restored KL, label-shift, and quantizer examples precede their definitions; label shifting is even used in cells 59–60 before cell 64 explains it. Put definitions/derivations before the first dependent code. |
| F-022 | SOL56 | 1 | CLAIM | MAJOR | OPEN | cell 95 — "set by its largest-magnitude entry" | The taught affine quantizer uses global min/max range, not max absolute magnitude; distinguish asymmetric range calibration from symmetric max-absolute calibration. |
| F-023 | SOL56 | 1 | NOTE | MINOR | OPEN | cell 44 — "## 5 · The block: new features, and surviving depth" | Attention occupies cells 33–43 but Chapter 4 has no heading, while later text refers to Chapter 4 and the close claims all chapters are present. Add the missing Chapter 4 heading. |
| F-024 | SOL56 | 1 | FIDEL | MAJOR | OPEN | cell 112 — "retrieval / external memory" | Source A's modern-system boundary (prompting, retrieval/tool/memory distinctions, sparse/dense RAG failures, evaluation matching, serving scheduling/batching) remains dropped. Restore a compact substantive map. |
| F-025 | SOL56 | 2 | MATH | MAJOR | OPEN | cell 35 — "which already sits at position t+1 in the same input tensor" | True only for t<T; the final target x_{T+1} is outside input x. State the masked-future and outside-window cases separately. |
| F-026 | SOL56 | 2 | CLAIM | MAJOR | OPEN | cell 22 — "Every backpropagation step in every language model" | `p-e_y` is specific to one-hot softmax CE, not every LM objective. Scope it accordingly; distributional CE gives `p-q`. |
| F-027 | SOL56 | 2 | FIDEL | MAJOR | OPEN | cell 61 — "a tied unembedding W_U=W_E^top" | Source A cell 55's parameter-group map and precise tying interpretation remain absent. Restore `z_i=<h,E(i)>`, coupled geometry, `V*C` saving, and scaling intuition. |
| F-028 | SOL56 | 2 | FIDEL | MINOR | OPEN | cell 80 — "The repair: three ways to reshape the simplex" | Source A's beam-search distinction remains dropped. Add accumulated-log-probability sequence search and contrast it with top-k/top-p sampling. |
| F-029 | SOL56 | 3 | CLAIM | MAJOR | OPEN | cell 93 — "it can only reproduce answers it was shown" | Maximum-likelihood/SFT models can generalize to novel responses; pairwise preference data is a distinct training signal, not a repair for literal replay-only behavior. Correct this repeated alignment premise in cells 93, 96, 105–106, and 121. |
| F-030 | SOL56 | 3 | CODE | MINOR | OPEN | cell 16 — `res = minimize(... method='SLSQP' ...)` | The solver returns `res.x` without checking success and emits an unexplained bounds-clipping RuntimeWarning; the same issue recurs in cell 107. Check success and numerical tolerance, and handle or avoid the known warning. |
| F-031 | SOL56 | 5 | MATH | MINOR | OPEN | cell 100 — "the scale must satisfy" | The affine-grid coverage formula omits its interior-zero-point domain and yields `0/0` for ordinary one-sided ranges. State it for `qmin<z<qmax` and define boundary/degenerate cases piecewise. |
| F-032 | SOL56 | 5 | NOTE | NIT | OPEN | cell 116 — "RAG composes retrieval with generation" | Four intended LaTeX arrows are parsed as literal tab-plus-`o` sequences. Store escaped `\\to` commands so the pipeline renders correctly. |
| F-033 | SOL56 | 5 | MATH | MAJOR | OPEN | cell 10 — "It is a bijection: knowing all the conditionals" | A joint with zero-mass prefixes does not uniquely determine conditionals on those prefixes. Restore strict positivity on joints/conditionals or qualify the factorization modulo arbitrary unreachable-branch conditionals. |
| F-034 | HUMAN | 8 | CLAIM | MINOR | RESOLVED | cell 0 — "Every one is self-contained `numpy`" | Contradicts cell 119's correct shared-kernel caveat (F-007 fix). i9: cell 0 now says "in one shared kernel, top to bottom". (FABLE5 audit P-001.) |
| F-035 | HUMAN | 8 | PED | MINOR | RESOLVED | cell 71 — "the train/validation curves above" | Self-checks referenced curves 7 cells below and Ch-7 perplexity material. i9: block moved after the held-out demo; (c) retargeted to AdamW first-step scale-invariance. (P-002.) |
| F-036 | HUMAN | 8 | PED | MINOR | RESOLVED | cell 95 — "`.max(1)*0 +`" | Dead subexpression in the numerical-stability lesson invites false meaning-hunting. i9: deleted, with a comment on why the shift cancels. (P-003.) |
| F-037 | HUMAN | 8 | PED | MINOR | RESOLVED | cells 10/30/62 — "one prefix in; one distribution out" vs `(B,T,V)` | The type change from prefix→one-distribution to per-position outputs was never taught; pooling silently retired. i9: explicit type-reconciliation beat added to the assembly cell. (P-004.) |
| F-038 | HUMAN | 8 | PED | MINOR | RESOLVED | cell 93 — "That is Chapter 11" | Ch-8 forced move skipped Chapters 9–10, breaking the promise chain. i9: detour named at the point of promise. (P-005.) |
| F-039 | HUMAN | 8 | PED | MINOR | RESOLVED | cells 33–35 — "### Where the supervised pairs come from" | Label shifting interposed after the chapter's cliffhanger. i9: plumbing moved before the bag-model break; chapter ends on the break. Definitions still precede all use (F-021 preserved). (P-006.) |
| F-040 | HUMAN | 8 | PED | MINOR | RESOLVED | cells 60/61–66 — "We now hold the complete machine" | Chapter 5 ended twice; forced move fired before assembly/tying. i9: cell 60 is a segue; forced move re-landed verbatim after the parameter budget. Same pattern fixed in Ch 1 (cell 22→post-self-checks) and Ch 6 (cell 76→post-held-out). (P-007.) |
| F-041 | HUMAN | 8 | NOTE | NIT | RESOLVED | cell 60 — "exactly the shifted labels of Chapter 3 consume" | Mangled sentence. i9: composition sentence deduplicated with cell 61; grammar fixed. (P-008.) |
| F-042 | HUMAN | 8 | PED | MINOR | RESOLVED | cell 28 — "encoding it raises a missing-key error" | Ch 2's break was narrated, never executed, against the cell-0 method promise. i9: 3-line cell runs the `KeyError` and prints the byte-level escape. (P-009.) |
| F-043 | HUMAN | 8 | NOTE | MINOR | RESOLVED | cells 9/23/35/36/57/73/96/120 — "ported from source A" | Merge provenance leaked into learner-facing text; cell 96 carried an editorial aside addressed to nobody. i9: all stripped; disclosure consolidated in the cell-0/colophon notes. (P-010.) |
| F-044 | HUMAN | 8 | PED | MINOR | RESOLVED | cells 42/44 — "state … at exactly the strength it holds" (×2) | The F-002 repair was delivered twice, nearly verbatim, straddling its own demo. i9: cell 42 leans to setup+prediction; full scoping, proof, and Haviv caveats live once in cell 44, verbatim. (P-011.) |
| F-045 | SOL56 | 9 | CODE | MAJOR | OPEN | cell 1 — `matplotlib.use("Agg")` | The forced non-GUI backend makes all 16 `plt.show()` calls warn and emits no figure outputs; use an inline headless-safe backend or explicitly embed figures. |
| F-046 | SOL56 | 9 | CLAIM | MAJOR | OPEN | cell 38 — "Repairing it requires an operation with two new powers" | Symmetric pooling's failure does not force attention; position-dependent pooling, recurrence, and convolution are counterexamples. Present attention as the chosen parallel per-position repair or state the constrained design target. |
| F-047 | SOL56 | 9 | PED | MAJOR | OPEN | cells 49/82 — "Why must the mask" / "making that exact" | Two new self-checks have false absolute premises: post-softmax zero+renormalize is valid, and AdamW bias correction does not make the epsilon/decay-bearing update magnitude exactly eta. |
| F-048 | SOL56 | 9 | CLAIM | MAJOR | OPEN | cells 30/98/111/121 — "Where we stand" | New consolidation beats conflate token, attention, response-policy, bigram, cache-arithmetic, and transformer objects, falsely calling one machine instruction-following, compressed, and aligned. Scope each summary to what was actually executed. |
| F-049 | SOL56 | 9 | CLAIM | MAJOR | OPEN | cell 111 — "The model's own corpus is the right yardstick" | Target-token training NLL measures in-sample task performance, not fidelity to the full model's beliefs; use full-vs-quantized output KL/CE for fidelity and held-out data for quality. |
| F-050 | SOL56 | 9 | CLAIM | MINOR | OPEN | cell 125 — "Every chapter opened … watching it break" | The universal method promise remains false after the Chapter-2 fix: Chapters 9 and 13 are declared dictionary/send-off exceptions. Scope the promise to core build chapters or name exceptions. |
| F-051 | SOL56 | 11 | CLAIM | MINOR | RESOLVED | cell 38 — "a short path between any receiver and source" | Causal attention has a direct path only to causally allowed self/earlier sources. Qualify the sentence accordingly; discovered and repaired inside the pre-signoff hostile gate. |

## STATE LOG (append-only; newest at bottom)

- i0 · HUMAN · workspace initialized · product_i0 = copy of source/99c · contract frozen.
- i0 · OPUS48 · per HUMAN: deliverable confirmed = union notebook (MERGE MODE, CONTRACT §1); the seed note "product_i0 = copy of source/99c" above is superseded — product_i0 will be merge-authored from A(99)+B(99c). A one-time advisory pre-merge critique of 99c by SOL56 → premerge/99c_advisory_SOL56.md precedes the merge (advisory only; no LEDGER rows).
- i0 · OPUS48 · merge-draft authored product/product_i0.ipynb from A(99)+B(99c) on numpy substrate; executed all cells clean via nbclient.
- i0 · OPUS48 · resolved F-001 F-002 F-003 F-004 F-005 F-006 F-007 in the merge on external ML truth; each RESOLVED and awaiting SOL56's iter-0 audit for confirmation.
- i0 · SOL56 · confirmed F-001 (MAJOR/FIDEL); propose FROZEN.
- i0 · SOL56 · re-OPENED F-002 (BLOCKER/MATH): cell 36 retains the positions-only order claim.
- i0 · SOL56 · re-OPENED F-003 (BLOCKER/MATH): cells 34/41/43 retain the MLP-only hull-escape story.
- i0 · SOL56 · re-OPENED F-004 (BLOCKER/MATH): cells 45/46 retain the residual-gradient guarantee story.
- i0 · SOL56 · re-OPENED F-005 (BLOCKER/MATH): cell 47 assigns depth-wise activation-scale control to layer norm.
- i0 · SOL56 · re-OPENED F-006 (MAJOR/FIDEL): the held-out validation port contradicts its own runtime evidence.
- i0 · SOL56 · re-OPENED F-007 (MAJOR/CLAIM): listed overclaims remain in cells 27, 77, and 98.
- i0 · SOL56 · raised F-008 (BLOCKER/CODE).
- i0 · SOL56 · raised F-009 (MAJOR/CLAIM).
- i0 · SOL56 · raised F-010 (MAJOR/NOTE).
- i0 · SOL56 · raised F-011 (MAJOR/FIDEL).
- i0 · SOL56 · raised F-012 (MAJOR/PED).
- i0 · SOL56 · raised F-013 (MAJOR/CLAIM).
- i0 · SOL56 · raised F-014 (MAJOR/FIDEL).
- i0 · SOL56 · raised F-015 (MAJOR/FIDEL).
- i0 · SOL56 · raised F-016 (MAJOR/FIDEL).
- i0 · SOL56 · raised F-017 (MINOR/CODE).
- i0 · SOL56 · raised F-018 (MAJOR/FIDEL).
- i0 · OPUS48 · meta-audit adjudicated audit_SOL56_i0 (verified accurate): F-002 F-003 F-004 F-005 F-006 F-007 F-008 F-009 F-010 F-011 F-012 F-013 F-014 F-015 F-016 F-017 F-018 accepted; F-010 F-012 F-016 F-018 reclassified MAJOR->MINOR (severity noted in metaaudit_OPUS48_i0.md).
- i0 · OPUS48 · F-001 confirmed stable and frozen (numpy substrate call stands).
- i0 · OPUS48 · raised F-019 (MINOR/FIDEL): merge dropped A's exact-digit worked examples and precise AdamW algorithm; missed by SOL56.
- i0 · OPUS48 · rework materialized product/product_i1.ipynb (118 cells) from product_i0; executed all cells clean via nbclient; wrote rework/rework_OPUS48_i0.md.
- i0 · OPUS48 · resolved F-002 F-003 F-004 F-005 F-006 F-007 F-008 F-009 F-010 F-011 F-012 F-013 F-014 F-015 F-016 F-017 F-018 F-019 (each FIXed; contradictions propagated to all sibling cells; A-only rigor ported; held-out demo and end-to-end training now assert their lessons).
- i1 · OPUS48 · audit re-executed product_i1 clean; wrote audits/audit_OPUS48_i1.md.
- i1 · OPUS48 · confirmed the iter-0 rework stable and frozen: F-002 F-003 F-004 F-005 F-006 F-007 F-008 F-009 F-010 F-012 F-013 F-014 F-015 F-016 F-017 F-018 F-019.
- i1 · OPUS48 · raised F-020 (MINOR/CLAIM): end-to-end training updates only the tied W_E, so 'trained end to end' overstates it. F-011 held RESOLVED pending F-020.
- i1 · OPUS48 · STATE LOG correction: F-020 reopened (its status is OPEN; a prior line mis-paired it with another finding's status word, folding it wrongly).
- i1 · SOL56 · meta-audit RECLASSIFIED F-020 MINOR->MAJOR and ACCEPTED: one tied parameter group is optimized, not the assembled model's parameter set.
- i1 · SOL56 · re-OPENED F-010 (MINOR/NOTE): cell 58 still points to shifted labels in Chapter 3; the definition is later in Chapter 6.
- i1 · SOL56 · re-OPENED F-013 (MAJOR/CLAIM): the GPT block mapping is fixed, but the required encoder/decoder family distinction remains absent.
- i1 · SOL56 · re-OPENED F-014 (MAJOR/FIDEL): the restored entropy-floor prose falsely makes strict positivity universal.
- i1 · SOL56 · re-OPENED F-015 (MAJOR/FIDEL): the restored zero-point rule omits clipping and does not always represent real zero.
- i1 · SOL56 · re-OPENED and RECLASSIFIED F-016 MINOR->MAJOR (FIDEL): the compressed retrieval/JEPA repair introduces false bottleneck claims.
- i1 · SOL56 · re-OPENED F-019 (MINOR/FIDEL): agreed Worked Example 1.2 was not restored.
- i1 · SOL56 · raised F-021 (MAJOR/PED).
- i1 · SOL56 · raised F-022 (MAJOR/CLAIM).
- i1 · SOL56 · raised F-023 (MINOR/NOTE).
- i1 · SOL56 · raised F-024 (MAJOR/FIDEL).
- i1 · SOL56 · rework materialized product/product_i2.ipynb (119 cells, 46 code); nbclient and independent shared-kernel execution both completed with zero exceptions.
- i1 · SOL56 · resolved F-010 F-011 F-013 F-014 F-015 F-016 F-019 F-020 F-021 F-022 F-023 F-024; definitions now precede use, partial training is scoped, quantizer/math claims are conditioned, and omitted family/system content is restored.
- i2 · SOL56 · audit confirmed F-010 F-011 F-013 F-014 F-015 F-016 F-019 F-020 F-021 F-022 F-023 F-024 stable; propose FROZEN.
- i2 · SOL56 · raised F-025 (MAJOR/MATH).
- i2 · SOL56 · raised F-026 (MAJOR/CLAIM).
- i2 · SOL56 · raised F-027 (MAJOR/FIDEL).
- i2 · SOL56 · raised F-028 (MINOR/FIDEL).
- i2 · OPUS48 · meta-audit of audit_SOL56_i2: F-025 F-026 F-027 F-028 accepted (each verified against product_i2 and upheld).
- i2 · OPUS48 · meta-audit note: audit accurate; F-026 is additionally an internal contradiction with the DPO cell; no false positives to reverse; no additional BLOCKER or MAJOR missed after scrutinizing SOL56's own new cells (family table, quantizer calibration, entropy floor).
- i2 · OPUS48 · rework materialized product/product_i3.ipynb (122 cells) from product_i2; executed all cells clean via nbclient; wrote rework/rework_OPUS48_i2.md.
- i2 · OPUS48 · resolved F-025 F-026 F-027 F-028 (label-shift two cases; p-e_y scoped to one-hot CE + distributional p-q + DPO reconciliation; weight-tying derivation and parameter-budget restored; beam-search paragraph added).
- i3 · OPUS48 · audit re-executed product_i3 clean; confirmed F-025 F-026 F-027 F-028 stable and frozen; wrote audits/audit_OPUS48_i3.md.
- i3 · OPUS48 · emitted signoff/SIGNOFF_OPUS48.md on product_i3 (no BLOCKER/MAJOR found; strongest remaining objection is two unported exact-digit worked examples, below the bar). Convergence pending SOL56's independent signoff on the same unchanged version.
- i3 · SOL56 · meta-audit independently confirmed F-025 F-026 F-027 F-028 stable and FROZEN; the four iter-2 repairs hold.
- i3 · SOL56 · raised F-029 (MAJOR/CLAIM): the repeated claim that SFT can only reproduce shown answers is false, contradicts the course's own generalization lesson, and misstates why preference training is useful.
- i3 · SOL56 · raised F-030 (MINOR/CODE): cells 16 and 107 emit non-deliberate SLSQP warnings and return optimizer results without checking success, contrary to OPUS48's warning inventory.
- i3 · SOL56 · OPUS48's product_i3 signoff is not convergence-valid while F-029 remains OPEN; a later signoff must name the repaired product after a zero-change audit round.
- i3 · SOL56 · rework materialized product/product_i4.ipynb (122 cells, 47 code); fresh-kernel nbclient and independent shared-namespace execution both completed 47/47 with zero exceptions.
- i3 · SOL56 · resolved F-029: replay-only alignment premises were replaced across cells 93, 96, 105–106, and 121 with the distinction between sequence-likelihood generalization and direct pairwise-comparison supervision.
- i3 · SOL56 · resolved F-030: cells 16 and 107 now check optimizer success, assert numerical/closed-form agreement, and narrowly handle the known harmless SLSQP clipping warning; only the deliberate cell-55 LayerNorm warning remains.
- i4 · SOL56 · audit re-executed product_i4 clean (47/47, zero exceptions); confirmed F-029 and F-030 stable and proposed both FROZEN.
- i4 · SOL56 · re-OPENED F-015 (MAJOR; mathematical defect in the FIDEL repair) on new evidence: integer zero-point rounding shifts the representable interval, so cell 100's coverage claim is false and cell 101 invokes the no-clipping half-step lemma on `x=1`, whose pre-clipped code is 8 and is clipped to 7.
- i4 · SOL56 · no signoff emitted because F-015 is OPEN at MAJOR.
- i4 · OPUS48 · meta-audit of audit_SOL56_i4: F-029 F-030 concur frozen; wrote metaaudits/metaaudit_OPUS48_i4.md.
- i4 · OPUS48 · F-015 re-open verified independently (grid [-8/7, 6/7] does not cover [-1,1]; x=1 clips; assertion passes by coincidence) and accepted (MATH/MAJOR, blocking).
- i4 · OPUS48 · retracted my product_i3 signoff (SIGNOFF_OPUS48.md removed): it affirmed a version carrying the F-015 defect my iter-3 audit missed.
- i4 · OPUS48 · rework materialized product/product_i5.ipynb from product_i4; executed all cells clean; wrote rework/rework_OPUS48_i4.md.
- i4 · OPUS48 · resolved F-015 (affine-quantizer calibration corrected to an honest break->repair: naive scale under-covers so x=1 clips; repaired scale s=1/3 covers [-1,1] and the half-step lemma holds for all points).
- i5 · OPUS48 · audit re-executed product_i5 clean; confirmed F-015 stable and frozen; wrote audits/audit_OPUS48_i5.md.
- i5 · OPUS48 · re-emitted signoff/SIGNOFF_OPUS48.md on product_i5 (all findings FROZEN; no BLOCKER/MAJOR). Convergence pending SOL56's independent signoff on the same unchanged version.
- i5 · SOL56 · meta-audit independently confirmed F-015 stable and FROZEN; product_i5 executed 47/47 with zero exceptions and only the deliberate cell-55 warning.
- i5 · SOL56 · raised F-031 (MINOR/MATH): the new affine-grid coverage formula is undefined (`0/0`) at common one-sided-range boundary zero-points unless its domain and piecewise constraints are stated.
- i5 · SOL56 · raised F-032 (NIT/NOTE): cell 116 contains four literal tab characters where the RAG pipeline intends LaTeX arrows.
- i5 · SOL56 · raised F-033 (MAJOR/MATH): cell 10 drops source A's strict-positivity hypothesis and falsely claims a bijection between arbitrary joints and all conditionals despite non-unique conditionals on zero-mass prefixes.
- i5 · SOL56 · OPUS48's product_i5 signoff is not convergence-valid while F-033 is OPEN and F-031 is neither fixed nor explicitly waived by both models.
- i5 · SOL56 · rework materialized product/product_i6.ipynb (122 cells, 47 code); fresh-kernel nbclient and independent shared-namespace execution both completed 47/47 with zero exceptions.
- i5 · SOL56 · resolved F-033: cell 10 now states the strict-positive joint/conditional bijection, explains arbitrary conditionals on zero-mass prefixes, and separates chain-rule sufficiency from non-guaranteed generalization by parameter sharing.
- i5 · SOL56 · resolved F-031: cell 100 now defines piecewise coverage constraints at boundary zero-points and handles the degenerate `[0,0]` range without undefined quotients.
- i5 · SOL56 · resolved F-032: cell 116 now contains four literal LaTeX `\\to` arrow commands and no tab control characters.
- i6 · SOL56 · audit re-executed product_i6 clean (47/47, zero exceptions); confirmed F-033 and F-032 stable and proposed both FROZEN.
- i6 · SOL56 · re-OPENED F-031 (MINOR/MATH): the piecewise constraints are correct, but cell 100 falsely makes an interior zero-point automatic for every nondegenerate two-sided range; asymmetric `[-0.001,1]` rounds to boundary `z=qmin`, making finite coverage impossible with that fixed z.
- i6 · SOL56 · emitted signoff/SIGNOFF_SOL56.md on product_i6 with an explicit F-031 MINOR waiver; convergence still requires same-version OPUS48 signoff and the harness's unchanged-round check.
- i6 · OPUS48 · meta-audit of audit_SOL56_i6: concur F-032 F-033 stable and frozen; wrote metaaudits/metaaudit_OPUS48_i6.md.
- i6 · OPUS48 · F-031 re-open verified (asymmetric range e.g. [-0.001,1] rounds z to a boundary; interior z is a feasibility condition, not automatic) and accepted (MATH/MINOR).
- i6 · OPUS48 · rework materialized product/product_i7.ipynb from product_i6; executed all cells clean; wrote rework/rework_OPUS48_i6.md.
- i6 · OPUS48 · resolved F-031 (cell 100 sentence now states interior zero-point as a feasibility condition, not automatic; matches the piecewise c-/c+ definition).
- i7 · OPUS48 · audit re-executed product_i7 clean; confirmed F-031 stable and frozen; wrote audits/audit_OPUS48_i7.md.
- i7 · OPUS48 · re-emitted signoff/SIGNOFF_OPUS48.md on product_i7 (all 33 findings FROZEN; zero-waiver). Convergence pending SOL56 signing the same product_i7.
- i7 · SOL56 · meta-audit independently re-executed product_i7 clean (47/47, zero exceptions), confirmed F-031's repaired implication and asymmetric-boundary handling, and upheld F-031 as FROZEN.
- i7 · SOL56 · independent MATH/CODE/CLAIM/FIDEL/PED/NOTE review found no new BLOCKER, MAJOR, or MINOR; product_i7 is clean at the contract bar.
- i7 · SOL56 · no-change rework found no ACCEPTED/OPEN/CONTESTED item to edit; fresh-kernel execution completed 47/47 with zero errors and product_i8 was materialized byte-identically from product_i7 (SHA-256 `451d12fb06e1f9abe41ceff04b87c3f4faca780ee28319c5d0739c0957c32ec8`).
- i7 · SOL56 · replaced the stale product_i6/F-031-waiver signoff with a zero-waiver signature on audited product_i7; OPUS48 and SOL56 now sign the same version, with convergence left to the harness.
- i8 · HUMAN · commissioned a third-model pedagogy/movement audit of product_i7 (FABLE5, outside the CONTRACT §7 loop) → audits/audit_FABLE5_i7.md; adopted its 11 proposed rows as F-034…F-044 (raised_by HUMAN). None BLOCKER/MAJOR; the i7 convergence record stands.
- i8 · HUMAN · sanctioned a recomposition charter for iteration 9: prose and structure may be re-composed for movement and voice; NO claim may change strength in either direction; every FROZEN fix survives verbatim-or-stronger; both models must run a regression audit on product_i9 before any new signoff.
- i8 · FABLE5 (HUMAN-sanctioned) · rework materialized product/product_i9.ipynb (128 cells, 48 code) from product_i7; fresh-kernel nbclient execution 48/48 with zero exceptions (only the deliberate ε=0 LayerNorm warning); wrote rework/rework_FABLE5_i8.md.
- i8 · FABLE5 · resolved F-034…F-044 and implemented advisory items A-1…A-5 from the audit: qualification-sediment recomposed lesson-first in cells 10/53/76/105/110 (all scoped claims retained); mystery-thread forward-spoilers removed (Ch 4 no longer names Chapter 11 or the third scale; the Ch 11 reveal is intact); thirteen "Where we stand" consolidation beats fused with the existing forced moves; four new self-check blocks (Ch 0, 4, 5, 10) plus the retargeted Ch 6 block; Ch 2's break executed in code; Ch 10 opens with a behavioral perplexity delta worded to its observed magnitude.
- i8 · FABLE5 · charter-compliance sweep: 12/12 critical frozen-fix anchors verified present in product_i9 (F-002/003/004/005/008/015/025/026/029/030/031/033); provenance strings absent; verification transcript in rework/rework_FABLE5_i8.md.
- i8 · FABLE5 · note: SIGNOFF_OPUS48/SIGNOFF_SOL56 name product_i7 and remain valid for it; product_i9 carries no signoff until both models complete the charter's regression audit.
- i9 · SOL56 · regression audit confirmed the narrow F-034 F-035 F-036 F-037 F-038 F-039 F-040 F-041 F-042 F-043 F-044 repairs stable and frozen; separate regressions are logged under their own IDs.
- i9 · SOL56 · reopened F-007 on new sibling-location evidence: product_i9 cells 26/39 repeat the unscoped softmax-necessity claim, cell 28 denies character OOV immediately before the executed counterexample, and cell 78 labels an untrained uniform prior "fully generalizing."
- i9 · SOL56 · raised F-045 F-046 F-047 F-048 F-049 F-050: missing figure outputs under forced Agg, a non-forced attention inference, two invalid self-checks, scope-collapsing consolidation claims, a wrong belief-fidelity metric rationale, and the still-untrue universal chapter-method promise.
- i9 · SOL56 · product_i9 validates structurally and executes 48/48 without exceptions, but fresh execution produces 16 Agg no-show warnings plus the deliberate LayerNorm warning and zero figure outputs; no SOL56 i9 signoff emitted while F-007 and F-045…F-049 are OPEN at MAJOR.
- i9 · FABLE5 (HUMAN-sanctioned) · meta-position on audit_SOL56_i9: **no contests.** All reclassifications of audit_FABLE5_i7 items accepted (P-005/006/007/011 advisory; P-003 NIT; P-004 folded upward into F-046); the F-007 reopen and F-045…F-050 verified independently on the merits before rework (16 plt.show / 0 embedded figures confirmed; all sibling anchors and false premises located).
- i9 · FABLE5 · rework materialized product/product_i10.ipynb (128 cells, 48 code) from product_i9; fresh-kernel nbclient execution 48/48, zero exceptions, **16/16 figures embedded**; wrote rework/rework_FABLE5_i9.md.
- i9 · FABLE5 · resolved F-007 (reopen): softmax necessity scoped to its exact variational objective in both sibling locations; char-OOV comment scoped to the fixed inventory; "fully generalizing" legend relabeled "untrained near-uniform baseline".
- i9 · FABLE5 · resolved F-045: forced Agg backend removed; inline backend embeds all 16 figures; execution verified.
- i9 · FABLE5 · resolved F-046: the Ch-3 break now forces the two *requirements* only; recurrence/convolution named as counterexamples; attention selected by the further direct-access + parallelism demands.
- i9 · FABLE5 · resolved F-047: Ch-4 check (b) rewritten as the zeroing-plus-renormalization equivalence; Ch-6 check (c) rewritten to make bias-corrected moments exact and the step approximately η, naming ε and λθ as the exactness breakers.
- i9 · FABLE5 · resolved F-048: all Where-we-stand beats scoped to the object actually demonstrated (next-token alphabet; training discipline on the bigram + one tied transformer group; bigram speaks; masking arithmetic, no instruction model trained; bigram weights quantized + hypothetical cache bytes; final beat inventories separate toys).
- i9 · FABLE5 · resolved F-049: pareto sweep now also computes KL(p_full‖p_quant) per bit width (0→0.0713 nats, 8→1 bit); the yardstick paragraph rewritten as three instruments (in-sample sanity / belief fidelity via KL / held-out quality).
- i9 · FABLE5 · resolved F-050: universal break promise scoped to the build chapters in cell 0, the Ch-13 practice cell, and the colophon, naming Chapters 9 and 13 as flagged exceptions.
- i9 · FABLE5 · A-2 residue landed: remaining advance notices of the final Gibbs return removed from the Ch-8 and Ch-10 forced moves; the Ch-11 reveal and three-scale table unchanged.
- i9 · FABLE5 · charter sweep on product_i10: 12/12 critical frozen anchors present; F-007 sibling strings and F-047 false premises absent; transcript in rework/rework_FABLE5_i9.md. product_i10 awaits regression audits by OPUS48 and SOL56; no FABLE5 signoff attaches (the reworker does not certify its own rework).
- i10 · SOL56 · regression audit independently validated and executed product_i10 (48/48, zero exceptions, 16/16 embedded figures, only the deliberate LayerNorm warning); all 12 declared frozen anchors remain present.
- i10 · SOL56 · confirmed F-007 F-045 F-048 F-049 F-050 stable and frozen: softmax/OOV/baseline scope, figure rendering, object-specific consolidation, KL-vs-NLL-vs-held-out metrics, and build-chapter scoping all hold.
- i10 · SOL56 · re-OPENED F-046 (MAJOR/CLAIM): direct all-prefix dependence plus train-time position parallelism does not uniquely select attention; a full-window causal convolution is an order-sensitive, direct, parallel counterexample.
- i10 · SOL56 · re-OPENED F-047 (MAJOR/PED): the masking half is correct, but cells 76/82 still claim an approximately eta AdamW first step regardless of gradient scale; the sign-step approximation requires nonzero |g| much larger than epsilon.
- i10 · SOL56 · A-2 advisory did not land substantively: cells 49/98/111 retain synonymous advance notices of the Gibbs return. No SOL56 i10 signoff emitted while F-046 and F-047 remain OPEN at MAJOR.
- i10 · SOL56 · rework materialized product/product_i11.ipynb from product_i10 with exactly three markdown-source edits (cells 38/76/82); fresh-kernel execution completed 48/48 with zero exceptions, 16/16 embedded figures, and only the deliberate LayerNorm warning; wrote rework/rework_SOL56_i10.md.
- i10 · SOL56 · resolved F-046: cell 38 now presents attention as the course's chosen content-adaptive parallel routing mechanism, explicitly not a uniqueness theorem, and retains full-window causal convolution/global mixing as counterexamples to selection by the stated requirements.
- i10 · SOL56 · resolved F-047: cells 76/82 now give the exact first-step adaptive component, condition its sign-step approximation on nonzero |g| much larger than epsilon, cover near-zero/zero gradients and decoupled decay, and retain cell 49's correct masking equivalence.
- i11 · SOL56 · pre-signoff hostile gate raised F-051 (MINOR/CLAIM): i11 cell 38's “any receiver and source” short-path wording omitted the causal-mask restriction.
- i11 · SOL56 · resolved F-051 before formal audit: cell 38 now says “between each receiver and every causally allowed source”; the red/green scope check passes and product_i11 was freshly re-executed 48/48 with 16/16 figures.
- i11 · SOL56 · final regression audit on product_i11 SHA `1902accaa9bfb1627182557552e5d3bd193b2ee2e2703dfeddfa11b4751162bf` passed three independent gates (math/pedagogy, notebook integrity, hostile six-axis); each fresh execution completed 48/48 with zero errors, 16/16 figures, and only the deliberate LayerNorm warning.
- i11 · SOL56 · confirmed F-046 F-047 F-051 stable and frozen: attention is a chosen rather than uniquely forced mechanism, AdamW's sign-step approximation is correctly conditioned and edge-tested, and the direct-path claim is restricted to causally allowed sources.
- i11 · SOL56 · independent final audit found no new BLOCKER, MAJOR, or MINOR on any CONTRACT axis; wrote audits/audit_SOL56_i11.md and emitted a zero-waiver SOL56 signoff on product_i11. Historical OPUS48 product_i7 signoff and coord/STOP remain untouched.
