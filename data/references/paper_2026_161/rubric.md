# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly handles the ordered, no-padding convolutional composition and derives the stride-dilated polynomial representation. Polynomial degrees are upper bounds unless nonvanishing leading coefficients have been established.
- **3 points:** Proves loss decrease, establishes residual domination for every listed loss and its full parameter range, and uses the right inverse supplied by full row rank to obtain a uniform bound on the effective filter. Negative generalized-Huber loss values must not be treated as nonnegative without an appropriate additive constant. Any auxiliary function claimed to have domain all of R must actually be defined there.
- **3 points:** Derives the conserved differences of layer squared norms and rigorously obtains boundedness of every layer. In the factorization route, proves or otherwise validly establishes the normalized-factor bound, retains the scalar units, cancels them only in the product of squared layer norms, and supplies the bounded-coefficient polynomial/root argument or an equivalent elementary bound. Handles zero and nonzero-constant effective polynomials, reduced degree, N=1, k_v=1, and bounds below one. An alternative argument earns full credit if it closes the same layer-boundedness obligation under the entire stated contract.
- **2 points:** Verifies global real analyticity and local Lipschitz continuity of the vector field, establishes global existence by continuation from the uniform parameter bound, and applies correctly stated standard Lojasiewicz results to conclude convergence to a critical point.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's constants, normalized-factor construction, or incidental presentation choices. Standard local ODE existence/continuation and the analytic Lojasiewicz gradient inequality and bounded-flow convergence theorem may be invoked with their relevant hypotheses verified.

The layer-boundedness argument must be derived rather than merely naming balancedness, factorization, or a paper-specific boundedness lemma. Bounded normalized factors do not individually bound the original layer polynomials: their scalar units can be unbounded, and the cancellation or an alternative argument is essential. A proof that silently assumes nonzero filters, maximal polynomial degree, unit strides, a filling architecture, or loss nonnegativity does not establish the entire task. A missing case merits an 8-9 assessment only when it is genuinely local and readily repaired; a missing theorem-critical mechanism belongs in the incomplete-proof range.

All four loss families and the full-row-rank conversion remain theorem-critical. The target is convergence to a critical point, not necessarily to a local or global minimizer. There are no unresolved reference-proof obligations and no GT-quality exception in this rubric.
