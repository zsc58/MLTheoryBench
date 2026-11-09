# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes compactness and continuity from the specified activation and affine dictionaries, and proves the signed-measure integral representation and total-variation formula. Handles both inclusions, compactified endpoint atoms, and removal of scale for homogeneous activations. A direct compact-hull argument is acceptable.
- **3 points:** Proves existence for the penalized fitting problem through measure optimization, a finite comparison objective, bounded total variation, weak-* compactness, continuous evaluation integrands, and lower semicontinuity. Justifies equivalence of the measure and function optimization problems.
- **3 points:** Obtains an at-most-N outer atomic expansion and recursively proves hidden widths K_l<=N^{L-l} for l=1,...,L-1. An extreme-point proof must handle potentially nonatomic measures and show that the prediction-preserving perturbations also preserve minimal total variation. The recursive argument must keep every replacement in the appropriate unit ball, preserve sample predictions, justify continued optimality, stop at the affine dictionary, and explain the width count.
- **2 points:** Handles the feasible nonlinear interpolation problem and obtains a finite minimum-norm representation with the same width bounds, including the zero solution and allowed endpoint atoms.

# Evaluator Notes

Accept any complete valid alternative proof, including finite-dimensional convex geometry instead of measure extreme points. Accept equivalent width indexing that clearly permits up to N atoms in the single hidden level when L=2.

Compactness of the recursive dictionaries is not a public assumption and must be derived or justified by an applicable standard result. Weak-* continuity of the finitely many evaluation integrands suffices for fitting existence; uniform convergence of integral images need not be proved for that step.

A perturbation that preserves only predictions does not by itself establish an extremality contradiction: both perturbed measures must remain in the minimal-total-variation fiber. Adding a total-variation constraint as an independent linear equation and obtaining only N+1 atoms does not prove the requested N bound unless a further valid reduction is supplied.

Recursive replacement need not preserve the represented function away from the sample. It must preserve sample predictions and not increase the relevant norm. The inner norm at recursive depth r is V_r, not the final V_L norm.

The public interpolation claim assumes feasibility. Do not require proof that every consistent dataset is feasible, a universal-approximation theorem, or activation-equivalence and depth-containment results. A proof that also treats feasible interpolation with the linear activation is valid.

Do not award a completed core step for merely citing the paper's selected conclusions or a specialized representer theorem without supplying its relevant hypotheses and sufficient derivation. Standard Riesz-Markov-Kakutani, Banach-Alaoglu, and Krein-Milman results may be used with their hypotheses verified.
