# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **4 points:** Establishes the necessity mechanism: for a fixed coordinate section, constructs a separating direction and a convex rank-one quadratic realizing the required two-point gradients, thereby forcing every output difference to be a nonnegative multiple of the input difference. For the smooth claim, it must validly control the quadratic's Hessian norm by \(L\), or otherwise validly establish the same necessity.
- **3 points:** Correctly turns the section-wise directional condition into affine sections with constant nonnegative slopes, proves compatibility across coordinates, and obtains the global form \(A(z_1,\ldots,z_n)=\sum_i\alpha_i z_i+c\).
- **2 points:** Proves both preservation directions from the positive-affine form: monotonicity by summing component inequalities and co-coercivity by using the convex \(L\)-smooth gradient inequality together with the required weighted norm bound. It must address the \(\sum_i\alpha_i=0\) case.
- **1 point:** Correctly derives the arithmetic-mean specialization from idempotence and permutation invariance.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.
