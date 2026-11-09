# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derives the regret decomposition for the actual online learner, whose round-(t+1) prediction uses A_{epsilon_{X_t}}(X_t). Explicitly justifies exchangeability between a uniformly deleted occurrence and the next occurrence conditional on the reduced multiset, and applies bounded-loss TV control, the triangle inequality, approximation, and average sensitivity. A leave-one-out statement without the fresh-loss comparison does not by itself close this step.
- **3 points:** Justifies the minimizing selector and needed concave-conjugate properties, optimizes the per-prefix tradeoff, and applies both weighted Jensen and expectation Jensen. Establishes the random-order prefix-optimum estimate, for example by evaluating a full-multiset minimizer on each random prefix, to obtain H_T phi*(OPT_T/H_T+lambda).
- **3 points:** Applies parameter-change stability, uses conditional uniform deletion to obtain the expected weighted prefix-optimum increments, and derives the supergradient inequality from minimizer optimality. Telescopes the resulting increments to phi*(OPT_T+lambda)-phi*(lambda). Merely naming stability or conjugacy without the derivation is insufficient.
- **2 points:** Combines the estimates with correct prediction/update indexing, constants, and expectations. Controls the initial prediction, the singleton parameter-change term, and the uniform approximation-error sum by a T-independent additive constant. Covers T=1 and zero prefix optima without an undefined selector argument.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its exact additive constant c+3, or use of the parameter-change assumption if an alternative argument genuinely avoids it. No coupling or product-measure bound is required. Allow extended-valued phi with effective domain strictly smaller than (0,1]. A proof that only analyzes a learner choosing theta_t after observing x_t does not establish the stated online theorem.

Award downstream points when a conclusion is independently established despite an earlier flawed derivation; propagate a dependency failure only when the downstream claim is unsupported.
