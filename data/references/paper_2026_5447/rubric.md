# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly handles the supplied additive target cost, its global sum S, and the complementary weight C(y,y')=S-D(y',y). Computes S and the unweighted outer cost sum from the compact tables without an exponential-size oracle, retaining the constant shift.
2. **3 points:** Derives the exact product factorization of the actual inner relative-score sum over y'', together with the finite-sum identities needed for weighted label-wise marginalization. Does not substitute a single unnormalized exponential or merely name factorization.
3. **3 points:** Handles tau=0 by expanding the logarithm of the inner product and evaluating the constant, matching, and cross contributions. Explains how to aggregate cross contributions without a quadratic loop and covers l=1. An equivalent partition-and-score derivation is equally acceptable.
4. **2 points:** Handles tau>0 with the sign in the task, the factor 1/tau, and the full subtracted unweighted cost sum. Establishes that all necessary products and replacements take O(l) operations, divisions are legitimate, and the complete evaluation uses O(l) storage under the stated computational model.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular arrays.

Deduct substantially for evaluating a different surrogate, omitting either parameter regime, treating S or another exponential-size sum as an oracle, dropping the constant cost contribution, or asserting linear time while retaining a quadratic cross-term computation.

The relevant partition marginals are strictly positive for finite scores. Do not require a zero-partition-factor case or prefix/suffix products when this positivity justifies division. Individual additive cost terms and weighted marginals need not be positive and may vanish.

The task deliberately retains Phi_tau(u)=(u^{-tau}-1)/tau for tau>0. Do not require continuity at tau=0, statistical consistency, or nonnegativity of the resulting surrogate. Do not award full credit to a proof that silently reverses this sign.

The operation count includes elementary-function evaluations as specified in the task; arbitrary-precision bit complexity and floating-point stability are not required. No population-risk, hypothesis-class, sampling, or parameter-search theorem is part of this task.
