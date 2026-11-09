# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Expands the network into its \(d+1\) homogeneous monomials and, after arbitrary coordinate substitution, expresses the output matrix as a sum of at most \(d+1\) rank-one outer products. Correctly concludes \(\operatorname{rank}(M)\le d+1\), independently of width.
- **3 points:** Establishes \(AA^*=qI\) for \(A_{ab}=\zeta^{ab}\), hence its full rank and flat singular spectrum, and correctly derives both non-representability when \(d<q-1\) and the normalized best rank-\((d+1)\) residual \(1-(d+1)/q\).
- **2 points:** Proves that width \(m\ge d+1\) permits realization of any homogeneous coefficient vector, with a valid invertible Vandermonde construction or an equally complete alternative. Merely asserting universal approximation or coefficient freedom earns no credit for this step.
- **2 points:** Uses the inverse of \(d-1\) modulo \(q\) to construct coordinate maps realizing any relevant factorization \(g(a)h(b)\), and explicitly verifies that all linear phases and the three listed nonlinear phases have such factorizations.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The roots-of-unity orthogonality calculation and the best low-rank approximation theorem are standard background, but their hypotheses and numerical consequences must be applied correctly. A failure to prove coefficient surjectivity does not invalidate an independently correct rank obstruction, while representability points require an actual valid construction or equivalent existence proof.
