"""Convergence predicate + anti-collapse / anti-oscillation guards.

State lives in LEDGER.md, not in either model's word. These functions read the
ledger and decide whether the loop may terminate. The models never self-certify
termination — the harness does, using this module.
"""
from __future__ import annotations
import re
from dataclasses import dataclass
from pathlib import Path

SEV_BLOCKING = {"BLOCKER", "MAJOR"}
SUBSTANTIVE_SEV = {"BLOCKER", "MAJOR"}  # MINOR counts only if upheld; see below


@dataclass
class Finding:
    id: str
    raised_by: str
    iter: int
    axis: str
    sev: str
    status: str
    loc: str
    note: str


_ROW = re.compile(r"^\|\s*(F-\d+)\s*\|\s*(\w+)\s*\|\s*(\d+)\s*\|\s*([\w—-]+)\s*\|"
                  r"\s*([\w—-]+)\s*\|\s*([\w—-]+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$")


def parse_ledger(ledger_path: Path) -> list[Finding]:
    """Parse the current (post-STATE-LOG-applied) status of each finding.

    The ledger table holds each finding once; the STATE LOG below it records
    transitions. We fold the STATE LOG over the table so a row's *effective*
    status reflects the latest transition. STATE LOG lines look like:
        i{n} · {MODEL} · <verb> F-012 ...   with verbs mapping to statuses.
    """
    text = ledger_path.read_text(encoding="utf-8")
    findings: dict[str, Finding] = {}
    for line in text.splitlines():
        m = _ROW.match(line.strip())
        if not m:
            continue
        fid, by, it, axis, sev, status, loc, note = m.groups()
        if fid == "F-000":
            continue  # example row
        findings[fid] = Finding(fid, by, int(it), axis, sev, status, loc, note)

    # Fold STATE LOG transitions (verb -> status).
    verb_status = {
        "raised": "OPEN", "accepted": "ACCEPTED", "upheld": "ACCEPTED",
        "rejected": "REJECTED", "overturned": "REJECTED",
        "resolved": "RESOLVED", "frozen": "FROZEN", "contested": "CONTESTED",
        "reopened": "OPEN",
    }
    log_start = text.find("STATE LOG")
    if log_start != -1:
        for line in text[log_start:].splitlines():
            for verb, st in verb_status.items():
                for fid in re.findall(r"F-\d+", line):
                    if verb in line.lower() and fid in findings:
                        findings[fid].status = st
    return list(findings.values())


def substantive_count(findings: list[Finding], model: str) -> int:
    """Findings that count toward a model's anti-collapse quota: MAJOR+ it raised,
    plus MINORs it raised that survived meta-audit (status not REJECTED)."""
    n = 0
    for f in findings:
        if f.raised_by != model:
            continue
        if f.sev in SUBSTANTIVE_SEV and f.status != "REJECTED":
            n += 1
        elif f.sev == "MINOR" and f.status in {"ACCEPTED", "RESOLVED", "FROZEN"}:
            n += 1
    return n


def blocking_open(findings: list[Finding]) -> list[Finding]:
    return [f for f in findings
            if f.sev in SEV_BLOCKING and f.status in {"OPEN", "CONTESTED", "ACCEPTED"}]


def stale_contested(findings: list[Finding], current_iter: int, limit: int) -> list[Finding]:
    """CONTESTED for >= `limit` rounds -> must escalate to human/tiebreak."""
    return [f for f in findings
            if f.status == "CONTESTED" and (current_iter - f.iter) >= limit]


def read_signoff(path: Path) -> dict | None:
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    def grab(key):
        m = re.search(rf"{key}:\s*(.+)", text)
        return m.group(1).strip() if m else None
    return {
        "version_signed": grab("version_signed"),
        "findings_logged": grab("findings_i_logged_this_run"),
        "has_strongest_objection": "strongest_remaining_objection" in text
                                   and "nothing" not in text.lower().split(
                                       "strongest_remaining_objection")[-1][:80],
        "raw": text,
    }


def signoff_valid(sig: dict | None, model: str, findings: list[Finding],
                  min_findings: int) -> tuple[bool, str]:
    if sig is None:
        return False, f"{model}: no signoff present"
    if not sig["version_signed"]:
        return False, f"{model}: signoff names no version"
    if not sig["has_strongest_objection"]:
        return False, f"{model}: signoff lacks a real strongest_remaining_objection"
    got = substantive_count(findings, model)
    if got < min_findings:
        return False, f"{model}: only {got} substantive findings (need {min_findings}) — anti-collapse"
    return True, f"{model}: valid, signed {sig['version_signed']}"


def converged(findings: list[Finding], sig_opus: dict | None, sig_sol: dict | None,
              product_unchanged_this_round: bool, min_findings: int) -> tuple[bool, list[str]]:
    reasons = []
    ok = True

    blk = blocking_open(findings)
    if blk:
        ok = False
        reasons.append(f"{len(blk)} blocking finding(s) still open: {[f.id for f in blk]}")

    if not product_unchanged_this_round:
        ok = False
        reasons.append("product changed this round; need one clean round with no edits")

    v_opus, msg_o = signoff_valid(sig_opus, "OPUS48", findings, min_findings)
    v_sol, msg_s = signoff_valid(sig_sol, "SOL56", findings, min_findings)
    reasons += [msg_o, msg_s]
    if not (v_opus and v_sol):
        ok = False

    if v_opus and v_sol and sig_opus["version_signed"] != sig_sol["version_signed"]:
        ok = False
        reasons.append("signoffs name different versions")

    return ok, reasons
