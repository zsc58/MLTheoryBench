# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly expands `HH^T` into the squared-column and pairwise-product Gram terms and applies `2 sum_{a<b}x_a x_b=(sum_a x_a)^2-sum_a x_a^2` entrywise.
- **2 points:** Uses `WW^T=I_m` to obtain `RR^T=1/2(I_m-QQ^T)` and hence `HH^T=1/2 QQ^T+1/2 I_m`.
- **3 points:** Correctly reduces `tr(QQ^T Sigma)` by cyclicity and `Sigma=W diag(v)W^T` to `tr(C^T diag(v)C)=v^T((C^(odot 2))1_m)`.
- **2 points:** Combines the trace terms, handles the sign and absolute value in the curvature definition, and states the exact closed-form identity (including the contraction-elimination consequence).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The central Gram-matrix collapse and the subsequent trace reduction are theorem-critical; merely naming orthogonality, a pairwise-sum identity, or a spectral argument without carrying out the derivation does not earn the corresponding credit.
