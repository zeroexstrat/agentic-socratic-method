# Adversarial audit — candidate-v1 → candidate-v2

Auditing `candidate-v1.md` against a fixed standard: Rafael's technical-expository voice (the
register of `writing/model-in-the-sentence.html`), the brief's obligations and must-avoids, and
the instruction to foreground the *general movement and design* over blow-by-blow iterations.
candidate-v1 is a strong draft; these are the findings that produced candidate-v2.

## Findings

### F1 · EMPHASIS · major — the middle reads as an iteration timeline
- loc: "A signoff that did not stay signed" and "What recomposition disturbed"
- wrong: The draft narrates chronology — "At iteration 3… At iteration 5… At iteration 6…" —
  which is exactly the shape that reads as machine-generated. The interesting object is the
  *mechanism* (a signoff that can be retracted; a frozen state that still yields to evidence),
  not the calendar.
- fix: Collapse the timeline into one vivid, load-bearing episode (the quantizer assertion that
  passed by coincidence and the retracted signoff), then state the *principle* it demonstrates.
  The two later recurrences become one clause, not three dated beats.

### F2 · VOICE · major — build-report stat dumps
- loc: "128 cells: 80 markdown, 48 executable code, and 16 embedded figures. Its final recorded
  execution completed 48 of 48 code cells… sixteen warnings and embedded none of the sixteen"
- wrong: Spec-sheet counts read as a CI log, not Rafael's prose. They also invite the "list of
  features" failure the brief warns against.
- fix: Keep only numbers that carry meaning — *thirty-three findings*, and the version identity
  at the convergence boundary. Drop cell/figure/warning counts; describe the final artifact
  qualitatively (strongest, zero-waiver, hostile final pass).

### F3 · VOICE · minor — a few generic-essay seams
- loc: "The strongest evidence for the method was the process's ability to embarrass its own
  confidence."; "This is what the FROZEN state did and did not mean."
- fix: Re-anchor in first person and concrete consequence ("The part I trust most is that the
  method could catch itself being sure."). Preserve the genuinely strong lines ("So I made the
  disagreement part of the artifact."; "That turn is still mine.").

### F4 · STRUCTURE · minor — five sections track phases; thematic movement is stronger
- fix: Four movements — problem, giving disagreement a state, the process catching itself,
  convergence and its blind spot, the method under the notebook — so the essay reads as an
  argument, not a log.

## Must-preserve (verified retained in v2)
- The exact status boundary: two-model zero-waiver convergence names **product_i7**; the final
  **product_i11** is signed by one model only and does **not** satisfy the original predicate.
  (Stated explicitly; not blurred by compression.)
- Fable sits **outside** the frozen two-model contract and authored one source (vantage + bias).
- Agreement is never described as proof of truth; the reusable pattern is a governance method,
  not a benchmark; no invented counts, citations, or capabilities.
- Opens on the baton (`turn.json`); ends on human judgment, implicitly (no explicit "this is how
  I work with agents" thesis — that phrasing is the AI-slop tell the piece must avoid).

## Result
candidate-v2: ~2,000 words (brief window 1,800–2,400). Timeline compressed to two illustrative
failure-and-reopening episodes; design foregrounded (contract, append-only ledger, separated
audit/rework, meta-audit as the hinge, executable checks, unchanged-round completion); recruiter
signal carried by the reasoning, not a pitch.
