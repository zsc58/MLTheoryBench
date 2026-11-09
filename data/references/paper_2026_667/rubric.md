# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly define reverse-tail quantiles for the projected positive-half-line measures and justify marginal recovery and admissibility of their joint coupling on the punctured plan space. Account for zero measures, unequal masses, and possible infinite total mass; discard the (0,0) component.
2. **3 points:** Prove or validly justify the one-dimensional quantile transport formula throughout the required exponent range, including p=1 and infinite-total-mass marginals. A complete finite-support uncrossing proof followed by a justified approximation is sufficient. An endpoint limiting argument must control both marginals and costs; merely saying to truncate and pass to the limit is not sufficient when the missing passage is substantive.
3. **3 points:** Verify the projection and integration conditions on the full stated measure class, substitute the quantile formula into D_p^p, and derive the zero-sum quadratic-form inequality from scalar negative type for 1<=p<=2. This includes finiteness almost everywhere of the projected moments, measurability, finiteness of D_p, and justification for integrating the finite signed quadratic form. Readily recoverable measure-theoretic details may be treated as minor omissions rather than failures of the main argument.
4. **2 points:** Correctly apply the exponential criterion, checking the applicable symmetry, finiteness, zero-diagonal, and bandwidth conditions, to conclude positive semidefiniteness for every sigma>0.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's particular truncation map, finite-matrix presentation, or limiting-exponent argument. A direct valid treatment of p=1 is equally acceptable. Proving the auxiliary quantile formula for all p>=1 is welcome but not required beyond what establishes the public target for 1<=p<=2.

The monotone-transport justification and integrated CND argument are theorem-critical; merely naming the paper-specific quantile formula or a specialized boundary-reservoir optimal-plan theorem does not close them. An invoked standard independent result must be stated sufficiently precisely and its hypotheses checked. The standard scalar negative-type theorem and exponential-kernel criterion may be used without reproving them.

Do not accept arguments that require finite total mass, probability normalization, finite higher moments, or finite projected p-moments at every parameter value as though these were public assumptions. An integrated additive approximation error must include the measure's mass; this is not harmless for infinite-mass plans. Positive upper rectangles determine only the interior-interior part directly; prescribed marginals recover the boundary-axis parts.

Do not require correction of the source's separate empty-diagram normalization claim. The task fixes the prefactor 2^(-1/2), and the proof must consistently use 2^(-p/2) after taking the pth power. No metric-separation, stability, topology-equivalence, or numerical-approximation result is part of the target.
