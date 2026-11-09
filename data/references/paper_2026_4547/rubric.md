# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **1 point:** Correctly uses shared-coupled, data-independent initialization and the explicit zero-discrepancy assumption to establish D_0=0 and sets up the pathwise recursion for a neighboring pair, with coefficients evaluated at that pair and the shared randomness.
- **3 points:** Derives the explicit unrolled certificate bound D_T<=C_T, including the empty-product convention and/or equivalent induction, rather than merely naming an unrolling argument.
- **3 points:** Applies loss domination, expectation over U, and the neighbor supremum to prove the stated stability bound with gamma_T(S)=L sup_{S'~S} E_U C_T(S,S';U). Keeps the supremum outside the expectation and respects the order |E_U[loss difference]| in the target.
- **3 points:** Gives a valid replace-one-sample exchangeability argument and correctly concludes the expected population-minus-empirical risk gap is at most E_S gamma_T(S). The correct signed identity uses ell(h_T(S^(i),U),z_i)-ell(h_T(S,U),z_i). An unchanged replacement has zero loss difference and does not require the neighbor hypothesis.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's incidental presentation choices.

The explicit measurable and integrable setup justifies the expectation calculations. A solver need not reprove the assumed measurability of the dataset-level supremum, and should not claim that an arbitrary uncountable supremum is automatically measurable. No bounded-loss, metric, contraction-factor-less-than-one, interpolation, optimizer-specific or adaptedness assumption is needed.

The source proof has a locally repairable sign error in its exchangeability calculation; do not reproduce or reward that false equality. A valid absolute-value proof is acceptable. The previous reference proof already used the correct sign.

The example distribution may have atoms. A ghost replacement is either an actual neighbor or an identical dataset. An otherwise correct proof that merely omits this readily supplied zero-difference case has a minor omission, not a fundamental failure. Likewise, the empty-neighbor case is covered by the public zero-supremum convention. All steps apply for n=1 and T=1.

There are no unresolved reference-proof obligations and no specialized external result whose invocation alone is required for credit.
