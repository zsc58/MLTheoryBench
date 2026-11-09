# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Reduction and instance construction (2 points):** Correctly reduce from clique, construct the loopless adjacency matrix, choose R=1/sqrt(k), and identify the threshold 1-1/k. The restriction 1<k<n must be compatible with the reduction; it may be justified by padding with an isolated vertex and handling trivial input cases, or by another valid argument.
2. **Universal upper bound and yes case (3 points):** Justify restriction to nonnegative vectors, derive x^T A x<=||x||_1^2-||x||_2^2<=1-R^2, and exhibit the normalized vector on a k-clique attaining equality.
3. **No-clique strict gap (3 points):** Normalize an arbitrary feasible nonnegative vector to the simplex, correctly apply the Motzkin--Straus bound with 1<=omega(G)<=k-1, and derive a uniform strict bound below 1-1/k. A valid alternative argument establishing the strict optimum inequality earns the same credit. The proof must remain valid for k=2 and edgeless graphs.
4. **Complexity conclusion (2 points):** Establish the threshold equivalence and explain why the polynomial reduction proves NP-hardness of exact optimization. The radius is encoded exactly through k; an equivalent rational squared-radius encoding is valid. No floating-point approximation to the radius is required or presumed.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or the use of Motzkin--Straus specifically. The two standard independent external results used by the reference proof, clique NP-completeness and the Motzkin--Straus simplex theorem, may be invoked without reproving them, provided their relevant hypotheses are satisfied.

A solver must derive the strict no-clique optimum inequality and cannot receive full credit merely for naming a clique reduction or a graph method. A uniform bound strictly below the threshold suffices. If a proof instead uses pointwise strict inequality, it must also justify attainment or otherwise rule out a supremum equal to the threshold. On the restricted instances the feasible set is nonempty and compact, so attainment is available. The infeasible-instance convention does not affect the reduction.

Do not demand a lengthy discussion of input encoding when the proof clearly uses the exact (G,k) representation specified by the task. Likewise, routine details about padding or compactness can be brief. Do not impose a rational-R assumption: the public task specifies R exactly as 1/sqrt(k).
