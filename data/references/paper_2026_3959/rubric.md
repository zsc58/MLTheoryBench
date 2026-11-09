# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Establishes derivative reproduction under the C^2 assumption and proves the three finite-span reductions. The reductions preserve sampled gradients, input-map values, and operator-induced sampled matrices, while not increasing the respective norms. The operator compression preserves Q+Q* positive semidefinite and admits coefficients with Lambda+Lambda^T positive semidefinite, including singular or zero feature spans. Establishes existence using compact sublevels in the finite-dimensional function/operator spaces.
- **2 points:** Derives the sampled identities and all three squared regularizer identities, including the Hilbert-Schmidt trace identity for potentially nonsymmetric Lambda. Proves equality of optimal values, attainment of the finite program, and reconstruction of every finite minimizer.
- **3 points:** Establishes the norm-epigraph interpretation of the block constraints, surrogate convexity and nonemptiness, existence and uniqueness under invertible Grams, feasible propagation, quantitative strong-convexity descent, and compact invariant feasible sublevel behavior. Verifies the stated initialization.
- **2 points:** Establishes continuity of the unique surrogate minimizer map using strict feasible approximations or another valid argument, and proves the convergence/connected-accumulation-set alternative with all hypotheses checked. Shows that every fixed-point coefficient tuple is stationary for (P), including the zero-residual case and the elimination of the auxiliary p coordinates.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The operator and coefficient cones permit nonsymmetric elements. Replacing Q+Q* positive semidefinite by Q self-adjoint positive semidefinite, or replacing Lambda+Lambda^T positive semidefinite by Lambda symmetric positive semidefinite, changes the problem and does not establish the requested result.

For singular Grams, raw coefficient sublevel sets need not be bounded. Compactness may be proved in the represented function/operator spaces or in appropriate reduced coefficient coordinates.

A derivative reproducing theorem may be used with its precise C^2 hypothesis stated and checked, or proved. A selected weakly convergent subsequence of difference quotients alone does not prove differentiability.

The residual LMI enforces p_i>=||r_i||, including p_i>=0. The inequality p_i^2>=||r_i||^2 for unrestricted real p_i is not by itself equivalent to that LMI.

A convergence theorem may replace the elementary accumulation-set argument if its relevant statement is supplied and its hypotheses are verified. Merely naming a monotone-iteration theorem does not complete this step.

Tangency transfers first-order conditions to the lifted problem, but the task concludes stationarity for the coefficient program. A proof must justify this further passage, for example by a tangent-feasible perturbation or a complete multiplier-elimination argument. It must not assume all residuals are nonzero.

A proof that merely names projection, convex-concave linearization, or a convergence theorem without verifying the corresponding preservation, descent, continuity, or stationarity conditions does not earn the associated full credit.
