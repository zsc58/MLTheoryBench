# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives the uniform-action posterior formula from conditional probability, conditional independence, and reward/decoder realizability, including the positivity of its denominators on the stated event. The argument must be valid for the permitted feedback space and the almost-sure interpretation of conditional probabilities.
- **3 points:** Proves heterogeneous-state separation from the uniform distribution and establishes the threshold consequences for both realized reward/decoder values. Justifies the positive constants and the zero-reward separation comparison, and covers every maximizing action, including ties.
- **3 points:** Correctly analyzes the given piecewise ramp decoder at the posterior, proving heterogeneous lower-bounding and optimal-action exactness together with homogeneous-state equality. Includes $c=0$ and $c=1$ without evaluating undefined fractions, and distinguishes the homogeneous expected reward from its realized reward.
- **2 points:** Proves global Lipschitz continuity of the decoder under the infinity norm with constant at most $4/\kappa+1/\xi$, handling regime boundaries and points lying in different regimes. The smaller valid constant $2/\kappa+1/\xi$ is acceptable.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's sigma-field notation, auxiliary clipped weight, or other incidental presentation choices. The decoder $J$ is already defined in the task; constructing a new decoder is not required.

The two cases are the values of the binary reward or its decoder, not two values of the feedback. Feedback need not be binary, discrete, or supplied with a density. A conditional-probability, conditional-expectation, or otherwise justified likelihood argument is acceptable; an unjustified division by probabilities of individual non-atomic feedback values is not a complete posterior derivation.

The posterior derivation, both heterogeneous reward cases, the homogeneous interior and endpoint cases, and a genuinely global Lipschitz argument are theorem-critical. No values on null conditioning events, full-support assumptions, counterfactual coupling of rewards across actions, or extra parameter restrictions are required. Do not require separate treatment of an impossible heterogeneous configuration. Do not award duplicate credit merely for restating the same optimal-action conclusion in the posterior and decoder discussions.
