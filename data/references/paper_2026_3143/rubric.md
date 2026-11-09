# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Adaptive finite-population unbiasedness (3 points).** Establish that LURE is unbiased for the mean of an arbitrary fixed real array under the admissible adaptive sampling process, or supply an equivalent complete argument for the arrays needed in the task. The reference route derives the running-average representation, its conditional-mean identity, and coefficient normalization. Accept other valid routes without requiring those particular auxiliary objects. Recognize that the fixed finite pool and finite history tree, together with strict positivity, ensure the moments used in the proof exist.
2. **Exact PPAT unbiasedness (2 points).** Use the centered proxy array \(c_i=\widetilde\ell_i-\widetilde R_M\) and its zero finite-pool mean to prove \(\mathbb E[\widehat R_{\mathrm{PPAT}}(\lambda)]=R_M\) for every fixed \(\lambda\) and admissible adaptive proposal process.
3. **Control-variate variance identity (3 points).** With a fixed proposal process and common sampled indices and weights, express PPAT as \(L-\lambda C\), establish \(\mathbb EC=0\), and derive the full quadratic variance formula including the covariance and variance terms.
4. **Optimal tuning and strict-reduction region (2 points).** For \(\operatorname{Var}(C)>0\), derive \(\lambda^*=\operatorname{Cov}(L,C)/\operatorname{Var}(C)\), prove uniqueness of the variance minimizer, and characterize strict improvement precisely for \(\lambda\) strictly between \(0\) and \(2\lambda^*\), with endpoints ordered. The interval is empty when \(\lambda^*=0\). When \(\operatorname{Var}(C)=0\), conclude that \(C=0\) almost surely, every coefficient gives the same estimator and variance as LURE, and there is no strict improvement.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. In particular, neither pairwise uncorrelatedness of the running averages nor the general LURE variance decomposition is a required conclusion or an additional condition for full credit.

Award no credit for merely naming importance weighting, control variates, or a generic unbiasedness theorem without justifying its application to the stated adaptive finite-population sampling law. A complete alternative derivation can replace the reference conditional calculations.

The proposal process and its induced sampling law must remain fixed during optimization over the coefficient. The task does not optimize a family of sampling laws that changes with that coefficient, and it does not assert unbiasedness for a coefficient estimated from the sampled data.

Fixed labels are not initially available to the proposal maps. Their fixedness permits the index-history filtration after conditioning, while admissibility still restricts information access to initial side information and previously queried labels.

No uniform-overlap bound across budgets or asymptotic moment condition is required. The claims are finite-sample statements; a proof need not use the assumed pool-ratio limit.
