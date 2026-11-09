# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: Concentration, optimism, and surplus.** Establishes a correctly calibrated transition event for realized contexts and completed batches, proves optimism, and derives a local-variance surplus bound with current-stage and propagated inverse-count contributions. Checks the information dependence of adaptive continuation values. A specialized monotonicity assertion must be proved or obtained from a valid independent result with its relevant statement and hypotheses supplied. Merely citing a named method or replacing the public bonus coefficients by unsupported smaller coefficients does not close this step. Profile concentration is not mandatory. In the reference route, using H^{-2} in Young's inequality yields a current count coefficient of order SH^2 Lambda and a future coefficient of order SH Lambda.

- **3 points: Clipped regret decomposition and p-tail control.** Uses a variance- and gamma_min^p-dependent clipping threshold; establishes the required variance budget, including its H^2 bound and zero-variance interpretation; proves the clipping comparison and first-suboptimal-action decomposition; and obtains the tail term of order (pK+1)SAH gamma_min^p Lambda by conditioning before the fresh context is drawn. Covers admissible zero-gap occurrences outside Z_pos on the trimmed side. Correctly converts the current and expected future surplus contributions into clipped envelopes, controlling the total amount discarded.

- **2 points: Filtered visitation integration and the exact burn-in logarithm.** Proves or correctly applies a predictable weighted-count estimate for retained and trimmed context filters. Accounts for the fact that the cached denominator is a completed-batch sample size, only comparable within a constant factor to cumulative prior visits. Obtains the retained square-root estimate, the trimmed term of order |Z_trim^p| W Lambda log(eH)/gamma_min^p, and the burn-in term with the public logarithm. The reference proof separately integrates direct and future count envelopes to obtain C S^2 A H^3 Lambda ell(H^3/gamma_min^p), then uses the remaining factor H to obtain the public H^4 bound. Handles zero variance, empty integral intervals, and H=1. Assuming cached counts dominate cumulative filtered counts is invalid.

- **3 points: Gap charging and self-bounding closure.** Charges retained counts using the local gaps gamma_h^p(s,a), compares realized gap sums with regret using a valid adapted concentration argument, and applies Cauchy-Schwarz to a consistently defined retained square-root quantity. Solves the resulting quadratic with consistent universal coefficients. Combines all terms and optimizes over a sample-path-independent p without replacing local gaps by gamma_min^p in the local sum.

# Evaluator Notes

Accept any complete proof under the public assumptions, including different universal constants and logarithmic expressions demonstrably bounded by universal multiples of the displayed total bound. Do not require inconsistent exact numerical constants from the source.

The reference architecture uses retained/trimmed contextual decomposition and self-bounding, but a different complete argument proving the stated bound is acceptable. No credit is conditional on citing the paper, a theorem number, or the profile-concentration method. Separating the two count envelopes is a sufficient reference repair, not a mandatory proof format.

The comparison log(CSAH^5/d)<=C ell(SAH Lambda/d), with d=gamma_min^p, is false under the public assumptions. In particular, d proportional to H and K polynomial in H can make its two sides have orders log H and log log H. A proof using the old combined count envelope cannot obtain full credit for the precise burn-in term merely by asserting this comparison, invoking unspecified equivalent logarithms, or increasing a universal constant. A valid alternative must derive the displayed total bound, for example by saving a polynomial factor before absorbing the extra logarithm.

Check that the variance quantity used is the public full-trajectory conditional complexity. Private envelope suprema may be restricted to reachable context/triple combinations because unreachable combinations contribute neither occupancy nor visits. Using an unrestricted supremum and asserting it is bounded by the conditional complexity needs justification.

Do not award full downstream closure when the clipped-envelope conversion, completed-batch counting, burn-in estimate, retained-count inequality, or lower-tail conditioning remains unsupported. The proof must address W=0, arbitrary positive integer K, and the deterministic-p infimum passage. Empty Z_pos makes the public bound vacuous by its explicit convention.
