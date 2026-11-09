# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derives the interpolant drift and proves the preterminal diagonal identity. Also establishes that the continuous terminal diagonal is a conditional-expectation version, rather than asserting equality with an arbitrary terminal version off support. A valid argument may combine joint continuity with the estimate E||q_r(Z_r)-Z_r|| <= (1-r)E||Z_1-Z_0||.
- **3 points:** Proves that every off-diagonal denoiser is simplex-valued. The reference route derives the weighted conditional-expectation integral for s<t<1 and verifies its normalization. It treats t=1 by continuity and closedness of the simplex, not by substituting terminal time into the ordinary density formula.
- **2 points:** Derives the semigroup identity with the correct coefficients and composed argument, including t=1. The endpoint coefficients are zero and one.
- **3 points:** Derives the Lagrangian and Eulerian identities with their correct coefficients and proves the converse reconstruction, with well-defined compositions and diagonal initial condition. Correctly distinguishes the target-time ODE for t<1 from terminal extension by continuity. Handles the terminal Lagrangian identity, for example by deriving m_{1,1}(Phi_{s,1}(x))=Phi_{s,1}(x) from composition and joint continuity. The source-time equation remains valid for s<t<=1.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its integral representation if another argument proves the simplex conclusion.

The data endpoint is simplex-valued, but the noise endpoint need only be integrable and R^K-valued. Do not assume simplex-valued noise, independence of the endpoints, or a vertex-valued data endpoint.

The terminal conditional expectation is determined only almost surely under p_1. The task selects the version supplied by the continuous terminal diagonal. It does not require this version to equal x at every point of D.

The t=1 boundary is part of the task. A preterminal proof with no terminal justification is incomplete. Do not accept the displayed weighted integral as an ordinary probability-density representation at t=1, cancellation of 1-t there, or an equation involving an undefined v_1. Assess omitted endpoint arguments according to their mathematical significance and whether the answer supplies the continuity and composition facts needed to repair them.

No proof of a separate marginal-transport theorem, optimization claim, logit-space identity, or guidance theorem is required.
