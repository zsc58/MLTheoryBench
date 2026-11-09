# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Works with the specified diagonal-second-moment surrogate, expands or differentiates it correctly, and obtains the unrestricted Frobenius gradient flow. With P=WW^T, C=W Sigma W^T, and S=W Sigma A W^T, the correct gradient is PBC-S. An equivalent direct coordinate derivation is acceptable.
- **3 points:** Computes the hard-cluster projected matrices, establishes entrywise decoupling, solves the diagonal scalar ODEs for the prescribed initial condition, and identifies the rate eta n_j C_j. Establishes the quadratic cluster-size comparison relative to q_j with constants controlled by m and M.
- **3 points:** Uses rotational invariance and unit norm to establish the two exact embedding-ensemble mean identities. Applies the defined separate-expectation approximation and proves that its homogeneous matrix directions have common relaxation rate eta(N/K)^2 bar_sigma^2. This step does not require, and must not falsely assert, concentration or an equation for E[B(t)].
- **2 points:** Determines the limiting shared coefficients and the minimum surrogate loss, and explains collision error correctly. The limiting coefficient is S_j/(n_j C_j). The minimum loss is one half of the sum over clusters of T_j-S_j^2/(n_j C_j), where T_j=sum_{i in G_j} a_i^2 sigma_i^2. It is positive if any cluster has more than one feature and zero when all clusters are singletons. Correctly distinguishes aggregation-based acceleration from mean-field rate equalization.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's notation or presentation.

The input coordinates have nonzero means, so the exact population objective does not have diagonal uncentered second moment. The public task expressly defines the surrogate flow; showing that the exact population flow differs does not refute this repaired task.

The trainable matrix is unrestricted. The symmetrized formula (PBC+CBP-S-S^T)/2 is not its general gradient. A proof using that formula must repair the differentiation or supply a valid direct derivation of the requested dynamics; agreement on some special diagonal rates alone does not establish the general gradient step.

The random-case target concerns ensemble means and the explicitly defined mean-field approximation. Do not demand independence of columns for the first-moment identities, a concentration bound, an approximation error estimate, or a proof about E[B(t)]. Conversely, an unsupported assertion that N much larger than K forces W Sigma W^T to concentrate is an error, not an acceptable substitute for the requested mean-field reasoning.

The collision error includes unwanted within-cluster outputs, not merely disagreement among teacher coefficients. In particular it remains positive for a nonsingleton cluster when b=0. Calling S_j/(n_j C_j) the weighted average without its factor 1/n_j is incorrect.

The variance-scale comparison does not hold that q_j is fixed while the normalized feature distribution changes. No nonlinear power-law exponent is part of the task. No proof of the private concentration counterexample is required.
