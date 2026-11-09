# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Decomposes \(V_c=V+\xi\) conditionally, uses the stopped derivative correctly, and derives \(\operatorname{Cov}(\nabla_\theta\ell_{\rm sg}\mid X_t)=4H^\top K\Sigma K^\top H\), including the trace consequence.
- **2 points:** Establishes the conditional loss decomposition and correctly obtains the exact full-versus-stopped population gradient identity, including the residual-zero consequence. The differentiation and conditioning must respect the parameter-independent data law and the stated integrability and interchange assumptions.
- **3 points:** Derives the mixed-tangent gradient error and its conditional MSE by separating the proxy-bias term from the centered transformed-noise term.
- **2 points:** Under the scalar-isotropic assumptions, obtains the correct strictly convex quadratic, unique \(\beta^*\), and optimum value, with the nondegeneracy condition used correctly. Verifies that \(\beta^*\in[0,1]\), so the unconstrained quadratic minimizer also solves the stated constrained problem; the argument must allow \(\sigma=0\) and \(b=0\) separately.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A response that merely asserts Jacobian amplification, a semi-gradient discrepancy, or the final coefficient without deriving the relevant conditional covariance, gradient identity, or MSE decomposition has not completed the corresponding core step.

The ideal target in \(M\) is the explicitly defined vector \(2H^\top R\), not the full derivative of \(\|R\|^2\). There is no requirement to establish an asymptotic convergence statement from \(R\to0\).

A proof may derive the population gradient identity by differentiating the original sample loss and conditioning. If it instead differentiates the two terms of the population loss decomposition separately, it should justify the needed interchange rather than assume that it automatically follows for each summand.

No general-matrix optimization formula is required. If one is used, the two cross traces are equal because the Gram and covariance matrices are symmetric; the previous source-map allegation to the contrary is incorrect. Preserve the factor four when computing exact MSE values.
