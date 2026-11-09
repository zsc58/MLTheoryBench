# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **4 points:** Derives a valid global one-round inequality from the parallel projected client updates, including explicit local drift bounds, telescoping over components, strong-convexity terms, and averaging of client endpoints. Uses the update direction with the correct plus sign inside its squared norm. An exact contraction coefficient involving S, its valid weakening involving m, or another sufficient descent estimate is acceptable. Merely naming a projected-subgradient or federated method earns no credit for this step.
- **2 points:** Applies the inequality at the bilevel solution for feasible rounds, separates the inner-objective gap from the regularization contribution, controls that contribution by boundedness of H, and telescopes with a finite square-step error. Correctly handles the arbitrary initial point by absorbing the finite first weighted objective term or by another valid argument; does not apply bounds restricted to X at an unjustified initial point.
- **2 points:** Uses the prescribed gamma-weighted average and applies Jensen on the global domain. Does not assume the average lies in X when x_1 may be outside X. Establishes sufficient control of the possible negative objective gap to justify ordinary Big-O, for example using bounded supporting subgradients at the feasible tail average. A valid alternative treatment of the initial point and two-sided bound is acceptable.
- **2 points:** Estimates the polynomial sums for a=1/2+epsilon/2 and b=1/2-epsilon, verifies 2a>1, a+b<1, and 1-a>b, and combines the estimates to obtain the claimed O(K^{-(1/2-epsilon)}) rate under the stated parameter restriction.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its particular error constant, or its weakened contraction coefficient. The initial product restriction need not be used if a valid proof establishes the conclusion without needing it.

A theorem-critical omission in the local-to-global estimate or in regularization-bias control is a major gap; propagate a failed dependency only when the later conclusion is thereby unsupported. Do not award a completed derivation merely for invoking an unnamed federated or incremental method.

The task allows x_1 outside X. All iterates from x_2 onward are feasible, but the full prescribed average can remain outside X. Jensen still applies because F is globally convex. A proof of only an upper bound does not by itself establish ordinary two-sided Big-O if it leaves the negative part uncontrolled. An isolated false feasibility assertion is readily repairable only when the proof otherwise supplies a valid justification for the required bound; the reference repair uses a routine supporting-subgradient estimate.

Do not require convergence of the full iterate sequence, moving regularized minimizers, or the separate iterate-convergence theorem. Those are not dependencies of this rate target.
