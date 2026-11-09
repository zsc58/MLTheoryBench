# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Defines the normalized tilted density \(\rho_\tau\), verifies it is a probability density, and sets up the weighted KL objective over all probability densities under the stated extended-value convention.
- **5 points:** Correctly expands and rearranges the weighted KL terms to obtain the exact decomposition \(J_\tau(r)=\mathcal S_\tau(P\|Q)+D_{\mathrm{KL}}(r\|\rho_\tau)/[\tau(1-\tau)]\), including the normalization constant and the extended-value support cases.
- **3 points:** Uses KL nonnegativity and its equality condition to prove the minimum value, attainment at \(\rho_\tau\), and uniqueness almost everywhere.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A proof must not perform undefined \(\infty-\infty\) algebra; it should either justify the extended-value identity or explicitly handle support and infinite-KL cases.
