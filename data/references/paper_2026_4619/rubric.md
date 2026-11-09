# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: Valid instance and normalization.** Defines a finite stochastic convex optimization instance on the Euclidean unit ball in dimension 6m and verifies convexity, 1-Lipschitzness, and the required strong convexity. The verification must cover every m>=6 and the entire inclusive curvature interval. Tracks normalization of curvature and empirical accuracy, rather than appealing to an unspecified constant rescaling. For the reference construction, the message and code curvatures need not be equal, and the actual Lipschitz estimate must justify any coefficients exceeding one.

- **3 points: Code geometry and sample probability.** Supplies or correctly invokes an appropriate standard code-existence result, verifies its application, and establishes a sample event of probability at least 1/2 on which the required message control holds. Derives the sign pattern and the codeword's absence from every sampled set. Establishes that at least half of the population indices contain that codeword conditional on each sample. In the reference route this last fact is deterministic sample geometry used inside an expectation, not a second sample event. A direct second-moment argument is sufficient; the source's printed general exponential concentration inequality must not be accepted without a valid justification.

- **3 points: Empirical optimality mechanism.** Proves the explicit candidate is feasible, proves inactivity of the sampled code-loss terms, and proves that the desired max-link branch uniquely dominates every other branch and the zero branch. Checks the resulting empirical gradient or subgradient optimality conditions and uses strong convexity for uniqueness. A comparison with the zero branch must not require evaluating the code on an undefined zero message. Equivalent valid optimality arguments receive the same credit.

- **2 points: Population gap and every-approximate-ERM conclusion.** Derives the population excess-risk gap on the already established sample event, with a valid comparison to the population minimum. Uses strong convexity and Lipschitzness, or another valid argument, to obtain the stated accuracy threshold simultaneously for every approximate ERM. Establishes both the constant and curvature-dependent conclusions with universal constants and verifies their endpoints.

# Evaluator Notes

Accept any complete valid alternative proof. The reference construction, the particular numerical constants, the elementary concentration method, and the choice to obtain the constant regime as the lower-curvature endpoint are not mandatory. Award corresponding credit for alternative arguments that close the same logical obligations.

Do not require a common event across different curvature-dependent instances. The required simultaneity is over approximate minimizers and permitted accuracies within each fixed instance and sample event. The instance must be fixed before the sample is drawn.

It is not valid to intersect two events each known only to have probability at least 1/2 and claim that their intersection still has probability at least 1/2. In the reference proof no such intersection is needed. Changing numerical risk constants cannot repair a missing probability guarantee.

Do not accept the technical lemma as a black box outside its printed parameter range merely because the intended extension is by a constant factor. Either supply the elementary extension, as in the reference proof, or give another construction or argument covering the entire public range. Likewise, proving a result only for sufficiently large m does not discharge the explicit m>=6 requirement without handling the remaining cases.

In the constant-gap regime the required approximate-ERM accuracy is of order m^{-3/2}. A proof that establishes only a smaller threshold, such as order m^{-3}, does not establish that target unless it also supplies a valid stronger transfer argument.

Treat omission of either regime, an unclosed empirical-optimality mechanism, failure to achieve probability at least 1/2, or failure to establish the simultaneous every-approximate-ERM conclusion as a theorem-critical gap. The separate GD trajectory analysis is not required. The corrected reference proof has no unresolved proof obligation.
