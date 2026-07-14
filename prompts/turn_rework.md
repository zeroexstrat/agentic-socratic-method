# TURN: REWORK  (steward produces the next product version)

**You are {SELF}. Iteration {n}. You are the STEWARD this round.**

Read: `LEDGER.md` (every `ACCEPTED` and still-`OPEN` row), your
`metaaudits/metaaudit_{SELF}_i{n}.md`, and `product/product_i{n}.ipynb`.

Produce two files:
1. `rework/rework_{SELF}_i{n}.md` — the decision log + concrete edits.
2. `product/product_i{n+1}.ipynb` — the materialized next version (apply your edits).

## rework markdown structure

Top of file — a decision table covering EVERY non-`REJECTED` finding:
```
| id | decision | where | one-line rationale |
|----|----------|-------|--------------------|
| F-012 | FIX | cell 34 | corrected √D scaling claim; variance lemma now stated for unit-variance inputs |
| F-013 | REJECT-WITH-RATIONALE | cell 9 | reference 99 is wrong here; external ML backs 99c. Escalating F-013 as CONTESTED. |
```
Rules:
- Every `ACCEPTED`/`OPEN` finding gets FIX or REJECT-WITH-RATIONALE. No silent drops.
- A FIX must be the *minimal* change that resolves the finding. Do not rewrite cells
  that no open finding touches. Scope creep is itself reviewable next round.
- If a fix would introduce a new claim, that claim is fair game for audit next round
  — flag it in the rework so {OTHER} looks there.

Then, per FIX, the concrete edit:
```
### F-012 — cell 34
- before: "{quoted anchor}"
- after:  "{new text / new code}"
```

## LEDGER updates
- Each FIX → status `RESOLVED` (the next audit will confirm → `FROZEN`).
- Each REJECT-WITH-RATIONALE where you overrule an `ACCEPTED` finding → `CONTESTED`
  (you and the meta-audit now disagree; it escalates).
- Add STATE LOG lines: `i{n} · {SELF} · resolved F-012; rejected F-013 (contested)`.

## Materializing the notebook
Apply the edits to `product_i{n}.ipynb` and save as `product_i{n+1}.ipynb`.
Re-run all code cells top-to-bottom before saving; if any cell errors, you have not
finished the rework. Then roles swap and iteration {n+1} begins with an AUDIT turn.
