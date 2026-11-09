# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly expands the two feasible one-dimensional objective restrictions, proves that a violating pair has positive relevant curvature even for singular positive-semidefinite kernels, and derives or verifies the clipped exact updates and their feasibility. Handles equality between an unconstrained minimizer and a constraint endpoint correctly.
- **2 points:** Establishes the quantitative objective-decrease bound and uses a lower bound for the objective plus telescoping to prove convergence of the full coefficient sequence to a feasible limit. The tail estimate must be uniform in the later iteration; in particular, step magnitudes tend to zero.
- **4 points:** Gives a complete recurrent-pair argument. Derives limiting gaps at least τ, obtains a common tail of saturated updates using finiteness of the pair families, and rigorously establishes the eventual boundary-transfer forms. For the reference route, the relevant counts are positive ordinary coordinates and interior auxiliary coordinates; their eventual constancy and exclusion of the unit auxiliary corner swap must be justified. Establishes recurrent predecessor and successor pairs by examining coordinate restoration between repeated occurrences, excludes the reverse pair, and obtains strict limiting-score order within the same family. Conservation of the block sums alone does not establish the boundary forms.
- **2 points:** Iterates the strict score chain to contradict the finite index set and correctly identifies absence of a violating pair at termination with the stated τ-approximate optimality condition.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or require both predecessor and successor constructions when a one-sided extension already gives a complete contradiction.

A proof that works for every feasible initialization or for any choice of an eligible τ-violating pair also proves the public result; do not penalize such a stronger private argument. It must still establish finite termination, rather than only convergence or vanishing step sizes.

Do not require positive-definite kernels, an extra lower bound on step sizes as an assumption, a fairness assumption on family selection, or a probabilistic convergence claim. These are not public hypotheses. The coefficient bounds ensure that the extrema in the stopping rule are over nonempty sets.

For the reference counting argument, a saturated auxiliary update starting with both coordinates interior decreases the number of interior coordinates, and increases the number of boundary coordinates. The opposite counting assertion is incorrect. The auxiliary corner transfer (0,1) to (1,0) has step magnitude 1 and must be excluded on a late tail or otherwise handled. Merely naming coordinate descent, asserting a cycling contradiction, or citing an unproved paper-specific convergence lemma does not close the termination argument.

No objective-error estimate or assertion of exact optimality is required: τ-approximate is defined by the two public score gaps.
