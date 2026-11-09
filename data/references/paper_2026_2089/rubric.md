# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Regional decomposition (2 points):** Defines the regional value components under the specified conditional/interventional convention and proves that the Local Shapley value is the sum of their weighted marginal contributions. Uses legitimate finite expectations and finite linearity.
2. **Independence-based formula (4 points):** Derives an explicit regional-value formula containing the appropriate membership indicators, coordinate-region probabilities, affine coefficients, intercepts, and truncated first moments. Accept the product-sum formula or an equivalent factored formula. Substitution into the weighted regional marginal sum is sufficient; a separately factorized marginal identity is not an additional requirement of the public task.
3. **Cross-region mechanism (2 points):** Correctly explains why a feature outside the active set and outside the region-boundary set can still receive attribution through other regions. In particular, outside G means that the feature does not determine region membership; it does not mean that its affine coefficient vanishes in every region. The explanation may be integrated into the witness.
4. **Nonzero witness (2 points):** Supplies and verifies a concrete example satisfying all setup conditions, including genuinely disjoint closed interval factors, positive coordinate-region probabilities, independence, and finite first moments. Verifies both set exclusions and computes a nonzero total attribution, rather than only a nonzero individual regional term.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A proof may use equivalent notation or an algebraically equivalent regional formula. The conclusion must retain both the local-inactivity and outside-G conditions and the possibility of nonzero attribution.

The existential conclusion concerns some admissible configuration; it does not claim nonzero attribution for every feature, point, distribution, or dimension. The decomposition and regional-value formula must hold throughout the stated setup, including empty and full coalitions and arbitrary regional intercepts.

The problem fixes the product-law conditional version, including at null conditioning events. Do not require conditioning events to have positive point probability. The coordinate-region probabilities, in contrast, are assumed positive.

The domain need not be all of R^p or connected. A witness may use a disconnected domain to satisfy the literal closed-rectangle requirements. A witness using half-open interval factors does not exactly satisfy the task; a transparently local conversion to a valid closed-rectangle witness may qualify as a readily repairable error, but should not be described as already satisfying every assumption.

If a solver derives a factorized regional marginal, its second probability product must exclude the added coordinate l. Retaining an extra q_{l,k} there is incorrect. The source appendix contains this locally repaired error; do not reward copying it. Likewise, an affine proof cannot silently drop all regional intercepts, although a witness may choose them to be zero.

The reference proof closes all required obligations by elementary finite linearity, product integration under independence, direct algebra, and an explicit witness. No external paper-specific theorem or specialized method is required.
