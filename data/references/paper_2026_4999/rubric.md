# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the shared-bias cancellation and the feature bound together with the induced spectral norm to prove `\|\widetilde z(x)-z(x)\|_\infty\le R\|\widetilde W-W\|_2`.
- **3 points:** Derives the softmax Jacobian coordinate formula (or an equivalent Jacobian expression) and proves that every row has absolute sum at most `1/2`.
- **3 points:** Applies a valid mean-value/integral argument with the `\ell_1`-`\ell_\infty` bound to obtain the `1/2` Lipschitz estimate for each softmax coordinate.
- **2 points:** Combines the estimates, takes the maximum over classes, and states the resulting bound uniformly for every input and each class.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.
