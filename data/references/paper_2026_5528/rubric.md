# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly constructs the activation-time auxiliary graph and source-capacitated network, with the threshold and activation-time hypotheses used accurately. In this approach, equal-time edges are omitted from the auxiliary graph, graph arcs have unit capacity, and each auxiliary source arc has capacity `kappa`.
- **4 points:** Proves the `kappa` cut lower bound in both cut cases and uses integral flow and path extraction to derive `kappa` pairwise edge-disjoint paths in the activated graph from the initial active set to each target vertex. Establishes the length bound by strict increase of integer activation times. Disjointness is required for graph edges, not the auxiliary source arcs.
- **2 points:** Constructs a unit flow by routing equal amounts along the edge-disjoint paths, verifies conservation, and computes its energy as at most `T(u)/kappa`. The construction respects electrical contraction, including distinct parallel edges.
- **2 points:** Applies the effective-resistance variational principle and concludes both `R_eff^H(S_0,u) <= T(u)/kappa` and `<= ell/kappa` for every required vertex.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The point allocation describes mathematical progress, not a mandatory method; a complete valid alternative receives full credit.

The path certificate and the resistance conclusion are inseparable parts of the target; theorem-critical omissions in either are major gaps. An unrestricted edge-connectivity argument alone does not establish the required path-length bound.

The public process permits multiple vertices to activate at the same time. Every newly activated vertex must have its required support in the preceding active set, not among vertices first activated simultaneously. An argument that assumes all activation times are distinct does not cover the full task. Even a sequential process can have edges between initially active vertices, all of which have activation time zero. In an activation-time proof, equal-time edges must be omitted or otherwise handled without asserting an unsupported strict-time increase.

Auxiliary source arcs of capacity `kappa` may be shared in a flow decomposition. Unit capacities guarantee disjointness only for the graph portions of the extracted paths. The target does not require vertex-disjoint paths or distinct endpoints in `S_0`.

Electrical contraction retains distinct parallel resistors; it does not replace them by one unit resistor. Shared internal vertices of edge-disjoint paths do not prevent the sum of their path flows from conserving current. The activation-time paths meet `S_0` only at their initial endpoint; an alternative path construction can instead trim each path at its first encounter with `S_0` when viewed from the target.

No randomness, uniform selection, or connectedness assumption is required. Empty target sets are vacuous, and `kappa=1`, repeated active sets, early stopping, and simultaneous activations are covered by the same argument. Do not require separate discussion of these cases when the submitted proof already handles them.
