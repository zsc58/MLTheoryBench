# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly reduces expected excess risk to Bayes-classifier disagreement. Establishes that threshold-classifier disagreement requires posterior-estimation error to be at least the local Bayes margin, and consequently that disagreement outside the margin-at-most-t event requires estimation error greater than t. A justified strict local-margin implication is also acceptable.
- **3 points:** Establishes or validly derives the required k-nearest-neighbour posterior tail under the displayed assumptions, with a suitable integer choice of k of order nt^(d/v) and exponent nt^(2+d/v). Verifies that the choice is feasible and does not depend on the sample or query. A direct pointwise argument controlling neighbour radius, Holder bias, and conditional label fluctuations is sufficient; a stronger uniform theorem is not required.
- **3 points:** Splits disagreement at a threshold t, applies the exponential boundary-mass condition, and selects t=n^(-1/(beta+2+d/v)) to balance the two exponents.
- **2 points:** Obtains the resulting deterministic integer sequence with k_n=O(n^((beta+2)/(beta+2+d/v))), verifies the sample-size conditions needed for posterior-tail admissibility and any prefactor absorption, and derives the claimed expected excess-risk bound with constants depending only on the displayed parameters.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its use of a 2n prefactor, or use of every source assumption when a weaker set already suffices.

A specialized regression citation is not by itself a completed proof of the posterior-tail step. A cited standard independent result must have its relevant statement specified and its hypotheses and parameter scaling verified. Otherwise, the theorem-critical estimate must be derived. A bare assertion of a k-nearest-neighbour concentration result without its applicable rate and parameter scaling does not earn the posterior-tail step.

Do not require a strict estimation-error comparison with the local margin when the estimate may equal 1/2. The non-strict comparison, followed by restriction to margin greater than t, is sufficient and correct. Conversely, an unqualified strict comparison for arbitrary threshold estimates needs correction or a valid tie-exclusion justification.

The Big-O requirement describes an upper-order constraint on a suitably chosen sequence; it does not make every smaller k valid. A proof must justify its selected k, including integer rounding and 1<=k<=n for the claimed regime. A proof that does not justify the balancing choice or the resulting k exponent cannot receive full credit.

The reference proof closes the needed pointwise posterior tail directly. Its discussion of the source's stronger specialized uniform assertion must not be treated as a proof of that assertion or as an additional solver obligation.
