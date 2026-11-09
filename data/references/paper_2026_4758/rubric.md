# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes well-defined sampling from reverse time infinity, proves that the sampled event times lie strictly between the current time and zero almost surely, and concludes that exactly d non-mask replacements occur. Correctly handles uniform masked-index selection.
- **3 points:** Establishes the exact/learned path comparison: derives or otherwise justifies the true token conditional, the common time and index kernels, and the fact that the learned token law is evaluated at the newly sampled event time. Gives a valid construction or justification of the exact path's terminal law q_0.
- **3 points:** Computes or validly bounds the relevant joint/path KL while retaining the predictor's time dependence, identifies the accumulated error with the primitive integrated score-entropy loss, and transfers the bound to the output. Any required event-time/context distribution or equivalent occupation calculation must be justified rather than imported as an unexplained specialized identity.
- **2 points:** Supplies a valid equality construction for every finite ε≥0 on the fixed allowed alphabet and dimension, computes both the integrated loss and the output KL, and shows both equal ε.

# Evaluator Notes

Accept any complete valid alternative proof, including a joint random-order representation, a direct occupation calculation, or another rigorous divergence argument. Do not require the reference proof's notation, use of the word 'decoupling', explicit NELBO calculation, or explicit Beta terminology.

The theorem allows measurable time-dependent predictors. A proof only for predictors independent of time does not establish the requested upper bound. In particular, an unaveraged subset-weighted conditional KL sum is generally not the stipulated loss. Uniform index selection supplies a factor 1/k; event-time averaging must still be accounted for.

Distinguish the common autonomous time/index law from independence of token states and event times. The latter independence holds for the true path used in the reference calculation, but need not hold for the learned path.

Check probability-zero contexts, zero predictor probabilities, and the finite-loss assumption using the stated extended-KL conventions. Do not demand strictly positive predictor probabilities at every time or context. The case ε=0 must not be excluded. Equality of predictors inferred from zero integrated loss is only an almost-everywhere, supported-context conclusion.

The precise path representation is not mandatory, but its mathematical role cannot be omitted without an alternative justification: the solution must relate the correct output law and the full integrated error. The specialized event-time/loss identification and the matching lower construction are substantive obligations, not facts supplied by the problem.
