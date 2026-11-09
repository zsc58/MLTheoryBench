# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derives Phi(f)-Phi(L)=E^{pi_L}D_KL(mu_L^y||mu_f^y), proves nonnegativity, and identifies equality with d_Phi(f,L)=0. Identification is almost everywhere on the observation support; full support or pointwise uniqueness is not required.
- **3 points:** Establishes well-definedness and the needed moments under the actual true law lambda_L; justifies continuity and a positive population-objective gap outside each d_Phi-ball. A compactness proof must verify that its closure elements admit the normalizers, KL identity, and identification used at attainment. If using log-normalizer continuity, its density-ratio or other supporting estimate must be justified, not merely named. Treat an empty separated set correctly. Accept a valid direct separation argument instead of compactness.
- **3 points:** Proves uniform convergence sup_{f in F}|Phi_N(f)-Phi(f)|->0 in probability, including ordinary empirical control and nested log-normalizer control for every M(N)->infinity. In a bracketing proof, verify ordering for inner as well as outer evaluations, admissibility of endpoints, endpoint convergence, and vanishing population widths. The two objective components have opposite monotonicities and must be controlled separately. An alternative valid uniform-control proof is equally acceptable.
- **2 points:** Uses the approximate-argmin inequality and r_N=o_P(1) to conclude the target for every epsilon>0. An explicit bound by 2 sup_f|Phi_N-Phi|+|r_N| closes this step without needing a named consistency theorem.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, entropy rates, particular Holder exponents, or a particular compactness topology. Do not require a relation between M(N) and N, monotonicity of M(N), full prior support, Gaussianity of the prior, or exact empirical minimization.

The true observation law is lambda=lambda_L and pi=pi_L. Do not credit an integrability argument that incorrectly infers observation moments solely from a posterior conditional with an arbitrary marginal. Do not assume the x-marginal of every induced lambda_f equals mu.

Bracket endpoints need not belong to F. Class-specific estimates cannot be applied to them without checking an applicable extension. Total boundedness alone does not authorize applying potentials or identification to unspecified closure elements. Treat omission of nested-Monte-Carlo uniform control or of the separation argument as theorem-critical.

Do not credit the source's incorrect positive interpolation derivative, signed equality for an expected absolute value, unweighted growing-exponential Lebesgue integral, or joint-law invariance under addition of h(y). Readily corrected sign or constant slips may be minor only when the needed valid inequalities and downstream arguments are otherwise established.

Routine measurability may be handled concisely through continuity and a countable dense class. Do not impose an additional information restriction beyond the stated sampling and measurable-estimator contract.

All reference-proof obligations have been derived. There is no unresolved private GT dependency.
