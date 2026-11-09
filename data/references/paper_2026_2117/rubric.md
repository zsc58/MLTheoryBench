# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes that isotropic Gaussian KL depends only on the fitted covariance eigenvalues and obtains the exact retained-plus-pinned spectral loss. A diagonal/e-flat reformulation is valid but not mandatory.
- **2 points:** Correctly obtains the limiting expected KL per coordinate from the MP law, with sufficient control of inverse-eigenvalue and logarithmic tails and with the rank-zero and retain-all endpoints included. If using the decomposition route, justifies the normalized component limits and normalized variance disappearance rather than inferring them solely from a deterministic empirical spectral limit.
- **3 points:** Differentiates with respect to rank ratio, obtains the equation f(c)=f(epsilon), and proves that c=epsilon is the unique interior local minimum. Correctly handles the second root: it is a local maximum only when it is an interior feasible cutoff. No false global-convexity claim is needed.
- **3 points:** Supplies a valid global comparison: establishes retain-all for epsilon<=lambda_-, excludes retain-all for lambda_-<epsilon<1, proves existence and uniqueness of epsilon_*(alpha), and derives the interior/collapse phases and the tie at the threshold.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's notation, decomposition order, presentation choices, or use of information geometry. In particular, direct minimization of the expected Gaussian spectral loss can earn full credit.

The expectation is over the independent training observations, and the objective is optimized over deterministic limiting rank ratios. The cutoff description is asymptotic; do not demand an exact finite-sample identity between a deterministic optimal rank and the random number of sample eigenvalues above epsilon.

Theorem-critical omissions of the expected MP limit, cutoff classification, or global boundary comparison are major gaps. Weak convergence of spectral measures alone does not control expected inverse-eigenvalue loss; an appropriately stated applicable standard spectral-integrability result or a valid direct bound is acceptable. Merely observing that all spectral values exceed epsilon does not prove retain-all: the scalar KL cost is not monotone over the entire positive half-line. Likewise, invoking a unique collapse threshold without establishing the endpoint signs and strict monotonicity does not complete the phase proof.

At epsilon=epsilon_*(alpha), both collapse and the interior rank are global minimizers. A proof must not assert uniqueness of collapse at that value. All points assigned above concern actual proof obligations; there are no unresolved reference-proof steps.
