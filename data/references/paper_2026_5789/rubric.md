# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: Effective-rank sensitivity.** Correctly differentiates the normalized eigenvalues and entropy to obtain \(\partial r_{\mathrm{eff}}/\partial\lambda_k=b_k\), or establishes an equivalent directional-derivative formula.
- **4 points: New-direction regime.** Justifies that positive mass on \(\ker(A)\) creates normalized spectral mass \(\varepsilon_t=(\operatorname{tr}(QBQ)/\operatorname{tr}(A))t+O(t^2)\), or obtains another estimate sufficient for the entropy argument. The justification must remain valid when the positive eigenvalues of A are repeated: an elementary block argument or a correctly stated and applicable standard spectral-cluster perturbation result is acceptable. Establishes a positive entropy contribution of order \(t\log(1/t)\), controls changes from the old spectrum by \(O(t)\), and concludes strict increase for all sufficiently small positive t. A lower bound on the new entropy contribution suffices; a matching upper asymptotic is not required. Merely asserting that additional eigenvalues increase rank is insufficient.
- **4 points: In-span regime.** Uses the range condition to show that the kernel remains inactive, obtains \(\lambda_k'(0)=u_k^{\mathsf T}Bu_k\), applies the effective-rank chain rule, and uses the assumed positive sum to conclude strict increase on a right neighborhood of zero. The eigenvalue derivative may be derived or obtained by stating and correctly applying standard simple-eigenvalue perturbation. Merely naming eigenvalue perturbation without giving the relevant derivative and checking its applicability is insufficient.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular orthogonal block transformation. The two regimes are both required. A proof of only one regime cannot receive credit for the other. Do not impose simple positive eigenvalues in the new-direction regime. If a solver independently establishes the needed entropy or directional-derivative conclusion despite an error in an earlier derivation, score the independently established downstream achievement on its merits.
