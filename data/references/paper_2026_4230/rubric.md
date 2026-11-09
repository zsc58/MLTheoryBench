# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly formulates and solves the diagonal reverse-KL covariance optimization, deriving \(1/d_p^*=e_p^\top\Sigma^{-1}e_p\).
- **3 points:** Uses the spectral overlap weights and weighted AM-HM inequality to prove \(\operatorname{Tr}(\Sigma)\ge\operatorname{Tr}(S^*)\); merely naming AM-HM without the weighted representation is insufficient.
- **2 points:** Derives the conserved identity \(\operatorname{Tr}(\Sigma^{-1}S^*)=P\).
- **3 points:** Relates empirical predictive variances to \(\operatorname{Tr}(\widehat\Gamma C)\), substitutes \(\widehat\Gamma=(\sigma^2/N)(\Sigma^{-1}-\alpha I)\), and concludes MFVI's empirical average predictive variance is no smaller than the exact posterior's.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The common observation-noise term may be omitted if the solver explicitly compares parameter-induced predictive variances.
