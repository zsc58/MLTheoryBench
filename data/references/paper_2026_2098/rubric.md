# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly restricts the dependency matrix and interaction graph to the coordinates where the two parents differ, and identifies component masks with the connected components of the induced graph.
- **2 points:** Correctly uses the separating threshold supplied by perfectness, with all induced-graph edges above it and all distinct non-edges below it. The task already assumes the threshold, so no independent derivation of its existence is required.
- **4 points:** Proves the maximum-linkage bottleneck using a valid component-refinement argument: initially every current cluster lies within one component; while a component is split, a path supplies an above-threshold linkage between current clusters, whereas all linkages between clusters in different components are below threshold. Hence a maximizing merge preserves refinement until each component is formed. An equivalent first-cross-component-merge argument is acceptable.
- **2 points:** Uses finite progress and retention of every created node to conclude that each component occurs as a singleton or intermediate node. The reasoning must accommodate singleton components, an empty difference set, and termination without an actual threshold crossing.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Do not award the central points for merely naming hierarchical clustering, thresholding, or connectivity without deriving the merge-order argument. Propagate a missing restriction or threshold justification only to the downstream claims that depend on it.

The invariant concerns different connected components, not every nonadjacent vertex pair. Nonadjacent vertices may lie in the same component and be clustered together. A proof asserting that all current clusters must be cliques contains a substantive error in the central step.

No prescribed tie-breaking rule is needed: the argument must work for any maximizing choice. A proof that otherwise closes the argument but omits an explicit vacuous empty-set case has only a routine boundary omission. Do not require a separate paragraph for every boundary case if the argument already covers it. Do not require a below-threshold merge to exist.

Do not require statistical estimation, a population model, a normalized-information calculation, a PX fitness-preservation theorem, or any claim about optimizer performance. They are not obligations of this task.
