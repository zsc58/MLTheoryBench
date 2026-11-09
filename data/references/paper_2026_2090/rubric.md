# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Uses the perfect-predictor assumption and quadratic loss to show that the baseline loss is zero and that permutation importance is the expectation of the squared prediction difference under the chosen perturbation law.
- **4 points:** For an independently resampled marginal feature, correctly matches that expectation to the definition of the unrestricted total index and derives $\nu_j^{\mathrm{ind}}=2\tau'_j$.
- **4 points:** For a conditionally resampled feature, correctly uses the conditional law given $X_{-j}$ (with the required conditional independence) to match the dependent-feature total index and derives $\nu_j^{\mathrm{cond}}=2\tau_j$.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. The factor-of-two normalization and the distinction between independent and conditional perturbation laws are theorem-critical; merely naming total indices without establishing the expectation identities is insufficient.

The marginal-resampling expectation may be infinite even though $\mathbb E[g(X)^2]<\infty$. The target permits this, and the direct proof by equality of nonnegative integrands remains valid without a separate finiteness argument. Do not require an additional marginal-resampling moment assumption or penalize a proof that works directly with nonnegative extended expectations. Conversely, do not accept an unsupported claim that the original square-integrability assumption ensures marginal-resampling finiteness.

The conditional-resampling expectation is finite because the perturbed vector has the original joint law, but proving that additional fact is not a separate scoring requirement. Neither a variance representation of the index nor any normalization by output variance is required. Constant predictors, degenerate features, and $d=1$ are included; the same algebra applies without case splits.
