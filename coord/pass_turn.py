#!/usr/bin/env python3
"""Advance the baton after I finish my turn. This is the "hand off" half.

Usage:  python coord/pass_turn.py --me OPUS48

What it does, in order:
  1. Refuses if the baton isn't currently yours (prevents out-of-turn writes).
  2. Verifies you actually produced this phase's expected output file(s).
  3. If the phase is `rework`: runs the convergence + escalation checks. On
     convergence or stale-contested it writes coord/STOP and does NOT advance.
  4. Otherwise advances turn.json atomically to the next (iter, phase, actor).

Termination is decided HERE (via convergence.py), never by an agent's say-so.
"""
import argparse
import json
import os
import sys
from pathlib import Path

COORD = Path(__file__).resolve().parent
ROOT = COORD.parent
TURN = COORD / "turn.json"
STOP = COORD / "STOP"

sys.path.insert(0, str(COORD))
sys.path.insert(0, str(ROOT / "harness"))
import state_machine as sm          # noqa: E402
import convergence as cv            # noqa: E402

MIN_FINDINGS = 3                    # keep in sync with harness/config.yaml
CONTESTED_LIMIT = 2


def atomic_write(p: Path, text: str) -> None:
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, p)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--me", required=True, choices=["OPUS48", "SOL56"])
    ap.add_argument("--force", action="store_true",
                    help="advance even if expected output is missing (debug only)")
    a = ap.parse_args()

    if STOP.exists():
        print(STOP.read_text().strip(), "\n(STOP already set; not advancing.)")
        return

    s = json.loads(TURN.read_text())
    if s["actor"] != a.me:
        print(f"NOT YOUR TURN: baton held by {s['actor']} "
              f"(phase {s['phase']}, iter {s['iter']}). Nothing done.")
        sys.exit(3)

    # 2. verify this turn's artifacts exist
    missing = [f for f in sm.expected_output(s) if not (ROOT / f).exists()]
    if missing and not a.force:
        print("CANNOT PASS — you have not written this phase's output:")
        for f in missing:
            print("  missing:", f)
        sys.exit(4)

    # 3. convergence / escalation only at end of a rework
    if s["phase"] == "rework":
        i = s["iter"]
        findings = cv.parse_ledger(ROOT / "LEDGER.md")

        stale = cv.stale_contested(findings, i, CONTESTED_LIMIT)
        if stale:
            atomic_write(STOP, f"ESCALATE at iter {i}: contested >= {CONTESTED_LIMIT} rounds "
                               f"{[f.id for f in stale]} — human arbitration needed.")
            print("ESCALATED — see coord/STOP. Both agents will stop.")
            return

        cur = ROOT / f"product/product_i{i}.ipynb"
        nxt = ROOT / f"product/product_i{i+1}.ipynb"
        changed = nxt.exists() and cur.read_bytes() != nxt.read_bytes()
        sig_o = cv.read_signoff(ROOT / "signoff/SIGNOFF_OPUS48.md")
        sig_s = cv.read_signoff(ROOT / "signoff/SIGNOFF_SOL56.md")
        ok, reasons = cv.converged(findings, sig_o, sig_s,
                                   product_unchanged_this_round=not changed,
                                   min_findings=MIN_FINDINGS)
        if ok:
            atomic_write(STOP, f"CONVERGED on {sig_o['version_signed']} at iter {i}.")
            print("CONVERGED — see coord/STOP.")
            return
        print("not converged this round:")
        for r in reasons:
            print("  -", r)

    nxt_state = sm.next_state(s)
    atomic_write(TURN, json.dumps(nxt_state, indent=2))
    print(f"baton -> {nxt_state['actor']} (phase {nxt_state['phase']}, iter {nxt_state['iter']})")


if __name__ == "__main__":
    main()
