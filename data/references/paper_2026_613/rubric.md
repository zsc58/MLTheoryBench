# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **Step 1 (2 points):** Correctly derives the conditional Gaussian covariance, Bayes coefficient and residual law, and establishes the almost-sure context empirical-moment limits. Uses the stated density assumption correctly to obtain radial atomlessness when needed.
- **Step 2 (2 points):** Proves the probability-zero assertion for every fixed single-layer predictor. Expands the limiting coefficient and gives a valid conditional polynomial-root and finite-spectrum argument, or an equally complete alternative. A contradiction only to almost-sure equality does not establish probability zero; equality at a realized scalar value does not by itself justify comparing polynomial coefficients. Accounts for the conditionally nondegenerate Gaussian query.
- **Step 3 (2 points):** Solves the tied recurrence, handles zero parameters without an invalid division, and obtains the fixed-depth almost-sure readout limit. Justifies disappearance of the residual for the actual sample-dependent embeddings, for example by polynomial factorization and the mixed-moment strong law. Establishes the relevant contraction behavior without assuming bounded individual Gaussian embeddings.
- **Step 4 (2 points):** Establishes existence and the scalar formula for the population loss with the limit outside the expectation. Justifies the required expectation limit under bounded m and only the stated second moment of zeta. Proves strict convexity, coercivity, the unique minimizer, global existence of gradient flow, and convergence from arbitrary real initialization.
- **Step 5 (2 points):** Establishes the large-depth minimizer limit $2/(2+\underline m+\overline m)$ with a valid moving-parameter lower bound and minimizer comparison, or an equally complete alternative. Handles $\underline m=0$ without adding endpoint-density or positive-weight-lower-bound assumptions. Proves prediction convergence for the varying trained parameters, with the context limit taken before the depth limit.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or a named convergence theorem. In particular, a direct scalar monotonicity proof of gradient-flow convergence is acceptable.

Treat failure to prove probability-zero shallow equality, an unjustified loss-limit interchange, a missing global gradient-flow argument, or a missing depth-minimizer argument as theorem-critical gaps. Distinguish a missing argument from a small algebraic slip that the answer otherwise resolves.

Do not accept pointwise polynomial coefficient comparison at one realized zeta, commutation of sample and population covariance matrices without justification, an iid law of large numbers for arbitrary sample-dependent embedding products, or a fixed-parameter contraction argument alone for a depth-dependent trained sequence. Do not require a fourth moment of zeta, bounded individual embeddings, or the endpoint-density assumptions of a different model.
