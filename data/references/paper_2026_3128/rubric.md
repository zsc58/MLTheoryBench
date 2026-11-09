# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **(2 points)** Correctly uses the two exact estimators and their feasible sets: the normalized covariance decomposition and off-diagonal penalties, casewise retention, cellwise masks, the pattern-dependent Gaussian likelihood including \(|J|\log(2\pi)\), fixed per-flagged-cell penalties, and the positive-eigenvalue constraints. Correctly uses the integer contamination-count domains, the two contamination neighborhoods, and the quantifiers in the breakdown definitions. Mere repetition of the problem's setup is not required.
2. **(2 points)** For every contamination vector below \(\beta_0\), constructs clean feasible benchmarks whose objective values are uniformly bounded independently of replacement magnitudes. Uses the eigenvalue floor to bound the implosion infimum strictly away from zero and hence obtains implosion breakdown equal to one under the stated convention.
3. **(2 points)** Rules out covariance explosion in both regimes using the benchmark and uniform finite lower bounds for the other objective contributions. A valid cellwise route uses a retained pattern containing a coordinate with a diverging diagonal covariance entry and principal-submatrix eigenvalue bounds. Equivalent valid arguments are accepted.
4. **(2 points)** Rules out location explosion in both regimes by using a retained clean row in the casewise setting and clean-retained intersections in every coordinate in the cellwise setting, together with uniform covariance bounds. Any casewise norm lower bound must use its positive-part form, or be explicitly restricted to the eventual diverging-mean regime. A coordinatewise cellwise argument must avoid double counting and account for the possibility that the selected clean indices vary. Relates bounded means to the fixed-baseline displacement in the definition.
5. **(2 points)** Establishes sharpness at \(\beta_0\) with permitted finite replacements. A valid casewise route derives the weighted-mean equation. For the cellwise route in the reference proof, derives the full embedded partial-likelihood mean score and multiplies it by the fitted covariance to obtain the completion identity for varying observed patterns, including empty patterns. An independently justified equivalent identity or alternative proof is accepted. Shows that retention of a diverging replacement value contradicts simultaneous uniform boundedness of location and scatter, and explicitly concludes that at least one of the two breakdown suprema is infinite. Full-sequence divergence of one fixed mode is not required.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or a particular named matrix theorem when the needed inequality is proved directly. Award downstream steps when independently justified even if an earlier auxiliary argument is flawed; theorem-critical unsupported claims remain major gaps.

The completion identity is not justified merely by referring to an EM update or calling it equivalent to the score equation. The bridge must be derived, or supplied by an explicitly stated applicable result with its hypotheses verified. The reference proof now closes this obligation by direct matrix algebra.

Exact minimizers exist for all finite inputs by the attainment argument in the reference proof. Solvers may use the problem's exact-estimator definition without reproducing that ancillary existence argument; an incorrect assertion that the normalized penalty is everywhere continuous is not needed for the breakdown proof and should be assessed according to its actual role.

Retain the previously applied positive-part correction in the casewise location argument. Do not require an unsupported sequence-level dichotomy in the cellwise sharpness argument; the supremum-based breakdown disjunction is the intended conclusion.
