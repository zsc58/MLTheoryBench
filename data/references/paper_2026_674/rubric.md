# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derive the five Lipschitz bounds for phi and the constrained unique-maximizer sensitivity with the stated constants. Justify the envelope gradient representation and obtain both envelope-gradient Lipschitz constants. No Lipschitz assumption on nabla_zeta l in zeta is available or needed.
- **3 points:** Establish gamma-strong convexity of the envelope and the exact expected gradient's strong-monotonicity and global Lipschitz inequalities. Correctly bound the vector-valued distribution-shift term by s L^f_{theta xi}||theta-theta'||. Verify the finite expectations and the frozen-law differentiation needed for stable-point identification.
- **3 points:** Handle the singleton domain directly. In the nonsingleton case, justify beta>0 and the real-valued rate, derive kappa_gd^2=1+2eta(s L^f_{theta xi}-gamma)+eta^2 beta^2 using projection nonexpansiveness, and prove 0<=kappa_gd<1. Establish existence and uniqueness of a projected fixed point on the closed domain and identify it with the frozen-surrogate stable point by the projection optimality condition.
- **2 points:** Bound the approximate gradient error by L^phi_{theta zeta}delta, obtain the projected recurrence, and solve it with the finite geometric-sum factor. Deduce the limiting neighborhood radius and exact-inner convergence for delta=0 without setting s=0.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Require the distribution-shift contribution, contraction constants, and explicit perturbation radius; merely naming strong convexity, Wasserstein duality, or projected-gradient descent is insufficient.

The distribution sensitivity s and inner approximation tolerance delta are independent. A proof restricted to delta=s, or one that assumes s=0 in the exact-inner case, does not prove the task. The update uses an exact expectation, not one noisy sampled gradient. The target is the Lagrangian-surrogate stable point, not an asserted equivalent solution of the original ambiguity-constrained problem.

A missing technical estimate may lose its associated points, while a theorem-critical unsupported contraction, stable-point identification, or neighborhood claim is a major gap. A brief correct treatment of the singleton case is sufficient. The case kappa_gd=0 is allowed, and the t=0 estimate uses the empty geometric sum. A solver need not prove convergence of approximate iterates to an individual point: the requested conclusion is the finite-time distance bound and its limiting-radius consequence.
