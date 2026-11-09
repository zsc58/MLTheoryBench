# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Definitions and local geometric control (2 points).** Uses strict benchmark-vector dominance, not distinctness of predictors, to obtain the antichain property. Establishes the tangent asymmetric gauge, positive-normal norm comparison, uniformly small smooth-chart distortion, and the necessary continuity and area-Jacobian bounds. Justifies global localization of small Pareto balls, for example by combining local comparison with compactness away from the diagonal. Handles boundary charts under the stated smooth-manifold convention.

2. **Central simplex-cover asymptotic (4 points).** Establishes the center-constrained covering limit for tangent simplices. A source-aligned proof derives positivity and finiteness of periodic density, the cube limit by periodization and periodic restriction with a shell completion, and the Jordan-set extension by interior cubes and negligible boundary neighborhoods. It also proves affine invariance, identifies the correctly oriented covering body, and calculates its volume as (sum_k nu_k)^(K-1)/((K-1)! product_k nu_k), yielding C_K=(K-1)! theta_{K-1}. The exact numerical value of the dimension-only density is not required. Merely naming a covering theorem or a linearization method without establishing the relevant center restriction, hypotheses, and geometric links earns only partial credit. A precisely stated independent standard result may replace a derivation only if it really supplies the needed covering statement and its hypotheses are checked; the source's internally proved Jordan-set proposition is not an automatic black box.

3. **Global patching and both inequalities (3 points).** Builds matching upper and lower bounds from a finite low-distortion chart partition. Accounts for both distance distortion and the area Jacobian. Proves that null remainders have negligible scaled covering cost with centers in the covered subset. In the upper bound covers A intersected with the remainder, not the entire remainder using inadmissible centers. In the lower bound uses A-intersected layers or another valid localization argument. If Jordan-set limits are applied to distance layers, chooses widths with null level sets or otherwise proves their applicability; Jordan measurability at every width must not be assumed without justification.

4. **Passage to the limiting measure (1 point).** Takes the small-scale limit first, then removes boundary layers, and finally refines the partition. Uses uniform continuity and the area formula to obtain the Hausdorff integral with a constant depending only on K. Covers empty and zero-measure Jordan sets without imposing an additional positive-measure assumption.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its particular partition, or an explicit numerical covering density. The theorem-critical simplex limit, density calculation, and matching global limsup/liminf are major obligations; unsupported appeals to a paper-specific result should not receive full credit.

A covering whose centers belong to a larger ambient set is not automatically a center-constrained cover of a smaller subset. Also, center-constrained covering numbers are not automatically monotone under set inclusion. These issues must be resolved by actual constructions or justified asymptotic comparisons.

A cover of a large cube formed from periodic centers in that cube and supplementary shell centers is valid even when the periodic centers do not lie in its inner core. Do not penalize this direct construction for failing to prove a stronger, unnecessary core-centered assertion.

If Euclidean covering rescaling is used, the valid elementary inequality is N_2(t,E)<=(1+2/c)^K N_2(t/c,E); the inverted factor appearing in the source is not valid. This auxiliary bound is not itself required when another valid remainder estimate is supplied.

The replacement reference proof closes all listed obligations. There is no outstanding private ground-truth warning.
