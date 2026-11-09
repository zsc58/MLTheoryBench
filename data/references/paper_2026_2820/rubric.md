# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Adaptive RKHS confidence bound (3 points).** Uses the actual infimum-representation RKHS norm, verifies predictable features and the conditional moment assumption, and derives the factor-two comparison for the attained parametric minimizer. Either the full-RKHS-minimizer argument or the direct inequality from `L_t(g_t)<=L_t(f)` is acceptable. Applies self-normalized concentration at the fixed positive lower ridge and retains the factor `alpha_ell^{-1/2}` in the induced-kernel radius. Handles time zero consistently.
2. **Kernel-to-GP reduction (2 points).** Uses `lambda_t>=lambda_0`, Woodbury, posterior-variance monotonicity under positive-semidefinite kernel domination, and determinant monotonicity at the same fixed ridge. Obtains the exact public radius, including the noise factor `1/sqrt(alpha_ell lambda_0)`, rather than only an unspecified constant multiple.
3. **Exploration and variance decay (3 points).** Shows that a favorable initialization eventually forces the unique optimal decision on the confidence event, using the finite positive gap and `lambda_t/log t -> infinity`. Establishes a quantitative count for favorable initialization events under the original probability measure and transfers it pathwise to optimal visits on the confidence event. Derives the repeated-observation variance bound and its logarithmic-schedule specialization. Accounts for the time shift and for singleton or zero-diagonal cases, either explicitly or by an argument that already covers them.
4. **Cumulative regret (2 points).** Gives a summable initialization-tail bound covering `t=0`, uses the model `g_{t-1}` in the greedy regret decomposition, and combines both variance sums with Cauchy-Schwarz. The played-point determinant must correspond to inverse ridge `alpha_ell/lambda_0`. Allocates failure probabilities validly and proves the stated uniform-in-horizon high-probability asymptotic rate. A stronger rate with exponent `zeta+q/2+1/2+q d_eff/4` also proves the requested conclusion.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its particular exponential counting process, or introduction of an auxiliary full-space minimizer.

A qualitative ordinary or conditional Borel-Cantelli invocation does not by itself establish an `Omega` count. A quantitative counting law must be stated with applicable hypotheses or derived. Moreover, an implication that holds on a global confidence event does not establish an unconditional conditional lower probability for optimal visits. Treat either uncorrected inference as a substantive gap in the exploration step.

Do not assume `||g_theta||_{H_G}^2=k_Theta(theta,theta)` or identify `rho` with the unprojected parameter-kernel distance without proving minimum-norm representability. The quotient norm is the task's definition.

The first target is an exact confidence inequality, so its normalization cannot be repaired by hiding factors in big-O notation. Constant-factor slips confined to the asymptotic regret calculation are readily repairable when the probability and rate arguments are otherwise complete. Do not penalize the omission of a separate proof at `delta=1`, whose probability lower bound is vacuous.

All listed core steps have complete derivations in the replacement reference proof; no unresolved external or paper-specific proof obligation is being treated as completed.
