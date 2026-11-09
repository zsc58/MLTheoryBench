# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derives the dual of the stated generalized KL transport objective with constraints f_i+g_j<=D_ij and objective sum_i a_i psi_kappa(f_i)+sum_j b_j psi_kappa(g_j). Explains the scalar conjugacy and justifies equality of primal and dual values, either directly or by a valid duality theorem with its hypotheses checked. The uniform specialization has coefficients 1/n and 1/m, with no redundant factor kappa.
- **2 points:** Establishes dual attainment and uniqueness under positive masses and finite costs. Gives the KKT marginal relations (T*1_m)_i=a_i exp(-f_i*/kappa) and ((T*)^T1_n)_j=b_j exp(-g_j*/kappa), with complementary slackness, or an equivalent characterization sufficient for the argument. Strict concavity establishes uniqueness only after attainment is justified. Accept either compact-superlevel arguments or construction from a primal optimum with positive marginals.
- **4 points:** Justifies sensitivity of the value for the specified two-sided, mass-preserving perturbation with D fixed. Establishes the relevant local compactness/continuity conditions for an envelope theorem, proves the required comparison inequalities directly, or supplies an equivalent complete sensitivity argument. Obtains psi_kappa(f_i*)-(n-1)^(-1)sum_{k!=i}psi_kappa(f_k*) with all normalization factors correct.
- **1 point:** Identifies the score as the negative derivative and correctly explains that a positive score gives a negative first-order change for increasing that segment's mass with uniform compensation. A negative score has the opposite interpretation; a zero score gives no strict first-order change.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not award the central points for merely naming duality, KKT, or an envelope theorem without carrying out the normalization and centered differentiation and verifying their applicable hypotheses.

The cost compares segment distributions conditional on labels, not distributions of labels conditional on segments. The matrix is constructed from the original empirical data and remains fixed when the outer masses vary; differentiating a recomputed cost matrix answers a different question.

Opposite constant shifts of f and g preserve the constraints but do not preserve the KL dual objective. A balanced-transport gauge argument is not a valid attainment or uniqueness argument here. Neither uniqueness of the primal transport plan nor differentiability of the optimizer is required. Zero costs, c=0, repeated segments, tied values, and nonunique primal plans must not be excluded. The theorem imposes no independence or stationarity assumption and uses no entropy-regularized approximation.
