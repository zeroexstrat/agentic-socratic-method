# Audit OPUS48 i1 — auditing product_i1 (my own iter-0 rework; role swap)

**Verdict: REVISE (one MINOR).** product_i1 executes top-to-bottom clean (all assertions
pass), the five iter-0 contradictions are gone — corrections now propagated to every sibling
cell — and the ported A-rigor checks out numerically. One new overstatement remains in the
end-to-end training claim. I confirm the iter-0 fixes and propose freezing them; I raise F-020.

## Verification performed
- Re-executed all code cells in a fresh kernel (nbclient): 0 exceptions; every `assert` passed.
- Re-checked each RESOLVED finding against product_i1 by anchor + output:
  held-out `start 1.367 → min 1.158 @ 88 → end 1.194` (F-006/F-008 assert the dip-and-rise);
  end-to-end training `1.4396 → 1.1393` (F-011); `H(q,p)=H(q)+KL` (F-014); quantizer
  `max|x−x̂|=0.1429=s/2` (F-015); LayerNorm C=2 `→ ±(1,−1)` (F-019); label shift (F-010).
- Grepped for the iter-0 overclaim phrasings: all removed from narrative cells; the only
  remaining "lossless recall" is the *corrected* negating usage ("not a 'lossless recall'
  guarantee by theorem"), and the SSM table row now reads "growing exact cache vs fixed state."

## Re-audit of the iter-0 rework (F-002 … F-019)

| finding | disposition | basis |
|---|---|---|
| F-002 | confirm → **FROZEN** | cell 39 now teaches unmasked-only equivariance + causal-mask caveat; no sibling contradicts. |
| F-003 | confirm → **FROZEN** | cell 34 scoped to single-head projected values; demo title/prints scoped to W_V=I; cell 38 consistent. |
| F-004 | confirm → **FROZEN** | cell 45 title/prose + cell 47 plot no longer promise a guaranteed identity route. |
| F-005 | confirm → **FROZEN** | cell 50 credits LN with sublayer-input statistics, not depth-scale bounding; consistent with the LN section. |
| F-006 | confirm → **FROZEN** | held-out section now backed by a run that demonstrates its lesson. |
| F-007 | confirm → **FROZEN** | cell 30 "differentiable random parameterization"; cell 88 print "direct loss term is 0"; cell 111 table fixed. |
| F-008 | confirm → **FROZEN** | new demo asserts `0<argmin<end`, `val[min]<val[0]`, `val[-1]>val[min]`; verified. |
| F-009 | confirm → **FROZEN** | cell 13 now allows subgradients (ReLU); no false universal. |
| F-010 | confirm → **FROZEN** | label shift defined in Ch6 (cell 64); the "shifted labels" references resolve. |
| F-012 | confirm → **FROZEN** | portable self-checks added at Ch1/Ch6; consistent with §3 (99c's pedagogy kept). |
| F-013 | confirm → **FROZEN** | cell 90 names GPT2Block as the decoder-only match; flags TransformerDecoderLayer's cross-attention. |
| F-014 | confirm → **FROZEN** | KL/entropy-floor restored + numeric check (cells 24–25). |
| F-015 | confirm → **FROZEN** | affine quantizer + tight half-step bound restored + asserted (cells 97–98). |
| F-016 | confirm → **FROZEN** | reading rubric + retrieval/world-model directions restored (cell 112). |
| F-017 | confirm → **FROZEN** | "byte-for-byte" → "numerically equal to fp tolerance"; `np.allclose` + honest note. |
| F-018 | confirm → **FROZEN** | portable NLP task-family map + warning restored (cell 116). |
| F-019 | confirm → **FROZEN** | WE 5.1 (LN C=2) and AdamW statement restored, at the agreed scope. |
| F-011 | confirm partial → **hold RESOLVED** | the fix works but the claim it backs is still slightly overstated — see F-020. Freeze only once F-020 lands. |

## New finding

### F-020 · CLAIM · MINOR
- loc: cell 60 — "the model it calls 'trained' is trained" / cell (close) — "trained end to end by gradient descent below"
- wrong: The bounded end-to-end training updates **only the tied `W_E`**; the attention, MLP, and LayerNorm parameters in every block remain at random initialization. So "trained end to end" overstates what the demo does — it trains one parameter group (whose gradient does flow through every block), not the whole model.
- correct: Say the demo **trains the tied embedding end-to-end** — its gradient propagates through every block — and that the remaining parameter groups would train by the identical `p − e_y` signal carried by backprop (Ch 6); do not imply all parameters were updated. One-line qualification in cell 60's print and the closing.
- evidence: cell 60 perturbs only `trained["W_E"]`; `trained["blocks"]` are copied unchanged. This is the same class of overclaim the loop has been catching (a demo's caption outrunning what the code did), now on my own rework — hence MINOR, not waved away.

## Axis coverage
- **MATH:** none new. Re-derived the restored items (KL decomposition, √D variance, half-step
  bound, LN geometry) against the code outputs; all correct.
- **CODE:** none new. All cells execute clean in a fresh kernel; every assertion passes; the
  finite-difference training is O(64·2·20) forward passes, bounded and fast.
- **CLAIM:** F-020 (above).
- **FIDEL:** none new. The A-only items flagged in iter 0 (KL, quantizer bound, worked
  examples, label shift, AdamW) are now present at the agreed scope; no correct source content
  remains dropped beyond what F-019 already scoped and resolved.
- **PED:** none new. The break→repair flow is intact and the added self-checks/worked examples
  reinforce rather than interrupt it.
- **NOTE:** none new. The dangling "Chapter 3 shifted labels" reference is resolved; symbol
  usage is consistent across the new cells.

## Signoff
Not emitted: F-020 is an open (minor) overstatement I just raised, so the artifact is not yet
one I can affirm without reservation. It is a one-line qualification for the iter-1 steward.
Ranking: F-020 (MINOR) is the only open item; no BLOCKER/MAJOR remains open.
