# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

## Core Steps

- **2 points:** Correctly exploits evenness and Gaussian sign symmetry to eliminate conditional first moments and off-diagonal second moments, and uses permutation symmetry to identify the scalar informative operator. Distinguishes the limiting independent Gaussian channel from finite-d projections with covariance U*U*^T. Explains why the gain is nonzero under finite NSE.
- **3 points:** Isolates one planted coordinate with signal amplitude p^{-1/2}; carries out an exact channel-density decomposition; and justifies the large-p reduction through Gaussian smoothing and a CLT, with adequate control for integration. A claim of exact Gaussian nuisance at fixed p does not complete this step. A valid alternative bound or reduction is acceptable.
- **3 points:** Establishes the positive-integer NSE cancellations, the nonzero leading coefficient, and both bounds K_p=Theta(p^{-beta_*}). Controls a weighted remainder and the leading-remainder cross term, or supplies an equally rigorous alternative. Polynomial boundedness by itself is not a justification for an unrestricted uniform Taylor/Hermite expansion. Zero-mean or unit-variance normalization must be justified rather than added as a substantive assumption.
- **2 points:** Establishes the threshold and specialization events for the particular public profile, not merely for some unspecified AMP scheme. A complete route proves preservation of Q=qI_p, identifies the scalar update derivative as alpha K_p with justified differentiation or expansion, and uses local contraction below one and finite-time escape above one. The normalized profile then supplies an orthogonal deterministic witness for p>=2. Handles the supremum over finite iteration counts before seed removal and obtains the threshold infimum without needing to decide the equality case.

## Profile Bridge

The gain calculation alone does not establish a threshold for the prescribed recursion. Do not award the final core-step points solely for citing a threshold formula or a full-easy-subspace assertion for an appropriate AMP scheme without establishing its application to the public profile.

The repaired reference derives the bridge directly from the noisy output potential by Gaussian-kernel differentiation and integration by parts. Accept a valid alternative derivation. Do not require that particular kernel presentation or an unnecessary global convergence theorem: finite-time escape from a fixed neighborhood suffices for the public event.

## External-Dependency Qualification

The public limiting-performance specification may be used as the definition of the AMP profile in this problem. An answer proving its threshold claims need not recover omitted finite-dimensional implementation details from an unavailable citation.

A private GT warning remains for the specialized source-to-algorithm correspondence: the supplied paper does not derive the finite-dimensional AMP construction or prove its fixed-iteration convergence under the stated initialization. Do not record that realization obligation as completed merely because state evolution is named or cited.

The external algorithmic threshold and easy-subspace assertions are retained as source context but are not needed by the repaired direct profile proof. An answer claiming an independent finite-dimensional algorithmic theorem must separately state and justify the relevant realization result.

## Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, optional normalization, or exact limiting constant. The target is a Theta law, not the corrected private prefactor.

Do not import the information-theoretic global-maximizer theorem or the non-rigorous generic-activation committee-symmetry ansatz into the even-activation target. The overlap constant may depend on fixed p and alpha; no uniform-in-p overlap requirement from the separate generic-activation result is imposed here.

Do not credit a fixed-t zero-seed argument as an instability proof. Iteration counts may depend on the seed but not on dimension. The boundary alpha K_p=1 need not be resolved to determine the infimum.

Maintain the narrowed private GT warning when assessing source-correspondence completeness. It is not evidence that the public profile target is false.
