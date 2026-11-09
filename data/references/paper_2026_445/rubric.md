# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **4 points: Weighted path identity.** Correctly expands the joint forward-path density and product weight, cancels the forward transitions and telescoping Gibbs factors on the proposal support, uses the stated support condition to avoid losing target mass, and uses normalization of every backward kernel to prove
  \[
  \mathbb E[\varphi(X_j)\omega_j]
  =\frac{1}{Z_{\theta_0}}\int\varphi(x)\rho_{\theta_j}(x)\,dx.
  \]
  A complete justification can first treat nonnegative test functions and then target-integrable signed or vector-valued functions. Merely naming a weighted-particle or path-space identity without deriving or otherwise justifying it does not earn full credit.
- **2 points: Exact gradient recovery.** Applies the identity to both h_{theta_j} and 1, verifies that the denominator is finite and positive and the numerator is absolutely integrable, cancels the common normalizing factor, and uses the stipulated gradient representation to obtain the exact ratio nabla F(theta_j). Recognizes that unconditional exact expectations give deterministic parameters and well-defined updates at every finite time.
- **3 points: One-step loss contraction.** Identifies the recursion as exact gradient descent and correctly combines the L-smooth descent inequality, eta<=1/L, and PL to establish
  \[
  F(\theta_{j+1})-F_*\le(1-\eta\mu)(F(\theta_j)-F_*).
  \]
  The usual smooth descent inequality may be invoked as standard background or derived by integrating the gradient along a segment.
- **1 point: Geometric iteration and boundary cases.** Justifies iteration with the correct exponent and initial gap, including k=0 and a zero contraction factor. For a nonconstant objective, mu<=L follows by combining PL with the smoothness consequence ||nabla F(theta)||^2<=2L(F(theta)-F_*). A constant objective has zero gaps and must not be excluded by adding mu<=L as an assumption. Accept any equivalent treatment of the possible sign of the contraction factor.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. The weighted identity and exact-gradient conclusion must be established rather than assumed. A failure to justify the weighted identity leaves the central reduction unsupported, but later convergence credit may still be awarded if exact gradient descent is independently established. Minor indexing or notation errors are repairable only when they do not alter the path cancellation or the iterate used in the update.

The initialization omega_0=1 means the weighted identity includes 1/Z_{theta_0}; it is not permissible to assume Z_{theta_0}=1. Omitting a common factor while correctly obtaining the normalized ratio is a local normalization error, not a failure of the entire gradient-descent argument. Likewise, omission of the readily repairable constant-objective case is a minor completeness issue rather than grounds for rejecting all otherwise valid steps.

Do not require invariant, reversible, mixing, or everywhere-positive forward kernels, bounded h_theta, a parameter-independent normalizer, or finite-particle estimates. These are not assumptions of this task. The explicit support condition suffices for the cancellation argument and must not be replaced by an unsupported claim that almost-sure evaluability of the quotient alone is sufficient.
