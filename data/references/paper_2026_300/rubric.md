# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly transfers the instrumental-variable moment from the latent model to the observed unpaired covariances, states the high-dimensional limits and sampling/moment assumptions, and sets up the covariance-error decomposition.
2. **2 points:** Expands the naive two-sample IV numerator and denominator and proves the self-product error has limit \(b/\widetilde r\), while the other terms vanish, obtaining the attenuation limit \(Q\beta^*/(Q+b/\widetilde r)\).
3. **4 points:** Derives the cross-fold expansions for \(C_{XX}\) and \(C_{XY}\), proves all signal-error, cross-sample, and distinct-fold error products vanish under the stated bounds, and identifies the limits \(Q\) and \(Q\beta^*\). This is the central debiasing bottleneck.
4. **2 points:** Uses positive definiteness and convergence of the weight matrix, establishes eventual invertibility, and applies a valid continuous-mapping argument to conclude \(\widehat\beta_{\rm CF}\to_p\beta^*\) for fixed dense dimension.

# Evaluator Notes

Accept any complete valid alternative proof under exactly the public assumptions. Do not award credit for merely naming cross-fitting, GMM, concentration, or U-statistics without deriving the required limits. A minor algebraic or notation slip is repairable only when the corresponding limit argument is otherwise complete; omission of the nonvanishing self-product term or replacement of cross-fold products by self-products is theorem-critical.
