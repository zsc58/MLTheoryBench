# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Constructs cellwise degree-s-1 approximants with W^{r,infinity} error O(K^{r-s}), verifies the averaging-ball geometry and uniform coefficient bounds, and correctly distinguishes cellwise norms from global weak derivatives. Uses extension where shifted targets or the final rescaling require it.
- **3 points:** Establishes fixed-architecture encoding and evaluation of arbitrarily large coefficient tables. Justifies the finite-table density mechanism, realizes the addressing and readout maps with the given activation, verifies the domains of exact square and multiplication identities, and controls derivatives of the coefficient error on active cells. Handles the constant monomial without incorrectly charging a generic multiplier to the smallest width budget.
- **3 points:** Builds the shifted smooth partition of unity, verifies localization on the approximation subcube with a sufficiently large grid parameter, and bounds gate derivatives through the finite order s-1. Applies the weak Leibniz rule to obtain an O(K^{-1}) error. Establishes that the constructed global network realizes the products on the entire approximation domain, not merely where the local error estimates hold.
- **1 point:** Tracks the exact stated width and depth through composition, identity padding, and parallelization; normalizes shifted targets and their tolerances; and performs extension and affine rescaling for arbitrary cubes and target norms, including the zero target.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular proof of torus density. A correctly stated, applicable standard mathematical theorem may justify a solver's density argument; merely naming a specialized mechanism or asserting arbitrary table encoding does not establish it.

A gluing argument that ignores derivatives of the gates or does not justify localization cannot establish the third core step. It must also distinguish genuine global Sobolev derivatives from the cellwise estimates used earlier.

For n=infinity, constants may depend on the finite derivative cutoff. Do not require or reward an order-independent bound for every derivative of the smooth gate. Constants and weights may depend on the fixed n, target, cube, and tolerance; the specified width and depth may not grow with the tolerance.

Exact multipliers are only guaranteed on prescribed bounded boxes. For the final products, a bound on the complete compact-domain input range is sufficient and may depend on the constructed local networks. No uniform bound outside the active cells is necessary.

The degree-zero case and s=1 are part of the task. A correct constant branch can bypass monomial evaluation and multiplication. Minor omissions that are genuinely routine may fall in the 8-9 range, but a resource count that cannot fit the stated architecture is not a complete proof.

The source uses an ell-infinity ball for the equality with a grid rectangle. There is no Euclidean-ball-versus-cube source error to identify. A correct proof should use the smaller Euclidean averaging ball and the open-cell geometry.

An affine input change alone does not transfer an approximation of an unchanged target from a subcube to the whole cube. The proof must first pull back and extend the target, or supply an equivalent valid construction. The rescaled Sobolev tolerance must include the derivative scaling factors.
