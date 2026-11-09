# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly identifies the conditional mean and zero-mean noise and obtains parameter-uniform conditional second-moment bounds from the random-envelope fourth moments. Constants may depend on gamma.
- **3 points:** Derives the gradients and their pairing with the mean direction; controls the beta and theta terms using (A4), Cauchy-Schwarz, and Young's inequality; and chooses a threshold and positive descent coefficients valid for every gamma above it.
- **3 points:** Establishes global Lipschitzness of the Lyapunov gradient from the stated random-envelope and Hessian assumptions, then obtains the conditional one-step recursion with the correct noise term.
- **2 points:** Telescopes at tau_k=alpha/sqrt(N), uses W>=G^min, and converts the average to the independent uniform iterate bound.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the particular numerical constants in the reference proof. Do not award the descent or smoothness steps merely for citing a paper-specific lemma without deriving or verifying its needed bounds. Propagate a missing moment, descent, or one-step dependency when the final rate is thereby unsupported.
