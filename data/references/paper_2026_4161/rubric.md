# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives the terminal-reweighting identity for the batch variance tilt, using the positive finite normalizer Z_A and showing that the tilted score is the independent base score plus the logarithmic gradient of the conditional expected variance. The argument supports the pointwise claim at every positive time and batch, for example through the Gaussian posterior density.
- **2 points:** Establishes the conditional bias-variance decomposition into the variance of posterior means and the (n-1)/n^2 covariance-trace contribution, using conditional independence under the base posterior experiment.
- **3 points:** Derives or adequately verifies the VE posterior mean, covariance, and Jacobian identities, and differentiates the mean-variance term to obtain (2/n)J_t^T B(mu_i-bar mu). In particular, the covariance identity must be justified rather than treated as an unexplained paper-specific input.
- **3 points:** Differentiates the covariance trace with the required third-derivative and column-wise divergence calculation, combines both gradients, obtains the exact normalized score, and justifies the reverse-time sampler initialized from q_T^A with continuous terminal law pi_0^A.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

For the reverse-time conclusion, an accurately stated standard Brownian time-reversal result with its hypotheses checked is sufficient; reproducing the reference proof's transition-kernel derivation is not mandatory. The application is in dimension nd to the joint tilted density, and the score is evaluated only at positive forward times. The terminal state is the continuous limit as reverse time approaches T.

The normalization condition 0<Z_A<infinity is supplied by the task, so solvers need not derive it from separate moment assumptions. Do not require a full-rank feature map, a formula for Z_A in terms of an unconditional covariance, or full-dimensional second moments of p_0. Posterior moments at positive times are finite by Gaussian damping. A=0 and all other zero or nonnormalizable tilts are excluded by the normalization assumption.

Do not accept initialization from a product Gaussian as an exact substitute for q_T^A. Do not accept an almost-everywhere conditional-expectation identity as the entire justification of an everywhere score claim unless its positive-time continuous version is supplied or established. Routine omitted Gaussian-domination details can be treated as readily repairable when the reasoning is otherwise complete.
