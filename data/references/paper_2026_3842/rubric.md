# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **Step 1 (2 points):** Justify that the centered quantity is well-defined from the stated assumptions, construct the Doob decomposition S=sum D_i, identify the replace-one conditional-expectation representation, and derive deterministic conditional second- and pth-moment bounds from the envelope moments. Independence from the preceding sigma-field must justify replacing the conditional envelope moment by its unconditional value.
- **Step 2 (3 points):** Rigorously control truncation and centering. For the reference route, take y=pz/[4(p+2)], define T_i, mu_i and U_i, and establish the large-increment bound, the deterministic centering-bias bound, and the conditional moment estimates. In particular, conditional variance is bounded by the original second moment, whereas a valid general bound for the centered pth moment is 2^p times the original pth moment. Obtain P(|S|>z)<=(1+2y/z)A_p/y^p+P(|sum U_i|>z/2), or a valid alternative with sufficient constants.
- **Step 3 (3 points):** Establish and correctly apply the finite-moment exponential estimate, including its cutoff and the centering factor. For the reference route, the iterated pth-moment term has coefficient (exp(2ty)-1-2ty)A_p/y^p. Complete the Chernoff analysis in all relevant regimes: with alpha=2/(p+2), gamma=p/(p+2), and B=A_p/y^p, the optimized bound is at most the sum of exp{-z^2/[2(p+2)^2e^p A_2]} and B. A Gaussian-only claim for the truncated sum is not valid in general. An alternative correct optimization or concentration argument is acceptable if its hypotheses and constants are verified.
- **Step 4 (2 points):** Combine the common exceptional event with both signs of the truncated tail without double-counting the polynomial budget. Obtain the stated two-sided bound with polynomial coefficient 4(4(p+2)/p)^p and the stated Gaussian exponent. Cover A_2=0, p=2, and equality cases in any regime split.

# Evaluator Notes

Accept any complete valid alternative proof; neither this particular truncation level nor this proof architecture is mandatory if the alternative establishes the exact requested bound. No source-specific theorem names or references are required.

Do not award credit for merely naming truncation, martingales, or concentration without deriving the polynomial and Gaussian terms. A precisely stated independently applicable result may be used only with verified hypotheses and constants; merely citing the desired result under another name does not prove it.

The pth moment of a centered truncation cannot be assumed to be bounded by the original pth moment without proof. Omitting the large-tilt polynomial contribution, extending a cutoff-limited Gaussian MGF estimate to unrestricted tilts, or deriving the two-sided coefficient by an unsupported union bound is a theorem-critical gap, not a minor arithmetic slip.

The assumptions already imply integrability of f; do not require the solver to add an integrability assumption. A routine omitted explanation of that implication, or an otherwise readily repairable omitted degenerate case, should be distinguished from a missing concentration argument.

Minor arithmetic slips in an otherwise correct argument may lose at most one point; omission of a theorem-critical truncation or MGF justification is a major gap. All obligations in the replacement reference proof are explicitly closed; there is no unresolved GT step for the evaluator to assume.
