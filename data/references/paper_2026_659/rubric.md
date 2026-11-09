# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Uses input separability to express the pre-activation as channelwise functions plus the broadcast bias.
- **3 points:** With channelwise parameters frozen, defines the processed tensors and explicitly derives the scalar-weighted recombination with one scalar per channel.
- **3 points:** Correctly identifies that recombination with the tensor-dot definition gives the tensor-affine node form, including dimensions, nonlinearity, bias, and possible node-specific (inhomogeneous) inputs.
- **2 points:** Correctly establishes inheritance of any tensor-affine property or training result allowing inhomogeneous inputs, including scalar-only training with frozen channelwise functions.

# Evaluator Notes

Accept any complete valid alternative proof. Do not award full credit for merely naming a projection or reweighting method. Treat omission of the tensor-dot identification, inhomogeneous-input qualification, or frozen-versus-trainable distinction as theorem-critical.
