# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **3 points:** Correctly substitute the exponential-family score into the empirical loss, collect the quadratic and linear parameter terms, including the plus-divergence contribution inside the linear-loss coefficient, and complete the square with the Gaussian prior. Establish positive-definite precision and a finite posterior normalizer, and obtain the stated precision and mean. Distinguish the canonical linear coefficient from the posterior mean.
2. **2 points:** Formulate the one-observation replacement using the same surrogate, weight, prior, and learning rate, and apply the correctly oriented KL identity for two nondegenerate multivariate Gaussians, or provide an equivalent valid method of controlling their KL divergence.
3. **3 points:** Use the actual public derivative assumptions and positive-semidefinite matrix inequalities to establish contamination-uniform precision/covariance bounds and a uniform posterior mean-shift bound. In particular, justify boundedness of w²∇T∇b from the derivative-product condition and justify the divergence bound from the weight-gradient and full second-derivative conditions. Do not assume a separate uniform bound on w∇b. A valid argument may use a common lower precision bound supplied by the prior and a common upper precision bound supplied by the weighted statistic derivatives.
4. **2 points:** Combine uniform control of the covariance-trace, quadratic mean, and log-determinant contributions, or equivalent direct KL estimates, to prove a finite supremum over every replacement value. Constants may depend on the fixed sample size, dimensions, learning rate, prior parameters, and derivative-bound constants, but not on the replacement value.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, exact constants, or symmetric bounds where a one-sided bound suffices. A direct valid bound on the entire KL divergence need not explicitly reproduce the three-term decomposition.

For a proof using the Gaussian KL decomposition, an unsupported robustness conclusion or omission of a potentially unbounded term is incomplete. Merely naming score matching, conjugacy, or matrix inequalities earns no credit for the corresponding derivation.

The empirical posterior argument is pointwise in the data. Do not require iid sampling, a training argument, refitting the surrogate, recalibrating the learning rate, or estimating a new weight after replacement. Constant weights and singular or zero data precision contributions are permitted; the positive-definite prior precision handles them. A solver need not reprove the auxiliary population score-matching identity when proving the requested empirical posterior theorem.

The public mean formula already uses the locally corrected divergence sign. Do not reward the erroneous minus-divergence sign in the source statement. Likewise, do not require the source appendix's malformed scalar constants, dropped factors, or incorrect extra factor n in a single-observation precision contribution.

All reference-proof obligations are closed; there is no private GT completeness exception.
