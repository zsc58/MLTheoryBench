# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly handles the quotient of jointly measurable conditional probability densities and the finite supremum L_n metric. Establishes that the discounted visitation expression is a probability kernel, that q^pi belongs to Q, and that the operator preserves joint measurability, nonnegativity, normalization, and finite supremum L_n norm. Justifies representative independence, possibly through the contraction estimate awarded below.
- **4 points:** Proves the gamma-contraction inequality. A reference route cancels the one-step feature term, applies Jensen to the transition-policy expectation, justifies interchange with feature integration, and bounds the result by the supremum over all next conditioning pairs. Equivalent valid norm estimates receive full credit.
- **3 points:** Derives the one-step discounted-visitation recursion from its series and the transition-policy dynamics, then uses it in the feature integral to establish directly that [q^pi] is a fixed point. A valid alternative direct verification receives full credit.
- **1 point:** Uses the established fixed point and contraction to prove uniqueness and the exact error bound for every initial class and every k>=0, and concludes convergence. Correctly recognizes that the intrinsic reward depends only on the resulting probability measures, without claiming that L_n convergence implies convergence of KL values.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or a particular order of the obligations.

Q is not asserted to be complete. The normalized density subset of L_n can fail to be complete when n>1 and the reference measure has infinite mass. Do not require a proof of completeness, and do not accept an unsupported assertion of completeness or a bare invocation of Banach's theorem as an existence argument. The reference route proves existence by checking the explicit q^pi and then derives uniqueness and convergence directly. A different Banach-based proof is acceptable only if it verifies the hypotheses of the space to which it applies and still proves every claim for the full domain in the task.

The quotient uses mu-almost-everywhere equality separately for every conditioning pair, not a single null set common to all pairs and not almost-everywhere equality in the conditioning variable. The supremum is over all conditioning pairs. Integral interchanges may be justified by nonnegativity and Tonelli, using the sigma-finite reference measure and probability kernels.

Cover gamma=0, n=1, and the k=0 error estimate. No positivity of q*, finite-KL assumption, smoothness assumption, ergodicity assumption, or stationary initial-state assumption is needed. Extended KL values are allowed. Do not award the contraction or fixed-point points merely for naming Jensen's inequality, a recursion, or a fixed-point theorem without establishing the relevant claims.
