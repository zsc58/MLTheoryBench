# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly establishes the child-wise divergence decomposition using the correctly signed three-point identity and empirical-mean cancellation, or equivalent direct expansion.
- **3 points:** Derives the exact impurity-gain identity as the child-size-weighted sum of divergences from child barycenters to the parent barycenter, without requiring strong convexity.
- **3 points:** Under the additional lambda-strong-convexity assumption, bounds both divergence terms and obtains the corresponding weighted squared-distance lower bound.
- **2 points:** Uses the parent barycenter's weighted-mean relation to simplify that expression to (lambda/2) p_L p_R ||mu_{t_L}-mu_{t_R}||^2, with correct normalization.

# Evaluator Notes

Accept a complete valid alternative proof and allocate the corresponding points for equivalent mathematical steps. Do not require the reference proof's incidental presentation choices. In particular, direct expansion or a direct strong-convexity argument need not be presented through the named three-point identity.

A response that merely names the three-point identity or strong convexity without providing the relevant argument should not receive credit for an unestablished step. The reference proof's preliminary verification that the empirical mean is the minimizing representative is source-contract verification, not an additional solver obligation: the public task defines the representative as the empirical mean.

The exact decomposition must hold under differentiability and strict convexity alone; strong convexity is used only for the quantitative bound. The argument must remain valid when child means coincide and when either child is a singleton. No separate case split is necessary if the proof already includes these cases.

The correctly signed residual term is <x-y,grad psi(y)-grad psi(z)> in the expansion of D_psi(x,z). The source's opposite sign is a recorded local typo, not an accepted identity. Assess an isolated sign slip according to its actual effect on the submitted argument; in a centered sum the residual vanishes with either sign, but the pointwise formula with the reversed sign is false.
