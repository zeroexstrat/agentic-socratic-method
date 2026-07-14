# Meta-audit OPUS48 i6 — adjudicating audit_SOL56_i6

**Overall:** SOL56's audit is correct. I concur that F-032 and F-033 are properly fixed →
FROZEN, and I uphold its re-open of F-031 (MINOR) — verified independently. F-031 is the sole
remaining item, and it is a genuine (if minor) false implication, so I will FIX it in my rework
rather than converge on a waived-wrong sentence. Note: SOL56 raised F-031/F-032/F-033 against my
product_i5 — three things my iter-5 audit missed. The independent second reader keeps earning
its place.

## Re-audit disposition (SOL56's iter-6 audit)

### F-033 — verdict: UPHELD → FROZEN (concur)
- reasoning: Cell 10 now maps the finite-logit softmax model into the open simplex and states the
  chain-rule bijection only between *strictly positive* joints and strictly positive conditional
  families, with the caveat that a joint with zeros leaves conditionals on zero-mass prefixes
  arbitrary. It also separates "conditionals suffice to specify the joint" (chain rule) from
  "shared parameters enable transfer" (not a generalization guarantee). Correct. Freeze.

### F-032 — verdict: UPHELD → FROZEN (concur)
- reasoning: A notebook-wide scan finds zero non-newline control characters; the `\to` commands
  in the Ch-13 map render correctly. Freeze.

### F-031 — verdict: UPHELD → ACCEPTED (MATH / MINOR)
- reasoning: Verified independently. On an unsigned 3-bit grid with `[a,b']=[-0.001, 1]`, the
  naive `s=1.001/7≈0.143` gives `z=round(0.00699)=0=qmin` — the range is nondegenerate and
  two-sided, yet the rounded zero-point lands on the boundary. So cell 100's sentence "For a
  nondegenerate two-sided range, `qmin<z<qmax`" presents an interior zero-point as automatic when
  it is actually a feasibility condition (the piecewise `c_-/c_+` correctly returns `+∞` on the
  uncovered side). MINOR is right — the formula, the `[-1,1]` example, and all code are correct;
  only the explanatory implication is off. I will apply SOL56's suggested wording.

## Findings SOL56 missed — none
SOL56's audit is accurate and self-critical (it re-opened its own iter-5 sentence). Per axis:
MATH — F-031 only; CODE — none (47/47 execute); CLAIM/FIDEL/PED/NOTE — none, the F-032/F-033
repairs restored the load-bearing content and the rest is unchanged from already-audited product.

## For the rework turn (mine, iter 6)
One-sentence fix to cell 100: change "For a nondegenerate two-sided range, `qmin<z<qmax` and this
reduces to …" to "If fixed-`z` coverage of a nondegenerate two-sided range is feasible, then
`qmin<z<qmax` and this reduces to …; if the rounded `z` lands on a boundary (a highly asymmetric
range can force this), `c_-` or `c_+` is `+∞` — no fixed-`z` scale covers that side, so move `z`
inward and recompute `s`." Then re-execute, re-audit, and re-sign on the fixed version so
convergence needs no MINOR waiver.

## LEDGER
- F-032, F-033 → FROZEN (concur). F-031 → ACCEPTED (re-opened, upheld, MINOR).
