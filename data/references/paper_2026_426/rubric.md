# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Centering and foldwise conditioning (2 points).** Centers the loss by subtracting \(\ell(0,Y)\), explains why this preserves the empirical minimizer and all population excess-risk comparisons, and conditions on each training complement so that the fold dictionary is fixed and its validation data are independent. An equivalent argument that cancels the common loss baseline is equally acceptable. Introducing an uncontrolled bound on the raw loss baseline does not establish this step.

2. **Uniform convex-hull generalization bound (4 points).** Uses Lipschitz contraction, convex-hull invariance, a finite-class Rademacher bound, and bounded-range concentration to obtain a uniform foldwise deviation for the centered risks of order \(L_\ell B\sqrt{\log(MK/\delta)/n_k}\). Correctly makes the events simultaneous and derives the aggregate rate using \(n^{-1}\sum_k\sqrt{n_k}\le\sqrt{K/n}\). Merely naming Rademacher complexity or concentration without deriving the uniform rate earns limited credit.

3. **Cross-fitted oracle comparison (2 points).** Applies empirical optimality with the two uniform-deviation terms to prove the oracle inequality for \(R_{\mathrm{CF}}\), and obtains the comparator restricted to prior-free candidates by set inclusion. Identification of this functional with the conditional risk of a randomized fold-deleted aggregate is an optional interpretation, not a required proof obligation.

4. **Refit transfer (2 points).** Applies the uniform refit-gap bound once at \(\widehat w\) and once to compare the two oracle infima, producing exactly \(2\varepsilon_n\), and derives the prior-free refit consequence.

# Evaluator Notes

Accept any complete alternative proof under the stated assumptions. Do not require the reference proof's notation or incidental presentation choices. In particular, do not deduct credit for omitting the auxiliary randomized-predictor interpretation, which is not requested in the public task. A proof that assumes a bounded raw loss and hides its bound in the universal constant has a theorem-critical gap because the assumptions control only \(\ell(0,Y)\) separately from \(L_\ell B\). The baseline-free uniform deviation is for the centered risks, not generally for the raw risks. Fold balance must not be assumed unless the same stated rate is otherwise justified.
