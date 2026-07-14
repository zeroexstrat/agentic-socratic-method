# Rework FABLE5 i9 — product_i9 → product_i10 (responding to audit_SOL56_i9)

**Meta-position first: SOL56's audit is accepted in full, without contest.** Every
reclassification of audit_FABLE5_i7 is the contract read correctly (P-005/006/007/011 were
movement preferences I should have labeled advisory from the start; P-004's real defect was
the forced-attention inference, which SOL56 upgraded into F-046). Every new finding was
verified independently before this rework: the Agg count (16 `plt.show()`, 0 embedded
figures), all three F-007 sibling strings, both F-047 false premises. Two of the MAJORs —
F-048 and F-047 — are defects *I introduced* while fixing composition, which is precisely why
the charter routed my rework back through the two-model loop. The system worked.

**Result:** product_i10.ipynb — 128 cells, 48 code; fresh-kernel nbclient 48/48, zero
exceptions, **16/16 figures embedded**; 12/12 critical frozen anchors verified present.

## Resolutions

| finding | repair in i10 |
|---|---|
| **F-007 (reopen)** | "by necessity, not convention" → "unique answer to the score-plus-entropy question, and unique only for that question"; "the *only* principled way" → "a principled way … unique for its score-plus-entropy objective"; char comment → "no OOV *within its fixed inventory* (the break two cells down…)"; legend → "untrained near-uniform baseline". |
| **F-045** | Forced `matplotlib.use("Agg")` removed from cell 1; the kernel's inline backend (headless-safe) embeds every figure. Execution shows 16 image outputs. |
| **F-046** | The Ch-3 break now claims only its two *requirements* (content-dependence, asymmetry); recurrence and convolution named as alternatives that also deliver them; attention selected by the additional direct-access and train-time-parallelism demands. The "only principled way" softmax echo fixed under F-007. |
| **F-047** | Ch-4 (b): now asks to *prove the equivalence* of −∞-before-softmax with zero-after-plus-renormalize, and what breaks without renormalization. Ch-6 (c): bias corrections stated as making the *moment estimates* exact; step is η·g/(|g|+ε) ≈ ±η, with ε and decoupled λθ named as why "approximately". |
| **F-048** | Every consolidation beat scoped to its demonstrated object: "next-token probability" (Ch 2); "training discipline … exercised on the factorized bigram; the assembled transformer trained one tied group" (Ch 6); "a trained model speaks — the bigram, here" (Ch 7); "recipe on the table … no instruction model is trained in this course" (Ch 8); "weights (here, the trained bigram's)" + "transformer cache … counted" (Ch 10); final beat inventories the separate toys instead of one machine (Ch 12). |
| **F-049** | The bit-width sweep now also computes KL(p_full‖p_quant) averaged over contexts (executed: 0.0000 / 0.0009 / 0.0348 / 0.0713 nats for 8/4/2/1 bits). The yardstick paragraph rewritten as three instruments: paired in-sample sanity check (target NLL), belief fidelity (the KL column), deployment quality (held-out only). |
| **F-050** | Universal rhythm scoped in all three locations (cell 0 method, Ch-13 practice cell, colophon): "the build chapters," with Chapters 9 and 13 named as deliberate, self-flagging exceptions. |
| **A-2 residue** | "returns for the last time" removed from the Ch-8 and Ch-10 forced moves ("returns" / "walks on stage one more time — next"); the Ch-11 reveal, boxed Gibbs optimum, and three-scale table untouched. |

## Verification transcript

- `nbclient` fresh kernel: 48/48 code cells, 0 errors, all assertions pass.
- Embedded figures: 16/16 (`display_data` with `image/png`).
- F-007 sibling strings and F-047 premise strings: 0 occurrences.
- Frozen-anchor sweep (F-002/003/004/005/008/015/025/026/029/030/031/033): 12/12 present.
- New-repair anchors (recurrence/convolution counterexample, no-instruction-model scoping,
  KL column, three-instruments paragraph, build-chapter scoping, bigram scoping in beats):
  all present.

## Disposition

product_i10 awaits regression audits by OPUS48 and SOL56 under the recomposition charter.
No FABLE5 signoff attaches now or later — the reworker does not certify its own rework.

— FABLE5, iteration-9 rework under HUMAN sanction
