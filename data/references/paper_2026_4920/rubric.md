# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Finite-class statistical control (2 points).** Obtain a high-probability trajectory-level error of order log(|Pi|/delta)/n. A direct deterministic-label consistency/union-bound argument is sufficient. Alternatively, give a valid finite-class realizable Hellinger argument followed by the appropriate deterministic-policy comparison. A generic claim that TV is bounded by squared Hellinger is not sufficient.

2. **Correct observation experiment and disagreement interpretation (2 points).** Connect the statistical error to the probability of any auxiliary learner-label mismatch along an expert trajectory, or establish the equivalent correctly typed auxiliary trajectory-TV bound. Distinguish expert-induced conditional dequantization from representative-action deployment. A direct proof of the disagreement interpretation earns full credit without introducing extended raw-action laws. If projection identities are used, their common-kernel and zero-probability cases must be justified.

3. **Shared-noise stability/RTVC coupling (4 points).** Construct a valid sequential coupling with correct expert and deployed-learner marginals. Justify the threshold-cost coupling and the conditioning used in the RTVC estimate. On a good prefix, combine binning with the k epsilon_q transport threshold to bound raw-action discrepancies by (k+1)epsilon_q, and then use the maximum-input global P-IISS assumption. Derive a first-failure or equivalent estimate charging statistical disagreement once and at most H kappa(gamma((k+1)epsilon_q)) for transport failure. Merely naming coupling or stability receives no credit for this step. A whole-trajectory gluing argument must not assume, without proof, preservation of conditional laws under an enlarged filtration.

4. **Regret comparison and final substitution (2 points).** Use bounded rewards on the failure event and Lipschitz rewards on its complement. Obtain the H log(|Pi|/delta)/n statistical term, the H^2 kappa(gamma((k+1)epsilon_q)) term, and the H[gamma((k+1)epsilon_q)+(k+1)epsilon_q] term, with constants depending only on the stated reward bounds and Lipschitz constants.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require Hellinger distance, an extended-law construction, or a maximal whole-trajectory coupling when an equivalent direct statistical-disagreement and causal-coupling proof is supplied. The theorem-critical stability/RTVC argument remains a major requirement.

The expert's quantized policy is deterministic; the raw expert may be stochastic. A proof that assumes raw determinism without addressing this distinction does not prove the full task. Policies may assign zero mass to labels, and a complete argument must not rely on an unstated strict-positivity assumption.

The broader source general-decomposition proof has an unsupported post-gluing conditional estimate. It is not an available black-box premise. The replacement reference proof closes the required specialization independently, so there is no unresolved reference-proof obligation for this task.
