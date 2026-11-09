# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes that the mixture-plus-OU map preserves finite second moments and proves the mixture coupling bound and OU contraction, obtaining the strict W₂ contraction factor κ=√(1−α)e^(−t₀/2).
- **3 points:** Establishes existence and uniqueness of the fixed point and derives its representation α∑_{k≥0}(1−α)^kU_{(k+1)t₀}(p_data). A Banach argument must use a complete ambient space. A linear Neumann argument must identify an appropriate linear space and justify convergence, or be replaced by an explicit finite expansion with a vanishing remainder. The infinite mixture must be shown to have finite second moment. Any claim of W₂ convergence of finite approximants must use probability measures, not uncompleted subprobability partial sums.
- **2 points:** Derives the geometric iterate bound W₂(p̂ᴺ,p_∞*)≤κᴺW₂(p_data,p_∞*) for the specified initialization.
- **3 points:** Identifies the OU action on density ratios, establishes the limiting density's L²(γ) membership, uses the orthonormal Hermite expansion and OU eigenvalues with a justified limiting or coefficient argument, and obtains m_n=αλ_n/[1−(1−α)λ_n], λ_n=e^(−|n|t₀/2). Proves the monotone higher-degree attenuation claim, including the degree-zero endpoint.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

In particular, direct construction and verification of the infinite-mixture fixed point, followed by contraction for uniqueness and convergence, is acceptable in place of Banach and operator inversion. A correct argument using continuous Hermite coefficient functionals is acceptable in place of interchanging two infinite series.

Standard completeness of the full Wasserstein space, the fixed-point theorem, and the classical Hermite basis/eigenvalue facts may be cited with their relevant hypotheses satisfied. Do not accept the nonlinear W₂ contraction factor alone as verification of the hypotheses of the linear Neumann theorem. The absolutely continuous subclass of P₂ should not be assumed complete.

The public task uses an orthonormal Hermite basis. A solver choosing an unnormalized orthogonal family must include the appropriate squared-norm divisors in function reconstruction; the coefficient multiplier identity itself does not require such a divisor. The spectral expansion is an L² identity, not an additional demand for pointwise convergence.

There is no requirement to prove a reverse-SDE theorem or to analyze an approximately initialized learned sampler. The ideal recursion is explicitly given. No claim of a strictly positive distance from p_data is requested, and p_data=γ is allowed.

All reference-proof obligations are closed; there is no outstanding private GT quality warning.
