# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derives the truncation mean bound ||mu_P-mu_Q||<=2 nu_{P,p} epsilon^(1-1/p) and the covariance/operator-norm comparison.
- **3 points:** Establishes the U-statistic expectation and variance bound, including both variance terms, and converts it to the stated dimension-dependent fluctuation control.
- **3 points:** Uses the null/alternative mean separation, threshold alpha^2/4, and a valid concentration argument to prove the 2/3-success guarantee under the stated sample size.
- **2 points:** Gives a correctly quantified two-point indistinguishability construction for every p>=2, 0<epsilon<=1/2, and signal level alpha>0, with finite directional p-moment, alternative mean norm at least alpha, the relation alpha<=c nu_{P,p} epsilon^(1-1/p), a zero-mean null, retained mass at least 1-epsilon, identical observed laws, and the resulting impossibility conclusion.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of either the achievable test guarantee or the matching lower bound as a theorem-critical gap.
