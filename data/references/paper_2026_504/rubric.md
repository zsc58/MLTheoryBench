# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes rho tensor rho-almost-everywhere avoidance of the cut relation from its measurable rho-null sections, then transfers this to the coupling by absolute continuity. Uses complete-manifold exponential/geodesic facts to obtain smooth interpolation on the whole closed time interval with one exceptional set of endpoint pairs. Establishing only pi_{0,1}-almost-sure avoidance does not by itself establish the stated product-volume assertion.
- **2 points:** Proves that multiplication by 1-t maps ID(y) diffeomorphically onto (1-t)ID(y), not generally onto ID(y); obtains an open image under Exp_y; verifies the inverse on U_t(y); and derives the cut-time equivalence with the center treated separately from the unit-direction formula.
- **4 points:** Correctly selects a conditional version consistent with the fixed initial density kernel, and derives the conditional density with its exact determinant ratio and zero extension outside the image. Allocate up to 1 point for the conditional-version/pushforward justification and up to 3 points for the actual Jacobian and domain computation. An explicit polar radial substitution or an equivalent calculation using the exponential-map volume Jacobian earns full credit. Merely naming change of variables without computing the required factor is not a complete Jacobian step, but does not erase independently earned credit.
- **2 points:** Justifies absolute continuity and normalization for every endpoint under the chosen kernel convention, and proves existence of a smooth density representative on the entire open image when the initial conditional density is smooth. Allocate up to 1 point for absolute continuity/normalization and up to 1 point for smoothness. The smoothness argument must cover the center; smoothness of polar coordinates only away from the center is insufficient for full credit.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or require polar integration if the same determinant ratio is correctly computed by another method. Standard cut-locus, exponential-map, Jacobi-field, and manifold change-of-variables results may be invoked with their applicable statements and hypotheses; the theorem-specific composition and Jacobian computation must still be justified.

A conditional distribution is determined only almost everywhere in its conditioning variable. The task asks for a suitable version with the displayed properties for every y, not for those properties to hold for every arbitrary modification of a conditional kernel. The initial conditional sections must remain normalized probability densities on null conditioning fibers. No independence, moment assumption, or extra regularity of the coupling is required.

Do not accept evaluation of F_t^{-1} outside U_t(y) on the ground that an indicator subsequently multiplies the expression by zero. Piecewise definition or an explicitly harmless extension is adequate. The determinant is on the normal space of dimension d-1; confusing it with the full tangent-coordinate Jacobian without the radial power gives the wrong factor.

For full smoothness credit, a proof may use the smooth positive volume Jacobian of the inverse diffeomorphism or an equivalent normal-coordinate extension. Simply asserting that dist(y,z) and Log_y(z)/dist(y,z) are smooth at z=y is false. No regularity across the boundary of U_t(y) is required.

The four steps are logically connected; propagate a missing geometric inverse or Jacobian computation to downstream claims only when those claims are not independently established. Do not demand lengthy separate discussions of d=1, t=0, or infinite cut times when the argument already covers them. If dimension zero is admitted, the connected one-point case is immediate and the off-center formula is vacuous. Do not impose conditional absolute continuity at t=1. The marginal-density notation is justified by mixing the conditional kernels and by the prescribed target density at t=1; this does not introduce a separate theorem branch or extra scoring step.
