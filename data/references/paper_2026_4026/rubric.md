# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes isotropy of the Gaussian TT probe and unbiasedness of its quadratic-form trace estimate, using the core independence and normalization or an equally rigorous argument. Centering may also be established but is not a separate requirement for full credit.
- **4 points:** Derives a sufficient TT-specific fourth-moment or quadratic-form variance estimate. For the reference route, demonstrates the Gaussian Frobenius fourth-moment inequality and a valid conditional interface recursion, including its base case, norm-preserving reshaping, independence of the fresh core, and accumulation of the factor (1+2/r)^(d-1). A proof for every integer p>=1 is welcome but not required. Merely naming a paper-specific moment lemma without establishing the necessary result does not close this obligation.
- **2 points:** Obtains a variance bound sufficient for the stated block size, such as Var(omega^T A omega)<=22 tr(A)^2 under r>=d-1, then uses independence and Chebyshev's inequality to show that ell>=88 epsilon^(-2) gives block failure probability at most 1/4. With the directional-moment route, handles PSD factorization and cross terms correctly, including zero columns.
- **2 points:** Proves the median guarantee for arbitrary admissible positive integer k, including the permitted even-k median selections. Uses independent blocks and a valid tail estimate to obtain failure probability at most delta for k>=7 log(1/delta). For the complexity consequence, chooses ceiling-sized k and ell, accounts for integer rounding over 0<delta<1, and recovers O(epsilon^(-2)log(1/delta)) as delta tends to zero with constants independent of tensor order.

# Evaluator Notes

Accept any complete valid alternative proof and allocate credit for equivalent accomplishments. Neither all higher even moments nor the reference proof's particular interface notation or recursion is mandatory if another rigorous argument establishes the public claim with its constants. Do not deduct points for omitting centering when isotropy and unbiasedness have been correctly proved.

Any measurable median selection between the two central order statistics is allowed for even k. A proof must cover the stated median convention, not silently assume k is odd. The block-failure probability may be zero; a fixed exponential parameter avoids division by that probability.

The sample-count conclusion is a sufficient-budget statement for the specified ceiling choices, not an upper bound for every k and ell satisfying only lower bounds. The uniform rounded form is O(epsilon^(-2)(1+log(1/delta))); the logarithmic form holds as delta tends to zero. Do not require or reward a false uniform O(epsilon^(-2)log(1/delta)) upper bound as delta approaches one.

All reference-proof obligations are closed. No external specialized theorem is supplied as a substitute for the TT-specific moment argument.
