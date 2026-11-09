# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly identifies the iid/kernel learning experiment, centered generalization process, minimum covering radius, separate entropy integral, and radius-based nested partitions. Treats the zero-radius singleton case and keeps representatives and partitions fixed independently of the realized data. Does not replace the covering radius by the entropy integral or impose an unrequested singleton initial partition.
- **3 points:** Telescopes the original representative sequence at finite depth and derives a valid per-scale shifted-log-information bound under the joint cell/sample law versus its product law. Verifies that the child cell determines the parent representative, conditions under the product law before invoking independence, and uses the correct normalization. Handles the first increment using an admissible deterministic anchor, including possible nonattainment of the minimum covering radius. An approximate-radius anchor followed by a limit is acceptable.
- **2 points:** Establishes the independent centered-sum control with a constant depending only on theta, uniformly in the scale and sample size. A complete truncated-moment proof or the elementary full-exponential moment proof is acceptable. Derives the change-of-measure estimate used, or invokes a genuinely standard independent result with its exact statement and checked hypotheses. Explains how the theta-only constant gives the requested information coefficient and additive 4. Merely naming a specialized sub-Weibull sum inequality or a paper-specific decorrelation lemma does not complete this step.
- **2 points:** Sums the finite-depth bounds, uses the zero-mean deterministic baseline, preserves the factor e M_theta/sqrt(n) and the geometric weights, and removes any approximate-anchor error. Does not assume that an arbitrary finite-valued learner is eventually reproduced by prescribed partitions of a larger hypothesis space. The geometric weights sum to 2.
- **1 point:** Justifies the general learner limit using a common-event regularity argument and an integrable envelope. In particular, metric convergence and separability alone are not a complete justification for convergence along the prescribed representatives; deriving uniform continuity from the entropy and increment assumptions is sufficient. Handles the nonnegative series by a valid limit argument and states finiteness only under weighted-series summability, not merely finiteness of each scale's information.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental constants, net choices, or presentation. The task quantifies an existential theta-only M_theta; a particular numerical appendix formula is not required. Its dependence must not include n, A, the metric space, the learner, the loss distribution, or the partitions.

The partitions satisfy a radius-cover condition. Representatives are not assumed to belong to their own cells, although child representatives belong to parent cells. The initial partition is not required to have a single cell, and the minimum covering radius need not be attained.

The source's unrestricted auxiliary change-of-measure claims for A>=1 and its uniform-in-A additive Renyi comparison are not accepted as black-box proof obligations. The public large-shift regime remains unchanged, and the reference proof gives an independent elementary derivation sufficient for it. Renyi refinements are not requested and carry no additional credit.

A finite-valued cell variable has finite shifted-log information at each fixed scale, but arbitrarily rapid refinement can make the weighted series diverge. Do not award a finiteness conclusion based only on discreteness or scale-by-scale finiteness. Infinite ordinary mutual information does not invalidate a bound expressed through a convergent quantized-information series.

All theorem-critical obligations in the replacement reference proof are explicitly closed; there is no private GT quality warning.
