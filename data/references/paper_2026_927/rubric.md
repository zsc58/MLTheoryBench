# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Mixture expansion and residual decomposition (2 points).** Correctly expands each group mean by conditioning on the label and adds/subtracts the cross-group mixture, identifying the weighted within-label term with the target's orientation and absolute value.
2. **Within-cluster heterogeneity bound (3 points).** Partitions the label-composition term by clusters and rigorously bounds its within-cluster component by \(\max_j\varepsilon_{j,u}\). Accept either conditional-mean centering with cancellation of the group-u contribution and probability averaging, or a valid midpoint/probability-vector argument, or another correct method. A separate L1 estimate is not required for the cancellation proof. The argument must be valid under the stated null-event convention; a zero-mass cluster in group u has all relevant labelwise and clusterwise means equal to zero.
3. **Cross-cluster spread bound (3 points).** Bounds the cluster-mass component by \(\max_j\mu_{j,u}-\min_j\mu_{j,u}\), for example using zero total cluster-mass difference, midpoint centering, and an L1 bound of two, or by comparing convex combinations. The constant must be correct.
4. **Assembly (2 points).** Combines the components to obtain the exact stated inequality for arbitrary groups, retaining the absolute value outside the weighted within-label residual sum.

# Evaluator Notes

Accept a complete valid alternative proof and allocate credit by the mathematical obligations it establishes. Do not require the reference proof's incidental presentation choices. A theorem-critical missing bound in either decomposition component is a major gap; merely naming a clustering or concentration method earns no credit for that step.

The requested result is an inequality about conditional expected cardinalities. A fully correct proof need not derive a conformal coverage guarantee, use exchangeability quantitatively, or explain a comparison with group-specific calibration. A shared-threshold observation is optional and earns no separate required credit. Do not demand a Lipschitz assumption or a claim that calibration noise disappears. Such claims are not consequences required by the public task.

Respect the public zero-event convention. Do not accept a proof that substantively assumes all label/group or cluster/group cells have positive probability without addressing absent cells. A missing but immediate zero-cluster case split is a readily repairable omission, not automatically a major gap. Likewise, the proof should remain valid when ranges vanish, for singleton clusters, and when the two groups coincide; separate discussions are unnecessary if the argument already covers these cases.
