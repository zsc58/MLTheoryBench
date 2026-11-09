# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the SO(2) feature action and the M-fold angles and direct aggregate. Any discussion of complex-linear equivariance respects the same-order restriction.
- **3 points:** Evaluates the finite Fourier sum and concludes that all retained positive orders below M vanish while order zero is constant.
- **2 points:** Explains why products, conjugates, fixed linear combinations, and fixed order-zero gates depending only on the retained aggregates remain orientation-independent after aggregation.
- **3 points:** For a given retained pair whose orders sum to M, forms the product on each edge before aggregation, computes M exp(i M phi), and establishes both nonconstancy in phi and the order-M rotation law.

# Evaluator Notes

Accept any complete valid alternative proof. Do not award credit merely for naming a method.

The order-zero aggregate is M, not zero. The post-aggregation conclusion is orientation-independence, not universal vanishing of scalar outputs. Gates use only the retained aggregated inputs and fixed rules; no separate orientation input is permitted by their definition.

The edge claim is conditional on a retained pair summing to M. Do not require a solver to prove that such a pair exists for every m_max<M, and do not require distinct input orders. The direct claim includes m_max=0. The output harmonic of order M is allowed by the stated edge construction even though the retained input orders are below M.

Orientation-sensitive means nonconstant as phi varies; it does not mean injective on all real angles or changed by every nonzero rotation. The specified inputs are unit complex exponentials. A solver need not prove nonzero output for arbitrary learnable weights.

A full-credit proof must justify the rotation law as well as the aggregate formula. There is no required appeal to a generalized contraction algorithm, specialized external theorem, or particular architecture implementation.
