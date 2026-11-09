# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Establishes well-definedness of the quantities used: measurable positive generalized means and positive finite normalizers for the universal guarantee and the constructed counterexamples. A proof of `0<Z_{k,r}<=k` for all orders is sufficient, but the incidental all-order bound is not mandatory if every normalizer needed for the requested claims is justified. The supplied definitions need not be copied.
2. **3 points:** Proves `Z_{k,r}<=1` for every order in `[0,1]` and derives the pointwise log-likelihood guarantee for every permitted collection and point using a valid Jensen or equivalent argument, including `r=0`. The stronger normalizer bound for every `r<=1` is also valid.
3. **3 points:** Constructs and verifies a genuine normalized violation for every fixed finite `r<0`, and handles `r=-infinity`. Normalization must be controlled rather than assumed away. For the separated Gaussian construction, a lower bound on the normalizer combined with a sufficiently negative unnormalized deficit closes this step; an upper bound on the normalizer does not establish the required upper bound on the normalized density.
4. **2 points:** Constructs and verifies a violation for every `r>1`, including `r=+infinity`. The reference method uses a consensus point and a justified strict-normalizer argument; complete valid alternatives receive full credit.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, Gaussian constructions, or asymptotic notation. The counterexample domain is existential, so finite discrete domains are permitted. Counterexamples and their parameters may depend on the fixed order. A solver must establish the counterexamples and normalization estimates; merely naming Jensen, Gaussian separation, or power-mean monotonicity is insufficient. Do not accept an unnormalized violation as a normalized one without the needed argument. Routine positivity and measurability facts may be stated succinctly. All requested endpoints and extended orders must be covered for full credit.
