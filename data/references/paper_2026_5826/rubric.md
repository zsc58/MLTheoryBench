# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Uses the stated score-only experiment and conditional iid window correctly; uses the upper-tail p-value definition, the estimator \(1-\overline Y/(1-\lambda)\), two-sided clipping to [0,1], the \(1/n\) quantile allowance, and the +infinity overflow convention consistently. Definitions need not be recopied merely to earn these points.
- **3 points:** Derives the conditional expectation identity from the mixture probabilities, applies Hoeffding with the proper direction and scaling, explains why clipping preserves the upper-bound event, and proves ID-FPR validity using one-sided DKW and mixture nonnegativity. Handles overflow and accounts correctly for reserve conditioning and confidence probabilities.
- **3 points:** Establishes the empirical quantile's upper population-CDF level, accounting for its empirical jump; verifies containment in the stated density interval; treats a threshold below the oracle as a nonpositive-loss case; and converts the CDF gap to the stated power loss through the two density bounds. Respects the event formulation of the density condition and does not condition DKW on that event. An equivalent valid quantile argument is acceptable.
- **2 points:** Specifies the identical joint observable law in the two worlds, couples the same measurable randomized rule using the same independent seed, and derives the exact ceiling from the two threshold cases. Handles extended thresholds and the already-included endpoint pi=0, and transfers the inclusion to the probability assertion.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of either the conservative calibration argument or the indistinguishability converse as a theorem-critical gap.

The requested confidence bounds need not be tight. A Hoeffding failure bound eta_1/2 is sufficient for the requested eta_1 allowance. A proof of the power implication with failure probability eta is stronger than the requested eta+eta_1 and deserves full credit; the power calculation does not need the contamination-upper-bound event.

Do not accept clipping an excessive quantile level to one in place of the prescribed +infinity output. Do not accept an upper empirical-quantile CDF bound without controlling its jump or giving a valid alternative argument. Do not accept an unconditional reserve guarantee based on an unspecified high-probability reserve condition whose failure probability has not been charged.

The density condition is a realization-wise premise inside a high-probability assertion. A proof must not replace the requested bound on the joint event of regularity and failure with a concentration statement conditioned on regularity. When its upper endpoint is infinite, the positive density lower bound cannot hold; this does not invalidate the false-positive certificate and does not establish a nontrivial power guarantee without the density premise.

The frozen task requires only the conditional component of the source's contamination-estimation theorem. It does not require or permit using its unestablished reserve-averaged DKW transfer as a completed proof step. The source's additional asymptotic drift-floor discussion is also outside the scoring contract. There are no unresolved theorem-critical obligations in the replacement reference proof.
