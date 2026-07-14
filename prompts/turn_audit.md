# TURN: AUDIT  (non-steward audits the current product)

**You are {SELF}. Iteration {n}. You are the AUDITOR this round.**

Read, in order: `CONTRACT.md`, `product/product_i{n}.ipynb`, `LEDGER.md`, and BOTH
sources `source/99_complete_college_level_walkthrough.ipynb` and
`source/99c_the_machine_that_predicts_the_next_token.ipynb` (read-only). Merge-mode
duty: for FIDEL, check the product against BOTH — flag correct content from either
source that was dropped, and any place the merge silently resolved a source conflict
without a LEDGER finding recording the call.

Produce exactly one file: `audits/audit_{SELF}_i{n}.md`.

For every issue, one entry:

```
### F-{NNN or NEW}  ·  {AXIS}  ·  {SEVERITY}
- loc: cell {index} — "{anchor phrase ≤15 words}"
- wrong: {precisely what is incorrect / misleading / non-executing}
- correct: {what the correct statement, value, shape, or code is}
- evidence: {derivation, the reference cell, or the external ML fact — enough that
  {OTHER} can verify without redoing your work}
```

Then, for EACH new issue, append a row to `LEDGER.md` with status `OPEN`, and add
one STATE LOG line: `i{n} · {SELF} · raised F-{NNN} ({SEV}/{AXIS})`.

Rules specific to this turn:
- **Do not fix anything.** Auditing is find-only. Fixes happen in the rework turn.
- **Coverage obligation.** For each rubric axis, either raise ≥1 finding OR state
  "AXIS {X}: none found" with a one-sentence justification of why you looked and
  are satisfied. "None found" with no justification is not acceptable.
- **Re-audit prior fixes.** For every `RESOLVED` finding from iteration {n-1},
  verify the fix actually landed and is correct. Confirm → propose `FROZEN`.
  Fix is wrong or incomplete → re-`OPEN` with a note.
- Run the code cells if you can. A claim that a cell errors must quote the error.
- Rank findings BLOCKER → MAJOR → MINOR → NIT within the file.
