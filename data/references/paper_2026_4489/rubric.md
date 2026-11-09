# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derives valid conditional moments and the variance decomposition, identifies policy dependence through E[g/pi], and relates the defined audit-induced component to E[g(1/pi-1)]. Justifies use of the one-summand variance in the fresh fixed-arm experiment.
- **3 points:** Solves the bounded mean-constrained functional minimization on the positive-residual stratum, deriving the clipped square-root propensity and proving global optimality by a pointwise convex/Lagrange argument or another correct method.
- **3 points:** Establishes existence of a budget-feasible optimizer, handles positive-measure zero-residual strata and saturation, and covers rho=pi_min, rho=1, pi_min=1, and g=0 almost surely. A normalizing constant need not be unique. Zero-stratum spending must be compatible with optimality, not just feasibility.
- **2 points:** Proves that uniform auditing need not be optimal and establishes the quantified arbitrary-gap claim for every fixed 0<pi_min<rho<1 using admissible bounded heterogeneous instances. Verifies the lower and upper propensity bounds, exact budget, a strictly positive optimal audit-induced component, and an unbounded ratio.

# Evaluator Notes

Accept any correct alternative proof. Do not require a particular tie-breaking rule on the zero-residual stratum; only the bounds, budget, and optimality matter. A proof that asserts a normalizing c without addressing a positive-measure zero-residual stratum has a theorem-critical gap. Do not require uniqueness of c, which can fail because of clipping.

The conditional variance of AR/pi given only (X,F) is g/pi-m^2, where m=E[Y-F|X,F]. The expression g(1/pi-1) describes the audit-induced contribution after the appropriate conditioning and averaging; it is not in general that conditional variance. Accept any valid derivation of the total variance objective.

A two-region comparison must respect Y,F in [0,1]. In particular, sending a residual second moment to infinity is not an admissible construction. If one region of probability q is audited with propensity one, the remaining propensity (rho-q)/(1-q) must also satisfy the lower bound; q<rho alone is insufficient. A suitable small q and a low-region residual second moment tending to zero suffice.

The arbitrary-gap claim concerns the explicitly defined audit-induced variance component and excludes endpoint budgets. Do not require an arbitrary-gap proof at rho=pi_min or rho=1, where the feasible policy is unique almost surely. A construction with constant Y also proves an arbitrary gap for total variance, but this additional observation is not required.

All listed obligations are established in the reference proof; there is no unresolved private ground-truth dependency.
