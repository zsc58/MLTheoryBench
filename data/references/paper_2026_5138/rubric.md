# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derives the weighted chi-square evolution bound from the two continuity equations, including the score and ratio-integrability estimates, and correctly uses the Gaussian terminal comparison to obtain `chi2(rhohat_1||q) <= C_F epsilon`. When using differentiation and integration by parts, supplies a valid justification for the quotient-weighted terms. The existing ratio-integrability hypothesis, together with the field-growth bounds, permits a cutoff argument; upper bounds on the individual densities alone are not a sufficient justification for reciprocal-density terms.
- **2 points:** Transfers the terminal divergence bound to the generated core distribution by invariance under the common invertible flow, verifies the inverse-flow Lipschitz estimate, and obtains the stated core `W_2` bound from the correctly oriented transport/divergence inequalities. The standard Gaussian inequality is `W_2^2(nu,q)<=2 KL(nu||q)`. A measurable-bijection or almost-everywhere change-of-variables argument is sufficient; spatial Lipschitz continuity must not be treated as implying an everywhere `C1` diffeomorphism. Checks finite moments and the absolute-continuity/entropy conditions needed for the argument.
- **4 points:** Constructs a valid lifted coupling, preserving the original matrix model and the core marginals, and proves the three-term ambient decomposition. Correctly controls the geometric term by principal angles and the expected oracle-core Frobenius bound, identifies the core embedding as an isometry, and controls the residual noise through Frobenius projection contraction and the Frobenius/spectral comparison.
- **1 point:** Applies Minkowski and the definition of Wasserstein distance to combine the three estimates with the exact constants and conclusion.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular cutoff notation. Correct standard ODE, conditional-probability, and Gaussian transport facts may be invoked with their relevant hypotheses verified. A proof need not reproduce an elementary conditional-expectation calculation if the marginal-velocity definition and its continuity equation are used correctly.

Do not require or credit an added pointwise bound on `S0`, an added classical differentiability assumption on the learned flow, or an independence assumption between `S0` and `E`. The source requires only conditional mean-zero noise and the stated second-moment bounds. Do not demand a finite-sample or missing-observation argument. Handle zero noise and dimensional boundary cases within the stated contract. No unresolved reference-proof step is treated as an established grading requirement.
