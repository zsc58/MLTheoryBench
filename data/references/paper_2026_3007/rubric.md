# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Kernel positivity and convex risk (2 points).** Verify sufficient weighted integrability to define the representation and justify the pairings and Fubini. Establish the kernel quadratic form as an integral of a square, or use an equivalent bounded-linear-representation argument, expand the risk, and conclude convexity.
2. **Strong convexity, existence, uniqueness, and Euler equation (3 points).** Use both regularization terms and coercivity/weak lower semicontinuity in the Hilbert space W to obtain a unique minimizer. Derive its variational equation for every test in W and then the distributional elliptic equation. An equivalent valid variational existence argument is acceptable. Do not assume compactly supported smooth functions are dense in W on an arbitrary open domain.
3. **Elliptic regularity (3 points).** Prove the nonlocal forcing is locally Lipschitz under the stated growth, weight, and feature assumptions. State and apply the relevant interior elliptic estimates and local Sobolev/Morrey embeddings with verified hypotheses. Give a dimension-correct bootstrap from W^{1,2}_loc to W^{3,p}_loc for every finite p>1, handling critical exponents by subcritical embeddings or another valid method. For each 0<s<1, choose a sufficiently large finite p to obtain C^{2,s}_loc. No parameter-domain boundary regularity is needed.
4. **Linearity and quantitative target stability (2 points).** Derive linear dependence on f from the full variational equation and its uniqueness. Test legitimately with the minimizer, use kernel positivity and weighted Cauchy-Schwarz, and prove both weighted-L2 and gradient bounds, including the corresponding difference estimates with the stated 1/alpha and 1/sqrt(alpha beta) scaling. The constant must be independent of alpha, beta, and the targets. Handle zero norms without division by zero, explicitly or by an argument that already includes them.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its auxiliary constants. Treat omission of either stability norm, the uniqueness argument, or the regularity bootstrap as a theorem-critical gap; do not award full credit for merely naming elliptic regularity or convexity without applying it to the stated objects.

The full variational equation follows directly by differentiating along every direction in W. It is not justified merely by extending a compactly supported distributional identity through an unproved density assertion. Likewise, the distributional equation without boundary information is not by itself a uniqueness characterization of the minimizer. Accept other valid arguments that establish the required full variational identities.

Do not require a boundary condition, positivity or mass normalization of the density, boundedness of Omega, or a smooth boundary. Such additions change the stated problem. Empty Omega, zero-measure D, and zero targets are permitted; a proof that covers them through its general argument need not discuss them separately.
