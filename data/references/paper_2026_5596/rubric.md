# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Regret decomposition and aligned queue geometry (3 points).** Establishes feasibility of the projections and decomposes regret using the observed subgradient. Derives the scalar positive-part recursion with the exact Euclidean coefficient, including the interpolation/feasibility argument and initialization.
2. **UPPD clearing reduction (2 points).** Uses the stated filtration and iterated conditional expectation, without assuming independent demands for the upper bound. Proves windowed clearing with probability at least 1-delta, handles B_delta>=T, and justifies the bound Delta_gap<=B_delta Delta_mv, including terminal partial intervals. Explains why the event works simultaneously for all static comparators.
3. **Projected-OGD achievability (2 points).** Establishes the OGD potential and movement bounds, verifies the movement-window condition at the stated stepsize, and obtains the displayed high-probability and expectation bounds with their parameter dependence. Handles T=1 and zero-diameter/zero-gradient cases without undefined divisions. The failure-event bound follows from the observed subgradient inequality; a global Lipschitz assumption is not available or needed.
4. **Matching lower bound (3 points).** Constructs one admissible randomized Bernoulli two-product environment for all possibly randomized learners. Uses equality dynamics to prove freezing, correctly partitions the T rounds into nonempty blocks, and proves independence of each fresh loss choice from the learner's committed block action. Computes regret against the hindsight-best static comparator, with minimization inside expectation, and derives a universal sqrt(T/mu) lower bound through valid conditional moment and probability estimates.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its numerical universal lower-bound constant. The upper and lower clauses must both be addressed; omitting a theorem-critical direction is a major gap.

For nonempty blocks, the correct count is K=1+sum_{t=1}^{T-1}xi_t. A convention that also counts a zero-length terminal block is acceptable only if explicitly defined and used consistently. Do not accept an unexplained extra nonempty block caused by xi_T.

The source's lower-bound probability estimate follows by applying Markov to N=K-1 at threshold 2mu T, then using mu T>=1. A direct Markov estimate on K at threshold 4mu T also suffices and changes only the universal constant. A direct application to K at threshold 3mu T does not by itself give probability at least one half.

Conditioning on the entire demand path for analysis must not be treated as giving that path to the learner. The lower-bound construction must respect action-before-feedback timing and independent learner randomization. The upper-bound algorithm uses only states and observed subgradients; full demand or full loss-function feedback is not an assumption.

Do not demand global constancy of losses when G_2=0: a zero observed subgradient gives nonpositive regret against every comparator. The matching-rate interpretation concerns T>=mu^{-1}, as in the converse.
