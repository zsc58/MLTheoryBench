# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps for the Geometric Route

- **2 points:** Establishes the distributional continuity equation and verifies the hypotheses of standard ODE/continuity-equation representation, obtaining increasing homeomorphic flow maps that transport the source to every marginal. Derives affine trajectories directly from straightness without importing additional differentiability or moment assumptions.
- **3 points:** Uses source quantiles and monotone transport to obtain the correct one-sided endpoint confinement, constructs the moving interval, and proves its marginal occupancy is at most epsilon. Handles the exact-total-mass and touching-hull cases without adding a positive-gap assumption.
- **3 points:** Gives a complete quantitative crossing argument. Accounts for motion of interval boundaries, proves that every constant used to choose the threshold depends only on permitted parameters, and controls the initial strip using the Frostman bound and path-modulus estimate. A claim that the mesh bound is automatic from interval width alone does not close this step.
- **2 points:** Uses endpoint independence to identify a positive-probability forced-crossing event and chooses the auxiliary parameters and epsilon threshold in a valid order to obtain the contradiction.

# Evaluator Notes

Accept any complete valid alternative proof. The point allocation above describes one route, not mandatory intermediate results.

In particular, the exact source quantifiers permit epsilon0 to depend on the exact masses w0 and w1. If w0+w1<1, choosing epsilon0<(1-w0-w1) makes the required mass inequality incompatible with epsilon<=epsilon0. If w0+w1=1, a valid flow-representation argument shows that a source positive on every nonempty open interval must be transported by a homeomorphism to a full-support target, contradicting concentration on the bounded union of the mode sets. A solution proving these two cases is a complete proof of the stated task and merits full credit. Do not penalize it for omitting the geometric construction, Frostman estimate, or mesh argument.

For a solution that does rely on the geometric route, omitted low-occupancy or crossing estimates are theorem-critical gaps unless replaced by another valid argument. In particular:

- Do not assume target half-line masses equal mode masses; the valid confinement statements are inequalities.
- Do not assume disjoint convex hulls of open sets have positive distance.
- Do not assume connectedness of either mode set.
- Do not use the unrestricted moving-interval crossing claim as an established theorem; boundary motion must be controlled or avoided.
- Do not allow constants depending on unbounded source quantiles, an unspecified source location, or process-specific velocity bounds to enter epsilon0 without proving the required uniform control.
- Do not require W^{2,1} sample paths, finite second moments, densities at intermediate times, or jointly C^1 velocity. Those were not assumptions of the source target.

The replacement reference proof contains a complete direct mesh argument and the shorter exact-weight argument. It has no unresolved private proof obligations.
