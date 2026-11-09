# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **4 points:** Rigorously establishes the three auxiliary-relative homology comparisons for \((X^a_\alpha,I_\alpha)\), \((U_\alpha,I_\alpha)\), and \((U_\alpha,X^a_\alpha)\), with reduced degree-zero homology on the auxiliary side. A valid general proof for \(T(A,B)\) when \(B\leq A\), followed by the three substitutions, is sufficient. Accept a correct mapping-cone proof, a simplicial-retraction and relative-chain proof, or another complete argument. The triangular mask and the additional vertex must be respected. Merely asserting that a mapping-cone method applies without establishing the correspondence earns at most 1 of these points.
- **4 points:** Forms the correct short exact sequence of relative chain complexes for \(I_\alpha\subseteq X^a_\alpha\subseteq U_\alpha\), uses its long exact homology sequence, and derives the pointwise identity with both \(\ker\gamma_i^a\) and \(\ker\gamma_{i-1}^a\). The maps, dimensions, and indices must be correct, including the zero group in degree minus one.
- **2 points:** Uses the finite-bar/reduced degree-zero convention correctly, justifies finite integrals and the absence of essential positive-dimensional bars, applies the argument to both indexed orientations, and averages consistently with the divergence definitions. A sufficient finiteness argument observes that above the largest matrix entry the three base complexes coincide and uses the already-proved auxiliary-relative comparisons. Merely observing eventual connectedness does not establish the positive-dimensional assertion.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its particular vertex-removal order if another valid construction is supplied, or explicit chain-map formulas when a rigorous topological or relative-chain argument supplies the same comparison.

The upper complex in this task is \(U_\alpha=R_\alpha(A_\wedge)\). In general it is not the ordinary simplicial union \(R_\alpha(w)\cup R_\alpha(\widetilde w)\). A proof replacing it by that ordinary union changes the task and does not establish the stated result.

A proof using ordinary unreduced auxiliary \(H_0\) without removing its essential component is not valid for the stated finite-bar quantities. Ordinary relative homology of the same-vertex pairs is valid. An argument over a field of characteristic two alone does not prove the claim for the arbitrary field in the task unless the restriction is removed; correctly signed chain arguments and coefficient-independent topological arguments are both acceptable.

A proof establishing only one directional identity without obtaining the stated averaged identity is incomplete. The two orientations are counted with multiplicity even when the matrices coincide. No distinctness, strict positivity, generic filtration values, or positive divergence assumption may be imposed. Empty inputs give singleton auxiliary complexes and zero relative groups; zero distances and tied scales require no change to the identity.
