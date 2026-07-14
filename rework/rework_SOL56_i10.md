# Rework SOL56 i10 — product_i10 → product_i11

**Scope:** repair only the two MAJOR findings reopened by `audit_SOL56_i10.md`. No chapter
movement, new examples, or broad prose recomposition. Product i11 preserves all 128 cells and
changes exactly three markdown sources: cells 38, 76, and 82.

## Root cause

Both i10 failures came from a correct local qualification followed by a new universal claim:

- Cell 38 acknowledged recurrence and convolution as alternatives, then said direct reach plus
  train-time parallelism *selects* attention. A full-receptive-field causal convolution satisfies
  both stated requirements, so the conclusion still did not follow.
- Cell 82 wrote the exact AdamW first-step formula but called it approximately a sign step “at any
  gradient scale”; cell 76 retained the same sibling claim. The approximation requires
  nonzero `|g| >> epsilon` and fails near zero.

## Repairs

### F-046 — cell 38

Attention is now explicitly the course's **chosen** operation, motivated by content-adaptive
pairwise routing, short paths to allowed sources, and position-parallel training. The text says
these are engineering advantages rather than a uniqueness theorem and names a full-receptive-
field causal convolution/global parallel mixer as a counterexample to uniqueness.

### F-047 — cells 76 and 82

- Cell 76 now separates AdamW's RMS adaptation from the first-step special case, gives the exact
  adaptive component `eta*g_1/(|g_1|+epsilon)`, states the required
  `g_1 != 0, |g_1| >> epsilon` condition, and retains epsilon plus decoupled decay.
- Cell 82 asks the learner to derive the exact moments and component, state that condition, analyze
  `|g_1| <= epsilon` and `g_1 = 0`, and then account for decay. It no longer supplies a false
  unconditional conclusion.
- Cell 49's already-correct masking equivalence was untouched.

## Red/green and execution evidence

- A claim-level regression check failed on i10 at all seven expected anchors: the two attention-
  selection strings, three unconditional AdamW strings, and two missing `|g_1| >> epsilon`
  conditions.
- The identical check passes on i11. The mathematical edge case
  `g_1=1e-12, epsilon=1e-8` gives an adaptive magnitude about `1e-4*eta`, exercising the condition.
- `nbformat.validate(product_i11)` passes.
- Fresh-kernel `nbclient`: 48/48 code cells, zero exceptions, 16 distinct embedded PNGs at the
  same cells as i10, and only the deliberate epsilon-zero LayerNorm warning in cell 58.
- Product-i11 SHA-256 after execution:
  `1902accaa9bfb1627182557552e5d3bd193b2ee2e2703dfeddfa11b4751162bf`.

## Pre-signoff hostile-gate correction

The first independent hostile pass found one i11-introduced CLAIM/MINOR: cell 38 said attention
provides a short path between “any receiver and source,” overlooking the causal mask. A new
regression check failed on that wording; the text now says “between each receiver and every
causally allowed source.” The check passes, and the notebook was executed and saved again. This
is recorded as F-051 and resolved before the formal i11 audit.

## Deliberate non-change

The A-2 mystery-thread objection remains below the CONTRACT finding bar and is not required for
signoff. Its advance notices are the strongest remaining editorial objection; changing them here
would exceed this repair's claim-correctness scope.

## Disposition

F-046, F-047, and F-051 are RESOLVED pending an independent regression audit of product i11. No
signoff is emitted by this rework step.
