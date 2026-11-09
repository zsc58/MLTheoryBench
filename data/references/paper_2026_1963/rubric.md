# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1–2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3–7:** Some correct core steps or conclusions, but important steps are missing.
- **8–9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Information-theoretic converse — 3 points.** Derive the Gaussian trajectory KL identity with common policy kernels and the centered covariance recursion. Construct a finite-dimensional packing, obtain a testing lower bound of order n_x+log(1/delta) uniformly for delta<1/2, and prove the stated information lower bound under the unchanged small-epsilon condition. Crucially, an adaptive policy's unconditional input covariance can depend on the parameter. A valid route first uses the power constraint to dominate each alternative's information matrix by its noise-only Gramian, then applies the perturbation bound. Do not credit a same-covariance perturbation lemma as directly comparing the actual adaptive Gramians under different parameters.

2. **Optimal-Gramian reduction — 2 points.** Reorder the finite covariance sums, extend positive semidefinite summands to infinite time, and use the feasible averaged covariance to show lambda_min(G_t(A))<=(t-1)J_A^*. Establish or justify optimizer existence and the Lyapunov/SDP characterization as needed. A claim that one optimizer Loewner-dominates every instantaneous covariance is not a valid substitute.

3. **Fixed-covariance LSE analysis — 2 points.** Establish the horizon-indexed convolution representation, normalized design concentration, and a score bound sufficient for the stated accuracy dependence. The design bound alone does not close the LSE proof. The reference route uses an explicitly stated independent-coordinate quadratic-form inequality and a Gaussian martingale-transform bound for the score. Verify the required conditional independence in phase two and the bound ||Gamma_{U,h}||^2<=bar_gamma. Use the bias-free error identity only when the empirical design is invertible, or retain the pseudoinverse bias term.

4. **Adaptive covariance and horizon control — 2 points.** Prove the perturbation stability and Gramian estimates under the specified radius, derive optimized-objective loss at most 64(1+||B||^2 ubar)||Delta||||Gamma_infinity(A)||^3, and recover the exact stationary-tail, weighting, and discarded-initialization terms. Handle A=0, equivalently ||Gamma_infinity(A)||=1. Do not assume that the stable projection is nonexpansive: on the good initialization event the raw estimate is already stable.

5. **Two-phase conclusion — 1 point.** Use covariance (ubar/n_u)I in initialization, condition on the complete first-phase data, apply the fixed-covariance bound to the reset trajectory, and verify that the displayed implicit sufficient inequality gives failure probability at most delta. Prove the per-time power guarantee by covariance traces. Singular covariances and a zero power budget must not be excluded from the upper bound.

# Evaluator Notes

Accept any complete valid alternative proof; neither the reference presentation nor its particular packing is mandatory. Standard independent inequalities may be invoked with their relevant statements and hypotheses made clear. Merely citing a paper-specific prior theorem or saying 'the same argument applies' does not close a theorem-critical obligation.

The source's coefficient-one lower bound kl(p,q)>=log(N/(4delta)) is not a required step and must not be enforced. A uniform universal-constant lower bound of order log N+log(1/delta) is sufficient. Likewise, the source's strict upper packing-distance endpoint and asymptotic-only cardinality are not required.

The theorem has unspecified universal constants c and c', so harmless universal-factor changes are acceptable. Changes to the displayed system-dependent factors, perturbation regime, initialization normalization, or horizon terms require justification. Missing the dimension term, the valid adaptive-covariance comparison, the score concentration, or the optimized-objective sensitivity is theorem-critical.

The horizon inequality is sufficient and implicit; no unconditional existence of a satisfying horizon is asserted. The unrestricted local-stability ball is part of the task definition, although the proof may use only stable alternatives inside it. With zero input power, the density-requiring converse class is empty; this does not invalidate the upper-bound experiment.

The repaired reference proof has no outstanding private proof obligation.
