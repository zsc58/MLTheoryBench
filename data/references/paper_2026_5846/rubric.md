# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes the population fixed point and relevant Jacobian structure, verifies the real spectrum and simple leading eigenvalue, and justifies how normalization replaces that eigenvalue by zero. Concludes rho_sync(alpha)=max{lambda_2(alpha),-lambda_n(alpha)}. An explicit projection calculation or an equivalent quotient-space argument is required; merely saying that normalization removes scale is not a complete spectral justification.
- **3 points:** Establishes analytic eigenvalue branches using an analytic symmetric representative or another valid method, with the leading branch identified. Derives the requested differential inequalities, for example through the identity psi_i'=(1-psi_i)/(alpha+gamma_i) and an explicitly justified coefficient bound gamma_i in [kappa^{-1},kappa]. Proves strict increase of nonleading branches, convergence to 1, and the rational comparison bounds. The exact auxiliary identity is not mandatory if the requested inequalities are obtained otherwise.
- **3 points:** Correctly passes from branches to ordered extreme eigenvalues, allowing eigenvalue crossings and multiplicities. Uses their strict monotonicity and continuity to prove quasi-convexity and the complete unique-minimizer characterization: alpha_opt=0 for s_0>=0, and the unique positive balancing point for s_0<0.
- **2 points:** Derives kappa^{-1}|s_0|<=alpha_opt<=kappa|s_0| in the negative-s_0 case and both stated all-parameter bounds for rho_sync. Handles signs and endpoints without assuming that individual terms in the bounding maxima are nonnegative.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or auxiliary notation. Standard Perron-Frobenius and real-analytic symmetric spectral theory may be invoked with their relevant hypotheses verified; the problem-specific Jacobian, symmetrization, and eigenvalue differential control must be established rather than merely attributed to an unspecified formula.

Ordered extreme eigenvalues need not themselves be analytic through crossings. A proof through maxima and minima of finitely many analytic branches is valid. Strict increase, not just weak monotonicity without further justification, must support uniqueness of the minimizer.

The cases alpha=0, s_0=0, kappa=1, n=2, repeated eigenvalues, and a zero minimum factor must not be excluded. They need no separate calculation if the argument already covers them.

The public factor is defined as a spectral radius. Do not require a stronger trajectory-wise convergence assertion. Do not require the additional source-specific optimal-factor formulas in the optional final paragraph of the reference proof; the scored factor bounds are exactly the all-parameter inequalities requested publicly. There are no unresolved reference-proof obligations.
