# Rework SOL56 i3 — product_i3 -> product_i4

Materialized `product/product_i4.ipynb` with the same 122 cells (47 code). The two active
findings are fixed without changing chapter structure or adding a new conceptual dependency.
Fresh-kernel `nbclient` execution completed **47/47 code cells with 0 exceptions**; an
independent top-to-bottom shared-namespace execution also completed 47/47. Both runs leave only
the deliberately demonstrated `epsilon=0` LayerNorm warning at cell 55.

## Decision table (every OPEN finding)

| id | decision | where (product_i4) | one-line rationale |
|----|----------|--------------------|--------------------|
| F-029 | FIX | cells 93, 96, 105–106, 121 | Replaced the replay-only premise with the precise distinction: token likelihood can generalize to unseen sequences, while ordinary SFT examples do not directly supply pairwise comparison labels. |
| F-030 | FIX | cells 16, 107 | Both constrained solvers now check `res.success`, assert agreement with the closed form, and narrowly suppress only SLSQP's harmless bound-clipping trial-step warning. |

All earlier non-rejected findings are RESOLVED/FROZEN; no settled cell was reopened.

## Concrete edits

### F-029 — cells 93, 96, 105–106, 121

- before: “imitation has a ceiling: it can only reproduce answers it was shown” and sibling
  claims that likelihood can only copy text/responses.
- after: “Masked token likelihood can learn from good responses and generalize beyond the exact
  answers shown. What it does **not directly consume** is a comparative label such as ‘answer A
  is better than answer B.’”
- propagation: the Chapter-9 bridge, Chapter-10 forced move, Chapter-11 opening, and Chapter-13
  recap now all use the same comparison-label distinction. The repaired Chapter-11 opening says
  explicitly that pretraining/SFT can generalize to sequences not shown verbatim and motivates
  preference optimization when comparisons are available.
- source basis: follows source A's defensible progression—learn which distribution to imitate,
  then ask whether good behavior is easier to compare than demonstrate—while preserving source
  B's break-to-repair motion.

### F-030 — cells 16 and 107

- before: each helper returned `res.x` without checking optimizer status; both committed output
  streams contained SLSQP bounds-clipping `RuntimeWarning`s, and the printed agreement had no
  executable tolerance assertion.
- after: each solver wraps only the known SLSQP clipping warning, raises `RuntimeError` unless
  `res.success`, and the caller asserts `np.allclose(numerical, closed_form, atol=1e-5)`.
- executed evidence: Chapter 1 maximum differences are `4.59e-08`, `2.10e-07`, and `5.97e-09`;
  Chapter 11 maximum differences are `8.60e-09`, `1.15e-07`, and `1.26e-07`. The saved outputs
  contain neither SLSQP warning; cell 55's deliberately elicited LayerNorm warning remains.

## New material for the iter-4 audit

Audit the revised alignment transitions at cells 93, 96, 105–106, and 121 for consistent scope.
Audit the new fail-closed solver guards and tolerance assertions at cells 16 and 107. No other
product cell source changed.

## LEDGER

- F-029 -> **RESOLVED** (next audit confirms -> FROZEN or re-OPEN).
- F-030 -> **RESOLVED** (next audit confirms -> FROZEN or re-OPEN).
- No REJECT-WITH-RATIONALE; nothing CONTESTED.
