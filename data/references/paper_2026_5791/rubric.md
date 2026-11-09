# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly uses the two reduced estimators on the pinned chain without changing the boundary or data assumptions, and justifies that the minimizers used in the proof exist and are unique. Valid interior coordinates, gap coordinates, or an equivalent approach are acceptable.
2. **3 points:** Derives the ridge normal equations with the correct coefficient, \((D_L^TD_L+2\lambda I)x_R=D_L^Tr_L\), establishes a valid inverse bound, computes or otherwise controls the data vector uniformly in \(L\), and proves \(\Delta_R(\lambda)\le2\sqrt3/\lambda\). The stronger bound \(\sqrt3/\lambda\) from the reference proof is acceptable. An unspecified length-independent \(O(\lambda^{-1})\) bound alone does not establish the explicit inequality requested in the task.
3. **4 points:** Correctly minimizes the gauge-invariant objective and derives \(\Delta_S(\lambda)=(2L+1)/(2L+1+2\lambda)\), with the dynamic range taken over interior vertices only. In the gap-coordinate approach, this requires the bijective parametrization under the pinned boundary, separability, \(d_0^*=-\tau_L/(\tau_L+2\lambda)\), and \(d_i^*=0\) for \(i\ge1\). A complete alternative derivation of the exact range receives equal credit.
4. **1 point:** Correctly draws both limiting conclusions: ridge collapse is uniform in \(L\) as \(\lambda\to\infty\), while \(\Delta_S(\lambda)\to1\) for fixed \(\lambda>0\) as \(L\to\infty\), explicitly contrasting the two regularizers.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. All parameter coefficients must be interpreted according to the displayed public objectives. Multiplying an entire objective by a positive constant is harmless; changing only one term changes the estimator unless a parameter substitution is explicitly made and translated back to the public parameter before stating the conclusion.

The ridge normal equations contain \(2\lambda I\). The second objective is already consistent with the source appendix after its data normalization is included; there is no additional half-weighted-penalty repair to impose. The pinned energy includes the terminal edge \((u_L-1)^2\). Replacing it by the interior quadratic form alone drops a boundary-dependent linear term and is not an equivalent formulation.

A proof of only an unspecified \(O(\lambda^{-1})\) ridge bound earns partial credit for the uniform-rate argument but does not receive full credit for the requested explicit inequality. Neither a fixed-length ridge limit nor a limit allowing \(\lambda\) to vary with \(L\) substitutes for the two stated quantifiers.
