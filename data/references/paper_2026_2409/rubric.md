# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly formulates the continuous residual on the two subintervals, uses the affine parameter structure and the information-matrix eigenvalue bound, and handles the no-switch case by selecting the active parameter. Integral identities may be asserted almost everywhere; no derivative at the switching time is required.
- **3 points:** Minimizes the weighted quadratic, or gives an equivalent completed-square identity, to obtain the harmonic-length lower bound and derives the half-minimum bound with the parameter-jump factor. The infimum over Theta is compared with the unconstrained minimum; no convexity of Theta or membership of the unconstrained minimizer in Theta may be assumed.
- **3 points:** For an approximate trajectory on the post-switch set, performs the residual decomposition and rigorously applies the finite-Lp triangle inequality or reverse triangle inequality, state Lipschitz control for the chosen mismatched parameter, and mismatch identifiability to obtain the continuous positive-part lower bound.
- **2 points:** Applies the powered quadrature-error inequality with exponent alpha_q, uses nonnegativity of the weighted sum, and takes the increasing 1/p_y power to obtain the discrete residual lower bound. Correctly specializes to the opposite regime parameter under the hypotheses for that choice to expose dependence on the regime jump.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The no-switch conclusion concerns the infimum over constant parameters. The residual is the unnormalized weighted residual norm defined in the task, not a screening score divided by total weight.

Respect the finite exponent domain, positive collocation count, positive weights, and positive-part operations. The identifiability constant alpha and quadrature exponent alpha_q are independent quantities. A consistent renaming is acceptable, but identifying them or using the wrong exponent without explanation is not a correct quadrature transfer.

The final specialization does not assert that constants or hypotheses established for a different fixed parameter automatically hold for theta^-. Do not require a solver to prove mismatch identifiability, quadrature accuracy, or the stated Lipschitz condition; they are primitive hypotheses. Do not require existence and uniqueness, estimator optimality, conditional stability, or a generalization bound.

A negative continuous comparison or a negative quadrature-adjusted expression gives the zero lower bound after taking positive parts. Zero quadrature error is allowed. Endpoint values do not affect the integral residuals. The theorem-critical omissions of the quadratic minimization, mismatch decomposition, or quadrature transfer are major gaps; isolated, unambiguous notation slips may be readily repairable.
