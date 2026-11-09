# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly handles the absolutely continuous and singular contributions and establishes f_alpha(q(E)/p(E))<=Dbar_alpha^E(q||p), together with its swapped version, or supplies an equally strong valid replacement. The singular term cannot be discarded without justification.
- **2 points:** Establishes the scalar control needed for both directions: sublevels strictly below one exclude zero and are bounded above, while every finite sublevel is bounded above. A valid quantitative relative-error estimate may supply the upper bound, but the strict condition below one must still be used correctly to obtain a positive lower ratio bound.
- **3 points:** Under the strict q||p limsup condition, proves two-sided small-ball mass comparability and transfers equality of power indices, together with existence and equality of the logarithmic index when it exists for p.
- **3 points:** Under finite p||q limsup, proves the one-sided comparison m_q>=c m_p and derives the stated power inequality and the logarithmic inequality under equal power indices and existence of both logarithmic indices.

# Evaluator Notes

Accept any complete valid alternative proof and redistribute method-specific credit accordingly. In particular, the quantitative relative-error estimate is not a public target and is not required for full credit. A direct scalar sublevel-set argument is sufficient.

Treat omission of the asymmetry between the two divergence orders or of the logarithmic qualifications as theorem-critical. Both normalizations must use the mass of the second argument. Comparison constants must be independent of the shrinking radius.

The power indices may equal zero or infinity. Logarithmic indices are defined only at finite positive power index; do not impose an additional finite-log-index assumption. Respect the public empty-set conventions. For the one-sided logarithmic conclusion, U_log(q) subset U_log(p) directly gives the required ordering of infima. A lower-gauge argument is also acceptable if its handling of empty sets is justified; generic supremum monotonicity on arbitrary real subsets is not justified by the convention sup(empty set)=0 alone.

The reference proof includes a derivation of the optional quantitative scalar bound. Do not require its incidental presentation choices or award mandatory points for an unrequested intermediate result.
