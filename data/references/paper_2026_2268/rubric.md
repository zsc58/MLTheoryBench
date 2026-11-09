# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly rewrites SPO+ as the support-function/optimal-value term plus the optimizer decision term, establishes the Hausdorff support and value estimates, and establishes fixed-set objective sensitivity with coefficient equal to the diameter. Handles translations on the complete loss using a transported optimizer selection or an equivalent valid argument.
2. **4 points:** Derives the general discrepancy bound with the minimum of the two asymmetric expressions defining \(T(h)\), and the decision term \(2\|h\|(\delta_N+D_{\min})\). Applies component estimates to a single consistently translated comparison before taking the shape-distance infimum; an approximating translation sequence is sufficient. A valid proof of attainment is also acceptable.
3. **2 points:** Under the stated intersection-of-balls definition, establishes the needed curvature growth and directional stability, and obtains the cross-set support estimate \(\delta+2\sqrt{\rho_{\min}\delta}\). Derives the refined optimizer estimate with \(\rho_{\min}\) multiplying the normalized cost-direction difference. Minimizers correspond to negative normalized support directions. A complete alternative route to the same estimate receives full credit.
4. **2 points:** Combines the refined optimizer estimate with the unchanged \(T\)-bound to prove \(H_{\rm SC}\), and rigorously establishes the existential diameter-scale obstruction using fixed admissible parameters, a common nontrivial feasible set, and cost shifts tending to zero while the normalized discrepancy has positive liminf.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular lower-bound construction.

The original selectors are arbitrary. Do not demand an added global translation-equivariance assumption. A proof can transport the client selector on an auxiliary translated copy. Translation invariance of the full loss does not imply translation invariance of either separated contribution; in particular, a shape-distance estimate on the original unshifted optimizer difference is not generally valid.

The refinement requires positive radii and Euclidean geometry. All directions used in the quadratic-growth estimate must be unit vectors, and the true costs are nonzero by assumption. Do not accept an unexplained specialized citation as a completed derivation of the curvature mechanism; a precisely stated standard independent result with verified hypotheses, or a valid derivation, is needed.

The necessity claim is existential, not a claim for every dimension, set, or budget. A construction must verify the fixed cost bounds and positive prediction budget and must show an actual loss discrepancy, not merely separated optimizer locations. The zero-budget upper-bound case remains part of the general claims, but is not part of the existential obstruction.
