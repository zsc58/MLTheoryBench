# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes forward invariance of every hidden-state cube and the uniform gate/candidate bounds using the stated activation properties.
- **4 points:** Derives the coupled incremental inequalities, obtains the stated `alpha_l` (and an appropriate input coefficient), uses the strict condition `alpha_l<1`, and unrolls the recursion to valid `KL` and `K_infinity` estimates for each layer.
- **3 points:** Correctly composes the layer estimates into a nonnegative lower-triangular comparison matrix, identifies its diagonal contractions, proves Schur stability, and obtains decay and bounded accumulated input gain for the stack.
- **1 point:** States the resulting delta-ISS estimates with the required quantifiers, invariant domains, and input-difference supremum for both individual layers and the stacked network.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of the coupled gate/candidate term or of the network comparison argument as a theorem-critical gap.
