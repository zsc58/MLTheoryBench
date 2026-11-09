# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly establishes the common recurrent/transient decomposition for positive policies and the relevant Cesaro and transient-resolvent properties. Uses the public visitation definitions correctly: d is zero on transient states, while delta need not be zero on recurrent states. Standard finite-chain results may be used with their hypotheses verified.
2. **3 points:** Derives the performance-difference decomposition from the average-reward and Bellman identities. Correctly uses Q=r+PV-K and obtains the recurrent visitation-weighted Q action-difference contribution. An equivalent derivation using r+PV is acceptable if its equivalence in the recurrent action-difference sum is justified.
3. **2 points:** Justifies constancy of J and K within each common recurrent class, the cancellation of recurrent K action differences, and the transient identity yielding the weight mu_T^T(I-T^pi)^-1. This must be a derivation or a justified equivalent argument, not merely an assertion that the remaining terms have the desired form.
4. **3 points:** Establishes sufficient regularity of the visitation quantities and obtains the full differential for an arbitrary differentiable positive-policy parameterization. Continuity of the weights, together with the performance-difference identity and a differentiability remainder argument, is sufficient; differentiating the weights themselves is not required. Finite stationary linear systems and the matrix-inverse formula provide one valid route, including periodic recurrent classes.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, particular auxiliary matrices, or independent reproofs of standard finite-chain facts.

The public relative value has the stated normalization. The performance-difference argument itself can use only its Bellman equation; a solver need not use normalization in every step or differentiate V or Q.

The transient contribution is essential in the general multichain case. An unexplained omission is theorem-critical, but a justified vanishing contribution in an applicable special case, including an empty transient set, is correct. The full proof must still establish the general claim.

Do not impose aperiodicity, a unichain assumption, a globally uniform positivity bound, or continuously differentiable policy parameterizations beyond the differentiability requested. Interpret parameter gradients in local coordinates, or equivalently evaluate the differential on arbitrary tangent directions. A directional argument must establish a genuine differential, either through known differentiability or a suitable remainder estimate.

All reference-proof obligations are closed. The specialized source citations are not mandatory solver dependencies and are not substitutes for verifying the relevant hypotheses.
