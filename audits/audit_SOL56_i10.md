# Regression audit SOL56 i10 — landing of rework_FABLE5_i9

**Overall verdict: NEEDS NARROW REVISION; no i10 signoff.** The rework is computationally
sound and most of its scope repairs landed. F-007, F-045, F-048, F-049, and F-050 are stable
and can be FROZEN. F-046 still presents attention as uniquely selected by requirements that
other operations satisfy, and F-047 still teaches unconditional first-step scale invariance in
the AdamW self-check and a sibling explanation. Both remain MAJOR under CONTRACT §4.

The historical `coord/STOP` and both existing signatures name product i7; I did not alter them.

## Verification performed

- Read `CONTRACT.md`, both source notebooks, `audits/audit_SOL56_i9.md`, the folded ledger,
  `rework/rework_FABLE5_i9.md`, and product i9/i10.
- Stable-ID diff: both products have **128 cells (80 markdown, 48 code)** with identical cell
  IDs/order and notebook metadata. Exactly 18 cell sources changed:
  `0, 1, 26, 28, 30, 38, 39, 49, 78, 82, 83, 94, 98, 109, 111, 121, 125, 127`.
- `nbformat.validate(product_i10)` passes. Saved execution counts are sequential 1–48, with
  zero error outputs.
- Fresh-kernel `nbclient` execution completed **48/48 with zero exceptions**. Saved and fresh
  runs both contain 16 valid, distinct PNG outputs at cells
  `18, 52, 55, 62, 73, 75, 78, 81, 88, 93, 97, 103, 109, 115, 118, 120`.
  The only runtime warning is the deliberate epsilon-zero LayerNorm demonstration in cell 58.
- The fresh bit sweep reproduces the claimed mean
  `KL(p_full || p_quant)` values `0.0000 / 0.0009 / 0.0348 / 0.0713` nats for
  8/4/2/1 bits. All 12 critical frozen anchors named by the reworker remain present.

## Resolution audit

| finding | i10 disposition | evidence |
|---|---|---|
| F-007 | **confirm → FROZEN** | Cells 26/39 scope softmax uniqueness to the score-plus-entropy objective; cell 28 scopes character OOV to its fixed inventory; cell 78 says “untrained near-uniform baseline.” The defective sibling strings are absent. |
| F-045 | **confirm → FROZEN** | Cell 1 no longer forces `Agg`; independent fresh execution embeds all 16 expected figures with no no-show warnings. |
| F-046 | **re-OPEN · MAJOR** | Cell 38 acknowledges recurrence/convolution but still says direct all-prefix reach plus train-time parallelism “select” attention. Those conditions do not uniquely do so. |
| F-047 | **re-OPEN · MAJOR** | Cell 49's masking check is now correct. Cells 76/82 still make the AdamW sign-step approximation unconditional in gradient scale, so the pedagogical repair is incomplete. |
| F-048 | **confirm → FROZEN** | The consolidation beats now distinguish next-token probabilities, the trained bigram, one trained transformer parameter group, masking arithmetic without a trained instruction model, cache arithmetic, and separate compression/alignment toys. |
| F-049 | **confirm → FROZEN** | Cell 109 computes full-distribution KL over every one of the toy bigram's four contexts; cell 111 correctly separates in-sample target NLL, belief-fidelity KL, and held-out deployment quality. The context average is uniform, not deployment-frequency weighted, but the toy scope is explicit. |
| F-050 | **confirm → FROZEN** | Cells 0/127 scope the rhythm to build chapters and name Chapters 9/13 as exceptions; cell 125 now says “Nearly every chapter.” |

## Findings still open

### F-046 · CLAIM/PED · MAJOR
- loc: cell 38 — “the operation those requirements select”
- wrong: Direct access to every earlier position and parallel computation over positions do not
  uniquely select attention. The repair withdraws the original exclusion of recurrence and
  convolution, then restores the same forced inference with two insufficient extra conditions.
- correct: Present attention as the chosen content-adaptive, parallel routing mechanism, not a
  logically forced one; or state narrower desiderata without claiming uniqueness.
- evidence: A full-receptive-field causal convolution
  $y_t=\sum_{d=0}^{t}K_d x_{t-d}$ is order-sensitive, gives each output direct dependence on
  every earlier input when the kernel has full support, and computes all positions in parallel.
  Global token mixers supply further counterexamples. The stated criteria therefore do not entail
  dot-product attention.

### F-047 · MATH/PED · MAJOR
- loc: cells 76/82 — “regardless of gradient scale” / “at any gradient scale”
- wrong: The self-check still expects
  $\eta g_1/(|g_1|+\varepsilon)\approx\pm\eta$ at *any* gradient scale, while cell 76 says the
  first step has magnitude $\eta$ regardless of scale. That approximation fails when
  $|g_1|\lesssim\varepsilon$; at $g_1=0$ the adaptive component is zero. The full AdamW update
  also includes decoupled decay.
- correct: Bias correction gives $\hat m_1=g_1$ and $\hat v_1=g_1^2$ exactly. The adaptive
  component is approximately a sign step only for nonzero $|g_1|\gg\varepsilon$; the full
  parameter change additionally contains $-\eta\lambda\theta_1$.
- evidence: With $g_1=10^{-12}$ and $\varepsilon=10^{-8}$,
  $|g_1|/(|g_1|+\varepsilon)\approx10^{-4}$, so the adaptive magnitude is about
  $10^{-4}\eta$, not $\eta$. This leaves a false expected conclusion in a learner self-check,
  which CONTRACT §4 classifies as MAJOR. Cell 49's post-softmax-zero-plus-renormalize
  equivalence is correct and is not part of the reopen.

## Advisory landing

The A-2 edit landed lexically, not pedagogically. Cell 49 still says the Gibbs structure “is not
done returning” and “Keep watching”; cell 98 says it “returns” and explicitly names Chapter 11;
cell 111 says it “walks on stage one more time — next.” Replacing “returns for the last time”
with synonymous advance notices does not restore the intended reveal. This remains advisory,
not a ledger finding, because movement/spoiler preference is outside CONTRACT §3.

## Axis coverage

- **MATH:** F-047 remains open; the other changed derivations and the KL computation check out.
- **CODE:** none found; structural validation, fresh execution, assertions, figures, and outputs pass.
- **CLAIM:** F-046 remains open; the object-scoping repairs in F-007/F-048/F-050 hold.
- **FIDEL:** none found; the 18-cell patch drops no correct source content and preserves all
  named frozen anchors from the two-source merge.
- **PED:** F-046/F-047 remain open; A-2's non-landing is recorded separately as advisory.
- **NOTE:** none found; symbols and names in the changed cells remain consistent, with no stray
  markdown control characters.

## Signoff disposition

No SOL56 signoff on product i10 while F-046 and F-047 remain OPEN at MAJOR. The required next
step is a two-location reasoning repair, not another structural recomposition: weaken cell 38's
selection claim and condition the AdamW sign-step statements in cells 76/82 on
$|g|\gg\varepsilon$.
