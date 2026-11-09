# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Threshold encoding and complexity accounting (3 points):** Correctly characterizes the attained minimum threshold by a universal formula with one d-dimensional quantified block. Expands all realized ternary sign-pattern regions, including boundary points, and guards the inner box without using an undefined objective outside its domain. Counts O(M_f+T_f+d) distinct atomic polynomials, rather than repeated Boolean occurrences, and verifies that both boundary and value polynomials have degree at most Delta_f. Handles degree budget 1, zero boundary count, and degenerate boxes consistently.

2. **Upper pseudo-dimension derivation (2 points):** Uses a valid quantifier-elimination and GJ/sign-computation argument to obtain the stated upper bound with absolute constants. For the source route, the relevant bounds are log I=O((d+1)log M+pd log Delta_f) and log D_QE=O(d log Delta_f), followed by a threshold bound O(p log(2D_QE Lambda)) with Lambda=O(I). The degree-dependent term in log I cannot simply be omitted. Strict comparisons and equality may be implemented by a constant number of sign tests per polynomial. The final simplification must preserve the p,d dependence and remain meaningful when Delta_f=1.

3. **Discrete lower-bound construction (3 points):** Gives an explicit family of polynomials of total degree at most Delta and at least a universal multiple of pd log Delta designated instances. In the source construction, specify K=floor(Delta/2), B=floor(log_2 K), the grid polynomial, the squared selector, interpolation polynomials that recover bits on the grid, and the base-K parameter encoding. Prove that every labeling produces grid values on opposite sides of fixed thresholds and establish separation from competing grid points. Merely naming bit extraction or interpolation is insufficient. Verify the total degree jointly in alpha and theta. The corrected source extractor coefficient is 1/2, not 5; other constants or constructions are acceptable if their separation is proved.

4. **Continuous stabilization and shattering conclusion (2 points):** Proves existence of finite attained minima for every instance and every alpha in the constructed family, not only at the encoded parameters. Supplies a complete stabilization argument: control perturbations near grid points, exclude competitors near the wrong grid points, and control the unbounded region as well as the bounded region away from the grid. A finite penalty coefficient must be chosen independently of all labels and designated instances; dependence on p,d,Delta is allowed. In the source route, C multiplies the grid penalty, and the neighborhood radius must be small enough relative to a Lipschitz bound, not merely an unexplained fixed distance. Derive separated continuous optimal values and conclude binary threshold shattering and the universal asymptotic rate. Closed stabilization intervals suffice; strict improvement over the grid minimum is not required.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental constants, threshold, instance encoding, or presentation choices.

The upper-bound boundedness assumptions do not apply to the converse, whose objectives and losses are real-valued on unbounded domains. Do not require a globally bounded polynomial construction for the converse.

The standard independent quantifier-elimination and GJ results may be invoked in suitable stated forms with verified hypotheses. A paper-specific conclusion or the name of a specialized method does not by itself close a proof obligation. The reference proof supplies the lower-bound construction and all stabilization details; no unresolved GT obligation is being treated as an established scoring step.
