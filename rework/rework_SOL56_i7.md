# Rework SOL56 i7 — product_i7 → product_i8 (unchanged)

No `ACCEPTED`, `OPEN`, or `CONTESTED` finding remains. I therefore made no notebook edit:
changing a clean product merely to create a new version would violate the prompt's minimality rule.
Immediately before materialization I independently executed product i7 in a fresh kernel with
`nbclient`: **47/47 code cells executed, 0 errors, all assertions passed**. Product i8 is a
byte-identical materialization of that already-executed notebook (SHA-256 for both:
`451d12fb06e1f9abe41ceff04b87c3f4faca780ee28319c5d0739c0957c32ec8`).

## Decision table

The ledger table retains historical `OPEN` row text by design; the append-only state log folds all
33 registered findings below to `FROZEN`. `KEEP FROZEN` is therefore the only valid no-change
decision. There is no silent drop.

| id | decision | where (product_i7) | one-line rationale |
|----|----------|--------------------|--------------------|
| F-001 | KEEP FROZEN | cell 0 / global substrate | The NumPy substrate remains executable and preserves the portable source content. |
| F-002 | KEEP FROZEN | cell 38 | The order claim is correctly limited to unmasked attention, with the causal-mask caveat. |
| F-003 | KEEP FROZEN | cell 44 | Projected values, output projection, residuals, and the MLP are distinguished correctly. |
| F-004 | KEEP FROZEN | cell 47 | Residual connections are presented as conditional aids, not gradient guarantees. |
| F-005 | KEEP FROZEN | cells 48, 55 | LayerNorm's domain, epsilon behavior, and limited stabilization claim remain correct. |
| F-006 | KEEP FROZEN | cells 8, 31, 53, 63, 93 | The accepted A-only rigor ports remain present and executable. |
| F-007 | KEEP FROZEN | product-wide claim repairs | Previously catalogued overclaims retain their required qualifiers. |
| F-008 | KEEP FROZEN | cells 63–64 | The held-out demo now exhibits and asserts the lesson its prose teaches. |
| F-009 | KEEP FROZEN | cell 13 | Softmax is motivated without the false claim that nonsmooth maps have no usable derivative. |
| F-010 | KEEP FROZEN | label-shift definition and uses | Shifted inputs/targets are defined before dependent references and code. |
| F-011 | KEEP FROZEN | bounded transformer training section | The trained parameter scope is explicit and the runnable check remains honest. |
| F-012 | KEEP FROZEN | learner self-checks throughout | Bounded derivation and interpretation checks remain integrated. |
| F-013 | KEEP FROZEN | framework/family mapping | Decoder-only GPT analogues are separated from encoder-decoder cross-attention APIs. |
| F-014 | KEEP FROZEN | entropy/KL section | The decomposition and conditional-entropy floor use the correct hypotheses. |
| F-015 | KEEP FROZEN | cells 100–101 | Affine calibration now exposes clipping, repairs coverage, and conditions the half-step bound. |
| F-016 | KEEP FROZEN | alternatives section | Retrieval, memory, and world-model boundaries retain qualified, testable framing. |
| F-017 | KEEP FROZEN | cross-entropy equivalence check | The claim is numerical equivalence within tolerance, not byte identity. |
| F-018 | KEEP FROZEN | Chapter 13 boundary map | The broader NLP task-family map and evidence-scope warning remain present. |
| F-019 | KEEP FROZEN | exact-digit worked examples | The agreed highest-value examples and AdamW precision remain restored. |
| F-020 | KEEP FROZEN | bounded training prose | It states which tied parameter group is updated rather than calling all groups trained. |
| F-021 | KEEP FROZEN | chapter dependency order | Definitions and derivations precede the code and claims that depend on them. |
| F-022 | KEEP FROZEN | quantizer calibration prose | Asymmetric min/max and symmetric max-absolute calibration are distinguished. |
| F-023 | KEEP FROZEN | Chapter 4 heading | Attention has the heading required by later cross-references and the chapter inventory. |
| F-024 | KEEP FROZEN | modern-systems map | Prompting, RAG, tools, memory, evaluation, and serving boundaries remain substantive. |
| F-025 | KEEP FROZEN | label-shift explanation | Masked in-window futures and the final outside-window target are stated separately. |
| F-026 | KEEP FROZEN | softmax-CE gradient derivation | `p-e_y` is scoped to one-hot CE and `p-q` to distributional targets. |
| F-027 | KEEP FROZEN | tying section | Coupled geometry, parameter saving, and scaling are explicitly derived. |
| F-028 | KEEP FROZEN | decoding section | Beam sequence search is distinguished from top-k/top-p sampling. |
| F-029 | KEEP FROZEN | cells 93, 96, 105–106, 121 | SFT generalization and direct pairwise preference supervision remain correctly separated. |
| F-030 | KEEP FROZEN | cells 16, 107 | Both optimizer calls check success and tolerance while narrowly handling the known warning. |
| F-031 | KEEP FROZEN | cell 100 | Interior zero-point is a feasibility condition; boundary rounding yields the correct infinite side constraint. |
| F-032 | KEEP FROZEN | cell 116 | All intended RAG arrows remain escaped LaTeX commands; no tab controls remain. |
| F-033 | KEEP FROZEN | cell 10 | The joint/conditional bijection has strict positivity and unreachable-prefix qualifications. |

## Concrete edits

None. There is no active finding to fix or reject, and no new claim was introduced.

## Materialization and signoff alignment

- Fresh-kernel execution gate: 47/47 code cells, 0 errors.
- `product/product_i8.ipynb` is byte-identical to `product/product_i7.ipynb`; this is the
  coordinator's required unchanged round, not a claim that i8 supersedes the audited artifact.
- Replaced SOL56's stale product-i6 signoff (which carried an F-031 waiver) with an independent,
  zero-waiver signature on product i7, matching OPUS48's audited-version signature.
- No finding status changes: all 33 remain `FROZEN`; none is `OPEN`, `ACCEPTED`, `CONTESTED`, or
  `REJECTED` in the folded ledger state.
