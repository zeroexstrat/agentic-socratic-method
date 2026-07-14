# Meta-audit SOL56 i3 — adjudicating audit_OPUS48_i3

**Overall verdict: REVISE.** OPUS48 raised no new finding to adjudicate, and its confirmation of
F-025–F-028 is correct: those four repairs are stable. Its clean-sign-off conclusion is not.
The audit missed a repeated false premise in the course's alignment argument and incorrectly
reported that the deliberate LayerNorm demonstration was the notebook's only warning.

Verification: I re-executed all 47 code cells top-to-bottom in a fresh shared namespace (0
exceptions; all assertions passed), recomputed the parameter budget, and checked the changed
label-shift, cross-entropy, weight-tying, and beam-search sections against both sources. I also
inspected the notebook's saved streams: cells 16 and 107 contain SLSQP `RuntimeWarning`s in
addition to cell 55's deliberate `epsilon=0` warning.

## Findings OPUS48 raised

None. There is therefore no new per-finding UPHELD/OVERTURNED/RECLASSIFIED disposition.

## Prior-resolution confirmations in OPUS48's audit

- **F-025 remains FROZEN.** Cell 35 now distinguishes the interior target that is present at
  input position `t+1` from the final target outside `x`; its Python and mathematical indexing
  are consistent.
- **F-026 remains FROZEN.** Cell 22 limits `p-e_y` to one-hot token cross-entropy, states the
  soft-target result `p-q`, and explicitly separates DPO.
- **F-027 remains FROZEN.** Cells 65–66 correctly derive `z_i=<h,E(i)>`. The computed budget is
  64 token-embedding + 128 position-embedding + 6432 block + 32 final-LN = 6656 parameters;
  an otherwise identical untied, bias-free head adds `V*C=64`.
- **F-028 remains FROZEN.** Cell 85 correctly distinguishes accumulated-log-probability
  sequence search from one-step distribution reshaping/sampling. “About K times” is an
  acceptable bounded compute approximation here.

## Findings OPUS48 missed

### F-029 · CLAIM · MAJOR (missed by OPUS48)

- **loc:** cell 93 — “it can only reproduce answers it was shown”
- **wrong:** Maximum-likelihood/SFT models are not restricted to replaying observed responses.
  They assign probabilities compositionally and can generalize to novel sequences. The same
  false bridge recurs in cell 96 (“reproduce text and shown responses”), cell 106 (“hard
  ceiling”), and cell 121 (“imitation forced alignment”). It also contradicts the notebook's
  own Chapter-6 held-out-generalization lesson. Preference pairs are a different *training
  signal*, but that does not make sequence likelihood incapable of novel output or preference-
  shaped behavior through curated/reweighted demonstrations.
- **correct:** Say token NLL directly learns from observed continuations and can generalize to
  unseen responses; SFT does not directly consume pairwise comparison labels. Preference
  optimization is useful when relative judgments are easier or more informative than writing
  target demonstrations, and it directly trains on those comparisons. Propagate that precise
  distinction through cells 93, 96, 105–106, and 121.
- **evidence:** Product cells 74–78 explicitly distinguish generalization from memorization and
  test it on held-out data, so the later replay-only premise is internally inconsistent. Source
  A cells 69, 74, and 86 use the defensible formulation—learning which distribution to imitate,
  then asking whether good behavior is easier to compare than demonstrate—without claiming
  outputs are confined to the training responses. This is MAJOR because the false premise is
  repeated as the forced pedagogical reason alignment must exist, not used once as loose prose.

### F-030 · CODE · MINOR (missed by OPUS48)

- **loc:** cell 16 — `res = minimize(... method='SLSQP' ...)`
- **wrong:** The max-entropy “verification” returns `res.x` without checking `res.success`, and
  its saved output emits an unexplained bounds-clipping `RuntimeWarning`; the same pattern and
  warning recur in cell 107. OPUS48's claim that cell 55's deliberate LayerNorm warning is the
  only warning is factually false. Current numerical answers happen to agree, so this is not a
  failed derivation or a MAJOR.
- **correct:** Check optimizer success, assert the numerical/closed-form tolerance, and either
  use a stable simplex parameterization or narrowly handle the known harmless SLSQP clipping
  warning. Apply the same repair to both solver cells; leave the deliberately demonstrated
  LayerNorm warning labeled.
- **evidence:** The committed notebook streams at cells 16 and 107 both contain `RuntimeWarning:
  Values in x were outside bounds during a minimize step, clipping to bounds`; an independent
  47/47 execution reproduced them. Neither solver currently asserts success.

## Axis sweep beyond those findings

- **MATH:** no additional issue found. The four new repairs, entropy/KL floor, attention
  scaling, quantizer bound, and Gibbs derivations check out.
- **CODE:** F-030. Apart from those warning/self-check sites and the labeled cell-55 warning,
  47/47 cells execute and their assertions pass.
- **CLAIM:** F-029. The changed `p-e_y`, tying, and beam claims are properly bounded.
- **FIDEL:** F-029 is inherited from source B while source A supplies the sounder alignment
  transition. OPUS48's acknowledged unported exact-digit attention/AdamW examples remain the
  already-adjudicated scope of frozen F-019, so I do not duplicate that finding without new
  evidence.
- **PED:** F-029 is pedagogically material because it is the Chapter-11 forced move. Otherwise
  the repaired definitions precede their dependent demonstrations.
- **NOTE:** no new notation issue found.

## LEDGER disposition

- F-025, F-026, F-027, F-028: confirmation stands; remain **FROZEN**.
- F-029: new **OPEN** MAJOR.
- F-030: new **OPEN** MINOR.

OPUS48's `product_i3` sign-off cannot satisfy convergence while F-029 is open. A later sign-off
must name the repaired product version after a zero-change audit round.
