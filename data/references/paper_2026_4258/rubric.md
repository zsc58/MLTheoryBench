# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly conditions on the training data, uses the stated conditional Dirichlet experiment and empirical stationarity, and handles the gradient/Hessian dimensions and covariance transformation correctly. Supplied assumptions need not be proved.
- **3 points:** Derives the exact conditional covariance from a correct Dirichlet covariance formula, removes the simplex-centering term using the zero empirical gradient, and applies the influence linear map. The standard Dirichlet moment formula may be stated without deriving its density integrals.
- **2 points:** Establishes the asymptotic matrix-difference statement using stochastic boundedness of the sandwich matrix; identifies the alpha=1 Bayesian-bootstrap scaling; and proves the curvature-only specialization from the explicitly assumed convergence ||H_F-H|| ->p 0. Do not require or reward an unsupported claim that correct specification alone establishes empirical convergence.
- **3 points:** Uses uniform convergence of the coverage criterion, minimization, uniqueness, and compactness to prove selector consistency and nominal population coverage. A direct compactness-separation proof or a correctly stated standard argmin result with its hypotheses checked is acceptable. The argument must accommodate endpoint roots and, when retaining random training data, the training-dependent population criterion with n fixed.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A theorem-critical omission in either covariance scaling or selector consistency is a major gap. Merely naming an influence-function, Dirichlet, CLT, or argmin method without stating and applying the relevant result earns no credit for that step.

The covariance target compares two sample-dependent matrices; convergence of H or H_F to fixed matrices is not required. The covariance and calibration limits use n -> infinity and m -> infinity, respectively; a simultaneous triangular-array calibration theorem is not requested. No conditional CLT, Gaussian approximation, weighted-refit approximation rate, predictive-Jacobian covariance theorem, or proof of the assumed uniform law of large numbers is required. The predictive rule is supplied; its continuity or monotonicity need not be derived, because the necessary properties of population coverage are assumptions. Measurability of the selector is also supplied.
