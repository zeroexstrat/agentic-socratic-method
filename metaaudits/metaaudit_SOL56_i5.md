# Meta-audit SOL56 i5 — adjudicating audit_OPUS48_i5

**Overall verdict: REVISE (one MAJOR, one MINOR, one NIT).** OPUS48 correctly verifies the
repaired two-sided quantizer example and product i5 executes cleanly. Its sign-off audit is not
complete: Chapter 0 drops the strict-positivity condition required for its claimed
joint/conditional bijection; the newly added quantizer coverage formula omits its boundary
conditions; and an older RAG pipeline contains four broken arrow escapes.

Verification: I independently re-executed all 47 code cells in a fresh kernel (0 exceptions;
all assertions pass; only the deliberate cell-55 `epsilon=0` warning), diffed i4→i5 to confirm
only cells 100–101 changed, recomputed both quantizer grids, tested one-sided calibration edge
cases, scanned parsed cell sources for control characters, and checked the Chapter-0 theorem
against source A's precise proposition and a zero-mass-prefix counterexample.

## Findings OPUS48 raised

None new. There is therefore no new per-finding UPHELD/OVERTURNED/RECLASSIFIED disposition.

## Prior-resolution confirmation

### F-015 — confirmation UPHELD -> FROZEN

- reasoning: Cells 100–101 correctly expose the naive grid `[-8/7,6/7]`, identify `x=1` as
  clipped, restrict the original `s/2` assertion to non-clipped points, then hold `z=4` fixed
  and enlarge `s` to `1/3`. The repaired grid `[-4/3,1]` covers `[-1,1]`; no sample clips;
  every error is at most `1/6`, tight at `x=0.5`; and zero remains exact. The code asserts each
  premise rather than merely printing it. F-015 is correctly resolved on external truth and
  should remain FROZEN.

## Findings OPUS48 missed

### F-033 · MATH · MAJOR (missed by OPUS48)

- **loc:** cell 10 — “It is a bijection: knowing all the conditionals”
- **wrong:** The cell first defines outputs in the closed simplex, then says **any** full-sequence
  distribution is in bijection with all of its next-token conditionals. For a joint with a
  zero-probability prefix, the ratio defining the conditional on that prefix is undefined, and
  arbitrary choices on that unreachable branch all induce the same joint. Thus factorization
  still exists after choosing versions of the conditionals, but joint-to-*all-conditionals* is
  not one-to-one without a positivity condition.
- **correct:** Restore source A's theorem: strictly positive joints on `V^T` are in bijection
  with conditional families valued in the relative interior of the simplex. Alternatively,
  state the non-strict version only up to arbitrary choices on zero-mass prefixes and drop the
  bijection claim.
- **evidence:** Let `V={0,1}`, `T=2`, and put all joint mass on sequence `00`. Then
  `P(X1=1)=0`, so `P(X2 | X1=1)` is undefined by the ratio and may be assigned any distribution
  without changing the joint product (the branch is multiplied by `P(X1=1)=0`). Source A cell
  3, Proposition 0.4, explicitly restricts both sides to strict positivity and its self-check
  asks where that hypothesis is used; the merge dropped exactly that load-bearing condition.
  MAJOR fits CONTRACT §4: the central claim is correct in spirit but true only under an unstated
  condition. It is not BLOCKER because the later softmax model is strictly positive and the
  ordinary chain-rule factorization itself remains valid with suitable conditional versions.

### F-031 · MATH · MINOR (missed by OPUS48)

- **loc:** cell 100 — “the scale must satisfy”
- **wrong:** The displayed coverage formula divides by `z-qmin` and `qmax-z` without requiring
  `qmin < z < qmax` or defining the boundary cases. The paragraph presents it for the general
  range `[a,b']`, which includes ordinary one-sided ranges after zero extension. For an
  all-nonnegative range `[0,1]`, naive calibration gives `z=qmin=0`, so its first term is
  `-a/(z-qmin)=0/0`; for `[-1,0]`, `z=qmax=7` and its second term is `0/0`. The theorem is thus
  undefined in common cases even though the demonstrated two-sided case is correct.
- **correct:** State the formula under `qmin < z < qmax`. At a boundary, omit an inactive zero
  side (`a=0,z=qmin` or `b'=0,z=qmax`); if a nonzero side has zero available levels, coverage is
  impossible at finite scale. Handle the degenerate `[0,0]` range separately. Equivalently,
  define each coverage constraint piecewise rather than writing an unqualified quotient.
- **evidence:** With `qmin=0,qmax=7,[a,b']=[0,1]`, `s=1/7,z=0`; direct evaluation of the printed
  formula produces `max(0/0,1/7)`, while the actual needed lower-side constraint is vacuous and
  `s=1/7` covers the range. The symmetric `[-1,0]` case produces `max(1/7,0/0)`. This is MINOR:
  the `[-1,1]` derivation and code remain right, and one explicit domain qualifier resolves the
  general statement.

### F-032 · NOTE · NIT (missed by OPUS48)

- **loc:** cell 116 — “RAG composes retrieval with generation”
- **wrong:** Each intended `\to` in the five-stage RAG pipeline is stored as a literal tab
  character followed by `o` because `\t` was consumed as an escape. The rendered math therefore
  does not contain arrows.
- **correct:** Store literal LaTeX arrow commands (`\\to` at the JSON-serialized level), or use
  a notation that survives notebook serialization, so the pipeline renders
  `question -> retriever -> passages -> LM context -> answer`.
- **evidence:** Parsing product i5 finds four ASCII horizontal-tab characters (`ord=9`) in cell
  116 and no other non-newline control characters in the notebook. Source A's corresponding
  pipeline stores escaped `\\to` commands correctly. This is a localized notation NIT.

## Axis sweep beyond those findings

- **MATH:** F-033 and F-031. F-015's actual two-sided calculation, entropy/KL identities,
  attention scaling, parameter budget, optimizer checks, and DPO derivation remain correct.
- **CODE:** none. Fresh execution completed 47/47 with zero exceptions; the new clipping and
  coverage assertions test the conditions they claim.
- **CLAIM:** none. The SFT/preference, decoding, partial-training, KV-cache, and quantization-toy
  claims remain appropriately scoped.
- **FIDEL:** no additional finding. F-015 properly departs from an error shared by source A;
  F-032 restores rather than changes source A's intended pipeline notation.
- **PED:** no separate finding. F-033 is already logged on its primary mathematical axis; it is
  pedagogically material because the dropped hypothesis supports Chapter 0's central theorem.
  The quantizer break→repair sequence is now honest and its code follows the prose.
- **NOTE:** F-032. Other symbols and shapes are consistent.

## LEDGER disposition

- F-015 -> **FROZEN** (confirmation upheld).
- F-033 -> new **OPEN** MAJOR.
- F-031 -> new **OPEN** MINOR.
- F-032 -> new **OPEN** NIT.

OPUS48's product-i5 sign-off cannot complete convergence while F-033 is blocking and its
`minors_left_open: []` omits F-031. All three repairs are local and need not alter the notebook's
argument.
