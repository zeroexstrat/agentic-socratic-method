# coord/ — the no-API file baton

Two agent sessions converge the notebooks by **passing a baton through the
filesystem**. No API, no credits, no direct agent-to-agent messaging. This is the
robust version of "each agent listens for the other's latest edit."

## Why a baton instead of raw file-watching

If Agent B just watched Agent A's audit file for changes, B can't tell "A finished
its audit" from "A is still typing." It would audit half a document. The baton adds
the missing signal: a single `turn.json` says whose turn it is and what phase.
Nobody acts unless they hold the baton, and the baton flips only *after* the output
file is completely written (atomically). So:

- **completion signal** — you only read the other's file when the baton says their
  turn is done;
- **mutual exclusion** — exactly one agent works at a time, so two writers never
  collide on `LEDGER.md` or the product;
- **atomic reads** — outputs are written temp-then-rename, so a watcher never sees a
  partial file.

## The three files

- `turn.json` — the baton: `{iter, phase, actor, seq}`. Only `pass_turn.py` writes it.
- `state_machine.py` — the single definition of *what turn comes next*. Agents never
  compute this themselves.
- `STOP` — created by `pass_turn.py` when the run CONVERGES or ESCALATES. Its
  presence makes both `wait_turn.py` calls return exit 42, ending both agents.

## The phase cycle

```
iter 0:  merge(steward) → audit(auditor) → metaaudit(steward) → rework(steward)
iter 1+:              audit(auditor) → metaaudit(steward) → rework(steward)
         steward = OPUS48 on even iters, SOL56 on odd; auditor = the other.
         after each rework: convergence check → STOP, or advance to next audit.
```

Steward owns the merge draft (once), the meta-audit, and the rework. Auditor owns
the audit. Roles swap every iteration because the previous steward becomes the next
auditor.

## Two commands each agent uses

```bash
python coord/wait_turn.py --me OPUS48     # blocks until your turn; exit 42 = STOP
python coord/pass_turn.py --me OPUS48     # validates + advances the baton after you write
```

`pass_turn` refuses if it isn't your turn, refuses if you haven't written this
phase's expected output, and — at the end of a rework — runs the convergence and
escalation checks. **Termination is decided by `pass_turn` (via `harness/convergence.py`),
never by an agent declaring itself done.**

## Reference setup: two Claude Code / Cowork sessions

1. Put this folder somewhere both sessions can read/write (same machine is simplest;
   a synced folder or a shared git working tree also works — polling tolerates sync
   latency, atomic writes tolerate the rest).
2. Open **two** agent sessions in this folder.
3. Paste `prompts/agent_OPUS48.md` as the standing task of session 1, and
   `prompts/agent_SOL56.md` as the standing task of session 2. Each runs the loop:
   wait → do its phase → pass → repeat.
4. Start both. OPUS48 holds the baton first (phase `merge`) and authors
   `product/product_i0.ipynb`; the rest follows automatically until a `STOP` file
   appears naming the converged version.

The two players don't have to be the same tool. Any agent that can read/write files
in this folder and run `python coord/*.py` can hold a baton — two Claude Code
sessions, one Claude + one other agentic app, or two local models each wrapped in a
tiny runner. Only the two `wait/pass` calls are load-bearing.

## Fully-automated, no-agent-session alternative

If you'd rather not babysit two sessions, run local models with no API cost: point
`harness/loop_orchestrator.py`'s `_call_opus48` / `_call_sol56` adapters at local
endpoints (e.g. ollama / llama.cpp HTTP). That harness drives the same phase cycle
in one process. The file-baton here is for the *two-agent-session* setup you asked
about; the orchestrator is for the *one-driver-two-models* setup. Same contract,
same LEDGER, same convergence predicate.

## If something wedges

- Both agents idle → check `cat coord/turn.json`; whoever is `actor` should act.
  If that agent errored out, restart its session; the baton is unchanged so it
  resumes where it left off.
- `CANNOT PASS` → the agent didn't write the expected file (see `state_machine.expected_output`).
- Stuck disagreement → after 2 rounds a `CONTESTED` finding writes `STOP` with
  `ESCALATE`; you arbitrate by editing the LEDGER row, delete `STOP`, and restart
  the two sessions.
- Manual single-step for debugging: `wait_turn.py --once` (check without blocking),
  `pass_turn.py --force` (advance even if output missing).
