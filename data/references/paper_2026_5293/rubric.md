# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly computes the empirical marginal from the independent conditional Gaussian model and uses Gaussian scaling to obtain the de-scaled Gaussian mixture with bandwidth \(h_t=\tau_t/t\). The resulting formula represents the specified continuous density.
- **4 points:** Correctly derives \(v_t(ty)=y+(M_t(y)-y)/\tau_t\), including the time-dependent coefficients and the conditional means used. Either the score/local-mean and velocity--score route or a direct finite-mixture conditioning argument earns full credit. The argument must identify the specified continuous conditional-mean version, not merely an arbitrary version on a set of full probability.
- **3 points:** Shows that normalized exponential Gaussian logits give precisely the local-mean weights and verifies that the affine post-map outputs the exact velocity for all stated \(t\) and \(y\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or insist that a direct conditioning proof introduce scores. A proof that asserts the velocity identity or the equality of weights without derivation does not satisfy the corresponding core step. Algebraically equivalent definitions of the normalized exponential aggregation are acceptable.

The clean input is \(B=s_J\); it is not the interpolated endpoint \(Y_1=B+\epsilon Y_0\). All pointwise claims refer to the continuous versions specified in the task. An explicit positive Gaussian-mixture density and continuous finite-mixture conditional-mean formula justify these versions; do not demand a separate lengthy version-uniqueness argument when these facts are clear from the proof. An almost-everywhere identity alone, without identifying or extending to the continuous versions, leaves a readily repairable pointwise-justification omission rather than refuting the target.

Check that divisions are legitimate for \(t>0\), \(\tau_t\geq\epsilon>0\), and \(m\geq1\). A general argument covering the domain need not separately discuss \(m=1\), repeated support points, \(t=1\), or \(\epsilon=1\). Do not require assertions at excluded parameter values, iid sampling of the fixed support, a population density, statistical rates, or a learned-attention implementation.
