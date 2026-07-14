# TURN: MERGE-DRAFT  (iteration 0 only; steward authors the first product)

**You are {SELF}. Iteration 0. You hold the baton with phase = `merge`.**

Read: `CONTRACT.md` (esp. §1 merge rule), and BOTH sources in full:
`source/99_complete_college_level_walkthrough.ipynb` and
`source/99c_the_machine_that_predicts_the_next_token.ipynb`.

Produce exactly one artifact: `product/product_i0.ipynb` — the first merged draft.

This is a draft, not the final product; the audit loop will harden it. Your job is
a *faithful union*, not a fresh rewrite.

## How to merge
- Work section by section through the shared course arc (both cover the same
  progression: what an LM computes → tensors/probability → tokenization → embeddings
  → attention → the block → training → generation → fine-tuning → HF translation →
  quantization → modern practice → beyond transformers → how to study).
- For each section, take the **rigorous spine and self-checks from Source A** and
  the **break→repair narrative motion from Source B**, and state each technical
  point once, correctly.
- **Preserve every correct technical claim that appears in only one source.** If A
  has a variance lemma B lacks, keep it. If B has a "here's the exact line that
  repairs it" B has and A lacks, keep it.
- **Conflicts are not yours to silently resolve.** Where A and B disagree on a fact,
  resolve on the merits (external ML truth), and for each such case append a `FIDEL`
  LEDGER row (status `RESOLVED`) recording: the conflict, which source was right,
  and why. This makes your merge calls auditable next round.
- Keep it **runnable**: every code cell must execute top-to-bottom. Re-run before
  saving. Prefer Source A's code where both provide it and A's runs clean; port any
  unique working code from B.

## LEDGER
Append one STATE LOG line: `i0 · {SELF} · merge-draft authored product_i0 from A+B`.
Append a `FIDEL … RESOLVED` row per conflict you resolved, and a `FIDEL … OPEN` row
per conflict you could NOT resolve confidently (flag for the auditor).

## When done
Save `product/product_i0.ipynb`, then run `python coord/pass_turn.py --me {SELF}`.
The baton moves to the other agent for the first AUDIT.
