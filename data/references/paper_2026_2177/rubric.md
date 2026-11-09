# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Tensor-product basis (2 points):** Verifies orthonormality and identifies the finite tensor-product space.
2. **Kernel/RKHS bridge (2 points):** Derives the finite kernel expansion and establishes kernel-section membership and the reproducing property.
3. **SVM-to-coordinate derivation (4 points):** Expands the defining signed kernel combination and derives \(c_k=\sum_i\alpha_i y_i p_k(x_i)\); naming a method alone earns little credit.
4. **Matrix identity and uniqueness (2 points):** Proves \(c=P^Ts\) and uniqueness of coefficients.

# Evaluator Notes

Accept any complete valid alternative proof. The bias term is irrelevant because the target concerns the regularized component. The signed kernel representation of h is a definition in the task: do not require a proof of the representer theorem, solution of the dual optimization problem, or use of optimality in the coefficient calculation. A direct proof from that definition is sufficient. No full-rank assumption on P, distinctness of training points, or nonzero-norm assumption on h is needed. A uniform argument covering n=0 and h=0 need not discuss them separately.
