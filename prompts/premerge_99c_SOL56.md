# PRE-MERGE ADVISORY PASS — agent SOL56 (Codex)

**One-time, advisory. This is NOT a baton turn.** Do not run any `coord/` script, and
do not touch `LEDGER.md`, `product/`, or `coord/turn.json`. You raise NO LEDGER rows.
Your output is advisory input to OPUS48's upcoming merge-draft — nothing more.

## Context
- The deliverable of this project is a NEW union notebook merging two sources.
- `source/99_complete_college_level_walkthrough.ipynb` = your (Codex's) original.
- `source/99c_the_machine_that_predicts_the_next_token.ipynb` = Claude's redesign of
  your 99. You are giving it an independent read BEFORE Claude folds it into the merge.

## Rules
- Audit ONLY on CONTRACT.md §3 rubric axes: **MATH, CODE, CLAIM, FIDEL, PED, NOTE**.
  Out-of-scope (§3) — voice, tone, style, ordering preference, length — are NOT findings.
- Ground-truth priority: external ML/math > either notebook. 99 is reference, not oracle.
- Cite every finding: `cell {index}` (0-based in 99c) + a quoted anchor <=15 words, and
  state what CORRECT looks like. No location or no fix = drop it.

## What to look for in 99c
1. Errors introduced by the redesign — wrong math, non-executing code, false claims.
2. Misleading simplifications a learner would internalize as true.
3. Correct content in YOUR 99 that 99c dropped or garbled (FIDEL / PED).
4. Notation / consistency drift within 99c.

## Output
Write ONLY this file (atomically: write `.tmp`, then rename):
`premerge/99c_advisory_SOL56.md`

Rank findings BLOCKER -> MAJOR -> MINOR -> NIT. Per finding:
- loc: cell {i} — "anchor phrase"
- wrong: what is incorrect / misleading / non-executing
- correct: the correct statement, value, shape, or code
- evidence: derivation, the specific 99 cell, or the external ML fact

When done, tell Rafael. OPUS48 then authors `product_i0` informed by your advisory,
and the normal baton loop begins with your iter-0 audit of that product.
