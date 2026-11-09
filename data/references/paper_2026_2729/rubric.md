# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives the label-resolved witness integral and substitutes the pointwise signed-measure decontamination rule, including the supremum characterization. Correctly types row multiplication by the correction matrix and respects integrability.
- **2 points:** Specializes the operator to PU and derives both the corrected population moment and the unbiased positive/unlabeled empirical estimator for a fixed predictor and witness independent of the estimating samples. Uses the true supplied prior and the ordinary domain of the inverse.
- **3 points:** Establishes the uniform PU deviation bound with the exact stated constants, including the eta-net approximation, empirical-process control, signed fixed-multiplier contraction to the subgroup Rademacher complexities, and the covering-number/logarithmic terms. Handles both deviation directions under the stated non-absolute Rademacher convention. Establishes uniform individual-residual control sufficient for the downstream adaptive argument, either here or separately in the final step.
- **3 points:** Proves projected-update potential decrease, bounds successful updates by K_epsilon, and uses fresh-batch conditioning plus a union bound to obtain the joint 1-delta termination, multicalibration, and sample-budget guarantees. Makes the finite-W approximation error vanish, verifies sample sufficiency with a constant depending only on C_R, and includes K_epsilon=0 and the final stopping call.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Deduct substantially for treating the decontamination identity, uniform empirical-process control, or potential decrease as unexplained named methods.

The expected Rademacher complexity has no absolute value inside its supremum. Do not accept an unqualified absolute-supremum symmetrization step that assumes a symmetric class. One-sided symmetrization with a union bound over signs is valid. Negative score multipliers are allowed and must be covered by the contraction argument.

The original source's consolidation of separate square-root terms does not justify the exact displayed constants. Do not reward that invalid numerical inference. Direct net-wise one-sided concentration proves the requested constants without changing the target.

A scalar bound on |MC_hat-MC| alone does not certify that a selected empirical witness is a true violation. The proof must provide uniform residual control, or an equivalent argument that certifies every accepted witness. A finite-W argument may use W itself as an exact net rather than introduce a positive eta approximation term.

The sufficient sample-size constant may depend on C_R, but on no other problem parameter. The concrete choice in the reference proof is optional. The termination and sample-budget claims are required on the same high-probability event; no almost-sure budget claim is required outside that event.

Unbiasedness is not asserted for the supremum estimator, for a predictor fitted on the same sample, or for a witness selected from that sample. No error guarantee for an inaccurate pre-estimated class prior is part of this task. Routine measurability and adaptedness conventions should not be mistaken for computational-efficiency assumptions.
