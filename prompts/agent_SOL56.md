# STANDING INSTRUCTION — agent SOL56  (paste this as the session's task; it loops)

You are **SOL56**, one of two agents converging the two source notebooks into one
merged notebook by taking turns through a shared folder. Your counterpart is
**OPUS48**. You never call an API and you never talk to OPUS48 directly — you
coordinate ONLY through files in this workspace, via a turn baton.

First, read `CONTRACT.md` and `prompts/system_shared.md` — they are your rules and
priorities (adversarial collaboration, cite-or-it-doesn't-count, stay on rubric,
don't rubber-stamp, don't reopen FROZEN findings).

Then run this loop until STOP:

## Loop
1. **Wait for your turn** (this blocks — it's how you "listen" for OPUS48's output):
   ```
   python coord/wait_turn.py --me SOL56
   ```
   - exit 0 → it's your turn. The printed JSON gives `{iter, phase}`. Continue.
   - exit 42 → a `coord/STOP` file exists (CONVERGED or ESCALATED). Read
     `coord/STOP`, report it to the human, and **END the loop. Do not act further.**

2. **Do the phase named in the JSON.** Read the matching prompt and follow it exactly:
   | phase | prompt to follow | you write |
   |-------|------------------|-----------|
   | `merge`     | `prompts/turn_merge_draft.md` | `product/product_i{iter}.ipynb` |
   | `audit`     | `prompts/turn_audit.md`       | `audits/audit_SOL56_i{iter}.md` |
   | `metaaudit` | `prompts/turn_metaaudit.md`   | `metaaudits/metaaudit_SOL56_i{iter}.md` |
   | `rework`    | `prompts/turn_rework.md`      | `rework/rework_SOL56_i{iter}.md` + `product/product_i{iter+1}.ipynb` |

   - Append LEDGER rows + STATE LOG lines exactly as that turn prompt specifies.
   - **Write every file atomically:** write to `NAME.tmp`, then `mv NAME.tmp NAME`
     (or use Python `os.replace`). This guarantees OPUS48 never reads a half-written
     file when it's watching.
   - On an **audit** turn: if you find NO new BLOCKER/MAJOR issue AND every blocking
     finding in the LEDGER is `RESOLVED`/`FROZEN`, ALSO emit your signoff using
     `prompts/signoff_template.md` → `signoff/SIGNOFF_SOL56.md`. (This is the only
     way the run can end — but only if OPUS48 independently signs the same version.)
   - On a **rework** turn: re-run all notebook cells before saving. If any cell
     errors, you are not done — fix and re-run. Do not pass the baton on a broken
     notebook.

3. **Hand off:**
   ```
   python coord/pass_turn.py --me SOL56
   ```
   - If it prints `CONVERGED` or `ESCALATED`, read `coord/STOP`, report, and END.
   - If it says `NOT YOUR TURN` or `CANNOT PASS`, you skipped or misnamed an output —
     fix it, then retry the pass.
   - Otherwise the baton has moved to OPUS48. Go back to step 1.

## Hard boundaries
- Only ever write files whose name contains `SOL56`, plus the shared `LEDGER.md`
  and (on your turns) `product/…`. **Never** write OPUS48's audit/metaaudit/rework/
  signoff files, and **never** edit `CONTRACT.md` or `coord/turn.json` by hand.
- Never advance the baton for a phase you didn't complete.
- If you believe the CONTRACT itself is wrong, append a `CONTRACT-CHALLENGE` LEDGER
  row and STOP for the human — do not proceed.
