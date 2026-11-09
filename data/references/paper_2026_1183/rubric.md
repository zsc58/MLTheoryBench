# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly defines the max/min network, softmax cross-entropy, maximum-over-samples objective, trainable sparse first-layer coordinates, and the stated meaning of a valid nonsmooth subgradient.
- **2 points:** Selects a worst-loss sample and one active output maximizer per class, computes the softmax cross-entropy derivative, and establishes the at-most-C support for the output layer.
- **4 points:** Applies the active-branch nonsmooth chain rule through the selected max and min operations using one consistent active minimizer for each shared hidden unit, derives the hidden-layer and first-layer components, and correctly aggregates coincident class paths.
- **2 points:** Uses the row-wise sparse mask to obtain the first-layer count, justifies that the selected limiting/active-branch derivative is a valid subgradient of the full objective, and concludes the at-most-C bound for all three layers.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A proof that selects independent minimizers for repeated uses of the same hidden node must justify why the resulting vector is a valid generalized subgradient; otherwise require a common active branch or an equivalent limiting-gradient argument.
