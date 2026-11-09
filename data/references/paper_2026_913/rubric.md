# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly expands the quadratic objective using symmetry and the CND inequality to establish concavity on the coupling polytope.
- **3 points:** Establishes attainment and uses a justified finite extreme-point decomposition (or an equivalent valid polytope argument) and concavity to show that a minimizing extreme coupling exists.
- **3 points:** Proves the cycle perturbation characterization of extreme couplings and derives the forest edge bound \(|\operatorname{supp}(\gamma)|\le n+m-1\).
- **2 points:** In the uniform square case, proves that extreme couplings are exactly scaled permutation matrices and concludes equality between the coupling minimum and the permutation minimum.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not award credit for merely naming concavity, extreme points, cycle elimination, or the permutation characterization without deriving the required conclusions. A gap in the cycle characterization or in the uniform-marginal argument is theorem-critical.

A finite extreme-point decomposition must be justified, for example by a terminating cycle-splitting construction or by a correctly stated applicable standard polytope theorem. A complete alternative proof need not establish auxiliary characterizations that it does not use.

The theorem allows zero marginal entries and includes \(n=1\), \(m=1\), and \(n=m=1\). Do not require strictly positive marginals. The permutation normalization is \(1/n\), not one. In a cycle perturbation \(H\in\mathbb R^{n\times m}\), the correctly typed marginal equations are \(H\mathbf 1_m=0\) and \(H^\top\mathbf 1_n=0\). A graph-following argument must justify a cycle, for example using minimum degree at least two and the first repeated vertex of a nonbacktracking walk; return specifically to the initial vertex is unnecessary.
