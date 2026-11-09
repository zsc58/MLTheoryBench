# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly solves the linear SDE and obtains the transition and joint endpoint covariances with the stated sigma-squared normalization. Establishes the needed invertibility, including the terminal transition covariance for every t<1, and justifies the symmetry needed in the control formula.
- **3 points:** Correctly conditions the joint Gaussian law to derive both the bridge mean and its Schur-complement covariance. Establishes convergence of the full bridge path law to the deterministic path in the uniform-topology continuous-path space, not merely convergence of one-time marginals, and accounts for the endpoint values.
- **3 points:** Derives the endpoint bridge drift correction from the Gaussian transition density, or an equivalent valid argument, and proves the residual identity needed to obtain the stated control on the limiting path. Any use of a standard bridge formula must be appropriate to the nondegenerate transition density and the time interval t<1.
- **2 points:** Correctly diagonalizes the heat drift while retaining the arbitrary deterministic forcing through the stated centering or an equivalent calculation. Obtains both the zero-mode linear formulas and the nonzero-mode hyperbolic-sine path and correctly normalized control formulas, including kappa=0.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A solution that merely asserts Gaussian conditioning or a bridge-score formula without carrying out the resulting required formulas does not establish the corresponding core step. Conversely, a solution may use standard Gaussian conditioning, Brownian stochastic-integral facts, or the standard diffusion-bridge identity without reproving the general theorem when it states or correctly applies the relevant result and verifies its hypotheses.

For full-path convergence, a representation of the bridge as b+sigma G with one fixed continuous centered Gaussian bridge G is sufficient. Vanishing covariance at each individual time, without an argument controlling the continuous-path law, is not sufficient by itself.

The heat calculation may not silently impose alpha=0. The endpoint in centered spectral coordinates is x_1-h_1, and the displayed path formulas describe b_t-h_t. Equivalent formulas in uncentered coordinates are acceptable if they retain the forcing terms.

The nonzero-mode control must use the mathematically equivalent corrected normalization, including the factor corresponding to 1-e^{-2 kappa lambda_i}.

State independence refers to the displayed value of the control on the deterministic limiting path. Do not require the finite-noise drift correction to be independent of an arbitrary intermediate state, or require uniform convergence of random controls as t approaches 1. Do not require an inverse of the remaining transition covariance at t=1.

The marginal Schrödinger bridge optimizer, endpoint-coupling optimization, and the specialized generator-mixture proposition are not proof obligations for this fixed-endpoint task.
