# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Endpoint, domain, and confidence analysis (2 points).** For the reference route, establish equality of the endpoint constants and the needed tail-integral estimate. Verify the exponential transformation and the estimator confidence event, using epsilon_m<1 only for sufficiently large horizons. Respect the genuine inverse domain, eventual derivative domains, and finite true mean. A valid alternative analytic route receives equivalent credit.
2. **Known-parameter benchmark (3 points).** Derive the optimal DP value and prophet-maximum asymptotics on the psi((log n)/theta) scale, including their constants, and conclude the stated ratio. Correctly initialize the terminal DP value at the mean. For the scale-transform route, justify the transformed increments and summation; for the prophet integral, justify convergence of expectations rather than only convergence in distribution.
3. **Confidence-DP comparison (3 points).** Conditional on exploration data in the confidence event, prove that the true reward of the plug-in policy is at least the DP value at theta_+. Establish the necessary parameter monotonicity and independence of subsequent observations. Average correctly to obtain the factor 1-delta. Do not assume that the estimated parameter exceeds c, or that its surrogate mean is finite, on every exploration outcome.
4. **Moving-parameter control and final limit (2 points).** Justify applying the DP asymptotic at theta_+, by compact uniformity or another rigorous argument. Show that m=o(n) and epsilon_m log n->0 preserve the psi scale and prefactor. Combine with the prophet asymptotic to obtain the required unconditional liminf guarantee.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental notation, order, or use of a scale transform. In particular, a different rigorous treatment of the moving parameter can replace a separately stated compact-uniform lemma.

Unjustified moving-parameter asymptotics, failure to establish the conditional comparison, and unsupported interchange of limits and expectations are theorem-critical gaps. A reference to a paper-specific lemma without proof does not close these obligations.

The theorem includes c=0 and both x0=0 and x0>0. Bounds and estimates must cover these cases. Calling r_eta(0) without a valid definition when x0>0 is not the stated DP initialization. Infinite surrogate means outside the confidence event are permitted: the defined infinite thresholds reject until final acceptance. No almost-sure finite-surrogate assumption may be added.

The conclusion is pointwise for a fixed family, fixed theta, and fixed delta. Do not demand rates, uniformity over underlying families, varying-confidence conclusions, or equality of the learning ratio that the task does not claim.
