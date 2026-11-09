# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Similarity representation and inequalities (3 points):** Derives the semigroup inner-product representation, applies positivity and Cauchy-Schwarz to establish 0<s_t<=1 and s_t(x,x)=1, and concludes 1<=gESS_w(t)<=ESS(w) for every t>0. The reciprocal operation must be valid; nonnegative weights summing to one ensure sum_i w_i^2>0 and hence a positive denominator.
2. **Duplicate invariance (2 points):** Correctly groups equal locations and shows that replacing duplicate labels by one atom with their summed weight leaves the gESS denominator, and hence gESS, unchanged. Zero-weight labels may be retained or discarded.
3. **Fine-scale limit (3 points):** Applies valid small-time heat-kernel estimates to finitely many fixed distinct support points to prove off-diagonal normalized overlaps vanish, and obtains gESS_w(t)->(sum_a alpha_a^2)^(-1), including the distinct-atom specialization. For example, Gaussian upper and diagonal lower bounds yield s_t(z_a,z_b)<=C_1 exp{-c_1 d_g(z_a,z_b)^2/t} for sufficiently small t. A diagonal asymptotic and an appropriate off-diagonal estimate are also acceptable. The limiting denominator is positive because the merged masses sum to one.
4. **Coarse-scale limit (2 points):** Uses valid compact connected heat-flow convergence, or spectral convergence with sufficient control, to show the normalized similarities tend to one and therefore gESS_w(t)->1. One acceptable justification smooths at a fixed positive time, applies mean-zero L^2 spectral contraction between the smoothed sections, and uses the semigroup identity to obtain uniform heat-kernel convergence to one.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Standard independent heat-kernel results may be invoked without reproving them, but their relevant content and application must be clear. Require justification of the limiting arguments; merely naming Cauchy-Schwarz, Gaussian bounds, or a spectral gap without applying them is insufficient. Uniform convergence over all of M is sufficient but not necessary: convergence at the finitely many relevant pairs and diagonal points suffices.

The support configuration and weights remain fixed while t varies. Do not require homogeneity, curvature restrictions, strictly positive individual weights, or a minimum-separation assumption beyond distinctness of finitely many fixed locations. A single positive-mass location entails no off-diagonal limit obligation.

The stated manifold assumptions also allow the connected zero-dimensional case, which is a singleton with normalized heat kernel identically one. It can be handled directly rather than by invoking a nonexistent nonconstant eigenvalue. An otherwise complete proof that overlooks only this immediate case has a readily repairable omitted case, not a failure of the positive-dimensional limit arguments. Do not award full correctness to an argument that explicitly asserts a nonconstant spectral gap exists on a singleton without addressing that case.
