# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly differentiates the causal log-sum-exp energy and derives the causal softmax-weighted interaction gradient.
- **3 points:** Applies the factorization $A_k=(W_k^Q)^{\mathsf T}W_k^K$ and rewrites both logits and interaction vectors in query/key coordinates.
- **3 points:** Evaluates the unit descent step at $x_i=h_i$ and derives the complete causal residual multi-head update.
- **1 point:** Correctly compares with the defined MHA update, identifying $W_k^V=W_k^K$, $W_k^O=W_k^{Q\mathsf T}$, unit step size, and $\tau=\sqrt{D_r}$.

# Evaluator Notes

Accept any complete valid alternative proof. Do not award credit for merely naming an energy or attention mechanism.
