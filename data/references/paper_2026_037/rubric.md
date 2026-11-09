# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Common weighted-mean reduction (3 points):** Correctly identifies the self-normalized weighted reference mean and rewrites both estimators using it, including the Gaussian score formula for estimator B. Justifies well-definedness and finite second moments: the transition weights are positive and normalized, and the squared norm of the weighted mean is bounded by the sum of the squared norms of the references, which has finite expectation.
2. **Exact anticorrelation (3 points):** Centers both estimators at their own reference-bank expectations, derives the opposite linear transforms of the common fluctuation, and proves rho <= 0. Establishes the requested strictness conclusion using positive definiteness: equality occurs exactly when the weighted reference mean is almost surely constant.
3. **Variance minimization (3 points):** Expands the blend variance, differentiates or completes the square, and obtains the stated unique minimizer and minimum under D > 0. Justifies global uniqueness by the positive quadratic coefficient.
4. **Interior weight conclusion (1 point):** Correctly proves that rho < 0 implies 0 < lambda* < 1.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Scores should reflect the centered finite-sample variance objective; no finite-sample unbiasedness claim is required. The optimization is over deterministic real lambda with y and t fixed, not reference-bank-dependent mixing rules. The strictness conclusion is part of the task and is required for full credit, although it may follow immediately from a displayed negative quadratic form and a clear invocation of positive definiteness. A brief justification of positivity and integrability suffices; omission of this routine justification alone is a readily repairable omission, not a failure of the main argument. No asymptotic argument, proof of unconditional strict negativity for every Gaussian reference bank, or separate analysis of D = 0 is required. The proof must remain valid for N = 1.
