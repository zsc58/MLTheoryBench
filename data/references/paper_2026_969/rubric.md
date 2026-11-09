# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Quantile reduction (2 points).** Correctly uses or proves the one-dimensional W2 quantile identity for the laws appearing in the task, with the finite-second-moment setting justifying the L2 operations. A valid alternative argument establishing the same reduction receives equivalent credit.
2. **Exact decomposition (4 points).** Inserts the within-group barycenter, expands the L2 square, and correctly identifies \(G_2=V_{\rm mix}+V_{\rm bar}+R\), or supplies an equivalent valid derivation.
3. **Remainder bound (3 points).** Derives \(|R|\le2\sqrt{V_{\rm mix}V_{\rm bar}}\) using valid Cauchy–Schwarz estimates with the stated weights, or an equivalent argument.
4. **Scope fidelity (1 point).** Respects the one-dimensional finite-second-moment setting and normalized nonnegative weights, proves both target clauses, and does not impose extra density, boundedness, or positivity assumptions.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's presentation. The standard one-dimensional Wasserstein quantile identity may be invoked without reproving optimality of the quantile coupling; it must be correctly applied. Naming a method without carrying out the theorem-specific inference earns no credit for that inference.

Do not require a separate derivation of the weighted-average barycenter quantiles or a separate existence-and-uniqueness proof: these are setup verifications supplied in the reference proof, not additional requested conclusions, and the decomposition does not require the barycenter formulas. A proof using the defined centers directly can receive full credit.

Zero weights and vanishing variance terms are allowed. An argument valid for nonnegative weights without division already covers these cases and need not list them separately. Endpoint values of quantiles are irrelevant to the Lebesgue integrals; arbitrary endpoint extensions cause no mathematical error if used only under those integrals.
