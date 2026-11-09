# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **Step 1 (2 points):** Correctly models the network by the quadratic coefficient map, identifies the one-unit scaling symmetry, and justifies the one-unit effective dimension \(p+d-1\) at a nonzero atom. A local normalization or an injective tangent-space calculation is sufficient; parameter counting without accounting for possible additional dependencies is not sufficient.
- **Step 2 (3 points):** Derives the one-neuron tangent-space formula, including absorption of the parallel feature direction into coefficient variation, and justifies that it is the full atom tangent space. Proves that the raw or scaling-quotiented network differential image is the sum of the \(K\) atom tangent spaces.
- **Step 3 (3 points):** Validly applies Terracini's lemma at the assumed algebraically generic constituent configuration and generic smooth secant point. Uses smoothness, non-defectivity, and the ambient symmetric-tensor dimension to obtain \(r=\min\{K(p+d-1),p d(d+1)/2\}\).
- **Step 4 (2 points):** Computes the LLC from the centered local excess KL. Validly invokes the KL-preserving submersion onto the local identifiable manifold and the regular-model value \(\lambda=r/2\), verifying the positive prior and positive-definite identifiable curvature. A local product-coordinate, co-area, sublevel-volume, or integrability-threshold argument is acceptable. Concludes the displayed formula.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Steps 1-3 may be combined or replaced by another rigorous derivation of the same local identifiable dimension.

The stated submersion and regularity hypotheses may be used directly. A solver need not construct a particular statistical observation model or prove those hypotheses from a dataset. The task concerns local excess KL, not empirical sample-size asymptotics or an arbitrary uncentered positive KL value.

Do not assume that the individual scaling symmetries exhaust all network redundancies, especially after the ambient dimension saturates. The correct LLC depends on the dimension of the local identifiable model, with all remaining local fibre directions integrated out.

A claimed equality of differential image and tangent space must be justified by a valid local parametrisation, smoothness argument, or appropriate standard result. Mere differentiation of an arbitrary parametrisation is not universally sufficient.

Comparability with a quadratic loss justifies the real integrability threshold or sublevel-volume exponent. It should not be treated, without further argument, as equality of meromorphic zeta functions or their full pole sets.

There is no additional case exclusion for \(d=1\), \(p=1\), \(K=1\), or equality of the two dimension expressions. No unresolved private proof obligation is being scored as completed.
