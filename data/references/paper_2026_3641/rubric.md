# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives unbiasedness and the finite-population variance quadratic with the exact factor $D=(N-n)/(n(N-1))$ for the stated denominator-$N$ variance, minimizes over the scalar coefficient, and obtains the oracle variance in terms of squared correlation (including appropriate degeneracy handling).
- **3 points:** Proves finite-population conditional-regression residual orthogonality to every measurable function of the proxy and consequently replaces $\operatorname{Cov}_N(Y,\phi(\hat Y))$ by $\operatorname{Cov}_N(m(\hat Y),\phi(\hat Y))$.
- **3 points:** Uses Cauchy-Schwarz to establish the sharp upper bound by $R^2_{Y\sim\hat Y}$ and shows that $\phi=m$ attains the infimum, with the resulting variance expression.
- **2 points:** Compares the optimum with the identity surrogate, derives the exact gain $D S_Y^2(R^2_{Y\sim\hat Y}-\rho_N^2(Y,\hat Y))$, and proves strict improvement occurs exactly when $m$ is non-affine on the proxy support, including the constant-$m$ case.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Equality in the unnormalized covariance bound for a constant recalibration does not imply equality in the correlation bound when $\operatorname{Var}_N(m(\hat Y))>0$.
