# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Constructs an interior linear/quadratic exponential tilt with zero mean and identity second moment, proves existence and uniqueness, and establishes KL/free-energy minimization by an explicit decomposition. In the dual approach, the integrability boundary concerns the effective precision Q-B. Coercivity must be justified, for example by a global affine lower bound on the smoothed log-sum-exp and the resulting Gaussian bound involving tr(K)-log det(K) and a quadratic linear-parameter term.
- **2 points:** Uses regular-value coarea conditioning and orthogonal/Stiefel transitivity to identify the finite-particle constrained Gibbs law, including constancy of the coarea Jacobian and agreement of normalized surface measure with Stiefel-Haar measure. Conditioning at the probability-zero constraint must use a specified density/coarea version; the subsequent density formula must agree with that version at the regular value.
- **3 points:** Verifies the Fourier and density local-CLT hypotheses for W=(Y,YY^T), obtains the density-ratio estimate, and derives convergence of the one-particle marginal under the tilted product law. A Fourier route must justify the anisotropic estimate for a non-product Schwartz amplitude and integrability of a sufficiently high convolution power. Integration by parts must avoid stationary points, for example through localization. Full support establishes pointwise nonlattice behavior but does not by itself establish the strong Cramer condition; the proved Fourier decay supplies that condition. A standard local CLT may be invoked when its relevant statement and all hypotheses are specified and verified.
- **3 points:** Shows the base and tilted conditioned laws coincide because the likelihood ratio is constant on the constraint manifold; pushes the limit to z-space; verifies the limit has the required moments and finite free energy; proves uniqueness of the constrained minimizer; and derives both multiplier identities by justified integration by parts.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the particular repaired dual estimate, localization, or local-CLT route if another rigorous argument closes the same obligations. Do not award full credit for merely naming a local CLT, coarea formula, exponential-family argument, or equivalence of ensembles without verifying the relevant hypotheses and explaining the conclusion.

Use the corrected triangle bound ((||u||-R)_+)^2<=min_j||u-x_j||^2, or any valid alternative confinement estimate. The uncorrected bound (||u||-R)^2 is false inside the radius-R ball. An isolated use is readily repairable when the intended confinement argument is otherwise sound; do not treat it as invalidating the target theorem.

The smallest admissible P may have a singular one-particle law; only the limiting law is asserted to have a density. Large-P density arguments suffice for the limit, while the Gibbs law itself must be defined for all admissible P. The case sigma=0 is included. All other data and parameters remain fixed as P tends to infinity.

Propagate a missing tilt or conditioning argument only when the downstream conclusion depends on it; theorem-critical gaps remain major. The reference proof has no unresolved obligations.
