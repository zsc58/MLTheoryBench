# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes that the surrogate's expectation under the applicable true-label channel equals the clean loss, and uses the stated selection/noise independence to identify \(m_i=\mathbb E[\widetilde\ell_i\mid x_i,o_i=1]=\ell(\hat r_\theta(x_i),r_i^*)\). Direct use of the defining surrogate equations is sufficient; explicit inversion and display of the two surrogate values are optional.
- **3 points:** Correctly justifies indicator weighting or equivalent conditioning with fixed propensity estimates and obtains IPS unbiasedness when \(\hat p_i=p_i\). A general expectation formula \((p_i/\hat p_i)m_i\) is sufficient but not mandatory if the proof correctly specializes directly to exact propensities.
- **3 points:** Computes the DR expectation or supplies an equivalent valid argument, and proves the correct-propensity branch for arbitrary fixed finite imputations. The identity \(\mathbb E[L_{\mathrm{DR}}^*]-L_{\mathrm{ideal}}=n^{-1}\sum_i(1-p_i/\hat p_i)(\hat\varepsilon_i-m_i)\) is one acceptable route, not a required presentation.
- **2 points:** Proves the correct-imputation branch using \(\hat\varepsilon_i=m_i=\mathbb E[\widetilde\ell_i\mid x_i,o_i=1]\), establishing unbiasedness for arbitrary fixed positive propensity estimates.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require matrix inversion, the reference proof's exact bias decompositions, or its incidental presentation choices. Merely naming double robustness without establishing the relevant expectation cancellation is insufficient.

The public contract fixes the predictor and estimated functions with respect to the annotation and observability draws. A proof may use this assumption without restating it, but must not replace it with the invalid claim that conditioning on arbitrary same-sample fitted nuisances leaves the stipulated sampling law unchanged.

Treat omission of either DR branch or failure to justify the surrogate conditional mean as theorem-critical. Do not require cross-unit independence, positivity of imputed or surrogate losses, both preference classes to occur, or strict inequality \(p_i<1\). The finite-value and positive-denominator assumptions already ensure integrability. Separate discussion of every boundary case is unnecessary when the argument applies to them. In particular, a proof should not rely on conditioning on \(o_i=0\) when that event may have probability zero.
