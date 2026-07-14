# Audit OPUS48 i3 — auditing product_i3 (my iter-2 rework; role swap)

**Verdict: SIGN-OFF.** product_i3 executes clean (47 code cells, 0 exceptions), the four iter-2
fixes landed correctly and introduced no contradictions, and after a section-by-section pass I
find no new BLOCKER or MAJOR. I confirm F-025–F-028 as stable → FROZEN and emit
`signoff/SIGNOFF_OPUS48.md`. Convergence still requires SOL56's independent signoff on this same
version.

## Verification performed
- Re-executed all cells in a fresh kernel: 0 exceptions; all assertions pass.
- Re-checked each iter-2 fix against its cell and output.

## Re-audit of the iter-2 fixes (F-025 … F-028)

| finding | disposition | basis |
|---|---|---|
| F-025 | confirm → **FROZEN** | cell 35 now prints both cases: interior `t<T-1` target at future input pos `t+1` (masked); final `t=T-1` target `ids[T]` dropped by `x=ids[:-1]`, not in the input. Output shows it. |
| F-026 | confirm → **FROZEN** | cell 22 scopes `p−e_y` to one-hot softmax CE, adds the distributional `p−q`, and reconciles with the DPO objective (cell 107) — the cross-cell contradiction is gone. |
| F-027 | confirm → **FROZEN** | cells 65–66 restore `z_i=⟨h,E(i)⟩` (head = log-linear model in embedding geometry) and a parameter-group budget; the count checks out (W_E 64, W_P 128, 2 blocks 6432, final LN 32, total 6656; tying saves V·C=64). |
| F-028 | confirm → **FROZEN** | cell 85 adds the beam-search scoring recursion and the sequence-search-vs-simplex-reshaping distinction; correctly placed before evaluation. |

## New findings — none
This is a checked conclusion. I scrutinized the newly added/edited cells hardest (the tying
derivation + parameter budget, the beam paragraph, the scoped `p−e_y`, the two-case label
shift) since they are the freshest surface area.
- **MATH:** none. The tying identity `z_i=⟨h,E(i)⟩`, the `p−q` generalization, and the
  parameter arithmetic are correct; the entropy-floor, √D-variance, half-step-bound, and
  attention max-entropy checks still hold.
- **CODE:** none. 47/47 cells execute; the parameter-budget numbers are computed from the
  assembled `gpt`, not asserted; the only warning remains the deliberate ε=0 LayerNorm demo.
- **CLAIM:** none. The previously over-universal `p−e_y` is now scoped; greedy/temperature,
  KV-cache O(T²), quantization-toy, and DPO claims are all correctly bounded.
- **FIDEL:** none blocking. The remaining un-ported source-A items are exact-digit Worked
  Examples 4.1 (one attention head over "cat") and 6.1 (one AdamW step); these are enrichment
  within F-019's agreed scope and are below the blocking bar (the attention and AdamW mechanics
  are present and numerically checked elsewhere). Noted as my strongest remaining objection.
- **PED:** none. Definitions precede demonstrations; the break→repair flow and the Gibbs
  three-scale thread are intact and now include the head-scale (tying) member explicitly.
- **NOTE:** none. Chapter numbering, references, symbols, and shapes are internally consistent.

## Signoff
Emitted (`signoff/SIGNOFF_OPUS48.md`, version product_i3). Strongest remaining objection: the
exact-digit Worked Examples 4.1 and 6.1 remain unported — the least-satisfying part, judged
below the BLOCKER/MAJOR bar. No MINOR left OPEN (all findings FROZEN). Termination remains the
harness's call, contingent on SOL56 independently signing the same unchanged version.
