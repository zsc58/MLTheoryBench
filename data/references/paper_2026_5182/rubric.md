# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses a minimum-cardinality exact vector as a comparator and obtains surrogate value \(\tau^2K\).
- **5 points:** For every binary vector with \(k<K\) nonzero entries, correctly applies the definition of \(r_k\) and the strict separation condition to prove its surrogate value is strictly greater than \(\tau^2K\). This exclusion is vacuous when \(K=0\).
- **3 points:** For an arbitrary surrogate minimizer, combines the comparator bound, exclusion of under-budget vectors, nonnegativity of the residual, and positivity of \(\tau\) to prove both cardinality \(K\) and zero residual, concluding minimum-flip exact feasibility throughout the stated domain.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A proof that only asserts that the penalty favors sparsity, without establishing the strict exclusion of every \(k<K\) case, misses the central argument.

The task permits \(K=0\). In that case the separation assumption has no instances. Accept either a uniform proof covering this case, as in the reference proof, or a separate argument using the zero vector's zero objective and the strictly positive objective of every nonzero binary vector. Do not require a separate case split when the argument already handles \(K=0\). A genuinely omitted zero-cardinality case is a readily repairable omitted case under the scoring guide.
