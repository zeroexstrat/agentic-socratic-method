"""The turn state machine. One place defines whose turn is next, so agents never
have to reason about it — they just call pass_turn and the baton advances here.

A turn is (iter, phase, actor). Phases: merge (once), audit, metaaudit, rework.
Steward owns merge+metaaudit+rework; auditor owns audit. Roles swap each iteration.
"""

def steward(it: int) -> str:
    return "OPUS48" if it % 2 == 0 else "SOL56"


def auditor(it: int) -> str:
    return "SOL56" if it % 2 == 0 else "OPUS48"


def initial() -> dict:
    return {"iter": 0, "phase": "merge", "actor": steward(0), "seq": 0}


def next_state(s: dict) -> dict:
    it, ph, seq = s["iter"], s["phase"], s["seq"]
    if ph == "merge":
        return {"iter": it, "phase": "audit", "actor": auditor(it), "seq": seq + 1}
    if ph == "audit":
        return {"iter": it, "phase": "metaaudit", "actor": steward(it), "seq": seq + 1}
    if ph == "metaaudit":
        return {"iter": it, "phase": "rework", "actor": steward(it), "seq": seq + 1}
    if ph == "rework":
        nit = it + 1
        # previous steward becomes next auditor — the natural role swap
        return {"iter": nit, "phase": "audit", "actor": auditor(nit), "seq": seq + 1}
    raise ValueError(f"unknown phase: {ph}")


def expected_output(s: dict) -> list[str]:
    """Files the current actor must have written before it may pass the baton."""
    it, ph, me = s["iter"], s["phase"], s["actor"]
    return {
        "merge":     [f"product/product_i{it}.ipynb"],
        "audit":     [f"audits/audit_{me}_i{it}.md"],
        "metaaudit": [f"metaaudits/metaaudit_{me}_i{it}.md"],
        "rework":    [f"rework/rework_{me}_i{it}.md", f"product/product_i{it+1}.ipynb"],
    }[ph]
