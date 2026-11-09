# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Protocol reduction and definitions (1 point):** Correctly identifies the bipolar binding/unbinding setup and reduces recovered-value cosine similarity to the cosine between \(\operatorname{sign}(H+N)\) and \(H\), noting that bipolar binding preserves norms and inner products.
2. **Normalized bipolar-noise geometry (3 points):** Derives the agreement/cancellation outcomes, the binomial count, the exact finite-dimensional identity \(\operatorname{CosSim}=\sqrt{K_D/D}\), and the limit \(1/\sqrt2\). Merely naming a binomial or concentration argument without these calculations is insufficient.
3. **Gaussian recovery formula (3 points):** Handles zero-probability ties, computes the coordinate agreement probability \(\Phi(1/\sigma)\), and derives the expected cosine \(2\Phi(1/\sigma)-1\) for arbitrary \(\sigma>0\).
4. **High-dimensional concentration (3 points):** Supplies valid Hoeffding-based concentration for the bipolar case, including the justified inverse-square-root transfer with the required constants, and for the Gaussian case around its stated mean; preserves the required probability and parameter regimes.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat the finite-dimensional bipolar expectation as a convergence statement, not as an exact equality at every D.
