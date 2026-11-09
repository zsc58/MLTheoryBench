# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly proves that zero discrepancy forces equality of all one-dimensional projection laws. An increment proof must retain the tail contribution, account for the common baseline, use admissible shifts, and handle continuity points, atoms, and bounded-support endpoints. Other valid separation arguments receive equal credit.
- **2 points:** Uses projection/characteristic-function uniqueness to conclude D(P,Q)=0 if and only if P=Q, including the converse.
- **4 points:** Establishes the uniform empirical-population error bound with the required dimension dependence and probability exponent. In the reference route, this includes a centered empirical-process supremum dominating the error; the bounded envelope and coordinate sensitivities; a product-cover entropy estimate with controlled dimension dependence; valid absolute Rademacher symmetrization and entropy integration; and bounded-differences concentration. Measurability must be justified or follow from a clearly applicable separability argument. Equivalent valid methods are accepted.
- **2 points:** Under a fixed alternative with equal sample sizes, combines positive population discrepancy, the deterministic vanishing threshold, and a valid estimation bound to prove the eventual power rate and consistency, respecting the stated constant dependencies.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, an exact covering exponent, or its numerical constants when an alternative argument implies every requested bound.

The empirical IPM itself generally has a nonzero limiting expectation under an alternative. A claim that its expectation is O(n^(-1/2)+m^(-1/2)) without centering is incorrect and does not establish the estimation or power steps. Bounding the centered empirical process, the actual absolute estimation error, or another valid dominating quantity is necessary.

An entropy estimate with an arbitrary dimension-dependent prefactor does not by itself establish c_d=O(sqrt(d)); its logarithm must be controlled appropriately, or another valid complexity estimate must provide the required rate. Absolute suprema require an appropriate Rademacher convention, signed enlargement, or equivalent argument. Outer expectations on conditional complexities must not be silently dropped unless a deterministic sample-uniform bound is used.

For the power step, Markov's inequality requires an expectation estimate, not merely an unintegrated high-probability assertion. Direct use of the estimation tail is also valid and gives an eventually exponential type-II bound. The coefficient 4c_d/D(P,Q) naturally depends on the fixed slope interval through D; the stronger exponential bound permits a universal eventual coefficient such as c_3=1, with the onset depending on the fixed interval and threshold sequence.

No Type-I error guarantee, permutation-threshold theorem, numerical optimization guarantee, null limit theorem, or local-alternative result is requested. Do not require these. Treat omitted technical constants as minor only when the stated rate, dimension dependence, and probability mode remain established. Failure to prove separation or a valid centered estimation bound is theorem-critical.
