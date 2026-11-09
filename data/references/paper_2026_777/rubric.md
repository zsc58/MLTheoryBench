# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly represent the iterates as centered Gaussians and derive the linear slice map and covariance recursion. Verify positive definiteness, use gamma_0=1 at initialization, and establish the trace/eigenvalue upper bound for k>=1.
- **3 points:** Establish sufficient uniform lower spectral control, or another valid control giving the required uniform inverse moments, for the entire stated stepsize range. The reference obtains a deterministic determinant lower bound from scalar log concavity and AM-GM and combines it with the trace bound. A different complete argument is equally acceptable. Do not require the source's selected-column averaging, inverse-eigenvalue supermartingale assertion, or product inequality.
- **3 points:** Establish sufficient Gaussian gradient domination and control its constants along the trajectory. The reference proves the Gaussian Wasserstein/sliced-Wasserstein comparison and a quadratic-potential coupling inequality explicitly. A stronger direct Gaussian inequality or another valid substitute is acceptable. Keep F=(d/2)SW_2^2 normalized consistently; handle zero loss before cancellation and dimension one where needed.
- **2 points:** Derive a valid conditional stochastic descent recursion and obtain both claimed rate regimes with their stated parameter ranges and constant dependencies. If using truncation and scalar-recursion lemmas, specify the thresholds, moment orders, relevant lemma hypotheses, and resulting exponents. A valid stronger convergence bound implying both claims earns full credit without reproducing the reference's truncation route.

# Evaluator Notes

Accept any complete valid alternative proof under the public assumptions. Do not require the incidental notation or ordering used in the reference proof.

The range 0<alpha<=1/2 is part of the task. A proof that assumes sum_k gamma_k^2<infinity does not establish that range. Restricting the answer to alpha>1/2 leaves a substantive part incomplete.

A basis column selected through an eigenvalue minimum or maximum need not have the uniform spherical law. Independence of the whole fresh basis from the past does not justify assigning a fixed-column marginal law to such a selected column. Do not award the spectral-control points for that unsupported averaging argument.

The compact-support differentiability proposition quoted in the source does not apply verbatim to Gaussian measures. Direct Gaussian residual calculations and projected-coupling descent estimates are valid alternatives and require no compact-support assumption.

The source's particular signed binomial moment bound is incorrect. Pointwise bounds such as |theta^T Q theta-1|<=max(1,d-1) for Q>=0 with Tr(Q)<=d establish the finite-moment consequence without that formula.

Merely naming concentration, a PL inequality, a specialized smoothness theorem, or a covariance bound without establishing the needed statement and checking its hypotheses is insufficient. The unused sharper monotonicity and product claims in the source inverse-eigenvalue proposition are not requirements of this task.

The first-regime constant may depend on epsilon. No conclusion is requested at alpha=2/3. All finite initial indices must be covered, possibly by enlarging the constant.
