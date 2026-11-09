# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1–2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3–7:** Some correct core steps or conclusions, but important steps are missing.
- **8–9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct, including the mechanism-level conclusion and the stated computational scope.

# Core Steps

1. **Tail-bound derivation (3 points).** Derives a valid variational or equivalent lower bound on the history-prefix log likelihood ratio, computes its affine Gaussian mean and variance, and obtains valid remove and add lower-tail bounds. The remove reference is the full uniform mixture over all components; the add reference is the zero-mean Gaussian. Handles zero variance without dividing by zero and does not define an empty prefix mixture at component index 1.

2. **Threshold and per-round domination construction (3 points).** Allocates each positive round budget, constructs finite certified thresholds or an equally valid deterministic substitute, and obtains normalized fixed comparison weights. Proves that the relevant history-measurable failures have probability at most beta_n under P for remove and Q for add. The comparison weights may differ by orientation. The construction must use history-prefix information from the fixed mean array, not future observed data or current observations. Handles b=1, empty history, and ties; no nondegeneracy assumption may be added.

3. **Prior-order transfer (2 points).** Proves the categorical ordering bridge and its transfer to both scalar Gaussian-pair orientations, or provides an equally complete alternative argument. Checks nonnegative scalar current means and carries component labels consistently when reordering. Establishes domination for all positive hockey-stick thresholds, not merely thresholds at least 1 when a composition argument needs the full order.

4. **Global accountant and complexity (2 points).** Proves the two product-pair inequalities with the correct first-law exceptional probabilities and additive delta_E in each orientation. Derives a deterministic privacy accountant, including the transfer to actual neighboring outputs of the specified adaptive matrix mechanism. States the initial O(N^2 b^2) remove and O(N^2 b) add construction costs and the repeated-common-noise O(Nb^2) remove and O(Nb log b) add costs for b>=2, with O(N) for b=1. Distinguishes per-step-pair construction from final product-divergence evaluation and uses the fixed scalar numerical-iteration convention. Within this item, allocate 1 point to composition, 0.5 to the actual-mechanism transfer and privacy conclusion, and 0.5 to the computational claims.

# Evaluator Notes

Accept any complete valid alternative proof. The named steps describe one route, not mandatory public lemmas. Do not award credit for merely naming a variational, stochastic-order, composition, or adaptive Gaussian comparison method without deriving the required inequalities.

P and Q are auxiliary laws. A proof for them alone does not automatically prove the claim for actual adaptive neighboring mechanism outputs. Conversely, the add-side history law Q does not replace the mixture posterior function by a new posterior based on a zero-mean latent model. Both orientations use the same conditional mixture law as a function of history, with different history sampling measures and potentially different fixed comparison weights.

A sum of only components k=i,...,b with weights 1/b is not the full remove history law. Do not accept it as a probability distribution or use its tails to bound the omitted components without a separately valid argument. Do not accept arbitrary vector means in the scalar stochastic-order step, or a single ordered comparison pair asserted to work for both orientations without proof.

Distinguish strict and non-strict tails at atoms. Conservative finite numerical searches are acceptable when their chosen endpoint is certified feasible. A fixed iteration count does not justify unaccounted approximation error in a privacy bound. No extra factor of two is required in delta_E merely because both neighboring orientations must be checked.

# Mechanism-Transfer Verification

The reference now explicitly proves the mechanism-transfer obligation; there is no remaining private GT warning. Its proof conditions on the common records' assignments, applies a common invertible triangular residual map, and keeps the differing record's persistent batch index hidden. The residual shifts remain predictable functions of the evolving history. Their norm bounds alone are not a proof of domination by the fixed auxiliary means.

The reference completes the comparison by tracking the entire vector of component likelihood ratios under the zero-shift Gaussian law. Their conditional Gaussian log-increment covariance is bounded entrywise by that of the aligned scalar auxiliary experiment. A derived Gaussian differentiation identity proves the needed exponential-vector comparison. Continuation functions obtained from smooth convex approximations to both hockey-stick payoffs have nonnegative mixed second derivatives, so conditional iteration establishes both orientations. Smoothing and covariance regularization are removed with justified limits. Averaging over common assignments and discarding the revealed common information finishes the reduction.

A solution may use another complete valid argument. It must, however, address adaptivity and the hidden persistent index, not identify actual residual shifts with deterministic means or reveal the differing record's batch index while retaining the same amplified bound. Merely citing the specialized upstream domination result does not satisfy the public request to justify the connection. Evaluate alternative derivations on their mathematical merits rather than requiring the reference's particular proof route.
