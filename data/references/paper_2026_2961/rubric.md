# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Marginal bounds and norm equivalence (2 points).** Derives positive finite bounds for every marginal density and proves equivalence of the Lebesgue and density-weighted L2 norms.
2. **Triangular operator and Riesz basis (4 points).** Constructs an operator sending the subset-indexed tensor Legendre orthonormal basis to Xi, including the correctly normalized constant element. Proves boundedness, triangular block structure, coercive invertible diagonal blocks, and bounded invertibility. Merely naming Lax-Milgram or triangularity without the needed derivations is insufficient.
3. **Full hierarchical orthogonality (2 points).** Uses marginalization and positive-degree Legendre orthogonality to prove that each nonempty Xi element is orthogonal to every square-integrable function of each strict subset. Extends this property to the L2 limits defining the components. Orthogonality only between selected components is insufficient.
4. **Identification with the constrained decomposition (2 points).** Groups the unique basis coefficients by subsets, verifies L2 convergence, summation and the full constraints, and invokes the stated uniqueness assumption to identify the unique constrained least-squares solution.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Deduct for changing the density assumptions, omitting or misnormalizing the constant component, failing to prove operator invertibility, or treating the basis representation as an assumption.
