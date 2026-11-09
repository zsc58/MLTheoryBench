# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Proves capacity uniqueness for the stated generalized separable form \(h(\sum g(\|f_k\|))\), including a valid treatment of the domain of \(g^{-1}\), the zero argument, rational homogeneity, and continuity. Do not accept assuming direct additivity as the proof of the generalized statement.
- **2 points:** Establishes scale invariance of \(c\), the corresponding density scale law, and the additive logarithmic path integral. Treats the derivative of capacity almost everywhere when necessary and obtains extinction divergence with the initial state fixed and a uniform positive lower bound on \(c\).
- **3 points:** Uses the correct duplicated-parent pre-deletion endpoint and normalized merge objective. Establishes the correlated-path lower-capacity guarantee for an attained optimal parent, then integrates the constant-speed geometric cost to obtain \(J_{\rm proj}\le c(\Phi_a)D/E(\Phi_b)\). The proof must work throughout the path, including both endpoints, for arbitrary nonnegative residual capacity. It must not impose monotonicity on the geometric path or assume that an optimizer selection is continuous without justification.
- **3 points:** Derives the fixed-magnitude optimization from the duplicated-parent squared error, exhaustively parameterizes realizable unit directions, kernelizes the alignment, optimizes the output direction by Cauchy–Schwarz, proves attainment on the actual positive-self-kernel domain, and handles zero alignment.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. The explicit numerical correlation threshold in the reference proof is not required; any valid threshold with the stated dependencies and uniform path guarantee suffices.

Do not award credit for minimizing \(\|f_i+f_j-p\|^2\) over parent magnitude in place of the normalized merge objective. At a fixed magnitude the direction problems coincide, but their optimal scales do not.

Do not require a separate continuity-based proof of the correlation assertion. A direct inequality or another valid argument is fully acceptable. The optimal scale's strict inequality below the sum of the child norms is a derived fact in the correlated regime, not a public assumption or an independently scored target.

The affine input \((X,1)\) is not an isotropic Gaussian vector. The exact direction theorem does not require an angular-kernel formula or a boundary derivative identity. In particular, strict positivity of \(K(u,u)\) on the entire unit sphere cannot be assumed for one-sided activations. A compactness argument must address the excluded zero-self-kernel directions.

In the zero-maximum-alignment case, accept any feasible unit input direction and any unit output direction. Do not require normalization of a zero vector.

Do not award credit for merely naming a projection, kernel, homogeneity, or continuity method without supplying the relevant derivation. There are no unresolved reference-proof obligations and no hidden specialized-method requirement.
