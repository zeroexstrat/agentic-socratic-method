# Audit FABLE5 i7 — third-model audit of product_i7 (pedagogical movement, exposition, motivation, transitions)

**Commissioned by:** HUMAN, outside the two-auditor loop. FABLE5 is not a CONTRACT §7 party;
findings below are *proposed* rows for HUMAN to adopt or discard. Where a finding falls under
CONTRACT §3 axes it is stated to the §5 evidence standard (cell index + anchor ≤ 15 words +
what correct looks like). Where it falls in the contract's out-of-scope zone (pedagogical
*preference*, motivation, narrative movement — the explicit subject of this commission) it is
segregated into Part II and never framed as a contract finding.

**Reviewer's position:** FABLE5 authored source A. That grants unusual visibility into what
the merge kept, transformed, and dropped — and a known bias toward A's devices. Part II
discounts for that bias explicitly.

---

## Verdict

**The convergence is real and the mathematical hardening is excellent.** The 33-finding war
produced a notebook whose *claims* are more careful than either source: the permutation-
equivariance scoping (Haviv caveat), the residual non-guarantee with one-line counterexamples,
the LayerNorm ε-honesty, the KV-cache "re-projection, not total complexity" precision, and the
quantization calibration trap are each better than anything in source A or B. The break→repair
spine holds, the forced moves are mostly earned, and the Gibbs mystery-thread (cell 2 → 19 →
46 → 108) is genuine narrative craft.

**But the adversarial protocol left a specific class of damage the contract could not see:
findings were resolved by *amendment*, almost never by *re-composition*.** Thirty-three
correct patches, each individually verifiable, have accreted into qualification sediment: core
teaching moments now deliver the caveat at equal or greater volume than the claim, several
deliver it *twice*, and the seams of the merge ("ported from source A", "the original text")
are visible to a learner who was promised one course. The mathematics converged; the prose
shows the scar tissue of how.

Recommendation at the end: one human-sanctioned **recomposition iteration** with an explicit
no-new-claims constraint, then a regression audit by both models.

---

## Part I — Contract-legible findings (proposed rows)

### P-001 · CLAIM · MINOR — cell 0, "Every one is self-contained `numpy`"
Cell 0 promises "Every one is self-contained `numpy`/`scipy`/`matplotlib`" while cell 119
states the direct opposite, correctly: "the cells are **top-to-bottom runnable in one shared
notebook state**, not independently self-contained." The F-007 self-contained→shared-state fix
landed in cell 119 but the contradicted promise survived in cell 0. Correct looks like: cell 0
says "Everything runs on `numpy`/`scipy`/`matplotlib` alone — no repository, no GPU, no
framework — in one shared kernel, top to bottom." Both auditors signed a product whose first
cell contradicts its second-to-last.

### P-002 · PED · MINOR — cell 71, "the train/validation curves above"
Self-check (b) references "the train/validation curves **above**", but those curves first
appear in cell 78, *below* the self-check; self-check (c) asks why perplexities under
different tokenizers are incomparable, but perplexity is not developed until Chapter 7 (cells
84/86; the cell-11 aside does not carry tokenizer-dependence). A learner reaching cell 71
top-to-bottom cannot answer (b) or (c) from material presented. Correct looks like: move the
self-check block after cell 78, or retarget (b)/(c) to the minibatch/AdamW material the
checks actually sit beside. Likely a cell-reordering scar from the F-012 restoration.

### P-003 · PED · MINOR — cell 95, "`.max(1)*0 +`" dead code in a stability lesson
`ce_vectorized` contains `Z[np.arange(len(targets)), :].max(1)*0 + np.log(...)` — a
subexpression multiplied by zero. The math is right (Z is already max-shifted, and the max
cancels in the CE difference), but in a course that *teaches* the log-sum-exp max trick, a
line that visibly computes a max and multiplies it by zero invites the careful reader to hunt
for meaning that is not there. Correct looks like: delete the vestigial term and add the
one-line comment for why the shift cancels.

### P-004 · PED · MINOR — cells 10/30/62, the untaught type change from one distribution to (B,T,V)
Cell 10 types the model as prefix ↦ **one** distribution; cell 30's bag model implements
exactly that type (pool → single logit vector). The assembled transformer in cell 62 outputs
`(B,T,V)` — a distribution *per position* — and the shift is never taught as a move: pooling
silently disappears, and the reconciliation ("one forward pass evaluates the conditional for
every prefix of the window simultaneously; the network's type is 𝒱^T → (Δ)^T while the
*model's* type is still prefix ↦ Δ, read off at the last position for generation") appears
only as subordinate clauses in cells 60/61. For a course this disciplined about types, the
one type change with real conceptual content is the one that goes unmarked. Correct looks
like: a short beat at the top of Chapter 5's assembly (or end of Chapter 4) stating the two
types and why evaluating all prefixes at once is the same object as cell 10's map, batched
over prefixes. (Cell 34's label-shift contract is the natural hook; it already says "T
next-token examples at once" without connecting back to cell 10's type.)

### P-005 · PED · MINOR — cell 93, "That is Chapter 11" breaks the forced-move chain
Chapter 8's forced move promises pairwise-preference supervision and names its destination —
"That is Chapter 11" — sending the reader's momentum two chapters downstream, after which
Chapters 9 and 10 arrive as unannounced detours. Chapter 9's own opening ("a dictionary, not
a movement") and cell 96's patch-up ("Two practical layers still sit between here and a
deployed system. Both are next.") do damage control, but the promise structure of the course
— each break forces *the next* chapter — is violated at exactly one seam, and it reads as a
merge-order artifact. Correct looks like: Chapter 8's forced move states the detour up front
("using that signal is Chapter 11's derivation; between here and there sit two practical
layers a deployed system cannot skip — naming the objects in a real stack, and making the
model small enough to serve").

### P-006 · PED · MINOR — cells 33–35, the Chapter-3 cliffhanger is stepped on
Cell 33 lands the chapter's break (order-blindness) and fires its cliffhanger: "The next
chapter is exactly these two powers — and it is where the shape you were told to watch for
comes back." Then two administrative cells (34–35, label shifting) interpose before Chapter 4
begins, deflating the transition the course's method depends on. The content of 34–35 is
correct and its placement satisfies F-010/F-021 (definitions before use); only the *order
within the chapter* is wrong. Correct looks like: label shifting moves before the bag-model
break (framed as "one more piece of plumbing while the machine still looks fine"), so the
chapter ends on cell 33's cliffhanger.

### P-007 · PED · MINOR — cells 60/61–66, Chapter 5 ends twice
Cell 60 declares the machine complete and fires the forced move to training ("That is the
next chapter") — followed by six more cells of Chapter 5 (assembly, partial optimization,
weight tying, parameter budget), after which Chapter 6 begins with no fresh transition. The
chapter has two endings, and the real one has no forced move. Cells 60 and 61 also restate
the same composition sentence nearly verbatim ("evaluates all T conditionals … exactly the
shifted labels of Chapter 3"). Correct looks like: cell 60 shrinks to a segue into the
assembly ("hold that claim until it is executable — here is the machine, actually run"), and
the forced-move paragraph moves to the end of cell 66. Also fixes P-008's anchor.

### P-008 · NOTE · NIT — cell 60, "exactly the shifted labels of Chapter 3 consume"
Mangled sentence: "A single forward pass evaluates *all* T conditionals of Chapter 0 at once
— exactly the shifted labels of Chapter 3 consume." Correct looks like: "…at once — exactly
what the shifted labels of Chapter 3 consume."

### P-009 · PED · MINOR — cell 28, the one break the course narrates instead of running
The method statement (cell 0) promises every chapter builds the naive thing and *watches it
break in runnable code*. Chapter 2's break — a char tokenizer trained on four symbols dies on
`'b'` — is narrated ("encoding it raises a missing-key error") but never executed, making
Chapter 2 the only chapter whose break is asserted rather than experienced. (Chapter 9
deviates too, but flags itself: "a dictionary, not a movement.") Correct looks like: a
three-line cell that attempts `stoi['b']`, catches the `KeyError`, and prints the byte-level
escape route; the chapter then earns its slot in the method.

### P-010 · NOTE · MINOR — cells 9, 23, 35, 36, 57, 73, 96, 120 — provenance leaks into the learner's text
Reader-facing prose repeatedly cites the merge's internal archaeology: "ported from source A"
(cells 35, 57, 73), "from the derivations-first source" (cells 23, 120), "the exact `"cat"`
residual vectors from **the original text**" (cell 36 — which original?), and cell 96's
editorial parenthetical addressed to nobody a learner can identify ("*the original notebook's
'map to the curriculum' … kept out of the conceptual spine*"). Cell 0's colophon already
discloses the merge once, correctly. Correct looks like: provenance moves to code comments or
the closing colophon; the body text speaks with one voice. A learner should never need to
know what "source A" is to parse a sentence.

### P-011 · PED · MINOR — cells 42/44, the equivariance correction is delivered twice, nearly verbatim
The F-002 repair now straddles the demo: cell 42 pre-empts ("State this at exactly the
strength it holds… Two honesties… the causal mask … already breaks full permutation-
equivariance… not strictly *necessary*"), and cell 44 repeats the same scoping, the same
mask-caveat, the same Haviv citation, under the same rhetorical frame ("state the theorem at
exactly the strength it holds… Two caveats"). Individually correct; together, a rework scar
that doubles the reader's toll at the course's single most delicate theorem. Correct looks
like: cell 42 carries only the setup and prediction ("watch the symmetry hold, then
shatter"); the full strength-scoping and citation live once, in cell 44, after the reader has
seen the phenomenon.

---

## Part II — Advisory (explicitly outside CONTRACT §3; the commissioned subject)

These are judgments about pedagogy and movement that the contract rightly excludes from the
two-model loop and that the HUMAN asked FABLE5 to make anyway. No severities; discount A-1
and A-2 for authorial bias toward source A's devices.

### A-1 · Qualification sediment: the systemic cost of convergence-by-amendment
The single largest pedagogical pattern in i7 is not any one cell — it is that ~10 of the 33
resolutions were implemented as *appended corrections* to standing text rather than
re-composition, because appends are what an adversarial verification loop can cheaply check.
The reader now routinely receives claim → retraction → re-scoped claim where a single
correctly-scoped claim was available:

- cell 76: a beautiful demo (p(t|c) sliding from prior to memorized zero) is followed by three
  paragraphs of "read it carefully / that is ignorance, not transfer / a caveat, not a law"
  before any crisp statement of what the reader *should* take;
- cell 110: "'indistinguishable' overstates the only high value shown" — a paragraph arguing
  with a wording that could simply have been corrected upstream;
- cell 105: the "do NOT read this curve as…" paragraph outweighs the positive lesson;
- cell 53 spends its energy on what residuals don't guarantee; the true statement is there,
  but the emotional arithmetic of the section is caveat-dominant;
- cell 10: the F-033 strict-positivity repair is correct and *belongs*, but as written it
  walls off the gentlest chapter with measure-theoretic caution at full volume — fine print
  delivered as headline.

None of these is wrong. Each was the rational minimal fix under the protocol. Their *sum* is
a course that too often teaches by disclaimer. The repair is not more auditing — it is one
recomposition pass (below) that restates every corrected claim once, at its final strength,
and deletes the visible argument-with-a-ghost framing ("the sloppy version is false", "state
it at exactly the strength it holds" ×2).

### A-2 · The mystery thread spoils itself
Cell 2 stakes the course's best dramatic device: "I am not going to tell you where. Watch for
it." Cell 19 plants the flag perfectly. Cell 46 then names the principle *and* announces the
third appearance's chapter ("returns a third and final time in Chapter 11"); cells 93 and 105
re-announce it. By the time cell 108 delivers "the flag planted quietly in Chapter 1 came
home," the reader has been told the ending three times. Keeping cell 46's *naming* (earned:
two instances justify naming the pattern) while cutting the two-and-a-half forward
announcements would let Chapter 11 land the way cell 2 promised. The table in cell 108 is the
right consolidation point and needs no advance advertising.

### A-3 · Self-check coverage is token-level
F-012's resolution restored exactly two self-check blocks (cells 25, 71 — one now misplaced,
see P-002). Chapters 4 and 5 — the derivation-densest, where source A's checks did their
heaviest lifting (prove the softmax/permutation commutation step; the C=2 dimension count;
why `n_embd % n_head == 0`) — have none. If the notebook is to be studied from rather than
read, three to four more blocks at Chapters 0, 4, 5, 10 would carry most of the value at
trivial cost. (F-012 is FROZEN; this is offered as new evidence for HUMAN, not a unilateral
reopen.)

### A-4 · The consolidation half of the movement is missing
The course has a superb *tension* mechanism (the forced move) and no *consolidation*
mechanism. Source A's late revisions closed each chapter with a "where we stand" beat: the
evolving definition of the object ("an autoregressive LM is now: …"), restated once per
abstraction layer. The merged course tracks its arc only twice — cell 2 (prospect) and cell
121 (retrospect, excellent). In a break→repair course this device is *cheaper* than in a
derivations course: each chapter's consolidation is one sentence of "what the machine now is"
plus one sentence of "the crack that remains," and the second sentence is the forced move the
course already writes. Fusing them would give every chapter the same shape as its best ones
(7 and 11) at a cost of two sentences each. Discount for bias: this is my device; but the
asymmetry (all tension, no consolidation) is visible independent of whose device fills it.

### A-5 · Two smaller motivation gaps
- **Chapter 10's break is bloodless**: the staircase plot shows *distortion*, not *failure* —
  nothing downstream is hurt until cell 104. Leading with the 1-bit perplexity blowup (already
  computed in cell 104's loop) and *then* explaining the staircase would give the chapter the
  same felt-break as the others. The genuinely great break of the chapter (the calibration
  trap, cells 100–101) is well placed.
- **Cell 105's train-set perplexity** confesses mid-paragraph that it scores on training data
  two chapters after the course made "held-out or it didn't happen" a moral principle. One
  sentence would turn the confession into a lesson: representation damage is measured against
  the model's own beliefs, so the train set is the *right* yardstick here — unlike every
  generalization claim before it.

---

## Recommendation

1. **HUMAN adopts Part I findings** (11 rows: 1 CLAIM/MINOR, 8 PED/MINOR, 1 NOTE/MINOR,
   1 NOTE/NIT) into the LEDGER under `raised_by: HUMAN` (or a sanctioned FABLE5 identity).
   None is BLOCKER/MAJOR; under CONTRACT §6 the i7/i8 convergence *stands* unless HUMAN
   elects to reopen — these are quality rows, not a convergence challenge.
2. **Sanction one recomposition iteration (i9)** with an amended, narrow charter: re-compose
   prose for movement and voice; **no claim may change strength in either direction**; every
   FROZEN finding's fix must survive verbatim-or-stronger; steward alternates as usual; both
   models then run one regression audit against the FROZEN ledger. This addresses A-1/A-2 and
   Part I's structural rows (P-005/006/007/010/011) in a single pass that the existing
   protocol can verify.
3. Fold A-3/A-4/A-5 into the i9 charter at HUMAN's discretion — they are additive, not
   corrective.

**Signed judgment:** product_i7 is mathematically converged and pedagogically *sound*; it is
not yet pedagogically *composed*. The two-model war made every sentence defensible; one more
deliberate pass should make the sentences again feel inevitable — which is the standard the
course's own method sets: each idea arriving as the thing that had to come next.

— FABLE5, iteration 7, commissioned audit
