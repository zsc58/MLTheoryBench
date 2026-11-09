# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly sets up the signature vectors, empirical and population means, and the fixed Q_s Hilbert geometry. Uses the finite uniform radius of individual signatures and the independence of the sample. Integrability and the bounded positive regularized operator must be respected.
2. **3 points:** Derives the expected-deviation bound by ghost-sample symmetrization and independent Rademacher randomisation, obtaining (2/n) E_{sample,signs} ||sum_i sigma_i S(tilde gamma_i)||_{Q_s}. Preserves joint sample-and-sign expectation throughout.
3. **3 points:** Verifies coordinate sensitivity at most 2R_s/n and applies bounded differences to obtain the remainder 2R_s sqrt(log(1/delta)/(2n)), then combines this with Step 2. Handles R_s=0 directly if the concentration argument divides by R_s.
4. **2 points:** Proves the conditional empirical-complexity estimate by Q_s duality and Rademacher orthogonality/Jensen, obtaining (M/n) sqrt(sum_i ||S(tilde gamma_i)||_{Q_s}^2) for every realised sample. The zero signed-sum case is included.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A correctly stated standard bounded-differences inequality may be cited once its independence and sensitivity hypotheses are verified; reproducing its moment-generating-function proof is not required.

Treat omission of either conclusion, failure to justify the concentration constant, or merely naming symmetrization/concentration/duality without the relevant application as theorem-critical gaps. The first target contains a deterministic joint-expectation complexity term, whereas the second concerns conditional empirical complexity. It is invalid to replace the former by a realised conditional sign average without a separate argument. A radius bound supplies sensitivity 2R_s/n, not R_s/n. No sample-dependent precision operator or uniform-in-horizon conclusion is requested.
