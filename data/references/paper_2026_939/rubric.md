# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Uses the assumed conjugate derivative and the chain rule to obtain a_hat(x_i)psi_j(x_i), and uses linearity of m on the basis span to obtain m(w_i,psi_j). Concludes that the jth derivative of the unpenalized empirical objective at beta_hat is Delta_j. Re-proving the conjugate derivative identity explicitly assumed in the task is not required.
2. **4 points:** Derives from minimization the existence of a single vector s in partial Omega_q(beta_hat) satisfying Delta_j+lambda s_j=0 simultaneously for every coordinate. A correct convex first-order/subgradient argument or a direct coordinate and one-sided derivative argument is acceptable. Merely naming KKT without connecting it to this objective and deriving the equation earns no credit for this step. Do not treat an arbitrary penalty subgradient as necessarily satisfying stationarity.
3. **2 points:** Correctly handles the q=1 subgradient and proves |Delta_j|<=lambda, and handles finite q>1 to prove |Delta_j|=lambda|beta_hat_j|^(q-1). Includes the zero-coefficient cases: the q=1 subgradient is [-1,1] at zero, and the q>1 derivative is zero at zero.
4. **2 points:** Correctly derives exact coordinate-wise sample balancing when lambda=0 under the stated feasibility/minimizer conditions. Does not divide by lambda without separating lambda=0 and does not infer existence of an empirical minimizer merely from feasibility.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its direct coordinate construction when a valid subgradient optimality argument is supplied. Standard finite-dimensional convex optimality and subgradient rules may be used with their applicability justified by the explicit task hypotheses. Treat an unjustified conjugate-term differentiation, linear moment differentiation, or claimed stationarity/subgradient relation as a theorem-critical gap. The conjugate derivative identity is a task assumption, not an additional result the solver must prove. No analysis at q=infinity, population representation theorem, sampling assumption, cross-fitting argument, or external generalized-duality theorem is required.
