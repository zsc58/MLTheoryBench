# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Upper-bound descent and self-bounding closure (4 points).** Derives an appropriate averaged-iterate recursion under the stated sampling model; defines trajectory disagreement at the common average iterate; proves consensus control and the optimum/second-order heterogeneity estimate; closes the A_max-C_max-V_max inequalities under the prescribed step-size restrictions; and verifies all five terms with the stated constant 18. The final tuning calculation must be valid, rather than merely asserted. A valid stronger recursion or alternative closure is acceptable.
2. **Second-order hard instance (2 points).** Constructs and verifies deterministic convex quadratic objectives on R^2 with two clients, a common bounded minimizer, and second-order heterogeneity at most tau. The same objectives must work for every K>=1 and eta>0. Establishes the exact synchronized dynamics and the lower bound min{HB^2/R,tau B^2/sqrt(R)}. If using an effective-step argument, it must cover negative effective steps as well as positive ones. Any valid universal constant is acceptable.
3. **Optimum first-order hard instance (3 points).** Constructs and verifies deterministic convex H-smooth objectives on R^3 with two clients, tau=0, and optimum-gradient heterogeneity at most zeta_*. The same objectives must work for every K>=2 and eta>0. Proves the active-coordinate estimate or a valid alternative and combines the small-, intermediate-, and large-step cases to establish the cubic term and both saturation terms. For the reference construction, L=H/2 and mu=Q/(4B^2) give the required overlap and intermediate-regime calculation. Other calibrations require their own valid justification. Verification of tau=0 must hold for every pair of points, not just where Hessians exist.
4. **Parameter and output fidelity (1 point).** Preserves the instance-before-K-and-eta quantifier order, initialization, arbitrary-M upper experiment versus two-client lower experiments, distinct averaged and final outputs, expectation mode, and universal-constant dependencies. Handles B=0, zero noise or heterogeneity, K=1 where applicable, and boundary or empty step-size intervals without adding substantive assumptions.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular universal lower constant. A named method, an invocation of an unspecified 'audited construction', or a citation to a paper-specific lemma without establishing the needed result is not a closed theorem-critical step. Major omissions include failure to establish consensus closure, failure to verify either hard instance, and failure to prove uniformity over step sizes and local-step counts.

The corrected reference uses elementary derivations throughout and has no outstanding proof obligation. Its upper-bound coefficient calculation replaces a faulty intermediate source coefficient while retaining the public constant 18. Its second-order proof uses a valid conservative universal constant instead of the source's faulty numerical comparison. Solvers need not reproduce or identify either source error.
