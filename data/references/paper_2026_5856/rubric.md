# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly formulates the population/empirical covariance operators, cross-covariance vectors, and ridge normal equations; uses h=Sigma w_star and spectral calculus or an equivalent argument to prove the well-specified approximation bound E(f_lambda,f_star)<=lambda||w_star||^2. Operator and integral manipulations must be well defined.
- **4 points:** Establishes the single-trajectory concentration mechanism. In the reference route, this includes uniform convergence of the bounded Poisson solution under the specified total variation convention, the martingale-plus-endpoint decomposition, and application of a correctly stated bounded Hilbert-martingale inequality. It also includes the transition residual's adaptedness and conditional moment bounds with respect to the full trajectory filtration. The proof must obtain explicit bounds for the centered state observable, covariance observable, and transition residual, and combine the three failure probabilities to at most delta. Standard independent Hilbert-valued martingale concentration inequalities may be cited with their relevant statements and verified hypotheses; they need not be reproved.
- **2 points:** Derives the deterministic ridge perturbation estimate on the event ||hatSigma-Sigma||_op<=lambda/2 and verifies that the prescribed threshold supplies this event. Combines the explicit deviations to obtain the stated D4,D2,D3 estimation-error expression, or a stronger estimate implying it. In the reference calculation, the factors arise from (a+b+c)^2<=3(a^2+b^2+c^2) and (s+t)^2<=2(s^2+t^2).
- **2 points:** Combines estimation and approximation errors, states the 1-delta probability guarantee for each fixed T and admissible lambda, and correctly specializes to lambda_T=gamma T^{-1/2}. The specialization must retain the T^{-1/2} leading terms and T^{-3/2} boundary and squared-logarithm terms, with gamma fixed independently of T for the rate assertion.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's notation or presentation. A proof that merely names concentration, Poisson equations, or regularization without verifying how they control the trajectory-dependent covariance terms should not receive credit for the corresponding core step.

The deterministic perturbation inequality is conditional on covariance closeness; it is not an unconditional bound for arbitrary empirical and population covariance operators. A proof must supply this condition or use a different valid argument. Conditioning transition residuals only on X_t is insufficient as a justification of martingale concentration unless the proof also invokes the Markov property to establish conditioning on the full past.

Do not require stationarity, independent transition pairs, a moment assumption on X_0, injective features, or invertible unregularized covariance. Zero features and zero w_star are allowed, even though the source's bounding constants are strictly positive. The total variation convention is specified in the task; exact constants must be consistent with it.

The requested probability statement is not a simultaneous-in-T or almost-sure rate. For fixed delta, an admissible gamma independent of T exists. Do not demand simultaneous probability guarantees not requested by the task. No private proof obligation remains unresolved.
