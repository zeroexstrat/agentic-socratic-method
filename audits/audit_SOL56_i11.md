# Regression audit SOL56 i11 — final signoff gate

**Overall verdict: PASS at the CONTRACT bar; zero-waiver SOL56 signoff.** Product i11 repairs
F-046 and F-047 without changing code or disturbing the two-source merge. A hostile pre-signoff
pass found one new causal-scope MINOR (F-051); it was reproduced, repaired, re-executed, and then
rechecked on the final artifact. F-046, F-047, and F-051 are stable and can be FROZEN.

This audit follows the HUMAN-directed single-model repair loop. To avoid self-certifying the
rework, the final SHA was independently checked by separate math/pedagogy, notebook-integrity,
and hostile six-axis reviewers. This is a SOL56 signoff only; it does not fabricate OPUS48's
agreement or alter the historical product-i7 `coord/STOP`.

## Final artifact and execution

- artifact: `product/product_i11.ipynb`
- SHA-256: `1902accaa9bfb1627182557552e5d3bd193b2ee2e2703dfeddfa11b4751162bf`
- structure: 128 cells = 80 markdown + 48 code; all stable IDs are unique and retain i10 order
- exact source diff from i10: markdown cells `38`, `76`, and `82`; no code source changed
- `nbformat.validate`: pass
- independent cleared-kernel execution: 48/48 sequential counts, zero exceptions/errors
- figures: 16 distinct PNGs at cells
  `18, 52, 55, 62, 73, 75, 78, 81, 88, 93, 97, 103, 109, 115, 118, 120`
- warning inventory: only the deliberate epsilon-zero LayerNorm `RuntimeWarning` at cell 58
- frozen-anchor sweep: 12/12 stable (F-002/003/004/005/008/015/025/026/029/030/031/033)
- KL outputs preserved at cell 109:
  `0.0000 / 0.0009 / 0.0348 / 0.0713` nats for 8/4/2/1 bits

## Resolution audit

| finding | final disposition | evidence |
|---|---|---|
| F-046 | **confirm → FROZEN** | Cell 38 calls attention the course's chosen content-adaptive parallel mechanism, not a uniquely forced one. It explicitly retains a full-receptive-field causal convolution/global mixer as a counterexample to uniqueness. |
| F-047 | **confirm → FROZEN** | Cell 76 gives the exact first-step adaptive component and conditions the sign-step approximation on nonzero `|g_1| >> epsilon`; cell 82 makes the learner derive that condition and cover zero/near-zero gradients plus decay. Cell 49's masking equivalence remains correct. |
| F-051 | **confirm → FROZEN** | Cell 38 now says the short path runs between each receiver and every **causally allowed** source, so future masked positions are not included. The old overbroad string is absent. |

## Independent reasoning checks

For F-046, a full-support causal convolution
$y_t=\sum_{d=0}^{t}K_d x_{t-d}$ is order-sensitive, directly depends on every earlier input,
and computes all positions in parallel. That counterexample survives in the final explanation,
so the prose no longer derives attention by false necessity.

For F-047, from $m_0=v_0=0$,

$$
\hat m_1=g_1,\qquad \hat v_1=g_1^2,\qquad
u_1=\eta\frac{g_1}{|g_1|+\varepsilon}.
$$

Thus $u_1=0$ at $g_1=0$, has magnitude about $10^{-4}\eta$ at
$g_1=10^{-12},\varepsilon=10^{-8}$, and approaches a sign step only when
$|g_1|\gg\varepsilon$. The final cells state exactly that and retain the separate decay term.

## Axis coverage

- **MATH: none found.** The changed AdamW identity, limiting condition, edge cases, and decay
  distinction were independently re-derived and agree with the written self-check.
- **CODE: none found.** Three cleared-kernel final-SHA runs completed 48/48 without errors and
  reproduced all expected figures and numerical outputs.
- **CLAIM: none found.** Attention is presented as an engineering choice, the causal direct-path
  scope is explicit, and no universal selection claim remains.
- **FIDEL: none found.** No source content or code was removed; external truth correctly narrows
  the source notebooks' attention and AdamW overclaims.
- **PED: none found.** The forced move no longer teaches false necessity, and the AdamW self-check
  now makes the crucial approximation condition something the learner must state and test.
- **NOTE: none found.** Symbols, cell IDs, cross-references, and the changed cells' notation remain
  consistent; the Python-version metadata update merely records the executing kernel.

## Remaining advisory objection

Cells 49/98/111 still announce the later Gibbs return before Chapter 11. That weakens the intended
reveal and is the first editorial change I would make next. It is not a blocker or open MINOR:
the notices are technically accurate, introduce no false premise, and movement/spoiler preference
is outside CONTRACT §3.

## Signoff disposition

SOL56 signs product i11 with no open MINOR waiver. All effective ledger findings are FROZEN after
this audit. The historical OPUS48 signature still names product i7, so the two-model convergence
predicate remains unsatisfied unless OPUS48 independently audits and signs this exact i11 SHA.
