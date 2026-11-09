# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **(2 points)** Correctly use the OU model, nondegenerate Gaussian initialization, positive observation noise, continuously differentiable Gaussian marginal parameters, covariance compatibility, and the actual drift coefficients of both gauges. Distinguish the actual coefficient B from the coefficient K in the diffusion-free Lyapunov equation. Justify applicability of the path-entropy formula from the bounded affine coefficients and finite Gaussian moments, or use another valid entropy argument.
2. **(2 points)** Expand posterior KL using Bayes' formula and the path-entropy identity. Correctly identify the observation constant and discard only nonnegative terms: initial KL, mean drift cost, squared observation residuals, and observation covariance traces. Obtain the covariance path functional with its factor of one-half. No optimization over the posterior mean is required.
3. **(4 points)** Establish the common covariance lower bound and the occupation-time/control-cost estimate. For the reference route, derive the diagonal residual u=lambda_1-dot-1+2alpha lambda_1 and justify the rotational lower bound for each gauge, including repeated eigenvalues without singular eigenbasis formulas. Then split at delta=1/(4omega), prove both occupation alternatives, and account for low-set endpoint terms, obtaining the stated linear coefficient and additive constant. A correct alternative covariance estimate giving the requested conclusion earns full credit; merely asserting the theorem-critical scalar inequality without justification does not.
4. **(2 points)** Under stationary initialization, establish positive lower and finite upper spectral bounds for the stacked observation covariance, uniform in omega, and use the Gaussian density formula to bound C_OU from below independently of omega. Combine this with the first conclusion for both gauges.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's incidental presentation choices, its particular eigenbasis notation, or its explicit numerical stationary lower bound. A stronger lower bound implying the requested inequality is acceptable.

The rotational estimate for both gauges, treatment of repeated eigenvalues or an argument avoiding that issue, the occupation estimate or a valid replacement, and the uniform stationary evidence bound are theorem-critical. The mean path need not be optimized and no claim that the posterior mean belongs to the C1 candidate family is necessary.

The source has three locally corrected intermediate formulas: the square-root conjugation uses Lambda^{1/2} Omega Lambda^{-1/2}; the completed-square subtraction contains omega^2; and the isotropic covariance equation uses the actual coefficient B=A_q, not K. Do not require or reward the erroneous versions.

The expanded reference proof closes all theorem-critical obligations; there is no unresolved GT dependency.
