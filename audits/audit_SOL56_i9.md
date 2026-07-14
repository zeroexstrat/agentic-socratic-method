# Regression audit SOL56 i9 — FABLE5 audit, rework, and product_i9

**Overall verdict: NEEDS REVISION; no i9 signoff.** FABLE5 identified real composition damage,
and every one of its eleven narrow Part-I edits is visibly present in product i9. The landing is
structurally valid and executes 48/48 code cells without an exception. It is not regression-safe:
the audit misclassified several contract-excluded preferences, missed surviving F-007 siblings,
and the recomposition introduced false consolidation claims and invalid self-check premises.

The historical `coord/STOP` and both existing signatures correctly name product i7; I did not
alter them. Product i9 requires repair and another regression audit before either model signs it.

## Verification performed

- Read `CONTRACT.md`, both source notebooks, `audits/audit_FABLE5_i7.md`,
  `rework/rework_FABLE5_i8.md`, the folded ledger, and product i7/i9.
- Diffed notebooks by stable cell ID: **32 inherited source cells changed, 6 cells added, 0
  removed**; 122/47 cells/code became 128/48.
- `nbformat.validate(product_i9)` passes; saved execution counts are sequential 1–48 and contain
  no error output.
- Fresh-kernel `nbclient` execution completed **48/48 with zero exceptions**.
- The execution did not support the rework's “only deliberate epsilon warning” claim in this
  environment: cell 1 forces the non-GUI `Agg` backend, so all 16 `plt.show()` calls warn that
  they cannot show a figure. The saved artifact has 46 stream outputs and **zero**
  `display_data`/`execute_result` outputs. The epsilon-zero LayerNorm warning is the seventeenth.

## Meta-audit of audit_FABLE5_i7

FABLE5's editorial diagnosis is useful, but its contract taxonomy and completeness do not hold.

| item | disposition | reasoning |
|---|---|---|
| P-001 | **UPHOLD · CLAIM/MINOR** | Cell 0's independent-self-containment promise contradicts cell 119's shared-state caveat. This is new-location evidence that F-007 propagation was incomplete. |
| P-002 | **PARTIAL UPHOLD · PED/MINOR** | The train/validation curves really are below the self-check. The tokenizer-perplexity question is less defective than claimed: cells 11, 23, and 28 supply most prerequisites, though not the comparison rule as directly as source A. |
| P-003 | **RECLASSIFY · PED/NIT** | `.max(1)*0` is dead and distracting, but the calculation and output are correct; MINOR is too high. |
| P-004 | **RECLASSIFY UPWARD · CLAIM/PED MAJOR** | The missing prefix-map/per-position-output bridge is real, but the deeper error is cell 33's forced inference. Symmetric pooling's failure does not make cross-position attention necessary; position-dependent pooling, recurrence, or convolution are counterexamples. |
| P-005 | **ADVISORY, not a contract finding** | The destination is accurate and cells 94–105 are merely intervening chapters. Promise-chain movement is section-order/narrative preference, explicitly outside CONTRACT §3. |
| P-006 | **ADVISORY, not a contract finding** | Moving label shifting before a cliffhanger is ordering preference; its i7 location already met the definitions-before-use requirement. |
| P-007 | **ADVISORY, not a contract finding** | The double ending is real composition scar tissue, but it is movement/repetition/ordering. P-008 contains the in-scope defect. |
| P-008 | **UPHOLD · NOTE/NIT** | The sentence “exactly the shifted labels … consume” is malformed and inconsistent with its sibling explanation. |
| P-009 | **PARTIAL UPHOLD AND BROADEN · CLAIM/PED MINOR** | Chapter 2 narrated rather than ran its OOV break, but it was not the sole exception. Chapters 9 and 13 explicitly do not follow the universal runnable-break rhythm, so adding one KeyError cell cannot make the global “every chapter” promise true. |
| P-010 | **RECLASSIFY · narrow NOTE/NIT; remainder advisory** | Undefined reader-facing referents (“source A”, “original text/notebook”) are a weak consistency defect. The one-voice/provenance objection is style and therefore out of scope. |
| P-011 | **ADVISORY, not a contract finding** | The duplicated caveat is correct both times. Repetition and length alone are excluded, not a new PED defect against F-002. |

### Advisory assessment

- **A-1:** directionally right, but incomplete. The audit calls cell 76's uniform output
  “ignorance, not transfer” while missing cell 75's executable plot legend “uniform prior
  (fully generalizing).” The course still contains claim→retraction scar tissue because the
  upstream false label survived.
- **A-2:** valid editorial advice, only partially implemented. Product i9 still announces the
  final Gibbs return at cells 49, 98, and 111; the explicit Chapter-11 pointer was reduced, but
  the promised mystery is still telegraphed three times.
- **A-3:** not new evidence for reopening F-012. The earlier adjudication deliberately chose a
  bounded handful rather than all source-A checks. HUMAN could add retrieval practice, but the
  audit should label that additive scope, not a missed convergence defect.
- **A-4:** materially overstated. Product i7 already had consolidation-like summaries at cells
  22, 28, 46, 60, 76, 89, 93, 96, 105, and 110. What was absent was a uniform labeled device,
  not consolidation itself. Adding thirteen summaries was authorized, but each new summary
  still had to preserve scope.
- **A-5:** the motivation idea is useful, but its metric argument is wrong. The 1-bit change in
  i7 is 2.349→2.511 (about 6.9%), not a “blowup,” and target-token NLL is not a measure of
  fidelity to the full model's beliefs. That requires full-vs-quantized output KL/cross-entropy
  on representative contexts; deployment quality still requires held-out data.

FABLE5 also missed that no plot is embedded or displayed under the forced `Agg` backend, despite
making repeated judgments about what the plots show.

## How F-034…F-044 landed

The **narrow repair requested by each adopted row is present and stable**, so I confirm F-034
through F-044 as FROZEN. New or under-scoped defects are logged separately below; freezing a
narrow row does not certify the new prose surrounding its repair.

| finding | i9 result |
|---|---|
| F-034 | Cell 0 now promises top-to-bottom shared-kernel execution, consistent with cell 125. |
| F-035 | The Ch-6 block moved after the held-out curves and (c) was retargeted. Its replacement question introduces F-047. |
| F-036 | Cell 100 removes the dead term, explains max-shift cancellation, and remains numerically equal to the loop path. |
| F-037 | Cell 64 explicitly reconciles prefix→distribution with all-prefix `(T,V)` output, retires pooling, and identifies the last row for generation. The deeper forced-attention inference remains F-046. |
| F-038 | Cell 98 names the Chapters 9–10 detour at the promise point. |
| F-039 | Label-shift plumbing precedes the bag-model break; definitions still precede every dependent use. |
| F-040 | Chapters 1, 5, and 6 now each have one terminal forced move. |
| F-041 | The mangled cell-60 sentence is gone rather than duplicated. |
| F-042 | New cell 29 catches and prints the expected KeyError. The immediately preceding false OOV comment reopens F-007. |
| F-043 | Listed body provenance strings are absent; disclosure remains in the colophon. |
| F-044 | The pre-demo attention paragraph is setup-only and the full caveat appears once after the run. Other softmax-scope contradictions remain under F-007. |

## Reopened finding

### F-007 — REOPEN · CLAIM · MAJOR

**New sibling-location evidence shows the bundled overclaim repair never fully propagated and i9
adds another contradiction:**

- cell 26, “softmax — by necessity, not convention,” and cell 39, “the *only* principled way,”
  contradict cell 49's correct statement that softmax is unique only for the specific
  score-plus-Shannon-entropy objective and that other smooth mappings exist;
- cell 28's code comment says character tokenization has “nothing unseen … OOV,” immediately
  contradicted by cell 29's executed KeyError and cell 30's byte-level qualification;
- cell 78 labels a uniform untrained prior “fully generalizing,” immediately contradicted by
  recomposed cell 79: “ignorance, not transfer.”

Correct looks like: qualify softmax by its exact variational objective; say character tokenizers
avoid OOV only inside their fixed inventory; relabel the plot line “untrained near-uniform
baseline.” These are precisely F-007's frozen softmax/OOV/untrained-generalization scopes, so this
is a reopen on new locations rather than a duplicate finding.

## New product-i9 findings

### F-045 · CODE/PED · MAJOR — cell 1, `matplotlib.use("Agg")`

The forced non-GUI backend makes all 16 `plt.show()` calls warn and produce no embedded figure.
Fresh execution has zero exceptions but zero figure outputs; the learner cannot “watch” any of the
curves the prose interprets. Correct: use the notebook inline backend (which is headless-safe) or
explicitly embed/save and display each figure, then assert the executed notebook contains the
expected display outputs.

### F-046 · CLAIM/PED · MAJOR — cell 38, “Repairing it requires an operation with two new powers”

The demonstrated bag model fails because `mean(axis=0)` is symmetric. That rules out symmetric
pooling, not every non-attention repair. Position-specific weighted pooling, an RNN, or a causal
convolution can distinguish order and condition on context. The new type bridge appears only in
Chapter 5 and does not retroactively make attention logically necessary. Correct: call attention
the chosen parallel, per-position repair, or state the constrained design target before claiming
what it forces.

### F-047 · MATH/PED · MAJOR — cells 49 and 82, invalid new self-check premises

- Cell 49 asks why a mask **must** add `-∞` before softmax rather than zeroing afterward. Zeroing
  forbidden probabilities **and renormalizing** is mathematically equivalent; only zeroing
  without renormalization breaks the simplex. State that qualifier.
- Cell 82 asks how AdamW bias corrections make the first-step magnitude “exact.” They give
  `m_hat_1=g_1`, `v_hat_1=g_1^2`, but the adaptive magnitude is
  `eta*|g|/(|g|+epsilon)`, and the full update also contains `eta*lambda*theta`. Bias correction
  makes the moment estimates unbiased at that step, not the complete update exactly `eta`.

The contract explicitly treats a self-check with a false expected answer as MAJOR.

### F-048 · CLAIM/PED · MAJOR — cells 30/98/111/121, consolidation collapses distinct objects

The new “Where we stand” beats repeatedly turn separate demonstrations into achievements of one
machine:

- cell 30 says **every probability** in the course lives on token alphabet `V`; attention rows
  live over positions and Chapter 11's policy lives over response candidates;
- cell 98 says “The machine follows instructions,” but Chapter 8 only computes masking arithmetic
  on fixed illustrative losses and trains no instruction model;
- cell 111 says “The machine now fits in memory,” but the code fake-quantizes a trained bigram and
  separately counts hypothetical transformer-cache bytes;
- cell 121 calls “the machine” complete, compressed, and aligned, although the assembled
  transformer is neither quantized nor preference-aligned; those are separate toy objects.

Correct: scope each summary to the exact object demonstrated. This is the central no-claim-
strength-change charter violation.

### F-049 · CLAIM/PED · MAJOR — cell 111, “The model's own corpus is the right yardstick”

The code computes NLL against observed target tokens. That measures in-sample predictive
performance on those contexts, not whether the quantized output distributions preserve the full
model's beliefs. A model can keep or improve target NLL while changing all non-target
probabilities. Correct: call this a paired in-sample task sanity check; use
`KL(p_full || p_quantized)`/cross-entropy on representative contexts for belief fidelity and
held-out task data for quality/generalization.

### F-050 · CLAIM/PED · MINOR — cell 125, “Every chapter opened … watching it break”

F-042 makes Chapter 2 runnable, but the universal promise remains false: Chapter 9 explicitly
calls itself a dictionary rather than a movement, and Chapter 13 is a practice/send-off rather
than a naive-answer break. Cell 127 repeats the universal claim. Correct: say “the core build
chapters” or name the deliberate exceptions.

## Advisory landing beyond the findings

- A-1's lesson-first rewrites generally improve cells 53/76/105/110 without dropping their
  qualifications, but the surviving cell-78 legend shows recomposition was not propagated across
  prose, code labels, and outputs.
- A-2 reduced explicit spoilers but did not achieve its own stated reveal: cells 49, 98, and 111
  still announce the final return.
- A-3 added four useful retrieval-practice blocks, but two contain F-047's false premises.
- A-4 added all thirteen labeled beats, but F-048 shows why summary sentences require the same
  adversarial scope check as derivations.
- A-5 added the observed 2.349→2.391→2.503 behavior line and correctly calls it modest, but the
  line is appended after the staircase rather than leading the chapter, and F-049 rejects its
  evaluation rationale.

## Signoff disposition

No SOL56 signoff on product i9. F-007 is reopened at MAJOR and F-045 through F-049 are OPEN at
MAJOR. Product i7's existing signatures and STOP record remain untouched as historical artifacts;
the newly discovered i7 sibling evidence must now be adjudicated under the contract's frozen-
finding/new-evidence rule.

