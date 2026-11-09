# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly analyzes the rank-one PSD lift, verifying its unit Frobenius norm and proving that its Frobenius overlap is $(u^\top v)^2$. Translates the rank-one PSD interference constraint into the absolute spherical line-correlation constraint.
- **3 points:** Establishes a sufficient spherical-cap estimate and a valid finite maximal antipodal packing/covering argument, yielding $C_\varepsilon(S_+^p)\ge\tfrac12(1-\varepsilon)^{-(p-1)/2}$ and exponential growth for fixed positive epsilon. Finite maximality must be justified, for example through compactness and positive separation; an equivalent direct finite construction is acceptable.
- **3 points:** Under the fixed-address isotropic-value model and stipulated query-to-distractor correlations, derives both pSNR formulas, including the squared-versus-unsquared interference contributions. If invoking expected powers, correctly holds coefficients fixed and eliminates cross terms using independence and zero means. Recognizes that the stipulated regime makes both denominators positive.
- **2 points:** Solves the strict ideal-retrieval inequalities, obtaining linear iff $T<2p$ and PSD iff $(T-p)^2<p^2(T-1)$. Establishes that, within $T>p$, the latter is equivalent to $T<T_+$, where $T_+=(p^2+2p+p\sqrt{p^2+4p-4})/2=p^2+2p-2+O(p^{-1})$. Justifies the quadratic-scale conclusion and does not include equality in the ideal regime.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Stronger valid cap estimates and equivalent packing constructions are acceptable.

The public definition already gives pSNR as a coefficient quotient; a solver may compute directly from that definition without separately deriving its expected-power interpretation. Do not require the private upstream Welch verification, an equiangular tight frame, or a construction attaining global pairwise Welch equality. Only each distractor's squared correlation with the matched query is stipulated.

The packing lower bound concerns dictionaries constructed from rank-one matrices inside the full PSD cone. Do not treat a general unit PSD matrix as necessarily rank one. The theorem does not assert that the greedy dictionary also realizes the stipulated retrieval correlations.

Ideal retrieval means a strict expected-power criterion, not exact realized recall or a high-probability success guarantee. At an integer value equal to $T_+$, pSNR is one and the criterion fails. A proof that knowingly includes this equality is not fully correct. Equivalent descriptions using the largest integer strictly below $T_+$ are acceptable.

All theorem-critical reference obligations are closed. Minor omissions of routine compactness or algebraic details should be assessed under the general 8-9 category rather than mistaken for a substantive counterexample to the theorem.
