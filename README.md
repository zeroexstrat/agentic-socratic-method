# nb99 · Socratic Agentic Method — cross-model iterative auditing

Two models (**Opus 4.8** = `OPUS48`, **Sol 5.6** = `SOL56`) converge on the best
version of an ML-pedagogy notebook by auditing each other's work — and auditing
each other's *audits* — until both can defensibly sign off on the same version.

## What's here

```
nb99-socratic-agentic-method/
  README.md                 ← you are here
  CONTRACT.md               ← FROZEN rubric + severities + convergence predicate. Read first.
  LEDGER.md                 ← append-only finding register. The single source of truth for state.
  source/
    99_complete_college_level_walkthrough.ipynb      ← REFERENCE (read-only)
    99c_the_machine_that_predicts_the_next_token.ipynb ← seed for the PRIMARY artifact
  product/
    product_i0.ipynb        ← copy of 99c; each iteration adds product_i{n}.ipynb
  audits/       audit_{model}_i{n}.md
  metaaudits/   metaaudit_{model}_i{n}.md      ← the "audit the audit" step
  rework/       rework_{model}_i{n}.md         ← decision log + concrete edits
  signoff/      SIGNOFF_{model}.md             ← emitted only at convergence
  prompts/      system_shared.md + turn_{audit,metaaudit,rework}.md + signoff_template.md
  harness/      loop_orchestrator.py + convergence.py + config.yaml
```

## The default framing (change in CONTRACT §1 if you want)

`99c` (the literary rewrite) is the artifact under audit. `99` (the complete
walkthrough of the same course) is a **reference**, not an oracle — a 99c/99
mismatch is a finding only when 99 is actually right. External ML/math outranks
both. To instead converge the two notebooks *against each other*, swap the
PRIMARY/REFERENCE roles in `CONTRACT.md` and re-freeze. That's the only supported
contract edit, and only you make it.

## The loop (one round, roles swap each round)

Steward = OPUS48 on even iterations, SOL56 on odd. Auditor = the other one.

1. **AUDIT** — auditor reads `product_i{n}`, finds issues (no fixes), logs `OPEN`
   rows → `audits/audit_{auditor}_i{n}.md`.
2. **META-AUDIT** — steward adjudicates each finding UPHELD / OVERTURNED /
   RECLASSIFIED, *and* adds findings the auditor missed → `metaaudits/…`. This is
   the anti-sycophancy step: overturning false positives matters as much as fixing.
3. **REWORK** — steward FIXes or REJECTs-with-rationale every non-rejected finding,
   materializes `product_i{n+1}.ipynb`, re-runs all cells → `rework/…`.
4. **SIGNOFF** — either model may emit one when the predicate looks met.
5. Harness checks convergence; else swap, `n += 1`.

## Why it converges instead of (a) flattering or (b) oscillating

The prompts alone don't guarantee this — the **guards in `convergence.py`** do:

- **Anti-collapse.** A model that never disagrees can't sign off: each must log
  ≥ 3 substantive findings, and each signoff must name its strongest *remaining*
  objection. "Looks great!" is a void signoff.
- **Anti-oscillation.** A confirmed fix becomes `FROZEN`; reopening needs new
  evidence. Stops A-changes-it / B-reverts-it loops.
- **Anti-deadlock.** A finding `CONTESTED` for 2 rounds escalates — to you, or to
  an optional third tiebreak model (`config.yaml → guards.tiebreak_model`).
- **Hard cap.** `max_iterations` (default 6); on timeout the harness hands you the
  unresolved LEDGER rows rather than pretending to be done.
- **Termination is the harness's call, never a model's.** Models can *propose*
  done by signing off; only `convergence.converged()` declares it.

## Running it — NO API (two agent sessions, filesystem baton)

You don't need API credits. Two agent *sessions* take turns through the shared
folder via a turn baton in `coord/`. Full mechanism and troubleshooting:
`coord/README_coord.md`. Short version:

1. Open **two** agent sessions in this folder (two Claude Code / Cowork windows is
   the reference setup; any agent that can read/write files + run Python works,
   including a local model wrapped in a runner).
2. Paste `prompts/agent_OPUS48.md` as session 1's standing task, and
   `prompts/agent_SOL56.md` as session 2's. Each then loops:
   ```bash
   python coord/wait_turn.py --me OPUS48    # blocks until its turn (this is "listening")
   #   ... do the phase the baton names, write files atomically ...
   python coord/pass_turn.py --me OPUS48    # validates output, advances/【or ends】the baton
   ```
3. Start both. OPUS48 holds the baton first (`merge`) and authors `product_i0` from
   both sources; audit → meta-audit → rework → swap repeats automatically until a
   `coord/STOP` file names the converged version.

`pass_turn` refuses to advance if it isn't your turn or if you didn't write the
phase's output, and runs the convergence check itself at each rework — so
termination is never an agent's self-declaration. Cell execution during merge/rework
needs `pip install nbclient nbformat`.

### Fully-automated alternative (still no API)
Prefer one driver over two sessions? Point `harness/loop_orchestrator.py`'s
`_call_opus48` / `_call_sol56` adapters at **local** model endpoints (ollama /
llama.cpp). Same contract, same LEDGER, same predicate — one process drives both
models. (`harness/` is the one-driver-two-models path; `coord/` is the
two-agent-sessions path you asked about.)

## Sanity-check before a full run (do this first)

Dry-step one round by hand to make sure the *meta-audit actually overturns things*
rather than rubber-stamping: manually run the `merge` then `audit` then `metaaudit`
turns once, but **plant a false-positive finding** in the first audit (e.g. flag a
correct √D scaling claim as wrong). If the meta-audit upholds your planted error,
tighten `prompts/turn_metaaudit.md` before automating — that failure mode is the
whole reason the guards in `harness/convergence.py` exist.
