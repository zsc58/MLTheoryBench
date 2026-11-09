# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes support-function scaling and attained strong duality. The argument must accommodate the stated extended-real objective. A correctly stated standard convex duality theorem with verified hypotheses is acceptable; a separation proof is also acceptable. Do not require primal attainment or assume it without justification.
- **4 points:** Derives both partial Clarke sensitivities for every optimal dual multiplier, with correct scaling. This includes establishing local finiteness and local Lipschitz continuity, for example by a Slater-based uniform multiplier bound and dual comparisons, and justifying the active-gradient inclusion on each coordinate section. A precise applicable envelope theorem with its hypotheses verified is acceptable; merely naming one is insufficient. Smooth lower contact is a valid alternative. Do not differentiate dual sections with value identically -infinity.
- **2 points:** Establishes the quantile identity from the positive-radius infimum and continuity, then derives the radius derivative using joint regularity and the strictly positive radial derivative. Direct differentiation using the assumed C1 profile or a properly justified implicit-function argument is acceptable.
- **2 points:** At the profiled pair, identifies every active multiplier's expressions with the ordinary partial derivatives under the stated differentiability of W, then applies the chain rule. Retains both direct shape and induced-radius terms. The support gradient in the first term must be taken at fixed radius before evaluation at the profile.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

No unique-dual assumption is part of the task. All claimed formulas must hold for any optimal multiplier at the relevant pair. A proof may use that a smooth active dual section touches W from below to identify its gradient at a differentiable point. Ordinary differentiability of a general locally Lipschitz function does not, by itself, imply that its Clarke subdifferential is a singleton.

The partial Clarke subdifferentials are those of the fixed-coordinate sections. A proof using joint generalized gradients must justify any passage to these section subdifferentials.

The zero-exposure case and a zero uniform multiplier bound require no divisions and are included. No empirical sampling, calibration, smoothing, ellipsoidal specialization, or radius-minimization theorem is required.
