# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points: Parity-density argument.** Defines an appropriate even-certificate dimension, proves it is at most DS dimension, and proves that it upper-bounds one-inclusion density. Full credit requires the low-coordinate spanning argument or another complete argument. The density must use finite nonempty subclasses and the correct deletion-fiber normalization. Its supremum allows tuples with repeated inputs, so a proof restricted to distinct inputs must explicitly justify the reduction or supply the repeated-coordinate argument. Merely asserting a dimension comparison earns little credit.
- **4 points: Rollout-stability argument.** Starting from an even certificate for complete traces, uses prefix-freeness and a valid product-prefix peeling argument to produce a nonzero even certificate for local next-action values at distinct aligned states. Naming a peeling or parity method without establishing nonzeroness, preservation of all line-even equations, realization of every supported action tuple by one common local hypothesis, and distinctness of the final states is insufficient. Zero extension to the full finite local table must preserve the deletion equations. Only pointwise termination is available; no global horizon may be assumed.
- **2 points: Learning-theoretic upper bound.** Correctly identifies exact-trace learning with possibly randomized, improper multiclass learning of the rollout class. Applies correctly stated standard one-inclusion and leave-one-out-to-PAC results in the public probability model, verifying permutation invariance, the uniform bound for every sample size, and the hypotheses needed for the confidence term. The resulting bound must hold in the stated parameter range without trace-length dependence. Handles empty classes, zero dimension, and infinite dimension, or gives an argument that explicitly covers them. An expected-error bound followed only by Markov's inequality does not establish the claimed logarithmic confidence dependence. The public standing convention concerning measurable risks and success events is not a conclusion to be inferred from totality or density.
- **1 point: Matching lower bound.** Uses one-action stopping and a class of exactly the prescribed DS dimension, with a valid risk-preserving reduction for arbitrary randomized and improper learners. Establishes both the dimension and confidence terms for the same chosen class, either by a complete finite construction or by a precisely stated applicable standard worst-case lower bound. Constants and the small-parameter range must be universal. The assertion that every positive-dimensional class necessarily has the displayed confidence lower bound is not an acceptable substitute for the required existential construction.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, auxiliary terminology, explicit numerical constants, or particular lower-bound family. A solution may prove the structural inequalities by another valid argument or avoid the parity framework entirely if its alternative argument establishes the full target.

The two independent learning black boxes, stated in the reference proof with their relevant hypotheses and probability convention, may be invoked without reproving their general theory. The paper-specific density and rollout-stability conclusions may not simply be assumed. Do not award the upper-bound conversion when its structural premise has not been established. If an intermediate argument is flawed but its conclusion is independently proved, score later steps according to what is actually established.

Use the nonempty pseudo-cube definition on distinct domain points and the public PAC quantifier order. The learner is selected before the unknown target and distribution; its output need not be a member of the rollout class or arise from a learned local rule.

The public model takes probability over raw i.i.d. inputs and the learner's random seed, with deterministic target labels substituted. Its displayed disagreement sets and success events are assumed measurable. It does not impose a separately prescribed measurable label space or require the full labeling map to be measurable into one. Do not demand such an additional property from a solution, and do not treat its failure alone as a counterexample to the task. Conversely, do not credit a claim that pointwise termination, a density bound, or a pointwise transductive construction proves that stronger measurability property.

All theorem-critical reference-proof obligations are closed in this probability model; there is no private ground-truth completeness warning.
