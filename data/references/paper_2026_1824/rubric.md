# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Justifies the local stationary-value definitions by a valid chart and transverse implicit-function argument, obtains the available regularity, and proves exact correspondence between nearby critical points and stationary points of phi. Uses derivatives of the pulled-back scalar objective, or an equivalent valid geometric formulation.
- **3 points:** Identifies the reduced mixed coefficient with the normalized Hessian eigenvalue crossing speed and derives the exhaustive transcritical classification, including the nontrivial branch, its slope -2alpha/beta, and the O(mu^2) remainder at k>=4.
- **3 points:** Uses evenness of phi and the nonzero cubic stationarity coefficient to prove exactly two opposite-coordinate nontrivial branches on the specified side, the squared-coordinate asymptotic, and absence of nontrivial branches on the other side. Provides a valid finite-regularity argument rather than applying the IFT from differentiability at a single point.
- **2 points:** Establishes the sign of the reduced second derivative on the bifurcating branches, correctly identifies the supercritical and subcritical alternatives, and proves the one-unit full Morse-index change with the constant transverse inertia handled.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The local stationary-value notation in the task does not grant its existence, uniqueness, or critical-point correspondence as assumptions; these must be justified. No explicit formula for gamma in terms of unreduced derivatives is required. A raw fourth kernel-direction derivative is not generally gamma.

At finite k, the generic branch is guaranteed at least C^{k-2}; C-infinity regularity is not required. The pitchfork branches need not be differentiable as functions of mu at the meeting point. Parameterizing their combined curve by the kernel coordinate is valid.

A squared-coordinate IFT proof is acceptable if its required neighborhood and regularity hypotheses are established. Merely showing continuity and a derivative at the origin is insufficient. Solving for mu as an even function of a and proving one-sided monotonicity is also valid.

Symmetry is the stated evenness of phi. No global manifold involution, isometric group action, or additional symmetry hypothesis may be required. Supercritical and subcritical follow the task's reduced-stability convention, not a presumed sign of alpha. Reduced minima may retain negative transverse directions. The trivial index changes by one, but its direction of change depends on the sign of alpha.

The zero-dimensional transverse complement is allowed. Do not penalize an otherwise valid proof solely for leaving its vacuous transverse equations implicit.
