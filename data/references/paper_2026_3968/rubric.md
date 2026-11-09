# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes existence and uniqueness of the regularized system, the stated barriers, and identification with the policy infimum. Derives the Gibbs intensities by scalar minimization and verifies their admissibility and optimality. A truncation proof must use a realizable monotone cutoff and justify existence and cutoff removal.
- **2 points:** Proves the gradient bound uniformly over all lambda>0, including the boundary estimate. The reference closes this with a uniform value barrier, a boundary-distance barrier, and a Bernstein estimate with a concave quadratic correction. Any complete valid alternative is acceptable. A bound only for a bounded temperature interval does not establish the full stated gradient claim.
- **3 points:** Establishes the small-temperature obstacle estimate with C_up=2C_coef(1+C_Lip), or another argument sufficient to prove the exact requested kappa inequality with that constant. In the reference route, common diffusion cancels the second-order difference, strict switching-cost geometry controls third-mode terms, and the reverse-exponential term is retained. The small-temperature restriction and constant arithmetic must be justified.
- **3 points:** Proves both comparisons with the correctly signed classical viscosity variational inequality and derives the exact kappa inequality and the O(lambda log(1/lambda)) rate. The upper comparison must respect viscosity regularity. The lower comparison must justify continuation-region use, propagation at obstacle contact, and termination by strictly positive cycle costs, or supply a valid alternative.

# Evaluator Notes

Accept any complete valid alternative proof. Do not award credit for merely naming a standard method without its theorem-critical inequalities. All obligations in the reference are closed; there is no unresolved reference-proof waiver.

Do not require global C^2 regularity of the classical value. Do not accept mode-dependent diffusion as a substitute for the stated common-diffusion hypothesis in the obstacle-subtraction argument. Do not accept the incorrect differential sign from the earlier public revision.

In particular, multiplication of a squared gradient by exp(delta x_1) does not by itself make an arbitrarily unfavorable zeroth-order coefficient positive: after the corresponding drift correction its quadratic-in-delta contribution is negative. A proof following that route must repair the actual inequality, not merely assert that delta can be chosen large. The reference's quadratic Bernstein correction is one complete local repair, not a mandatory solution template.

The KL interpretation is ancillary and is not an additional scoring requirement. If invoked, it concerns stopped joint path laws, uses the expectation of the log likelihood, and includes the zero-rate convention. The public objective is already defined directly by its discounted integral.
