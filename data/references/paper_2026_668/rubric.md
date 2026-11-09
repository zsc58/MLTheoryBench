# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the deterministic one-dimensional protocol, positive integer horizon, cumulative sums, and admissible history-dependent variance schedule. Establishes that the Gaussian expectations are well-defined, that the actions use only previous gradients, and that |x_t|<=1 by the bound on the Stein solution itself. Does not impose an additional bound on the real gradients.
- **4 points:** Derives the one-round Stein identity and explicit error terms. In the reference route, Gaussian integration by parts gives D_t=c_t E f_t'(X+g_t)-g_t E f_t(X+g_t), with X=s_{t-1}+rho_t Z. Expanding around X isolates -g_t x_t and (c_t-g_t^2)E f_t'(X). Justifies f_t'<=0 from convexity, for example through the standard semigroup representation. The derivative bound controls the mismatch by sqrt(2/pi) max{g_t^2-c_t,0}/rho_{t-1}; the Lipschitz derivative or integral Taylor remainder gives (2c_t|g_t|+|g_t|^3)/rho_{t-1}^2. The reasoning must remain valid when rho_t=0 and when g_t=0.
- **1 point:** Telescopes the one-round relation pathwise and obtains the complete total-loss upper bound with the correct endpoint expectations, constants and parameter dependence. History-dependent scales are held at their realized values inside Gaussian expectations.
- **3 points:** Proves the Boolean lower bound for an arbitrary deterministic online algorithm and an arbitrary real-valued 1-Lipschitz h, without assuming convexity. Uses independent Rademacher gradients to obtain zero expected predictable loss, applies a uniform O(1) Wasserstein comparison with N(0,T), and extracts a Boolean realization. Explains how a universal constant larger than the comparison bound yields the strict inequality.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

Standard Gaussian Stein solution representations, regularity and factor bounds, Gaussian integration by parts, and the standard Rademacher Wasserstein estimate may be invoked with their relevant statements and verified hypotheses; reproducing their independent classical proofs is not required. The convexity consequence and the explicit one-round error estimate must be justified, rather than merely named or asserted.

Almost-everywhere existence of f'' alone is not a justification for evaluating it at an atom when rho_T=0. Pointwise remainder inequalities from the Lipschitz continuity of f', integral Taylor formulas with the appropriate endpoint treatment, or a justified limiting argument are acceptable. A readily repairable omission of this endpoint can receive 8-9, but not 10.

A proof restricted to gradients in [-1,1] or to predetermined scales is incomplete unless its argument is explicitly shown to apply to the full stated domain and history-dependent schedules. No expectation over gradient sequences belongs in the upper bound. The lower bound concerns the deterministic algorithm class defined in the task; a different quantifier or expectation over internal algorithmic randomness is not a substitute.

Cover's sufficiency theorem or its strategy is not required for the lower bound. The elementary finite-space averaging argument suffices. The constant C need not equal the reference proof's choice, provided it is absolute and the strict inequality is established.
