# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derives the global estimate \(d_1(\Phi(\eta),\Phi(\xi))\le5T\,d_N(\eta,\xi)\), including valid control of both rank-matched nodal-value mismatch and time-grid mismatch, or an equivalent argument. Handles unequal event counts and the eventless case. If using regridding, distinguishes rank-matched values from evaluations on the other grid and does not require the alignment map to be surjective.
- **2 points:** Proves injectivity by reconstructing the event times from \(f_x(t)=t-x(t)\), or by another valid method, including termination and the eventless case, and establishes the inverse identities.
- **4 points:** Proves the separated-class inverse modulus \(d_N\le\kappa(\delta,T)d_1^{1/2}\). The reference route derives the active-interval slope bounds, an \(L^1\)-to-sup square-root estimate, recursive same-count event-time control with valid domains, treatment of both small and large perturbations, and compact separation of different count classes. Empty and eventless-only sieves must be handled without evaluating singular auxiliary constants. The final constant must be finite and depend only on \(\delta,T\), not on the selected paths or their counts.
- **2 points:** Establishes well-defined measurable expected signature features and proves that distinct admissible laws differ at some finite signature degree, with a valid justification for transferring equality of feature or path laws back to counting-path laws. Also proves the fixed-degree pseudometric assertion, including zero on the diagonal. The reference proof derives the needed restricted determinacy statement from time-letter signature coordinates, shuffle products, bounded mixed-moment determinacy, and measurable recovery; an equally complete alternative is acceptable.

# Evaluator Notes

Accept any complete valid alternative proof under exactly the stated assumptions. Do not require the reference constants, ordering, or particular reconstruction method. An alternative argument may bypass a reference intermediate step if it closes the same obligation.

The public task does not assume expected-signature determinacy or signature injectivity. A bare citation to a specialized determinacy or uniqueness theorem is not, by itself, a closed derivation of the signature-separation step. A solution must supply the needed restricted argument or a fully justified alternative. General statements about signatures of arbitrary bounded-variation paths must not ignore starting-point, parametrization, or tree-like ambiguities.

The reference proof's bounded-variation estimates show that signature integrability and infinite radius hold automatically for this embedding; this observation is acceptable but is not an additional public assumption. The finite-first-\(d_N\)-moment law domain must not be silently replaced by finite expected event count, which is a stronger condition.

Theorem-critical gaps in unequal-count grid alignment, inversion, inverse-recursion domains, separated-count handling, measurable law recovery, or signature determinacy are major. Do not insist on deriving a reference-specific estimate when a valid alternative avoids it.
