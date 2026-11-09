# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Introduces a valid representation separating the error due to the true probabilities at the observed covariates from label noise, for example through normalized kernel weights and a virtual estimator, or provides an equivalent valid setup.
- **3 points:** Establishes the L lambda bias bound using Lipschitz continuity, nonnegative normalized weights and compact support. The distance restriction is needed only for strictly positive weights; zero-weight observations need not lie within the bandwidth.
- **4 points:** Establishes a valid probability bound for the label-noise term with the constants and confidence dependence required by the target. For the conditional route, verifies the almost-everywhere conditional product law and common sub-Gaussian scale, uses S=sum_i K_i epsilon_i with epsilon_i=p_c(Y_i)-1_{C_i=c}, and controls V=sum_i K_i^2<=kappa. Justifies the concentration inequality rather than merely citing an unrestricted random-weight claim, and derives both alpha regimes, including kappa=1. Within this component, award 1 point for correct centering and probabilistic hypotheses, 2 points for justified concentration with adequate constants, and 1 point for the two-regime comparison. Accept a different complete concentration argument yielding the target.
- **1 point:** Combines the probability estimate and bias bound to prove the joint training-sample guarantee, with no evaluation of the estimator at kappa=0. For a conditional proof, integrates the conditional failure bound over the covariates.

# Evaluator Notes

Accept any complete valid alternative proof and assign credit for equivalent work rather than requiring the reference proof's notation or route.

The requested probability statement is joint over the i.i.d. training sample, for each fixed n, query, class and confidence level. An almost-everywhere conditional guarantee is sufficient and stronger, not equivalent in general. Do not require a solver using another valid method to prove that stronger statement. Do not require statements for arbitrary null covariate realizations or a simultaneous guarantee over queries, classes, sample sizes or confidence levels.

Conditional on the covariates, the class indicators are independent Bernoulli variables whose success probabilities may differ. They need not be identically distributed. Unconditional sub-Gaussianity alone is not a justification for applying a bound to arbitrary label-dependent weights. A cited concentration result must have its relevant statement supplied and applicable hypotheses verified; the overgeneralized stochastic-weight quotation in the source is not sufficient by itself.

The scale convention is E exp(tX)<=exp(sigma^2 t^2/2). A universal centered-Bernoulli scale is 1/2, not 1/4. The theorem uses any scale satisfying its stated conditional requirement; no numerical scale substitution is required. The source's erroneous numerical assertion cannot be used to change the public bound.

The zero-mass case is vacuous for the requested implication, including an identically zero kernel. If sigma=0, the stipulated moment bounds force the centered noises to vanish almost surely; a short treatment suffices. L=0 and kappa=1 require no separate restrictive assumptions. Small omissions in these routine cases should be distinguished from a missing core concentration argument.
