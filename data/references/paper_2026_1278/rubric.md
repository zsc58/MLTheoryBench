# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses balance to show (p+q)h and its complement (p+q)(1-h) are probability densities, including the complementary normalization from integral(p+q)=2. For an alternative proof that does not introduce these densities, award these points for the equivalent correct use of balance and probability normalization.
- **3 points:** Derives E_P[b/h]>=1. In the reference route, identifies b/h=p/f P-almost surely for f=(p+q)h, applies KL nonnegativity and Jensen with their hypotheses justified, and covers possible infinite expectation. Merely naming KL or Jensen without the derivation is insufficient. A complete valid alternative derivation earns the same points.
- **2 points:** Derives E_Q[(1-b)/(1-h)]>=1. In the reference route, uses g=(p+q)(1-h), identifies the complementary density ratio Q-almost surely, and applies KL nonnegativity and Jensen with their hypotheses justified, including possible infinite expectation. A complete valid alternative derivation earns the same points.
- **3 points:** Substitutes the Bayes classifier into the balance condition, proves it is balanced even if it takes 0 or 1, and correctly concludes that the balanced restriction of the full [0,1]-valued class preserves the exact solution. Values on the common zero-density set do not affect this conclusion.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or the use of KL or Jensen when another valid method closes the same obligations. All ten points are available to an equivalent complete proof.

The two expectation inequalities and Bayes feasibility are all theorem-critical. Treat omission or material misstatement of any of them as a substantive gap when assigning the score.

The ratio expectations are nonnegative extended expectations and may equal +infinity. Do not require a classifier to have finite ratio expectations or finite KL divergence. For a KL/Jensen proof, log integrability must either be justified or a valid extended-expectation argument supplied. An otherwise complete proof that omits only this routine analytic justification belongs in the 8-9 range rather than receiving full credit. A proof that assumes additional finiteness without addressing the remaining cases does not establish the full target.

Balance is defined for all measurable [0,1]-valued classifiers. The strict-interiority condition belongs only to the two ratio inequalities; do not impose it on the Bayes-feasibility step. Neither pointwise probability comparisons nor coverage or training-convergence guarantees are requested or implied by the target.
