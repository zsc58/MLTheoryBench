# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Define the population and subsample fairness gaps and derive the max/absolute-value reduction to the sum of the two sensitive-group uniform empirical deviations.
- **3 points:** Establish a uniform parameter-Lipschitz bound for every Gaussian-mixture responsibility on the regular class, controlling score derivatives using the weight, mean, covariance, and bounded-data assumptions.
- **3 points:** Derive the groupwise empirical-process rate by combining the bounded-loss Rademacher inequality with the Lipschitz parametric covering-number and Dudley estimate, obtaining the C sqrt(d/m) term rather than merely naming concentration.
- **2 points:** Combine the two groups with the stated confidence allocation and substitute n'=min(n_1,n_2) to obtain the displayed bound uniformly over the parameter class.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of the responsibility-Lipschitz derivation or the entropy/Rademacher calculation as a theorem-critical gap. A correct proof using equivalent empirical-process tools receives full credit when it verifies the same hypotheses and rate.
