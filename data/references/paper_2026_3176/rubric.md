# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Ambient conformal control (2 points):** Correctly invoke or derive the exchangeable rank argument showing \(\Pr(S_{n+1}>\tau_\alpha)\leq\alpha\) for the stated calibration quantile. The justification must apply to tied scores and the \(+\infty\) cutoff convention. An accurate invocation of standard split-conformal coverage under the stated fixed-score and exchangeability assumptions is sufficient.
2. **Manifold-tube bottleneck (4 points):** Show that empirical-tube failure implies an empty cover cell containing the test target, and rigorously derive the iid probability \(p_j(1-p_j)^{n_0}\), where \(p_j=Q(A_j)\), and its bound using \(p_j\geq\beta_\varepsilon\). An equivalent argument bounding the probability that any cover cell is empty also earns full credit; the particular test-cell factor is not mandatory.
3. **Finite-cover aggregation (2 points):** Apply the finite union bound and obtain \(\Pr(d_M(Y_{n+1})>\varepsilon)\leq N_\varepsilon(1-\beta_\varepsilon)^{n_0}\), without assuming disjoint cells or strictly positive cell masses.
4. **Final coverage conclusion (2 points):** Combine the two failure events by a union bound and conclude exactly the claimed lower bound for the empirical manifold-constrained set. No independence between the two failure events, or between the test target and calibration, may be presumed.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, auxiliary tie-breaking variables, or a separate discussion of measurability when the task's explicit definitions already ensure it. No transport-geometric theorem or special metric property is needed beyond the specified score and cover diameter condition.

The task permits \(\beta_\varepsilon=0\) and \(\beta_\varepsilon=1\). A proof whose inequalities already cover these cases need not discuss them separately. Conditional calculations on zero-mass cells require appropriate treatment; unconditional iid products avoid this issue. Cover cells may overlap. A negative final lower bound is valid and does not require truncating or changing the target.

Treat omission of the empty-cell implication or the finite-cover occupancy bound as theorem-critical gaps. Do not penalize a proof that correctly notes some stated source assumptions are unnecessary for a particular proof step. Do not require independence of tube failure from calibration scores.
