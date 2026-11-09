# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly handles the robust objective, compact active model sets, objective subgradients, and normalized discounted occupancy. Establishes the full-support occupancy ratio bound. Uses the objective's ambient subdifferential, not the subdifferential after adding the policy constraint indicator. Correctly justifies the active-gradient convex-hull formula, including its application to compact, potentially infinite uncertainty sets.
2. **4 points:** Proves subgradient dominance under both globally quantified alternatives. The argument must control every convex combination of active gradients, not just gradients of individual worst-case models. In the common-transition branch, combine advantages before taking their nonnegative statewise maximum. In the common-Q branch, factor common advantages while retaining the mixture of occupancies. Justify occupancy comparison after obtaining nonnegative terms, identify the directional gap, and take the minimum over subgradients. Merely naming performance difference, occupancy ratios, or Danskin's theorem earns little credit.
3. **2 points:** Establishes bounded objective subgradients and weak convexity with the required constants, then proves a sufficient objective-gap bound through proximal optimality or a valid alternative. For the reference route, apply dominance at the proximal point and use ||pi-prox||=||grad M||/(2ell), giving D'=2D sqrt(|S|)+sqrt(|A|)/[2ell(1-gamma)^2]. The source's reciprocal scaling error must not be used.
4. **2 points:** Proves or correctly applies a stationarity estimate for the actual schedule eta=1/sqrt(T), with constants sufficient for the displayed C. A sufficient explicit estimate is min_t ||grad M||^2 <= 2Delta/(eta T)+2ell eta L^2, where Delta<=1/(1-gamma) and L=sqrt(|A|)/(1-gamma)^2. Combines this with objective-gap control to obtain the stated T^(-1/4) bound and the O(epsilon^(-4)) best-iterate update complexity.

# Evaluator Notes

Accept a complete valid alternative proof and any stronger estimate implying the stated bound. Do not require the reference proof's incidental presentation choices or a particular citation. Do not award closure of a convergence step merely for naming a specialized theorem without stating a sufficient bound and checking its schedule, constants, and hypotheses.

Omission of either uniqueness branch, failure to handle arbitrary subgradient convex combinations, or omission of the explicit convergence/complexity conclusion is a major gap. Selecting a single active model does not by itself establish the minimum-over-subgradients claim. Replacing eta by 1/(ell sqrt(T)) while retaining the stated constant does not prove the task.

The public statement uses either global transition uniqueness or global Q uniqueness. A proof establishing the stronger pointwise-disjunction version is acceptable. Clarke and Frechet subgradients agree for the specified local Bellman extension; no distinction needs to be manufactured between them. The one-action case has zero policy gap and is included. The task concerns exact-subgradient update complexity, not an unstated polynomial-time implementation of a worst-case-model oracle.
