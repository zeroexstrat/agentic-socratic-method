# The Socratic Agentic Method

*Two models improve one artifact by auditing each other — and auditing each other's
audits — until both can defensibly sign off on the same version. A frozen contract, an
append-only ledger, and a file passed between them make the disagreement operational
instead of hiding it in fluent prose.*

This repository is the full, inspectable record of one run: two language notebooks merged
into a single self-contained course, hardened by cross-model review to a formal convergence,
then reopened by hand for the one thing the contract could not measure. Every audit,
counter-audit, repair, and signature is here — including a retracted signoff and a bug that
passed its own test by coincidence.

---

## The outcome, first

- **What was built.** One self-contained NumPy course, *The Machine That Predicts the Next
  Token*, merged from two earlier drafts: a rigorous, self-check-heavy PyTorch walkthrough
  (`source/99…`) and a "build it until it breaks" narrative rewrite (`source/99c…`).
- **How it was reviewed.** Two models — **Opus 4.8** (`OPUS48`) and **Sol 5.6** (`SOL56`) —
  alternated the roles of author and critic across a fixed loop, adjudicated against a frozen
  rubric. Findings accumulated in an append-only ledger; fixes had to be verified by the model
  that did not make them; every code cell was re-executed on every rework.
- **How it converged.** Formal two-model, zero-waiver convergence landed on **`product_i7`**,
  after **33 findings** were resolved and an unchanged verification round changed nothing and
  ran clean. Only then did the coordination layer write `CONVERGED on product_i7 at iter 7`.
- **What came after.** A human-commissioned third reader (**Fable 5**, `FABLE5`) — outside the
  frozen two-model contract — audited *pedagogy*, the axis the contract had deliberately left
  out of scope, and found that all the mathematical hardening had left scar tissue. Under a
  narrow human charter (recompose prose and structure; **no claim may change strength**), the
  work reopened and moved to **`product_i11`**: a 128-cell course (48 executable cells, 16
  embedded figures) carrying a zero-waiver `SOL56` signoff after a deliberately hostile final
  pass. The full run recorded **51 findings** end to end.
- **The honest status line.** `OPUS48`'s surviving signoff still names `product_i7`; the
  coordination stop still records convergence there. `product_i11` is signed by **one** model,
  not two, and does **not** satisfy the original two-model convergence predicate. It is the
  strongest artifact in the repository, and it is signed once. Both are true, and collapsing
  them would erase the provenance this project exists to test.

For the narrative version of all this, read the essay:
**[`output/compositions/the-ledger-between-the-models/final.md`](output/compositions/the-ledger-between-the-models/final.md)** — *"The Ledger Between the Models."*

---

## Why it needs a method at all

A normal merge hides exactly the disagreements worth keeping. Where one source made a sharper
claim about attention and the other a more careful one, a drafting model can silently pick.
Where one carries a derivation the other drops, compression makes the loss look editorial. The
merged notebook reads smoothly and becomes *less true*, and nothing in the prose reports it.

"Make it better" is also not a stable target: two capable models can want incompatible things
and then bury the incompatibility in confident language, or pile up findings because criticism
is cheap, or thrash a paragraph back and forth until a human gets tired and calls it done.

The method's whole job is to make the disagreement a first-class object with a state, and to
make *stopping* a fact rather than a mood.

## How it works

### The frozen contract — [`CONTRACT.md`](CONTRACT.md)
Written and frozen by the human *before* the models touch the artifact, so they cannot optimize
against a moving target. It names the two sources as **co-equal inputs**, puts **external
mathematics above both** (so conflicts break on the math, not on whichever draft sounds more
confident), and fixes the only six axes anything may be judged on:

`MATH` · `CODE` · `CLAIM` · `FIDEL` (reference fidelity) · `PED` (pedagogy) · `NOTE` (notation).

It also defines severities (`BLOCKER` → `MAJOR` → `MINOR` → `NIT`), the evidence a finding must
carry, and the exact predicate under which the loop may stop. Voice, tone, and pedagogical
order are explicitly **out of scope** — a decision that keeps the loop from churning over taste,
and that later turns out to be the contract's one blind spot.

### The ledger — [`LEDGER.md`](LEDGER.md)
The single source of truth for *state*. Every finding cites a specific notebook cell and a short
anchor phrase, and enters as an append-only row with an identity, an axis, a severity, and a
state: `OPEN → ACCEPTED → RESOLVED → FROZEN`, with `REJECTED`, `CONTESTED`, and `REOPENED` as the
other transitions. Rows are never edited in place; the state log below the table folds forward.
The notebooks and prose are the *reasoning*; the ledger is the *record*.

### The baton — [`coord/`](coord/)
Coordination is a JSON file, not a conversation. `coord/turn.json` records whose turn it is,
which iteration is live, and which phase is next. A session **waits** for its turn, does its one
bounded job, writes its artifact atomically, and **passes** the baton; the other session wakes to
a changed filesystem and no memory of the exchange that changed it. No API, no direct
model-to-model channel — continuity lives in plain files, which is what makes the whole run
inspectable afterward.

```
python coord/wait_turn.py --me OPUS48    # blocks until it's your turn  (exit 42 = STOP)
#   ... perform the phase the baton names; write files atomically ...
python coord/pass_turn.py --me OPUS48    # validates your output, then advances or ends the baton
```

### The loop
One steward and one auditor per round; roles swap every iteration, so neither model becomes the
permanent author or the permanent critic. Steward = `OPUS48` on even iterations, `SOL56` on odd.

1. **Merge** *(once, iteration 0)* — the first steward authors `product_i0` from both sources.
2. **Audit** — the auditor reads `product_i{n}`, raises `OPEN` findings, **fixes nothing** → `audits/`.
3. **Meta-audit** — the steward rules on each finding (`UPHELD` / `OVERTURNED` / `RECLASSIFIED`)
   *and* adds what the auditor missed → `metaaudits/`. This is the anti-sycophancy hinge:
   overturning a false positive counts as much as landing a real one.
4. **Rework** — the steward `FIX`es or `REJECT`s-with-rationale every live finding, writes
   `product_i{n+1}`, and **re-runs every cell** → `rework/`. A broken notebook cannot pass the baton.
5. **Signoff** — a model may emit one only when the predicate looks met, and it must name its
   single strongest *remaining* objection. Convergence is declared by the harness, never by a model.

### The guards — [`harness/convergence.py`](harness/convergence.py)
Prompts alone don't produce convergence; these do:

- **Anti-collapse.** A model that never disagrees can't sign off: each must log ≥ 3 substantive
  findings across the run, and each signoff must name a real strongest-remaining objection.
  *"Looks great"* is a void signature.
- **Anti-oscillation.** A confirmed fix becomes `FROZEN`; reopening it requires **new evidence**.
  This is what stops the author-changes-it / critic-reverts-it loop.
- **Anti-deadlock.** A finding `CONTESTED` for two rounds escalates — to the human, or to an
  optional tiebreak model.
- **Termination is the harness's call.** A model *proposes* done by signing; only
  `convergence.converged()` — both valid signoffs on the same version, zero open blockers, one
  unchanged round — declares it, and it writes `coord/STOP`.

## How it worked out (the interesting part)

**The process caught itself being sure.** At one iteration a steward signed off on a version it
believed was finished. The next pass went after an affine-quantizer example: the prose explained
scale and zero-point calibration and carried an assertion that *passed* — and passed by
coincidence. Recomputing the representable grid showed the rounded integer zero-point had shifted
the interval, and the example's own endpoint clipped: exactly the case the surrounding error
bound said could not happen. The test had been green for the wrong reason. The steward verified
the counterexample, accepted the reopening, and **withdrew its own signoff**. Related coverage
assumptions surfaced twice more under narrower conditions and were each reopened, checked, and
repaired. A late iteration bought a claim no ceremonial protection; a signature was falsifiable.

**Convergence had a blind spot.** `product_i7` met the contract's bar exactly — and *only* that
bar. Because the contract had scoped pedagogy out (correctly, or the loop would have churned on
taste), the predicate was structurally unable to see that all the hardening had left
**qualification sediment**: in places the course spent more energy arguing with an earlier
overclaim than teaching the idea it had finally gotten right. `FABLE5`, brought in from outside
the frozen contract to read only for exposition, named it. The human then reopened the work
under a hand-written charter — recompose freely, but no claim changes strength and every frozen
fix must survive — which produced a better-moving notebook *and* new regressions (a broken figure
path, a few resurfaced overclaims). Those went into the ledger like any other finding, were
reopened by the model that had not made them, and were repaired. The endpoint is `product_i11`.

The lesson isn't that models agreeing proves anything true. It's that a bounded contract, a
falsifiable signature, and a human who owns the scope can turn cross-model disagreement into a
record you can actually audit.

## The artifact

The final course, `product/product_i11.ipynb`, is self-contained NumPy — no repository, no GPU,
no framework — so any claim can be broken by deleting a line and re-running. It is published two
other ways:

- **Read it rendered:** [0xstrategies.com/writing/llm-from-scratch.html](https://0xstrategies.com/writing/llm-from-scratch.html)
- **As a companion to its rigorous sibling:** [github.com/zeroexstrat/lm-foundations](https://github.com/zeroexstrat/lm-foundations)

## Repository map

```
CONTRACT.md        Frozen rubric: six axes, severities, evidence, convergence predicate.
LEDGER.md          Append-only finding register — the single source of truth for state.
coord/             The baton: turn.json, state_machine.py, wait_turn.py, pass_turn.py, STOP.
harness/           convergence.py (the guards) + loop_orchestrator.py + config.yaml.
prompts/           System prompt, per-turn prompts, agent standing instructions, signoff template.
source/            The two read-only inputs (99 and 99c).
premerge/          Advisory pre-read of one source before the merge.
product/           product_i0 … product_i11 — every version the loop produced.
audits/            audit_{model}_i{n}.md            (find-only)
metaaudits/        metaaudit_{model}_i{n}.md        (audit the audit)
rework/            rework_{model}_i{n}.md           (decision log + concrete edits)
signoff/           SIGNOFF_{model}.md               (emitted only at the predicate)
output/compositions/the-ledger-between-the-models/  The reflective essay, in drafts and final.
```

## Reproduce it

No API credits required — two agent sessions and a shared folder are enough. Open two sessions in
this directory (two Claude Code / Cowork windows is the reference setup; any agent that can
read/write files and run Python works, including a local model wrapped in a runner). Paste
`prompts/agent_OPUS48.md` as one session's standing task and `prompts/agent_SOL56.md` as the
other's; each then loops `wait_turn` → do the named phase → `pass_turn` until a `coord/STOP` file
names the converged version. Cell execution during merge/rework needs `pip install nbclient
nbformat`. Prefer one process driving both models? Point `harness/loop_orchestrator.py`'s adapters
at local endpoints — same contract, same ledger, same predicate.

> **A note on trusting the meta-audit.** The load-bearing step is the meta-audit's willingness to
> *overturn* a false positive, not just uphold true ones. A quick way to check that on your own
> setup before trusting a full run: plant a deliberately wrong finding in an audit (flag a correct
> √D scaling claim as an error) and confirm the meta-audit throws it out. If it rubber-stamps the
> plant, the guards aren't biting yet.

## What this is — and isn't

This is one worked example, not a benchmark. A clean execution and a closed ledger establish
compliance with *the chosen contract*, not universal correctness or pedagogical perfection, and
one project cannot show this protocol beats any other. The human writes the contract, arbitrates
scope, decides when a new question justifies reopening the work, and remains responsible for what
goes out in public. The baton can say when to act; the ledger, what is unresolved; the harness,
when a predicate is met. None of them can decide whether the predicate was the right one.

## License

Code (`coord/`, `harness/`, notebook code cells) under the MIT License; text (prose, the essay,
the notebooks' expository content) under CC BY 4.0. Reuse either freely with attribution.

## Author

Rafael Almeida — [0xstrategies.com](https://0xstrategies.com) · [zeroexstrat@gmail.com](mailto:zeroexstrat@gmail.com)
