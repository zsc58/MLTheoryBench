# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps for the Reference Architecture

1. **2 points:** Use the policy-dependent discounted occupancy law to establish TD coercivity and the bounded-gradient estimates. Derive the critic norm recursion with squared KL forcing and the correct step-size range. A covariance bound under beta alone is not a substitute for occupancy weighting in g.
2. **3 points:** Derive the explicit mirror update using the old-policy log density. Couple its centered-log recursion with the critic bound to establish uniform policy KL and critic stability throughout the displayed h range. Keep the stability constant independent of h and lambda. An unsquared running-maximum proof is valid and avoids the source's faulty squaring.
3. **2 points:** Derive uniform Bellman and realizable-parameter bounds, consecutive-policy control, and moving-target critic-error control. For the reference rate calculation, show target increments of order lambda and average critic error bounded by a constant times 1/sqrt(nh)+lambda/h. A bounded log-partition variance calculation is one valid way to obtain consecutive-policy KL of order lambda squared. Do not credit the false bound D_n<=lambda||theta^{n+1}||/(1-tau lambda).
4. **2 points:** Establish the KL three-point relation and performance-difference identity, control signed-policy critic errors, and telescope against a fixed optimal occupancy law. Keep the initial value term integrated against that occupancy law, or replace it by a justified uniform upper bound. Include all residual contributions in the error coefficient. Convert a cumulative error sum to its average correctly.
5. **1 point:** Obtain one finite constant C valid simultaneously for all rho and n>=1 and all allowed h, with the stated dependence. Convert the averaged gap to the best-iterate gap and handle the initial terms and n=1.

# Evaluator Notes

Accept every complete valid alternative proof; the reference architecture is not mandatory. In particular, the task permits C to depend on lambda but not on h. If a proof first establishes uniform stability and then obtains the second inequality directly from a uniform value-gap bound using this allowed dependence, it can be fully correct and must not be penalized merely for avoiding moving-target or telescoping estimates. When scoring such a proof, allocate the remaining credit to verification of its value bound, uniform quantifiers, and constant dependence.

The admissible policy class requires uniformly bounded log densities, not merely bounded densities or finite statewise KL. The actor objective is linear in log p_n; an implicit new-policy entropy minimization defines a different algorithm. All critic residual integrals use d_beta^{pi^n}, while the covariance condition uses beta. Exact population integration is the experiment; no sampling or concentration argument is required.

Naming an external TD result or a specialized convergence method does not establish its hypotheses or close its proof obligations. Routine contraction, KL, Jensen, Cauchy-Schwarz, and geometric-series arguments may be used when their application is justified. If following the reference architecture, an omitted coupled-stability argument, unsupported target movement, or invalid performance telescope is theorem-critical. Apparent source identities that omit advantage-centering terms are not valid proof steps; those terms cancel only in the appropriate signed-policy integrals.
