# CONTRACT — frozen evaluation contract

**Status: FROZEN.** Human-authored. Neither model may edit this file. All audits,
meta-audits, and rework decisions are evaluated *only* against the axes and
severity definitions below. If a model believes the contract itself is wrong, it
raises a `CONTRACT-CHALLENGE` row in the LEDGER and stops — the human arbitrates.

---

## 1. The artifacts — MERGE MODE

The goal is to **converge the two source notebooks into one**. They are co-equal
inputs, not primary-vs-reference.

- **PRODUCT (what converges):** `product/product_i{n}.ipynb`. It does **not** exist
  at start. Iteration 0 opens with a one-time **MERGE-DRAFT** turn in which the
  first steward authors `product_i0.ipynb` from BOTH sources (see
  `prompts/turn_merge_draft.md`). Every later iteration audits and reworks it.
- **SOURCE A (read-only):** `source/99_complete_college_level_walkthrough.ipynb`
  — the complete, sectioned, self-check-heavy walkthrough. Strength: rigor and
  coverage.
- **SOURCE B (read-only):** `source/99c_the_machine_that_predicts_the_next_token.ipynb`
  — the "build-it-till-it-breaks" narrative rewrite of the same course. Strength:
  motion, the break→repair pedagogy.
- **EXTERNAL ground truth:** standard ML/math (transformer mechanics, autograd,
  softmax/cross-entropy, attention, quantization, decoding). Where A, B, and
  external truth conflict, external truth wins.

**Merge rule (binding on every turn):** neither source is an oracle. Where A and B
state the same thing compatibly, keep it. Where they conflict, the merge may not
silently pick one — the drafter/steward raises a `FIDEL` finding in the LEDGER and
resolves it *on the merits* (external truth), recording which source was right and
why. A correct technical claim present in only one source must survive into the
product unless it's wrong; dropping it is a `FIDEL`/`PED` finding.

## 2. Goal of the artifact

A single self-contained, build-from-raw-tensors course in the mathematics of
language models that (a) is mathematically correct, (b) is executably correct,
(c) is pedagogically sound, (d) loses no correct content that either source had,
and (e) contains no contradiction between material inherited from the two sources.
Convergence means both models agree the merged notebook meets this bar.

## 3. Rubric axes (the ONLY things auditable)

| axis | code | what it covers |
|------|------|----------------|
| Mathematical correctness | **MATH** | Derivations, identities, theorem statements, dimensional/shape claims, variance/scaling arguments, probability & information-theory claims (softmax, log-partition, KL, cross-entropy, Gibbs). |
| Code correctness & executability | **CODE** | Cells run top-to-bottom without error; outputs match claims; shapes/dtypes as stated; no silent NaN; seeds/reproducibility; deprecated API misuse. |
| Claim accuracy | **CLAIM** | Any factual assertion about how LLMs/transformers/training/serving actually work; "this breaks / this repairs it" narrative claims must be literally true. |
| Reference fidelity | **FIDEL** | Where 99c restates something 99 also covers, the restatement must not introduce error or contradiction. Stylistic divergence is NOT a finding. |
| Pedagogical soundness | **PED** | Concept order, unstated prerequisites, misleading simplifications, self-check validity (a self-check whose stated answer is wrong is PED **and** MATH/CODE). |
| Notation & consistency | **NOTE** | Symbol collisions, undefined notation, units/shape notation drift, inconsistent naming across cells. |

**Out of scope (never a finding — raising one is itself a false positive):**
voice, tone, "literary vs plain" style, section ordering *preference*, length,
British vs US spelling, formatting/markdown aesthetics, whether a different
pedagogy *could* work, anything requiring information not in the artifacts or
standard ML.

## 4. Severity definitions

| severity | definition | must fix before convergence? |
|----------|------------|------------------------------|
| **BLOCKER** | Wrong math/code that a learner would internalize as true, or a cell that errors. Actively teaches something false. | Yes |
| **MAJOR** | Correct-in-spirit but materially misleading; a claim true only under unstated conditions; a self-check with a wrong answer; shape/dtype claim off. | Yes |
| **MINOR** | Imprecision that a careful reader survives but that should be tightened; notation drift; a claim that needs one qualifier. | Convergence allowed with these OPEN only if BOTH models explicitly waive them in signoff. |
| **NIT** | Cosmetic-adjacent within an in-scope axis (e.g. an undefined symbol used once, later defined). | No. Logged, never blocks. |

## 5. Evidence standard

Every finding MUST cite an exact location: `cell {index}` (0-based, top-to-bottom
of the current `product_i{n}.ipynb`) plus a quoted anchor phrase ≤ 15 words, or a
line within a code cell. A finding without a resolvable location is auto-`REJECTED`
at meta-audit. Claims of the form "this is wrong" must state what *correct* looks
like, or they are downgraded to a question, not a finding.

## 6. Definition of done (convergence predicate)

Declared converged only when, across **one full round with zero product changes**:
1. `LEDGER.md` has zero `OPEN` and zero `CONTESTED` rows at BLOCKER/MAJOR.
2. Neither model raises a new BLOCKER/MAJOR finding in that round.
3. Both `signoff/SIGNOFF_OPUS48.md` and `signoff/SIGNOFF_SOL56.md` exist, each
   naming the exact `product_i{n}` version signed, each listing its single
   strongest remaining objection it chose not to block on.
4. Each model has logged ≥ 3 substantive findings (MAJOR+ or upheld MINOR) across
   the whole run. A model that only ever agreed cannot validly sign off.

Any MINOR left OPEN at convergence must be explicitly waived by both signoffs.

## 7. Roles

- Two auditors: **OPUS48** and **SOL56** (Opus 4.8 and Sol 5.6). Symmetric — same
  system prompt, roles swapped by iteration.
- **Steward** of iteration `n`: OPUS48 on even `n`, SOL56 on odd `n`. The steward
  owns the rework that produces `product_i{n+1}`, and — at iteration 0 only — the
  one-time MERGE-DRAFT that authors `product_i0` from both sources.
- Human: freezes this contract, arbitrates `CONTESTED` deadlocks and
  `CONTRACT-CHALLENGE`, holds the stop button.
