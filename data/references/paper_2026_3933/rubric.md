# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Establishes the conditional weighted-law representation, including that the weighted measure depends only on the unordered multiset, and proves known-weight membership by inserting the realized response. Allocate up to 2 points to the conditional-law argument and 1 point to membership.
- **3 points:** Proves the three calibration implications under their respective finite-law assumptions, with correct inequalities and conditioning objects. Allocate 1 point each to probabilistic calibration, isotonic calibration, and auto-calibration. For isotonic calibration, the argument must justify passage from conditional finite-law lattice calibration to unconditional lattice calibration, for example by deriving and averaging the least-squares variational inequalities. An ordinary tower-property assertion for sigma-lattice conditioning is insufficient.
- **2 points:** Proves robust event inclusion on the true-vector coverage event, respecting positive-total-mass normalization. Either compare the full envelopes using the stated candidate-response independence assumption, or use the admissible realized response and realized true vector directly. Handles empty feasible boxes and zero coordinates consistently with the definitions.
- **2 points:** Derives the finite-sample bound and the asymptotic liminf bound from their respective simultaneous box-coverage assumptions.

# Evaluator Notes

Accept any complete valid alternative proof. Naming a method without deriving the conditional weighted-law representation, calibration transfer, or event inclusion is insufficient. Gaps in those theorem-critical steps should propagate to downstream claims when unsupported.

The three calibration properties are alternative assumptions for three separate implications; do not require G to satisfy all three simultaneously. In-sample calibration must be applied under (X,Y) drawn from the same fixed finite-support law supplied to G.

Do not require a joint density: the theorem is for arbitrary joint laws, and conditional atom probabilities suffice. Do not require an independent estimator or observed-data-only box, since neither restriction is part of the task.

Do not accept isotonic calibration as if it were auto-calibration. In particular, equality of residual integrals on every event in sigma(F*) is not implied by the isotonic assumption. Likewise, complementing a sigma-lattice conditional expectation is not an ordinary conditional-expectation operation.

The direct robust-membership proof need not establish inclusion of the entire known-weight band. A solver who proves the required containment through the single realized admissible pair has completed that obligation.

The source's isotonic proof has a local error repaired in the reference proof. The source's uncertainty-proof equation labels are present and require no repair.
