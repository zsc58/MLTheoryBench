# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Distance laws and scale identification (2 points):** Derives the current- and competing-centroid squared-distance distributions as scaled chi-square variables for each fixed index partition, with the correct variance scales and allowance for dependence. The current noise variance is (1-1/c_j)sigma^2, and the competing noise variance is (1+1/c_barj)sigma^2.
2. **Uniform scale and tail bound (3 points):** Establishes purity/size envelope bounds, verifies the high-noise condition, and applies a valid scaled-chi-square difference inequality to obtain the uniform per-sample bound rho_q^(d/4). A Chernoff derivation must use the scaled MGF with its valid domain and must not assume independence between the two distance variables. Merely naming concentration or a chi-square tail without the scale comparison earns little credit.
3. **Uniformization over balanced partitions (2 points):** Correctly handles monotonicity over the admissible cluster-size range, proves positive ordered scales from beta>1, and identifies the resulting factor with the specified rho_q in (0,1). Direct monotonicity of the two envelope scales and of the tail factor is sufficient; optimizing the pointwise threshold separately is not required. Evaluating both envelope functions at their common upper endpoint is a bound, not a claim that both endpoint sizes or extremal purities are simultaneously attainable.
4. **Probability conclusion by union bounds (3 points):** Performs the union bound over all samples for a fixed partition and over at most 2^n bipartitions, concluding probability at least 1-2^n n rho_q^(d/4) that every approximately balanced partition is a Lloyd fixed point. The probability experiment remains the same throughout, and no independence among the union-bound events is needed.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A proof that obtains the fixed-partition or per-sample estimate but omits the simultaneous union bound cannot receive full credit. Treat an unverified or reversed high-noise inequality, incorrect scale ordering, incorrect MGF scaling or domain, or unsupported fixed-point conclusion as a theorem-critical gap.

The public imbalance inequalities are strict, as in the source definition. A proof that also establishes the same estimate at the endpoints is valid, but the solver is not required to prove that extension. The approximately balanced family can be empty, in which case the target is immediate. Do not impose n>=6, an upper bound on q, balanced true classes, or a dimension condition making the probability lower bound positive.

The Gaussian distance laws are pointwise statements for fixed index partitions. Union-bounding over that deterministic finite family establishes the simultaneous event even for subsequently selected data-dependent partitions; it does not justify applying the distance laws conditional on a data-dependent selection event.

The supplied task states tie-nullness. A solver may use that statement without reproving it; a direct argument that includes ties in the bounded event is also acceptable. The reference proof verifies tie-nullness privately. No convergence theorem or Hartigan analysis is required.

No singleton current cluster occurs in the public approximately balanced family. If a solver invokes the more general single-sample support result, its singleton case is immediate because the current squared distance is zero; the positive-second-scale chi-square lemma must not be applied to that case.

The reference proof contains explicit derivations of all theorem-critical obligations. No specialized cited method or unresolved GT step is a scoring requirement.
