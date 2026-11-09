# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Polynomial state/regressor growth (2 points).** Obtains a fixed positive C_z and r in the stated range, independent of T, eta, and epsilon, with the requisite aggregate second-moment and truncation bound. A covariance/Jordan proof must handle possible dependence between x_0 and w_0: bound the first state directly and run the covariance recursion from time one, or give an equally valid alternative. Absorb the summation factor into C_z before defining the task's radii.
2. **Uniform regressor small-ball bound (3 points).** Proves the displayed k_z and p_z using a valid filtration and the actual independence assumptions. The log-concave projection moment comparison, shift argument, and input moment calculation must give numerical bounds sufficient for the task. The supplied proof gives noise probability 3/32 and input probability min{1,sigma_u^2}/[4(1+m u_max^2)]. Do not assume a positive conditional small-ball bound for z_1; it may vanish identically under the task assumptions.
3. **Block persistent excitation (2 points).** Establishes the applicable conditional lower-tail result at every included observation, constructs sufficient sphere nets, controls approximation on truncation, and obtains PE failure at most eta/2. The sharper quoted covering cardinality is not required: an elementary packing-volume proof of the needed logarithmic bound is sufficient. Blocks must start where the excitation hypothesis is valid.
4. **Boundary elimination and final sample bound (3 points).** Uses a parameter-direction net and empirical PE to select a sufficiently large signed coordinate at a predictable first-hit time. Feasibility requires avoidance of the opposite boundary interval. Apply the two-sided boundary mass assumption, use atomlessness for endpoint equality if necessary, and justify iteration over blocks without conditioning on future PE or truncation. Verify the exact sample-size coefficient and integer block count, including any discarded initial observations. For the reference construction, kappa=ceil(8L_z/p_z^2), N=floor((T-2)/kappa), and q=c_w k_z p_z epsilon/(16sqrt(n)) give qN>=L_gamma-1. Combine the two failure bounds to prove the stated Frobenius-diameter guarantee.

# Evaluator Notes

Accept any complete valid alternative proof, including different valid block arrangements or elementary concentration/covering arguments. Do not require the reference proof's incidental notation or its exact decomposition into events.

The source allows x_0 to depend on w_0. Imposing independence of these two variables is not an acceptable way to close an initialization gap. An otherwise complete proof that only needs a routine initialization/indexing repair should be judged according to the scale above, rather than automatically rejected; a proof that relies essentially on the stronger assumption is incomplete.

Merely naming BMSB, a net argument, or a specialized elimination method does not close the corresponding obligation. A missing predictable block iteration or an unsupported exact probability calculation is a theorem-critical gap. The opposite-sign probability inequality may be shown directly without separately announcing a sign reversal. Do not penalize that presentation choice when the inequality is correct.

The final rate is tilde-O(1/epsilon) for fixed model parameters and confidence, with dependence given by the task's explicit formula. Do not require an additional dimension-only uniformity claim that suppresses the dependence of r or C_z.
