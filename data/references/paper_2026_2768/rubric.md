# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Uses the finite candidate set, finite horizon, and history-specific polyhedral partitions to represent the trajectory event; combines it with the target event and proves that intersection with the affine slice is a finite union of intervals. Gives an exact finite linear-constraint procedure, including strict/weak boundary assignments, empty intersections, unbounded intervals, and zero-coefficient constraints.
- **3 points:** Correctly handles the adaptive observation experiment. Derives its sequential product density and identifies its restriction to a fixed trajectory-and-weight stratum with the restriction of a fixed-trajectory Gaussian reference density, or supplies an equivalent valid argument. Derives the fixed-weight residual and affine representation, and proves independence of the statistic and residual under that reference law. Does not assume that the adaptive response vector is unconditionally Gaussian.
- **3 points:** Uses the reference-density restriction to derive the actual conditional truncated-normal law and its dependence on the objective only through the selected effect. Justifies almost-sure positivity of the normalizer and the almost-sure conditioning interpretation. Establishes composite-null validity using a proved stochastic-ordering argument, or a correctly stated standard ordering result with verified hypotheses, together with boundary probability-integral-transform calibration. Handles disconnected truncation sets without assuming their CDF is strictly increasing everywhere.
- **2 points:** Gives the finite-sum normal-CDF formula or an equivalent exact procedure for the selective tail probability. Integrates the conditional inequality with the indicator of the selected-null event to obtain the stated joint bound, its conditional-on-null interpretation when that event has positive probability, and the ordinary marginal bound when the selected null holds almost surely.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not award credit for merely naming selective inference, conditioning, or polyhedral methods without carrying out the corresponding derivations.

The distinction between the actual adaptive experiment and the fixed-trajectory Gaussian reference law is theorem-critical. A proof that simply declares Y jointly Gaussian with a fixed unconditional mean has not proved the public task. Independence of a fixed-weight statistic and residual is established before restricting the Gaussian reference law to selection; unconditional independence for a randomly selected weight must not be assumed.

The residual may have a singular distribution, including a deterministic residual when N=1. A valid disintegration or coordinate argument is sufficient; an N-dimensional Lebesgue density for the residual is not required. Conditional distribution claims need only hold almost surely. The exceptional-input convention is not a substantive restriction on the model.

Exact set computation must account for the maps' assigned boundaries. Endpoint differences do not affect the normal-CDF integrals, but an argument that computes only one component or one internal selection cell does not establish equality with the full selection-consistent set.

A missing Gaussian-reference bridge, independence argument, or truncation argument is theorem-critical. A missing selected-null marginalization argument loses the final validity credit. Do not interpret the random selected null as automatically holding on every selection output. Do not demand confidence-interval results, randomized-selection results, or algorithm-specific GP-UCB/TPE calculations.
