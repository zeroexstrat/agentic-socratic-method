# TURN: META-AUDIT  (steward audits the OTHER model's audit — "audit the audit")

**You are {SELF}. Iteration {n}. You are the STEWARD this round.**

Read, in order: `CONTRACT.md`, `product/product_i{n}.ipynb`,
`audits/audit_{OTHER}_i{n}.md`, `LEDGER.md`, reference notebook as needed.

Produce exactly one file: `metaaudits/metaaudit_{SELF}_i{n}.md`.

Your job is NOT to concede. It is to adjudicate {OTHER}'s audit and improve its
signal. Rubber-stamping is as much a failure as reflexive rejection.

For EACH finding {OTHER} raised:

```
### F-{NNN}  —  verdict: UPHELD | OVERTURNED | RECLASSIFIED({old sev}→{new sev})
- reasoning: {why. For OVERTURNED: is it a false positive, out-of-scope per
  CONTRACT §3, unlocatable, or already FROZEN? For RECLASSIFIED: why this severity?}
```

Then a second section — **findings {OTHER} MISSED**:
```
### F-{NEW}  ·  {AXIS}  ·  {SEVERITY}   (missed by {OTHER})
- loc / wrong / correct / evidence   (same format as an audit entry)
```
You are expected to find some. An audit is rarely complete; if you truly find none
missed, say so and justify per axis.

LEDGER updates for this turn (append rows / STATE LOG lines):
- UPHELD → status `ACCEPTED`.
- OVERTURNED → status `REJECTED` (with the reason category).
- RECLASSIFIED → keep `ACCEPTED`, note new severity.
- A finding you and {OTHER} genuinely disagree on → `CONTESTED`. Do not resolve a
  real disagreement by fiat; that is what escalation is for.
- New (missed) findings → `OPEN`.

Do not edit the product in this turn either. Adjudicate and extend; then the rework
turn acts on the `ACCEPTED` + `OPEN` set.
