# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Restricted tangent-space estimate (4 points).** Establishes the high-probability uniform entrywise l1 support estimate, with all three coefficient terms and the stated failure-probability order. For the reference route this includes explicit Bernstein increment metrics, incoherence-based diameter bounds, the Gaussian-width contribution of order sqrt(p log(mn)), a valid entropy calculation, and a correctly anchored mixed-tail application. The entropy argument must use the row-sum bounds actually available for the decomposition factors, retain or otherwise validly control support-selection entropy, handle cover centers consistently, and justify absorption of the Z-cover contribution. An induced 2-to-1 norm cannot simply be equated with a sum of row norms. Merely naming generic chaining earns at most 1 point in this category.
2. **Clarke criticality (2 points).** Correctly establishes criticality of every true factorization on the same support event. The reference proof constructs a certificate by compact convex separation, checks its strict off-support bound and its annihilation of U and V, and verifies the Clarke subdifferential formula. A valid alternative, including generalized Fermat after independently proving the required local minimality, is acceptable; a certificate is not an additional public target.
3. **Sharp local-growth geometry (3 points).** Establishes local projection onto the exact-rank factorization manifold, normality of the displacement, the tangent-linear and quadratic product decomposition, and a lower bound sufficient for the exact epsilon/8 coefficient. In the reference route, the correct normality identity is (X^sharp)^T H=K^T Y^sharp. It makes the cross term nonnegative and gives ||Delta_1||_1 >= sigma_sharp d. The certificate estimate must distinguish its on-support and off-support bounds. The supported-residual step is a subgradient inequality, not an unconditional equality. Continuity gives sigma_sharp >= sigma_*/2, and ||HK^T||_1 <= sqrt(mn)d^2/2 is absorbed with an explicit sufficiently small radius. Unspecified positive constants do not by themselves establish the requested numerical constant.
4. **Conclusion and quantifiers (1 point).** Preserves the source sampling model, parameter regime, separate universal bound and probability constants, a common positive margin, one support event uniform over all W and all true factorizations, and a radius allowed to depend on the fixed factorization. Handles W=0, points on the factorization set, and empty support without imposing S!=0.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or demand a dual certificate when another argument proves the public conclusions. Do not award credit twice for the same argument merely because it contributes to both growth and criticality.

Treat omission of the central restricted empirical-process argument, or replacement of it by an unproved paper-specific lemma, as a theorem-critical gap. A proof that establishes the restricted bound and criticality but not the required local-growth inequality cannot exceed 6 points. A proof of local growth that assumes the restricted bound without deriving it cannot exceed 6 points.

Standard independent probability and differential-geometric results may be cited in correct applicable forms; their relevant hypotheses must be checked. A named specialized method alone does not close the covering, entropy, anchoring, or singular-value obligations. The reference proof contains complete derivations of these obligations and has no outstanding GT warning.
