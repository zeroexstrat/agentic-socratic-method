# Rework FABLE5 i8 — product_i7 → product_i9 (recomposition charter)

**Charter (HUMAN-sanctioned):** re-compose prose and structure for pedagogical movement;
**no claim may change strength in either direction**; every FROZEN fix survives
verbatim-or-stronger; both models regression-audit product_i9 before any new signoff.

**Result:** product_i9.ipynb — 128 cells (48 code), fresh-kernel nbclient execution
48/48, zero exceptions, all assertions pass, only the deliberate ε=0 LayerNorm warning.

---

## Findings resolved (F-034…F-044 = audit P-001…P-011)

| finding | change in i9 |
|---|---|
| F-034 | cell 0: "self-contained" → "in one shared kernel, top to bottom" (now consistent with the F-007 caveat cell). |
| F-035 | Ch-6 self-checks moved after the held-out demo; check (c) retargeted from tokenizer-perplexity (Ch-7 material) to AdamW first-step scale-invariance (Ch-6 material). |
| F-036 | `ce_vectorized`: dead `.max(1)*0` deleted; comment explains the shift cancels in `-Z_y + logsumexp(Z)`. Executed equal to the loop version. |
| F-037 | New type-reconciliation paragraph in the assembly cell: model type (prefix ↦ one distribution) vs network type (𝒱^T → (Δ)^T), row *t* = the Chapter-0 map at prefix x_{1:t}; pooling's retirement made explicit; generation reads the last row. |
| F-038 | Ch-8 forced move now names the Ch-9/Ch-10 detour at the point of promise; preference-signal claims verbatim. |
| F-039 | Ch-3 reordered: label shifting ("plumbing while the machine still looks finished") now precedes the bag-model break; new two-line bridge; chapter ends on the cliffhanger. F-021's definitions-before-use strengthened, not weakened. |
| F-040 | Single endings for Ch 1, 5, 6: forced moves relocated verbatim to true chapter ends (after self-checks / parameter budget / held-out demo). Cell 60 became a segue into the executable assembly. |
| F-041 | "exactly the shifted labels of Chapter 3 consume" — deduplicated with cell 61's correct sentence. |
| F-042 | New 3-line code cell executes the `KeyError` on `'b'`; prose updated to point at the run. Ch 2 now honors the cell-0 method promise. |
| F-043 | All reader-facing provenance stripped (cells 9, 23, 35, 36, 57, 73, 96, 120); the cell-96 editorial aside deleted; disclosure remains in cell 0 + colophon only. |
| F-044 | Cell 42 leans to setup + prediction ("watch the symmetry hold, then shatter"); the full strength-scoping, proof, Haviv citation, and both caveats live once, verbatim, in cell 44. |

## Advisory items implemented (A-1…A-5)

- **A-1 sediment recomposition** — lesson-first rewrites, all scoped claims retained:
  - cell 76: trajectory lesson leads; ignorance-not-transfer, infinite-loss escape,
    overfitting-as-divergence, factorization caveat, bottleneck remark all present.
  - cell 53: correct residual statement first (incl. the "arbitrary hundred-layer"
    clause), counterexamples second, demo-scoping third; ODE reading and the LN hazard
    hand-off verbatim.
  - cell 110: the β=4 numbers folded into a single correctly-scoped sentence
    (no claim-then-retraction); DPO note untouched.
  - cell 105: intuition first; new train-set-vs-held-out lesson sentence (representation
    damage, not generalization); the "Do **not** read this curve as…" list verbatim.
  - cell 10: F-033 fine print marked as fine print ("safe to skim; the punchline is: no");
    text unchanged.
- **A-2 despoiling** — Ch 4 no longer announces Chapter 11 or the third scale
  ("it is not done returning… two scales so far. Keep watching."); Ch 8's tease reduced
  to "returns for the last time"; the Ch 11 reveal and three-scale table unchanged.
- **A-3 self-checks** — new blocks for Ch 0 (zero-factor, perplexity-by-hand, smoothing
  vs sharing), Ch 4 (softmax/permutation commutation, −∞-before-softmax, hull), Ch 5
  (C=2 by hand, J=−I, C divisible by H), Ch 10 (repaired-grid coverage, lemma domain,
  outlier rows). Total self-check blocks: 6.
- **A-4 consolidation** — thirteen "**Where we stand.**" beats, one per chapter end,
  fused with the existing forced moves (evolving one-sentence definition of the machine;
  Ch 11's "Where this leaves us" renamed to match).
- **A-5 felt break in Ch 10** — cell 98 now scores the Chapter-7 bigram before/after
  quantization (full 2.349 → 3-bit 2.391 → 1-bit 2.503 on execution); wording matched
  to the observed *modest* magnitude, pointing to the chapter's closing sweep for where
  modest turns sharp. Train-set-perplexity confession converted to a lesson (cell 105).

## Charter-compliance verification (transcript)

Frozen-anchor sweep on product_i9 — all present:
F-002 ("Haviv et al., 2022"), F-003 ("not by the MLP alone"), F-004 ("gives $I+J_f=0$…"),
F-005 ("maps to $\mathbf 0$, not to radius"), F-008 (`assert va[vmin] < va[0]`),
F-015 ("equals s/2 only by coincidence"), F-025 ("final t = T-1"),
F-026 ("generalizes to $p-q$"), F-029 ("generalize beyond the exact answers shown"),
F-030 (`raise RuntimeError(f"SLSQP failed`), F-031 ("move $z$ inward and recompute $s$"),
F-033 ("strictly positive** distribution over full sequences").
Provenance strings ("ported from source A", "derivations-first source", "the original
text", the cell-96 aside): zero occurrences.

Execution: nbclient, fresh kernel, 48/48 code cells, 0 errors, all assertions pass.

## What was deliberately NOT done

- No claim re-scoped, strengthened, or weakened; no new mathematical content.
- Cell 50's "the sloppy version is false" framing kept — it names a live misconception
  once, which is teaching, not scar tissue.
- The i7 signoffs were not touched; product_i9 awaits both models' regression audit.

— FABLE5, iteration-8 rework under HUMAN sanction
