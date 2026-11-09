# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Signomial calculus and elasticities (2 points).** Correctly differentiates components in the positive input orthant and derives the log-gradient identity without a score-sign restriction. Derives the weighted-elasticity identity and G=zE where the class score is positive.
2. **Global and proportional sensitivity (3 points).** Proves the exact rescaling formula for q>0 and its first-order perturbation with O(epsilon^2) remainder for fixed parameters and input. Derives the class-margin derivative throughout the positive input orthant, including its elasticity form when both scores are positive.
3. **Probability sensitivity (2 points).** Differentiates the softmax with respect to log-features and obtains the centered log-gradient expression. The argument must allow zero or negative class scores; positivity of the softmax denominator, not of the scores, is sufficient.
4. **Log-space explanations (3 points).** Establishes exact logarithmic additivity for positive components and for a positive single-component whole score. Derives all three first-order Taylor expansions with O(||delta||^2) remainder. The log-score expansion requires z_c(b)>0; the score and probability expansions hold at every positive-coordinate baseline. Justifies the remainder by local C2 regularity or an equivalent argument.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

Do not require positivity of every coefficient, component, or class score. Zero coefficients and mixed-sign components are allowed. Component logarithms and elasticities must only be used on their specified positive domains. A proof of the probability formula only when every class score is positive does not establish the full claim unless it also gives a valid extension argument.

The asymptotic statements are local for fixed parameters and expansion points, not uniform over all models or baselines. A standard Taylor theorem with verified local smoothness is sufficient; an explicit numerical remainder constant is not required. Do not require exact additive decompositions of aggregate scores or probabilities beyond the stated single-component logarithmic identity.
