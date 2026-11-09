# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly works with densities on E and the beta-integrated likelihood-prior function, obtains its quadratic kernel, and uses the assumed positivity of A=tau_y P_X^perp+tau_u R on E. Recognizes A_E as the positive definite self-adjoint compression Pi_E A|_E.
- **3 points:** Uses b_E=Pi_E(tau_y P_X^perp Y), completes the square on E, and derives the proper Gaussian posterior with mu_*=A_E^(-1)b_E and Sigma_*=A_E^(-1). Justifies that the normalizing integral is finite and positive.
- **2 points:** States and derives the ELBO-KL decomposition relating L, the ELBO, and posterior KL divergence, with expectations well-defined and KL nonnegative.
- **3 points:** Observes that the posterior belongs to Q, selects it as the variational distribution, and concludes equality of the ELBO supremum with L and zero posterior approximation error.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or explicit evaluation of constants that cancel, provided the proof establishes a finite positive normalizing integral and uses the same g in L and the ELBO.

The result is pointwise in Y and the positive precisions. It does not require a proof of convergence of coordinate ascent, existence of a joint maximum over precisions, or a uniform bound over the precision parameter space.

Do not assume that X contains an intercept or that A maps E into itself. An expression such as A_E^(-1)tau_y P_X^perp Y is acceptable only if the author explicitly defines the inverse notation as including projection onto E, or supplies an equivalent constrained-coordinate formulation. Under the task's operator convention, the mean is A_E^(-1)Pi_E(tau_y P_X^perp Y).

The covariance is positive definite as an operator on E, not on all of R^n. The function g need not be a normalized probability density over Y and u because the fixed effects were integrated against an improper flat prior.
