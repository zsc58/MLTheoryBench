# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes the endpoint-map construction and the needed same-kernel and cross-kernel coupling estimates from the stated dynamics. Justifies existence, differentiability, and the applicable change of variables. For the reference route, this includes the first-order position and derivative error estimates and the stronger same-kernel bounds used to handle all q>1. An equivalent quantitatively sufficient construction earns full credit.
- **3 points:** Derives the pointwise cross Rényi estimate at the correct order, including determinant control, the Gaussian linear-norm exponential bound, the Gaussian quadratic moment and its admissibility condition, and the coefficients alpha_0,...,alpha_4. A uniform-displacement Gaussian lemma cannot simply be applied with velocity-dependent displacement bounds.
- **2 points:** Lifts pointwise estimates by joint convexity under a coupling and proves the transient and invariant-to-target bias estimates using Orlicz contraction, Young's inequality, and exponential-moment interpolation. Checks the exact burn-in quadratic and both bias-moment conditions against the stated restrictions.
- **3 points:** Combines the estimates by an inequality valid throughout the public range q>1 and obtains the exact final constants and B. The reference route uses a three-quarters strengthened transient estimate at order 2q-1 and the Hölder coefficient 2q/(2q-1)<=2. A complete alternative proof is equally acceptable. Addresses h=0 and zero initial or stationary distances; an infinite initial distance makes the finite-k threshold empty.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental constants, notation, or order of presentation when another argument proves the stated conclusion.

The source's inequality R_q(a||c)<=3R_{2q}(a||b)/2+R_{2q-1}(b||c) is stated for q>=2. Applying it without justification to every q>1 is not a completed final step. Do not fix this by silently restricting the public task to q>=2. The replacement reference proof supplies an elementary all-q repair that preserves the target.

Distinguish same-kernel regularization, used for the transient term, from cross-regularization, used for comparison with the exact target-preserving kernel. Neither can be substituted for the other merely by changing an input law.

Treat an unproved paper-specific coupling estimate, failure to justify Gaussian exponential integrability, or replacement of cross-regularization by an extra assumption as a theorem-critical gap. Specialized external citations are not automatically completed proof steps. Standard independent results may be used with their relevant statements and hypotheses checked.

The reference proof demonstrates why the quadratic-in-velocity error route is unsuitable for its Gaussian exponential calculation. A different valid route need not discuss that failed route merely to receive credit.

Propagate a missing cross-regularization estimate to the final bias claim, but award independently correct subsequent calculations and combination steps. Do not award full credit solely for substituting claimed intermediate estimates into the final formula.
