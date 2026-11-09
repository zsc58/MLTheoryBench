# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Quadratic reduction and unconstrained projection (2 points).** Correctly relate the distance objective to the quadratic objective and derive the unique zero-mean minimizer `(g-E[g])/mu` using Hilbert-space projection or an equivalent direct argument.
2. **Bounded projection characterization (2 points).** Account for the lower bound `v>=-1` together with the shared mean constraint and justify the clipped form by scalar minimization, derived stationarity/KKT conditions, or an equivalent variational argument, rather than merely naming KKT.
3. **Chemical-potential normalization and optimality (4 points).** Establish existence and uniqueness of `lambda*` solving the mean equation and prove that the resulting clipped function is the unique global minimizer over `K`. Cover the countably infinite case by justifying the necessary integrability, any exchange of limit and expectation, and square integrability of the candidate. Equivalent variational proofs are acceptable.
4. **Probability validity and exact sparsity (2 points).** Show the update is a normalized nonnegative policy and prove that every action with `g<lambda*-mu` receives exactly zero mass.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its particular dominating bounds, or a KKT argument when direct optimality is established. A proof working directly with squared distances need not separately introduce the work-dissipation functional. Treat failure to establish the normalized multiplier or the global bounded optimality argument as a theorem-critical gap. Distinguish such gaps from readily repairable omissions of routine integrability estimates. Do not accept a finite-dimensional argument alone when it leaves the countably infinite case unresolved.
