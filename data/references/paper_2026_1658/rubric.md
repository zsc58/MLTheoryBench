# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

## Reference-Proof Status

The previously disclosed local projected-base/Wasserstein comparison gap is closed in the replacement reference proof by a direct flat-torus derivation. The proof pulls fields back by the admissible flow, identifies the resulting tangent spaces as DF_t^(-T)G, proves operator-Lipschitz variation of their orthogonal projections, and integrates the normal derivative of the exact parallel field. It does not invoke the unaudited external comparison as a black box. No private GT quality warning remains.

## Core Steps

- **2 points:** Establishes the homogeneous one-segment projected Jacobi/fanning error of order h^2 under the stated admissibility bounds. On the flat torus the base Jacobi calculation is elementary, but that calculation and projection contractivity alone do not establish comparison with exact Wasserstein transport. The comparison requires a valid derivation or a precisely stated applicable result with verified hypotheses; merely naming the specialized external method is insufficient. A valid direct derivation may use Lagrangian pullback, variation of the pulled-back tangent projections, and the normal-derivative property of exact parallel fields. Any such argument must justify its operator bounds, differentiation, and extension to the input fields used in composition.
- **2 points:** Correctly composes the N local maps, retaining the appropriate input norm, and derives the uniform O(N^-1) terminal operator error. Does not assume an unproved uniform H1 bound on approximate intermediate fields. Covers every positive integer N. Contractivity-based telescoping with the uniform local estimate is acceptable, as is the source's geometric error recurrence with a valid treatment of all resolutions.
- **3 points:** Proves destination-measure Lipschitz stability of exact Wasserstein parallel transport from the primitive admissibility hypotheses, with a valid projection/energy argument and Gronwall. Establishes any needed H1 propagation, projection regularity, and time regularity instead of assuming them or merely naming tools. A proof using the common Eulerian gradient tangent space on positive-density torus measures is acceptable. Accounts for weighted/unweighted norm equivalence in the norm used by the update.
- **1 point:** Derives the counterfactual one-step Wasserstein recurrence using the ith control source nu_i and its velocity v_i. Combines state Lipschitzness, destination stability, and fanning error with constants uniform in the horizon and resolution. Correctly allows B to depend on S.
- **2 points:** Solves the recurrence and obtains the stated geometric accumulated trajectory bound, including the continuous q=0 interpretation and fixed-horizon convergence. Does not assert a uniform O(T/N) rate for arbitrary growing horizons.

## Evaluator Notes

Accept any complete valid alternative proof under the public assumptions. Do not require the reference proof's notation or presentation. Treat omission of the local comparison, destination-stability mechanism, or geometric accumulation as theorem-critical gaps. Assess correct conditional composition, coupling, and recurrence arguments as partial progress, but not as closure of their missing antecedents. Projection contractivity and transport isometry alone do not establish the local consistency rate. The positive-density and velocity regularity assumptions in the public task are the primitive assumptions; derived projection and parallel-field estimates must not be imposed as additional hypotheses.
