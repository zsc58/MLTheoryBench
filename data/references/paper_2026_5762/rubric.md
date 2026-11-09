# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: Stabilization.** Proves a valid deterministic discrepancy bound for the sampling rule that includes the current target mass. Uses forced exploration and adaptive concentration to establish consistency of the constrained MLE, and deduces stabilization of the estimated top set and oriented inversion constraints from the positive gap. The one-edge case must be covered, either explicitly or by the argument.
- **4 points: Information-rate tracking.** Establishes the boundary-pair game properties and carries out the substantive stochastic two-player argument: valid bounded unbiased first-order estimates, regret bounds despite the initially changing boundary, regret-to-gap conversion, parameter-estimation transfer with fixed constraint sets, and transfer to empirical frequencies. It must conclude that the empirical information rate approaches the oracle value with sufficient probability control for the later expectation argument. Merely naming online learning, a minimax theorem, or the source's oracle-rate assertion is insufficient.
- **2 points: Fixed-confidence validity.** Proves the erroneous-stop probability bound and almost-sure finite stopping. For the mixture route, justifies likelihood ratios over the full centered subspace, the Gaussian integral bound using global curvature, and the implication from an erroneous GLR stop to a martingale crossing. Establishes the normalized GLR comparison and positivity of the limiting rate, then compares it with logarithmic threshold growth.
- **2 points: Expected-time optimality.** Derives a summable tail bound beyond a deterministic time asymptotic to log(1/delta) divided by the oracle rate, sums that tail, and proves the matching lower bound. The lower-bound application must use correctness at alternative parameters and justify the closed inversion-alternative formulation, or provide an equivalent valid argument.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or an explicit minimax interchange when the required game inequalities are proved directly.

The dual scores are stored on unordered comparison edges. Opposite estimated orientations do not have separate cumulative memories. A proof must analyze the procedure actually stated.

A fixed-simplex exponential-weights bound cannot simply be applied to the changing dual domain. The reference proof uses a shadow sequence on the true boundary, preserving all accumulated scores and charging the initial segment. An equivalent valid treatment is acceptable.

Do not condition score-noise concentration on a future stabilization event without justification. Predictable masking, a suitable stopped construction, or another valid unconditional argument suffices.

Non-stopping is a strict threshold-failure event. A good event establishing a non-strict lower bound excludes that strict failure event; it need not exclude equality with the comparison level.

Almost-sure rate convergence alone does not establish the expectation asymptotic. A summable tail estimate or another valid uniform-integrability argument is required. A missing oracle-tracking derivation remains a theorem-critical gap. The reference proof contains no unresolved proof obligation.
