# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Uniform identification and approximate roots (2 points):** Proves the weighted uniform law on the parameter ball using the explicit gradient envelope and propensity-rate bound, and uses separation to establish consistency of every bounded approximate-root sequence. Establishes existence with the specified residual rate, for example by a measurable empirical approximate minimizer compared with a one-step point whose residual is proved to be o_p(1/b). A uniform law alone does not establish that residual rate. A population-dependent comparison point is permissible in the proof but is not, by itself, a data-based estimator construction.
2. **Single-arm linearization and nonstandard CLT (3 points):** Proves target-Jacobian convergence and local derivative control using the integrable Hessian envelope. Derives a valid effective-Jacobian linearization without assuming the desired estimator rate in advance. Uses the past-history filtration, integrates over the current context in the predictable covariance, and proves convergence using scaled inverse-propensity stability and the normalized deterministic weights. Verifies conditional Lindeberg using the fourth score moment and the stated propensity-rate condition, then obtains the action-specific Gaussian limit.
3. **Joint multi-arm limit (2 points):** Applies a valid Cramer-Wold/martingale argument to the arm-specific normalizations. Uses zero conditional means given past history and disjoint action indicators to eliminate cross-arm predictable covariance terms. Checks joint Lindeberg, for example using the disjoint-support fourth-moment identity and the finite number of arms. Stacks the linearizations to obtain the block-diagonal joint limit.
4. **Sandwich variance consistency (3 points):** Proves plug-in derivative convergence using consistency and the local weighted Hessian envelope. Proves true-parameter meat convergence by predictable covariance convergence and a martingale second-moment bound involving the fourth score moment. Justifies meat substitution with scaled weighted score-gradient and squared-gradient envelopes having bounded expectations. Uses nonsingular limiting Jacobians and handles the empirical singularity event to conclude sandwich consistency.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not award substantial credit for merely naming a martingale CLT, Z-estimation, or sandwich method without verifying the required bounds and limits. A failure in the single-arm CLT or linearization propagates to the corresponding joint-normal conclusion; variance estimation is scored independently when established.

The score is only assumed twice differentiable. Do not require continuity of its second derivatives, fourth moments of its gradient envelope, nondegenerate limiting covariance, convergence of unscaled propensities, or regular variation of the deterministic rate sequence. The case rho=0 and other singular covariance cases remain within the target.

Conditioning on past history and the current context generally gives a nonzero score mean. The unintegrated expression pi_t(a)^{-1}E[g*g*^T|X_t] is a conditional second moment, not the predictable covariance for the history-filtration martingale. A proof must integrate over the current context or provide another correct filtration argument.

A conditional operator-norm bound M_2 on E[g*g*^T|X] implies E[||g*||^2|X]<=d M_2. Finite dimension-dependent constants need not be optimized. The relevant scaled weighted expectation converges to E rho(a,X), not to an assumed reciprocal limiting policy. The centered quadratic calculation requires the available fourth moment, not a substitution of a second moment.

A one-step comparison point may leave the ball on an event whose probability tends to zero; a valid proof must account for that event. The selected estimator must remain in the ball for every T and be measurable with respect to recorded data. Measurable compact minimization or a countable-dense-set approximate minimizer is acceptable.

The source-local corrections are recorded under theory_007 and theory_021. They introduce no additional scoring requirement beyond mathematical correctness. All reference-proof obligations are closed; no specialized paper-dependent assertion is accepted merely by citation.
