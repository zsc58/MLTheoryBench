# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly expands the generic product `Q_mu K_nu^T` as `sum_{beta,gamma} X_beta Phi_{mu beta}Psi_{nu gamma}^T X_gamma^T`, with compatible transposes and dimensions.
- **3 points:** Substitutes the generic expansion into all four Hamilton score components, correctly collects the signed coefficient matrices `Lambda_alpha^{beta gamma}`, and proves that they lie in `U`.
- **3 points:** Uses the real quaternion inner product to expand `R`, obtains `M^{beta gamma} = sum_mu Phi_{mu beta}Psi_{mu gamma}^T`, and proves every such coefficient lies in `U`.
- **2 points:** Establishes the claimed decompositions for all indices, simultaneously for every compatible input using coefficient matrices determined solely by the fixed weights, and draws the precise common-subspace conclusion without asserting an unsupported equality of spans or making a post-softmax claim.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Merely asserting that the scores use the same interactions, without deriving the coefficient expansions and subspace membership, does not earn the corresponding core-step credit. Minor sign or index errors may be treated as readily repairable only when the general derivation is complete and the claimed conclusion remains supported.

Weight-only dependence may be stated explicitly or be evident from the constructed coefficients; do not require a separate sentence when the construction already establishes it. A merely pointwise choice of coefficients that may depend on `X` does not establish the required input-uniform assertion.
