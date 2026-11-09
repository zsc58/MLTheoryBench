# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **(2 points)** Derive the Gaussian population loss and correctly normalized gradients, and prove invariance of the three-projector manifold for both algorithms. The matrix multiplying W in the W-gradient is twice the gradient with respect to M. Justify that the matrix dynamics do not depend on the orthogonal factor of the isotropic initialization.
2. **(3 points)** Derive the exact discrete scalar recursions. For ordinary GD these are squared multiplicative factors, with strictly positive learning rate and justified factor bounds. For polar descent the universally valid square-root recursion uses Sign(g_i times the square-root coordinate); zero coordinates remain zero. A sign-only formula is acceptable where positivity is proved. Do not assume an unstated nonresonance or full-rank condition.
3. **(3 points)** Prove the polar conclusions: synchronized early growth through the actual first spike turning index; O_kappa(1) first-stage duration for fixed kappa; uniform bounds on (1+lambda)h and (d-2)z; O(eta^-1) small-delta signal hitting; a persistent positive signal bound and uniform later alignment; and the explicit A-dependent alignment estimate after an index K_*=O(eta^-1). Distinguish the small-delta hitting time from the later threshold used to obtain the explicit constant.
4. **(2 points)** Prove the ordinary-GD comparison: invariant bounds or equivalent controls; spike escape and actual turning within O((eta_tilde lambda)^-1 log d); spike dominance and both early-alignment upper bounds at that turning index; and signal hitting within an additional O(eta_tilde^-1 log d), with a persistent positive signal and uniform o(1) nuisance Frobenius contribution thereafter. The source's spike-saturation/bulk-inflation phase route is acceptable when its comparisons are correctly derived, but an alternative direct comparison proving every public conclusion is equally acceptable.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Require derivations of the invariant reduction, recursions, and barrier/comparison estimates; naming a method or citing a paper-specific result without establishing the needed estimate is insufficient. Do not require the reference proof's incidental notation or ordering.

The first polar-stage O(1) notation is dimension-independent for each fixed positive kappa; it is not uniform as kappa tends to zero. The proof may display O(1+kappa^-1). Constants in the GD estimates may depend on the fixed numerical bounds in the anisotropy range, but not on dimension, the particular allowed lambda, the positive GD step size, the orthogonal directions, the initialization factor, or the observation-noise variance.

For the GD saturation subphase, the gap argument gives a sufficient bound O((eta_tilde lambda)^-1 log((1+lambda)/rho_0)); this is compatible with the required total first-stage bound. Do not require the stronger source assertion with only log(1/rho_0).

A fixed-epsilon bulk-inflation argument does not establish that the bulk deficit vanishes. Do not require or credit the unsupported assertion that both the scaled spike and 1-C contract geometrically throughout the final phase. Bounded scaled nuisance masses already imply vanishing nuisance Frobenius contribution in the stated anisotropy regime. A proof still must establish that the signal lower bound persists for every later iterate; merely proving a hitting time is insufficient.

The explicit polar estimate containing A need only hold for every k>=K_*, not at the earlier arbitrary small-delta hitting time. Uniform 1-o(1) alignment from the small-delta hitting time remains a required conclusion.

The reference proof contains no unresolved theorem-critical obligation. Its local corrections are part of the audited evaluator contract, not additional assumptions available to the solver.
