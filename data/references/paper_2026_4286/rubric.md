# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **(2 points)** Correctly work conditionally on the stated event and establish support containment from both current-active-support inclusion and true-support coverage. Distinguish the within-epoch/provisional trajectory from the thresholded endpoint. Do not treat local guards as available after an unproved exit, or assume that true-support coverage alone supplies error-support containment.
2. **(3 points)** Derive the l1 ratio inequalities from the local guards and perform a joint cone/radius induction. Use both explicit mass budgets and the strict initialization margin R_in<R. The proof must include the provisional endpoint and must use the assumed small-cone/R_in reset at every epoch, rather than claim that large-cone invariance automatically implies that reset.
3. **(1 point)** Prove that support-preserving hard thresholding cannot increase squared error, leaves the on-support error unchanged, and cannot increase off-support l1 error. Conclude endpoint cone and radius preservation. A separate beta-min argument is optional because support preservation is assumed.
4. **(2 points)** Use error-support containment, pathwise curvature, score control, and bounded directions to derive the squared-error recursion and epoch bound. Recursive substitution must use nonnegative coefficients; replacing each coefficient by exp(-mu eta_t) is valid without an extra step-size assumption. State geometric contraction with its stochastic tolerance and correctly use the quantified domination condition for contraction to zero.
5. **(2 points)** Derive the harmonic-step scalar recursion and sum or solve it to prove the logarithmic-over-linear squared-error rate starting at T_0+1, including the initial case and the corresponding norm rate. Constants must be independent of the time index over the stated horizon.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's presentation.

The local-gradient event, pathwise curvature, score inequality, and direction bound are explicit hypotheses of this conditional problem. Do not require a solver to prove their joint high probability from A1-A4. In particular, do not award a supposed statistical closure for a fixed-beta concentration bound followed only by a union bound over coordinates and times: that does not justify uniform control at adaptive iterates using overlapping windows.

The external additive-tolerance curvature result is unnecessary here and does not imply the assumed stronger pathwise inequality. Citation of that result alone is not a substitute for the update-expansion argument.

The source's pointwise coordinatewise lemmas have locally repaired proofs, recorded privately. Deriving them is optional background, not a condition for full credit on this conditional task. Their deterministic conversion to l1 guards may be discussed, but the public problem already stipulates the guards as part of its event.

If an answer includes optional concentration calculations, confidence prefactors must be handled correctly. A bound uniform over p,T>=1 and delta in (0,1) uses log(2pT/delta) for the truth score, or an equivalent logarithm bounded away from zero. Fixed-window on-support bounds use log(2p/delta), with confidence splitting absorbed correctly. The original log(p/delta) off-support form is harmless for p=1 because the off-support set is empty, and for p>=2 the prefactors can be absorbed into its constant. These auxiliary corrections do not change the public conditional task or require changing its stipulated zeta. An optional concentration error is not a missing core proof step when the conditional proof does not use it.

Do not accept an unspecified 'radius budget', an unproved small-cone reset, unqualified geometric convergence after dropping the remainder, or multiplication of inequalities by possibly negative contraction factors. These are theorem-critical issues unless repaired elsewhere in the answer.
