# Meta-audit OPUS48 i0 — adjudicating audit_SOL56_i0

**Overall:** SOL56's audit is accurate and high-signal. I independently verified every cited
location in `product_i0`; the contradiction sites are real. The central defect is mine: my
merge applied *single-cell* corrections (cells 38, 44, 47, 48, 62, 78, 96) but left the
*sibling* cells that repeat the same overclaim untouched (cells 36, 34, 45, 47, 77, 98), so
the notebook now teaches a claim and its correction in different cells — an internal
contradiction, which is worse than the original overclaim. I uphold all five BLOCKERs, uphold
most MAJORs, reclassify four findings I judge below MAJOR, and add one finding SOL56 missed.

Verification I ran: re-read all cited cells; grep-confirmed each anchor's cell index (36, 34,
45, 47, 27, 77, 96+98, 13, 79, 93); confirmed the KL-decomposition/entropy-floor is absent
(no `H(q,p)` anywhere); reproduced the held-out run (val NLL rises monotonically from step 0,
argmin=0) — F-008 is correct.

## Disposition of SOL56's re-opens (my prior F-001..F-007)

### F-001 — verdict: UPHELD (confirm → FROZEN)
- reasoning: The numpy substrate executes without the unavailable torch/repo dependency; the
  substrate call stands. Agreeing to freeze.

### F-002 — verdict: UPHELD → ACCEPTED (BLOCKER)
- reasoning: Correct. Cell 36 still asserts "Order enters only when we add a per-position
  signal," which my cell 38 then contradicts. A per-finding fix must propagate to every
  sibling cell, not just the most prominent one. My earlier RESOLVED was premature.

### F-003 — verdict: UPHELD → ACCEPTED (BLOCKER)
- reasoning: Correct. Cell 34 ("escaping it is later the job of the MLP") and the cell-41 plot
  title/print still teach MLP-only hull escape; cell 44 alone corrects it. Contradiction stands.

### F-004 — verdict: UPHELD → ACCEPTED (BLOCKER)
- reasoning: Correct. Cell 45 title "Depth kills gradients — unless you add the identity back"
  and the cell-46 plot title still imply a guaranteed identity route; only cell 47 gives the
  counterexamples. Contradiction stands.

### F-005 — verdict: UPHELD → ACCEPTED (BLOCKER)
- reasoning: Correct. Cell 47's closing "That is the job of the last ingredient" assigns
  depth-wise scale control to LayerNorm, which cell 48 explicitly denies. Contradiction stands.

### F-006 — verdict: UPHELD → ACCEPTED (MAJOR)
- reasoning: The held-out *section* is present, but per F-008 its run does not demonstrate the
  generalization-then-overfitting lesson, so the resolution does not hold as authored. The
  other F-006 ports (smoothing, √D, end-to-end forward, DPO loss) are present and stand.

### F-007 — verdict: UPHELD → ACCEPTED (MAJOR)
- reasoning: Correct. Sibling overclaims remain: cell 27 "it generalizes" (untrained model),
  cell 77's print "gradient contribution is exactly 0"/"100%", and the cell-98 table row
  "lossless recall" (my fix lives at cell 96). Same single-cell-edit defect.

## SOL56's new findings

### F-008 — verdict: UPHELD → ACCEPTED (CODE / BLOCKER)
- reasoning: Verified independently — validation NLL rises monotonically from step 0
  (1.3884 → 2.6523), so the cell's "validation loss falls with training loss / generalization
  early" narrative is contradicted by its own output. The demo must be changed (a setup whose
  held-out loss genuinely dips before rising, asserted) or the narrative rewritten to the
  honest result. Excellent catch — this is precisely the failure the held-out port was meant
  to prevent, reproduced.

### F-009 — verdict: UPHELD → ACCEPTED (CLAIM / MAJOR)
- reasoning: Correct. "non-smooth maps have no usable derivative" (cell 13) is false — ReLU
  is the standard counterexample (subgradient / a.e.-differentiable). The motivation for
  softmax only needs "smoothness is convenient," so the overclaim is both wrong and
  unnecessary. Keeping MAJOR: a learner internalizing "non-smooth ⇒ untrainable" is a real
  harm given ReLU's ubiquity.

### F-010 — verdict: RECLASSIFIED (MAJOR → MINOR) → ACCEPTED (NOTE)
- reasoning: The dangling reference is real — product Chapter 3 never defines label shifting,
  so cell 53's "exactly the shifted labels of Chapter 3" points at undefined content. But this
  is a fixable cross-reference / a light content restoration, not a wrong or misleading claim;
  NOTE-MINOR fits CONTRACT §4 better than MAJOR. Will fix by defining the shift in Ch3 (porting
  A's Worked Example 3.2) and retargeting the reference.

### F-011 — verdict: UPHELD → ACCEPTED (FIDEL / MAJOR)
- reasoning: Correct and sharp. The assembled transformer (cell 54) runs only at random init;
  Chapter 6 trains bigram/factored models, not the assembled model — so calling the model
  "trained" (cell 93) is unearned. Fix: add a bounded end-to-end training of the numpy GPT
  with an asserted loss decrease (mirroring A's `overfit_tiny_batch`), or qualify the claim.

### F-012 — verdict: RECLASSIFIED (MAJOR → MINOR) → ACCEPTED (PED)
- reasoning: Partly valid, partly scope. CONTRACT §3 lists "whether a different pedagogy could
  work" as out of scope, and 99c deliberately uses a break→repair pedagogy rather than
  self-check boxes; requiring self-checks wholesale imposes A's format. But a few high-value
  self-checks do carry unique interpretive content (goal (d)), so I keep it as a MINOR
  enhancement rather than overturning outright. Will add a handful at key chapters, not 16.

### F-013 — verdict: UPHELD → ACCEPTED (CLAIM / MAJOR)
- reasoning: Correct. `nn.TransformerDecoderLayer` includes encoder cross-attention (requires
  `memory`) and is *not* a decoder-only GPT block; listing it as the one-to-one counterpart is
  a factual mismap a learner would act on. `GPT2Block` is the right analogue. Fix the table row
  and frame entries as conceptual analogues.

### F-014 — verdict: UPHELD → ACCEPTED (FIDEL / MAJOR)
- reasoning: Correct. The merge dropped A's Theorem 1.9 (H(q,p)=H(q)+KL(q‖p); population NLL =
  irreducible conditional entropy + KL). Confirmed absent (no `H(q,p)` in product). This is
  unique, correct content from a co-equal source and materially deepens the loss/perplexity
  story. Restore a compact version.

### F-015 — verdict: UPHELD → ACCEPTED (FIDEL / MAJOR)
- reasoning: Correct. The quantization chapter kept the staircase picture but dropped A's
  affine quantizer (scale, zero-point), the representable interval, and the proved half-step
  bound |x−x̂| ≤ s/2 with the clipping exception. Restore Q_{s,z}/D_{s,z} and the bound.

### F-016 — verdict: RECLASSIFIED (MAJOR → MINOR) → ACCEPTED (FIDEL)
- reasoning: The product preserves the core diagnostic ("which cost does it cut, what does it
  pay") but drops A's retrieval/world-model directions and the paper-reading checklist. The
  dropped material is real content, but it is survey/enrichment adjacent to §3's scope-choice
  boundary rather than a wrong or missing technical claim; MINOR enrichment. Will restore a
  compact reading-method rubric + one line on retrieval/world-models.

### F-017 — verdict: UPHELD → ACCEPTED (CODE / MINOR)
- reasoning: Correct. Cell 80 checks `np.isclose` between two numpy implementations and never
  calls a framework `F.cross_entropy`, so "byte-for-byte the loss you already wrote" overstates
  it. Reword to "numerically equal within tolerance"; assert `np.allclose`.

### F-018 — verdict: RECLASSIFIED (MAJOR → MINOR) → ACCEPTED (FIDEL)
- reasoning: Same reasoning as F-016. A's broader-NLP task-family map (parsing, IE, coref,
  discourse, speech, agents) is a survey list; dropping it is enrichment loss, not a wrong
  claim. Will restore a portable one-paragraph version with A's "fluent generation ≠ every
  language behavior" warning.

## Findings SOL56 MISSED

### F-019 · FIDEL / MINOR (missed by SOL56)
- loc: product Chapters 1, 4, 5, 6 (worked-example gaps)
- wrong: SOL56 flagged two dropped A-only rigor items (F-014 KL decomposition, F-015 half-step
  bound) but missed that the merge also dropped A's **exact-digit worked examples** and the
  precise **AdamW algorithm statement** — A-unique concrete content. Specifically: Worked
  Example 1.1/1.2 (softmax digits z=(2,0,−1,1) → p=(0.6439,…), ℓ=1.4402, gradient sums to 0),
  Worked Example 4.1 (one attention head over "cat", every number), Worked Example 5.1
  (LayerNorm at C=2 collapses to ±(1,−1) — directly reinforces the F-005 fix), and Algorithm
  6.3 + Worked Example 6.1 (the AdamW bias-correction/decoupled-decay update, executed).
- correct: Restore the highest-value worked examples as small numpy self-checks — at minimum
  WE 5.1 (LN C=2 catastrophe, which strengthens the corrected LN section) and WE 1.2 (the
  residual p−e_y gradient summing to zero) — and state the AdamW update precisely where the
  AdamW-vs-SGD race already appears.
- evidence: Source A cells 21/22 (WE 1.1/1.2), 45/46 (WE 4.1), 53/54 (WE 5.1), 60/61 (WE 6.1),
  and Algorithm 6.3 (cell 57) contain this content; no product cell reproduces the exact-digit
  worked examples or the boxed AdamW update.

## Summary for the rework turn
- **BLOCKER (must fix):** F-002, F-003, F-004, F-005 (propagate each correction to all sibling
  cells so the notebook stops contradicting itself), F-008 (make the held-out demo match its
  lesson or rewrite honestly).
- **MAJOR (must fix):** F-006, F-007, F-009, F-011, F-013, F-014, F-015.
- **MINOR (address; may be waived at signoff):** F-010, F-012, F-016, F-017, F-018, F-019.
- **FROZEN:** F-001.
