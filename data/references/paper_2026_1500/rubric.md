# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Risk decomposition under uniform label noise (3 points).** Correctly condition on the clean label and derive $R^{(\eta)}=(1-J\eta/(J-1))R+\eta T/(J-1)$, including the definition of the total one-hot loss.
2. **Uniform total-loss range (3 points).** Expand the sum of the pointwise losses over all one-hot labels and use valid power-sum bounds for simplex probabilities to obtain the stated lower and upper bounds, hence their explicit difference.
3. **Optimizer comparison and positivity (2 points).** Apply noisy-risk optimality of $\theta^\eta$ against $\theta^*$, use clean-risk minimality for nonnegativity, and correctly rearrange using $\eta<1-1/J$.
4. **Final parameter/noise algebra (2 points).** Substitute the total-loss range and simplify the denominator and parameter expression to exactly the claimed $M_{\beta,\lambda}^{(\eta)}$ bound.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of the central decomposition or the explicit total-loss bound as a theorem-critical gap.
