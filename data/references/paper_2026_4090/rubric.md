# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **4 points:** Proves the tree-level squared-Euclidean isometry by relating separating-node indicators in the embedding to the edge-weight sum and then to the node path distance, including the zero-leaf telescoping argument.
- **2 points:** Correctly passes from individual trees to the concatenated forest and applies global normalization to obtain `||psi(x)-psi(x')||^2 = rho(x,x')`.
- **2 points:** Derives the deterministic linear-score Lipschitz inequality in the induced metric via cancellation of the intercept and Cauchy-Schwarz.
- **2 points:** Uses a positive signed margin and the strict metric-radius condition to prove sign preservation, handling the constant-score case appropriately.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Award no credit for merely naming an embedding or invoking robustness without deriving the separating-edge identity and its consequences.
