# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly center the proxy, use the regularized first-order condition, and justify that the stationary mean is `theta_hat` under the stated invertibility/stationarity assumptions.
- **3 points:** Derive the stationary covariance recursion and its expanded discrete Lyapunov identity, including the Gaussian term `2 beta^{-1}Lambda` and the `H-hat Sigma_psi H-hat` contribution. Justify the vanishing cross terms by conditional mean zero and fresh Gaussian independence, without assuming that the state-dependent sampling noise is independent of the state or that the matrices commute.
- **4 points:** Compute the expected minibatch-gradient covariance exactly, including the score moment, both Hessian covariance terms, the regularizer outer-product correction, and the `(N-B)/(N-1)` factor relative to the with-replacement formula. Justify the sampling coefficients for the specified experiments; an explicit finite-population expansion or a correctly stated and applicable elementary sampling-covariance identity is acceptable.
- **1 point:** Substitute the noise formula into the Lyapunov identity to state the resulting closed covariance-tuning relation for the two sampling schemes.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The covariance/noise calculation is the characteristic bottleneck; naming a Lyapunov equation or concentration argument without deriving the exact terms earns no credit for that step. Apply dependency penalties only when a missing step leaves a later conclusion unsupported.

The regularizer is fixed conditional on the state. A covariance expansion using unregularized observation gradients must subtract their own mean outer product, not the full regularized gradient outer product. Equivalently, one may include the same regularizer contribution in every sampled vector and show its cancellation.

The stated parameter domain includes `beta=infinity`; setting its Gaussian coefficient to zero handles this case directly. No temperature-limit argument is required. The sampling formulas must remain valid for `B=1` and for `B=N`; in the latter case only the without-replacement sampling covariance must vanish. A general calculation that already covers these boundaries needs no separate case discussion.

Do not require global convexity, positive definiteness of the stationary covariance, commuting matrices, uniqueness of a stationary law, or a proof of stationary-law existence beyond the hypotheses. The requested closure is a matrix identity, not a guarantee that an arbitrary prescribed covariance admits an admissible step matrix. There are no unresolved reference-proof obligations.
