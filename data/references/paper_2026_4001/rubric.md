# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Identification and score centering (2 points).** Derives psi=E_T[mu(X)] from covariate shift and source selection on observables, and verifies that the displayed score has mean zero. The weighted source representation is valid supporting material but is not required if unused in an otherwise complete proof.
2. **Exact split-sample expansion and overlap control (2 points).** Establishes a positive lower bound for the true pooled labeled propensity from source-label overlap and the likelihood-ratio bound, and obtains an exact normalized empirical decomposition on an event with probability tending to one. Keeps the true and estimated overlap constants distinct, or explicitly takes a common smaller constant. Respects the estimator's exceptional-case definition.
3. **Nuisance and normalization remainder control (4 points).** Bounds the population remainder by a constant times ||hat mu-mu||_2 (||hat g-g||_2+||hat pi-pi||_2), and uses the product condition to obtain o_p(n^{-1/2}). Establishes the L2 ratio-error bound and PB^2=o_p(1) using all three nuisance consistencies, the estimated-g bound, overlap, and the conditional residual second-moment bound. Uses independent training and a valid conditional variance or equivalent argument to show that the empirical nuisance remainder is o_p(n^{-1/2}). Controls hatrho-rho at O_p(n^{-1/2}) and the resulting normalization remainder. No upper bound on hat pi is assumed or needed.
4. **Limit theorem (2 points).** Concludes the asymptotic linear expansion, including transfer from the high-probability event to the actual estimator, and applies the iid finite-variance CLT and Slutsky to obtain the stated limit with variance Var_P(varphi). The argument must remain valid when that variance is zero; the limiting normal law is then the point mass at zero.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its notation for localization, or a separate derivation of the unused weighted source representation. Treat omission of the product-rate remainder bound or of a valid sample-split empirical-term argument as theorem-critical gaps. The population bound is a product with a sum, not a product of all three nuisance errors. Conditioning on the independent training sample is valid; conditioning additionally on an evaluation-dependent event cannot be used to assert that the evaluation observations remain iid without justification. A concise correct high-probability localization argument is sufficient. No semiparametric efficiency claim, canonical-gradient derivation, or specialized external efficiency lemma is required.
