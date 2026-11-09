# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives and verifies the KL-prior optimizer, including normalization, existence and uniqueness on the support simplex, zero prior coordinates, and boundary conventions. A valid convexity argument or direct global objective comparison is acceptable; stationarity must identify a genuine global minimizer.
- **3 points:** Proves the multiplicative inequalities for every score vector and every coordinate, including zero prior coordinates, and obtains pointwise convergence with L, tau, and pi fixed as omega tends to zero.
- **1 point:** Proves the Euclidean value-perturbation inequality with attention weights held fixed. The inequality applies to arbitrary scores, not only in the low-signal limit.
- **2 points:** Computes the fixed-length uniform-prior limiting sensitivity as (L-1)/L and then takes the subsequent length limit. Does not claim exact uniform attention at an arbitrary positive content range or require a strict sink margin in the uniform case.
- **2 points:** Derives the positive prior-margin bound for the limiting sensitivity and proves that delta_L>=log L+b with b independent of L keeps that limit uniformly bounded away from one. A correct length-independent bound, or an equivalent argument establishing positive separation from one, is required.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices, score-shifting method, or particular global-optimality verification. Equivalent rescaling of scores, temperature, or margin is acceptable when used consistently.

The low-signal limits hold at fixed finite L and fixed prior. The length limit in the uniform case follows the low-signal limit. Distinguish limiting identities from finite-positive-signal assertions.

The sensitivity comparisons assume a positive periodic weight function with a period T>L. A period need not be the least positive period, and the prior and period may vary with L. No periodic-function calculation is necessary: a proof that establishes the stated inequalities for all positive finite priors also proves them for the stipulated subclass.

Merely observing Psi(C)<=1 does not establish the logarithmic-margin consequence. Do not demand necessity of logarithmic growth, a claim that every positive multiple of log L suffices, or a bound tending to zero for every fixed b. No optimizer formula or proof technique is required to appear in a prescribed form.
