# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **5 points:** Factors both kernels through the common separating base, uses feature equality to equate the encoded probability measures, and establishes a globally injective measurable transition with both \(Q'=E_\tau Q\) and \(K=K'E_\tau\) \(\mu\)-almost everywhere. A proof using matching encoder images must first identify conull Borel domains and then justify a global injective extension. The reference proof accomplishes this using mutual absolute continuity and countable null-set saturation. An equally valid alternative construction is acceptable.
- **2 points:** Establishes the reverse Blackwell comparison and hence Blackwell equivalence. When equivalence properties of \(\sim_G\) are used, justifies inverse and composition comparisons with correct transport of null sets and correct composition order.
- **3 points:** Shows that the constructed transition belongs to both valid-transition sets, using the almost-everywhere kernel-transition definition, applies containment in \(G\), and concludes identifiability for every pair in the model class under that containment assumption.

# Evaluator Notes

Accept any complete valid alternative proof; do not require the reference proof's incidental presentation choices or its particular exceptional-set construction.

Equality of encoded laws identifies their images only up to null sets. Continuity and full topological support do not establish equality of the actual images, nor do they make an arbitrary conull matching domain equal to the entire latent space. An unsupported appeal to either assertion leaves the central transition argument unproved.

An injective map defined only on a conull subset is not yet an element of the stated transition sets. The proof must justify a globally defined measurable injective representative, or provide another argument that fully establishes the group comparison required by the task.

The source and task use almost-everywhere kernel equality. Do not demand pointwise equality on exceptional null sets, and do not award the transition-membership step merely from membership in a different, pointwise-defined transition set.

The common measure class may be an arbitrary subclass of the distributions equivalent to the base measure. No closure under every measure-equivalent perturbation is assumed. Empty model classes make the conclusions vacuous; no nonemptiness assumption on the model class is required.

Do not require a proof of the stronger standalone full-support-only injective assertion from the source. The public task includes the additional common-measure-class contract, and the corrected reference proof closes the required claim under exactly that contract.
