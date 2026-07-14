# Rework SOL56 i5 — product_i5 -> product_i6

Materialized `product/product_i6.ipynb` with the same 122 cells (47 code). Three local fixes
resolve every active finding; no chapter order or executable mechanism changed. Fresh-kernel
`nbclient` execution and an independent shared-namespace execution each completed **47/47 code
cells with 0 exceptions**. Both leave only the deliberately demonstrated cell-55 `epsilon=0`
LayerNorm warning.

## Decision table (every OPEN finding)

| id | decision | where (product_i6) | one-line rationale |
|----|----------|--------------------|--------------------|
| F-033 | FIX | cell 10 | Restored the strict-positive joint/conditional bijection, stated what fails on zero-mass prefixes, and separated chain-rule sufficiency from parameter-sharing generalization. |
| F-031 | FIX | cell 100 | Replaced the unqualified quotient with piecewise lower/upper coverage constraints that handle boundary zero-points and the degenerate zero range without `0/0`. |
| F-032 | FIX | cell 116 | Replaced four parsed tab-plus-`o` sequences with literal LaTeX `\to` commands. |

All earlier non-rejected findings are RESOLVED/FROZEN; no settled result was reopened.

## Concrete edits

### F-033 — cell 10

- before: the model codomain was the closed simplex and the text claimed that **any** sequence
  distribution was in bijection with all next-token conditionals, without addressing
  zero-probability prefixes.
- after: the course's finite-logit softmax model maps into the relative interior
  `mathring(Delta)`. For fixed `T`, the text states the bijection between strictly positive
  joints and strictly positive conditional families, explains why positivity makes every
  prefix denominator nonzero, and records the non-strict caveat: conditionals on unreachable
  branches are arbitrary, so a joint with zeros does not determine them uniquely.
- reasoning propagation: the final clause now says the chain rule makes conditionals sufficient
  to specify the joint, while parameter sharing makes transfer across prefixes *possible but
  does not guarantee generalization*. This removes the adjacent implication that factorization
  proves a finite shared model generalizes.
- source basis: restores source A cell 3's load-bearing strict-positivity hypothesis while
  retaining source B's compact narrative progression.

### F-031 — cell 100

- before: `s >= max(-a/(z-qmin), b'/(qmax-z))` was presented without a domain, producing `0/0`
  for `[0,1]` with `z=qmin` and for `[-1,0]` with `z=qmax`.
- after: piecewise constraints `c_-` and `c_+` assign zero to an inactive zero-valued side,
  use the quotient only when levels exist on that side, and assign `+infinity` when a nonzero
  side has no available levels. Coverage is `s >= max(c_-,c_+)`; the familiar quotient is shown
  only for a nondegenerate two-sided range with an interior zero-point. `[0,0]` explicitly takes
  any separately chosen `s>0`.
- unchanged example: the executable `[-1,1]`, `z=4` break→repair remains exactly as verified in
  i5; F-031 changes only the general theorem's edge conditions.

### F-032 — cell 116

- before: the parsed source contained four ASCII horizontal tabs followed by `o`, so the RAG
  chain did not contain valid arrow commands.
- after: all four separators are literal `\to` commands in the parsed markdown source. A full
  control-character scan finds no non-newline controls anywhere in product i6.

## New material for the iter-6 audit

Audit cell 10's strict-positive theorem and zero-mass-prefix caveat, including the distinction
between representational sufficiency and generalization. Audit cell 100's piecewise boundary
constraints. Confirm cell 116 parses with four literal `\to` commands. These are the only source
cells changed from i5.

## LEDGER

- F-033 -> **RESOLVED** (next audit confirms -> FROZEN or re-OPEN).
- F-031 -> **RESOLVED** (next audit confirms -> FROZEN or re-OPEN).
- F-032 -> **RESOLVED** (next audit confirms -> FROZEN or re-OPEN).
- No REJECT-WITH-RATIONALE; nothing CONTESTED.
