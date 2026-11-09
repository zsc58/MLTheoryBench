# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derives the squared-loss bias-variance identity, identifies the population minimizer as E[z(P)], and proves that the ERM is the sample mean in Lambda with excess risk equal to squared estimation error. Uses the box-restricted instance-wise optimal selector from the task, not a different global-optimum selector.
- **2 points:** Establishes the upper bound s Lambda_max^2/(4N) by independence across observations, coordinatewise boundedness, and a valid variance bound. The normalization is N^{-2} when summing variances over all N observations, equivalently N^{-1} when summing the variances of one observation over coordinates.
- **3 points:** Gives an explicit admissible two-point/separable MILP family, establishes its minimum-norm multiplier identity, constructs suitable binary-indexed distributions, and proves their population means are separated in squared distance by order epsilon^2 s. Checks the hard-feasible activity bound, finite attained minima, and membership of the selected multipliers in Lambda, including Lambda_max=2.
- **2 points:** Controls KL for N full-instance observations by a valid calculation, verifies the information condition throughout s>=8 and N>=1, applies Fano with an explicit conversion from decoding error to squared loss, and chooses epsilon proportional to N^{-1/2} to conclude the universal Omega(s/N) lower bound.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular hard family. In particular, an alternative family with nonunique optimal multipliers is acceptable if the task's minimum-norm selector is proved to have the required identity. A complete alternative mean-estimation lower bound may replace packing/Fano, provided its statistical hypotheses and its realization by admissible MILPs are checked.

The lower-bound construction must establish the multiplier identity and the separation/KL calculations; merely naming Fano or a hypercube is insufficient. Squared Euclidean distance is not a metric, so an unexplained direct application of a metric version of Fano to squared distance does not close the loss-conversion step. Nearest-mean decoding followed by squaring the half-separation threshold is valid.

For a Fano proof, the assertion log M>=(s/8)log 2 alone does not guarantee a positive universal bracket at s=8. The additive log 2 must be handled, for example by the reference proof's four-word packing for 8<=s<16. A proof only covering s>=16 leaves part of the stated regime unproved unless it supplies a valid remaining case argument. This is a locally repairable omission when the rest of the proof is complete, not a reason to change the public range.

For complementary Bernoulli biases, the claimed bound KL<=4epsilon^2 is valid for epsilon<=1/4, but it does not follow from writing 4epsilon^2/(1-epsilon^2)<=4epsilon^2. Use the exact KL formula or another correct estimate; a different absolute constant is acceptable with a corresponding perturbation choice.

The source's separable tent function has a unique maximizer but is not strictly concave. Coordinate slopes directly prove the multiplier identity. A solver need not prove optimization-selector existence again if treating the task's well-defined selector as given; any existence argument it supplies must be valid.

The final rate treats B and Lambda_max as fixed problem constants. Do not require the displayed universal lower bound to match the upper bound uniformly in a varying Lambda_max, and do not require an additional population-utility integrability assumption from the separate direct-multiplier learning problem.
