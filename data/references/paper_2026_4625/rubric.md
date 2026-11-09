# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Full-Credit Direct Route

The public smoothness assumption is uniform over all real weights and the finite objective family. It implies that the reconstruction map is constant. A complete proof exploiting this implication earns full credit without reproducing a vacuous splitting argument.

- **2 points:** Correctly uses the global coefficient quantifier, rather than treating the Hessian constant as dependent on the current weights.
- **3 points:** Computes the two-sample off-diagonal Hessian block at coincident locations and weights t,t as 2t² Dg(x)ᵀDg(x), bounds this block using the full Hessian bound, and lets t grow to prove Dg(x)=0 for every x.
- **3 points:** Concludes that g is constant and verifies that all location gradients, location Hessians, and splitting matrices vanish, so the initial point passes the stopping test.
- **2 points:** Concludes that both update counts are zero and hence both requested bounds and stationarity hold, including the zero-initial-loss case and every admissible positive step size.

# Original-Route Core Steps

For a proof organized around the splitting calculation, retain the following allocation; do not add these points to the direct-route allocation.

- **2 points:** Correctly differentiates the objective, identifies the splitting matrices, and derives the Hessian quadratic-form decomposition and lower bound by the smallest splitting eigenvalue.
- **3 points:** Establishes balanced cancellation and correctly controls the Taylor remainder in the augmented location space. The ordinary bound contains the cube of the concatenated displacement norm. A proof may establish the smaller claimed estimate by deriving the constant-map consequence of the actual assumptions, which makes the remainder zero.
- **3 points:** Correctly identifies the binary minimum-eigenvector choice, proves the conditional decrease of at least epsilon_H eta²/4, and obtains the split count from nonnegativity; or explicitly establishes that no split can occur under the full assumptions.
- **2 points:** Proves the gradient-descent decrease and count, supplies a valid justification of the total-iteration claim, and concludes stationarity using the Hessian lower bound or immediate stationarity.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require incidental presentation choices or the reference proof's supplementary calculations when a direct proof has already established immediate termination.

Do not award full credit for silently replacing the global coefficient quantifier by trajectory-only or bounded-weight smoothness. Do not accept the assertion that individually unit-bounded offspring displacements form a unit-bounded concatenated vector: a binary split with directions v and -v has concatenated norm sqrt(2). Do not infer an epsilon-uniform total bound for arbitrarily small epsilon-dependent splitting steps merely by adding the two generic count estimates, or silently add a lower bound on eta.

For a proof relying on the generic splitting route, omission of justified remainder control, valid split accounting, valid total-iteration accounting, or the final Hessian comparison is theorem-critical. These are not missing obligations when a valid direct argument already proves all location derivatives and splitting matrices vanish and the algorithm stops immediately. Zero weights never trigger a split because their splitting matrices are zero.
