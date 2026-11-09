# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Defines the truncation and correctly derives the coverage bias bound and integrated-coverage second-moment bound, then obtains a constant-success multiplicative estimate with $O(M/\epsilon)$ samples.
- **2 points:** Correctly boosts the constant-success estimate to confidence $1-\delta$ by grouping and taking a median, obtaining $O(M\log(1/\delta)/\epsilon)$ samples and rescales by $Z$.
- **3 points:** Constructs and analyzes a rare-set two-level perturbation with separated normalizing constants and verifies an $M$ for which $\operatorname{ICov}_M\le\epsilon M$ and $M/\epsilon=\Theta(1/p)$.
- **2 points:** Gives the indistinguishability/testing argument showing that fewer than a constant multiple of $1/p$ samples cannot achieve multiplicative success probability $2/3$, yielding the $\Omega(M/\epsilon)$ converse.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.
