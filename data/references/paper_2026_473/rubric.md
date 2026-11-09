# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Prove the upper bound by the continuous divergence. In the reference route, derive the conditional-binomial representation for arbitrary mu and the quantile-domain Bernstein/Beta representation under mu<<nu, then apply Jensen and the partition identity. Account for the stipulated infinite continuous divergence without absolute continuity. Award equivalent credit for a complete alternative argument.
- **2 points:** Prove monotonicity for arbitrary mu. In the reference route, construct and verify the adjacent-resolution deletion stochastic kernel, including its boundary columns and action on the uniform reference laws, then apply or derive finite-alphabet f-divergence data processing. Award equivalent credit for another complete proof.
- **1 point:** Establish convexity in mu and weak lower semicontinuity under continuity of the reference CDF, with appropriate treatment of extended-valued f. Include K=0, either directly or through an argument valid at that boundary.
- **4 points:** Prove convergence and every stated quantitative alternative. In the reference route, identify the piecewise-constant Beta-average approximation and derive uniform convergence for arbitrary continuous rho from its modulus of continuity and the uniform Beta second-moment bound. A concavity assumption on the modulus is not available. Transfer uniform estimates through Lipschitzness of f to obtain the Holder O(K^(-alpha/2)) and C2-rho O(K^-1) rates. For Lipschitz rho and C2 f, explicitly justify cancellation of the Taylor linear term, control Var(rho(S)) by the squared Lipschitz constant times Var(S), and average the resulting Jensen gaps to obtain O(K^-1). Verify that evaluation points stay in the range interval of rho and that constants are independent of K>=1. Award equivalent credit for complete alternative estimates.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its particular auxiliary approximation, or its deletion-kernel route when another argument establishes the same targets. Every theorem-critical estimate used must be derived or obtained from a correctly stated standard result with its hypotheses verified; merely naming Bernstein approximation is insufficient to establish rates for a different approximation operator. Do not require a concave modulus, strict positivity of rho, finite f outside the stipulated range in the convergence part, or additional smoothness beyond the public assumptions. Interpret rho's regularity as regularity of its almost-everywhere density-ratio class through the stated continuous extension. Treat all three rate alternatives as inheriting the base convergence assumptions. Minor omitted routine details may qualify for 8-9, but an unproved quantitative alternative or an unjustified restriction to concave moduli is a missing substantive step.
