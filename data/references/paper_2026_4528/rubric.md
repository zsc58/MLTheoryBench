# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the conditional Gaussian experiment, holding the historical center fixed and treating the mean as unknown rather than available to the rule. Translates to Y~N(mu,sigma^2 I_p), with mu=q-m, and computes the unrestricted risk p sigma^2.
- **3 points:** Establishes the stated positive-part risk comparison and translates it back: risk at most p sigma^2 everywhere and strict improvement whenever q!=m. A correctly stated and applicable standard positive-part James--Stein theorem is sufficient; alternatively accept a valid direct risk calculation. The estimator is already defined and need not be derived. The zero-observation convention must not cause an undefined rule. Strict improvement at q=m is valid but is not an additional public requirement.
- **3 points:** Establishes the minimax lower bound for all allowed rules, including randomized rules. For the Gaussian-prior route, computes posterior mean and covariance, obtains Bayes risk p tau^2 sigma^2/(tau^2+sigma^2), justifies why randomization cannot reduce posterior squared-error risk, bounds supremum risk below by Bayes risk, and lets tau^2 tend to infinity.
- **2 points:** Combines lower and upper bounds to prove that both the positive-part and unrestricted rules are minimax, distinguishes pointwise strictness from strictness of supremum risk, concludes inadmissibility of the unrestricted rule, and transfers the pointwise inequalities to the conditional-risk assertions almost surely.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its Gaussian-prior route, or a named theorem when an equivalent argument is supplied. Conversely, an applicable standard independent risk theorem may be cited with a sufficiently explicit statement and verified hypotheses; proving that classical theorem from scratch is not required.

Treat a missing conditional-experiment argument, access to the unknown mean as an estimator input, an asserted rather than justified minimax lower bound, or failure to establish strict nonzero-translated-mean improvement as a theorem-critical gap. The lower bound must cover the stated randomized class, though a concise posterior convexity or conditional-mean argument is enough. Do not require a separate computation of the limiting risk of the positive-part rule: the minimax lower bound and its pointwise upper bound already imply equality of its supremum risk with the minimax value.

The event assertion concerns the conditional-risk random variables. It does not assert a comparison of losses conditioned on an arbitrary event selected using the current observation. No unconditional moment assumption on the mean or center, stationarity assumption, optimization-convergence argument, or plug-in variance result is required.
