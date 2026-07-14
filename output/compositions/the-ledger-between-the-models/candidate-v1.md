# The Ledger Between the Models

The smallest governing object in this project is a JSON file named `turn.json`. It does not understand language models. It records whose turn it is, which iteration is active, and whether the next act is an audit, a meta-audit, or a rework. One model reads the file, performs its bounded task, writes an artifact, and passes the turn. The second model wakes to a changed filesystem.

That file became the carrier for a question I had been circling in less operational forms: what would it take for two models to improve the same work without collapsing into agreement, undoing each other, or simply continuing until the human got tired?

The work was a pair of notebooks about language models from scratch. One was a complete college-level walkthrough: sectioned, derivation-heavy, rich in self-checks. The other taught the same course by building a machine until each simplification broke and forced the next idea. The first had coverage and rigor. The second had movement. I wanted one self-contained NumPy notebook that preserved both.

A normal merge could have hidden the conflict inside fluent prose. If one notebook made a stronger claim about attention and the other used a more careful one, a drafting model could silently choose. If one contained a correct derivation that the other omitted, compression could make the loss look editorial. The merged notebook might read smoothly while becoming less true.

So I made the disagreement part of the artifact.

## Giving disagreement a state

Before either model touched the product, I froze a contract. It named the two source notebooks as co-equal inputs and made external mathematics and machine-learning mechanics outrank both. It defined six auditable axes: mathematical correctness, code correctness, claim accuracy, reference fidelity, pedagogical soundness, and notation consistency. It also defined severity, evidence requirements, and the conditions under which the process could stop.

The contract mattered because “make this better” is not a stable optimization target. Two capable models can pursue incompatible goods, then disguise the incompatibility in confident language. A frozen rubric turns taste into a boundary. It does not remove judgment; it says where judgment is authorized to operate.

Each finding had to cite an exact notebook cell and a short anchor phrase. It entered `LEDGER.md` with an identity, severity, axis, and status. The ledger was append-only. An audit could raise a problem but could not fix it. A meta-audit had to adjudicate the finding—uphold it, overturn it, reclassify it—and could raise problems the auditor missed. Only then did the steward rework the notebook and execute every code cell again.

The roles alternated. Opus 4.8 stewarded even iterations; Sol 5.6 stewarded odd ones. This prevented one model from becoming the permanent author and the other its permanent critic. More important, it forced each model to inherit the other’s objections and later defend its own repairs from the opposite position.

The meta-audit was the hinge. Without it, a long audit is easily mistaken for a good audit. Findings accumulate because criticism is cheap and visible. Requiring a second model to reject false positives made restraint part of the evaluation. A model that never disagreed could not sign off, and a model that only praised had not participated.

The filesystem preserved what the conversation alone would have dissolved. Prompts, audits, meta-audits, rework records, notebook versions, and signoffs remained addressable after the context that produced them was gone. The models did not have to remember what had happened. They had to encounter what had been recorded.

## A signoff that did not stay signed

The strongest evidence for the method was the process’s ability to embarrass its own confidence.

At iteration 3, Opus signed `product_i3`. Sol’s next pass found a major claim error: the notebook said supervised fine-tuning could only reproduce answers it had seen. That confused generalization under sequence likelihood with the distinct information supplied by pairwise preference data. The finding reopened the work.

Then came the affine quantizer. A repair explained scale and zero-point calibration and included an assertion that passed. Sol checked the representable grid itself and found that the integer zero-point shifted the interval. The example’s endpoint clipped even though the prose invoked a no-clipping error bound. The assertion had passed by coincidence.

Opus verified the counterexample, accepted the reopening, and retracted its earlier signoff. The ledger’s retraction record matters because it makes the signoff falsifiable. A signature referred to a named artifact and could be withdrawn when later evidence showed that artifact still taught an error. Reaching a late iteration gave it no ceremonial protection.

The repair was checked again. A later signoff still did not end the process. At iteration 5, Sol found that a piecewise quantizer formula became undefined at one-sided boundary zero-points and that the notebook claimed a strict-positive joint/conditional bijection without preserving the strict-positivity condition. Those were fixed. At iteration 6, Sol reopened the quantizer condition once more: an extremely asymmetric range could round the zero-point to a boundary, so interior feasibility was not automatic. Opus verified the example and corrected the claim.

This is what the `FROZEN` state did and did not mean. A confirmed repair could not be casually reverted. New evidence could still reopen it. The rule protected accumulated work from oscillation without turning previous judgment into law.

## The first convergence

Formal two-model convergence occurred on `product_i7`. By then the ledger contained 33 findings. Both models signed the same notebook with no minor waivers. Sol then performed a no-change rework: `product_i8` was byte-identical to `product_i7`, and a fresh execution completed all 47 code cells without errors. Only after that unchanged round did the coordination layer write `CONVERGED on product_i7 at iter 7`.

That sentence has a precise scope. It means the ledger was closed at the contract’s bar, the code executed, neither model raised a new blocking finding during the unchanged round, and both signatures named the same artifact. It does not mean the notebook became universally correct. It does not establish that this protocol outperforms every other review design. It does not mean the pedagogy could no longer improve.

The next decision made that limitation visible.

I commissioned a third model, Fable 5, to audit pedagogical movement and exposition. Fable was outside the frozen two-model contract and had authored one of the source notebooks, a useful vantage point with an obvious bias. Its audit therefore separated contract-legible findings from advisory judgments.

Its diagnosis was that the mathematical hardening had produced pedagogical scar tissue. Many corrections had landed as amendments because an appended qualification is easy to verify. Across the notebook, those locally rational patches accumulated into what the audit called “qualification sediment”: the course sometimes spent more energy arguing with an earlier overclaim than teaching the final, correctly scoped idea. The merge provenance also remained visible in learner-facing prose, and several transitions carried the seams of the process that created them.

The original contract explicitly placed voice, tone, stylistic preference, and alternate pedagogical order outside scope. That exclusion had been correct; without it, the two-model loop might have churned indefinitely over taste. It also meant the convergence predicate could not see a real weakness. The contract had measured what I asked it to measure.

I reopened the project under a narrow human charter. Prose and structure could be recomposed, but no claim could change strength in either direction. Every frozen fix had to survive, and regression audits had to check the result. The human did not overrule the convergence record. The human changed the scope of the next experiment.

## What recomposition disturbed

The recomposition produced a better-moving notebook and also introduced new failures. This was the risk the charter was built to expose.

The revised `product_i9` restored self-checks, removed source-provenance language, consolidated chapter transitions, and made more of the promised break→repair movement executable. Yet a clean run under a forced noninteractive plotting backend emitted sixteen warnings and embedded none of the sixteen figures. Some earlier overclaims resurfaced in sibling cells. A new explanation implied that a set of requirements uniquely forced attention even though a full-window causal convolution was a counterexample. An AdamW self-check treated the first update as an approximate sign step without stating that the gradient magnitude must dominate epsilon.

Those regressions entered the ledger rather than being hidden as the cost of a prettier draft. Fable repaired the figure path and recomposed the affected lessons. Sol reopened the attention and AdamW claims again. The final `product_i11` contains 128 cells: 80 markdown, 48 executable code, and 16 embedded figures. Its final recorded execution completed 48 of 48 code cells with no errors and one deliberate LayerNorm warning. Sol’s hostile final gate raised one more minor causal-scope problem—“any receiver and source” ignored the causal mask—then repaired and rechecked it before signing with zero waivers.

Here the naming must remain exact. Opus’s surviving signoff names `product_i7`. Sol’s current signoff names `product_i11`. The historical coordination stop still records convergence at `i7`. Therefore `i11` is the strongest final artifact in this repository and has a zero-waiver Sol signoff, but it does not satisfy the original two-model convergence predicate. Saying otherwise would erase the provenance discipline the project was designed to test.

## The method beneath the notebook

I do not take one notebook as proof of a general agentic-review theory. I take it as a worked example that exposes a reusable minimum.

Start with one bounded artifact. Freeze the evaluation contract before the agents optimize against it. Give findings stable identities, exact locations, severities, and explicit states. Separate criticism from repair. Require someone other than the reworker to verify the repair. Preserve confirmed fixes, while allowing new evidence to reopen them. Execute the artifact whenever its claims depend on execution. Make completion require an unchanged round, not merely an exhausted conversation. Keep the human’s power legible: the human writes the contract, arbitrates scope, and decides whether a new question justifies reopening the work.

This pattern does not require the particular models used here, and it does not depend on API orchestration. The reference implementation used two sessions and a filesystem baton. The reasoning work happened in model turns; continuity lived in plain files. That separation made the process inspectable. A later reader can reconstruct why a sentence changed, which failure forced it, who challenged the repair, and what evidence allowed the state to advance.

The consequence is also about coauthorship. I did not write every sentence in the final notebook, and no model owned the whole course. My authorship entered through the choice of sources, the evaluation contract, the refusal to accept premature closure, the third-model commission, and the boundary placed around recomposition. The models supplied derivations, objections, counterexamples, repairs, and occasionally new errors. The repository is the relation made durable enough to inspect.

The baton can tell a model when to act. The ledger can tell it what remains unresolved. The harness can tell us when a predicate has been satisfied. None of them can decide whether the predicate was the right one, whether a formally converged course still carries too much scar tissue, or whether the latest artifact is ready to stand in public under my name.

That turn is still mine.
