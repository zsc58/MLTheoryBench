# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly reduces recovery at fixed \(\theta^\star\) to the free-coordinate convex allocation problem, including fixed coordinates, zero coefficients, box-induced lower bounds, and the \(\bar k=0\) and affordable-support cases. The argument must retain indicators fixed at one even when their coefficients vanish and must cover empty free sets and all-zero free coefficients.
- **4 points:** In the over-budget case, establishes budget activity and derives or otherwise rigorously proves optimality of the capped proportional allocation \(u_j=\min\{1,|\theta_j^\star|/\tau\}\). A mere reference to KKT is insufficient: primal feasibility and an adequate global-optimality argument must be checked. An explicit convex KKT certificate is sufficient without a constraint qualification or an analysis of every possible multiplier choice. The argument must remain valid at \(\tau=M\) and when a coefficient of magnitude \(M\) makes the lower and upper indicator bounds coincide.
- **2 points:** Establishes existence of a threshold in \((0,M]\) satisfying the budget equation and derives the sorted capped-prefix formula with its consistency inequalities. Justifies that a suitable capped-prefix index satisfies \(s<\bar k\), using the existence of a positive tail when the number of positive free coefficients exceeds \(\bar k\), or an equivalent valid argument. Threshold ties may be handled by any consistent convention.
- **2 points:** Extends the free allocation to all coordinates, establishes attainment of the indicator-dependent partial minimum, and correctly concludes joint optimality from minimization of the full partially minimized objective.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or order of steps. In particular, a direct feasible construction and global-optimality certificate need not separately derive all multiplier regimes.

The central allocation characterization is theorem-critical: an unsupported water-filling assertion, an invalid threshold argument, or reliance on the claim that a lower-bound-only KKT coordinate forces an arbitrary multiplier-derived threshold to equal \(M\) is a major gap. Such a coordinate gives only a multiplier-derived threshold at least \(M\); the same primal allocation can instead be represented using threshold \(M\).

Do not confuse lower-bound-only activity with coincident lower and upper activity. A coordinate with magnitude \(M\) and indicator one can coexist with interior coordinates and need not force the multiplier-derived threshold to be at least \(M\). A correct explicit certificate already handles this case; no separate discussion is required if its validity is clear.

A solver need not prove uniqueness of the threshold, uniqueness of the entire indicator vector, or consequences for rounding and branching. These are not additional public targets. Do not require strict feasibility, a positive remaining budget in the zero-budget case, or a strict separation at threshold ties. Treat a merely omitted elementary justification of the strict capped-count bound as a readily repairable omission, not as equivalent to an invalid allocation characterization.
