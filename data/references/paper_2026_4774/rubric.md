# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly symmetrizes the leave-one-out estimator into the order-two U-statistic with kernel \(h(u,v)=\tfrac12(S(u)-S(v))(Z(u)-Z(v))\), uses the correct ordered/unordered pair normalization, and establishes unbiasedness.
- **3 points:** Correctly computes the projection. With the centered convention \(h_1(u)=\mathbb E[h(u,U')]-g\), the formula is \(h_1(Y,Z)=\tfrac12[S(Y)(Z-V)-g]\). Equivalently, the uncentered projection is \([S(Y)(Z-V)+g]/2\). Constructs a genuinely degenerate remainder, establishes the required orthogonality, and derives the \(\operatorname{tr}\Sigma_{\rm or}/G+O(\mathbb E\|S\|^2/G^2)\) MSE bound, with a constant depending only on the reward bound.
- **2 points:** Shows the oracle estimator has MSE exactly \(\operatorname{tr}\Sigma_{\rm or}/G\) and concludes equality of the leading MSE coefficients, including a possibly zero coefficient.
- **2 points:** For every deterministic prompt-only baseline, derives the oracle variance plus the nonnegative \(\mathbb E[\|S\|^2(V-b)^2\mid x]/G\) term using conditional uncorrelation, proving asymptotic optimality and the stated strict zero-baseline case.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its explicit numerical remainder constant, or its notation for projections. Direct covariance calculations may replace the Hoeffding argument if they establish the same claims and rate.

Treat omission of the second-order remainder rate, a valid first-order covariance identification, or the baseline comparison as theorem-critical gaps. A merely uncentered notation is not an error if the solver consistently uses covariance and supplies the correct mean subtraction in the decomposition. However, asserting \(h_1=\tfrac12S(Z-V)\) for a projection defined to be centered is incorrect in general. If a solver uses that formula to claim degeneracy or equates its uncentered second moment to the oracle covariance, the affected argument is not complete; assess whether the remainder of the answer actually repairs the mistake rather than requiring agreement with the original reference typo.

Do not require conditional independence of reward and squared score norm: the stated conditional uncorrelation suffices. Do not require positive oracle variance, nonzero reward variance, or a nonzero score second moment. The theorem includes \(G=2\) and degenerate cases. Oracle equivalence here means equality of the coefficient of \(1/G\), not an MSE ratio when the oracle coefficient is zero. Strict zero-baseline improvement is an asymptotic coefficient comparison under the stated positive weighted expectation; universal strict improvement for every finite \(G\) is not required.

All theorem-critical steps in the replacement reference proof are explicitly derived. No private ground-truth proof gap remains.
