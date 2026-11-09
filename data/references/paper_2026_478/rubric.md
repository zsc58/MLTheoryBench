# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **5 points: Path-union marginal consistency.** Derives from the tree factorization and ancestral structure of \(A(B)\) that, whenever an internal vertex is activated, the restricted and full laws agree on the variables needed by its local cost. Also handles an activated leaf parent, including the fixed-root case. Merely asserting this consistency without justification does not earn full credit.
- **2 points: Internal-cost correction.** For every \(s\in S\), uses the event \(s\in A(B)\), marginal consistency, and division by \(\pi_s\) to recover \(\mathbb E_{Q^\theta}[C_s^\theta]\), then sums over internal vertices.
- **2 points: Leaf-cost correction.** For every \(\ell\in L\), uses parent activation, marginal consistency, and division by \(\rho_\ell\) to recover \(\mathbb E_{Q^\theta}[C_\ell]\), then sums over leaves.
- **1 point: Final assembly.** Combines the two corrected sums and identifies them exactly with the stated full-tree objective, with the expectations taken under the correct laws.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The marginal-consistency argument is theorem-critical: inclusion-probability algebra alone is insufficient because the local costs are evaluated under a restricted variational law. Do not deduct twice for later uses of a marginal identity that the solution has independently established correctly.
