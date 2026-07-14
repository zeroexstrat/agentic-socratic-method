#!/usr/bin/env python3
"""Block until it is my turn. This is the "listen" half of the loop.

Usage:  python coord/wait_turn.py --me OPUS48
Exit codes:
  0  -> it's your turn. stdout is the turn JSON: {iter, phase, actor, seq}.
  42 -> STOP file present (CONVERGED or ESCALATED). stdout is the STOP message. Stop working.

Polls turn.json by mtime/content every --poll seconds. Reads are safe against a
concurrent write because pass_turn writes atomically (temp + os.replace), so this
never sees a half-written baton. Works across a synced folder (Dropbox/git) too,
subject to that sync's latency.
"""
import argparse
import json
import sys
import time
from pathlib import Path

COORD = Path(__file__).resolve().parent
TURN = COORD / "turn.json"
STOP = COORD / "STOP"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--me", required=True, choices=["OPUS48", "SOL56"])
    ap.add_argument("--poll", type=float, default=2.0)
    ap.add_argument("--once", action="store_true",
                    help="check once and exit (exit 1 if not your turn) — for manual/debug use")
    a = ap.parse_args()

    while True:
        if STOP.exists():
            print(STOP.read_text().strip())
            sys.exit(42)
        try:
            s = json.loads(TURN.read_text())
        except (FileNotFoundError, json.JSONDecodeError):
            if a.once:
                sys.exit(1)
            time.sleep(a.poll)
            continue

        if s.get("actor") == a.me:
            print(json.dumps(s))
            sys.exit(0)

        if a.once:
            print(f"waiting: baton held by {s.get('actor')} (phase {s.get('phase')}, iter {s.get('iter')})")
            sys.exit(1)
        time.sleep(a.poll)


if __name__ == "__main__":
    main()
