# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Uses the density-ratio inequality with valid almost-everywhere reasoning and derives the sharp mass bound `1 >= [2h+exp(-epsilon)(b-a)]v`. Explains the density-to-event implication where needed.
- **3 points:** Uses that bound to prove the fixed-interval upper bound, verifies feasibility and normalization of the two-level density, and shows that it attains `F(a,b)`. Does not assume positive prior mass for every interval or claim uniqueness in a zero-mass case.
- **3 points:** Proves that the finite candidate set contains a global optimum value. Correctly handles restriction to the prior support, attainment, boundaries, equal-height cells, diagonal cells, and feasible endpoint ordering. A valid coordinate-monotonicity or linear-fractional argument establishing corner sufficiency receives full credit without a redundant analysis of every critical-coordinate candidate.
- **2 points:** Verifies the full projected kernel for every real input label, including labels outside the selected interval, and proves epsilon label differential privacy for independently randomized neighboring datasets using common support and density bounds. The prior, parameters, and selected interval remain fixed in the neighboring-dataset comparison.

# Evaluator Notes

Accept any complete proof under the stated assumptions, including a correct linear-fractional optimization argument replacing the derivative enumeration. Merely naming privacy, monotonicity, or an optimization method does not earn the corresponding step. A missing sharp mass bound materially undermines the fixed-interval result. An independently valid proof of the fixed-interval formula may still receive its points even if an attempted preliminary argument is flawed.

The neighborhood equality holds almost everywhere separately for each fixed input. Therefore the bare substitution `r(t | pi_I(t))=v` is not justified by that assumption, even though the ratio constraint has a common exceptional set. A finite or countable fixed-center argument, an appropriately justified integration argument, or another valid treatment closes this local gap. Do not demand a stronger neighborhood-equality assumption than the public task states.

Only the density-to-event implication is needed for the theorem; proving the converse characterization is not an additional scoring requirement. If a converse is attempted, directly differentiating an arbitrary inequality between cumulative functions is not sufficient. The inequalities over every interval must be used.

At knots, cell derivative calculations may be interpreted through the smooth cell restrictions and continuity. Equal-height critical-point divisions are unnecessary, and diagonal cells have mass `alpha_i(b-a)`, not the off-diagonal mass expansion with a repeated bin. Zero-height bins, zero-width intervals, a one-bin prior, and ties must not cause undefined expressions or unsupported strictness claims.

For privacy, uniform lower and upper bounds suffice; pointwise attainment of both extrema is unnecessary. Dataset privacy follows from the single changed product factor, not an `m*epsilon` bound. Do not require a privacy analysis of a histogram-estimated prior, because that is not the mechanism in the public task.
