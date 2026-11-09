# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Conformity construction and event equivalence (2 points).** Establishes that the explicitly defined filter has a nonempty closed interval of safe thresholds, and consequently that the infimum defining each score is attained and that \(E_i\le\tau\) is equivalent to factuality of every retained claim. A direct analysis of the finite-prefix boundary lottery or any equivalent rigorous argument is acceptable. Monotonicity alone does not prove attainment. The argument must accommodate empty documents and zero and unit scores.
2. **Conditional group exchangeability (3 points).** Fixes a positive-probability test group and conditions on the calibration group-index set or count as appropriate. Justifies that the selected calibration scores and test score are exchangeable, using the fixed score/grouping maps, the i.i.d. document model, and independent auxiliary randomization.
3. **Finite-sample rank/quantile bound (3 points).** Uses \(r=\lceil(m+1)(1-\alpha)\rceil\), proves the needed probability bound, and handles ties and endpoint cases. For \(r\le m\), an explicit randomized-rank inclusion or equivalent counting proof earns full credit. For \(r=m+1\), including \(m=0\), uses the endpoint threshold one and its safe filtering behavior. Merely naming a conformal method is insufficient.
4. **Final group-conditional conclusion (2 points).** Transfers the score event through the filtering definition at the calibrated random threshold and averages over the calibration group indices or counts to prove the guarantee for every positive-probability group.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its auxiliary inclusion-boundary notation.

Do not require oracle factuality, conditional independence between claim labels, score accuracy, atomless scores, or a positive minimum calibration size within each group. These are not assumptions of the task. A solution that assumes any of them without disposing of the general case does not prove the full result.

The claim is conditional on test-group membership and averages over calibration data and randomization; it is not a guarantee conditional on the realized calibration sample. Independent continuous tie-breakers used only in a proof do not change the filtering algorithm.
