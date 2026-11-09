# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly handles the Gaussian-kernel drift, proves compact-support invariance, and establishes the spatial and measure Lipschitz estimates and compact nonlinear/particle well-posedness needed for the argument. A characteristic fixed-point construction and coupling stability estimate are sufficient. The compact flows must be the flows specified in the admissibility definition.
- **3 points:** Proves expected empirical W_1 convergence at fixed beta, radius, and terminal time, and transfers it to compact-uniform posterior-mean convergence. Accept either coupling to iid nonlinear characteristics with Gronwall and a justified time-integral limit, or pathwise nonlinear-flow stability applied to empirical initial laws. Compact empirical W_1 convergence must be established or obtained from a precisely applicable standard result; all its moment hypotheses are automatic at fixed radius.
- **3 points:** Uses the given deterministic admissibility convergence to pass R to infinity and justifies compact-uniform posterior-map continuity for general P_1 measures. A correct proof controls the globally bounded/Lipschitz Gaussian numerator and denominator kernels, obtains a positive denominator minimum for the fixed limiting measure on the query ball, and passes to the quotient. Do not require or assume denominator bounds uniform over all probability measures. No second-moment or transport-action estimate is needed for this continuity step.
- **2 points:** Applies the defining recovery property at T_beta=beta*tau/2, combines the limits in the required order N, then R, then beta, and proves both expectation and probability conclusions. The error must be a measurable integrable random variable, and the posterior interpretation uses independent Gaussian noise and the continuous version supplied by the quotient.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or an unnecessary fixed-k marginal argument when expected empirical convergence has already been established.

The public domain is P_1. Do not silently restrict the theorem to priors with a finite second moment, a density, nondegenerate covariance, or Gaussian tails. Compact support supplies every higher moment needed at the fixed-radius empirical step.

Admissibility and terminal recovery are assumptions defining the prior class. Proving Gaussian membership, weak–strong uniqueness around a Gaussian, or an unconditional noncompact existence theorem is not an additional requirement. Conversely, posterior-map continuity is a proof obligation, not an assumed component of admissibility.

Constants may depend on the fixed bandwidth, radius, finite horizon, dimension, query radius, observation variance, and fixed limiting measure where appropriate. Uniform estimates across the subsequent radius and bandwidth limits are not required.

Initialization consists of exactly N iid draws from the deterministic normalized truncation. Do not replace it by a random retained sample count, an untruncated sampling experiment, or a joint scaling law.

A reference to an unstated paper-specific theorem or a named specialized method alone does not close a core step. Standard independent results may be used when the relevant statement and its applicable hypotheses are clear. Routine analytic tools such as Gronwall, the contraction theorem, dominated convergence, and Markov's inequality are acceptable with their hypotheses verified.
