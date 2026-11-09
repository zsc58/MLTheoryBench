# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the operator-norm constraint, nuclear-norm support identity, cumulative matrices, admissibility conditions, and stated update; establishes the required feasibility. Ordinary gradients are evaluated only at positive-definite algorithmic parameters.
- **3 points:** Derives the exact Bregman regret decomposition and applies dominance, positive-definite smoothness, upper stability, and the initial boundary value. Correctly obtains the temporal-plus-initial contribution ||G_1||_*+(alpha/eta)Tr L_T.
- **3 points:** Establishes a valid trace estimate for the Bregman sum and obtains the general bound with the stated constants. The source route uses G_{t+1}G_{t+1}^T<=G^2 I, compares G^2 I+M_t with M_{t+1}, and applies trace-square-root concavity at the updated endpoint. It retains the subtraction Tr(M_1^{1/2})=||G_1||_*. Singular auxiliary cumulative matrices must be handled correctly, for example by positive-definite regularization. Substitution of eta=sqrt(alpha/beta) must give both the leading constant and the initial-gradient coefficient.
- **2 points:** Verifies that the specific family is finite and convex, continuously differentiable for positive-definite L, feasible including the singular-parameter subgradient boundary, dominant with the correct boundary value, upper stable with alpha=1, and smooth with beta=1. Correctly establishes the required Hessian or an alternative smoothness bound, then derives the explicit update and final adaptive trace bound.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's presentation choices or its augmented-matrix representation if another proof closes the same obligations.

The independent matrix-analysis facts stated in the reference proof may be invoked with their hypotheses verified. A bare citation to the paper-specific Hessian estimate is not by itself a completed admissibility proof; its derivation or another valid smoothness argument must be supplied.

Do not accept Tr(H A^{-1/2})<=2[Tr sqrt(A+H)-Tr sqrt(A)] as an initial-endpoint concavity inequality: it is generally false. The standard upper bound pairs H with the inverse square root at the updated endpoint. A solver may use any other valid argument that obtains the required constants.

Because G>0, every L_t is positive definite. Do not demand generalized inverses for L_t or penalize their absence. Conversely, a global Loewner comparison with a singular matrix's Moore-Penrose inverse is not justified merely by ordinary inverse order; support restrictions or a regularization argument are needed.

Do not require an ordinary gradient for the boundary value Psi~(S;0)=||S||_*. At singular parameters, feasibility is the subgradient condition explicitly stated in the task. The proof must not silently assert differentiability of the nuclear norm at zero.

The argument must cover T=1, zero gradient matrices, singular cumulative Gram matrices, and all positive m,n. No condition m<=n or n>=m+2 is needed for this task. Omission of the admissibility bottleneck or an error that leaves the claimed regret constants unsupported is theorem-critical.
