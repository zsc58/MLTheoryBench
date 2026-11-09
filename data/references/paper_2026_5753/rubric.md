# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly justifies density evolution for the stated initial law and rewrites `nu_t(A_H)-pi(A_H)` as an L2 pairing with the centered indicator, using normalization and preservation of constants. A transition-semigroup duality argument is sufficient; a classical Fokker-Planck derivative at time zero is not required.
- **3 points:** Uses reversibility to obtain the pairing with `P_t(1_A-pi(A))` and rigorously establishes decay at `lambda_A`. Accept either a scalar spectral-measure argument, including its relation to the defining supremum, or a direct argument that the admissible-rate supremum is finite and its endpoint is attained. Do not require a spectral construction when the public definition is handled rigorously by another method.
- **3 points:** Applies Cauchy-Schwarz, computes `||1_A-pi(A)||_2^2=pi(A)(1-pi(A))`, and obtains the sharp absolute-deviation bound, its relaxed version, and the multiplicative upper bound for every `t>=0`, with the specified local rate and constants.
- **2 points:** Proves the bounded-density ceiling from positivity preservation and preservation of constants, combines it with the relaxation bound through the stated minimum, and proves `lambda_A>=m` using the correctly normalized Poincare/spectral-gap consequence. Allocate one point to the ceiling and minimum and one point to the rate lower bound.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or an explicit spectral-support characterization if the necessary endpoint estimate is otherwise proved.

The theorem-critical conclusions are the local-rate deviation estimate, the conditional bounded-density ceiling and minimum, and the strong-convexity rate lower bound. Replacing the local rate by the global rate alone does not prove the requested estimate.

The multiplicative expression is the relaxed one-sided upper bound written differently; proving it alone does not establish the sharper two-sided absolute-deviation estimate. The word 'in particular' does not remove that stronger obligation.

The standard strongly log-concave Poincare inequality may be invoked with its relevant statement and checked normalization: `Var_pi(f)<=(sigma^2/(2m)) integral |nabla f|^2 d pi = E(f)/m`. A proof of that standard independent theorem is not required.

Do not demand regularity or finite Dirichlet energy of the indicator. An argument that applies the generator or its form directly to the indicator without justification has a domain gap. Semigroup or spectral arguments on L2 vectors avoid it.

The task allows `chi_0^2=0`, includes `t=0`, and allows `M=1`. A proof whose formulas already cover these cases need not discuss them separately. No conductance hypothesis, volume assumption, or quadratic specialization is required. There is no unresolved GT obligation to waive or treat as a completed step.
