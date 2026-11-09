# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives the one-dimensional exponential-moment recursion and logarithmic upper bound for 0<c<=1/4, including conditioning, the first-round base bound, and zero-covariate cases.
- **2 points:** Supplies a valid dyadic one-dimensional block construction and proves an Omega(log T) expected lower bound with constant-probability success. Check that its successful-block indexing agrees with X_1 and that any incomplete final block is defined.
- **3 points:** Gives the adaptive d>=2 covariance-preconditioned orthogonal construction and verifies, for the stated information timing, that regularized self-normalized energy gains r^2/(1+r^2) per round and transfers to the unregularized ratio.
- **1 point:** Proves the elementary upper bound R_T<=T and combines the bounds into the sharp dimension dichotomy.
- **2 points:** Defines and uses the stated prediction timing to derive the expected-regret lower bound for every learner, including the comparator-square identity and, for the bounded-covariate assertion, common rescaling of the finite tree.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Do not award the regret points solely for asserting that linear self-normalization implies linear regret; the required stochastic-environment reduction must be justified. An explicitly and harmlessly handled zero covariate or incomplete block is sufficient regardless of notation.
