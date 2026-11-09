# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes simultaneous degree and comparison-noise controls, obtains positive stationary-equation denominators on the good event, and derives the direct coordinate bound for the auxiliary vector. Treats n-1 versus n correctly and bounds, rather than equates, incoming and outgoing comparison sums.
- **2 points:** Establishes global perturbation control sufficient for the final theorem, with correct norm geometry and probability bookkeeping. The reference proof derives a reciprocal stationary-weight row-norm perturbation inequality, verifies empirical transition concentration, and separately proves the logarithm-free relative l2 bound. Operator concentration alone is not a proof of that sharper vector bound. A weaker global estimate is acceptable if the submitted complete argument shows it suffices for the requested entrywise rate.
- **3 points:** Constructs and correctly exploits a leave-one-out stationary vector independent of all incident observations; uses a valid normalization or generator formulation; defines every auxiliary coordinate used in a norm; gives the exact coordinate decomposition; and controls heterogeneous conditional means and centered fluctuations using the rowwise variation condition and coefficient-aware concentration.
- **3 points:** Controls the full/leave-one-out displacement through the graph/comparison split or an equivalent valid argument, retaining actual heterogeneous sampling probabilities and actual comparison coefficients. Derives and absorbs the final self-bounding inequality with c0 depending only on h,gamma, c1,c2 depending only on h,s, and total failure O(n^-5).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental normalization, numerical constants, auxiliary notation, stronger intermediate estimates, or presentation choices.

A named perturbation, leave-one-out, concentration, or ranking result earns credit only when its relevant statement is supplied and its hypotheses are checked, or the needed result is derived. The reference proof now supplies derivations for its specialized perturbation and transition-concentration applications.

For row probability vectors, do not silently use reversible spectral contraction in the norm sqrt(sum_i r_i u_i^2). The reciprocal-weight norm sqrt(sum_i u_i^2/r_i), or an explicitly justified equivalent formulation with appropriate constants, is valid.

Do not treat incident graph indicators as independent after conditioning on the spectral-gap event. A valid approach constructs concentration events under appropriate product-law conditioning and then intersects with the gap event or bounds conditional failure by division by its probability.

Do not accept factoring nonconstant coefficients out of an absolute centered sum. Apply concentration to the coefficient-weighted sum itself. An absent-edge coefficient is a_ij, not its lower bound rho.

Do not require positivity or uniqueness of the empirical stationary distribution on every possible observation outcome. The estimator is already totalized in the public task; uniqueness and denominator positivity on the high-probability event suffice.

The reference proof has no unresolved proof obligation. Its corrected source-local steps are not extra public assumptions and must not be demanded as assumptions from a solver.
