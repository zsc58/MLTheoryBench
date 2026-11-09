# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly works under the conditional predictive law, justifies the finite conditional mean and its recursion, derives the error recursion, and obtains the explicit coefficients a_{j,k} in the finite innovation expansion. Does not impose an additional unconditional moment assumption.
- **3 points:** Derives the conditional characteristic function by joint independence from F_N, conditional independence of the innovations, and the Laplace characteristic function, with the correct product over j. The argument permits zero propagated coefficients, which contribute factors equal to one.
- **3 points:** Under distinct positive scales, derives the partial-fraction coefficients and normalization, justifies Fourier inversion by checking integrability or supplies an equally valid alternative argument, and obtains the signed Laplace-density sum and stated CDF.
- **2 points:** Under the distinct-positive-scale condition, establishes symmetry, continuity and strict positivity of the conditional density; proves existence and uniqueness of the positive central radius for every alpha in (0,1); justifies its F_N-measurability; and derives the exponential equation on q>=0 and exact conditional coverage for hat y_{N+k}.

# Evaluator Notes

Accept any complete valid alternative proof under exactly the stated assumptions. A correct proof may establish some conclusions under a broader regime, but it must prove all requested assertions without adding assumptions.

The standard Laplace characteristic function and standard Fourier-inversion theorem may be used when their relevant statements are given or unambiguously invoked and their hypotheses are checked. The paper-specific partial-fraction formula must be justified, for example by evaluating at its distinct poles or by a polynomial identity. Merely naming partial fractions is not a completed derivation.

The displayed density is a signed sum; individual coefficients A_{j,k} need not be nonnegative. Positivity must follow from the actual conditional distribution or an equivalent valid argument, not from a false claim that all A_{j,k} are positive. A bounded continuous positive Laplace density convolved with an independent probability law gives a sufficient justification of positivity and continuity.

Conditional means are conditional-distribution integrals as specified in the task. Do not demand an unstated unconditional L^1 assumption. A short induction using the conditional absolute first moment suffices for their finiteness.

The radius may depend on F_N. Its measurability follows, for example, from a rational generalized-inverse construction. A correct but omitted routine measurability justification is a readily repairable omission, not grounds to reject an otherwise complete proof.

The exponential equation is asserted to have a unique solution only on q>=0. Additional negative roots do not contradict the theorem. Coverage concerns the fitted predictive variable hat y_{N+k}; it does not assert exact coverage for a different data-generating process with arbitrary estimation error.

The k=1 case is included by the empty-product convention. No distinct-scale density formula is required when scales coincide or a propagated coefficient is zero. Naming convolution or Fourier inversion without supplying the necessary theorem-critical justification earns only the corresponding partial credit.
