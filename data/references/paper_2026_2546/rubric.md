# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the specified Stieltjes transforms and the inverse-branch meaning of R and decompression. Justifies the legitimacy of reciprocal-transform expressions on the stated domain, for example from the strict sign of the imaginary part. Merely repeating the setup is not required and does not by itself earn these points.
- **3 points:** Correctly derives the decompression reparameterization \(P(z+(\tau-1)/(\tau m_\tau),\tau m_\tau)=0\), with a justified relation between the initial inverse coordinate and the decompressed coordinate. A local argument near infinity followed by analytic extension is sufficient; a global assertion that the shifted coordinate stays on the original physical sheet is not required and must not be assumed without justification.
- **3 points:** Clears denominators and performs the binomial expansion to construct the polynomial extension \(Q_\tau\), with a correct finite coefficient expression or an algebraically equivalent expansion. Correctly covers \(\tau=1\) and interprets the resulting polynomial at \(m=0\).
- **2 points:** Shows that \(Q_\tau\) is nonzero and that its relation holds throughout the stated physical domain, thereby establishing algebraicity. Nontriviality may be proved using invertibility of the rational coordinate substitution or another valid argument. Analytic extension may be established earlier in the proof.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Deduct substantially when the inverse-branch correspondence, rational reparameterization, or denominator-clearing coefficient derivation is merely asserted.

Herglotz normalization is not a general uniqueness theorem for roots of an arbitrary polynomial P, which may be reducible or have extraneous factors. The physical transforms in this task are specified by their measures. Do not require uniqueness of root selection, irreducibility of P, an explicit construction of the decompressed measure, infinite divisibility, or a matrix-subsampling limit.

There are no zeros of a probability measure's Stieltjes transform off the real axis. Therefore a solver may handle reciprocal-transform expressions directly by this fact rather than inventing a separate exceptional-zero case. The target concerns finite values on \(\mathbb C\setminus\mathbb R\), not values at poles. Missing an explicit discussion of extra real boundary or continuation values is not a defect.

The nonzero-polynomial obligation is necessary for the algebraicity conclusion. Its omission is a readily repairable gap when the rest of the proof is complete, but it should not receive full credit as though it had been established.
