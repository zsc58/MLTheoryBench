# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Constructs a valid `C^2` lower-bounded objective with the needed derivative plateau and a globally bounded derivative. Establishes both upper and lower numerical bounds for `L` relative to `mu/R` and for `Delta` relative to `mu R`, and hence the product comparison. A suitable cutoff must have the range and regularity actually used in the argument; merely imposing its endpoint values is insufficient.
2. **2 points:** Defines a valid oracle with fresh noise independent of the prior history, proves conditional unbiasedness and the bound `E[|xi_t|^p | H_(t-1)]<=2sigma^p`, and obtains the correct exponential representations of the accumulators. The same function and oracle must serve every horizon in the assertion.
3. **4 points:** Proves the required self-normalization estimate. This includes the deterministic normalized-update bound and its zero-denominator case; compatible universal choices ensuring a recent outlier occurs with probability at least `1-delta`; a uniform lower bound on the retained denominator contribution despite the ceiling in `K`; and a valid first-moment bound for the noise numerator of order `sigma rho_1^((p-1)/p)`. A precise standard independent martingale moment inequality may be invoked with its relevant statement and hypotheses checked, or it may be proved directly. Combines the event and complement estimates without assuming independence between the numerator and the recent-outlier event, and obtains the exact parameter powers appearing in the task.
4. **2 points:** Uses the public displacement condition to obtain `sum_(t=1)^T alpha_t E[u_t^+]<=R/4`, or an equivalent adequate bound. Correctly uses deterministic nonnegative step sizes in the negative-part displacement estimate, applies Markov's inequality, and concludes the average expected gradient-magnitude bound for every admissible integer horizon.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's particular cutoff, numerical constants, auxiliary notation, or order of presentation.

The constants must have the independence specified in the public task. The reference proof demonstrates that they can be chosen uniformly in `p`, despite the notation `C_p`.

The assertion is existential in the objective and oracle; it does not require the conclusion for every unbiased oracle. Finite `p`-th moment does not mean that the constructed oracle must have infinite variance. It is valid to choose a bounded two-point noise law for each fixed parameter instance.

Do not demand a result for negative, random, or data-dependent step sizes, or for memory parameters outside the explicit public domains. Conversely, a proof may not introduce an additional restriction within the stated domains. Check `beta_1=0`, zero step sizes, `rho_2=1/2`, `q=1/2`, and `M=2mu` when applicable. A nonzero numerator over a zero denominator cannot occur under the verified accumulator representation.

The recent-outlier event and the numerator are generally dependent. An unconditional moment bound cannot simply be asserted after conditioning on that event; an indicator decomposition with a pathwise denominator bound is sufficient.

All reference-proof obligations are closed. No rubric credit presupposes an unproved paper-specific or specialized dependency.
