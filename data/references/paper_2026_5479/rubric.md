# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **3 points:** Correctly unrolls the scaled open-loop covariance with the shared process-noise covariance $G$, groups terms by transport length, and establishes the decomposition of $\Omega_{\rm open}(s)$ with $s$-independent positive-semidefinite $m\times m$ matrices.
2. **3 points:** Establishes positive definiteness of the observation covariance, differentiates $\frac12\log\det\Omega_{\rm open}(s)$, and proves the trace formula and nonnegativity. Includes strict positivity whenever some $A_\ell\ne0$ for $\ell\ge1$, zero derivative when all those coefficients vanish, and zero derivative for the separately defined no-transport comparison.
3. **2 points:** Derives the one-step filtered log-determinant derivative with the correct Jacobian and covariance factors, holding the incoming filtered covariance fixed, and explains its nonnegativity.
4. **2 points:** Substitutes the gain into the covariance update and proves $P^+(s)\preceq P^-(s)$ by positive-semidefinite ordering, connecting this to non-strict covariance localization at individual assimilation steps.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Require derivations of the covariance decomposition, trace monotonicity, and Loewner contraction; merely naming filtering, chaos, or a covariance-volume argument is insufficient. The standard log-determinant differentiation identity may be used with its applicability established; reproducing its elementary derivation is not required.

Deduct for missing strictness or zero-pressure cases, incorrect matrix dimensions, unaccounted-for dependence on $s$, or unjustified inverses of potentially singular latent covariances. Nonzero latent transport alone does not ensure strict observed-space volume pressure: the nonzero condition concerns the observed-space coefficient matrices $A_\ell$.

The no-transport comparison is the stated additive recursion without a scaling factor. It is not obtained by setting $J_i=I_d$ and then applying the expansion factor to $I_d$.

A missing open-loop decomposition loses credit for that obligation and for any volume conclusion left unsupported, but an independently justified volume calculation should receive its appropriate credit. Score an independently correct filtered derivative or contraction separately.

Contraction is non-strict and compares the posterior with the prior at the same assimilation step. Do not require strict contraction, monotone covariance decrease across time, stability of the deterministic core, monotonicity of the full Gaussian likelihood, or a derivative through an entire recursively rerun filter. The reference proof's additional verification that the posterior is positive semidefinite supports repeated applicability but is not a separate scored target. No Lyapunov-limit or entropy theorem is required.
