# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly rewrites the update as a linear stochastic recursion and establishes the symmetric-part, operator-moment, and residual-covariance bounds. Uses stationarity of both state marginals and the feature normalization correctly. Does not confuse the symmetric part of the mean matrix with the generally nonsymmetric mean matrix itself.
- **2 points:** Derives a valid averaged-recursion bias/variance inequality with the stated step-size denominators and a precisely defined, correctly normalized finite power sum. The proof must account for multiplicative stochastic noise. Either the source's orthogonal centered-order expansion or a fully justified combined martingale-innovation calculation is acceptable; unjustified independent-additive-noise treatment is not.
- **4 points:** Proves a smallest-eigenvalue-free finite-power-sum bound sufficient to obtain de(1+epsilon)/(1-gamma)^2 with the exact advertised correction. A resolvent proof must justify its series/integral representation, retain the squared Frobenius norm, verify convergence, and control all integration regions. A real-right-hand-side estimate may be used columnwise but must not be silently promoted to an unrestricted complex operator estimate. The source's incorrect unsquared substitution on the final arc is not an acceptable proof; a valid integrated estimate, or an equally strong alternative argument, is required.
- **1 point:** Substitutes the estimates and simplifies to the exact advertised upper bound, respecting all parameter restrictions, k=1, gamma=0, and sigma=0, and establishing the absence of an explicit omega-dependent factor.
- **1 point:** Gives an admissible fixed instance for every specified d, omega, positive sigma, and deterministic initialization; verifies its assumptions; and derives scalar-recursion estimates establishing the factor-11 comparison along every stated limit with lambda fixed. A Jensen lower bound for the bias is sufficient. The noise calculation must retain the dimension factor, and the comparison coefficients must be valid rather than rounded downward.

# Evaluator Notes

Accept a complete valid alternative proof and do not require the reference proof's incidental presentation choices. The weights total ten points. The central four points assess an actually derived estimate, not recognition or citation of a specialized method. Naming a generic stability theorem or Kreiss/resolvent analysis does not close that obligation.

The lower bound is E/11, not 11E. Rewards need uniformly bounded conditional second moments, not bounded support; Gaussian rewards in a verified construction are admissible. The lower clause uses a positive noise scale, so its ratio is defined. The upper clause continues to allow zero noise. No mixing, irreducibility, reversibility, or conditional independence between a reward and its next state may be imposed without justification.

The reference proof includes local repairs of source errors. Do not penalize an answer for rejecting an erroneous source intermediate estimate, using the symmetric-part definition required by the matrix order, or using the correct equal-index integral identity. Conversely, copying those source errors does not establish a proof step. The repaired reference proof has no outstanding theorem-critical proof obligations.
