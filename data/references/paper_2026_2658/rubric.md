# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Establishes that each recipient-specific remote surrogate is a measurable function of its designated off-diagonal block, independent of the recipient's complete diagonal PU block. Also establishes independence of the local p-value vectors from their dependence on disjoint columns of the independent block array. Independence of agents or remote independence from evaluation data alone is not sufficient for the latter conclusion.
- **3 points:** Derives joint permutation invariance of the calibration and true-null test scores with the alternative scores and received models, using invariance of the local PU input and learned function and the pointwise maximum. Correctly obtains the requested conditional exchangeability. Does not condition on arbitrary ordered calibration/test data or claim unrestricted exchangeability at the fixed labeled training positions.
- **2 points:** Establishes null p-value validity and local PRDS, and proves that the independent local PRDS vectors concatenate to a globally PRDS vector. A complete direct local proof can condition on the sorted focal-null/calibration scores and remaining test scores, show that the focal rank is uniform and independent of this side information, and show that the complete p-value vector is coordinatewise nondecreasing in that rank. The increasing-cross-section argument closes global PRDS.
- **2 points:** States and correctly applies the standard BH-under-PRDS result with both null validity and global PRDS verified. Uses the exact pooled BH/FastLSU rejection-set equivalence to obtain the stated global FDR bound with the (R vee 1) denominator. Handles an empty global testing family, and does not divide by M when M=0.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of measurable remote independence, the recipient-specific disjoint-input justification, local PRDS closure, or the final validity-and-PRDS-to-FDR implication as theorem-critical.

A bare invocation of a named conformal method or the specialized inherited theorem does not itself constitute a completed local PRDS proof. An alternative invocation is acceptable only if its relevant statement is given and its required implication is derived, or justified through an independently established standard result with hypotheses checked. The reference proof supplies an elementary rank derivation, so no specialized citation is necessary.

Do not require the fixed labeled training scores to be exchangeable. PRDS concerns the entire local p-value vector, including alternative coordinates, but only true-null coordinates index the conditional monotonicity requirement. Global hypothesis indices are tagged by recipient.

For ell_j=0, all local p-values equal 1. Empty local true-null sets make the corresponding PRDS requirement vacuous. Empty local testing vectors are harmless; if M=0 the rejection set is empty and global FDR is zero. Minor omissions of immediately resolved boundary conventions may receive 8-9 when the substantive proof is otherwise complete.
