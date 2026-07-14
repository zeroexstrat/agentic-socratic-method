"""Cross-model iterative auditing orchestrator (stub).

The two models never talk directly. This relay passes files. Each round:

    iteration n (steward S, auditor A):
      1. A  AUDIT      product_i{n}      -> audit_A_i{n}.md      (+ OPEN rows)
      2. S  META-AUDIT audit_A_i{n}.md   -> metaaudit_S_i{n}.md  (+ ACCEPTED/REJECTED/CONTESTED)
      3. S  REWORK     ledger            -> rework_S_i{n}.md, product_i{n+1}.ipynb
      4. either model may emit SIGNOFF once the predicate looks met
      5. harness checks convergence; else swap roles, n += 1

The convergence check and the anti-collapse / anti-oscillation / anti-deadlock
guards live in convergence.py — NOT in the models. Fill in the two _call_* adapters
with your actual API clients; everything else is provider-agnostic.
"""
from __future__ import annotations
import shutil
from pathlib import Path

import yaml  # pip install pyyaml
import convergence as cv

HERE = Path(__file__).resolve().parent
CFG = yaml.safe_load((HERE / "config.yaml").read_text())
ROOT = (HERE / CFG["workspace_root"]).resolve()

PROMPTS = ROOT / "prompts"


# ----------------------------------------------------------------------------
# Model adapters — the ONLY provider-specific code. Each takes a fully assembled
# prompt (system + turn + attached file contents) and returns the model's text.
# The turn prompts instruct the model to emit exactly one artifact; the harness
# writes whatever the model returns to the expected path, so your adapter should
# return the file body verbatim (no code fences, no preamble).
# ----------------------------------------------------------------------------
def _call_opus48(system: str, user: str, attachments: dict[str, str]) -> str:
    # TODO: wire the Anthropic Messages API (model = CFG['models']['OPUS48']['model']).
    # Attach `attachments` (filename -> text) as context; return the artifact body.
    raise NotImplementedError("wire Opus 4.8 client")


def _call_sol56(system: str, user: str, attachments: dict[str, str]) -> str:
    # TODO: wire the second provider (Sol 5.6). Same contract as above.
    raise NotImplementedError("wire Sol 5.6 client")


ADAPTERS = {"OPUS48": _call_opus48, "SOL56": _call_sol56}


# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------
def steward_for(n: int) -> str:
    even = CFG["roles"]["steward_on_even_iter"]
    other = "SOL56" if even == "OPUS48" else "OPUS48"
    return even if n % 2 == 0 else other


def auditor_for(n: int) -> str:
    return "SOL56" if steward_for(n) == "OPUS48" else "OPUS48"


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def notebook_text(path: Path) -> str:
    """Cell-indexed plaintext of a notebook so findings can cite `cell {index}`.
    Uses the same 0-based top-to-bottom indexing the prompts assume."""
    import json
    nb = json.loads(path.read_text())
    out = []
    for i, c in enumerate(nb["cells"]):
        src = "".join(c["source"])
        out.append(f"===== cell {i} [{c['cell_type']}] =====\n{src}")
    return "\n\n".join(out)


def assemble_system(model: str) -> str:
    other = "SOL56" if model == "OPUS48" else "OPUS48"
    return read(PROMPTS / "system_shared.md").replace("{SELF}", model).replace("{OTHER}", other)


def assemble_turn(turn_file: str, model: str, n: int) -> str:
    other = "SOL56" if model == "OPUS48" else "OPUS48"
    return (read(PROMPTS / turn_file)
            .replace("{SELF}", model).replace("{OTHER}", other)
            .replace("{n}", str(n)).replace("{n-1}", str(n - 1)).replace("{n+1}", str(n + 1)))


def context_files(n: int) -> dict[str, str]:
    return {
        "CONTRACT.md": read(ROOT / "CONTRACT.md"),
        "LEDGER.md": read(ROOT / "LEDGER.md"),
        "product_i{n}.ipynb (cell-indexed)": notebook_text(ROOT / f"product/product_i{n}.ipynb"),
        "reference_99.ipynb (cell-indexed)": notebook_text(
            ROOT / "source/99_complete_college_level_walkthrough.ipynb"),
    }


def product_changed(n: int) -> bool:
    a = ROOT / f"product/product_i{n}.ipynb"
    b = ROOT / f"product/product_i{n+1}.ipynb"
    if not b.exists():
        return False
    return a.read_bytes() != b.read_bytes()


# ----------------------------------------------------------------------------
# One round
# ----------------------------------------------------------------------------
def run_round(n: int) -> None:
    S, A = steward_for(n), auditor_for(n)
    print(f"\n=== iteration {n}: steward={S}  auditor={A} ===")

    # 1. AUDIT
    body = ADAPTERS[A](assemble_system(A), assemble_turn("turn_audit.md", A, n), context_files(n))
    (ROOT / f"audits/audit_{A}_i{n}.md").write_text(body, encoding="utf-8")

    # 2. META-AUDIT (audit the audit)
    ctx = context_files(n) | {f"audit_{A}_i{n}.md": body}
    body = ADAPTERS[S](assemble_system(S), assemble_turn("turn_metaaudit.md", S, n), ctx)
    (ROOT / f"metaaudits/metaaudit_{S}_i{n}.md").write_text(body, encoding="utf-8")

    # NOTE: the model is instructed to append LEDGER rows itself. If you prefer the
    # harness to own the ledger, parse `body` here and write rows deterministically.

    # 3. REWORK -> next product. The rework prompt tells the model to emit the
    # rework md AND the new notebook JSON; split on a sentinel your adapter enforces,
    # or run two calls (one for the md, one that returns the edited notebook JSON).
    rework_md = ADAPTERS[S](assemble_system(S), assemble_turn("turn_rework.md", S, n),
                            context_files(n) | {f"metaaudit_{S}_i{n}.md": body})
    (ROOT / f"rework/rework_{S}_i{n}.md").write_text(rework_md, encoding="utf-8")
    # TODO: apply edits from rework_md to product_i{n}.ipynb -> product_i{n+1}.ipynb,
    # then execute all cells (nbclient) if guards.run_code_cells. If any cell errors,
    # the rework is not done — loop the rework turn before advancing.
    if not (ROOT / f"product/product_i{n+1}.ipynb").exists():
        shutil.copy(ROOT / f"product/product_i{n}.ipynb", ROOT / f"product/product_i{n+1}.ipynb")


def check_and_maybe_finish(n: int) -> bool:
    findings = cv.parse_ledger(ROOT / "LEDGER.md")

    stale = cv.stale_contested(findings, n, CFG["guards"]["contested_rounds_before_escalation"])
    if stale:
        print(f"ESCALATE (contested >= {CFG['guards']['contested_rounds_before_escalation']} rounds): "
              f"{[f.id for f in stale]}")
        if CFG["guards"]["tiebreak_model"]:
            pass  # TODO: call tiebreak model, write CONTESTED->resolution row
        else:
            print("  no tiebreak_model set -> hand these to the human and pause.")
            return True  # pause the loop

    sig_o = cv.read_signoff(ROOT / "signoff/SIGNOFF_OPUS48.md")
    sig_s = cv.read_signoff(ROOT / "signoff/SIGNOFF_SOL56.md")
    ok, reasons = cv.converged(findings, sig_o, sig_s,
                               product_unchanged_this_round=not product_changed(n),
                               min_findings=CFG["guards"]["min_substantive_findings_per_model"])
    print("convergence check:")
    for r in reasons:
        print("  -", r)
    if ok:
        print(f"\nCONVERGED on {sig_o['version_signed']}.")
    return ok


def main() -> None:
    for n in range(CFG["guards"]["max_iterations"]):
        run_round(n)
        if check_and_maybe_finish(n):
            return
    print(f"\nHit max_iterations={CFG['guards']['max_iterations']} without convergence. "
          f"Handing unresolved LEDGER rows to human.")


if __name__ == "__main__":
    main()
