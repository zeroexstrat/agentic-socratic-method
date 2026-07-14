# The Ledger Between the Models

The smallest thing governing this project is a JSON file called `turn.json`. It knows nothing about language models. It records whose turn it is, which iteration is live, and whether the next act is an audit, a meta-audit, or a rework. A model reads the file, does its one bounded job, writes an artifact, and passes the turn. The other model wakes to a changed filesystem and no memory of the conversation that changed it.

I built that file to carry a question I had been circling in softer forms: what would it take for two models to improve the same work without collapsing into agreement, quietly undoing each other, or grinding on until I lost patience and called it done?

The work was a pair of notebooks that teach language models from scratch. One was a complete, sectioned, derivation-heavy walkthrough, thick with self-checks. The other taught the same material by building a machine until each simplification broke and forced the next idea. The first had coverage and rigor. The second had movement. I wanted a single self-contained NumPy notebook that kept both.

The trouble is that a normal merge hides exactly the disagreements worth keeping. Where one notebook made a sharper claim about attention and the other a more careful one, a drafting model could silently pick. Where one carried a derivation the other dropped, compression could make the loss look like an editorial choice. The merged notebook would read smoothly and become less true, and nothing in the prose would tell me it had happened.

So I made the disagreement part of the artifact.

## Giving disagreement a state

Before either model touched the notebook, I froze a contract. It named the two sources as co-equal inputs and put external mathematics above both of them, so that when they conflicted the tie broke on the math and not on whichever draft sounded more confident. It fixed six axes anything could be judged on — mathematical correctness, code correctness, claim accuracy, reference fidelity, pedagogical soundness, notation — and it defined severity, the evidence a finding had to carry, and the exact conditions under which the process was allowed to stop.

The contract matters because "make this better" is not a stable target. Two capable models can want incompatible things and then bury the incompatibility in fluent language. A frozen rubric does not remove judgment. It says where judgment is allowed to operate, and it makes the rest legible.

Every finding had to cite a specific cell and a short anchor phrase, and it entered an append-only ledger with an identity, an axis, a severity, and a state. The separation of powers was the point. An audit could raise a problem but could not fix it. A meta-audit had to rule on the finding — uphold it, overturn it, reclassify it — and was expected to catch what the auditor had missed. Only then did the steward rework the notebook and re-run every cell.

Stewardship alternated: one model owned the even iterations, the other the odd. Neither became the permanent author or the permanent critic. Each had to inherit the other's objections and then defend its own repairs from the opposite chair.

The meta-audit was the hinge. A long audit is easy to mistake for a good one, because criticism is cheap and visible and findings pile up on their own. Requiring a second model to throw out the false positives made restraint part of the score. A model that agreed with everything could not sign off, and a model that only praised had not really shown up.

The filesystem held what a conversation would have dissolved. Prompts, audits, meta-audits, rework notes, notebook versions, signoffs — all of it stayed addressable after the context that produced it was gone. The models did not have to remember what happened. They had to encounter what was written down.

## The process catching itself

The part I trust most is that the method could catch itself being sure.

At one point a steward signed off on a version it believed was finished. The next pass went after the claim underneath a quantizer example. The prose explained scale and zero-point calibration and carried an assertion that passed — and the assertion passed by coincidence. When the other model recomputed the representable grid, the rounded integer zero-point had shifted the interval, and the example's own endpoint clipped: exactly the case the surrounding error bound said could not occur. The test had been green for the wrong reason.

The steward verified the counterexample, accepted the reopening, and withdrew its own signoff.

I care about that retraction more than about any single fix. It means a signature was falsifiable. It pointed at a named version and could be taken back when later evidence showed that version still taught something false, and reaching a late iteration bought it no ceremonial protection. The same claim came back twice more under narrower conditions — an asymmetric range that could round the zero-point onto a boundary and quietly break the feasibility the text assumed — and each time it was reopened, checked, and repaired.

This is the entire use of a frozen state. A confirmed fix could not be casually reverted, which kept the two models from thrashing the same cell back and forth. New evidence could still reopen it. The rule protected accumulated work from oscillation without turning yesterday's judgment into law.

## Convergence, and the thing it could not see

Formal convergence came on the seventh version, `product_i7`. By then the ledger held thirty-three findings. Both models signed the same notebook with nothing waived, one model ran an unchanged round that altered nothing and executed cleanly, and only then did the coordination layer record that the work had converged.

That word has a narrow meaning here. It means the ledger was closed at the contract's bar, the code ran, neither model raised a new blocking finding in the unchanged round, and both signatures named the same artifact. It does not mean the notebook was now universally correct, and it does not mean this protocol beats every other way of reviewing work. It means what the contract was built to measure, and no more.

The next decision is the one I find most honest, because it went looking for what the contract could not measure.

I brought in a third model to read only for pedagogy and exposition. It sat outside the frozen two-model contract, and it had authored one of the source notebooks — a real vantage point with an obvious bias, which is why its report kept contract-legible findings apart from advisory ones. Its diagnosis was that all the mathematical hardening had left scar tissue. Most corrections had landed as appended qualifications, because a qualification is easy to verify, and those locally reasonable patches had accumulated into sediment: in places the course spent more energy arguing with an earlier overclaim than teaching the idea it had finally gotten right. The seams of the process were visible in the thing the process made.

The contract had put voice, tone, and pedagogical order out of scope on purpose. That exclusion was correct — without it the two-model loop could have churned forever over taste — but it also meant the convergence predicate was structurally unable to see a genuine weakness. The contract measured what I told it to measure. Nothing else was going to surface on its own.

So I reopened the work, under a charter I wrote by hand and kept deliberately narrow. Prose and structure could be recomposed; no claim was allowed to change strength in either direction; every frozen fix had to survive; regression audits had to prove it. I did not overrule the convergence record. I changed the scope of the next experiment.

Recomposition made the notebook move better and introduced new failures — which was the charter's purpose, not a surprise. A cleaner draft brought back a few of the old overclaims in neighboring cells and broke a figure path, so that a clean run emitted its plots into nothing. Those regressions entered the ledger like any other finding, were reopened by the model that had not made them, and were repaired and rechecked.

The final notebook, `product_i11`, is the strongest artifact in the repository, and it carries a zero-waiver signoff from one of the two models after a deliberately hostile final pass. Here the naming has to stay exact, because the exactness *is* the discipline. One model's surviving signoff still names `product_i7`. The historical convergence stop still records that version, not this one. `product_i11` is signed by one model, not two, and it does not satisfy the original two-model convergence predicate. It is better, and it is signed once. Both are true, and collapsing them would erase the provenance the project was built to test.

## The method under the notebook

I do not take one notebook as proof of a general theory of agentic review. I take it as a worked example that exposes a reusable minimum.

Start from one bounded artifact. Freeze the evaluation contract before the agents can optimize against it. Give findings stable identities, exact locations, severities, and explicit states. Keep criticism separate from repair, and make someone other than the reworker verify the repair. Preserve confirmed fixes, but let new evidence reopen them. Execute the artifact whenever its claims depend on execution. Make completion require a round that changed nothing, not a conversation that ran out of energy. And keep the human's authority legible: the human writes the contract, arbitrates scope, and decides whether a new question is worth reopening the work.

None of that depended on the particular models, and none of it depended on an orchestration layer wired through an API. The reference version was two sessions and a file passed between them. The reasoning happened in the model turns; the continuity lived in plain files, which is what made the whole thing inspectable. Someone can still open the repository and reconstruct why a sentence changed, which failure forced it, who challenged the repair, and what evidence let the state advance.

What I keep returning to is the shape of the authorship. I did not write every sentence in the final notebook, and no model owned the course. My part entered through the choice of sources, the contract, the refusal to accept an early ending, the decision to bring in a third reader, and the boundary I drew around what recomposition was allowed to touch. The models supplied the derivations, the objections, the counterexamples, the repairs, and now and then a fresh error. The repository is that relationship, made durable enough to inspect.

The baton can tell a model when to act. The ledger can tell it what is still unresolved. The harness can tell us when a predicate has been met. None of them can decide whether the predicate was the right one, whether a formally converged course still carries too much scar tissue, or whether the latest version is ready to go out in public under my name.

That turn is still mine.
